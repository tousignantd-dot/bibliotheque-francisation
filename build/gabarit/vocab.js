// ── SECTION VOCABULAIRE ───────────────────────────────────────────────
// Trois exercices sur la même liste de mots (FC_CARDS), plus la traduction
// en langue maternelle. La seule entrée est la liste de mots : ce bloc est
// le même pour tous les modules, seul fccards.js change.
//
//   1. Le mot et sa définition   — association par clic, six mots à la fois
//   2. Je me souviens du mot     — rappel actif, notation, reprise des ratés
//   3. Le mot et son image       — trois choix mélangés, sauté s'il n'y a
//                                  aucune photo dans la liste
//
// Le pointage global (l'étoile en haut) ne compte que l'exercice 1 : c'est
// le seul dont les zones sont déclarées dans ZONES. Les exercices 2 et 3
// tiennent leur propre compteur et n'appellent jamais trackPlacement(), qui
// gonflerait le total de l'étoile avec des identifiants inconnus.

const VOC_LANGUES = [
  {c:'ar', n:'arabe',      loc:'العربية',    rtl:true},
  {c:'es', n:'espagnol',   loc:'Español'},
  {c:'uk', n:'ukrainien',  loc:'Українська'},
  {c:'fa', n:'persan',     loc:'فارسی',      rtl:true},
  {c:'zh', n:'chinois (mandarin)', loc:'中文'},
  {c:'pt', n:'portugais',  loc:'Português'},
  {c:'en', n:'anglais',    loc:'English'},
  {c:'ro', n:'roumain',    loc:'Română'},
  {c:'ur', n:'ourdou',     loc:'اردو',       rtl:true},
  {c:'ru', n:'russe',      loc:'Русский'},
  {c:'ti', n:'tigrigna',   loc:'ትግርኛ'},
];
// La langue est choisie une fois et vaut pour tous les modules ; les
// traductions déjà payées sont partagées par tous les élèves de l'appareil.
const VOC_LS_LANGUE = 'francisation-langue';
const VOC_LS_TRAD   = 'francisation-traductions';
const VOC_LS_RAPPEL = 'francisation-rappel-' + MODULE_SLUG;
const VOC_TAILLE_GROUPE = 6;   // exercice 1 : mots montrés à la fois
const VOC_TAILLE_PAQUET = 8;   // exercice 2 : mots par paquet

// Le mode privé de Safari fait lever localStorage : on ne perd que la
// mémoire, jamais l'exercice.
function vocLire(cle, defaut){
  try{ const v = localStorage.getItem(cle); return v===null ? defaut : JSON.parse(v); }
  catch(e){ return defaut; }
}
function vocEcrire(cle, valeur){
  try{ localStorage.setItem(cle, JSON.stringify(valeur)); }catch(e){}
}

function vocLangue(){
  const c = vocLire(VOC_LS_LANGUE, '');
  return VOC_LANGUES.find(l=>l.c===c) || null;
}

// ── LA TRADUCTION ─────────────────────────────────────────────────────
// Masquée par défaut : une traduction visible d'emblée et le français n'est
// plus traité. L'appel part vers le serveur, jamais vers l'API directement —
// la clé Anthropic ne descend pas dans le navigateur.
function vocEmpreinte(texte){
  let h = 5381;
  for(let i=0;i<texte.length;i++) h = ((h*33) ^ texte.charCodeAt(i)) >>> 0;
  return h.toString(36);
}
// La définition entre dans la clé : deux modules peuvent définir le même mot
// autrement, et la traduction de l'un ne doit pas s'afficher chez l'autre.
function vocCle(langue, mot, def){
  return langue + '|' + mot + '|' + vocEmpreinte(def||'');
}
async function vocTraduire(mot, def, exemple){
  const L = vocLangue();
  if(!L) throw new Error('langue');
  const cle = vocCle(L.c, mot, def);
  const cache = vocLire(VOC_LS_TRAD, {});
  if(cache[cle]) return cache[cle];
  const res = await fetch('/api/vocab/translate', {
    method:'POST', headers:{'Content-Type':'application/json'},
    body: JSON.stringify({code:studentCode, langue:L.n, mot:mot, definition:def, exemple:exemple||''})
  });
  const data = await res.json();
  if(!res.ok) throw new Error(data.error||'indisponible');
  cache[cle] = data;
  vocEcrire(VOC_LS_TRAD, cache);
  return data;
}

