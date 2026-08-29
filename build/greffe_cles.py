#!/usr/bin/env python3
"""La réponse écrite ne se juge plus au caractère près.

Relevé le 28 août 2026 sur `module-logement`, exercice des petites annonces.
L'élève répond « annonce 2 » ; le module refuse, puis affiche « L'annonce 2 :
cinq pièces, deux salles de bain, une école et un parc tout près » et lui
demande de la RÉÉCRIRE dans la case. Aucun élève de francisation n'y arrivera :
la comparaison était une égalité de chaîne, et la phrase fait quinze mots.

Le compte, sur les 77 modules générés : 3 904 items à liste fermée, dont
2 904 n'attendent qu'un seul mot — là, l'égalité exacte est la bonne règle.
Mais **159 items attendent quatre mots ou plus**, 29 en attendent huit et
plus, et 186 items ouverts finissent au même endroit quand l'IA a refusé deux
fois. Ce sont ceux-là que la greffe répare.

Ce qu'elle installe, sans le moindre appel à l'IA
-------------------------------------------------
`cles` — un champ d'item, facultatif : des GROUPES de termes équivalents. La
réponse passe dès qu'elle touche un terme de chaque groupe, dans n'importe
quel ordre, sans accents ni ponctuation, avec les équivalences de nombres
(2 ↔ deux ↔ deuxième, ½ ↔ et demi). Un groupe peut porter un libellé, et
c'est là le vrai gain : le module DIT ce qui manque.

    {q:"Quelle annonce conviendrait à une famille de quatre personnes ? Pourquoi ?",
     hint:"L'annonce 2 : cinq pièces, deux salles de bain, une école et un parc.",
     cles:[{q:"quelle annonce", mots:["annonce 2","la 2","5 ½","triplex"]},
           {q:"pourquoi", mots:["grand","5 pieces","2 salles de bain","ecole","parc"]}]}

    → « annonce 2 » seul : « ✅ Tu tiens une partie de la réponse.
      Il manque : pourquoi. »  C'est exactement ce que la question demandait.

`couvre` — le filet pour les items sans `cles`. Au-delà de trois mots
attendus, on compare les mots de contenu et non la forme : 80 % suffisent.
Une phrase juste, ponctuée ou ordonnée autrement, cesse d'être une faute. En
deçà de quatre mots, rien ne change — « arriverai », c'est « arriverai ».

`sauf` — la parade à la négation. « Ce n'est pas l'annonce 2 » contient tous
les bons termes ; c'est le trou connu de la méthode, et le seul prix à payer
pour se passer de l'IA.

Ce que la greffe ne fait pas
---------------------------
Elle n'écrit AUCUN `cles` dans les modules : elle installe le moteur. Les 159
items longs restent à équiper un par un, et c'est un travail de jugement.
Entre-temps ils profitent déjà de `couvre`, ce qui suffit à faire disparaître
le « réécris-la au caractère près ».

    python3 build/greffe_cles.py            # gabarit + les onze modules
    python3 build/greffe_cles.py --tous     # gabarit + les 87 modules
    python3 build/greffe_cles.py --retirer  # revient en arrière

Idempotente : un fichier déjà greffé est laissé tel quel. Elle vise le gabarit
ET les fichiers livrés, parce que les modules d'avant le gabarit — dont
`module-logement`, justement celui du relevé — ne se reconstruisent pas.

ATTENTION : le gabarit est partagé par les 87 modules. Une fois greffé, tout
module reconstruit prend le nouveau comportement, greffé ou non. Passer
--tous dès que la forme est validée, sinon deux comportements coexistent dans
la même classe.
"""

import argparse
import glob
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

ANCIEN = r"""const WESSAI={}, WSOL={}, WFB={};

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
  // La réponse attendue est déjà là, en clair, dans l'item : quand l'élève la
  // dit, il est inutile de la faire relire à un assistant — et surtout de la
  // payer. C'est aussi ce qui réparait le cas relevé le 28 août 2026 : une
  // bonne réponse refusée au premier envoi, puis exigée au caractère près.
  const attenduIA = reponseAttendue(it);
  if(attenduIA && couvre(attenduIA, val) >= COUV_MIN){
    fb.className='wfb ok'; fb.innerHTML='✅ Bravo, c\'est exact !';
    inp.classList.add('good'); trackPlacement(zid,true);
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

NOUVEAU = r"""const WESSAI={}, WSOL={}, WFB={};

