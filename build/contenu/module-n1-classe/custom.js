  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, un horaire écrit. Le jeu de rôle vient en premier parce qu'il
  // sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait l'enseignante
  // jouée par l'assistant vit dans server.py, scénario « classe1 ».
  const ROLE_CAS = [
    {id:'consigne', titre:"La consigne", txt:"L'enseignante dit deux mots : « <b>Ouvrez le livre.</b> » Tu fais le geste, ou tu dis que tu n'as pas compris."},
    {id:'objet', titre:"L'objet", txt:"L'enseignante montre une chose et demande : « <b>Qu'est-ce que c'est ?</b> » Tu dis le mot."},
    {id:'heure', titre:"L'heure", txt:"Tu ne sais plus à quelle heure le cours finit. Tu demandes : « <b>À quelle heure ?</b> »"},
  ];
  const ROLE_SUJETS = ["Dire bonjour et madame",
    "Comprendre une consigne de deux mots",
    "Dire « Pardon ? » quand tu n'as pas compris",
    "Nommer un objet de la classe",
    "Dire où est l'objet : sur, dans, sous",
    "Comprendre une heure : huit heures et demie, midi",
    "Dire merci"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Ton premier cours</span></div>
     <p class="lead">L'assistant joue <b>madame Cyr, ton enseignante</b>. Elle dit une seule chose à la fois, en trois ou quatre mots. Si tu ne comprends pas, dis « Pardon ? » : elle répétera plus lentement.</p>
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
       Nomme l'objet :
       <span class='savoir-ex'>C'est <b>un livre</b>.</span>
       Dis où il est :
       <span class='savoir-ex'>Il est <b>sur</b> la table.</span>
       Demande l'heure :
       <span class='savoir-ex'><b>À quelle heure</b> ?</span>
       Si tu n'as pas compris :
       <span class='savoir-ex'><b>Pardon ?</b></span>
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
         <button class="jr-opt" type="button" data-role="enseignante" onclick="jrChoisir('role','enseignante')">L'enseignante qui parle</button>
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
     <h3 class="prod-tit">Nomme ta classe</h3>
     <p class="prod-lead">Regarde autour de toi. Nomme cinq objets, dis où est un objet, puis dis l'heure de ton cours. Des phrases de trois ou quatre mots suffisent.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Nommer cinq objets</div><div class="plan-ex">« Un livre. Un stylo. Une chaise. Une porte. Une horloge. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Dire où est un objet</div><div class="plan-ex">« Mon sac est sous ma chaise. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Dire l'heure du cours</div><div class="plan-ex">« Le cours commence à huit heures et demie. Il finit à midi. »</div></div>
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
     <h3 class="prod-tit">Écris ton horaire</h3>
     <p class="prod-lead">Écris l'horaire de ton cours : les jours, l'heure du début, l'heure de la fin, l'heure de la pause. De 3 à 5 phrases très courtes.</p>
     <div class="req">
       <div class="req-hd">Ton horaire doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Les jours de cours : lundi, mardi…</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>L'heure du début, avec <em>à</em></span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>L'heure de la fin</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>L'heure de la pause</span></div>
       </div>
       <div class="req-note">Les jours s'écrivent en minuscules : <em>lundi</em>, et non <em>Lundi</em>.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">Horaire</span><span class="mail-v">Mon groupe</span></div>
       <div class="mail-row"><span class="mail-k">Centre</span><span class="mail-v">Francisation, niveau 1</span></div>
       <textarea id="peText" rows="7" aria-label="Ton horaire" data-min="3" data-max="5" oninput="peCount()" placeholder="Le cours est de lundi à…&#10;Le cours commence à…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 3 à 5</span>
         <button class="btn-prod" id="peBtn" type="button" onclick="peCheck()">Vérifier mon horaire</button>
       </div>
     </div>
     <div class="fb" id="peFb" aria-live="polite"></div>
     <div class="status" id="peStatus">Analyse en cours…</div>
     <div class="err" id="peErr"></div>
   </div>`;
  const rb=document.getElementById('recBtn'); if(rb) rb.addEventListener('click',toggleRec);

  // JE RETIENS DES MOTS — notes + cartes mémoire + autoévaluation
  const SELF=[
    "Je peux nommer six objets de ma classe.",
    "Je peux dire « un » ou « une » devant le mot.",
    "Je peux comprendre une consigne courte et faire le geste.",
    "Je peux dire « Pardon ? » quand je n'ai pas compris.",
    "Je peux dire où est un objet : sur, dans, sous.",
    "Je peux entendre la différence entre deux et douze.",
    "Je peux comprendre l'heure de mon cours et de la pause.",
    "Je peux dire les jours de la semaine et lire mon horaire.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Les objets de ma classe</div>
     <textarea rows="2" placeholder="Ex. : un livre, un stylo, une chaise, un sac, une porte, une horloge…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les consignes</div>
     <textarea rows="2" placeholder="Ex. : écoutez, regardez, ouvrez, fermez, prenez, répétez…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Où est la chose</div>
     <textarea rows="2" placeholder="Ex. : sur la table, dans le sac, sous la chaise…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">L'heure et les jours</div>
     <textarea rows="2" placeholder="Ex. : huit heures et demie, midi, la pause, lundi, mardi, la semaine…"></textarea>
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