let vocTradNo = 0;
// Renvoie le balisage du bouton + du bloc masqué ; vocTradBrancher() pose
// ensuite les écouteurs, une fois le balisage dans la page.
function vocTradBalisage(){
  const id = 'voctr' + (++vocTradNo);
  return {id,
    html:'<div class="vc-actions"><button type="button" class="btn btn-ghost" id="'+id+'-btn">Voir dans ma langue</button></div>'
       + '<div class="voc-tr" id="'+id+'" hidden aria-live="polite"></div>'};
}
function vocTradBrancher(id, mot, def, exemple){
  const btn = document.getElementById(id+'-btn');
  const box = document.getElementById(id);
  if(!btn || !box) return;
  btn.addEventListener('click', async ()=>{
    if(!box.hidden){
      box.hidden = true; btn.textContent = 'Voir dans ma langue'; return;
    }
    const L = vocLangue();
    box.hidden = false; box.removeAttribute('dir');
    if(!L){
      box.innerHTML = '<div class="voc-tr-att">Choisissez d\'abord votre langue, en haut de la section.</div>';
      return;
    }
    box.innerHTML = '<div class="voc-tr-att">Traduction en cours…</div>';
    btn.disabled = true;
    try{
      const t = await vocTraduire(mot, def, exemple);
      if(L.rtl) box.setAttribute('dir','rtl');
      let h = '<div class="voc-tr-mot">'+esc(t.traduction||'')+'</div>';
      if(t.definitionTraduite) h += '<div class="voc-tr-def">'+esc(t.definitionTraduite)+'</div>';
      if(t.exempleTraduit)     h += '<div class="voc-tr-ex">'+esc(t.exempleTraduit)+'</div>';
      h += '<button type="button" class="voc-flag">Signaler une traduction douteuse</button>';
      box.innerHTML = h;
      box.querySelector('.voc-flag').addEventListener('click', function(){ vocSignaler(this, mot, t); });
      btn.textContent = 'Cacher la traduction';
    }catch(e){
      // Message neutre en français : jamais l'erreur brute, hors ligne comprise.
      box.innerHTML = '<div class="voc-tr-att">La traduction n\'est pas disponible pour le moment. Vous pouvez continuer l\'exercice en français.</div>';
    }
    btn.disabled = false;
  });
}
// Les traductions ne sont pas révisées par un humain. Le signalement est
// journalisé côté serveur ; c'est ce qui permettra plus tard une liste revue.
async function vocSignaler(btn, mot, t){
  const L = vocLangue();
  btn.disabled = true;
  btn.textContent = 'Envoi…';
  try{
    const res = await fetch('/api/vocab/signaler', {
      method:'POST', headers:{'Content-Type':'application/json'},
      body: JSON.stringify({code:studentCode, module:MODULE_SLUG, mot:mot,
        langue: L ? L.n : '',
        traduction: [t.traduction, t.definitionTraduite].filter(Boolean).join(' — ')})
    });
    btn.textContent = res.ok ? '✓ Merci, c\'est noté.' : 'Le signalement n\'est pas parti.';
  }catch(e){
    btn.textContent = 'Le signalement n\'est pas parti.';
  }
}

// ── EN-TÊTE DE SECTION : le choix de la langue ────────────────────────
function vocEnteteHtml(){
  return '<div class="voc-head" id="voc-head">'
    + '<span class="voc-head-t"><label for="voc-lang">Ma langue maternelle</label></span>'
    + '<select class="voc-lang" id="voc-lang">'
    + '<option value="">— Choisissez votre langue —</option>'
    + VOC_LANGUES.map(l=>'<option value="'+l.c+'">'+esc(l.loc)+' · '+esc(l.n)+'</option>').join('')
    + '</select>'
    + '<span class="voc-head-s">Les mots restent en français. La traduction s\'affiche seulement quand vous la demandez.</span>'
    + '</div>';
}
function vocEnteteBrancher(){
  const sel = document.getElementById('voc-lang');
  if(!sel) return;
  sel.value = vocLire(VOC_LS_LANGUE, '');
  sel.addEventListener('change', ()=>{
    vocEcrire(VOC_LS_LANGUE, sel.value);
    // Les blocs déjà ouverts montrent l'ancienne langue : on les referme.
    document.querySelectorAll('.voc-tr').forEach(b=>{ b.hidden = true; });
    document.querySelectorAll('[id$="-btn"].btn-ghost').forEach(b=>{
      if(b.textContent.indexOf('traduction')>=0) b.textContent = 'Voir dans ma langue';
    });
  });
}

