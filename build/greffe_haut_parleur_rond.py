#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Le haut-parleur des mots devient un vrai cercle, teinté par sa section.

    python3 build/greffe_haut_parleur_rond.py [--retirer]

Le bouton faisait 40 × 40 avec un rayon de 14 px : un carré arrondi, que l'œil
lit comme un ovale dès qu'un fond apparaît au survol. Un rayon de 50 % en fait
un cercle — la forme que portent déjà tous les autres boutons audio du
dispositif (`.btn-audio-round`, `.jr-redire`).

LA COULEUR. Le gris employé était un noir à 5 % : une teinte inventée, qui
n'appartient à aucun jeton. Le fond prend maintenant la couleur de la SECTION,
à 12 % — la même que le filet, la pastille et le titre du bloc. Un contrôle
teinté par son contexte dit à quel bloc il appartient ; un gris ne dit rien.
Le rouge de `--audio` n'est pas retenu ici : le système le réserve à UN aplat
plein par écran, celui du gros bouton d'écoute, et le semer sur chaque mot lui
ferait perdre ce qu'il signale.
"""
import argparse, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
SENTINELLE = "/* HP-ROND */"

ANCIEN = (".word-chip .btn{padding:0!important;width:40px!important;height:40px!important;"
          "display:inline-flex;align-items:center;justify-content:center;font-size:14px;"
          "border-radius:14px}")
# 48 px et non 40 : une règle du système impose `min-height:48px` — la cible
# tactile confortable — et elle l'emportait sur `height:40px`. Le bouton faisait
# donc 40 × 48, et un rayon de 50 % y dessinait une ELLIPSE. Poser le rayon sans
# égaliser les côtés n'aurait rien réglé, et le défaut aurait paru corrigé dans
# la feuille tout en restant à l'écran. On prend 48 plutôt que de rabaisser à
# 40 : c'est le jeton `--tap-comfort`, et un bouton audio gagne à être grand.
NOUVEAU = (".word-chip .btn{padding:0!important;width:48px!important;height:48px!important;"
           "min-height:48px!important;display:inline-flex;align-items:center;"
           "justify-content:center;font-size:14px;border-radius:50%}   " + SENTINELLE)

ANCIEN_H = ".word-chip .btn:hover{background:rgba(0,0,0,.05)!important}"
NOUVEAU_H = (".word-chip .btn:hover{background:color-mix(in srgb,"
             "var(--sec-color,var(--ws-accent)) 12%, transparent)!important}")

PAIRES = [(ANCIEN, NOUVEAU), (ANCIEN_H, NOUVEAU_H)]


def pose(chemin, retirer=False):
    t = chemin.read_text(encoding="utf-8")
    if ".word-chip .btn{" not in t:
        return "sans haut-parleur de mot"
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
