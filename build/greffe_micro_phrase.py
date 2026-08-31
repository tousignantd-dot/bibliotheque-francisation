#!/usr/bin/env python3
"""Le micro du jeu de rôle repart à zéro à chaque envoi.

Le symptôme, vu au module n5-logement le 31 août 2026 : l'élève parle, envoie,
reparle — et le champ de saisie affiche **tout ce qu'il a dit depuis le début**
suivi de sa nouvelle phrase. Il croit se répéter, l'assistant reçoit une
réplique qui enfle à chaque tour.

La cause n'est pas la reconnaissance : c'est que le micro reste ouvert d'un
envoi à l'autre (`continuous=true`, et rien ne l'arrête à l'envoi), alors que
l'accumulateur des résultats finaux vivait en variable locale de `jrParler`.
`jrEnvoyer` vidait le champ, jamais l'accumulateur ; le résultat suivant
réécrivait donc le champ avec tout l'historique de la session d'écoute.

La greffe hisse l'accumulateur sur `JR` — `JR.dit` pour les résultats finaux,
`JR.inter` pour le provisoire — et le vide dans `jrEnvoyer` comme dans
`jrRecommencer`. Le micro n'a pas besoin d'être coupé : l'élève peut enchaîner
deux répliques sans retoucher au bouton.

    python3 build/greffe_micro_phrase.py            # gabarit + les 78 modules
    python3 build/greffe_micro_phrase.py --retirer  # revient en arrière

Idempotente : un fichier déjà greffé est laissé tel quel. Elle vise le gabarit
ET les fichiers livrés, parce que plusieurs modules n'ont plus de
`build/contenu/<slug>/` et ne se reconstruisent donc pas.
"""

import argparse
import glob
import io
import sys

GABARIT = "build/gabarit/module.html"
TOUS = "assets/interactive/module-*/module-*-activite-interactive.html"

# (ancien, nouveau) — posés dans cet ordre, retirés dans l'ordre inverse.
PAIRES = [
    (
        """  rec.interimResults=true; rec.continuous=true;
  let acquis='', provisoire='';
""",
        """  rec.interimResults=true; rec.continuous=true;
  // L'accumulateur vit sur JR, pas ici : le micro reste ouvert d'un envoi à
  // l'autre, et c'est jrEnvoyer qui doit pouvoir le vider. En variable locale,
  // la phrase déjà envoyée revenait en tête de la suivante.
  JR.dit=''; JR.inter='';
""",
    ),
    (
        """      if(r.isFinal) acquis+=r[0].transcript+' '; else inter=r[0].transcript;
    }
    provisoire=inter;
    inp.value=(acquis+inter).trim();
""",
        """      if(r.isFinal) JR.dit+=r[0].transcript+' '; else inter=r[0].transcript;
    }
    JR.inter=inter;
    inp.value=(JR.dit+inter).trim();
""",
    ),
    (
        """    if(!inp.value && provisoire) inp.value=provisoire.trim();
""",
        """    if(!inp.value && JR.inter) inp.value=JR.inter.trim();
""",
    ),
    (
        """  JR.hist=[];
  document.getElementById('jrFil').innerHTML='';
""",
        """  JR.hist=[]; JR.dit=''; JR.inter='';
  document.getElementById('jrFil').innerHTML='';
""",
    ),
    # La ligne `JR.hist.push` fait partie des deux versions : sans elle,
    # l'ancien texte serait un préfixe du nouveau, et la greffe se croirait à
    # refaire chaque fois qu'on la repose.
    (
        """function jrEnvoyer(){
  const inp=document.getElementById('jrInput');
  const txt=inp.value.trim();
  if(!txt || JR.occupe) return;
  inp.value='';
  JR.hist.push({role:'user', contenu:txt});
""",
        """function jrEnvoyer(){
  const inp=document.getElementById('jrInput');
  const txt=inp.value.trim();
  if(!txt || JR.occupe) return;
  inp.value='';
  // Ce qui vient d'être envoyé ne doit pas reparaître en tête de la réplique
  // suivante quand le micro est resté ouvert.
  JR.dit=''; JR.inter='';
  JR.hist.push({role:'user', contenu:txt});
""",
    ),
]


def cibles():
    fichiers = [GABARIT] + sorted(glob.glob(TOUS))
    # Neuf modules n'ont pas de jeu de rôle : rien à greffer chez eux.
    return [c for c in fichiers
            if "function jrParler(" in io.open(c, encoding="utf-8").read()]


def poser(chemin, retirer):
    s = io.open(chemin, encoding="utf-8").read()
    paires = [(b, a) for a, b in PAIRES] if retirer else PAIRES
    if all(avant not in s for avant, _ in paires):
        return "déjà fait" if all(apres in s for _, apres in paires) else "introuvable"
    for avant, apres in paires:
        if avant not in s:
            return "partiel"
        s = s.replace(avant, apres, 1)
    io.open(chemin, "w", encoding="utf-8").write(s)
    return "retiré" if retirer else "greffé"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--retirer", action="store_true", help="revenir en arrière")
    args = ap.parse_args()

    compte = {}
    for chemin in cibles():
        etat = poser(chemin, args.retirer)
        compte[etat] = compte.get(etat, 0) + 1
        if etat in ("introuvable", "partiel"):
            print("  ! {} — {}".format(chemin, etat))
    for etat in sorted(compte):
        print("{:>4}  {}".format(compte[etat], etat))
    return 1 if compte.get("introuvable") or compte.get("partiel") else 0


if __name__ == "__main__":
    sys.exit(main())