// ── EXERCICE 1 · Le mot et sa définition ──────────────────────────────
// Association par clic en deux colonnes, atteignable au clavier. Six mots à
// la fois : seize définitions d'un coup, personne ne lit jusqu'en bas.
function vocNbGroupes(ex){
  return Math.max(1, Math.ceil(ex.rows.length / VOC_TAILLE_GROUPE));
}
function vocGroupeCourant(ex){
  if(!S.vocabFile){
    S.vocabFile = ex.rows.map((r,i)=>i).sort(()=>Math.random()-.5);
    S.vocabGroupNo = 0;
    S.vocabOrderNo = -1;
  }
  return S.vocabFile.slice(S.vocabGroupNo*VOC_TAILLE_GROUPE,
                          (S.vocabGroupNo+1)*VOC_TAILLE_GROUPE);
}
function renderVocabPairs(){
  const ex = EXOS.find(e=>e.id==='prVocab');
  if(!ex) return;
  const wordsEl = document.getElementById('vocab-words');
  const defsEl  = document.getElementById('vocab-defs');
  if(!wordsEl || !defsEl) return;

  const groupe = vocGroupeCourant(ex);
  // L'ordre des définitions est retiré au sort à chaque groupe : sinon la
  // deuxième reprise se joue de mémoire, par position.
  if(S.vocabOrderNo !== S.vocabGroupNo){
    S.vocabOrder = groupe.slice().sort(()=>Math.random()-.5);
    S.vocabOrderNo = S.vocabGroupNo;
  }

  wordsEl.innerHTML = groupe.map(idx=>{
    const r = ex.rows[idx];
    const done = S.vocabPairs[r.id] !== undefined;
    const cls = 'chip chip-word'+(done?' is-paired':(S.vocabPick===r.id?' is-active':''));
    return '<button type="button" class="'+cls+'" data-w="'+esc(r.id)+'"'+(done?' aria-disabled="true"':'')+'>'+esc(r.q)+'</button>';
  }).join('');
  const takenDefIds = Object.values(S.vocabPairs);
  defsEl.innerHTML = S.vocabOrder.map(idx=>{
    const r = ex.rows[idx];
    const done = takenDefIds.includes(r.aid);
    const cls = 'chip'+(done?' is-paired':(S.fb[r.aid]==='no'?' is-miss':''));
    return '<button type="button" class="'+cls+'" data-d="'+esc(r.aid)+'"'+(done?' aria-disabled="true"':'')+'>'+esc(r.a)+'</button>';
  }).join('');

  wordsEl.querySelectorAll('[data-w]').forEach(b=>b.addEventListener('click',()=>{
    const wid = b.dataset.w;
    if(S.vocabPairs[wid] !== undefined) return;
    S.vocabPick = (S.vocabPick===wid) ? null : wid;
    S.fb = {};
    renderVocabPairs();
  }));
  defsEl.querySelectorAll('[data-d]').forEach(b=>b.addEventListener('click',()=>{
    const did = b.dataset.d;
    if(Object.values(S.vocabPairs).includes(did) || S.vocabPick===null) return;
    const row = ex.rows.find(r=>r.id===S.vocabPick);
    const ok = row && row.aid===did;
    if(ok){ S.vocabPairs[S.vocabPick] = did; S.vocabPick=null; S.fb={}; trackPlacement(row.id, true); }
    else { S.fb[did]='no'; trackPlacement(row?row.id:did, false); }
    renderVocabPairs();
  }));

  const faits = groupe.filter(idx=>S.vocabPairs[ex.rows[idx].id]!==undefined).length;
  const scoreEl = document.getElementById('score-'+ex.id);
  if(scoreEl) scoreEl.textContent = faits+' / '+groupe.length+' associé · groupe '
    + (S.vocabGroupNo+1) + ' sur ' + vocNbGroupes(ex);
}
function vocabAutreGroupe(){
  const ex = EXOS.find(e=>e.id==='prVocab');
  if(!ex) return;
  vocGroupeCourant(ex);
  S.vocabGroupNo = (S.vocabGroupNo + 1) % vocNbGroupes(ex);
  S.vocabOrderNo = -1;
  S.vocabPick = null;
  S.fb = {};
  renderVocabPairs();
  const c = document.getElementById('exo-prVocab');
  if(c) c.scrollIntoView({behavior:'smooth', block:'start'});
}