// ── CONTRÔLE PAR TERMES-CLÉS ────────────────────────────────────────────
// Une réponse écrite était jugée par égalité de chaîne. Pour « arriverai »,
// c'est juste. Pour « L'annonce 2 : cinq pièces, deux salles de bain, une
// école et un parc tout près », c'est un test de dactylographie : aucun élève
// ne retrouve une phrase de quinze mots au caractère près, et le module lui
// répondait « Presque ! » puis lui demandait de la recopier. Relevé le
// 28 août 2026 sur module-logement, et vrai de 159 items du cours qui
// attendent quatre mots ou plus.
//
// Deux remèdes, tous deux sans appel à l'IA :
//
//   `cles` — l'auteur écrit des GROUPES de termes équivalents, et la réponse
//   passe dès qu'elle touche un terme de chaque groupe, dans n'importe quel
//   ordre. Le gain n'est pas que d'accepter plus large : un groupe manqué se
//   nomme, donc l'élève lit ce qui manque au lieu d'un refus sec.
//
//   `couvre` — le filet, pour les items sans `cles`. Au-delà de trois mots
//   attendus, la comparaison se fait sur les mots de contenu et non sur la
//   forme : une phrase juste, ponctuée autrement, n'est plus une faute.
//
// Ce que ça ne fait pas, et il vaut mieux l'écrire : « ce n'est pas
// l'annonce 2 » contient tous les bons termes. C'est à quoi sert `sauf`, et
// la négation reste le trou de la méthode. C'est le prix de se passer de
// l'IA, et il est petit devant celui qu'on payait.
const WSTOP = new Set(('a au aux avec c ce ces cet cette d dans de des du elle en est et '
  + 'eux il ils j je l la le les leur lui ma mais me mes moi mon n ne nos notre nous on '
  + 'ou par pas plus pour qu que qui sa se ses son sont sur ta te tes toi ton tous tout '
  + 'tres tu un une vos votre vous y').split(' '));

// Les équivalences s'appliquent des DEUX côtés, donc une même ambiguïté ne
// crée pas d'écart. « neuf » et « seconde » sont laissés de côté justement
// parce qu'ils en créeraient une : un logement neuf n'est pas un 9.
function normCle(s){
  return (s||'').toString().toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'')
    .replace(/½/g,' et demi').replace(/(\d)\s*1\/2/g,'$1 et demi')
    .replace(/\bpremieres?\b|\bpremiers?\b|\b1(?:er|re|ere)\b/g,'1')
    .replace(/\bdeuxiemes?\b|\b2e\b/g,'2')
    .replace(/\btroisiemes?\b|\b3e\b/g,'3')
    .replace(/\bquatriemes?\b|\b4e\b/g,'4')
    .replace(/\bcinquiemes?\b|\b5e\b/g,'5')
    .replace(/\bdeux\b/g,'2').replace(/\btrois\b/g,'3').replace(/\bquatre\b/g,'4')
    .replace(/\bcinq\b/g,'5').replace(/\bsix\b/g,'6').replace(/\bsept\b/g,'7')
    .replace(/\bhuit\b/g,'8').replace(/\bdix\b/g,'10')
    .replace(/[^a-z0-9]+/g,' ').replace(/\s+/g,' ').trim();
}
function motsUtiles(s){
  return normCle(s).split(' ').filter(m=>m.length>1 && !WSTOP.has(m));
}
// La part des mots de contenu attendus qui se retrouvent dans la réponse.
function couvre(attendu, donne){
  const a=motsUtiles(attendu); if(!a.length) return 0;
  const d=new Set(motsUtiles(donne));
  return a.filter(m=>d.has(m)).length / a.length;
}
const COUV_MIN = 0.8;
// Le seuil se compte en MOTS DE CONTENU, pas en mots. Compté sur les mots
// bruts, « a-t-elle été » en fait quatre et tombait dans le filet : « a-t-il
// été » y devenait juste, puisque tout ce qui les distingue est un mot vide.
// Douze items de grammaire du cours étaient dans ce cas, relevés par le
// contrôle des leurres. En mots de contenu, ils en font un — le filet les
// laisse tranquilles, et c'est ce qu'il faut : là, la forme EST la réponse.
//
// Trois et non quatre : le seuil a été choisi en mesurant, sur les 3 904
// items à liste fermée, combien d'items le filet couvre et combien de
// réponses d'une AUTRE question il laisserait passer. À 4 : 25 items
// couverts, 0 confusion. À 3 : 105 items couverts, 0 confusion. À 2 : 492
// items, mais 6 confusions. Trois est le dernier seuil encore gratuit.
const LONG_MIN = 3;

