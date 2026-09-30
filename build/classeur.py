#!/usr/bin/env python3
"""Le classement du classeur : étagère, chantier et état de chaque fiche.

POURQUOI CE SCRIPT EXISTE. Le 30 septembre 2026, le classeur portait 227
fiches sous 24 onglets qui mêlaient trois façons de classer — l'usage
(Présenter, Décider…), le projet (Hôtellerie, Compostelle…) et la pièce seule
(SimDEA, CV…). Le même chantier vivait sous deux ou trois onglets, et les tours
d'audit se rangeaient au même rang que les livrables. Daniel : « je m'y perds ».

La réponse retenue (proposition du 30 sept., recommandations acceptées) :
cinq ÉTAGÈRES — une par chantier —, un CHANTIER à l'intérieur de chacune, et
trois ÉTATS sur chaque fiche : en service, à trancher, travail (replié).

Ce script fait le PREMIER CLASSEMENT, pour que Daniel le corrige avant qu'on
l'applique. Il ne touche pas à la page :

    python3 build/classeur.py --releve > classement.json   # la proposition
    python3 build/classeur.py --texte                      # la même, en clair

L'état est DEVINÉ sur le titre et le texte de la fiche : c'est une proposition
à corriger, pas un verdict. L'étagère et le chantier, eux, se déduisent de la
famille d'origine — sauf les exceptions nommées dans `EXCEPTIONS`, une par
fiche, écrites à la main parce qu'aucune règle ne les attrape.
"""
import json
import pathlib
import re
import sys
import unicodedata

PAGE = pathlib.Path(__file__).resolve().parent.parent / "presentations.html"

ETAGERES = [
    ("francis", "francis"),
    ("formations", "Formations en entreprise"),
    ("portfolio", "Portfolio"),
    ("voyage", "Voyage"),
    ("maison", "La maison"),
]
ETATS = [("service", "En service"), ("trancher", "À trancher"), ("travail", "Travail")]

# Famille d'origine → (étagère, chantier). Le chantier est le sous-onglet.
FAMILLES = {
    "presenter": ("francis", "Présenter"),
    "decider": ("francis", "Décider"),
    "suivre": ("francis", "Suivre"),
    "comprendre": ("francis", "Comprendre"),
    "loi25": ("francis", "Loi 25"),
    "hotellerie": ("formations", "Hôtel Rive-Claire"),
    "francoeur": ("formations", "Maison Francœur"),
    "entreprise": ("maison", "Structure"),
    "compostelle": ("voyage", "Compostelle"),
    "montreal": ("voyage", "Montréal en poche"),
    "simdea": ("portfolio", "SimDEA"),
    "defibrillateur": ("portfolio", "SimDEA"),
    "barista": ("portfolio", "Barista"),
    "avant-louverture": ("portfolio", "Barista"),
    "barista-graphique": ("portfolio", "Barista"),
    "courriel": ("portfolio", "Le courriel de trop"),
    "bougies": ("portfolio", "À la main d'abord"),
    "plaquettes": ("portfolio", "Le dernier millimètre"),
    "cv": ("portfolio", "Vitrine"),
    "portfolio": ("portfolio", "Prototypes"),
    "prototype": ("portfolio", "Prototypes"),
    "boucle": ("portfolio", "Boucle"),
}

# Les fiches qu'aucune règle de famille ne range bien. Clé : début du titre
# aplati (sans accents ni casse). Valeur : (étagère, chantier) — l'un ou
# l'autre peut être None pour garder celui de la famille.
EXCEPTIONS = {
    # Décider → la maison : ce sont des décisions d'entreprise, pas de plateforme.
    "vendre au public sans s'exposer": ("maison", "Vente"),
    "l'assurance responsabilite": ("maison", "Structure"),
    # Entreprise → formations : des trousses de métier, comme Francœur.
    "quatre situations de travail": ("formations", "Belrive"),
    "huit heures chez belrive": ("formations", "Belrive"),
    "le bloc 3, jouable": ("formations", "Belrive"),
    "le diagnostic didactique": ("formations", "Belrive"),
    "le procedurier": ("formations", "Belrive"),
    "bloc a": ("formations", "Chaussures"),
    "un module pour la vente de chaussures": ("formations", "Chaussures"),
    "banc de registres": ("formations", "Chaussures"),
    "vendre en francais, au comptoir": ("formations", "Chaussures"),
    "le depliant de demarchage": ("formations", "Démarchage"),
    # Entreprise → la maison, rangée par sujet.
    "le marche, verifie": ("maison", "Vente"),
    "le plan d'affaires": ("maison", "Vente"),
    "la strategie de communication": ("maison", "Vente"),
    "trame": ("maison", "Identité"),
    "le banc d'essai des habillages": ("maison", "Identité"),
    # Portfolio : la vitrine de Daniel à part des prototypes.
    "braise": ("portfolio", "Vitrine"),
    "se mettre en marche": ("portfolio", "Vitrine"),
}