// ── EXERCICE 2 · Je me souviens du mot ────────────────────────────────
// Rappel actif : le mot seul, puis la réponse, puis l'élève dit s'il savait.
// C'est la seule des trois activités qui fasse vraiment travailler la mémoire.
let VR = {paquet:[], i:0, su:0, revoir:[], revele:false};

// Résultats gardés d'un cours à l'autre : les mots « à revoir » repassent
// devant au prochain tirage.
function vocRappelHisto(){ return vocLire(VOC_LS_RAPPEL, {}); }
function vocRappelNoter(mot, su){
  const h = vocRappelHisto();
  const e = h[mot] || {su:0, revoir:0};
  if(su) e.su++; else e.revoir++;
  e.etat = su ? 'su' : 'revoir';
  e.dernier = new Date().toISOString().slice(0,10);
  h[mot] = e;
  vocEcrire(VOC_LS_RAPPEL, h);
}
function vocRappelTirage(){
  const h = vocRappelHisto();
  const rang = i=>{
    const e = h[FC_CARDS[i].word];
    if(!e) return 1;                    // jamais vu
    return e.etat==='revoir' ? 0 : 2;   // à revoir d'abord, su en dernier
  };
  return FC_CARDS.map((c,i)=>i)
    .sort((a,b)=> (rang(a)-rang(b)) || (Math.random()-.5))
    .slice(0, Math.min(VOC_TAILLE_PAQUET, FC_CARDS.length));
}
function vocRappelDemarrer(indices){
  VR = {paquet: indices && indices.length ? indices : vocRappelTirage(),
        i:0, su:0, revoir:[], revele:false};
  vocRappelRender();
}
function vocRappelRender(){
  const host = document.getElementById('vcRappelBody');
  const scoreEl = document.getElementById('score-vcRappel');
  if(!host) return;

  if(VR.i >= VR.paquet.length){
    const n = VR.revoir.length;
    if(scoreEl) scoreEl.textContent = VR.su+' / '+VR.paquet.length+' su';
    let h = '<div class="vc-bilan">'+(n===0
      ? '✓ Vous avez su les '+VR.paquet.length+' mots du paquet.'
      : (n===1 ? '1 mot reste à revoir.' : n+' mots restent à revoir.'))+'</div>';
    if(n) h += '<div class="vc-bilan-s">'+VR.revoir.map(i=>esc(FC_CARDS[i].word)).join(' · ')+'</div>';
    h += '<div class="vc-actions">';
    if(n) h += '<button type="button" class="btn btn-pri" id="vcReprise">Reprendre les mots à revoir</button>';
    h += '<button type="button" class="btn btn-ghost" id="vcNeuf">Un autre paquet de mots</button></div>';
    host.innerHTML = h;
    const rep = document.getElementById('vcReprise');
    if(rep) rep.addEventListener('click', ()=>vocRappelDemarrer(VR.revoir.slice()));
    document.getElementById('vcNeuf').addEventListener('click', ()=>vocRappelDemarrer(null));
    return;
  }

  const c = FC_CARDS[VR.paquet[VR.i]];
  if(scoreEl) scoreEl.textContent = VR.su+' / '+VR.paquet.length+' su';

  let h = '<div class="vc-carte"><div class="vc-mot">'+esc(c.word)+'</div>';
  if(!VR.revele){
    h += '<div class="vc-q">Que veut dire ce mot ?</div>'
       + '<div class="vc-actions"><button type="button" class="btn btn-pri" id="vcVoir">Voir la réponse</button></div></div>';
    host.innerHTML = h;
    document.getElementById('vcVoir').addEventListener('click', ()=>{ VR.revele = true; vocRappelRender(); });
    return;
  }

  const trad = vocTradBalisage();
  h += '</div><div class="vc-rep">'
     + '<div class="vc-def">'+esc(c.def)+'</div>'
     + '<div class="vc-ex">'+c.ex+'</div>'
     + trad.html
     + '<div class="vc-actions">'
     + '<button type="button" class="vc-note vc-note--su" id="vcSu">✓ Je le savais</button>'
     + '<button type="button" class="vc-note vc-note--revoir" id="vcRevoir">↺ À revoir</button>'
     + '</div></div>';
  host.innerHTML = h;
  vocTradBrancher(trad.id, c.word, c.def, c.ex);
  document.getElementById('vcSu').addEventListener('click', ()=>vocRappelSuivant(true));
  document.getElementById('vcRevoir').addEventListener('click', ()=>vocRappelSuivant(false));
}
function vocRappelSuivant(su){
  const idx = VR.paquet[VR.i];
  vocRappelNoter(FC_CARDS[idx].word, su);
  if(su) VR.su++; else VR.revoir.push(idx);
  VR.i++;
  VR.revele = false;
  vocRappelRender();
}

