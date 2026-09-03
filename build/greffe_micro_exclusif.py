#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Le micro se ferme pendant que l'assistant parle.

    python3 build/greffe_micro_exclusif.py [--retirer]

LE DÉFAUT, MESURÉ LE 3 SEPTEMBRE 2026
La voix de l'assistant changeait de timbre en cours de réplique : plus mince,
plus filtrée, franchement moins bonne. Deux essais l'ont isolé sans laisser de
place au doute :

  · rejouer la bulle par son haut-parleur, sans toucher au micro → le son est
    le même du début à la fin ;
  · rejouer la MÊME bulle et toucher « parler » pendant la lecture → le son
    change à l'instant précis où le bouton passe au rouge.

Ce n'est donc ni Azure, ni le MP3 — les journaux de production le confirment,
`/api/voix` a répondu à chaque appel et le repli sur la voix du navigateur n'a
jamais joué. **C'est l'ouverture du micro.** Dès qu'un micro est ouvert, Chrome
active son annulation d'écho, et pour annuler l'écho il fait passer la SORTIE
audio par sa chaîne de traitement WebRTC : rééchantillonnée, filtrée. Le son ne
change pas, c'est le chemin par lequel il sort qui change.

POURQUOI ON NE PEUT PAS SIMPLEMENT LE DÉSACTIVER
Le jeu de rôle ouvre le micro par `SpeechRecognition`, qui **n'accepte aucune
contrainte audio** — pas de `echoCancellation: false`. C'est le navigateur qui
ouvre le micro, pas nous. La seule parade est de ne pas avoir le micro ouvert
pendant que l'assistant parle.

LE REMÈDE, ET IL INVERSE L'INTUITION
Jusqu'ici le micro restait ouvert d'un tour à l'autre — c'était voulu, pour que
l'élève enchaîne sans toucher au bouton ; c'est précisément ce choix qui le
laissait ouvert pendant toute la réplique. Désormais le micro se **ferme** avant
que la voix parte et se **rouvre** quand elle s'arrête. L'élève n'y perd aucun
geste : le micro se rouvre pile au moment où c'est à lui de parler.

Trois refus délibérés dans `jrMicroRouvrir()` :
  · rien si l'élève a écrit dans le champ pendant qu'il écoutait — `jrParler()`
    vide la ligne, et rouvrir effacerait sa phrase ;
  · rien si une autre voix a démarré entre-temps ;
  · un délai avant de repartir, parce que Chrome refuse un `start()` trop
    proche du `stop()` précédent.

`JR.sourd` reste en place : le micro n'entend plus le haut-parleur puisqu'il est
fermé, mais la fenêtre sourde couvre encore le repli sur la voix du navigateur
et l'instant où l'élève coupe la parole. Deux ceintures valent mieux qu'une sur
un chemin qu'on ne peut pas éprouver en classe avant la rentrée.