# L'état, deviné. Les motifs se lisent sur le titre aplati.
TRAVAIL_TITRE = [
    r"\baudit\b", r"\btour \d", r"\bplanche\b", r"^prompts?\b", r"comparaison",
    r"reprises de voix", r"lettres (epelees|a reprendre)", r"noms epeles",
    r"\bbruits\b", r"ce qui reste faux", r"chuchotements", r"premiere tentative",
    r"au banc d'essai", r"\bv[23]\b", r"^tri des", r"trois ouvertures",
    r"quelle voix", r"une seule personne", r"version comblee",
    r"le croquis, la voix", r"faire tenir la formation", r"contre-epreuve",
    r"^quatre-vingt-dix secondes", r"^sept cicatrices", r"^la chambre$",
    r"^le repartiteur$", r"^les mains$", r"^la cohorte$", r"^vous\.?$",
    r"storyline .vous", r"ont vieilli", r"^menage du depot",
    r"deux grammaires", r"^le titre des depliants",
]
# Une fiche « à trancher » dit qu'elle attend une réponse, et ne dit pas
# qu'elle l'a reçue.
ATTEND = re.compile(
    r"a valider|a confirmer|a trancher|a cocher|attend(ent)? (votre|ta|ton|vos|tes)"
    r"|(votre|ton|ta) (choix|decision|jugement|reponse)|a retenir ou a ecarter"
    r"|proposition\b|en attente|reste a decider|deux voies|trois voies")
REPONDU = re.compile(
    r"\bdecide|\btranche\b|choix de daniel|\bretenue?s?\b|\blivree?s?\b|\bvalidee?s?\b"
    r"|\bapplique(e|es)?\b|\bfait\b|integree? depuis|sortie de boucle|\brendues?\b")

# L'état que le texte ne dit pas, mais que la suite du chantier dit : un plan
# ou un cadrage « à valider » dont les étapes suivantes existent a été validé.
ETAT_EXCEPTIONS = {
    "la reception d'hotel, en trois langues": "service",
    "en route vers compostelle — le plan": "service",
    "maison francœur — le lexique a valider": "service",
    # Corrections de Daniel sur le premier classement (30 sept. 2026).
    "teaser — animatique de 48 s": "service",
    "application ou navigateur": "service",
    "le courriel aux directions": "service",
    "planifier — proposition pour l'administration": "service",
    "travailler avec claude": "service",
}


def plat(t):
    t = unicodedata.normalize("NFD", t.lower().replace("’", "'"))
    return "".join(c for c in t if unicodedata.category(c) != "Mn")


def texte(html):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)).strip()


def fiches(page=PAGE):
    """Chaque fiche avec sa famille d'origine, dans l'ordre de la page."""
    s = page.read_text(encoding="utf-8")
    bornes = [(m.start(), m.group(1)) for m in
              re.finditer(r'<section class="famille[^"]*" data-fam="([^"]+)"', s)]
    bornes.append((len(s), None))
    vus = {}
    for (a, fam), (b, _) in zip(bornes, bornes[1:]):
        for m in re.finditer(r'<article class="fiche".*?</article>', s[a:b], re.S):
            art = m.group(0)
            h3 = re.search(r"<h3[^>]*>(.*?)</h3>", art, re.S)
            titre = texte(h3.group(1)) if h3 else "(sans titre)"
            quoi = re.search(r'<p class="quoi">(.*?)</p>', art, re.S)
            date = re.search(r'<span class="date">(.*?)</span>', art)
            lien = re.search(r'class="btn[^"]*" href="([^"]+)"', art) or \
                re.search(r'href="([^"#]+)"', art)
            base = re.sub(r"[^a-z0-9]+", "-", plat(titre)).strip("-")[:48] or "fiche"
            vus[base] = vus.get(base, 0) + 1
            ident = base if vus[base] == 1 else "%s-%d" % (base, vus[base])
            yield {
                "id": ident, "famille": fam, "titre": titre,
                "date": texte(date.group(1)) if date else "",
                "lien": lien.group(1) if lien else "",
                "resume": texte(quoi.group(1))[:260] if quoi else "",
                "_texte": texte(art),
            }


