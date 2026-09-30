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


def main(argv):
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
