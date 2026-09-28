"""Les accès payants à « Parler librement » d'En route vers Compostelle.

Décision de Daniel, 26 sept. 2026 : la formule B de
assets/presentations/compostelle-prix.html. Le chemin (les dix journées, la
poche, le test) reste gratuit et ne passe par aucun code ; seul « Parler
librement » — le seul geste qui coûte — se paie : 19,99 $ pour 12 mois et
100 conversations, recharge de 50 conversations à 4,99 $.

**Un code de pèlerin n'est pas un code d'élève.** Il fait huit caractères et
commence par « PC » (six pour un élève, dix-sept pour un jeton de séance) :
`validate_student_code` ne le reconnaît donc pas, et toutes les autres routes
d'IA du portail le refusent d'office. Il n'ouvre qu'une chose : le scénario
`camino-es-fr` de /api/jeu-de-role. Un pèlerin qui paie 19,99 $ n'achète pas
la correction, la traduction ou la voix des 87 modules.

**Rien de la personne n'est gardé ici** (Loi 25) : ni nom, ni courriel, ni
carte. Stripe les tient, pour son reçu. Nous gardons le code, ses dates, son
compteur et les identifiants des sessions Stripe qui l'ont payé — ce qui
permet de rendre le code une seconde fois à qui revient avec le lien de retour,
et de ne jamais créditer deux fois le même paiement.

**Le code est tiré AVANT le paiement** et mis dans la description du paiement :
le reçu de Stripe le porte donc, et un pèlerin qui a fermé l'onglet trop tôt
le retrouve dans son courriel. Il n'est ACTIF qu'une fois le paiement confirmé
— par le webhook, ou par le retour du pèlerin (on demande alors à Stripe
lui-même) : deux chemins, le même geste, idempotent.

Aucune dépendance : l'API de Stripe se parle en formulaire HTTP, et la
signature du webhook est un HMAC-SHA256. Le serveur injecte son stockage
(`charger`, `sauver`, `verrou`) — ce module ne connaît ni fichier ni base.

    python3 build/controles/pelerins.py    # le contrôle, sans réseau
"""
import base64, datetime as _dt, hashlib, hmac, json, os, secrets, time, urllib.error, urllib.parse, urllib.request

SCENARIO = "camino-es-fr"
PREFIXE, LONGUEUR = "PC", 8
ALPHABET = "ABCDEFGHJKMNPQRSTUVWXYZ23456789"   # sans 0/O, 1/I/L : il se recopie à la main

# Les codes d'essai du pilote (27 sept. 2026) : Daniel fait valider l'outil
# par des amis pèlerins et des hispanophones avant de vendre. Gratuits, chacun
# ouvre « Parler librement » pour ESSAI_CONVERSATIONS conversations jusqu'à
# ESSAI_FIN inclus ; l'enregistrement se crée au premier usage. Coût plafonné :
# 12 × 25 conversations × ~8 ¢ ≈ 24 $ US au pire. Pour en couper un, le retirer
# d'ici ; pour tous, vider la liste.
ESSAI_FIN = "2026-10-18"
ESSAI_CONVERSATIONS = 25
CODES_ESSAI = {"PCF8D9GQ": "essai 01", "PCM6WNSV": "essai 02", "PCEAN6WQ": "essai 03", "PC72J5U8": "essai 04", "PC8JSFQV": "essai 05", "PCZ4VRGX": "essai 06", "PCBPQ8RW": "essai 07", "PCRWZECQ": "essai 08", "PCF8XAJQ": "essai 09", "PCZ4YFPX": "essai 10", "PCDUKPKG": "essai 11", "PCK3WC4E": "essai 12"}
# Les codes d'essai des trousses de métier (28 sept. 2026) : même formule que
# Compostelle, pour faire essayer la Maison Francœur (vêtements) et l'Hôtel
# Rive-Claire (réception) à des proches avant de les montrer à un employeur.
# Chacun n'ouvre que le jeu de rôle de SA trousse (TROUSSES) et les voix de ses
# personnages ; mêmes plafonds et même fin que les codes de Compostelle.
# Coût plafonné : 16 × 25 conversations × ~8 ¢ ≈ 32 $ US au pire, voix comprises.
TROUSSES = {
    "francoeur": ("magasin",),
    "hotel": ("comptoir-fr-en", "comptoir-fr-es", "comptoir-en-fr", "comptoir-en-es", "comptoir-es-fr", "comptoir-es-en"),
}
CODES_ESSAI_TROUSSES = {
    "PC4QSY45": ("francoeur 01", "francoeur"),
    "PCRDWBVU": ("francoeur 02", "francoeur"),
    "PCBUSXR6": ("francoeur 03", "francoeur"),
    "PCC65FF3": ("francoeur 04", "francoeur"),
    "PCWQHVXP": ("francoeur 05", "francoeur"),
    "PCAAEJUJ": ("francoeur 06", "francoeur"),
    "PCYV7JEM": ("francoeur 07", "francoeur"),
    "PCKN7EJ5": ("francoeur 08", "francoeur"),
    "PCSTQDXN": ("hotel 01", "hotel"),
    "PC2RGS5J": ("hotel 02", "hotel"),
    "PC4JHWWN": ("hotel 03", "hotel"),
    "PCG8DX7M": ("hotel 04", "hotel"),
    "PCFAEMBM": ("hotel 05", "hotel"),
    "PCKYJMPC": ("hotel 06", "hotel"),
    "PCUSZW3Q": ("hotel 07", "hotel"),
    "PCHK596K": ("hotel 08", "hotel"),
}
# Réglable pour les essais seulement (un faux Stripe local) ; jamais en production.
API = os.environ.get("STRIPE_API", "https://api.stripe.com/v1")
TOLERANCE_S = 300                              # âge maximal d'une signature de webhook


