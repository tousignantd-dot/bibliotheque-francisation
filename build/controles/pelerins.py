#!/usr/bin/env python3
"""Contrôle des accès payants de Compostelle (pelerins.py), sans réseau.

    python3 build/controles/pelerins.py

Stripe est simulé (on remplace `pelerins._stripe`), le stockage est une liste
en mémoire. Le contrôle vérifie surtout que les REFUS refusent : un code non
payé, expiré, épuisé, hors de son scénario, une conversation trop longue, une
signature de webhook fausse ou périmée, un paiement crédité deux fois. Sort en
code 1 au premier écart.
"""
import hashlib, hmac, json, os, pathlib, sys, threading, time

RACINE = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RACINE))
os.environ.update(STRIPE_SECRET_KEY="sk_test_faux", STRIPE_WEBHOOK_SECRET="whsec_faux",
                  COMPOSTELLE_PAR_JOUR="3", COMPOSTELLE_TOURS_MAX="16")
import pelerins as P  # noqa: E402

ECARTS = []


def ok(cond, quoi):
    print(("  ✓ " if cond else "  ✗ ") + quoi)
    if not cond:
        ECARTS.append(quoi)


# -- un faux Stripe ----------------------------------------------------------
SESSIONS, APPELS = {}, []


def faux_stripe(methode, chemin, donnees=None, cle=None):
    APPELS.append((methode, chemin, donnees))
    if methode == "POST" and chemin == "/checkout/sessions":
        sid = "cs_test_%d" % (len(SESSIONS) + 1)
        montant = donnees["line_items"][0]["price_data"]["unit_amount"]
        SESSIONS[sid] = {"id": sid, "payment_status": "unpaid", "amount_total": montant,
                         "metadata": dict(donnees["metadata"]), "url": "https://checkout.stripe.test/" + sid}
        return SESSIONS[sid], None
    if methode == "GET" and chemin.startswith("/checkout/sessions/"):
        s = SESSIONS.get(chemin.rsplit("/", 1)[1])
        return (s, None) if s else (None, "Stripe 404 : No such session")
    return None, "inattendu"


P._stripe = faux_stripe
MEMOIRE = []
R = P.Registre(lambda: json.loads(json.dumps(MEMOIRE)),
               lambda l: (MEMOIRE.clear(), MEMOIRE.extend(json.loads(json.dumps(l)))),
               threading.RLock())

print("L'achat")
res, err = R.commencer_achat("https://portail.edufrancis.ca")
ok(err is None and res["url"].startswith("https://"), "une session Checkout est créée")
envoi = APPELS[-1][2]
code = envoi["metadata"]["code"]
ok(P.est_code(code) and len(code) == 8, f"le code est tiré avant le paiement ({code})")
ok(code in envoi["payment_intent_data"]["description"], "le code est dans la description (donc sur le reçu)")
ok(envoi["success_url"].endswith("/modules-autonomes/compostelle/#achat/{CHECKOUT_SESSION_ID}"), "le retour mène à l'application")
ok(envoi["line_items"][0]["price_data"]["unit_amount"] == 999, "prix de lancement : 9,99 $ facturés")
ok(envoi["line_items"][0]["price_data"]["currency"] == "cad", "en dollars canadiens")
plat = dict(P._aplatir(envoi))
ok(plat.get("line_items[0][price_data][unit_amount]") == "999" and plat.get("metadata[code]") == code,
   "le formulaire envoyé à Stripe a la forme attendue (line_items[0][…])")
p = R.trouver(code)
ok(p and p["etat"] == "reserve", "le code est réservé, pas actif")
ok(R.refus(p, P.SCENARIO, 0, True) is not None, "un code réservé ne joue pas")
ok(not any(k in json.dumps(MEMOIRE) for k in ("email", "courriel", "nom", "card")), "rien de la personne n'est gardé")

print("Le retour avant paiement, puis après")
sid = res["session"]
etat, err = R.depuis_retour(sid)
ok(etat is None and err and err[1] == 409, "retour sans paiement : 409, rien de crédité")
SESSIONS[sid]["payment_status"] = "paid"
etat, err = R.depuis_retour(sid)
ok(err is None and etat["actif"] and etat["restant"] == 100, "retour payé : actif, 100 conversations")
etat2, _ = R.depuis_retour(sid)
ok(etat2["restant"] == 100 and len(R.trouver(code)["sessions"]) == 1, "revenir deux fois ne crédite pas deux fois")
ok(R.depuis_retour("nimporte")[1][1] == 400, "un identifiant de retour bidon est refusé")

