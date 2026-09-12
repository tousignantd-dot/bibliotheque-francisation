#!/usr/bin/env python3
"""La recherche dans le contenu : les modules et les fiches, pas seulement les
titres du catalogue.

Le catalogue cherchait dans l'enregistrement d'une activité — titre, mots-clés,
domaine. C'est ce qu'on sait *d'*une activité, pas ce qu'il y a *dedans*.
« La visite du quatre et demie » est le titre d'une fiche de séance et une
réplique de dialogue du module 78 ; aucun des deux n'est dans `activities.json`,
et la recherche ne rendait donc rien.

**Le piège, et c'est le seul vrai.** Le contenu d'un module ne vit pas dans son
HTML : il vit dans des constantes JavaScript (`DIALOGUES`, `EXOS`, `FC_CARDS`)
à l'intérieur d'un `<script>`. Retirer les scripts avant de dépouiller les
balises — ce que fait n'importe quel extracteur de texte — rend un module
**vide**. On dépouille donc les deux : le texte des balises, et les littéraux
de chaîne des scripts.

**L'index n'est pas versionné, et c'est volontaire.** `data/materiel.json` et
`data/sections.json` le sont parce qu'ils *décrivent* ce que le dépôt livre ;
celui-ci n'est qu'un **cache** de ce qui est déjà sur le disque, dix mégaoctets
qu'il faudrait réécrire à chaque construction de module. Il se refait au
démarrage, dans le fil d'initialisation, en une dizaine de secondes — et si
rien ne l'a encore construit, la recherche répond « pas encore prête » au lieu
de mentir par une liste vide.

    python3 build/recherche.py --etat
    python3 build/recherche.py "la visite du quatre et demie"
"""
import html
import json
import re
import threading
import time
import unicodedata
from pathlib import Path

# Ce qu'on ne garde pas d'un littéral de script : du code, une adresse, un
# sélecteur. Ce sont les chaînes qui ne disent rien à personne et qui pèsent.
_CODE = re.compile(r'[{};]|://|^[\w.#@-]+$|function|var |=>')
_BALISES = re.compile(r'<[^>]+>')
_SCRIPT_OU_STYLE = re.compile(r'<(script|style)\b[^>]*>.*?</\1>', re.S | re.I)
_SCRIPT_EN_LIGNE = re.compile(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>',
                              re.S | re.I)
_LITTERAL = re.compile(r"'((?:[^'\\\n]|\\.){3,})'|\"((?:[^\"\\\n]|\\.){3,})\"")
_TITRE = re.compile(r'<title[^>]*>(.*?)</title>', re.S | re.I)
_LETTRE = re.compile(r'[A-Za-zÀ-ÿ]')

# Un extrait de 300 caractères ne se lit pas dans une carte ; un mot isolé ne
# dit pas où l'on est tombé.
EXTRAIT_AVANT = 60
EXTRAIT_APRES = 150


def _table_des_accents():
    """Une table caractère → caractère, **un pour un**.

    C'est la condition de tout le reste : l'extrait montré à l'écran se découpe
    dans le texte d'origine, aux positions trouvées dans le texte aplati. Si
    l'aplatissement changeait la longueur — ce que fait le `NFD` + retrait des
    marques qu'on écrit d'ordinaire —, l'extrait glisserait d'un cran par
    accent rencontré et se couperait au milieu d'un mot. Mesuré : quatre
    caractères d'écart sur un seul module, à cause de sélecteurs de variante
    invisibles. Une table 1 pour 1 rend l'écart impossible par construction.
    """
    table = {}
    for cp in range(0x41, 0x2000):
        ch = chr(cp)
        nu = "".join(c for c in unicodedata.normalize("NFD", ch)
                     if unicodedata.category(c) != "Mn").lower()
        if len(nu) == 1 and nu != ch:
            table[cp] = nu
    return table


_ACCENTS = _table_des_accents()


def sans_accents(texte):
    """La forme sur laquelle tout se compare : sans accents, sans casse.

    « demenagement » doit trouver « déménagement » — un clavier pressé n'accentue
    pas, et une recherche qui échoue là-dessus passe pour un fonds vide.
    """
    return str(texte or "").translate(_ACCENTS)


def _propre(morceau):
    return re.sub(r"\s+", " ", html.unescape(_BALISES.sub(" ", morceau))).strip()


def texte_des_balises(source):
    return _propre(_SCRIPT_OU_STYLE.sub(" ", source))


def _utile(chaine):
    # Une chaîne sans espace et longue est un identifiant ou du base64 : les
    # activités exportées par un bundler en portent des mégaoctets.
    if len(chaine) > 300 or (" " not in chaine and len(chaine) > 40):
        return False
    return bool(_LETTRE.search(chaine))


