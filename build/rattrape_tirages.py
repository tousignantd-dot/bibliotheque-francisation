#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reprend les répliques dont le tirage est sorti hors bande.

    python3 build/rattrape_tirages.py [--plan]

La voix HD ne rend pas deux fois la même chose : chaque synthèse est une prise.
La médiane d'un dialogue peut donc être juste alors qu'une réplique isolée est
partie à 38 c/s — plus vite que ce dont on se plaignait au départ. Un débit
moyen correct ne garantit pas qu'aucune phrase ne déraille.

Le remède est de la nature du défaut : on retire. Jusqu'à trois fois, en
gardant la prise la plus proche de la cible. Ce n'est pas un réglage — le taux
ne change pas —, c'est refuser une mauvaise prise, comme au studio.

La bande est large à dessein (±35 %). Elle n'attrape pas les écarts de style
mais les accidents : une phrase deux fois plus rapide que sa voisine.
"""
import collections, json, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "build"))
import fournisseur as F
from azure_voix import parle
from regen_debit import (repliques, dialogues, en_hd, GENRE, HD_ROLE, CIBLE,
                         duree_parlee)

BANDE = 0.35
TIRAGES = 3
facteurs = json.loads((BASE / "build" / ".facteurs_debit.json").read_text(encoding="utf-8"))
passe2 = json.loads((BASE / "build" / ".facteurs_passe2.json").read_text(encoding="utf-8"))
facteurs.update(passe2)
mesure = {r["f"]: r for r in json.loads((BASE / "build" / ".debits.json").read_text(encoding="utf-8"))
          if r.get("cps")}

hors = []
for cle, e in dialogues(repliques()).items():
    hd = en_hd(e)
    for r in e["reps"]:
        m = mesure.get(r["f"])
        if not m: continue
        c = CIBLE[r["niveau"]]
        if abs(m["cps"] - c) / c <= BANDE: continue
        f = BASE / "assets" / "interactive" / r["f"]
        if not f.exists() or F.est_elevenlabs(f): continue
        role = HD_ROLE[GENRE.get(r["role"], "M")] if hd else r["role"]
        hors.append((r, role, f, c, m["cps"], hd))

par = collections.Counter(("HD" if h else "neurale") for *_, h in hors)
print("répliques hors bande (±%d %% de la cible) : %d   %s"
      % (BANDE*100, len(hors), dict(par)))
for r, role, f, c, cps, hd in sorted(hors, key=lambda x: -abs(x[4]-x[3]))[:8]:
    print("   %5.1f c/s (cible %d)  %-12s %s" % (cps, c, role, r["f"]))
if "--plan" in sys.argv:
    sys.exit(0)

print("\n── reprise ──", flush=True)
mieux = pareil = 0
for r, role, f, c, cps, hd in hors:
    taux = facteurs.get("%s|%d" % (role, r["niveau"]))
    if taux is None: continue
    meilleur, garde = abs(cps - c), None
    for _ in range(TIRAGES):
        tmp = f.with_suffix(".essai.mp3")
        parle(r["texte"], role, tmp, reference="%+d%%" % taux)
        d = duree_parlee(tmp)
        if not d: tmp.unlink(missing_ok=True); continue
        ecart = abs(len(r["texte"]) / d - c)
        if ecart < meilleur:
            meilleur, garde = ecart, tmp.read_bytes()
        tmp.unlink(missing_ok=True)
        if meilleur / c <= BANDE: break
    if garde:
        f.write_bytes(garde); mieux += 1
    else:
        pareil += 1
print("terminé : %d améliorées, %d laissées telles quelles" % (mieux, pareil))
