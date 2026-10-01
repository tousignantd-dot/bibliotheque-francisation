#!/usr/bin/env python3
"""Le système de design en UN fichier, pour les pages qui veulent s'afficher vite.

    python3 build/styles_bundle.py             # écrit assets/design-system/styles.bundle.css
    python3 build/styles_bundle.py --verifier  # code 1 si le paquet est en retard sur ses sources

POURQUOI. `styles.css` n'est fait que d'`@import` : le navigateur ne découvre
les seize feuilles qu'après l'avoir reçu, et `tokens/fonts.css` n'appelle
Google qu'après avoir été reçue elle-même — trois allers-retours en série avant
le premier affichage, relevés par l'audit du portail élève (1er oct. 2026).

Ce script suit les `@import` de `styles.css` dans l'ordre, recopie chaque
feuille à la suite, et réécrit ses `url()` relatives pour qu'elles restent
justes depuis `assets/design-system/`. **Il ne change rien au système** :
`styles.css` reste le point d'entrée de référence, et les feuilles sources ne
sont pas touchées. La seule chose qui reste dehors est l'`@import` vers
Google : une page qui sert des alphabets hors du latin (langue d'appui en
ukrainien) le charge elle-même, sans bloquer — voir eleve.html.

Le paquet est un fichier PRODUIT : ne jamais l'éditer à la main. Le relancer
après toute modification d'une feuille du système (le contrôle le dit).
"""
import pathlib
import posixpath
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
DS = RACINE / "assets" / "design-system"
ENTREE = DS / "styles.css"
SORTIE = DS / "styles.bundle.css"

IMPORT = re.compile(r'@import\s+url\(\s*["\']?([^"\')]+)["\']?\s*\)\s*;')
URL = re.compile(r'url\(\s*(["\']?)([^"\')]+)\1\s*\)')


def externe(chemin):
    return re.match(r"^(https?:)?//|^data:", chemin) is not None


def recopier(feuille, deja):
    """Le contenu de `feuille`, imports suivis, url() ramenées à la racine du système."""
    if feuille in deja:
        return ""
    deja.add(feuille)
    dossier = feuille.parent
    texte = feuille.read_text(encoding="utf-8")

    def sur_url(m):
        guillemet, cible = m.group(1), m.group(2)
        if externe(cible) or cible.startswith("/") or cible.startswith("#"):
            return m.group(0)
        absolu = (dossier / cible).resolve()
        rel = posixpath.relpath(absolu.as_posix(), DS.resolve().as_posix())
        return "url(%s%s%s)" % (guillemet, rel, guillemet)

    morceaux, pos = [], 0
    for m in IMPORT.finditer(texte):
        morceaux.append(URL.sub(sur_url, texte[pos:m.start()]))
        cible = m.group(1)
        if externe(cible):
            morceaux.append("/* @import externe retiré du paquet : %s */" % cible)
        else:
            sous = (dossier / cible).resolve()
            morceaux.append("\n/* ── %s ── */\n" % posixpath.relpath(sous.as_posix(), DS.resolve().as_posix()))
            morceaux.append(recopier(sous, deja))
        pos = m.end()
    morceaux.append(URL.sub(sur_url, texte[pos:]))
    return "".join(morceaux)


def produire():
    corps = recopier(ENTREE.resolve(), set())
    tete = ("/* styles.bundle.css — PRODUIT par build/styles_bundle.py à partir de styles.css.\n"
            "   Ne pas éditer : modifier les feuilles sources, puis relancer le script. */\n")
    return tete + corps


def main(argv):
    neuf = produire()
    if "--verifier" in argv:
        actuel = SORTIE.read_text(encoding="utf-8") if SORTIE.exists() else ""
        if actuel != neuf:
            print("styles.bundle.css est en retard sur ses sources : python3 build/styles_bundle.py")
            return 1
        print("styles.bundle.css à jour")
        return 0
    SORTIE.write_text(neuf, encoding="utf-8")
    print("Écrit : %s (%d Ko)" % (SORTIE.relative_to(RACINE), len(neuf.encode()) // 1024))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
