#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La série « avec les notions » ne doit rien perdre de la série d'origine.

    python3 build/controles/fiches_plus_a_jour.py

`build/fiches_plus.py` ne réécrit pas les fiches : il **recopie** celles de
`assets/documents/` et leur ajoute deux choses, toujours les mêmes — une
feuille de style et une section « En apprendre plus » posée juste avant le
pied de page. La série « avec » est donc, par construction, la série « sans »
plus un bloc.

Par construction, mais pas par surveillance. Le 7 septembre 2026, le document
source est descendu dans quatre fiches (l'ordre du jour, la note de service,
l'offre de Boisverte, les articles 12 et 13) ; la série d'essai, elle, datait
de la veille. Elle n'a **rien signalé** : elle était complète, simplement
complète d'une version antérieure. C'est le défaut propre à toute copie — elle
ne vieillit pas bruyamment.

Ce contrôle défait l'enrichissement et compare au fichier d'origine, octet
pour octet. Sortie en code 1 dès le premier écart : la réparation est
`python3 build/fiches_plus.py`, qui refait la série entière.
"""
import io
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parents[2]
DOCS = RACINE / 'assets' / 'documents'
PLUS = DOCS / 'plus'


def depouiller(html):
    """Retire ce que `enrichir()` ajoute, et rend la fiche d'origine."""
    html = re.sub(r'</style>\n<style>.*?</style>', '</style>', html, count=1, flags=re.S)
    html = re.sub(r'<div class="plus-papier">.*?</div>\n(?=<footer>|</body>)',
                  '', html, count=1, flags=re.S)
    return html


def main():
    if not PLUS.is_dir():
        print('pas de série « avec » : rien à contrôler')
        return 0
    ecarts, vus = [], 0
    for f in sorted(PLUS.glob('module-*.html')):
        base = DOCS / f.name
        if not base.exists():
            ecarts.append((f.name, 'aucune fiche d’origine de ce nom'))
            continue
        vus += 1
        nu = depouiller(io.open(f, encoding='utf-8').read())
        if nu != io.open(base, encoding='utf-8').read():
            ecarts.append((f.name, 'diffère de la fiche d’origine'))
    print('%d fiches « avec » comparées à leur original' % vus)
    for nom, quoi in ecarts:
        print('   ✗ %-62s %s' % (nom, quoi))
    if ecarts:
        print('\n%d écart(s). Réparation : python3 build/fiches_plus.py' % len(ecarts))
        return 1
    print('✓ la série « avec » porte tout ce que porte la série « sans »')
    return 0


if __name__ == '__main__':
    sys.exit(main())
