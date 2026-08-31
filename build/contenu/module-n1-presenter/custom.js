  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, une liste d'épicerie écrite. Le jeu de rôle vient en premier
  // parce qu'il sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait le personnage
  // joué par l'assistant vit dans server.py.
  const ROLE_CAS = [
    {id:'accueil', titre:"À l'accueil", txt:"C'est ton <b>premier jour</b>. On te demande ton nom, et on te demande de l'épeler."},
    {id:'classe', titre:"Dans la classe", txt:"Une nouvelle personne s'assoit à côté de toi. Vous vous <b>présentez</b> l'un à l'autre."},
    {id:'secretariat', titre:"Au secrétariat", txt:"On remplit ta fiche : ton nom, ton <b>adresse</b>, ta langue. Tu ne comprends pas tout."},
  ];
  const ROLE_SUJETS = ["Dire bonjour","Dire son nom",
    "Épeler son nom","Dire d'où on vient",
    "Dire quelle langue on parle","Faire répéter si on ne comprend pas",
    "Dire merci"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Présente-toi</span></div>
     <p class="lead">L'assistant joue <b>la personne qui t'accueille</b>. Elle parle lentement et pose une question à la fois. Si tu ne comprends pas, dis-le : c'est permis.</p>
     <p class="lead">Choisis ta situation et ton rôle</p>
     <div class="jr-annonces" id="jrLogs">
       ${ROLE_CAS.map((c,i)=>`<button class="jr-opt jr-tuile${i===0?' on':''}" type="button" data-log="${c.id}" onclick="jrChoisir('log','${c.id}')">
         <span class="jr-band"><span class="jr-band-off">Choix ${i+1}</span><span class="jr-band-on"><svg viewBox="0 0 20 20" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 10.5l4 4 8-9"></path></svg> Votre choix</span></span>
         <span class="jr-tuile-c"><span class="jr-tuile-t">${esc(c.titre)}</span><span class="jr-tuile-d">${c.txt}</span></span>
       </button>`).join('')}
     </div>
     <div class="jr-reglages">
       <div class="jr-carte">
         <div class="jr-champ-l">Tu joues qui ?</div>
         <div class="jr-tuiles" id="jrRoles">
         <button class="jr-opt on" type="button" data-role="eleve" onclick="jrChoisir('role','eleve')">Moi, l'élève</button>
         <button class="jr-opt" type="button" data-role="accueillant" onclick="jrChoisir('role','accueillant')">La personne qui accueille</button>
       </div>
       </div>
       <div class="jr-carte">
         <div class="jr-champ-l">Comment ?</div>
         <div class="jr-tuiles" id="jrModes">
         <button class="jr-opt on" type="button" data-mode="texte" onclick="jrModeVoix(false)"><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 20h4l10-10-4-4L4 16v4z"></path><path d="M14 6l4 4"></path></svg><span>J'écris</span></button>
         <button class="jr-opt" type="button" data-mode="voix" onclick="jrModeVoix(true)"><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="3" width="6" height="11" rx="3"></rect><path d="M5.5 11.5a6.5 6.5 0 0013 0M12 18v3"></path></svg><span>Je parle</span></button>
       </div>
       </div>
     </div>
     <div class="jr-bande">
       <div>
         <div class="jr-bande-t">Les sept sujets à couvrir</div>
         <p class="jr-bande-p">${ROLE_SUJETS.map((s,i)=>i?s.charAt(0).toLowerCase()+s.slice(1):s).join(', ')}.</p>
       </div>
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()">Commencer la conversation</button>
     </div>
     <div class="jr-rappel">
       <div class="jr-rappel-t">Réutilise ce que tu viens d'apprendre</div>
       <div class="jr-rappel-g">
         <div><div class="jr-rappel-l">Dis ton nom</div><div class="jr-rappel-x"><b>Je m'appelle</b> Amina.</div></div>
         <div><div class="jr-rappel-l">Épelle-le</div><div class="jr-rappel-x">A - M - I - N - A.</div></div>
         <div><div class="jr-rappel-l">Dis d'où tu viens</div><div class="jr-rappel-x"><b>Je viens d'</b>Algérie.</div></div>
         <div><div class="jr-rappel-l">Si tu ne comprends pas</div><div class="jr-rappel-x"><b>Plus lentement</b>, s'il vous plaît.</div></div>
       </div>
     </div>

     <div id="jrChat" class="hidden">
       <div class="jr-fil" id="jrFil" aria-live="polite"></div>
       <div class="jr-mic hidden" id="jrMicZone">
         <button id="jrMic" type="button" onclick="jrParler()" aria-label="Parler"><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="3" width="6" height="11" rx="3"></rect><path d="M5.5 11.5a6.5 6.5 0 0013 0M12 18v3"></path></svg></button>
         <span class="jr-mic-l" id="jrMicLbl">Touche pour parler</span>
       </div>
       <div class="jr-saisie">
         <input id="jrInput" type="text" placeholder="Écris ce que tu dis…" autocomplete="off"
                onkeydown="if(event.key==='Enter'){event.preventDefault();jrEnvoyer();}">
         <button class="btn btn-pri" id="jrSend" type="button" onclick="jrEnvoyer()">Envoyer</button>
       </div>
       <div class="status" id="jrStatus">L'assistant réfléchit…</div>
       <div class="err" id="jrErr"></div>
       <div class="jr-fin">
         <button class="btn btn-ghost" type="button" onclick="jrRecommencer()">↺ Recommencer</button>
         <button class="btn btn-send" type="button" onclick="jrFini()">J'ai fini — corrige mes phrases</button>
       </div>
       <div class="fb" id="jrFb" aria-live="polite"></div>
     </div>
   </div>

   <div class="card custom">
     <div class="prod-eyebrow"><span class="prod-num">1</span><span class="prod-kind">Production orale</span></div>
     <h3 class="prod-tit">Présente-toi</h3>
     <p class="prod-lead">Présente-toi à quelqu'un que tu rencontres pour la première fois. Dis ton nom, épelle-le, et dis d'où tu viens.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Saluer et dire son nom</div><div class="plan-ex">« Bonjour. Je m'appelle Amina Benali. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Épeler son nom de famille</div><div class="plan-ex">« B - E - N - A - L - I. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Dire d'où on vient et ce qu'on parle</div><div class="plan-ex">« Je viens d'Algérie. Je parle arabe et un peu français. »</div></div>
     </div>
     <div class="rec-panel">
       <div class="rec-steps">
         <div class="rec-step on" id="recStep1"><span class="n">1</span><span class="l">Je m'enregistre</span></div>
         <div class="rec-step" id="recStep2"><span class="n">2</span><span class="l">Je m'écoute et je corrige</span></div>
         <div class="rec-step" id="recStep3"><span class="n">3</span><span class="l">J'envoie à mon enseignant</span></div>
       </div>
       <div class="rec-body">
         <button id="recBtn" type="button" aria-label="Démarrer l'enregistrement"><span class="dot"></span></button>
         <div>
           <div class="rec-lbl" id="recLbl">Touche pour t'enregistrer</div>
           <div class="rec-hint">Parle environ 30 secondes. Tu pourras recommencer autant de fois que tu veux.</div>
         </div>
       </div>
     </div>
     <div id="poPrev" class="hidden prod-tools" style="display:flex;flex-direction:column;gap:12px">
       <audio id="poAudio" controls style="width:100%"></audio>
       <textarea id="poText" rows="2" placeholder="Transcription automatique (tu peux la corriger)…"></textarea>
       <div style="display:flex;gap:10px;flex-wrap:wrap">
         <button class="btn btn-ghost" onclick="resetRec()">Recommencer</button>
         <button class="btn btn-pri" id="poFbBtn" onclick="poGetFeedback()">Obtenir une rétroaction</button>
       </div>
       <div class="fb" id="poFb" aria-live="polite"></div>
       <div id="poSend" style="display:none;gap:10px;flex-wrap:wrap;align-items:center">
         <button class="btn btn-send" id="poSendBtn" onclick="poSend()">Envoyer à mon enseignant</button>
       </div>
     </div>
     <div class="status" id="poStatus">Analyse en cours…</div>
     <div class="err" id="poErr"></div>
   </div>

   <div class="card custom">
     <div class="prod-eyebrow"><span class="prod-num">2</span><span class="prod-kind">Production écrite</span></div>
     <h3 class="prod-tit">Écris ta fiche</h3>
     <p class="prod-lead">Écris ta fiche : ton nom, ton pays, ta ville, tes langues, ta famille. De 4 à 6 phrases.</p>
     <div class="req">
       <div class="req-hd">Ta fiche doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ton prénom et ton nom de famille</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le pays d'où tu viens</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>La ville où tu habites</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Les langues que tu parles</span></div>
       </div>
       <div class="req-note">Emploie les cinq phrases : <em>je m'appelle</em>, <em>je viens de</em>, <em>j'habite à</em>, <em>je parle</em>, <em>j'ai</em>.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">Fiche</span><span class="mail-v">Nouvel élève</span></div>
       <div class="mail-row"><span class="mail-k">Centre</span><span class="mail-v">Francisation, niveau 1</span></div>
       <textarea id="peText" rows="7" aria-label="Ta liste" data-min="4" data-max="6" oninput="peCount()" placeholder="Je m'appelle…&#10;Je viens de…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 4 à 6</span>
         <button class="btn-prod" id="peBtn" type="button" onclick="peCheck()">Vérifier ma fiche</button>
       </div>
     </div>
     <div class="fb" id="peFb" aria-live="polite"></div>
     <div class="status" id="peStatus">Analyse en cours…</div>
     <div class="err" id="peErr"></div>
   </div>`;
  const rb=document.getElementById('recBtn'); if(rb) rb.addEventListener('click',toggleRec);

  // JE RETIENS DES MOTS — notes + cartes mémoire + autoévaluation
  const SELF=[
    "Je peux dire mon nom et l'épeler.",
    "Je peux dire d'où je viens et où j'habite.",
    "Je peux dire quelles langues je parle.",
    "Je peux dire si j'ai des enfants.",
    "Je peux saluer et remercier.",
    "Je peux dire que je ne comprends pas et demander de parler plus lentement.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Mon identité</div>
     <textarea rows="2" placeholder="Ex. : mon nom, mon prénom, épeler, mon adresse…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">D'où je viens</div>
     <textarea rows="2" placeholder="Ex. : je viens de…, j'habite à…, je parle…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Ma famille</div>
     <textarea rows="2" placeholder="Ex. : j'ai un enfant, un fils, une fille, il a six ans…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Être poli</div>
     <textarea rows="2" placeholder="Ex. : bonjour, merci, de rien, pardon, plus lentement…"></textarea>
   </div>
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Autoévaluation</span><span class="ctit" style="color:#A5335F">Qu'est-ce que je suis capable de faire ?</span></div>
     <p class="lead">Pour chaque énoncé, choisis : pas encore 😟, un peu 🙂, ou oui 😃.</p>
     ${SELF.map((s,i)=>`<div class="selfrow"><div class="self-txt">${s}</div><div class="self-opts">
        <button onclick="rate(${i},this)">😟</button><button onclick="rate(${i},this)">🙂</button><button onclick="rate(${i},this)">😃</button>
     </div></div>`).join('')}
     <div style="margin-top:16px"><button class="btn btn-pri" onclick="finishEval()">Terminer le module 🎉</button></div>
     <div id="evalDone" class="fb" aria-live="polite"></div>
   </div>`;
}
