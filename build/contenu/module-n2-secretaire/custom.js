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
     <div class="jr-grid">
       ${ROLE_CAS.map(c=>`
       <div class="jr-log">
         <div class="jr-log-h">${esc(c.titre)}</div>
         <div class="jr-log-a">${c.txt}</div>
       </div>`).join('')}
     </div>
     <div class="jr-sub">Les sept sujets à couvrir</div>
     <div class="jr-sujets">
       ${ROLE_SUJETS.map(s=>`<div class="jr-sujet"><span class="jr-box"></span>${esc(s)}</div>`).join('')}
     </div>
     <div class="jr-gram">
       <div class="jr-gram-t">Réutilise ce que tu viens d'apprendre</div>
       Demande poliment :
       <span class='savoir-ex'><b>Je voudrais</b> une attestation, s'il vous plaît.</span>
       Vérifie une chose :
       <span class='savoir-ex'><b>Est-ce que</b> le bureau est ouvert le midi ?</span>
       Demande le jour et l'heure :
       <span class='savoir-ex'><b>Quand</b> est-ce que c'est prêt ? · <b>À quelle heure</b> ?</span>
       Préviens d'une absence :
       <span class='savoir-ex'>Demain, je <b>ne</b> viens <b>pas</b> au cours.</span>
     </div>

     <div class="jr-sep"></div>
     <div class="jr-sub">Choisis ta situation et ton rôle</div>
     <div class="jr-choix">
       <div class="jr-choix-l">Quelle situation ?</div>
       <div class="jr-opts" id="jrLogs">
         ${ROLE_CAS.map((c,i)=>`<button class="jr-opt${i===0?' on':''}" type="button" data-log="${c.id}" onclick="jrChoisir('log','${c.id}')">${esc(c.titre)}</button>`).join('')}
       </div>
       <div class="jr-choix-l">Tu joues qui ?</div>
       <div class="jr-opts" id="jrRoles">
         <button class="jr-opt on" type="button" data-role="moi" onclick="jrChoisir('role','moi')">Moi, l'élève</button>
         <button class="jr-opt" type="button" data-role="secretaire" onclick="jrChoisir('role','secretaire')">La secrétaire du comptoir</button>
       </div>
       <div class="jr-choix-l">Comment ?</div>
       <div class="jr-opts" id="jrModes">
         <button class="jr-opt on" type="button" data-mode="texte" onclick="jrModeVoix(false)">✍️ Écrire</button>
         <button class="jr-opt" type="button" data-mode="voix" onclick="jrModeVoix(true)">🎤 Parler</button>
       </div>
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()" style="margin-top:14px">Commencer la conversation</button>
     </div>

     <div id="jrChat" class="hidden">
       <div class="jr-fil" id="jrFil" aria-live="polite"></div>
       <div class="jr-mic hidden" id="jrMicZone">
         <button id="jrMic" type="button" onclick="jrParler()" aria-label="Parler">🎤</button>
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
