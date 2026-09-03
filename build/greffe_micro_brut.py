#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Le micro d'enregistrement demande le signal le moins retouché possible.

    python3 build/greffe_micro_brut.py [--retirer]

LE DÉFAUT
`toggleRec()` ouvrait le micro avec `getUserMedia({audio:true})` — les
contraintes par défaut, c'est-à-dire **annulation d'écho, réduction de bruit et
gain automatique tous les trois actifs**. Ces trois traitements sont faits pour
la visioconférence, où l'on veut une voix intelligible ; ils sont exactement à
contretemps quand on enregistre un apprenant **pour faire évaluer sa
prononciation** :

  · la réduction de bruit taille dans les fricatives et les attaques de
    consonnes — le [ʃ], le [s], le [f] sont les premiers à partir, et ce sont
    justement ceux qu'on écoute ;
  · le gain automatique remonte les passages faibles, donc transforme les
    silences en souffle et écrase les écarts d'intensité qui font l'accent
    d'insistance ;
  · l'annulation d'écho retire du signal ce qui ressemble à ce qui sort des
    haut-parleurs, ce qui n'a aucun objet ici.

L'élève est alors évalué sur un son que la machine a déjà réécrit.

LE REMÈDE
Demander les trois à `false`. Contrairement au jeu de rôle, qui passe par
`SpeechRecognition` et n'accepte aucune contrainte (voir
build/greffe_micro_exclusif.py), l'enregistrement passe par `getUserMedia`,
qui les accepte.

**Avec un repli, et il n'est pas décoratif** : certains appareils — surtout des
casques Bluetooth et des micros de téléphone — refusent ou ignorent ces
contraintes. Si l'appel échoue, on redemande le micro tel quel : mieux vaut un
son traité que pas de son du tout. Un élève qui ne peut pas s'enregistrer ne
fait pas l'activité.

Se pose sur les 88 fichiers : tous ont le bloc de production orale.
"""
import argparse
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
SENTINELLE = "MICRO_BRUT"

AVANT = """  try{ stream=await navigator.mediaDevices.getUserMedia({audio:true}); }
  catch(e){ showErr('poErr',"Impossible d'accéder au micro. Vérifie les autorisations."); return; }"""

APRES = """  // On enregistre un apprenant pour faire évaluer sa prononciation : la
  // réduction de bruit taille dans les fricatives et les attaques de
  // consonnes, et le gain automatique change les silences en souffle. Les
  // contraintes par défaut de getUserMedia activent les deux. On demande donc
  // le signal le moins retouché possible.
  const MICRO_BRUT={echoCancellation:false, noiseSuppression:false, autoGainControl:false};
  try{ stream=await navigator.mediaDevices.getUserMedia({audio:MICRO_BRUT}); }
  catch(e){
    // Des appareils refusent ces contraintes — casques Bluetooth, micros de
    // téléphone. Mieux vaut un son traité que pas de son : un élève qui ne
    // peut pas s'enregistrer ne fait pas l'activité.
    try{ stream=await navigator.mediaDevices.getUserMedia({audio:true}); }
    catch(e2){ showErr('poErr',"Impossible d'accéder au micro. Vérifie les autorisations."); return; }
  }"""


def pose(chemin, retirer=False):
    t = chemin.read_text(encoding="utf-8")
    if "async function toggleRec()" not in t:
        return "sans production orale"
    if retirer:
        if SENTINELLE not in t:
            return "déjà retiré"
        if t.count(APRES) != 1:
            return "RETRAIT IMPOSSIBLE : %d occurrence(s)" % t.count(APRES)
        t = t.replace(APRES, AVANT, 1)
    else:
        if SENTINELLE in t:
            return "déjà posé"
        if t.count(AVANT) != 1:
            return "REFUS : %d occurrence(s)" % t.count(AVANT)
        t = t.replace(AVANT, APRES, 1)
    chemin.write_text(t, encoding="utf-8")
    return "retiré" if retirer else "posé"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--retirer", action="store_true")
    a = ap.parse_args()
    cibles = [BASE / "build" / "gabarit" / "module.html"] + sorted(
        BASE.glob("assets/interactive/module-*/module-*-activite-interactive.html"))
    bilan, fautes = {}, []
    for c in cibles:
        r = pose(c, a.retirer)
        bilan[r] = bilan.get(r, 0) + 1
        if r.startswith(("REFUS", "RETRAIT")):
            fautes.append("%s : %s" % (c.parent.name, r))
    for k in sorted(bilan):
        print("  %-28s %d" % (k, bilan[k]))
    for f in fautes:
        print("  ⚠ " + f)
    return 1 if fautes else 0


if __name__ == "__main__":
    sys.exit(main())
