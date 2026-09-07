#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Le micro du jeu de rôle : quand il se ferme, et quand il ne se rouvre plus.

    python3 build/greffe_micro.py --releve   # ce qui serait changé
    python3 build/greffe_micro.py            # le gabarit + les 78 modules

Deux corrections du 7 septembre 2026, toutes deux signalées à l'oreille par
l'utilisateur. La première est décrite ci-dessous ; la seconde, plus simple,
est que **le micro se ferme quand l'élève demande la correction** — il vient
de dire qu'il a fini, et le laisser ouvert pendant qu'il lit sa correction
n'avait aucun sens (voir GREFFE 2, plus bas).

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

# ── GREFFE 1 · abort() plutôt que stop() ──────────────────────────────────

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


# ── GREFFE 2 · « J'ai fini — corrigez mes phrases » ferme le micro ────────
#
# Le bouton dit que l'élève a fini de parler ; le micro restait pourtant
# ouvert pendant toute la lecture de la correction. `jrMicroFermer()` ne
# convenait pas : il pose `JR.reprise`, donc la fin d'une réplique encore en
# vol aurait rouvert le micro derrière son dos. Il fallait une fermeture
# **définitive**, et c'est une fonction de plus plutôt qu'un drapeau de plus
# dans l'ancienne — deux fermetures qui ne veulent pas dire la même chose.

ARRETER = """// L'élève demande la correction : il vient de dire qu'il a fini de parler. Le
// micro se ferme pour de bon — `JR.reprise` remis à faux, sinon la fin d'une
// réplique encore en vol le rouvrirait derrière son dos.
function jrMicroArreter(){
  JR.reprise=false;
  if(!JR.rec) return;
  // `stop()` et non `abort()` : rien ne va parler ici, donc la fermeture peut
  // être polie — et ce que l'élève finissait de dire a le temps d'arriver dans
  // le champ, au cas où il voudrait l'envoyer avant de lire sa correction.
  try{ JR.rec.stop(); }catch(e){}
}

"""

AVANT_FINI = """  if(!mes.length){ showErr('jrErr',"Pose au moins une question avant de demander la correction."); return; }
  hideErr('jrErr');
  document.getElementById('jrStatus').classList.add('on');
"""

APRES_FINI = """  if(!mes.length){ showErr('jrErr',"Pose au moins une question avant de demander la correction."); return; }
  hideErr('jrErr');
  // APRÈS le refus ci-dessus, et pas avant : un élève qui touche le bouton
  // sans avoir rien dit se fait répondre de parler d'abord — lui fermer le
  // micro au même moment serait le contraire de ce qu'on lui demande.
  jrMicroArreter();
  document.getElementById('jrStatus').classList.add('on');
"""

# La fonction se pose juste avant `jrFini`, qui est son seul appelant.
ANCRE_ARRETER = "async function jrFini(){"


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
        besoin1 = 'JR.rec.abort()' not in texte
        besoin2 = 'function jrMicroArreter(' not in texte
        if not besoin1 and not besoin2:
            deja.append(rel)
            continue
        # Une seule occurrence de chaque, sinon on ne sait pas laquelle greffer.
        manque = []
        if besoin1 and (texte.count(AVANT_FERMER) != 1 or texte.count(AVANT_ROUVRIR) != 1):
            manque.append('greffe 1')
        if besoin2 and (texte.count(AVANT_FINI) != 1 or texte.count(ANCRE_ARRETER) != 1):
            manque.append('greffe 2')
        if manque:
            refus.append('%s (%s)' % (rel, ', '.join(manque)))
            continue
        a_faire.append((chemin, rel, texte, besoin1, besoin2))

    if refus:
        print('REFUS — le texte attendu n’est pas là, ou pas une seule fois :')
        for r in refus:
            print('  ✗ ' + r)
        print('\nRien n’a été écrit. Une greffe qui devine est une greffe qui casse.')
        return 1

    for chemin, rel, texte, besoin1, besoin2 in a_faire:
        if args.releve:
            continue
        neuf = texte
        if besoin1:
            neuf = neuf.replace(AVANT_FERMER, APRES_FERMER, 1)
            neuf = neuf.replace(AVANT_ROUVRIR, APRES_ROUVRIR, 1)
        if besoin2:
            neuf = neuf.replace(AVANT_FINI, APRES_FINI, 1)
            neuf = neuf.replace(ANCRE_ARRETER, ARRETER + ANCRE_ARRETER, 1)
        chemin.write_text(neuf, encoding='utf-8')

    quoi = 'à greffer' if args.releve else 'greffés'
    print('%d fichiers %s, %d déjà à jour, %d en refus.'
          % (len(a_faire), quoi, len(deja), len(refus)))
    if a_faire and not args.releve:
        print('Dont le gabarit : %s'
              % ('oui' if any('gabarit' in r for _, r, _, _, _ in a_faire)
                 else 'NON — à vérifier'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