def proposer(f):
    etagere, chantier = FAMILLES[f["famille"]]
    t = plat(f["titre"])
    for debut, (e, c) in EXCEPTIONS.items():
        if t.startswith(debut):
            etagere, chantier = e or etagere, c or chantier
            break
    corps = plat(f["_texte"])
    force = next((e for d, e in ETAT_EXCEPTIONS.items() if t.startswith(d)), None)
    if force:
        etat, pourquoi = force, "la suite du chantier dit que c'est tranché"
    elif any(re.search(p, t) for p in TRAVAIL_TITRE):
        etat, pourquoi = "travail", "document de travail (titre)"
    elif ATTEND.search(corps) and not REPONDU.search(corps):
        etat, pourquoi = "trancher", "attend une réponse, sans dire qu'elle l'a reçue"
    else:
        etat, pourquoi = "service", "par défaut"
    return {"etagere": etagere, "chantier": chantier, "etat": etat, "pourquoi": pourquoi}


def releve():
    out = []
    for f in fiches():
        f.update(proposer(f))
        f.pop("_texte")
        out.append(f)
    return out


# ── L'application : une seule fois, le 30 septembre 2026 ─────────────────
# Après elle, l'étagère et le chantier se lisent dans la PAGE (la section et
# le bloc où la fiche est rangée) et l'état sur la fiche (`data-etat`). Les
# devinettes ci-dessus ne servent plus : une fiche neuve se range à la main,
# et `build/controles/classeur.py` vérifie qu'elle l'a été.

# (clé, eyebrow, titre, chapeau, anciennes familles) — dans l'ordre d'affichage.
TETES = {
    "francis": ("La plateforme", "francis",
                "La plateforme de francisation, pour les centres : ce qu'on présente, "
                "ce qu'on décide, ce qu'on suit, ce qu'il faut comprendre, et la Loi 25.", ""),
    "formations": ("Pour les employeurs", "Formations en entreprise",
                   "Les trousses de français pour un métier, vendues aux employeurs. "
                   "Une par client ou par métier, dans l'ordre où elles se construisent.",
                   ""),
    "portfolio": ("Pour le portfolio", "Portfolio",
                  "Le métier de concepteur pédagogique, hors francisation : simulateurs, "
                  "prototypes, CV. En tête de chaque pièce, la dernière version ; les "
                  "audits et les essais sont dans le travail.", ""),
    "voyage": ("Grand public", "Voyage",
               "Les applications de voyage vendues par code : on les achète, on les "
               "garde dans son téléphone.", ""),
    "maison": ("L'entreprise", "La maison",
               "L'entreprise elle-même : sa forme, sa vente, son identité.", "entreprise"),
}

