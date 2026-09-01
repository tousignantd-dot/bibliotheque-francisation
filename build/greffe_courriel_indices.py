#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Le courriel corrigé ne s'affiche plus au premier envoi.

    python3 build/greffe_courriel_indices.py [--retirer]

LE DÉFAUT
L'élève envoyait son courriel et recevait, du même coup, un commentaire ET son
texte réécrit en français correct. Il lisait la version propre, la recopiait,
passait à la suite. Le seul moment où il apprend quelque chose — retrouver sa
faute et réparer sa propre phrase — était escamoté.

`greffe_deux_essais.py` avait réglé exactement cela pour les phrases isolées de
« Je me lance », en août. Le courriel y avait échappé : il passe par une autre
route (`/api/correct-email`) et une autre branche de `renderCorr`, celle qui
reconnaît `corpsCorrige`. Une correction posée sur un chemin ne se propage pas
aux autres — c'est la leçon à retenir de cette greffe-ci.

LE CYCLE
  envoi 1 — le commentaire de pertinence et les explications d'erreur, qui
            SITUENT sans réécrire ; un bouton pour qui reste bloqué ;
  envoi 2 — le texte corrigé vient de lui-même.

CE QUI NE SUFFISAIT PAS
Cacher `corpsCorrige` côté module ne suffit pas : rien n'empêchait le modèle
d'écrire la phrase attendue dans une explication (« il fallait écrire : je
voudrais réserver »). Le module envoie donc son numéro d'envoi au serveur, et
la consigne du premier envoi interdit d'y écrire la forme corrigée. Les deux
moitiés sont nécessaires ; l'une sans l'autre laisse la réponse passer.

Le bouton ne coûte aucun appel : la correction est déjà arrivée, le module la
garde de côté. Même parti pris que pour les phrases isolées.
"""
import argparse, glob, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
SENTINELLE = "function peDevoiler("

ANCIEN_FETCH = ("body:JSON.stringify({code:studentCode,text,scenario:peScenario(),"
                "subject:peSubject(),typeTexte:peTypeTexte()})")
NOUVEAU_FETCH = ("body:JSON.stringify({code:studentCode,text,scenario:peScenario(),"
                 "subject:peSubject(),typeTexte:peTypeTexte(),essai:PE.essai+1})")

ANCIEN_REND = "    html+='<div class=\"fb-c\">'+esc(data.corpsCorrige)+'</div>';"
NOUVEAU_REND = """    // La version corrigée attend le deuxième envoi — ou le bouton. Un élève
    // à qui on montre son texte réécrit le recopie ; il n'a rien réparé.
    if(PE.montre) html+='<div class="fb-c">'+esc(data.corpsCorrige)+'</div>';"""

ANCIEN_SUITE = """    (data.erreurs||[]).forEach(e=>{ html+='<div class="fb-e">'+esc(e.explication||e.explanation||e)+'</div>'; });
    fb.innerHTML=html; fb.classList.add('on'); return;"""
NOUVEAU_SUITE = """    (data.erreurs||[]).forEach(e=>{ html+='<div class="fb-e">'+esc(e.explication||e.explanation||e)+'</div>'; });
    if(!PE.montre){ PE.data=data;
      html+='<button type="button" class="btn btn-ghost" style="margin-top:10px;padding:7px 12px;font-size:12px"'
         +' onclick="peDevoiler()">Montrez-moi la version corrigée</button>'; }
    fb.innerHTML=html; fb.classList.add('on'); return;"""

BLOC = """/* Le courriel corrigé ne se donne plus au premier envoi : voir
   build/greffe_courriel_indices.py. `montre` s'ouvre au deuxième envoi ou par
   le bouton, et ne se referme plus — relire une correction qu'on a déjà vue
   n'apprend rien de plus, mais la cacher de nouveau serait une brimade. */
const PE = {essai:0, montre:false, data:null};
function peDevoiler(){
  if(!PE.data) return;
  PE.montre = true;
  renderCorr('peFb', PE.data, '');
}
"""

ANCRE_BLOC = "function renderCorr(elId,data,orig){"

# Le compteur s'incrémente là où la réponse arrive, pas à l'envoi : un appel
# qui échoue ne doit pas consommer l'essai de l'élève.
ANCIEN_REPONSE = "    renderCorr('peFb',data,text);"
NOUVEAU_REPONSE = """    PE.essai++; if(PE.essai>=2) PE.montre=true;
    renderCorr('peFb',data,text);"""

PAIRES = [(ANCIEN_FETCH, NOUVEAU_FETCH), (ANCIEN_REND, NOUVEAU_REND),
          (ANCIEN_SUITE, NOUVEAU_SUITE), (ANCIEN_REPONSE, NOUVEAU_REPONSE),
          (ANCRE_BLOC, BLOC + ANCRE_BLOC)]


def pose(chemin, retirer=False):
    t = chemin.read_text(encoding="utf-8")
    if "correct-email" not in t:
        return "sans courriel"
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
                return "REFUS : %d occurrence(s) d'un morceau attendu une fois" % t.count(a)
            t = t.replace(a, b, 1)
    chemin.write_text(t, encoding="utf-8")
    return "retiré" if retirer else "posé"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--retirer", action="store_true")
    a = ap.parse_args()
    cibles = [BASE / "build" / "gabarit" / "module.html"] + sorted(
        BASE.glob("assets/interactive/module-*/module-*-activite-interactive.html"))
    bilan = {}
    for c in cibles:
        r = pose(c, a.retirer)
        bilan[r] = bilan.get(r, 0) + 1
        if r.startswith(("REFUS", "RETRAIT")):
            print("  %-26s %s" % (c.parent.name, r))
    for k, v in sorted(bilan.items()):
        print("%4d  %s" % (v, k))


if __name__ == "__main__":
    sys.exit(main())