// ── EXERCICE 3 · Le mot et son image ──────────────────────────────────
// Une photo, trois mots, un seul juste. L'ordre des trois boutons est tiré
// au sort à chaque image : autrement la bonne réponse finit toujours au même
// endroit et l'élève répond à la position, pas au mot.
let VI = {ordre:[], i:0, juste:0, choix:[], repondu:false};

function vocImageMots(){ return FC_CARDS.map((c,i)=>i).filter(i=>FC_CARDS[i].img); }
function vocImageDemarrer(){
  VI = {ordre: vocImageMots().sort(()=>Math.random()-.5), i:0, juste:0, choix:[], repondu:false};
  vocImagePrepare();
}
function vocImagePrepare(){
  VI.repondu = false;
  const bon = VI.ordre[VI.i];
  if(bon === undefined){ VI.choix = []; vocImageRender(); return; }
  const leurres = FC_CARDS.map((c,i)=>i).filter(i=>i!==bon)
    .sort(()=>Math.random()-.5).slice(0,2);
  VI.choix = [bon].concat(leurres).sort(()=>Math.random()-.5);
  vocImageRender();
}
function vocImageRender(){
  const host = document.getElementById('vcImageBody');
  const scoreEl = document.getElementById('score-vcImage');
  if(!host) return;
  if(scoreEl) scoreEl.textContent = VI.juste+' / '+VI.ordre.length+' juste';

  if(VI.i >= VI.ordre.length){
    host.innerHTML = '<div class="vc-bilan">✓ Vous avez fait les '+VI.ordre.length+' images. '
      + VI.juste+' bonne'+(VI.juste>1?'s':'')+' réponse'+(VI.juste>1?'s':'')+'.</div>'
      + '<div class="vc-actions"><button type="button" class="btn btn-ghost" id="vcImgNeuf">Recommencer</button></div>';
    document.getElementById('vcImgNeuf').addEventListener('click', vocImageDemarrer);
    return;
  }

  const bon = VI.ordre[VI.i];
  let h = '<img class="vc-photo" src="'+esc(FC_CARDS[bon].img)+'" alt="Photo à associer à un mot de la liste">'
        + '<div class="vc-choix">'
        + VI.choix.map(i=>'<button type="button" class="choice" data-i="'+i+'">'+esc(FC_CARDS[i].word)+'</button>').join('')
        + '</div><div id="vcImgApres"></div>';
  host.innerHTML = h;
  host.querySelectorAll('.choice').forEach(b=>b.addEventListener('click', ()=>vocImageRepondre(parseInt(b.dataset.i,10))));
}
function vocImageRepondre(choisi){
  if(VI.repondu) return;
  VI.repondu = true;
  const bon = VI.ordre[VI.i];
  const ok = choisi === bon;
  if(ok) VI.juste++;
  // Le glyphe accompagne toujours la couleur — la couleur ne dit rien seule.
  document.querySelectorAll('#vcImageBody .choice').forEach(b=>{
    const i = parseInt(b.dataset.i,10);
    b.setAttribute('aria-disabled','true');
    if(i===bon){ b.classList.add(ok?'is-ok':'is-answer'); b.textContent = (ok?'✓ ':'← ')+FC_CARDS[i].word; }
    else if(i===choisi){ b.classList.add('is-no'); b.textContent = '✗ '+FC_CARDS[i].word; }
  });
  const scoreEl = document.getElementById('score-vcImage');
  if(scoreEl) scoreEl.textContent = VI.juste+' / '+VI.ordre.length+' juste';

  const apres = document.getElementById('vcImgApres');
  const c = FC_CARDS[bon];
  const trad = vocTradBalisage();
  apres.innerHTML = '<div class="vc-rep"><div class="vc-def">'+esc(c.def)+'</div>'
    + '<div class="vc-ex">'+c.ex+'</div>' + trad.html
    + '<div class="vc-actions"><button type="button" class="btn btn-pri" id="vcImgSuite">Une autre image</button></div></div>';
  vocTradBrancher(trad.id, c.word, c.def, c.ex);
  document.getElementById('vcImgSuite').addEventListener('click', ()=>{ VI.i++; vocImagePrepare(); });
}

