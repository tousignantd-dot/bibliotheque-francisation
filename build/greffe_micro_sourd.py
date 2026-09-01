#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Le micro n'écrit plus ce qu'il entend de l'assistant.

    python3 build/greffe_micro_sourd.py [--retirer]

LE DÉFAUT
Sans écouteurs, le haut-parleur et le micro sont dans la même pièce. Le micro
reste ouvert d'un tour à l'autre — c'est voulu, l'élève enchaîne sans toucher
au bouton — si bien qu'il entend la réplique du propriétaire et la transcrit
dans le champ de l'élève. Celui-ci trouve dans sa ligne les mots qu'il vient
d'entendre, et non ceux qu'il a dits.

`jrParler()` appelait déjà `jrTaire()` pour que le micro ne réentende pas
l'assistant — mais dans l'autre sens seulement : quand l'élève PREND la parole.
Le cas inverse, l'assistant qui parle alors que le micro est déjà ouvert,
n'était pas traité.

LE REMÈDE
Une fenêtre sourde. Pendant que l'assistant parle, `JR.sourd` est vrai : la
reconnaissance continue de tourner — l'arrêter et la relancer coûte un délai et
un `onend` qui remettrait le bouton au repos — mais tout ce qu'elle rend est
JETÉ, et la ligne de coupe avance d'autant. Rien ne s'écrit, rien ne traîne.

Le silence se lève dans jrTaire(), donc aussi quand l'élève coupe la parole :
toucher le micro pendant que l'assistant parle le fait taire ET rend l'oreille.
Sans cela, interrompre aurait rendu le micro sourd pour toujours.

Ne se pose que sur les modules qui ont un jeu de rôle.
"""
import argparse, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
SENTINELLE = "JR.sourd"

PAIRES = [
    # 1 · L'oreille se ferme quand la voix part, se rouvre quand elle s'arrête.
    ("""function jrTaire(){
  jrDireNo++;                 // toute lecture en vol devient caduque""",
     """function jrTaire(){
  jrDireNo++;                 // toute lecture en vol devient caduque
  JR.sourd=false;             // l'assistant se tait : le micro réentend"""),

    ("""    jrAudio=a;
    a.onended=()=>{ URL.revokeObjectURL(url); if(jrAudio===a) jrAudio=null; };""",
     """    jrAudio=a;
    // Sans écouteurs, le micro entend le haut-parleur. Tant que l'assistant
    // parle, ce que la reconnaissance rend est jeté : c'est la voix de
    // l'assistant, pas celle de l'élève.
    JR.sourd=true;
    a.onended=()=>{ URL.revokeObjectURL(url); if(jrAudio===a) jrAudio=null;
                    JR.sourd=false; };"""),

    # 2 · Ce qui est entendu pendant ce temps ne s'écrit pas et ne compte pas.
    ("""    JR.vus=e.results.length;
    let dit='', inter='';""",
     """    JR.vus=e.results.length;
    // La ligne de coupe avance : ces résultats-là ne devront pas reparaître
    // quand l'élève reprendra la parole.
    if(JR.sourd){ JR.coupe=e.results.length; return; }
    let dit='', inter='';"""),
]


def pose(chemin, retirer=False):
    t = chemin.read_text(encoding="utf-8")
    if "function jrTaire()" not in t:
        return "sans jeu de rôle"
    if retirer:
        if SENTINELLE not in t:
            return "déjà retiré"
        for a, b in PAIRES:
            if b not in t:
                return "RETRAIT IMPOSSIBLE : morceau absent"
            t = t.replace(b, a, 1)
    else:
        if SENTINELLE in t:
            return "déjà posé"
        for a, b in PAIRES:
            if t.count(a) != 1:
                return "REFUS : %d occurrence(s)" % t.count(a)
            t = t.replace(a, b, 1)
    chemin.write_text(t, encoding="utf-8")
    return "retiré" if retirer else "posé"


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--retirer", action="store_true")
    a = ap.parse_args()
    bilan = {}
    for c in [BASE / "build" / "gabarit" / "module.html"] + sorted(
            BASE.glob("assets/interactive/module-*/module-*-activite-interactive.html")):
        r = pose(c, a.retirer)
        bilan[r] = bilan.get(r, 0) + 1
        if r.startswith(("REFUS", "RETRAIT")):
            print("  %-26s %s" % (c.parent.name, r))
    for k, v in sorted(bilan.items()):
        print("%4d  %s" % (v, k))


if __name__ == "__main__":
    sys.exit(main())