# étagère → [(clé du chantier, titre affiché, chapeau ou famille d'origine dont
# on reprend le chapeau, anciennes familles, blocs engendrés)]
CHANTIERS = {
    "francis": [
        ("presenter", "Présenter", "=presenter", "presenter", []),
        ("decider", "Décider", "Les pages qui appellent une réponse : un tri à faire, "
         "une proposition à retenir ou à écarter, un plan à valider.", "decider", []),
        ("suivre", "Suivre", "=suivre", "suivre", []),
        ("comprendre", "Comprendre", "=comprendre", "comprendre", []),
        ("loi25", "Loi 25", "=loi25", "loi25", []),
    ],
    "formations": [
        ("rive-claire", "Hôtel Rive-Claire", "=hotellerie", "hotellerie", []),
        ("francoeur", "Maison Francœur", "=francoeur", "francoeur", []),
        ("belrive", "Belrive", "La première trousse, pour une usine : les situations "
         "de travail, le déroulé de la journée, le bloc jouable, le diagnostic et le "
         "procédurier.", "", []),
        ("chaussures", "Chaussures", "Vendre des chaussures en français : le cadrage, "
         "le premier bloc, l'écran du jeu de rôle.", "", []),
        ("demarchage", "Démarchage", "Ce qu'on laisse à un employeur pour ouvrir la "
         "porte.", "", []),
    ],
    "portfolio": [
        ("simdea", "SimDEA", "La formation au défibrillateur, le simulateur et la pièce "
         "« Vous. ». Le lien du haut est la dernière version ; sa date est celle où la "
         "page servie a changé.", "simdea defibrillateur", ["SIMDEA"]),
        ("barista", "Barista", "Avant l'ouverture : la tournée de la machine en 3D, "
         "puis le jeu où l'on trouve la panne.",
         "barista avant-louverture barista-graphique",
         ["BARISTA", "AVANT-LOUVERTURE", "BARISTA-GRAPHIQUE"]),
        ("courriel", "Le courriel de trop", "=courriel", "courriel", ["COURRIEL"]),
        ("bougies", "À la main d'abord", "=bougies", "bougies", ["BOUGIES"]),
        ("plaquettes", "Le dernier millimètre", "=plaquettes", "plaquettes", ["PLAQUETTES"]),
        ("prototypes", "Prototypes", "=prototype", "prototype", []),
        ("boucle", "Boucle", "=boucle", "boucle", []),
        ("vitrine", "Vitrine", "Le CV, la stratégie pour se mettre en marché, et le "
         "système de design Braise.", "cv", ["CV"]),
    ],
    "voyage": [
        ("compostelle", "En route vers Compostelle", "=compostelle", "compostelle", []),
        ("montreal", "Montréal en poche", "=montreal", "montreal", []),
    ],
    "maison": [
        ("structure", "Structure", "La forme de l'entreprise : incorporation, nom, "
         "assurance, Loi 25 côté entreprises.", "", []),
        ("vente", "Vente", "Le marché, le plan d'affaires, la communication et les "
         "conditions de vente.", "", []),
        ("identite", "Identité", "Trame, le système de design de la maison, et son banc "
         "d'essai.", "", []),
    ],
}
ORDRE_ETAT = {"service": 0, "trancher": 1, "travail": 2}