# Au-delà de cette longueur, une ligne n'est pas du contenu : c'est un actif
# encodé en base64. Les activités exportées par un bundler en portent une de
# 1,7 **mégaoctet** ; l'expression des littéraux y part en arrière — trois cents
# mégaoctets de mémoire par fichier, jamais rendus, et 3,5 Go pour douze
# fichiers. Mesuré, pas supposé. Les modules produits par la chaîne ne
# dépassent pas six cents caractères par ligne.
LIGNE_MAX = 2000


def texte_des_scripts(source):
    """Les littéraux de chaîne des scripts en ligne — là où vit un module."""
    vues, sortie = set(), []
    for bloc in _SCRIPT_EN_LIGNE.findall(source):
        for ligne in bloc.split("\n"):
            if len(ligne) > LIGNE_MAX:
                continue
            for m in _LITTERAL.finditer(ligne):
                brut = m.group(1) or m.group(2)
                if _CODE.search(brut):
                    continue
                chaine = _propre(brut.replace("\\'", "'").replace('\\"', '"'))
                if len(chaine) < 3 or chaine in vues or not _utile(chaine):
                    continue
                vues.add(chaine)
                sortie.append(chaine)
    return " ".join(sortie)


def texte_du_fichier(chemin, avec_scripts):
    source = Path(chemin).read_text(encoding="utf-8", errors="replace")
    titre = _propre(_TITRE.search(source).group(1)) if _TITRE.search(source) else ""
    texte = texte_des_balises(source)
    if avec_scripts:
        texte += " " + texte_des_scripts(source)
    return titre, texte


# ─────────────────────────── L'index ───────────────────────────

class Index:
    """Les documents dépouillés, et de quoi les retrouver.

    Un document : `{activiteId, type, titre, chemin, texte, plat}` — `plat`
    étant le texte sans accents ni casse, calculé une fois. C'est lui qu'on
    parcourt ; `texte` ne sert qu'à découper l'extrait qu'on montre.
    """

    def __init__(self):
        self.documents = []
        self.construit_le = 0.0
        self.duree = 0.0
        self.erreurs = []

    @property
    def pret(self):
        return bool(self.documents)


def _slugs_des_activites(activites):
    """{slug de dossier ou de fiche: id d'activité}, du plus long au plus court.

    Une fiche de séance s'appelle `module-n5-logement-c1-la-visite-….html` :
    elle appartient à l'activité dont le slug **préfixe** son nom. On lit donc
    le disque plutôt que `data/materiel.json`, qui décrit la même chose mais
    peut être en retard d'une construction — et un index en retard perd
    silencieusement les fiches les plus récentes, c'est-à-dire celles qu'on
    cherche.
    """
    slugs = {}
    for a in activites:
        for cle in ("interactive", "parcours", "studentDoc"):
            m = re.match(r"assets/\w[\w-]*/([^/]+)/", a.get(cle) or "")
            if m:
                slugs.setdefault(m.group(1), a["id"])
        m = re.match(r"assets/documents/(.+?)-fiches-eleves\.html$",
                     a.get("studentDoc") or "")
        if m:
            slugs.setdefault(m.group(1), a["id"])
    return slugs


def construire(base_dir, activites, volume_dir=None):
    """Dépouille le disque et rend un index prêt à servir.

    Deux racines, et elles ne se valent pas — c'est la règle du serveur de
    fichiers, recopiée ici pour que la recherche voie exactement ce que l'écran
    ouvrira. `assets/interactive/` est servi depuis le **code** ; le reste
    depuis le **volume**, avec le code en filet. Une fiche déposée en ligne
    n'existe que sur le volume : l'oublier reviendrait à ne jamais trouver ce
    que l'enseignante vient d'ajouter.
    """
    debut = time.time()
    index = Index()
    base = Path(base_dir)
    volume = Path(volume_dir) if volume_dir else base
    slugs = _slugs_des_activites(activites)
    ordre = sorted(slugs, key=len, reverse=True)

    def ajouter(activite_id, type_, fichier, rel, titre_defaut, avec_scripts):
        try:
            titre, texte = texte_du_fichier(fichier, avec_scripts)
        except (OSError, UnicodeError) as e:
            index.erreurs.append("%s : %s" % (rel, e))
            return
        if len(texte) < 40:
            return
        index.documents.append({
            "activiteId": activite_id,
            "type": type_,
            "titre": titre or titre_defaut,
            "chemin": rel,
            "texte": texte,
            "plat": sans_accents(texte),
        })

    # 1. Le module lui-même : c'est là que sont les dialogues et les exercices.
    for a in activites:
        rel = a.get("parcours") or a.get("interactive") or ""
        if not rel:
            continue
        f = base / rel
        if f.is_file():
            ajouter(a["id"], "module", f, rel, a.get("title", ""), True)

    # 2. Les fiches : tout `assets/documents/*.html`, rattaché par son préfixe.
    fiches = {}
    for racine in (base, volume):
        dossier = racine / "assets" / "documents"
        if dossier.is_dir():
            for f in dossier.glob("*.html"):
                fiches[f.name] = f      # le volume passe en second : il gagne
    for nom, f in sorted(fiches.items()):
        tige = f.stem
        aid = next((slugs[s] for s in ordre
                    if tige == s or tige.startswith(s + "-")), None)
        if aid is None:
            continue   # une fiche qui n'appartient à rien n'est pas montrable
        ajouter(aid, "fiche", f, "assets/documents/" + nom, tige, False)

    index.duree = time.time() - debut
    index.construit_le = time.time()
    return index


