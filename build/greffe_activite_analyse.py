#!/usr/bin/env python3
"""Ajoute activityId/activityTitle à l'appel /api/analyser-erreurs des modules.

Le module vit dans une iframe : l'activité se lit dans l'adresse du parent,
exactement comme le fait déjà lmsTrack. Sans elle, l'analyse gardée par le
serveur ne se rattache à aucun module, et le tableau de bord ne peut pas la
filtrer.

module-probleme est généré à partir de module-consultation : la greffe posée
sur le gabarit le suit à la reconstruction.
"""
import io, glob, sys

ANCIEN = """  try{
    const res = await fetch('/api/analyser-erreurs', {
      method:'POST', headers:{'Content-Type':'application/json'},
      body: JSON.stringify({
        code: studentCode,
        exercice: ex.tit || '',
        notion: (ex.savoir && ex.savoir.h ? ex.savoir.h.replace(/^›\\s*/,'') : ''),
        items: items,
      })});"""

NOUVEAU = """  // L'activité se lit dans l'adresse du parent, comme le fait lmsTrack : le
  // module est dans une iframe et ne connaît pas son propre numéro. Sans elle,
  // l'analyse que le serveur garde ne se rattache à aucun module.
  let actId = null, actTitre = '';
  try{
    const up = new URLSearchParams(window.parent.location.search);
    actId = parseInt(up.get('activityId')) || null;
    actTitre = up.get('title') || '';
  }catch(e){}

  try{
    const res = await fetch('/api/analyser-erreurs', {
      method:'POST', headers:{'Content-Type':'application/json'},
      body: JSON.stringify({
        code: studentCode,
        activityId: actId,
        activityTitle: actTitre,
        exercice: ex.tit || '',
        notion: (ex.savoir && ex.savoir.h ? ex.savoir.h.replace(/^›\\s*/,'') : ''),
        items: items,
      })});"""

fichiers = sorted(glob.glob("assets/interactive/module-*/module-*-activite-interactive.html"))
faits, deja = [], []
for f in fichiers:
    s = io.open(f, encoding="utf-8").read()
    nom = f.split("/")[2]
    if "activityId: actId," in s:
        deja.append(nom); continue
    if s.count(ANCIEN) != 1:
        sys.exit("!! %s : appel introuvable ou en double (%d)" % (nom, s.count(ANCIEN)))
    io.open(f, "w", encoding="utf-8").write(s.replace(ANCIEN, NOUVEAU, 1))
    faits.append(nom)

print("greffés :", len(faits), " ".join(faits))
if deja: print("déjà faits :", " ".join(deja))
