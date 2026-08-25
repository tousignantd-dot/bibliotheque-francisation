#!/usr/bin/env python3
"""La réponse écrite ne se donne plus au premier essai.

Un élève qui envoie une réponse fautive dans « Je me lance » recevait, du même
coup, un commentaire ET la phrase corrigée. Il la lisait, la recopiait, passait
à la suite : le seul moment où il apprenait quelque chose — réparer sa propre
phrase — était escamoté. La greffe installe un cycle en deux temps :

  essai 1 — un commentaire qui SITUE l'erreur, sans écrire la réponse, et un
            bouton « Montrez-moi la réponse » pour qui est bloqué ;
  essai 2 — la réponse vient d'elle-même, avec l'invitation à la réécrire ;
  après   — la case reste ouverte, la vérification se fait sur place.

Le ton du commentaire est décidé côté serveur : le module envoie le numéro
d'essai à /api/check-written (voir server.py, _handle_check_written), et la
consigne du premier essai interdit d'écrire la phrase attendue.

Le bouton ne coûte AUCUN appel : la correction arrive déjà avec le commentaire,
le module la garde simplement de côté. Seul un vrai deuxième envoi paie un
second appel — et c'est exactement là qu'il vaut la peine d'être payé.

    python3 build/greffe_deux_essais.py            # gabarit + les onze modules
    python3 build/greffe_deux_essais.py --tous     # gabarit + les 87 modules
    python3 build/greffe_deux_essais.py --retirer  # revient en arrière

La greffe est idempotente : elle se repose sans dommage, et un fichier déjà
greffé est laissé tel quel. Elle vise le gabarit ET les fichiers livrés, parce
que sept modules du niveau 4 n'ont plus de `build/contenu/<slug>/` et ne se
reconstruisent donc pas — module-procedure le premier.

ATTENTION : le gabarit est partagé par les 87 modules. Une fois greffé, tout
module reconstruit prendra le nouveau comportement, greffé ou non. Laisser
l'écart ouvert longtemps, c'est se garantir deux comportements dans la même
classe : mieux vaut passer --tous dès que la forme est validée.
"""

import argparse
import glob
import io
import sys

GABARIT = "build/gabarit/module.html"
TOUS = "assets/interactive/module-*/module-*-activite-interactive.html"

# Les onze modules du niveau 4 dans l'ordre du registre (build/powerpoints/
# modules.py) — ceux du chantier de réécriture, les seuls visés par défaut.
ONZE = [
    "module-consultation", "module-urgence", "module-sante", "module-travail",
    "module-procedure", "module-nouvelles", "module-meteo", "module-pub",
    "module-logement", "module-probleme", "module-relations",
]

ANCIEN = r"""async function checkWrite(exId, i){
  const ex=EXOS.find(e=>e.id===exId); if(!ex) return;
  const it=ex.items[i];
  const inp=document.getElementById('wi_'+exId+'_'+i);
  const fb=document.getElementById('wf_'+exId+'_'+i);
  const val=inp.value.trim();
  const zid='w_'+exId+'_'+i;
  if(!val){ fb.className='wfb no'; fb.textContent="✏️ Écris ta réponse d'abord."; return; }

  // Mode autocorrection (réponse connue)
  if(it.accept){
    const ok=it.accept.map(normWrite).includes(normWrite(val));
    fb.className='wfb '+(ok?'ok':'no');
    fb.innerHTML= ok ? '✅ Bravo, c\'est exact !'
      : '❌ Presque ! La bonne réponse est : <b>'+esc(it.accept[0])+'</b>';
    if(ok){ inp.classList.add('good'); inp.disabled=true; trackPlacement(zid,true); }
    else {
      trackPlacement(zid,false);
      // Ici le cumul a du sens : chaque envoi raté est une tentative distincte.
      const rates = ex.items.reduce((s,_,k)=> s + (TR.attempts['w_'+exId+'_'+k]||0), 0);
      evaluerAide(exId, rates);
    }
    return;
  }

  // Mode IA (réponse ouverte)
  fb.className='wfb wait'; fb.textContent='⏳ L\'assistant corrige ta réponse…';
  const btn=inp.parentElement.querySelector('.wbtn'); if(btn) btn.disabled=true;
  try{
    const res=await fetch('/api/check-written',{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({code:studentCode, consigne:(ex.sub||'')+' '+(it.q||''), reponse:val, attendu:it.hint||''})});
    const d=await res.json();
    if(btn) btn.disabled=false;
    if(!res.ok){ fb.className='wfb no'; fb.textContent=d.error||'Service momentanément indisponible.'; return; }
    fb.className='wfb '+(d.correct?'ok':'no');
    let html=(d.correct?'✅ ':'💡 ')+esc(d.feedback||'');
    if(!d.correct && d.correction){ html+='<br><b>Suggestion :</b> '+esc(d.correction); }
    fb.innerHTML=html;
    if(d.correct){ inp.classList.add('good'); trackPlacement(zid,true); }
  }catch(e){
    if(btn) btn.disabled=false;
    fb.className='wfb no'; fb.textContent='Impossible de contacter le serveur. Réessaie.';
  }
}
"""

