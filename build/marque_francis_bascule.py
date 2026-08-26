#!/usr/bin/env python3
"""Bascule l'ancienne marque SAAF vers la marque « francis ».

Remise du 26 août 2026 (~/Downloads/design_handoff_francis) : le produit
s'appelle désormais **francis**, le logotype n'est plus une pilule à contour
mauve mais le nom en minuscules, un trait, un descripteur — et pour tout
signe, le point du « i ».

Le script réécrit sur place tout ce qui portait l'ancienne marque : les liens
de la feuille de style et du favicon, les marqueurs de greffe, le markup du
verrouillage, les classes, le nom en toutes lettres et l'ancien descripteur.
Il touche le HTML déjà construit **et** les sources qui le construisent, pour
qu'une reconstruction ne ramène pas l'ancienne marque.

Il est idempotent : un fichier déjà basculé ne bouge plus.

    python3 build/marque_francis_bascule.py --essai   # ce qui changerait
    python3 build/marque_francis_bascule.py           # écrit

Ce que le script NE touche pas, volontairement :
  · `saaf-vitesse`, la clé de localStorage du bouton de débit — la renommer
    effacerait le réglage gardé par les élèves ; elle n'est pas visible.
  · `/FolioSAAF`, un nom de police interne aux PDF du manuel.
  · lui-même : il porte les motifs de l'ancienne marque, il s'exclut donc de
    la liste des fichiers, sans quoi il se réécrirait et deviendrait faux.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MOI = pathlib.Path(__file__).resolve()
SUFFIXES = {'.html', '.py', '.css', '.md', '.svg'}
IGNORES = ('.claude/worktrees/', 'node_modules/', '.git/')

VIEUX = 'SAAF'          # écrit une fois, jamais en clair dans les motifs
vieux_bas = VIEUX.lower()

# Le nom, composé avec « ı » (U+0131) pour que le disque remplace le point.
# role="img" + aria-label pour que rien ne lise « francıs ».
NOM = ('<span class="fr-nom" role="img" aria-label="francis">franc'
       '<span class="fr-i" aria-hidden="true">ı<span class="fr-point"></span></span>s</span>')
TRAIT = '<span class="fr-trait" aria-hidden="true"></span>'
DESC = '<span class="fr-desc">Aide à l\'apprentissage du français</span>'

REGLES = [
    # 1 · fichiers de la marque
    (r'marque-%s-favicon\.svg' % vieux_bas, 'marque-francis-favicon.svg'),
    (r'marque-%s\.css' % vieux_bas, 'marque-francis.css'),
    # 2 · marqueurs des greffes
    (r'MARQUE-%s' % VIEUX, 'MARQUE-FRANCIS'),
    # 3 · markup du verrouillage
    (r'<span class="%s-pilule">\s*<span class="%s-nom">%s</span>\s*</span>'
     % (vieux_bas, vieux_bas, VIEUX), NOM),
    (r'<span class="%s-filet"[^>]*></span>' % vieux_bas, TRAIT),
    (r'<span class="%s-desc">.*?</span>' % vieux_bas, DESC),
    # 4 · classes
    (r'%s-lockup--grand' % vieux_bas, 'fr-lockup--grand'),
    (r'%s-lockup' % vieux_bas, 'fr-lockup'),
    (r'%s-bandeau-portail' % vieux_bas, 'fr-bandeau-portail'),
    (r'%s-bandeau' % vieux_bas, 'fr-bandeau'),
    # 5 · le nom en toutes lettres et l'ancien descripteur
    (r'Système d[’\']aide à l[’\']apprentissage du français',
     DESC[DESC.index('>') + 1:DESC.index('</')]),
    (r'\b%s\b' % VIEUX, 'francis'),
]
REGLES = [(re.compile(m, re.S), r) for m, r in REGLES]


def fichiers():
    for f in sorted(ROOT.rglob('*')):
        if f.suffix not in SUFFIXES or not f.is_file():
            continue
        if f.resolve() == MOI:
            continue
        rel = f.relative_to(ROOT).as_posix()
        if any(i in rel + '/' for i in IGNORES):
            continue
        yield f


def bascule(texte):
    for motif, remplacement in REGLES:
        texte = motif.sub(remplacement, texte)
    return texte


def main(argv):
    essai = '--essai' in argv
    faits = 0
    for f in fichiers():
        try:
            vieux = f.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            continue
        if vieux_bas not in vieux.lower():
            continue
        neuf = bascule(vieux)
        if neuf == vieux:
            continue
        faits += 1
        print(f.relative_to(ROOT))
        if not essai:
            f.write_text(neuf, encoding='utf-8')
    print('\n%d fichier(s) %s' % (faits, 'à basculer' if essai else 'basculé(s)'))


if __name__ == '__main__':
    main(sys.argv[1:])
