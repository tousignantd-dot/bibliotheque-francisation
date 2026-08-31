  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, et le petit mot laissé au chef d'équipe. Le jeu de rôle vient
  // en premier : il sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait le chef
  // d'équipe joué par l'assistant vit dans server.py (scénario « horaire »).
  const ROLE_CAS = [
    {id:'echange', titre:"Échanger un quart", txt:"Ton garçon a un <b>rendez-vous jeudi à dix heures</b>. Tu travailles ce jeudi-là de six heures à quatorze heures, et un collègue peut te remplacer."},
    {id:'aide', titre:"Je n'ai pas compris", txt:"Le chef d'équipe vient de donner une consigne <b>trop vite</b>. Tu n'as retenu qu'une chose sur trois, et il faut le dire avant de commencer."},
    {id:'termine', titre:"C'est fait, et après ?", txt:"Tu viens de <b>finir ta tâche</b> avant l'heure prévue. Tu vas dire où tu en es et demander ce que tu fais ensuite."},
  ];
  const ROLE_SUJETS = ["Saluer et dire pourquoi tu viens",
    "Dire l'heure ou le jour dont tu parles",
    "Demander une permission, ou demander de l'aide",
    "Donner ta raison en une phrase",
    "Redire l'heure ou la consigne pour vérifier",
    "Dire où tu en es dans ta tâche",
    "Remercier avant de retourner travailler"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Parle à ton chef d'équipe</span></div>
     <p class="lead">L'assistant joue <b>le chef d'équipe de la cafétéria</b>. Il répond une chose à la fois, et il te demande de redire l'heure ou la consigne pour vérifier que tu as bien compris.</p>
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
         <button class="jr-opt on" type="button" data-role="employe" onclick="jrChoisir('role','employe')">L'employé</button>
         <button class="jr-opt" type="button" data-role="chef" onclick="jrChoisir('role','chef')">Le chef d'équipe</button>
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
         <div><div class="jr-rappel-l">Situe ton quart</div><div class="jr-rappel-x">Jeudi, je travaille <b>de six heures à quatorze heures</b>.</div></div>
         <div><div class="jr-rappel-l">Demande la permission</div><div class="jr-rappel-x"><b>Est-ce que je peux</b> échanger mon jeudi ?</div></div>
         <div><div class="jr-rappel-l">Explique pourquoi</div><div class="jr-rappel-x"><b>Je dois</b> aller à la clinique avec mon garçon.</div></div>
         <div><div class="jr-rappel-l">Dis où tu en es</div><div class="jr-rappel-x"><b>Je viens de</b> finir les plateaux.</div></div>
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
     <h3 class="prod-tit">Demande un changement à ton horaire</h3>
     <p class="prod-lead">Tu vas voir ton chef d'équipe. Dis quel jour et quelle heure te posent problème, demande poliment ce que tu veux, explique pourquoi, puis redis l'entente pour vérifier.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Dire pourquoi tu viens</div><div class="plan-ex">« Bonjour. Est-ce que je peux vous parler deux minutes ? »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Demander, et donner ta raison</div><div class="plan-ex">« Jeudi, je travaille de six heures à quatorze heures. Est-ce que je peux échanger ? Je dois aller à la clinique. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Redire l'entente et remercier</div><div class="plan-ex">« Alors jeudi, c'est Miguel à six heures. Merci beaucoup. »</div></div>
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
           <div class="rec-hint">Parle environ 45 secondes. Tu pourras recommencer autant de fois que tu veux.</div>
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
     <h3 class="prod-tit">Laisse un mot à ton chef d'équipe</h3>
     <p class="prod-lead">Avant de partir, tu écris le petit mot que tu laisses sur son bureau : ce qui est fait, ce qui ne l'est pas, et ce que tu demandes. De 5 à 8 phrases.</p>
     <div class="req">
       <div class="req-hd">Ton mot doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une tâche terminée : « c'est fait », « je viens de finir »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une tâche non terminée, avec ce qui reste</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une heure écrite avec de… à, jusqu'à ou à partir de</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une demande polie : « est-ce que je peux… ? »</span></div>
       </div>
       <div class="req-note">Attention aux petits mots de l'heure : <em>de six heures à quatorze heures</em>, <em>jusqu'à midi</em>, <em>à partir de lundi</em>.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">Pour</span><span class="mail-v">Gaétan Roy, chef d'équipe</span></div>
       <div class="mail-row"><span class="mail-k">De</span><span class="mail-v">ton nom · aide-cuisine</span></div>
       <textarea id="peText" rows="7" aria-label="Ton mot" data-min="5" data-max="8" oninput="peCount()" placeholder="Bonjour monsieur Roy,&#10;Les plateaux du deuxième étage, c'est fait.&#10;Je suis en train de ranger les boîtes…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 5 à 8</span>
         <button class="btn-prod" id="peBtn" type="button" onclick="peCheck()">Vérifier mon mot</button>
       </div>
     </div>
     <div class="fb" id="peFb" aria-live="polite"></div>
     <div class="status" id="peStatus">Analyse en cours…</div>
     <div class="err" id="peErr"></div>
   </div>`;
  const rb=document.getElementById('recBtn'); if(rb) rb.addEventListener('click',toggleRec);

  // JE RETIENS DES MOTS — notes + cartes mémoire + autoévaluation
  const SELF=[
    "Je peux nommer les lieux et les objets du travail : le vestiaire, le casier, l'horaire.",
    "Je peux lire mon quart sur l'horaire : « 6 h - 14 h », c'est de six heures à quatorze heures.",
    "Je peux dire un moment de la journée : le matin, le midi, l'après-midi, le soir.",
    "Je peux poser une question sur mon horaire : à quelle heure, quand, combien de temps.",
    "Je peux demander une permission poliment : « Est-ce que je peux… ? »",
    "Je peux demander de l'aide, et répondre quand un collègue m'en demande.",
    "Je comprends une consigne à l'impératif et je la redis pour vérifier.",
    "Je peux dire où j'en suis : c'est fait, je viens de finir, je suis en train de le faire.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#1D6B8F">Je retiens des mots</span><span class="ctit" style="color:#1D6B8F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#1D6B8F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:6px 0 4px">Le lieu de travail</div>
     <textarea rows="2" placeholder="Ex. : le vestiaire, un casier, un uniforme, poinçonner, la salle du personnel…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">L'horaire et les heures</div>
     <textarea rows="2" placeholder="Ex. : un quart de travail, une pause, un congé, de… à…, jusqu'à, à partir de…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">Demander et répondre</div>
     <textarea rows="2" placeholder="Ex. : Est-ce que je peux… ? Est-ce que vous pouvez m'aider ? Il faut aviser, échanger, remplacer…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">Les consignes et les tâches</div>
     <textarea rows="2" placeholder="Ex. : sortez, rangez, éteignez, une livraison, c'est fait, je viens de finir…"></textarea>
   </div>
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#1D6B8F">Autoévaluation</span><span class="ctit" style="color:#1D6B8F">Qu'est-ce que je suis capable de faire ?</span></div>
     <p class="lead">Pour chaque énoncé, choisis : pas encore 😟, un peu 🙂, ou oui 😃.</p>
     ${SELF.map((s,i)=>`<div class="selfrow"><div class="self-txt">${s}</div><div class="self-opts">
        <button onclick="rate(${i},this)">😟</button><button onclick="rate(${i},this)">🙂</button><button onclick="rate(${i},this)">😃</button>
     </div></div>`).join('')}
     <div style="margin-top:16px"><button class="btn btn-pri" onclick="finishEval()">Terminer le module 🎉</button></div>
     <div id="evalDone" class="fb" aria-live="polite"></div>
   </div>`;
}