NOUVEAU = r"""// La réponse n'arrive pas au premier essai. Un élève à qui on montre la
// phrase corrigée dès le premier envoi la recopie et passe : le seul moment
// où il apprend quelque chose, la réparation de sa propre phrase, est
// escamoté. Donc : essai 1, un commentaire qui situe l'erreur, et le choix
// entre retenter et cliquer « Montrez-moi la réponse ». Essai 2 raté, la
// réponse vient d'elle-même — faire deviner un troisième tour décourage.
// WESSAI compte les essais ratés, WSOL garde la réponse à dévoiler, WFB le
// dernier commentaire (pour ne pas le perdre quand on ajoute la réponse).
const WESSAI={}, WSOL={}, WFB={};

function wBoutonReponse(exId, i){
  return '<br><button type="button" class="btn btn-ghost" style="margin-top:8px;padding:7px 12px;font-size:12px" '
    + 'onclick="wDevoiler(\'' + exId + '\',' + i + ')">Montrez-moi la réponse</button>';
}

// Le bouton ne coûte aucun appel : la correction est déjà arrivée avec le
// commentaire, le module la gardait simplement de côté. Dévoiler clôt le
// cycle (essai forcé à 2) et rouvre la case : lire une phrase ne laisse pas
// la trace que laisse le fait de la réécrire.
function wDevoiler(exId, i){
  const k=exId+'_'+i, sol=WSOL[k];
  if(!sol) return;
  WESSAI[k]=Math.max(WESSAI[k]||0, 2);
  const fb=document.getElementById('wf_'+exId+'_'+i);
  const inp=document.getElementById('wi_'+exId+'_'+i);
  fb.className='wfb no';
  fb.innerHTML=(WFB[k]?WFB[k]+'<br>':'')+'<b>La réponse :</b> '+esc(sol)
    +'<br><span style="font-weight:600">Réécris-la dans la case, puis vérifie.</span>';
  if(inp){ inp.value=''; inp.focus(); }
}

async function checkWrite(exId, i){
  const ex=EXOS.find(e=>e.id===exId); if(!ex) return;
  const it=ex.items[i];
  const inp=document.getElementById('wi_'+exId+'_'+i);
  const fb=document.getElementById('wf_'+exId+'_'+i);
  const val=inp.value.trim();
  const zid='w_'+exId+'_'+i;
  const k=exId+'_'+i;
  if(!val){ fb.className='wfb no'; fb.textContent="✏️ Écris ta réponse d'abord."; return; }

  // Mode autocorrection (réponse connue)
  if(it.accept){
    const ok=it.accept.map(normWrite).includes(normWrite(val));
    if(ok){
      fb.className='wfb ok'; fb.innerHTML='✅ Bravo, c\'est exact !';
      inp.classList.add('good'); inp.disabled=true; trackPlacement(zid,true);
      return;
    }
    WESSAI[k]=(WESSAI[k]||0)+1;
    WSOL[k]=it.accept[0];
    WFB[k]='❌ Presque !';
    fb.className='wfb no';
    fb.innerHTML = (WESSAI[k]<2)
      ? '❌ Presque ! Relis ta réponse et essaie encore.'+wBoutonReponse(exId,i)
      : '💡 La réponse est : <b>'+esc(it.accept[0])+'</b>'
        +'<br><span style="font-weight:600">Réécris-la dans la case, puis vérifie.</span>';
    trackPlacement(zid,false);
    // Ici le cumul a du sens : chaque envoi raté est une tentative distincte.
    const rates = ex.items.reduce((s,_,k2)=> s + (TR.attempts['w_'+exId+'_'+k2]||0), 0);
    evaluerAide(exId, rates);
    return;
  }

  // Mode IA (réponse ouverte)
  // La réponse est déjà sortie : on ne rappelle plus le serveur. Un troisième
  // appel ne dirait rien de neuf et se paierait à chaque frappe. On compare
  // sur place, et une phrase écrite autrement n'est pas comptée comme fautive.
  if(WSOL[k] && (WESSAI[k]||0)>=2){
    const juste = normWrite(val)===normWrite(WSOL[k]);
    fb.className='wfb '+(juste?'ok':'no');
    fb.innerHTML = juste
      ? '✅ Voilà, tu l\'as réécrite.'
      : '💡 C\'est noté. La phrase à écrire : <b>'+esc(WSOL[k])+'</b>';
    if(juste){ inp.classList.add('good'); trackPlacement(zid,true); }
    return;
  }
  fb.className='wfb wait'; fb.textContent='⏳ L\'assistant corrige ta réponse…';
  const btn=inp.parentElement.querySelector('.wbtn'); if(btn) btn.disabled=true;
  const essai=(WESSAI[k]||0)+1;
  try{
    const res=await fetch('/api/check-written',{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({code:studentCode, consigne:(ex.sub||'')+' '+(it.q||''), reponse:val, attendu:it.hint||'', essai:essai})});
    const d=await res.json();
    if(btn) btn.disabled=false;
    if(!res.ok){ fb.className='wfb no'; fb.textContent=d.error||'Service momentanément indisponible.'; return; }
    if(d.correct){
      fb.className='wfb ok'; fb.innerHTML='✅ '+esc(d.feedback||'');
      inp.classList.add('good'); trackPlacement(zid,true);
      return;
    }
    WESSAI[k]=essai;
    WSOL[k]=d.correction||'';
    WFB[k]='💡 '+esc(d.feedback||'');
    fb.className='wfb no';
    if(!WSOL[k]) fb.innerHTML=WFB[k];
    else if(essai<2) fb.innerHTML=WFB[k]+wBoutonReponse(exId,i);
    else fb.innerHTML=WFB[k]+'<br><b>La réponse :</b> '+esc(WSOL[k])
      +'<br><span style="font-weight:600">Réécris-la dans la case, puis vérifie.</span>';
  }catch(e){
    if(btn) btn.disabled=false;
    fb.className='wfb no'; fb.textContent='Impossible de contacter le serveur. Réessaie.';
  }
}
"""