// ── MONTAGE DE LA SECTION ─────────────────────────────────────────────
// Les identifiants des trois cartes, dans l'ordre d'affichage. toggleVocabExo
// s'en sert pour n'ouvrir que celles-là.
const VOC_CARTES = ['exo-prVocab', 'exo-vcRappel', 'exo-vcImage'];

function vocCarteHtml(id, num, titre, sous, score){
  return '<div class="card" id="'+id+'" style="display:none">'
    + '<div class="c-hdr"><span class="tag">'+esc(num)+'</span>'
    + '<span class="exo-score" id="score-'+id.replace('exo-','')+'" aria-live="polite">'+esc(score)+'</span>'
    + '<span class="ctit">'+esc(titre)+'</span><span class="csub">'+esc(sous)+'</span></div>'
    + '<div id="'+id.replace('exo-','')+'Body"></div></div>';
}
function vocabBuild(){
  const host = document.getElementById('exs-prep');
  const carteUn = document.getElementById('exo-prVocab');
  if(!host || !carteUn) return;

  // L'en-tête (choix de la langue) passe devant l'exercice 1.
  carteUn.insertAdjacentHTML('beforebegin', vocEnteteHtml());
  const tete = document.getElementById('voc-head');
  if(tete) tete.style.display = 'none';
  vocEnteteBrancher();

  // Exercice 2, puis exercice 3 — sauté si aucun mot n'a de photo.
  let h = vocCarteHtml('exo-vcRappel', 'Vocabulaire · 2', 'Je me souviens du mot',
    'Lisez le mot, cherchez son sens dans votre tête, puis vérifiez.', '0 / 0 su');
  if(vocImageMots().length >= 3){
    h += vocCarteHtml('exo-vcImage', 'Vocabulaire · 3', 'Le mot et son image',
      'Regardez la photo, puis choisissez le mot qui lui va.', '0 / 0 juste');
  }
  carteUn.insertAdjacentHTML('afterend', h);

  renderVocabPairs();
  vocRappelDemarrer(null);
  if(document.getElementById('exo-vcImage')) vocImageDemarrer();
}

// Ouverture / fermeture du bloc vocabulaire. Tant qu'il est ouvert, les
// autres exercices de « Je découvre » sont mis de côté : une chose à la fois.
function toggleVocabExo(force){
  const carteUn = document.getElementById('exo-prVocab');
  const btn = document.getElementById('btnVocabToggle');
  if(!carteUn) return;
  const opening = (typeof force==='boolean') ? force : carteUn.style.display==='none';

  const tete = document.getElementById('voc-head');
  if(tete) tete.style.display = opening ? '' : 'none';
  VOC_CARTES.forEach(id=>{
    const c = document.getElementById(id);
    if(c) c.style.display = opening ? '' : 'none';
  });
  if(btn) btn.textContent = opening ? "Fermer l'exercice de vocabulaire" : 'Apprendre les mots de vocabulaire';

  EXOS.filter(e=>e.sec==='prep' && e.id!=='prVocab').forEach(e=>{
    const c = document.getElementById('exo-'+e.id);
    if(c) c.style.display = opening ? 'none' : '';
  });

  if(opening) carteUn.scrollIntoView({behavior:'smooth', block:'start'});
  else if(btn) btn.scrollIntoView({behavior:'smooth', block:'center'});
}
