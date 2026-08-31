"""Un bouton pour cacher les réponses de l'assistant et n'avoir que sa voix.

Demandé le 31 août 2026. Au jeu de rôle, l'élève lit la réplique en même temps
qu'il l'entend — et il la lit, forcément, parce que c'est plus facile. Le
bouton « Écouter sans lire » ferme le texte des réponses : la voix reste, la
compréhension orale redevient un exercice.

Ce qui est caché et ce qui ne l'est pas :

  caché    le texte des répliques de l'ASSISTANT ;
  gardé    ce que l'élève a dit lui-même — il doit pouvoir relire sa phrase ;
  gardé    le bouton haut-parleur de chaque bulle, pour réécouter autant de
           fois qu'il faut ; c'est le seul recours quand on n'a pas compris,
           et c'est exactement l'exercice.

Le bouton est INJECTÉ par le JS commun, sous la rangée « Comment ? ». La
rangée elle-même vit dans le `custom.js` de chaque module, et ils diffèrent
tous : l'écrire là voudrait dire 78 fichiers à retoucher à la main. Il n'entre
pas non plus DANS `#jrModes` — `jrModeVoix()` y balaie tous les `.jr-opt` et
allumerait celui-ci à contretemps.

Cacher le texte force la voix : sans elle, la réponse ne serait ni lisible ni
audible. `JR.voix` ne commandait que le couple micro+voix ; la lecture à haute
voix est désormais demandée par `JR.voix || JR.sansTexte`, ce qui permet
d'écrire au clavier tout en écoutant.

    python3 build/greffe_ecouter_sans_lire.py            # gabarit + 78 modules
    python3 build/greffe_ecouter_sans_lire.py --retirer  # revient en arrière
"""

import argparse
import glob
import io
import sys

GABARIT = "build/gabarit/module.html"
TOUS = "assets/interactive/module-*/module-*-activite-interactive.html"

PAIRES = [
    # 1. Le CSS : la bulle reste, son texte s'efface.
    (
        """.jr-b-moi{background:var(--sel-bg);color:var(--sel-ink);align-self:flex-end;border-bottom-right-radius:5px}
.jr-saisie{display:flex;gap:9px;align-items:center}
""",
        """.jr-b-moi{background:var(--sel-bg);color:var(--sel-ink);align-self:flex-end;border-bottom-right-radius:5px}
/* « Écouter sans lire » : la bulle de l'assistant garde sa place et son bouton
   de réécoute, seul son texte s'efface. Ce que l'élève a dit, lui, reste
   lisible — il doit pouvoir relire sa propre phrase. */
.jr-sans-texte .jr-b-ia .jr-txt{display:none}
.jr-sans-texte .jr-b-ia::after{content:'Texte caché — touchez le haut-parleur pour réécouter';
  display:block;font-size:13px;font-weight:700;font-style:italic;opacity:.6}
#jrEcoute{margin-top:10px}
.jr-saisie{display:flex;gap:9px;align-items:center}
""",
    ),
    # 2. Le texte de la bulle passe dans un <span> : sans lui, rien à cacher.
    (
        """  let h='<span class="jr-b-q">'+(qui==='moi'?'Moi':'Assistant')+'</span>'+esc(texte);
""",
        """  let h='<span class="jr-b-q">'+(qui==='moi'?'Moi':'Assistant')+'</span>'
        +'<span class="jr-txt">'+esc(texte)+'</span>';
""",
    ),
    # 3. Cacher le texte demande la voix, même au clavier.
    (
        """    if(JR.voix) jrDire(d.reponse);
""",
        """    if(JR.voix || JR.sansTexte) jrDire(d.reponse);
""",
    ),
    # 4. Le bouton, sa fonction, et son injection sous la rangée des modes.
    # L'ancien texte reprend la première ligne du corps : sans elle il serait
    # un préfixe du nouveau, et la greffe se croirait à refaire.
    (
        """function jrChoisir(quoi, val){
  JR[quoi] = val;
""",
        """// Le bouton n'est pas dans le HTML des modules : la rangée « Comment ? » est
// écrite dans le custom.js de chacun, et ils diffèrent tous. Il est posé ici,
// APRÈS #jrModes et non dedans — jrModeVoix() balaie les .jr-opt de #jrModes
// et allumerait celui-ci à contretemps.
function jrSansTexte(on){
  JR.sansTexte=on;
  const chat=document.getElementById('jrChat');
  if(chat) chat.classList.toggle('jr-sans-texte', on);
  const b=document.getElementById('jrEcouteBtn');
  if(b){ b.classList.toggle('on', on);
         b.textContent = on ? '👂 Écoute seule — texte caché' : '👂 Écouter sans lire'; }
  try{ localStorage.setItem('saaf-jr-sans-texte', on?'1':'0'); }catch(e){}
}
document.addEventListener('DOMContentLoaded', ()=>{
  const modes=document.getElementById('jrModes');
  if(!modes) return;
  const row=document.createElement('div');
  row.className='jr-opts'; row.id='jrEcoute';
  row.innerHTML='<button class="jr-opt" id="jrEcouteBtn" type="button"'
    +' data-info="Cache le texte des réponses de l\\'assistant : il ne reste que sa voix.'
    +' Le haut-parleur de chaque bulle la rejoue autant de fois qu\\'il faut.">'
    +'👂 Écouter sans lire</button>';
  modes.insertAdjacentElement('afterend', row);
  let garde=false;
  try{ garde = localStorage.getItem('saaf-jr-sans-texte')==='1'; }catch(e){}
  document.getElementById('jrEcouteBtn')
    .addEventListener('click', ()=>jrSansTexte(!JR.sansTexte));
  jrSansTexte(garde);
});

function jrChoisir(quoi, val){
  JR[quoi] = val;
""",
    ),
]


def cibles():
    fichiers = [GABARIT] + sorted(glob.glob(TOUS))
    return [c for c in fichiers
            if "function jrChoisir(quoi, val){" in io.open(c, encoding="utf-8").read()]


# L'état se lit sur une SENTINELLE et non en cherchant les anciens textes :
# ici le nouveau texte contient l'ancien (la fonction est insérée juste avant
# jrChoisir, qui reste), donc « l'ancien est encore là » ne veut plus dire
# « la greffe n'est pas posée ». Se fier aux textes obligerait à tordre chaque
# ancre jusqu'à ce qu'aucune ne soit ni préfixe ni suffixe de son remplaçant.
SENTINELLE = "function jrSansTexte("


def poser(chemin, retirer):
    s = io.open(chemin, encoding="utf-8").read()
    if (SENTINELLE in s) != bool(retirer):
        return "déjà fait"
    ps = [(b, a) for a, b in PAIRES] if retirer else PAIRES
    for avant, apres in ps:
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
