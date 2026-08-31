  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, un court message écrit. Le jeu de rôle vient en premier
  // parce qu'il sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait Line
  // Chartrand, jouée par l'assistant, vit dans server.py, scénario
  // « secretaire ».
  const ROLE_CAS = [
    {id:'papier', titre:"Je viens chercher un papier", txt:"Ton propriétaire demande une <b>preuve que tu suis le cours</b>. Tu ne sais pas si le secrétariat peut te la donner, ni quand."},
    {id:'absence', titre:"Demain, je ne viens pas", txt:"Tu as un <b>rendez-vous à la clinique</b> demain matin. Tu passes au comptoir avant de partir."},
    {id:'horaire', titre:"C'est ouvert à quelle heure ?", txt:"Tu veux revenir un autre jour. Tu ne sais pas <b>quand le bureau ouvre</b> ni s'il ferme le midi."},
  ];
  const ROLE_SUJETS = ["Saluer et dire ton nom",
    "Dire ce que tu veux, en une seule phrase",
    "Donner ton groupe ou ton local",
    "Demander le jour et l'heure",
    "Répéter la réponse pour vérifier",
    "Demander de répéter quand ça va trop vite",
    "Remercier et souhaiter une bonne journée"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Parle à la secrétaire du centre</span></div>
     <p class="lead">L'assistant joue <b>Line Chartrand, la secrétaire du centre</b>. Elle répond à trente personnes par matin : elle parle court, elle donne un renseignement à la fois. À toi de poser les questions, une par une.</p>
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
         <button class="jr-opt on" type="button" data-role="moi" onclick="jrChoisir('role','moi')">Moi, l'élève</button>
         <button class="jr-opt" type="button" data-role="secretaire" onclick="jrChoisir('role','secretaire')">La secrétaire du comptoir</button>
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
         <div><div class="jr-rappel-l">Demande poliment</div><div class="jr-rappel-x"><b>Je voudrais</b> une attestation, s'il vous plaît.</div></div>
         <div><div class="jr-rappel-l">Vérifie une chose</div><div class="jr-rappel-x"><b>Est-ce que</b> le bureau est ouvert le midi ?</div></div>
         <div><div class="jr-rappel-l">Demande le jour et l'heure</div><div class="jr-rappel-x"><b>Quand</b> est-ce que c'est prêt ? · <b>À quelle heure</b> ?</div></div>
         <div><div class="jr-rappel-l">Préviens d'une absence</div><div class="jr-rappel-x">Demain, je <b>ne</b> viens <b>pas</b> au cours.</div></div>
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
     <h3 class="prod-tit">Demande ton papier au comptoir</h3>
     <p class="prod-lead">Tu arrives au comptoir du secrétariat. Salue, dis ton nom, demande une attestation, puis demande quel jour elle sera prête. Vouvoie la personne du début à la fin.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Je salue et je me nomme</div><div class="plan-ex">« Bonjour, madame. Je m'appelle… »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Je demande une seule chose</div><div class="plan-ex">« Je voudrais une attestation, s'il vous plaît. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Je demande le jour, et je répète</div><div class="plan-ex">« C'est prêt quand ? … Jeudi. Merci beaucoup ! »</div></div>
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
     <h3 class="prod-tit">Écris un message au secrétariat</h3>
     <p class="prod-lead">Demain, tu ne viens pas au cours. Écris un court message au secrétariat : dis qui tu es, dis que tu ne viens pas, dis quel jour, et dis quand tu reviens. De 3 à 5 phrases.</p>
     <div class="req">
       <div class="req-hd">Ton message doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>« Bonjour », au début</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ton nom et ton groupe, ou ton local</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une phrase négative : <em>je ne viens pas</em></span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le jour de ton absence</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>« Merci » et ton nom à la fin</span></div>
       </div>
       <div class="req-note">Attention aux deux petits mots de la négation : on écrit <em>je ne viens pas</em>, même si on dit souvent « je viens pas ». Et devant une voyelle, <em>ne</em> devient <em>n'</em> : <em>je n'ai pas mon papier</em>.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">Pour</span><span class="mail-v">Le secrétariat du centre</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Mon absence</span></div>
       <textarea id="peText" rows="7" aria-label="Ton message" data-min="3" data-max="5" oninput="peCount()" placeholder="Bonjour,&#10;Je m'appelle… Demain, je ne viens pas…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 3 à 5</span>
         <button class="btn-prod" id="peBtn" type="button" onclick="peCheck()">Vérifier mon message</button>
       </div>
     </div>
     <div class="fb" id="peFb" aria-live="polite"></div>
     <div class="status" id="peStatus">Analyse en cours…</div>
     <div class="err" id="peErr"></div>
   </div>`;
  const rb=document.getElementById('recBtn'); if(rb) rb.addEventListener('click',toggleRec);

  // JE RETIENS DES MOTS — notes + cartes mémoire + autoévaluation
  const SELF=[
    "Je peux nommer les personnes qui travaillent au centre.",
    "Je peux dire où est le secrétariat et à quel étage est mon local.",
    "Je peux saluer et dire mon nom au comptoir.",
    "Je peux demander un papier avec « je voudrais ».",
    "Je peux demander l'heure d'ouverture et le jour où c'est prêt.",
    "Je peux répéter une réponse pour vérifier que j'ai bien compris.",
    "Je peux dire que je ne viens pas au cours demain.",
    "Je peux lire un avis affiché et trouver la date et ce qui est fermé.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Les personnes du centre</div>
     <textarea rows="2" placeholder="Ex. : une secrétaire, un concierge, une enseignante, la direction…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les lieux du centre</div>
     <textarea rows="2" placeholder="Ex. : le secrétariat, le comptoir, le couloir, le rez-de-chaussée, un étage, un local…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les papiers et les avis</div>
     <textarea rows="2" placeholder="Ex. : une attestation, un horaire, un avis, une absence, un congé…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les phrases du comptoir</div>
     <textarea rows="2" placeholder="Ex. : Je voudrais…, Est-ce que…, À quelle heure…, Pouvez-vous répéter ?, Merci beaucoup."></textarea>
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