print("Le webhook")
corps = json.dumps({"type": "checkout.session.completed", "data": {"object": SESSIONS[sid]}}).encode()
t = int(time.time())
sig = hmac.new(b"whsec_faux", f"{t}.".encode() + corps, hashlib.sha256).hexdigest()
ok(R.webhook(corps, f"t={t},v1={sig}")[0] == 200, "signature juste : accepté")
ok(R.trouver(code)["conversations"] == 100, "le webhook après le retour ne recrédite pas")
ok(R.webhook(corps, f"t={t},v1={'0' * 64}")[0] == 400, "signature fausse : refusé")
vieux = t - 3600
sigv = hmac.new(b"whsec_faux", f"{vieux}.".encode() + corps, hashlib.sha256).hexdigest()
ok(R.webhook(corps, f"t={vieux},v1={sigv}")[0] == 400, "signature d'il y a une heure : refusée (rejeu)")
ok(R.webhook(corps + b" ", f"t={t},v1={sig}")[0] == 400, "corps modifié : refusé")

print("L'usage")
p = R.trouver(code)
ok(R.refus(p, P.SCENARIO, 0, True) is None, "un code payé joue")
ok(R.refus(p, "louer", 0, True)[1] == 403, "hors de Compostelle : refusé")
ok(R.refus(p, P.SCENARIO, 17, False)[1] == 409, "au-delà de 16 tours : refusé")
for _ in range(3):
    R.consommer(code)
p = R.trouver(code)
ok(R.etat(p)["restant"] == 97, "chaque conversation se décompte")
ok(R.refus(p, P.SCENARIO, 0, True)[1] == 429, "plafond du jour atteint : refusé")
ok(R.refus(p, P.SCENARIO, 3, False) is None, "…mais une conversation en cours se termine")
MEMOIRE[0]["parJour"] = {"2000-01-01": 3}
MEMOIRE[0]["utilisees"] = 100
ok(R.refus(R.trouver(code), P.SCENARIO, 0, True)[1] == 402, "conversations épuisées : refusé")
MEMOIRE[0]["utilisees"] = 3
MEMOIRE[0]["expire"] = "2001-01-01"
ok(R.refus(R.trouver(code), P.SCENARIO, 3, False)[1] == 402, "accès expiré : refusé")

print("La recharge")
ok(R.commencer_achat("https://x", recharge=code)[1][1] == 409, "pas de recharge d'un code expiré")
MEMOIRE[0]["expire"] = "2999-01-01"
res2, err = R.commencer_achat("https://x", recharge=code)
ok(err is None and APPELS[-1][2]["line_items"][0]["price_data"]["unit_amount"] == 499, "une recharge coûte 4,99 $")
SESSIONS[res2["session"]]["payment_status"] = "paid"
R.depuis_retour(res2["session"])
ok(R.etat(R.trouver(code))["restant"] == 97 + 50, "la recharge ajoute 50 conversations")
ok(R.commencer_achat("https://x", recharge="PCZZZZZZ")[1][1] == 404, "recharge d'un code inconnu : refusée")

print("Le ménage (Loi 25)")
vieux = [{"code": "PCAAAAAA", "etat": "actif", "expire": "2000-01-01"},
         {"code": "PCBBBBBB", "etat": "actif", "expire": "2999-01-01"},
         {"code": "PCCCCCCC", "etat": "reserve", "cree": "2000-01-01T00:00:00+00:00"},
         {"code": "PCDDDDDD", "etat": "reserve", "cree": P._maintenant()}]
ok(R.menage(vieux) == 2 and [x["code"] for x in vieux] == ["PCBBBBBB", "PCDDDDDD"],
   "un code expiré depuis plus d'un an et une réservation de plus de 7 jours sont effacés")
ok(P.offre()["conservation"] == 365, "la durée de conservation est lue par l'offre (365 jours)")

print("Le prix de lancement")
o = P.offre(); ok(o["prix"] == 999 and o["prixRegulier"] == 1999 and o["promo"] and o["promoFin"] == "2026-12-31", "9,99 $ au lieu de 19,99 $, jusqu'au 31 décembre 2026")
os.environ["COMPOSTELLE_PROMO_FIN"] = "2000-01-01"
o = P.offre(); ok(o["prix"] == 1999 and not o["promo"] and o["promoFin"] == "", "la promotion finie, le prix régulier revient seul")
os.environ["COMPOSTELLE_PROMO_FIN"] = "2999-12-31"
ok(P.offre()["prix"] == 999 and P.offre()["promoFin"] == "2999-12-31", "avant la fin, la promotion tient")
os.environ["COMPOSTELLE_PROMO_CENTS"] = "0"
ok(P.offre()["prix"] == 1999, "COMPOSTELLE_PROMO_CENTS=0 coupe la promotion")
del os.environ["COMPOSTELLE_PROMO_FIN"], os.environ["COMPOSTELLE_PROMO_CENTS"]

