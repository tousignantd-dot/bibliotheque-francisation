#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Le retour à la banque, greffé en tête de chaque présentation.

Le problème, vu à l'usage : on ouvre une fiche depuis `presentations.html`,
elle s'ouvre dans un onglet neuf, et il n'y a **aucun chemin de retour** — ni
lien, ni fil d'Ariane. On se retrouve coincé dans un document.

La greffe pose un bandeau discret tout en haut du `<body>` : « ← Banque de
présentations ». Elle est indépendante de la mise en page de chaque document —
trente-quatre pages, quatre habillages différents, et vingt d'entre elles n'ont
même pas la barre de marque. Un élément posé en tête du flux ne peut recouvrir
personne ; une pastille flottante, si.

    python3 build/greffe_retour.py            # pose sur toutes les pages
    python3 build/greffe_retour.py --retirer  # dégreffe

Retrait par marqueurs, d'un marqueur à l'autre, jamais par chaîne exacte :
c'est la règle du dépôt, et elle a déjà coûté cher une fois.
"""

import argparse
import pathlib
import re

RACINE = pathlib.Path(__file__).resolve().parent.parent
DOSSIER = RACINE / "assets" / "presentations"

DEBUT = "<!-- RETOUR-BANQUE:début — greffé par build/greffe_retour.py -->"
FIN = "<!-- RETOUR-BANQUE:fin -->"

BLOC = """%s
<style>
  .retour-banque{background:#FFFFFF; border-bottom:1px solid #EAEAE8;
    font-family:"Nunito",system-ui,-apple-system,"Segoe UI",sans-serif;}
  .retour-banque a{display:inline-flex; align-items:center; gap:8px;
    max-width:1120px; margin:0 auto; padding:11px 24px; min-height:44px;
    font-size:15px; font-weight:800; color:#4B4F52; text-decoration:none;}
  .retour-banque a:hover{color:#17181A;}
  .retour-banque a:focus-visible{outline:3px solid #0A8F5B; outline-offset:-3px;}
  .retour-banque .fl{font-size:17px; line-height:1;}
  .retour-banque .où{color:#6E7175; font-weight:700;}
  @media print{ .retour-banque{display:none !important;} }
</style>
<div class="retour-banque">
  <a href="/presentations.html"><span class="fl" aria-hidden="true">&#8592;</span>
  Le classeur <span class="où">· toutes les pages du projet</span></a>
</div>
%s
""" % (DEBUT, FIN)


def poser(chemin):
    s = chemin.read_text()
    if DEBUT in s:
        s = retirer_de(s)
    # Deux pages du dépôt n'ont pas de <body> — il est implicite. On se rabat
    # sur la fin du <head>, puis sur le tout début du fichier.
    m = re.search(r"<body[^>]*>", s) or re.search(r"</head>", s)
    if m:
        s = s[:m.end()] + "\n" + BLOC + s[m.end():].lstrip("\n")
    else:
        s = BLOC + s
    chemin.write_text(s)
    return True, "posé"


def retirer_de(s):
    """D'un marqueur à l'autre. Une chaîne exacte échouerait en silence le jour
    où le bloc change d'une virgule."""
    # La ligne vide qui précède part avec le bloc : sans elle, chaque passage
    # en laisse une de plus, et le fichier grossit d'une ligne par exécution.
    return re.sub(r"\n?" + re.escape(DEBUT) + r".*?" + re.escape(FIN) + r"\n?", "", s,
                  flags=re.S)


def retirer(chemin):
    s = chemin.read_text()
    if DEBUT not in s:
        return False, "rien à retirer"
    chemin.write_text(retirer_de(s))
    return True, "retiré"


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--retirer", action="store_true")
    a = ap.parse_args()
    faits = 0
    for p in sorted(DOSSIER.glob("*.html")):
        ok, mot = (retirer if a.retirer else poser)(p)
        if ok:
            faits += 1
        else:
            print("  %-42s %s" % (p.name, mot))
    print("%s : %d page(s)" % ("retiré de" if a.retirer else "posé sur", faits))