def _entier(nom, defaut):
    try:
        return int(os.environ.get(nom, defaut))
    except ValueError:
        return defaut


def offre():
    """Les conditions en vigueur. Réglables par variables d'environnement, pour
    qu'un changement de prix ne demande pas de déployer du code."""
    # Le prix de lancement (Daniel, 27 sept. 2026) : 9,99 $ au lieu de 19,99 $,
    # pour un temps limité, jusqu'au 31 déc. 2026 (décidé par Daniel le 27 sept.).
    # COMPOSTELLE_PROMO_FIN (AAAA-MM-JJ, inclus) la déplace et borne la
    # promotion : passée cette date, le prix régulier revient tout seul.
    # COMPOSTELLE_PROMO_CENTS=0 la coupe. `prix` est TOUJOURS le montant facturé.
    regulier = _entier("COMPOSTELLE_PRIX_CENTS", 1999)
    promo, fin = _entier("COMPOSTELLE_PROMO_CENTS", 999), os.environ.get("COMPOSTELLE_PROMO_FIN", "2026-12-31").strip()
    en_promo = 0 < promo < regulier and (not fin or _aujourdhui() <= fin)
    return {
        "prix": promo if en_promo else regulier,
        "prixRegulier": regulier,
        "promo": en_promo,
        "promoFin": fin if en_promo else "",
        "recharge": _entier("COMPOSTELLE_RECHARGE_CENTS", 499),
        "devise": os.environ.get("COMPOSTELLE_DEVISE", "cad").lower(),
        "conversations": _entier("COMPOSTELLE_CONVERSATIONS", 100),
        "rechargeConversations": _entier("COMPOSTELLE_RECHARGE_CONVERSATIONS", 50),
        "jours": _entier("COMPOSTELLE_DUREE_JOURS", 365),
        "toursMax": _entier("COMPOSTELLE_TOURS_MAX", 16),
        "parJour": _entier("COMPOSTELLE_PAR_JOUR", 30),
        # Loi 25 : un code est effacé ce nombre de jours après son expiration
        # (menage()) ; la page de confidentialité le relit ici.
        "conservation": _entier("COMPOSTELLE_CONSERVATION_JOURS", 365),
    }


def disponible():
    """La vente est-elle branchée ? Sans clé Stripe, on ne propose pas d'acheter."""
    return bool(os.environ.get("STRIPE_SECRET_KEY"))


def est_code(code):
    return (isinstance(code, str) and len(code) == LONGUEUR and code.startswith(PREFIXE)
            and all(c in ALPHABET for c in code[len(PREFIXE):]))


def _aujourdhui():
    return _dt.datetime.now(_dt.timezone.utc).date().isoformat()


def _maintenant():
    return _dt.datetime.now(_dt.timezone.utc).replace(microsecond=0).isoformat()


# ── Stripe ──────────────────────────────────────────────────────────────────

