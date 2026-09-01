#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Le fragment de la phrase envoyée ne revient plus dans le champ du micro.

    python3 build/greffe_micro_coupe.py [--retirer]

LE DÉFAUT
Le micro reste ouvert d'un envoi à l'autre — c'est voulu, l'élève enchaîne sans
retoucher le bouton. Mais la reconnaissance vocale ne s'arrête pas net quand on
appuie sur « Envoyer » : elle livre encore, une fraction de seconde plus tard,
le résultat FINAL de la phrase qu'on vient d'envoyer. `onresult` l'ajoutait
alors à `JR.dit`, tout juste vidé, et la fin de la phrase envoyée réapparaissait
dans le champ. Second chemin vers le même symptôme : `onend` restaurait
`JR.inter` quand le champ était vide, sans regarder à quelle phrase il
appartenait.

`greffe_micro_phrase.py` avait déjà réglé l'accumulation d'une phrase sur
l'autre en sortant l'accumulateur de la fermeture. Il manquait la LIGNE DE
COUPE : vider l'accumulateur ne sert à rien si les résultats d'avant l'envoi
continuent d'y entrer.

LE REMÈDE
Une ligne d'eau sur la liste des résultats. `JR.vus` retient combien de
résultats la reconnaissance a produits ; « Envoyer » pose `JR.coupe = JR.vus`,
et `onresult` ne relit que ce qui vient après. Un résultat provisoire promu en
final GARDE SON INDEX : il tombe donc sous la ligne et reste ignoré, ce qu'un
simple « vide l'accumulateur » ne pouvait pas faire.

Le texte est recalculé à chaque événement plutôt qu'accumulé : la seule façon
qu'une ligne de coupe soit respectée rétroactivement.

Idempotent, réversible, et le retrait se fait par marqueurs.
"""
import re, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
CIBLES = [BASE / "build" / "gabarit" / "module.html"] + sorted(
    BASE.glob("assets/interactive/module-*/module-*-activite-interactive.html"))

SENTINELLE = "JR.coupe"

ANCIEN_RESULT = """  rec.onresult=e=>{
    let inter='';
    for(let i=e.resultIndex;i<e.results.length;i++){
      const r=e.results[i];
      if(r.isFinal) JR.dit+=r[0].transcript+' '; else inter=r[0].transcript;
    }
    JR.inter=inter;
    inp.value=(JR.dit+inter).trim();
  };"""

NOUVEAU_RESULT = """  rec.onresult=e=>{
    // Recalculé, jamais accumulé : c'est la seule façon qu'une ligne de coupe
    // posée après coup par jrEnvoyer soit respectée. `JR.coupe` est l'index du
    // premier résultat qui appartient à la phrase EN COURS ; tout ce qui est
    // avant a déjà été envoyé, y compris un provisoire promu en final, qui
    // garde son index et resterait donc sous la ligne.
    JR.vus=e.results.length;
    let dit='', inter='';
    for(let i=(JR.coupe||0);i<e.results.length;i++){
      const r=e.results[i];
      if(r.isFinal) dit+=r[0].transcript+' '; else inter=r[0].transcript;
    }
    JR.dit=dit; JR.inter=inter;
    inp.value=(dit+inter).trim();
  };"""

# La reconnaissance qui s'arrête repart d'une liste vide au prochain appui :
# garder l'ancienne ligne de coupe ferait taire les premiers mots suivants.
ANCIEN_PARLER = "  JR.dit=''; JR.inter='';\n  btn.classList.add('rec');"
NOUVEAU_PARLER = "  JR.dit=''; JR.inter=''; JR.coupe=0; JR.vus=0;\n  btn.classList.add('rec');"

# Envoyer, c'est clore la phrase : l'accumulateur se vide ET la ligne se pose.
ANCIEN_ENVOYER = "  JR.dit=''; JR.inter='';\n  JR.hist.push({role:'user', contenu:txt});"
NOUVEAU_ENVOYER = ("  JR.dit=''; JR.inter=''; JR.coupe=JR.vus||0;\n"
                   "  JR.hist.push({role:'user', contenu:txt});")

REMPLACEMENTS = [(ANCIEN_RESULT, NOUVEAU_RESULT),
                 (ANCIEN_PARLER, NOUVEAU_PARLER),
                 (ANCIEN_ENVOYER, NOUVEAU_ENVOYER)]


def pose(chemin, retirer=False):
    t = chemin.read_text(encoding="utf-8")
    if "function jrParler" not in t:
        return "sans micro"
    # L'état se lit sur la SENTINELLE, jamais sur la présence de l'ancien
    # texte : ANCIEN_PARLER est un préfixe de NOUVEAU_PARLER, et « l'ancien est
    # encore là » ne voudrait donc rien dire.
    pose_deja = SENTINELLE in t
    if retirer:
        if not pose_deja:
            return "déjà retiré"
        for a, b in REMPLACEMENTS:
            if b not in t:
                return "RETRAIT IMPOSSIBLE : morceau absent"
            t = t.replace(b, a, 1)
    else:
        if pose_deja:
            return "déjà posé"
        for a, b in REMPLACEMENTS:
            if t.count(a) != 1:
                return "REFUS : %d occurrence(s) d'un morceau attendu une fois" % t.count(a)
            t = t.replace(a, b, 1)
    chemin.write_text(t, encoding="utf-8")
    return "retiré" if retirer else "posé"


def main():
    retirer = "--retirer" in sys.argv
    bilan = {}
    for c in CIBLES:
        r = pose(c, retirer)
        bilan[r] = bilan.get(r, 0) + 1
        if r.startswith(("REFUS", "RETRAIT")):
            print("  %-26s %s" % (c.parent.name, r))
    for k, v in sorted(bilan.items()):
        print("%4d  %s" % (v, k))


if __name__ == "__main__":
    main()
