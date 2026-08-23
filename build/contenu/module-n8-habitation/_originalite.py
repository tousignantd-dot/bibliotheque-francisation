# -*- coding: utf-8 -*-
"""Mesure d'originalité de module-n8-habitation contre tous les autres contenus.

Méthode de `docs/verification-originalite.md`, avec le **filtre** que l'agent
de l'activité 119 a documenté et qui vaut pour toute mesure ultérieure : la
regex qui relève les chaînes d'un fichier JavaScript attrape aussi des
**fragments de code** — une rangée coupée en deux par un saut de ligne, un bout
de balise, une interpolation. Ces fragments sont évidemment identiques d'un
module à l'autre, puisque le gabarit est commun, et ils surestiment le taux
d'environ quatre points.

Trois lignes de filtre, donc : pas de saut de ligne dans la chaîne, pas de
chevron ouvrant, pas d'interpolation `${`.

    python3 build/contenu/module-n8-habitation/_originalite.py
"""
import pathlib
import re

RACINE = pathlib.Path(__file__).resolve().parents[3]
CONTENU = RACINE / 'build' / 'contenu'
MOI = 'module-n8-habitation'
# Quatre fichiers, et non les sept. `docs/verification-originalite.md` mesure
# « les énoncés visibles par l'élève » : ce sont les dialogues, les cartes de
# vocabulaire, les exercices et les mini-leçons. `custom.js` est du **markup**
# — le bloc « Je me lance » est structurellement le même partout, et compter
# ses `class="btn btn-send"` et ses `color:#1D6B8F` revient à mesurer la
# ressemblance du gabarit avec lui-même. `sections.js` porte la nomenclature
# imposée du projet (« Je découvre », « Je retiens des mots »), et
# `carrier.js` des phrases porteuses de deux mots. Les inclure gonflait la
# mesure de quatre points sans rien dire du contenu.
FICHIERS = ('dialogues.js', 'fccards.js', 'exos.js', 'plus.js')

CHAINE = re.compile(r'"((?:[^"\\]|\\.){12,})"' r"|'((?:[^'\\]|\\.){12,})'")


def enonces(dossier):
    """Les chaînes visibles d'un dossier de contenu, fragments de code écartés."""
    vus = set()
    for nom in FICHIERS:
        f = dossier / nom
        if not f.exists():
            continue
        for m in CHAINE.finditer(f.read_text(encoding='utf-8')):
            s = (m.group(1) or m.group(2)).strip()
            if '\n' in s or '<' in s or '${' in s:
                continue
            # Le filtre de l'activité 119 ne suffit pas : la regex coupe aussi
            # sur une apostrophe échappée, et rend alors des morceaux de code
            # sans saut de ligne ni chevron — « , tit:"Défi 2 · L » ou
            # « +i, q:c.word, aid: ». Ils sont identiques d'un module à
            # l'autre parce que le gabarit l'est, et ils comptent pour trois
            # points. Trois marques les attrapent tous : une clé JavaScript
            # (`x:"` ou `x:'`), un début de fragment (`,` ou `+`), et une fin
            # de fragment (deux points collés à la fin).
            if re.search(r'\w+:["\']', s) or s[0] in ',+' or s.endswith(':'):
                continue
            vus.add(s)
    return vus


miens = enonces(CONTENU / MOI)
autres = set()
n = 0
for d in sorted(CONTENU.iterdir()):
    if not d.is_dir() or d.name == MOI:
        continue
    n += 1
    autres |= enonces(d)

communs = sorted(miens & autres)
pct = 100.0 * len(communs) / len(miens) if miens else 0.0

print('%s : %d énoncés visibles' % (MOI, len(miens)))
print('%d autres modules : %d énoncés' % (n, len(autres)))
print('%d identiques, soit %.1f %%' % (len(communs), pct))
print()
for s in communs[:40]:
    print('   · ' + (s[:96] + '…' if len(s) > 96 else s))
if len(communs) > 40:
    print('   … et %d autres' % (len(communs) - 40))