def _aplatir(d, prefixe=""):
    """{'a': {'b': 1}} → [('a[b]', '1')] : la forme que l'API de Stripe attend."""
    out = []
    for k, v in d.items():
        cle = f"{prefixe}[{k}]" if prefixe else str(k)
        if isinstance(v, dict):
            out += _aplatir(v, cle)
        elif isinstance(v, list):
            for i, x in enumerate(v):
                out += _aplatir(x, f"{cle}[{i}]") if isinstance(x, dict) else [(f"{cle}[{i}]", str(x))]
        elif v is not None:
            out.append((cle, "true" if v is True else "false" if v is False else str(v)))
    return out


def _stripe(methode, chemin, donnees=None, cle=None):
    """Un appel à l'API de Stripe. Rend (réponse, None) ou (None, message)."""
    cle = cle or os.environ.get("STRIPE_SECRET_KEY", "")
    corps = urllib.parse.urlencode(_aplatir(donnees)).encode() if donnees else None
    req = urllib.request.Request(API + chemin, data=corps, method=methode, headers={
        "Authorization": "Basic " + base64.b64encode((cle + ":").encode()).decode(),
        "Content-Type": "application/x-www-form-urlencoded",
        # Même leçon que Resend : sans User-Agent, certains pare-feu refusent
        # « Python-urllib » avant même de lire la clé.
        "User-Agent": "francis-compostelle/1.0",
    })
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.loads(r.read()), None
    except urllib.error.HTTPError as e:
        try:
            msg = json.loads(e.read()).get("error", {}).get("message", "")
        except Exception:
            msg = ""
        return None, f"Stripe {e.code} : {msg or e.reason}"
    except Exception as e:  # réseau
        return None, f"Stripe injoignable : {e}"


def signature_valide(charge_utile, entete, secret, maintenant=None):
    """Vérifie l'en-tête Stripe-Signature (« t=…,v1=… ») d'un webhook.
    `charge_utile` : les octets bruts du corps, jamais le JSON relu."""
    if not (entete and secret):
        return False
    morceaux = {}
    for p in entete.split(","):
        k, _, v = p.partition("=")
        morceaux.setdefault(k.strip(), []).append(v.strip())
    try:
        t = int(morceaux.get("t", ["0"])[0])
    except ValueError:
        return False
    if abs((maintenant or time.time()) - t) > TOLERANCE_S:
        return False
    attendu = hmac.new(secret.encode(), f"{t}.".encode() + charge_utile, hashlib.sha256).hexdigest()
    return any(hmac.compare_digest(attendu, v) for v in morceaux.get("v1", []))


# ── Le registre des codes ───────────────────────────────────────────────────

