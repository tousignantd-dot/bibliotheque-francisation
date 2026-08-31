  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, un courriel au secrétariat. Le jeu de rôle vient en premier
  // parce qu'il sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait la secrétaire
  // jouée par l'assistant vit dans server.py (JEU_DE_ROLE_SECRETARIAT).
  const ROLE_CAS = [
    {id:'garderie', titre:"L'enfant malade", txt:"Ton fils de cinq ans a fait de la <b>fièvre</b> toute la nuit et la garderie ne le prendra pas demain. Tu viens dire que tu ne seras pas là demain matin."},
    {id:'billet', titre:"Le billet de la clinique", txt:"Tu as manqué <b>trois jours</b> la semaine passée : une grippe, puis un rendez-vous. Tu reviens ce matin avec un papier de la clinique dans ton sac."},
    {id:'arret', titre:"Le travail à temps plein", txt:"Tu commences un <b>emploi</b> le premier du mois prochain et tu ne pourras plus suivre le cours du matin. Tu viens le dire et demander un papier qui prouve que tu as suivi le cours."},
  ];
  const ROLE_SUJETS = ["Saluer : bonjour madame, bonjour monsieur",
    "Donner ton nom, ton prénom et ton groupe",
    "Dire en une phrase ce que tu viens annoncer",
    "Donner le jour, la date, l'avant-midi ou la journée",
    "Dire la raison en une phrase, avec « parce que »",
    "Demander s'il faut un papier, et lequel",
    "Répéter la date à voix haute avant de partir"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Au comptoir du secrétariat</span></div>
     <p class="lead">L'assistant joue <b>la secrétaire du centre</b>. Elle commence toujours par ton nom, ton prénom et ton groupe, et elle ne devine rien : la date, la raison, le papier, tout se dit. À toi de parler.</p>
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
         <button class="jr-opt on" type="button" data-role="eleve" onclick="jrChoisir('role','eleve')">L'élève</button>
         <button class="jr-opt" type="button" data-role="secretaire" onclick="jrChoisir('role','secretaire')">La secrétaire</button>
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
         <div><div class="jr-rappel-l">Salue</div><div class="jr-rappel-x"><b>Bonjour, madame.</b> Mon nom, c'est… , groupe 12.</div></div>
         <div><div class="jr-rappel-l">Annonce</div><div class="jr-rappel-x"><b>Je vais être absente</b> jeudi, l'avant-midi.</div></div>
         <div><div class="jr-rappel-l">Donne la date</div><div class="jr-rappel-x">Jeudi <b>prochain, le 12 mars</b>.</div></div>
         <div><div class="jr-rappel-l">Demande</div><div class="jr-rappel-x"><b>Est-ce que je peux</b> garder l'original ?</div></div>
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
     <h3 class="prod-tit">Annonce ton absence au comptoir</h3>
     <p class="prod-lead">Choisis une journée où tu ne pourrais pas venir au cours. Présente-toi, annonce ton absence au futur proche, donne le jour et le moment, dis la raison, puis demande s'il faut un papier.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Saluer et se nommer</div><div class="plan-ex">« Bonjour, madame. Mon nom, c'est… , groupe 12. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Annoncer, dater, expliquer</div><div class="plan-ex">« Je vais être absente jeudi, l'avant-midi, parce que ma fille a un rendez-vous. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Demander et remercier</div><div class="plan-ex">« Est-ce que je dois apporter un papier ? Merci beaucoup. Bonne journée. »</div></div>
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
     <h3 class="prod-tit">Écris au secrétariat</h3>
     <p class="prod-lead">Le secrétariat accepte les avis par courriel. Écris un court message : qui tu es, quelles journées tu vas manquer ou tu as manquées, pourquoi, et ce que tu apportes. De 5 à 8 phrases.</p>
     <div class="req">
       <div class="req-hd">Ton message doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une formule d'appel : « Bonjour madame, »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ton nom, ton prénom et ton groupe</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le ou les jours, avec la date</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>La raison, en une phrase avec « parce que »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une salutation finale : « Merci. Bonne journée. »</span></div>
       </div>
       <div class="req-note">Attention aux dates : on écrit <em>le 12 mars</em>, jamais « mars 12 », et les noms de jours ne prennent pas de majuscule.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">secretariat@centre-lachapelle.qc.ca</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Absence — groupe 12</span></div>
       <textarea id="peText" rows="7" aria-label="Ton message" data-min="5" data-max="8" oninput="peCount()" placeholder="Bonjour madame,&#10;Je m'appelle… , groupe 12.&#10;Je vais être absente jeudi le 12 mars…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 5 à 8</span>
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
    "Je peux nommer le secrétariat, le comptoir, mon groupe et mon dossier.",
    "Je salue et je vouvoie : bonjour madame, est-ce que vous pouvez…",
    "Je peux annoncer une absence au futur proche : je vais être absente jeudi.",
    "Je fais la différence entre « jeudi » et « le jeudi ».",
    "Je peux dire quelles journées j'ai manquées, une date à la fois.",
    "Je peux apporter un billet d'absence et demander une photocopie.",
    "Je peux annoncer que j'arrête le cours et donner mon dernier jour.",
    "Je peux demander une attestation de fréquentation avant de partir.",
    "Je peux écrire un court courriel d'absence au secrétariat.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Le centre et les gens</div>
     <textarea rows="2" placeholder="Ex. : le secrétariat, le comptoir, la secrétaire, le groupe, le dossier, l'enseignante…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Saluer et demander</div>
     <textarea rows="2" placeholder="Ex. : bonjour madame, s'il vous plaît, est-ce que je peux…, pourriez-vous…, merci beaucoup, bonne journée…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">L'absence et le billet</div>
     <textarea rows="2" placeholder="Ex. : une absence, prévenir, l'avant-midi, un billet d'absence, justifier, une photocopie, l'original…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Arrêter le cours</div>
     <textarea rows="2" placeholder="Ex. : un abandon, le dernier jour de cours, une attestation de fréquentation, signer, en main propre…"></textarea>
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
