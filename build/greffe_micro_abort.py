#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Le micro se ferme AVANT que l'assistant parle, pas pendant son premier mot.

    python3 build/greffe_micro_abort.py --releve   # ce qui serait changé
    python3 build/greffe_micro_abort.py            # le gabarit + les 78 modules

Le défaut, tel que l'utilisateur l'a entendu
---------------------------------------------
« Il y a généralement un mot avant que le micro se ferme, et le déclic
d'ouverture-fermeture de Chrome tombe dessus. » Le reste marchait déjà : quand
l'assistant se tait, le micro se rouvre.

Pourquoi le micro fermait en retard
------------------------------------
`jrDire()` fermait pourtant le micro **avant** la requête de synthèse, et le
commentaire du code le disait. Mais il le fermait avec `stop()`, qui est une
fermeture **polie** : le moteur de reconnaissance finit d'analyser ce qu'il a
entendu et ne rend le micro qu'à `onend`, un bon moment plus tard. La voix,
elle, part dès qu'Azure a répondu — et depuis que la latence du jeu de rôle a
été coupée de moitié, elle arrive souvent la première.

`abort()` rend le micro tout de suite et jette ce qui restait à analyser. Ce
qui restait à analyser, c'était la voix de l'assistant, pas celle de l'élève :
la phrase de l'élève est déjà partie dans `jrEnvoyer()`.

Le second défaut, invisible mais du même endroit
-------------------------------------------------
`JR.sourd` — le drapeau qui fait jeter ce que la reconnaissance rend pendant
que l'assistant parle — n'était levé qu'**après** la réponse du serveur. Entre
la fermeture du micro et la première note, un mot pouvait donc atterrir dans le
champ de saisie ; et un champ non vide empêche ensuite `jrMicroRouvrir()` de
rendre le micro à l'élève. Il se lève maintenant à la fermeture, et retombe à
la réouverture — les deux fonctions se répondent.

`jrMicroRouvrir()` ne le rabaissait nulle part : seul `a.onended` le faisait,
donc uniquement sur le chemin de la voix du serveur. Le repli du navigateur
laissait le micro rouvert et sourd.

Ce que la greffe touche
------------------------
Deux fonctions, dans 79 fichiers : `build/gabarit/module.html` et les 78
modules déjà générés. Leur texte est **identique partout** — vérifié avant
d'écrire, et la greffe refuse de travailler si ce n'est plus le cas. Elle est
rejouable : un fichier déjà greffé est laissé tel quel.
"""
import argparse
import os
import pathlib
import subprocess
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent

AVANT_FERMER = """function jrMicroFermer(){
  if(!JR.rec) return false;
  JR.reprise=true;
  try{ JR.rec.stop(); }catch(e){}
  return true;
}
"""

APRES_FERMER = """function jrMicroFermer(){
  if(!JR.rec) return false;
  JR.reprise=true;
  // Sourd DÈS MAINTENANT, et non quand le son commence. Entre la fermeture du
  // micro et la première note, la reconnaissance rendait encore des résultats,
  // qui atterrissaient dans le champ de saisie — et un champ non vide empêche
  // ensuite jrMicroRouvrir() de rendre le micro à l'élève.
  JR.sourd=true;
  // `abort()`, et non `stop()`. `stop()` est une fermeture POLIE : le moteur
  // finit d'analyser ce qu'il a entendu et ne rend le micro qu'à `onend`, un
  // bon moment plus tard. La voix de l'assistant, elle, part dès qu'Azure a
  // répondu — le déclic d'ouverture-fermeture de Chrome tombait donc sur son
  // premier mot. `abort()` rend le micro tout de suite et jette ce qui restait
  // à analyser : ce qui restait à analyser, c'était la voix de l'assistant,
  // pas celle de l'élève — celle de l'élève est déjà partie dans jrEnvoyer().
  try{ JR.rec.abort(); }catch(e){ try{ JR.rec.stop(); }catch(e2){} }
  return true;
}
"""

AVANT_ROUVRIR = """function jrMicroRouvrir(){
  if(!JR.reprise) return;
  JR.reprise=false;
"""

APRES_ROUVRIR = """function jrMicroRouvrir(){
  if(!JR.reprise) return;
  JR.reprise=false;
  // Le pendant de jrMicroFermer() : l'assistant s'est tu, ce qui sera entendu
  // est de nouveau l'élève. `a.onended` le faisait déjà pour la voix du
  // serveur ; le repli du navigateur, lui, ne le faisait nulle part, et le
  // micro rouvrait sourd.
  JR.sourd=false;
"""


def fichiers():
    """Les fichiers qui portent le jeu de rôle. Cherchés, jamais listés en dur :
    une liste écrite à la main vieillit au premier module de plus."""
    sortie = subprocess.run(
        ['grep', '-rl', 'jrMicroFermer', '.', '--include=*.html', '--include=*.js'],
        capture_output=True, text=True, cwd=str(RACINE))
    return sorted(f for f in sortie.stdout.split()
                  if f and not f.startswith('./.git'))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--releve', action='store_true')
    args = ap.parse_args()

    liste = fichiers()
    if not liste:
        print('Aucun fichier ne porte le jeu de rôle — rien à faire.')
        return 1

    a_faire, deja, refus = [], [], []
    for rel in liste:
        chemin = RACINE / rel
        texte = chemin.read_text(encoding='utf-8')
        if 'JR.rec.abort()' in texte:
            deja.append(rel)
            continue
        # Une seule occurrence de chaque, sinon on ne sait pas laquelle greffer.
        if texte.count(AVANT_FERMER) != 1 or texte.count(AVANT_ROUVRIR) != 1:
            refus.append(rel)
            continue
        a_faire.append((chemin, rel, texte))

    if refus:
        print('REFUS — le texte attendu n’est pas là, ou pas une seule fois :')
        for r in refus:
            print('  ✗ ' + r)
        print('\nRien n’a été écrit. Une greffe qui devine est une greffe qui casse.')
        return 1

    for chemin, rel, texte in a_faire:
        if args.releve:
            continue
        neuf = texte.replace(AVANT_FERMER, APRES_FERMER, 1)
        neuf = neuf.replace(AVANT_ROUVRIR, APRES_ROUVRIR, 1)
        chemin.write_text(neuf, encoding='utf-8')

    quoi = 'à greffer' if args.releve else 'greffés'
    print('%d fichiers %s, %d déjà à jour, %d en refus.'
          % (len(a_faire), quoi, len(deja), len(refus)))
    if a_faire and not args.releve:
        print('Dont le gabarit : %s'
              % ('oui' if any('gabarit' in r for _, r, _ in a_faire) else 'NON — à vérifier'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
