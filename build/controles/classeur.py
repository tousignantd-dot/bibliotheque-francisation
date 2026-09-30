#!/usr/bin/env python3
"""Le contrôle du classeur (`presentations.html`), rangé par chantier.

Depuis le 30 septembre 2026, le classeur a CINQ étagères (francis, formations,
portfolio, voyage, maison), des chantiers dans chacune, et un état sur chaque
fiche (`data-etat` : service · trancher · travail). Les 24 onglets d'avant
étaient nés un chantier à la fois, chacun ajouté sans que personne refasse le
rangement ; ce contrôle est ce qui empêche la même pente.

Il n'écrit rien et sort en code 1 au premier écart :

    python3 build/controles/classeur.py          # contrôle
    python3 build/controles/classeur.py --etat   # + l'inventaire à l'écran

Ce qu'il attrape, et qui ne lève aucune erreur à l'écran :
  - une fiche posée hors d'un chantier (elle ne s'afficherait sous aucun filtre
    de chantier, et le script de la page la perdrait) ;
  - une fiche sans état, ou avec un état inconnu ;
  - une étagère de plus que les cinq, ou un onglet de premier niveau qui ne
    correspond à aucune étagère — le chemin par lequel on est arrivé à 24 ;
  - un chantier vide, ou deux chantiers de même clé ;
  - un lien relatif qui pointe dans le vide, sur une fiche en service ou à
    trancher (le travail replié n'est pas vérifié : il documente le passé).
"""
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parents[2]
PAGE = RACINE / "presentations.html"
ETAGERES = ["francis", "formations", "portfolio", "voyage", "maison"]
ETATS = {"service", "trancher", "travail"}


def main(argv):
    s = PAGE.read_text(encoding="utf-8")
    ecarts = []
    main_ = s[s.index("<main>"):s.index("</main>")]

    fams = [(m.group(1), m.start()) for m in
            re.finditer(r'<section class="famille" data-fam="([^"]+)"', main_)]
    noms = [f for f, _ in fams]
    if noms != ETAGERES:
        ecarts.append("étagères %s — attendu %s" % (noms, ETAGERES))
    onglets = re.findall(r'<button type="button" class="onglet" data-f="([^"]+)"', s)
    if onglets != ["tout"] + ETAGERES:
        ecarts.append("onglets de premier niveau %s — un chantier neuf va DANS une "
                      "étagère, il n'ajoute pas d'onglet" % onglets)

    total = sum(1 for _ in re.finditer(r'<article class="fiche"', main_))
    bornes = fams + [("", len(main_))]
    vues, cles = 0, {}
    inventaire = []
    for (fam, a), (_, b) in zip(bornes, bornes[1:]):
        sec = main_[a:b]
        chs = [(m.group(1), m.start()) for m in
               re.finditer(r'<div class="chantier" data-chantier="([^"]+)"', sec)]
        avant = sec[:chs[0][1]] if chs else sec
        if '<article class="fiche"' in avant:
            ecarts.append("%s : fiche posée hors d'un chantier" % fam)
        for (ch, c1), (_, c2) in zip(chs, chs[1:] + [("", len(sec))]):
            if ch in cles:
                ecarts.append("chantier « %s » en double (%s et %s)" % (ch, cles[ch], fam))
            cles[ch] = fam
            arts = re.findall(r'<article class="fiche"[^>]*>.*?</article>', sec[c1:c2], re.S)
            if not arts:
                ecarts.append("%s › %s : chantier vide" % (fam, ch))
            compte = {e: 0 for e in ETATS}
            for art in arts:
                vues += 1
                titre = re.search(r"<h3[^>]*>(.*?)</h3>", art, re.S)
                titre = re.sub(r"<[^>]+>", "", titre.group(1)).strip() if titre else "?"
                e = re.search(r'data-etat="([^"]*)"', art.split(">", 1)[0])
                if not e or e.group(1) not in ETATS:
                    ecarts.append("%s › %s : « %s » sans état valable" % (fam, ch, titre))
                    continue
                compte[e.group(1)] += 1
                if e.group(1) == "travail":
                    continue
                for href in re.findall(r'<a class="btn[^"]*" href="([^"#?]+)', art):
                    if re.match(r"[a-z]+:", href):
                        continue
                    if not (RACINE / href).exists():
                        ecarts.append("%s › %s : « %s » pointe dans le vide (%s)"
                                      % (fam, ch, titre, href))
            inventaire.append((fam, ch, compte))
    if vues != total:
        ecarts.append("%d fiches dans la page, %d rangées dans un chantier" % (total, vues))

    if "--etat" in argv:
        for fam in ETAGERES:
            lot = [(ch, c) for f, ch, c in inventaire if f == fam]
            print("\n%s — %d fiches" % (fam, sum(sum(c.values()) for _, c in lot)))
            for ch, c in lot:
                print("  %-14s %3d en service · %2d à trancher · %2d travail"
                      % (ch, c["service"], c["trancher"], c["travail"]))
        print()
    for e in ecarts:
        print("  ÉCART  " + e)
    if ecarts:
        return 1
    print("  classeur : %d fiches, %d étagères, %d chantiers — aucun écart"
          % (total, len(ETAGERES), len(cles)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
