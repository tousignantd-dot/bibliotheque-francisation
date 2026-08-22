#!/usr/bin/env python3
"""Brancher les générateurs audio déjà écrits sur `build/voix.py`.

    python3 build/greffe_voix.py --essai   # dit ce qu'il ferait
    python3 build/greffe_voix.py

Quatre-vingts générateurs, écrits sur plusieurs mois, tous un peu différents.
Les réécrire un à un, c'est quatre-vingts occasions de se tromper. Mais ils
ont un point commun : ils envoient tous leur charge utile par
`requests.post(..., json=…)`. On enveloppe cet appel, et le contexte français
s'applique partout d'un coup.

Deux formes existent dans le dépôt :

    json=payload                          → json=enrichir(payload)
    json={"text": texte, "model_id": …}   → json=enrichir({...})

La seconde s'étale sur deux lignes ; on retrouve sa fermeture en comptant les
accolades plutôt qu'en devinant.

Le script est **idempotent** : un fichier déjà greffé est sauté. Et il
recompile chaque fichier touché — un générateur cassé se découvrirait
autrement au pire moment, la clé en main et les crédits rechargés.
"""
import ast
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
IMPORT = ("import sys as _sys, pathlib as _pl\n"
          "_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent / 'build'))\n"
          "from voix import enrichir  # contexte français pour les mots isolés\n")


def deja_greffe(s):
    return 'from voix import enrichir' in s


def poser_import(s):
    """Après le dernier import de tête, avant le premier code."""
    lignes = s.split('\n')
    dernier = 0
    for i, l in enumerate(lignes[:60]):
        if re.match(r'^(import |from )\w', l):
            dernier = i
    return '\n'.join(lignes[:dernier + 1] + IMPORT.rstrip('\n').split('\n')
                     + lignes[dernier + 1:])


def envelopper(s):
    """`json=payload` et `json={…}` deviennent `json=enrichir(…)`."""
    n = 0
    s, k = re.subn(r'json=(payload|corps)\b', r'json=enrichir(\1)', s)
    n += k
    # La forme littérale : on part de `json={` et on suit les accolades.
    out, i = [], 0
    for m in re.finditer(r'json=\{', s):
        if m.start() < i:
            continue
        debut = m.end() - 1                    # sur l'accolade ouvrante
        profondeur, j = 0, debut
        while j < len(s):
            if s[j] == '{':
                profondeur += 1
            elif s[j] == '}':
                profondeur -= 1
                if profondeur == 0:
                    break
            j += 1
        else:
            continue
        out.append(s[i:m.start()] + 'json=enrichir(' + s[debut:j + 1] + ')')
        i = j + 1
        n += 1
    out.append(s[i:])
    return ''.join(out), n


def main():
    essai = '--essai' in sys.argv
    faits, sautes, echecs = [], [], []
    for f in sorted(RACINE.glob('generer_audio_*.py')):
        s = f.read_text(encoding='utf-8')
        if deja_greffe(s):
            sautes.append(f.name); continue
        neuf, n = envelopper(s)
        if not n:
            echecs.append((f.name, 'aucun envoi de requête repéré')); continue
        neuf = poser_import(neuf)
        try:
            ast.parse(neuf)
        except SyntaxError as e:
            echecs.append((f.name, 'ne compile plus : %s' % e)); continue
        if not essai:
            f.write_text(neuf, encoding='utf-8')
        faits.append((f.name, n))
    print('%s%d greffé(s), %d déjà fait(s), %d écart(s)'
          % ('[essai] ' if essai else '', len(faits), len(sautes), len(echecs)))
    for nom, quoi in echecs:
        print('   ✗ %-46s %s' % (nom, quoi))
    return 1 if echecs else 0


if __name__ == '__main__':
    sys.exit(main())