# ────────────────────────── La recherche ──────────────────────────

# Les mots qui ne disent rien de ce qu'on cherche. Ils ne sont pas **exigés**
# d'un document — sans quoi « la visite du quatre et demie » rendrait tout
# module où traînent « la », « du » et « et » — mais ils comptent encore dans le
# score, et dans la phrase exacte, qui est la meilleure réponse possible.
VIDES = {
    "le", "la", "les", "un", "une", "des", "du", "de", "d", "l", "au", "aux",
    "et", "ou", "a", "en", "dans", "sur", "pour", "avec", "que", "qui", "quoi",
    "ce", "cet", "cette", "ces", "son", "sa", "ses", "mon", "ma", "mes", "est",
    "sont", "je", "tu", "il", "elle", "on", "nous", "vous", "ils", "elles",
    "ne", "pas", "plus", "y", "se", "s", "n", "c", "j", "me", "te", "par",
}

# Deux mots cherchés ensemble doivent se trouver **ensemble**. Sans cette
# borne, « visite » au début d'un module et « quatre » à la fin faisaient un
# résultat, et huit modules sans rapport remontaient devant la bonne fiche.
FENETRE = 220


def _position(plat, termes, exiges, phrase):
    """Où les mots se rencontrent dans ce document, ou `None` s'ils ne s'y
    rencontrent pas. C'est à la fois le filtre et l'ancre de l'extrait."""
    if phrase and len(termes) > 1:
        pos = plat.find(phrase)
        if pos >= 0:
            return pos
    if not all(t in plat for t in exiges):
        return None
    if len(exiges) < 2:
        return plat.find(exiges[0]) if exiges else 0
    # On part du mot le plus rare : c'est lui qui donne le moins d'endroits à
    # essayer, et le coût de la recherche suit ses occurrences, pas la taille
    # du document.
    rare = min(exiges, key=lambda t: plat.count(t))
    autres = [t for t in exiges if t != rare]
    depart = plat.find(rare)
    while depart >= 0:
        debut, fin = max(0, depart - FENETRE), depart + FENETRE
        coin = plat[debut:fin]
        if all(t in coin for t in autres):
            return depart
        depart = plat.find(rare, depart + 1)
    return None


def _extrait(document, pos):
    """Le passage à montrer : autour de l'endroit où les mots se rencontrent,
    jamais le début du document — sinon toutes les fiches montreraient leur
    en-tête, c'est-à-dire rien qui les distingue."""
    debut = max(0, pos - EXTRAIT_AVANT)
    fin = min(len(document["texte"]), pos + EXTRAIT_APRES)
    # `texte` et `plat` ont la même longueur : la normalisation ne retire que
    # des diacritiques combinants, jamais un caractère de base. Les positions
    # valent donc pour les deux — sans quoi l'extrait glisserait d'un cran par
    # accent rencontré, et se couperait au milieu d'un mot.
    morceau = document["texte"][debut:fin].strip()
    return ("…" if debut else "") + morceau + ("…" if fin < len(document["texte"]) else "")


def _score(document, termes, pos, phrase):
    plat = document["plat"]
    points = sum(min(plat.count(t), 5) for t in termes)
    if phrase and len(termes) > 1 and phrase in plat:
        points += 25          # la phrase entière : c'est ce qu'on cherchait
    titre = sans_accents(document["titre"])
    if all(t in titre for t in termes):
        points += 15          # le titre d'une fiche dit ce qu'elle est
    if document["type"] == "module":
        points += 2           # à égalité, le module avant sa fiche
    return points


