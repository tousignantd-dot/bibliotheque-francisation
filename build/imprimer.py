#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Le PDF d'une page HTML, par Chrome sans interface.

Un seul endroit, parce que trois scripts en avaient besoin le même jour et que
deux d'entre eux l'avaient recopié. Le format ne se règle **pas** en ligne de
commande : Chrome imprime ce que dit le `@page` de la feuille — c'est déjà la
règle de `programme/outils/fiche_pdf.py`, et la répéter ici serait la deuxième
façon de se tromper.

    from imprimer import imprimer
    n = imprimer(chemin_html, chemin_pdf)   # -> nombre de pages, ou None

`--virtual-time-budget` est ce qui laisse aux polices Google et aux images le
temps d'arriver : sans lui, une page se rend en Times sans que rien ne le dise.
"""

import pathlib
import subprocess

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def imprimer(source, cible, budget_ms=20000, timeout=300):
    """Rend `source` (un fichier HTML local) en PDF dans `cible`.

    Rend le nombre de pages quand `pypdf` est installé, `None` sinon — l'absence
    du compte n'est pas un échec, et faire de pypdf une dépendance dure d'un
    script d'impression serait payer cher un chiffre d'affichage.
    """
    source, cible = pathlib.Path(source), pathlib.Path(cible)
    if not pathlib.Path(CHROME).exists():
        raise SystemExit("!! Chrome est introuvable : %s" % CHROME)
    cmd = [CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
           "--run-all-compositor-stages-before-draw",
           "--virtual-time-budget=%d" % budget_ms,
           "--print-to-pdf=%s" % cible, source.as_uri()]
    subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    if not cible.exists():
        raise SystemExit("!! Chrome n'a produit aucun PDF pour %s." % source.name)
    try:
        from pypdf import PdfReader
        return len(PdfReader(str(cible)).pages)
    except Exception:
        return None