print("L'achat d'une trousse de métier")
for prod, tr in (("francoeur", "francoeur"), ("hotel", "hotel")):
    r3, e3 = R.commencer_achat("https://portail.edufrancis.ca", produit=prod)
    env3 = APPELS[-1][2]; c3 = env3["metadata"]["code"]
    ok(e3 is None and env3["success_url"].startswith("https://portail.edufrancis.ca" + P.PRODUITS[prod]["chemin"] + "#achat/"), f"{prod} : le retour mène à sa trousse")
    ok(env3["line_items"][0]["price_data"]["unit_amount"] == P.offre()["prix"], f"{prod} : même prix que Compostelle")
    ok(R.trouver(c3).get("trousse") == tr and R.refus(R.trouver(c3), P.TROUSSES[tr][0], 0, True)[1] == 402, f"{prod} : réservé, lié à sa trousse, ne joue pas avant paiement")
    SESSIONS[r3["session"]]["payment_status"] = "paid"
    et3, _ = R.depuis_retour(r3["session"])
    p3 = R.trouver(c3)
    ok(et3 and et3["actif"] and et3["produit"] == prod, f"{prod} : payé, actif, le produit est rendu à la page")
    ok(R.refus(p3, P.TROUSSES[tr][-1], 0, True) is None and R.refus(p3, P.SCENARIO, 0, True)[1] == 403 and R.voix_permise(p3),
       f"{prod} : ouvre son jeu de rôle et ses voix, pas Compostelle")
    R.commencer_achat("https://x", recharge=c3)
    ok(APPELS[-1][2]["metadata"]["produit"] == prod, f"{prod} : la recharge suit le produit du code")
ok(R.commencer_achat("https://x", produit="autre")[1][1] == 400, "un produit inconnu est refusé")

print("Les décisions du 28 septembre (vente au public)")
R.commencer_achat("https://portail.edufrancis.ca", produit="hotel")
env4 = APPELS[-1][2]; plat4 = dict(P._aplatir(env4))
ok(plat4.get("payment_method_types[0]") == "card" and "payment_method_types[1]" not in plat4, "carte seulement")
ok(plat4.get("billing_address_collection") == "required", "Stripe demande le nom et l'adresse")
ok(plat4.get("consent_collection[terms_of_service]") == "required" and "conditions-de-vente.html" in plat4.get("custom_text[terms_of_service_acceptance][message]", ""),
   "case obligatoire, avec le lien vers les conditions")
c4 = env4["metadata"]["code"]; SESSIONS[APPELS[-1][2] and list(SESSIONS)[-1]]["payment_status"] = "paid"; R.depuis_retour(list(SESSIONS)[-1])
ok(R.trouver(c4)["etat"] == "actif", "le code acheté est actif")
R.rembourser({"id": "ch_1", "amount": 999, "amount_refunded": 500, "description": f"Votre code d'accès : {c4}"})
ok(R.trouver(c4)["etat"] == "actif", "un remboursement partiel n'éteint pas le code")
R.rembourser({"id": "ch_2", "amount": 999, "amount_refunded": 999, "description": f"Votre code d'accès : {c4}"})
p4 = R.trouver(c4)
ok(p4["etat"] == "rembourse" and R.refus(p4, "comptoir-fr-en", 0, True)[1] == 402 and not R.voix_permise(p4), "un remboursement complet éteint le code, voix comprises")
R.rembourser({"id": "ch_2", "amount": 999, "amount_refunded": 999, "description": f"Votre code d'accès : {c4}"})
ok(R.trouver(c4)["rembourses"].count("ch_2") == 1, "un avis répété ne compte qu'une fois")

print("Le lot d'un employeur")
ok(R.commencer_achat("https://x", produit="hotel", quantite=1)[1] is None, "un seul code : l'achat ordinaire")
ok(R.commencer_achat("https://x", produit="hotel", quantite=51)[1][1] == 400 and R.commencer_achat("https://x", produit="hotel", quantite="deux")[1][1] == 400,
   "un lot de 51, ou une quantité illisible, est refusé")
r5, e5 = R.commencer_achat("https://portail.edufrancis.ca", produit="hotel", quantite=5)
env5 = APPELS[-1][2]; codes5 = env5["metadata"]["codes"].split(","); sv5 = env5["metadata"]["suivi"]
ok(e5 is None and len(codes5) == 5 and len(set(codes5)) == 5 and P.est_suivi(sv5) and not P.est_code(sv5), "5 codes distincts et un code de suivi, qui n'est pas un code de jeu")
ok(env5["line_items"][0]["quantity"] == 5 and all(c in env5["payment_intent_data"]["description"] for c in codes5 + [sv5]),
   "Stripe facture 5 fois le prix ; les codes et le suivi sont sur le reçu")