class Registre:
    """Les codes de pèlerins, sur le stockage que le serveur prête."""

    def __init__(self, charger, sauver, verrou):
        self.charger, self.sauver, self.verrou = charger, sauver, verrou

    def trouver(self, code):
        if not est_code(code):
            return None
        p = next((p for p in self.charger() if p.get("code") == code), None)
        if p is None and (code in CODES_ESSAI or code in CODES_ESSAI_TROUSSES):
            p = self._ouvrir_essai(code)
        return p

    def _ouvrir_essai(self, code):
        """Un code d'essai du pilote, créé à son premier usage (voir CODES_ESSAI)."""
        with self.verrou:
            tous = self.charger()
            p = next((x for x in tous if x.get("code") == code), None)
            if p is None:
                etiq, trousse = CODES_ESSAI_TROUSSES.get(code) or (CODES_ESSAI.get(code), None)
                p = {"code": code, "etat": "actif", "essai": etiq, "cree": _maintenant(), "active": _maintenant(),
                     "conversations": ESSAI_CONVERSATIONS, "utilisees": 0, "parJour": {}, "expire": ESSAI_FIN, "sessions": []}
                if trousse:
                    p["trousse"] = trousse
                tous.append(p)
                self.sauver(tous)
            return p

    def _nouveau_code(self, pris):
        while True:
            c = PREFIXE + "".join(secrets.choice(ALPHABET) for _ in range(LONGUEUR - len(PREFIXE)))
            if c not in pris:
                return c

    # -- le ménage (Loi 25) ---------------------------------------------------
    @staticmethod
    def _a_effacer(p, aujourdhui, conservation):
        """Un code actif, `conservation` jours après son expiration ; un code
        réservé jamais payé, après 7 jours (crediter() le recrée si un paiement
        tardif arrive)."""
        if p.get("etat") == "actif":
            fin = p.get("expire", "")
            return bool(fin) and (_dt.date.fromisoformat(fin) + _dt.timedelta(days=conservation)).isoformat() < aujourdhui
        cree = str(p.get("cree", ""))[:10]
        return bool(cree) and (_dt.date.fromisoformat(cree) + _dt.timedelta(days=7)).isoformat() < aujourdhui

    def menage(self, tous=None):
        """Retire les codes à effacer. Appelé à chaque achat (sous le verrou) :
        sans cron, l'effacement a lieu au plus tard au prochain achat. Rend le
        nombre de codes retirés."""
        j, c = _aujourdhui(), offre()["conservation"]
        garde = [p for p in tous if not self._a_effacer(p, j, c)]
        n = len(tous) - len(garde)
        tous[:] = garde
        return n

    # -- l'achat --------------------------------------------------------------
    def commencer_achat(self, adresse, recharge=None):
        """Crée la session Stripe Checkout. Rend ({url, session}, None) ou (None, (message, statut))."""
        if not disponible():
            return None, ("La vente n'est pas encore ouverte.", 503)
        o = offre()
        if recharge:
            p = self.trouver(recharge)
            if not p or p.get("etat") != "actif":
                return None, ("Ce code n'existe pas.", 404)
            if p.get("expire", "") < _aujourdhui():
                return None, ("Ce code a expiré : prenez un nouvel accès.", 409)
            code, montant, nb, quoi = recharge, o["recharge"], o["rechargeConversations"], "recharge"
            nom = f"Parler librement — {nb} conversations de plus"
        else:
            with self.verrou:
                tous = self.charger()
                self.menage(tous)
                code = self._nouveau_code({p.get("code") for p in tous})
                # Réservé, pas actif : il le devient au paiement. Un code réservé
                # jamais payé n'ouvre rien, et le ménage peut le retirer.
                tous.append({"code": code, "etat": "reserve", "cree": _maintenant(), "sessions": []})
                self.sauver(tous)
            montant, nb, quoi = o["prix"], o["conversations"], "achat"
            nom = f"En route vers Compostelle — Parler librement ({nb} conversations, {o['jours'] // 30} mois)"
        retour = adresse.rstrip("/") + "/modules-autonomes/compostelle/"
        session, err = _stripe("POST", "/checkout/sessions", {
            "mode": "payment",
            "locale": "fr-CA",
            "success_url": retour + "#achat/{CHECKOUT_SESSION_ID}",
            "cancel_url": retour + "#achat-annule",
            "line_items": [{"quantity": 1, "price_data": {
                "currency": o["devise"], "unit_amount": montant, "product_data": {"name": nom}}}],
            "metadata": {"produit": "compostelle", "quoi": quoi, "code": code},
            # La description du paiement paraît sur le reçu de Stripe : le code y
            # voyage, et c'est la façon de le retrouver sans rien garder de nous.
            "payment_intent_data": {"description": f"Votre code d'accès : {code}",
                                    "metadata": {"produit": "compostelle", "code": code}},
        })
        if err:
            return None, (err, 502)
        return {"url": session.get("url"), "session": session.get("id")}, None

    # -- le crédit ------------------------------------------------------------
    def crediter(self, session):
        """Applique une session Checkout PAYÉE. Idempotent : une session déjà
        créditée ne l'est pas deux fois. Rend l'enregistrement du code, ou None."""
        meta = session.get("metadata") or {}
        if meta.get("produit") != "compostelle" or session.get("payment_status") != "paid":
            return None
        code, sid, o = meta.get("code", ""), session.get("id", ""), offre()
        with self.verrou:
            tous = self.charger()
            p = next((x for x in tous if x.get("code") == code), None)
            if p is None:
                # Réservation perdue (volume vidé entre-temps) : le paiement est
                # réel, on recrée plutôt que de refuser un pèlerin qui a payé.
                p = {"code": code, "etat": "reserve", "cree": _maintenant(), "sessions": []}
                tous.append(p)
            if sid in p.get("sessions", []):
                return p
            if meta.get("quoi") == "recharge":
                p["conversations"] = p.get("conversations", 0) + o["rechargeConversations"]
            else:
                p.update(etat="actif", active=_maintenant(), conversations=o["conversations"],
                         utilisees=0, parJour={},
                         expire=(_dt.datetime.now(_dt.timezone.utc).date() + _dt.timedelta(days=o["jours"])).isoformat())
            p.setdefault("sessions", []).append(sid)
            p["paye"] = p.get("paye", 0) + int(session.get("amount_total") or 0)
            self.sauver(tous)
            return p

    def depuis_retour(self, session_id):
        """Le pèlerin revient de Stripe avec `session_id` : on demande à Stripe
        si c'est payé (sans attendre le webhook), on crédite, on rend le code."""
        if not (isinstance(session_id, str) and session_id.startswith("cs_")):
            return None, ("Retour invalide.", 400)
        session, err = _stripe("GET", "/checkout/sessions/" + urllib.parse.quote(session_id))
        if err:
            return None, (err, 502)
        if (session.get("metadata") or {}).get("produit") != "compostelle":
            return None, ("Ce paiement ne concerne pas Compostelle.", 404)
        if session.get("payment_status") != "paid":
            return None, ("Le paiement n'est pas encore confirmé.", 409)
        p = self.crediter(session)
        return (self.etat(p) if p else None), (None if p else ("Paiement introuvable.", 404))

    def webhook(self, corps, entete):
        """L'avis de Stripe. Rend (statut HTTP, message)."""
        if not signature_valide(corps, entete, os.environ.get("STRIPE_WEBHOOK_SECRET", "")):
            return 400, "signature"
        try:
            ev = json.loads(corps)
        except ValueError:
            return 400, "json"
        if ev.get("type") in ("checkout.session.completed", "checkout.session.async_payment_succeeded"):
            self.crediter(ev.get("data", {}).get("object", {}))
        return 200, "ok"

    # -- l'usage --------------------------------------------------------------
    def etat(self, p):
        o = offre()
        return {"code": p["code"], "actif": p.get("etat") == "actif",
                "restant": max(0, p.get("conversations", 0) - p.get("utilisees", 0)),
                "expire": p.get("expire", ""), "toursMax": o["toursMax"]}

    def voix_permise(self, p):
        """Un code d'essai d'une trousse lit les voix de ses personnages
        (/api/voix) tant qu'il est actif et non expiré ; Compostelle n'en a pas besoin."""
        return bool(p.get("trousse")) and p.get("etat") == "actif" and p.get("expire", "") >= _aujourdhui()

    def refus(self, p, scenario, nb_tours, premier_tour):
        """Pourquoi ce code ne peut pas jouer ce tour — ou None. (message, statut)."""
        o = offre()
        permis = TROUSSES.get(p.get("trousse"), (SCENARIO,))
        if scenario not in permis:
            return ("Ce code n'ouvre pas ce jeu de rôle." if p.get("trousse")
                    else "Ce code n'ouvre que « Parler librement » d'En route vers Compostelle.", 403)
        if p.get("etat") != "actif":
            return ("Ce code n'est pas encore actif : le paiement n'est pas confirmé.", 402)
        if p.get("expire", "") < _aujourdhui():
            return ("Votre accès a expiré.", 402)
        if nb_tours > o["toursMax"]:
            return (f"Une conversation compte {o['toursMax']} tours au plus : demandez le bilan, puis recommencez.", 409)
        if premier_tour:
            if p.get("conversations", 0) - p.get("utilisees", 0) <= 0:
                return ("Vos conversations sont toutes utilisées.", 402)
            if (p.get("parJour") or {}).get(_aujourdhui(), 0) >= o["parJour"]:
                return ("Assez pour aujourd'hui : revenez demain.", 429)
        return None

    def consommer(self, code):
        """Une conversation de plus — appelé après la PREMIÈRE réponse réussie,
        pour ne jamais faire payer une panne."""
        with self.verrou:
            tous = self.charger()
            p = next((x for x in tous if x.get("code") == code), None)
            if not p:
                return None
            p["utilisees"] = p.get("utilisees", 0) + 1
            j = _aujourdhui()
            pj = {k: v for k, v in (p.get("parJour") or {}).items() if k >= j}   # on ne garde que le jour
            pj[j] = pj.get(j, 0) + 1
            p["parJour"] = pj
            self.sauver(tous)
            return p