// Un groupe s'écrit ['annonce 2','la 2','triplex'] — ou, pour que le module
// puisse DIRE ce qui manque, {q:"pourquoi elle convient", mots:[…]}.
// Un `hint` n'est pas toujours une réponse : dans les items de production
// libre il commence par « Ex. : » et n'est qu'un modèle parmi d'autres. Le
// distinguer permet d'accepter une bonne réponse sans déranger l'assistant —
// et, dans les centres qui refusent l'IA, d'accepter tout court.
function reponseAttendue(it){
  const h=(it && it.hint || '').trim();
  if(!h) return '';
  if(/^(ex\.|exemple|reponse personnelle|réponse personnelle)/i.test(h)) return '';
  return h;
}
function verifCles(it, val){
  const n=' '+normCle(val)+' ';
  const dedans = t => n.includes(' '+normCle(t)+' ');
  for(const t of (it.sauf||[])) if(dedans(t))
    return {ok:false, msg:'❌ Relis la question : ta phrase dit le contraire.'};
  const manque=[];
  for(const g0 of it.cles){
    const g = Array.isArray(g0) ? {q:'', mots:g0} : g0;
    if(!(g.mots||[]).some(dedans)) manque.push(g.q||'');
  }
  if(!manque.length) return {ok:true, msg:''};
  const nommes=manque.filter(Boolean);
  const partiel=manque.length < it.cles.length;
  return {ok:false, msg:(partiel ? '💡 Tu tiens une partie de la réponse. ' : '❌ Pas encore. ')
    + (nommes.length ? 'Il manque : <b>'+nommes.join('</b>, <b>')+'</b>.'
                     : 'Relis la question : elle demande plus que ça.')};
}

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
    +'<br><span style="font-weight:600">Écris-la à ta façon, puis vérifie.</span>';
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

  // Termes-clés : passe avant tout le reste, et ne demande jamais de copie.
  if(it.cles){
    const r=verifCles(it, val);
    if(r.ok){
      fb.className='wfb ok'; fb.innerHTML='✅ Bravo, c\'est exact !';
      inp.classList.add('good'); inp.disabled=true; trackPlacement(zid,true);
      return;
    }
    WESSAI[k]=(WESSAI[k]||0)+1;
    const modele=it.hint||(it.accept&&it.accept[0])||'';
    fb.className='wfb no';
    fb.innerHTML = r.msg + ((WESSAI[k]>=2 && modele)
      ? '<br><b>Un exemple de réponse :</b> '+esc(modele)
        +'<br><span style="font-weight:600">Écris-la à ta façon, puis vérifie.</span>'
      : '');
    trackPlacement(zid,false);
    const ratesC = ex.items.reduce((s,_,k2)=> s + (TR.attempts['w_'+exId+'_'+k2]||0), 0);
    evaluerAide(exId, ratesC);
    return;
  }

  // Mode autocorrection (réponse connue)
  if(it.accept){
    const long = motsUtiles(it.accept[0]).length >= LONG_MIN;
    const ok = it.accept.map(normWrite).includes(normWrite(val))
            || (long && it.accept.some(a=>couvre(a,val)>=COUV_MIN));
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
        +'<br><span style="font-weight:600">'
        +(long?'Écris-la à ta façon, puis vérifie.':'Réécris-la dans la case, puis vérifie.')
        +'</span>';
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
    const juste = normWrite(val)===normWrite(WSOL[k]) || couvre(WSOL[k], val)>=COUV_MIN;
    fb.className='wfb '+(juste?'ok':'no');
    fb.innerHTML = juste
      ? '✅ Voilà, tu l\'as écrite.'
      : '💡 C\'est noté. Ce qu\'il fallait dire : <b>'+esc(WSOL[k])+'</b>';
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
      +'<br><span style="font-weight:600">Écris-la à ta façon, puis vérifie.</span>';
  }catch(e){
    if(btn) btn.disabled=false;
    fb.className='wfb no'; fb.textContent='Impossible de contacter le serveur. Réessaie.';
  }
}"""


def cibles(tous):
    fichiers = [GABARIT]
    for p in sorted(glob.glob(TOUS)):
        slug = p.split("/")[1]
        if tous or slug in ONZE:
            fichiers.append(p)
    return fichiers


def traiter(chemin, retirer):
    """(état, chemin) — 'greffé', 'dégreffé', 'déjà', 'sans objet'."""
    with open(chemin, encoding="utf-8") as f:
        t = f.read()
    avant, apres = (NOUVEAU, ANCIEN) if retirer else (ANCIEN, NOUVEAU)
    if avant not in t:
        return ("déjà" if apres in t else "sans objet"), chemin
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(t.replace(avant, apres, 1))
    return ("dégreffé" if retirer else "greffé"), chemin


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--tous", action="store_true", help="les 87 modules")
    ap.add_argument("--retirer", action="store_true", help="revenir en arrière")
    a = ap.parse_args()

    comptes = {}
    perdus = []
    for chemin in cibles(a.tous):
        etat, _ = traiter(chemin, a.retirer)
        comptes[etat] = comptes.get(etat, 0) + 1
        if etat == "sans objet":
            perdus.append(chemin)

    for etat in ("greffé", "dégreffé", "déjà", "sans objet"):
        if comptes.get(etat):
            print("%-12s %d" % (etat, comptes[etat]))
    if perdus:
        print("\n⚠️  ni l'ancien ni le nouveau bloc — ces fichiers ont divergé :")
        for p in perdus:
            print("   ", p)
        sys.exit(1)


if __name__ == "__main__":
    main()