ok(len(P._aplatir(env5)) and len(env5["metadata"]["codes"]) <= 500, "les métadonnées tiennent sous la limite de Stripe")
ok(all(R.trouver(c)["etat"] == "reserve" for c in codes5) and R.trouver(sv5) is None, "avant paiement : réservés ; le suivi n'est pas un code")
SESSIONS[r5["session"]]["payment_status"] = "paid"
e5b, _ = R.depuis_retour(r5["session"])
ok(e5b and e5b["suivi"] == sv5 and e5b["codes"] == codes5, "au retour : la liste des codes et le code de suivi")
ok(all(R.trouver(c)["etat"] == "actif" and R.trouver(c)["trousse"] == "hotel" for c in codes5), "payé : les cinq codes sont actifs, liés à l'hôtel")
R.depuis_retour(r5["session"])
ok(all(len(R.trouver(c)["sessions"]) == 1 for c in codes5), "revenir deux fois n'active pas deux fois")
R.consommer(codes5[0]); R.consommer(codes5[0])
s5 = R.suivi(sv5)
ok(s5 and len(s5["codes"]) == 5 and s5["codes"][0]["utilisees"] == 2 and s5["codes"][0]["dernier"] and s5["codes"][1]["utilisees"] == 0,
   "le suivi : 2 conversations sur le premier, rien sur les autres, et la date")
ok(not any(k in json.dumps(s5) for k in ("sessions", "paye", "nom", "email", "courriel")), "le suivi ne rend ni paiement ni personne")
ok(R.suivi("SVZZZZZZ") is None and R.suivi(codes5[0]) is None, "un code de suivi inventé, ou un code de jeu, ne montre rien")
R.rembourser({"id": "ch_lot", "amount": 4995, "amount_refunded": 4995, "description": env5["payment_intent_data"]["description"]})
ok(all(R.trouver(c)["etat"] == "rembourse" for c in codes5), "un lot remboursé éteint ses cinq codes")

print("Les codes d'essai du pilote")
ok(all(P.est_code(c) for c in P.CODES_ESSAI) and len(set(P.CODES_ESSAI)) == len(P.CODES_ESSAI), "les codes d'essai sont des codes de pèlerin valides et distincts")
ce = next(iter(P.CODES_ESSAI)); avant = len(MEMOIRE)
pe = R.trouver(ce)
ok(pe and pe["etat"] == "actif" and pe["conversations"] == P.ESSAI_CONVERSATIONS and len(MEMOIRE) == avant + 1, "un code d'essai s'ouvre à son premier usage")
ok(R.trouver(ce) is not None and len(MEMOIRE) == avant + 1, "…une seule fois")
ok(R.refus(pe, "louer", 0, True)[1] == 403, "un code d'essai n'ouvre que Compostelle")
print("Les codes d'essai des trousses de métier")
tous_essais = list(P.CODES_ESSAI) + list(P.CODES_ESSAI_TROUSSES)
ok(all(P.est_code(c) for c in P.CODES_ESSAI_TROUSSES) and len(set(tous_essais)) == len(tous_essais), "codes des trousses valides et distincts de ceux de Compostelle")
ok(all(t in P.TROUSSES for _, t in P.CODES_ESSAI_TROUSSES.values()), "chaque code nomme une trousse connue")
for tr in P.TROUSSES:
    ct = next(c for c, (_, t) in P.CODES_ESSAI_TROUSSES.items() if t == tr)
    pt = R.trouver(ct)
    ok(pt and pt.get("trousse") == tr and R.refus(pt, P.TROUSSES[tr][0], 0, True) is None, f"un code {tr} ouvre son jeu de rôle")
    ok(R.refus(pt, P.SCENARIO, 0, True)[1] == 403 and R.voix_permise(pt), f"un code {tr} n'ouvre pas Compostelle, mais lit les voix")
ok(not R.voix_permise(pe), "un code de Compostelle ne lit pas les voix des trousses")
ok(R.trouver("PCZZZZZZ") is None or "PCZZZZZZ" in P.CODES_ESSAI, "un code inventé n'ouvre rien")

print("Les codes")
ok(not P.est_code("ABC123") and not P.est_code("S" + "X" * 16), "un code d'élève ou un jeton de séance n'est pas un code de pèlerin")
ok(not P.est_code("PC0OIL11"), "l'alphabet exclut 0, O, I, L, 1")
del os.environ["STRIPE_SECRET_KEY"]
ok(R.commencer_achat("https://x")[1][1] == 503, "sans clé Stripe : la vente est fermée (503)")

print()
if ECARTS:
    print(f"{len(ECARTS)} écart(s)."); sys.exit(1)
print("Aucun écart.")
