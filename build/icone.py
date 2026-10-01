#!/usr/bin/env python3
"""Le jeu d'icônes du projet : Tabler (contour), 5 166 icônes, licence MIT.

    python3 build/icone.py --chercher maison          # noms, catégories, étiquettes
    python3 build/icone.py home                       # le SVG, prêt à coller
    python3 build/icone.py home --trait 2.2 --taille 20
    python3 build/icone.py home phone mail --dossier assets/presentations/x/icones

POURQUOI. Claude dessine mal les icônes, et chaque pièce du portfolio en
inventait de nouvelles, au trait inégal. Décision du 30 septembre 2026 : ne
jamais dessiner une icône, les prendre toutes dans UN jeu. Tabler a été choisi
pour son trait arrondi sur grille 24, le même que les tracés du système.

Le jeu vit dans assets/design-system/tabler/ en deux fichiers compacts plutôt
qu'en 5 166 SVG : tabler-outline.json (les tracés) et tabler-index.json
(catégorie et étiquettes, pour chercher). LICENSE doit rester à côté.

Le SVG sort en `stroke="currentColor"` : il prend la couleur du texte, donc les
jetons de la page. Par défaut le trait est à 2,2, celui des icônes du système ;
Tabler le livre à 2. Le portail garde ses propres tracés (barre d'outils) :
ce jeu sert partout ailleurs — pièces, trousses, pages de décision.
"""
import json
import pathlib
import sys
import unicodedata

RACINE = pathlib.Path(__file__).resolve().parent.parent
JEU = RACINE / "assets" / "design-system" / "tabler"


def charger():
    traces = json.loads((JEU / "tabler-outline.json").read_text(encoding="utf-8"))
    index = json.loads((JEU / "tabler-index.json").read_text(encoding="utf-8"))
    return traces, index


def plat(t):
    return "".join(c for c in unicodedata.normalize("NFD", t.lower()) if unicodedata.category(c) != "Mn")


def svg(nom, traces, trait=2.2, taille=24):
    if nom not in traces:
        raise KeyError(nom)
    enfants = []
    for balise, attrs in traces[nom]:
        a = " ".join('%s="%s"' % (k, str(v).replace('"', "&quot;")) for k, v in attrs.items())
        enfants.append("<%s %s/>" % (balise, a))
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="%s" height="%s" viewBox="0 0 24 24" '
            'fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" '
            'stroke-linejoin="round" aria-hidden="true" class="ic ic-%s">%s</svg>'
            % (taille, taille, trait, nom, "".join(enfants)))


def chercher(mot, index):
    m = plat(mot)
    trouves = [(0 if m == n else 1 if m in n else 2, n) for n, (cat, tags) in index.items()
               if m in n or m in plat(cat) or any(m in plat(t) for t in tags)]
    return [n for _, n in sorted(trouves)]


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    traces, index = charger()
    if argv[0] == "--chercher":
        # Les étiquettes sont en anglais : « maison » ne trouve rien, « home » oui.
        for n in chercher(" ".join(argv[1:]), index)[:40]:
            print("%-32s %s" % (n, index[n][0]))
        return 0
    trait, taille, dossier, noms = 2.2, 24, None, []
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--trait":
            trait = float(argv[i + 1]); i += 2; continue
        if a == "--taille":
            taille = int(argv[i + 1]); i += 2; continue
        if a == "--dossier":
            dossier = pathlib.Path(argv[i + 1]); i += 2; continue
        noms.append(a); i += 1
    manque = [n for n in noms if n not in traces]
    if manque:
        for n in manque:
            proches = chercher(n, index)[:5]
            print("Inconnue : %s%s" % (n, (" — essayer : " + ", ".join(proches)) if proches else ""), file=sys.stderr)
        return 1
    for n in noms:
        s = svg(n, traces, trait, taille)
        if dossier:
            dossier.mkdir(parents=True, exist_ok=True)
            (dossier / (n + ".svg")).write_text(s + "\n", encoding="utf-8")
            print("Écrit :", dossier / (n + ".svg"))
        else:
            print(s)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
