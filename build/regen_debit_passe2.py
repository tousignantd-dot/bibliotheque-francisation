#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Seconde passe : ne reprend que les couples (voix, niveau) restés hors cible.

    python3 build/regen_debit_passe2.py [--plan]

Le facteur ne se réétalonne pas — il se corrige sur ce qui est SORTI. On
connaît le taux employé au premier passage et le débit obtenu ; la cible
s'atteint par une règle de trois, sans resynthétiser pour mesurer. C'est ce
qu'un étalonnage sur échantillon ne peut pas faire : cinq répliques ne règlent
pas un facteur, cinq cents oui.

Ne touche que les couples dont l'écart dépasse 5 %. Reprendre ce qui est déjà
juste, c'est ajouter du bruit et de la dépense sans rien gagner.
"""
import collections, json, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "build"))
import fournisseur as F
from azure_voix import parle
from regen_debit import repliques, dialogues, en_hd, GENRE, HD_ROLE

facteurs = json.loads((BASE / "build" / ".facteurs_passe2.json").read_text(encoding="utf-8"))
travail = []
for cle, e in dialogues(repliques()).items():
    hd = en_hd(e)
    for r in e["reps"]:
        role = HD_ROLE[GENRE.get(r["role"], "M")] if hd else r["role"]
        k = "%s|%d" % (role, r["niveau"])
        if k not in facteurs:
            continue
        f = BASE / "assets" / "interactive" / r["f"]
        if not f.exists() or F.est_elevenlabs(f):
            continue
        travail.append((r, role, k, f))

par = collections.Counter(k for _, _, k, _ in travail)
for k, n in sorted(par.items()):
    print("  %-18s %+4d%%   %4d répliques" % (k, facteurs[k], n))
print("total : %d répliques" % len(travail))
if "--plan" in sys.argv:
    sys.exit(0)

faits = rates = 0
for i, (r, role, k, f) in enumerate(travail, 1):
    try:
        parle(r["texte"], role, f, reference="%+d%%" % facteurs[k])
        faits += 1
    except Exception as e:                                     # noqa: BLE001
        rates += 1
        print("  échec %s : %s" % (r["f"], e), flush=True)
    if i % 100 == 0:
        print("  %d / %d" % (i, len(travail)), flush=True)
print("terminé : %d refaites, %d échecs" % (faits, rates))