def cibles(tous):
    if tous:
        return [GABARIT] + sorted(glob.glob(TOUS))
    return [GABARIT] + [
        "assets/interactive/{0}/{0}-activite-interactive.html".format(s) for s in ONZE
    ]


def poser(chemin, retirer):
    avant, apres = (NOUVEAU, ANCIEN) if retirer else (ANCIEN, NOUVEAU)
    try:
        s = io.open(chemin, encoding="utf-8").read()
    except IOError:
        return "absent"
    if avant not in s:
        return "déjà fait" if apres in s else "introuvable"
    io.open(chemin, "w", encoding="utf-8").write(s.replace(avant, apres, 1))
    return "greffé" if not retirer else "retiré"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--tous", action="store_true",
                    help="poser sur les 87 modules, pas seulement les onze")
    ap.add_argument("--retirer", action="store_true", help="revenir en arrière")
    args = ap.parse_args()

    compte = {}
    for chemin in cibles(args.tous):
        etat = poser(chemin, args.retirer)
        compte[etat] = compte.get(etat, 0) + 1
        if etat in ("introuvable", "absent"):
            print("  ! {} — {}".format(chemin, etat))
    for etat in sorted(compte):
        print("{:>4}  {}".format(compte[etat], etat))
    return 1 if compte.get("introuvable") or compte.get("absent") else 0


if __name__ == "__main__":
    sys.exit(main())