Ne se pose que sur les modules qui ont un jeu de rôle (79 des 88 fichiers).
"""
import argparse
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
SENTINELLE = "jrMicroFermer"

PAIRES = [
    # 1 · Une reprise en attente devient caduque dès qu'on fait taire la voix :
    #     sans cela, couper la parole à l'assistant rouvrirait le micro une
    #     seconde fois, par-dessus celui que l'élève vient d'ouvrir.
    ("""function jrTaire(){
  jrDireNo++;                 // toute lecture en vol devient caduque
  JR.sourd=false;             // l'assistant se tait : le micro réentend""",
     """function jrTaire(){
  jrDireNo++;                 // toute lecture en vol devient caduque
  JR.sourd=false;             // l'assistant se tait : le micro réentend
  JR.reprise=false;           // et la reprise de micro en attente est annulée"""),

    # 2 · Les deux gestes, posés juste avant jrDire.
    ("""async function jrDire(texte){
  jrTaire();""",
     """// Le micro et la voix ne peuvent pas être ouverts en même temps. Dès qu'un
// micro est ouvert, Chrome fait passer la SORTIE audio par sa chaîne
// d'annulation d'écho, et la voix de l'assistant en ressort mince et filtrée —
// mesuré le 3 septembre 2026 : sur le MÊME fichier, le son change à l'instant
// précis où le bouton passe au rouge. `SpeechRecognition` n'accepte aucune
// contrainte audio, donc on ne peut pas désactiver ce traitement : on peut
// seulement éviter d'avoir le micro ouvert pendant qu'il parle.
function jrMicroFermer(){
  if(!JR.rec) return false;
  JR.reprise=true;
  try{ JR.rec.stop(); }catch(e){}
  return true;
}

function jrMicroRouvrir(){
  if(!JR.reprise) return;
  JR.reprise=false;
  // L'élève a écrit pendant qu'il écoutait : jrParler() vide le champ, et
  // rouvrir lui effacerait sa phrase. On lui laisse la main.
  const inp=document.getElementById('jrInput');
  if(inp && inp.value.trim()) return;
  // Chrome refuse un start() trop proche du stop() précédent, et `onend` doit
  // avoir rendu la main avant qu'on reparte.
  setTimeout(()=>{ if(!JR.rec && !jrAudio) jrParler(); }, 250);
}

async function jrDire(texte){
  jrTaire();
  // Avant la requête, pas après : quel que soit le chemin pris ensuite — voix
  // du serveur, repli du navigateur, panne — le micro doit être fermé avant
  // qu'un son sorte.
  jrMicroFermer();"""),

    # 3 · La voix du serveur rend la main au micro quand elle a fini.
    ("""    a.onended=()=>{ URL.revokeObjectURL(url); if(jrAudio===a) jrAudio=null;
                    JR.sourd=false; };""",
     """    a.onended=()=>{ URL.revokeObjectURL(url); if(jrAudio===a) jrAudio=null;
                    JR.sourd=false; jrMicroRouvrir(); };"""),

    # 4 · Le repli aussi. Sans `onerror`, une synthèse qui échoue laisserait le
    #     micro fermé pour de bon, et l'élève sans moyen de répondre autrement
    #     qu'en touchant le bouton.
    ("""    const v=jrVoixFr(); if(v) u.voice=v;
    speechSynthesis.speak(u);
  }catch(e){}""",
     """    const v=jrVoixFr(); if(v) u.voice=v;
    u.onend=jrMicroRouvrir; u.onerror=jrMicroRouvrir;
    speechSynthesis.speak(u);
  }catch(e){ jrMicroRouvrir(); }"""),

    # 6 · Un bouton qui ne ment pas. `start()` qui échoue laissait le bouton
    #     ROUGE et l'étiquette « Je t'écoute… » alors que plus rien n'écoutait.
    #     Chrome refuse un start() trop proche du stop() précédent : le cas
    #     était rare tant que le micro s'ouvrait une fois par exercice, il ne
    #     l'est plus depuis qu'il se referme à chaque réplique.
    ("""  try{ rec.start(); }catch(e){ JR.rec=null; }""",
     """  try{ rec.start(); }
  catch(e){
    JR.rec=null;
    btn.classList.remove('rec'); btn.textContent='🎤';
    lbl.textContent='Touche pour parler';
  }"""),

    # 5 · Et le cas où l'on ne parle pas du tout : élève qui a coupé la parole
    #     (le micro est déjà à lui), ou panne avant toute lecture.
    ("""    if(no===jrDireNo) jrDireNavigateur(texte);
  }
}""",
     """    if(no===jrDireNo) jrDireNavigateur(texte); else jrMicroRouvrir();
  }
}"""),
]


def pose(chemin, retirer=False):
    t = chemin.read_text(encoding="utf-8")
    if "function jrTaire()" not in t:
        return "sans jeu de rôle"
    if retirer:
        if SENTINELLE not in t:
            return "déjà retiré"
        for avant, apres in PAIRES:
            if t.count(apres) != 1:
                return "RETRAIT IMPOSSIBLE : %d occurrence(s)" % t.count(apres)
            t = t.replace(apres, avant, 1)
    else:
        if SENTINELLE in t:
            return "déjà posé"
        for avant, apres in PAIRES:
            if t.count(avant) != 1:
                return "REFUS : %d occurrence(s)" % t.count(avant)
            t = t.replace(avant, apres, 1)
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