def mots_pleins(requete):
    """Les mots qui portent la recherche — ceux qu'on surligne à l'écran.

    Rendus au client plutôt que recalculés par lui : la liste des mots vides
    est une règle, et deux exemplaires d'une règle finissent par diverger. La
    page surlignerait « la » et « du » dans un extrait, ce qui revient à
    surligner la moitié de la phrase.
    """
    termes = [t for t in sans_accents(requete).split() if t]
    return [t for t in termes if t not in VIDES and len(t) > 1] or termes


def chercher(index, requete, activites_permises=None, maxi=40, par_activite=3):
    """Les activités dont le contenu répond, la plus parlante d'abord.

    `activites_permises` est **le bornage**, et il se pose ici : la recherche
    ne doit pas faire découvrir un module d'un niveau que la personne n'a pas
    le droit de voir. Une recherche qui rendrait le titre, ou même seulement le
    nombre, apprendrait ce qu'il y a derrière la porte.
    """
    termes = [t for t in sans_accents(requete).split() if t]
    if not termes or not index.pret:
        return []
    phrase = " ".join(termes)
    # Les mots pleins sont exigés ; les mots vides ne le sont que s'il n'y a
    # qu'eux — « je me lance » est une recherche légitime.
    exiges = mots_pleins(requete)
    par_activite_dict = {}
    for doc in index.documents:
        if activites_permises is not None and doc["activiteId"] not in activites_permises:
            continue
        pos = _position(doc["plat"], termes, exiges, phrase)
        if pos is None:
            continue
        points = _score(doc, termes, pos, phrase)
        par_activite_dict.setdefault(doc["activiteId"], []).append((points, pos, doc))

    resultats = []
    for aid, trouves in par_activite_dict.items():
        trouves.sort(key=lambda p: -p[0])
        resultats.append({
            "activiteId": aid,
            "score": trouves[0][0],
            "total": len(trouves),
            "extraits": [{
                "type": doc["type"],
                "titre": doc["titre"],
                "chemin": doc["chemin"],
                "extrait": _extrait(doc, pos),
            } for _, pos, doc in trouves[:par_activite]],
        })
    resultats.sort(key=lambda r: (-r["score"], -r["total"]))
    return resultats[:maxi]


# ───────────────── Le service : un seul index, construit une fois ─────────────

_INDEX = Index()
_VERROU = threading.Lock()
_EN_COURS = False


def index_courant():
    return _INDEX


def construire_en_fond(base_dir, charger_activites, volume_dir=None):
    """Construit l'index dans un fil, sans jamais faire échouer l'appelant.

    Le serveur démarre avec un healthcheck : dix secondes de dépouillement dans
    le fil principal le feraient rater. Et une erreur ici ne doit pas tuer le
    démarrage — la recherche dans le contenu est un service de plus, pas une
    condition pour que la classe travaille.
    """
    global _EN_COURS
    with _VERROU:
        if _EN_COURS or _INDEX.pret:
            return
        _EN_COURS = True

    def travail():
        global _INDEX, _EN_COURS
        try:
            index = construire(base_dir, charger_activites(), volume_dir)
            _INDEX = index
            print("[recherche] %d documents dépouillés en %.1f s"
                  % (len(index.documents), index.duree), flush=True)
            if index.erreurs:
                print("[recherche] %d fichier(s) illisible(s)" % len(index.erreurs),
                      flush=True)
        except Exception as e:            # noqa: BLE001 — voir le docstring
            print("[recherche] index non construit : %r" % e, flush=True)
        finally:
            _EN_COURS = False

    threading.Thread(target=travail, daemon=True).start()


def etat():
    return {
        "pret": _INDEX.pret,
        "documents": len(_INDEX.documents),
        "modules": sum(1 for d in _INDEX.documents if d["type"] == "module"),
        "fiches": sum(1 for d in _INDEX.documents if d["type"] == "fiche"),
        "duree": round(_INDEX.duree, 1),
        "erreurs": len(_INDEX.erreurs),
    }


if __name__ == "__main__":
    import sys
    racine = Path(__file__).resolve().parent
    activites = json.loads((racine / "data" / "activities.json").read_text("utf-8"))
    idx = construire(racine, activites)
    print("%d documents (%d modules, %d fiches) en %.1f s, %d illisible(s)" % (
        len(idx.documents),
        sum(1 for d in idx.documents if d["type"] == "module"),
        sum(1 for d in idx.documents if d["type"] == "fiche"),
        idx.duree, len(idx.erreurs)))
    if len(sys.argv) > 1:
        for r in chercher(idx, " ".join(sys.argv[1:]))[:10]:
            print("\n#%s (%d)" % (r["activiteId"], r["score"]))
            for e in r["extraits"]:
                print("   %-6s %s\n          %s" % (e["type"], e["titre"], e["extrait"]))