def appliquer():
    s = PAGE.read_text(encoding="utf-8")
    classes = releve()
    # 1. Les fiches, rangées par (étagère, titre du chantier), avec leur état.
    arts = []
    for m in re.finditer(r'<section class="famille" data-fam="([^"]+)">', s):
        fin = s.find('<section class="famille"', m.end())
        fin = fin if fin > 0 else s.index("</main>")
        for a in re.finditer(r'<article class="fiche".*?</article>', s[m.start():fin], re.S):
            arts.append(a.group(0))
    assert len(arts) == len(classes) == 227, (len(arts), len(classes))
    rang = {}
    for art, f in zip(arts, classes):
        assert f["titre"] in texte(art), f["titre"]
        rang.setdefault((f["etagere"], f["chantier"]), []).append((f, art))
    # Les chapeaux d'origine, repris tels quels quand un chantier en hérite.
    chapeaux = {m.group(1): m.group(2).strip() for m in re.finditer(
        r'<section class="famille" data-fam="([^"]+)">\s*<div class="tete">.*?'
        r'<h2>.*?</h2>\s*<p>(.*?)</p>', s, re.S)}
    # Les blocs engendrés par portfolio-conception/onglets_simulateurs.py.
    blocs = {}
    for m in re.finditer(r'<!--<<FAMILLE-([A-Z-]+)>>-->(.*?)<!--<</FAMILLE-\1>>-->', s, re.S):
        blocs[m.group(1)] = m.group(2)
    titres_engendres = set()
    for b in blocs.values():
        titres_engendres |= {texte(t) for t in re.findall(r'<h3 class="titre">(.*?)</h3>', b, re.S)}

    def marquer(art, etat):
        return art.replace('<article class="fiche"', '<article class="fiche" data-etat="%s"' % etat, 1)

    def fiches_de(titre_ch, etagere):
        lot = rang.pop((etagere, titre_ch), [])
        lot.sort(key=lambda x: ORDRE_ETAT[x[0]["etat"]])     # tri stable
        return [marquer(a, f["etat"]) for f, a in lot if f["titre"] not in titres_engendres]

    def bloc_engendre(nom):
        b = blocs[nom]
        # Ne garder que les fiches : la section, sa tête et son chapeau
        # disparaissent — le chantier porte le sien.
        out = []
        for a in re.findall(r'<article class="fiche".*?</article>', b, re.S):
            t = texte(re.search(r'<h3 class="titre">(.*?)</h3>', a, re.S).group(1))
            etat = next(f["etat"] for f in classes if f["titre"] == t)
            out.append("        " + marquer(a.strip(), etat))
        return "<!--<<FAMILLE-%s>>-->\n%s\n        <!--<</FAMILLE-%s>>-->" % (
            nom, "\n".join(out), nom)

    etageres = []
    for e, (eyebrow, h2, chapeau, anciens) in TETES.items():
        h = ['    <section class="famille" data-fam="%s"%s>' % (
                e, ' data-anciens="%s"' % anciens if anciens else ""),
             '      <div class="tete">',
             '        <span class="eyebrow e-teal">%s</span>' % eyebrow,
             '        <h2>%s</h2>' % h2,
             '        <p>%s</p>' % chapeau,
             '      </div>']
        for cle, titre, ch, anc, engendres in CHANTIERS[e]:
            ch = chapeaux[ch[1:]] if ch.startswith("=") else ch
            h += ['      <div class="chantier" data-chantier="%s"%s>' % (
                     cle, ' data-anciens="%s"' % anc if anc else ""),
                  '        <div class="ch-tete"><h3 class="ch-titre">%s</h3>' % titre,
                  '          <p>%s</p></div>' % ch,
                  '        <div class="liste">']
            for n in engendres:
                h.append("        " + bloc_engendre(n))
            h += ["\n" + a for a in fiches_de(titre if titre != "En route vers Compostelle"
                                              else "Compostelle", e)]
            h += ['        </div>', '      </div>']
        h.append('    </section>')
        etageres.append("\n".join(h))
    # Les fiches rangées sous un titre de chantier qui ne correspond à aucun bloc
    # seraient perdues : on refuse plutôt.
    reste = {k: v for k, v in rang.items() if v and any(f["titre"] not in titres_engendres for f, _ in v)}
    assert not reste, sorted(reste)

    # 2. Remplacer la zone des familles, en gardant « vide » et la note.
    debut = s.index("    <!-- ══════════ PRÉSENTER")
    fin_main = s.index("</main>")
    fin = s.rindex("</section>", 0, fin_main) + len("</section>")
    vide = re.search(r'<p class="vide" id="vide">.*?</p>', s).group(0)
    note = re.search(r'<div class="note">.*?</div>', s, re.S).group(0)
    neuf = ("    <!-- Cinq étagères, une par chantier (réorganisation du 30 septembre\n"
            "         2026). Une fiche vit dans le bloc .chantier de son projet et porte\n"
            "         son état : data-etat = service · trancher · travail. Le travail est\n"
            "         replié à l'écran ; la recherche le trouve quand même. Contrôle :\n"
            "         python3 build/controles/classeur.py -->\n"
            + "\n\n".join(etageres) + "\n\n    " + vide + "\n\n    " + note)
    s = s[:debut] + neuf + s[fin:]
    PAGE.write_text(s, encoding="utf-8")
    n = len(re.findall(r'<article class="fiche"', s))
    print("  %d fiches rangées dans %d étagères" % (n, len(etageres)))
    assert n == 227


def main(argv):
    if "--appliquer" in argv:
        appliquer()
        return 0
    r = releve()
    if "--texte" in argv:
        for e, nom in ETAGERES:
            lot = [f for f in r if f["etagere"] == e]
            print("\n%s — %d" % (nom, len(lot)))
            for f in sorted(lot, key=lambda f: (f["chantier"], f["etat"])):
                print("  %-22s %-9s %s" % (f["chantier"][:22], f["etat"], f["titre"][:70]))
        return 0
    json.dump(r, sys.stdout, ensure_ascii=False, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
