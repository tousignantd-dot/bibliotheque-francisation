#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Les fichiers de langue d'appui du portail sont-ils complets et relus ?

    python3 build/controles/appui.py

Rien n'est écrit. Le contrôle répond à trois questions :

  1. **Le dictionnaire couvre-t-il ce que le portail affiche ?** Les clés sont
     les chaînes françaises exactes ; une phrase modifiée dans `eleve.html`
     cesse silencieusement d'être traduite — c'est le seul vrai défaut de ce
     mécanisme, et c'est ce contrôle qui l'attrape.
  2. **Les fichiers sont-ils cohérents entre eux ?** Toute langue doit porter
     les mêmes clés : un trou dans l'un ne se voit pas à l'écran, la ligne
     reste simplement en français.
  3. **Qui a relu ?** Une traduction produite par machine et jamais lue est
     utilisable — l'appui se pose SOUS le français, donc une erreur est un
     mauvais indice, pas une consigne perdue — mais on doit savoir laquelle
     l'est encore.

Ajouter une langue reste « un fichier + une relecture » : copier un fichier
existant, traduire les valeurs, poser le code dans la table `LANGUES` de
`js/appui.js`.
"""

import json
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent.parent
DOSSIER = RACINE / "langues" / "portail"
PORTAIL = RACINE / "eleve.html"
MODULE = RACINE / "js" / "appui.js"


def langues_declarees():
    """Les codes que le module propose dans son sélecteur."""
    t = MODULE.read_text(encoding="utf-8")
    bloc = re.search(r"var LANGUES = \[(.*?)\];", t, re.S)
    return re.findall(r"c:\s*'([a-z-]+)'", bloc.group(1)) if bloc else []


def main():
    fichiers = sorted(DOSSIER.glob("*.json"))
    if not fichiers:
        print("Aucun fichier de langue dans %s." % DOSSIER)
        return 1

    tables, souci = {}, 0
    for f in fichiers:
        tables[f.stem] = json.loads(f.read_text(encoding="utf-8"))

    # La langue de référence est celle qui a le plus de clés : c'est elle qui
    # dit ce que le portail sait traduire aujourd'hui.
    ref = max(tables, key=lambda c: len(tables[c].get("mots", {})))
    cles = set(tables[ref]["mots"])

    print("Langues : %s   (référence : %s, %d clés)\n"
          % (", ".join(sorted(tables)), ref, len(cles)))

    print("── Complétude ──")
    for code in sorted(tables):
        mots = tables[code].get("mots", {})
        manque = cles - set(mots)
        vides = [k for k, v in mots.items() if not str(v).strip()]
        etat = "✓" if not manque and not vides else "TROU"
        print("  %-6s %-4s %d clés%s%s"
              % (code, etat, len(mots),
                 " · %d manquante(s)" % len(manque) if manque else "",
                 " · %d vide(s)" % len(vides) if vides else ""))
        for k in sorted(manque)[:5]:
            print("         manque : %s" % k[:70])
        souci += bool(manque or vides)
    print()

    print("── Relecture ──")
    for code in sorted(tables):
        relu = tables[code].get("relu")
        print("  %-6s %s" % (code, relu if relu else
                             "PAS ENCORE RELU — traduction produite par machine"))
    print()

    # Le sélecteur ne doit proposer que des langues qui existent sur le disque.
    declarees, sur_disque = set(langues_declarees()), set(tables)
    print("── Sélecteur et fichiers ──")
    if declarees - sur_disque:
        print("  ⚠ proposées sans fichier : %s" % ", ".join(sorted(declarees - sur_disque)))
        souci += 1
    if sur_disque - declarees:
        print("  · fichiers non proposés : %s" % ", ".join(sorted(sur_disque - declarees)))
    if declarees == sur_disque:
        print("  ✓ les %d langues proposées ont toutes un fichier" % len(declarees))
    print()

    # Une clé qui ne se retrouve nulle part dans le portail ne sert plus à
    # rien — signe qu'une phrase a été réécrite sans que le dictionnaire suive.
    page = PORTAIL.read_text(encoding="utf-8")
    orphelines = [k for k in sorted(cles) if k not in page]
    print("── Clés encore présentes dans eleve.html ──")
    if orphelines:
        print("  ⚠ %d clé(s) introuvable(s) dans la page — la phrase a sans doute"
              % len(orphelines))
        print("    changé ; ces lignes ne sont plus traduites, en silence :")
        for k in orphelines[:10]:
            print("      · %s" % k[:70])
        souci += 1
    else:
        print("  ✓ les %d clés se retrouvent toutes dans la page" % len(cles))

    return 1 if souci else 0


if __name__ == "__main__":
    sys.exit(main())
