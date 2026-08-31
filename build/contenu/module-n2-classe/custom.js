  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, un mot d'absence écrit. Le jeu de rôle vient en premier
  // parce qu'il sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait l'enseignante
  // jouée par l'assistant vit dans server.py, scénario « classe ».
  const ROLE_CAS = [
    {id:'consigne', titre:"Je n'ai pas compris", txt:"L'enseignante vient de donner une <b>consigne</b>. Tu n'as pas compris. Tu le dis."},
    {id:'permission', titre:"Est-ce que je peux ?", txt:"Tu n'as pas de <b>crayon</b>, et tu veux sortir deux minutes. Tu demandes la permission."},
    {id:'absence', titre:"Demain, je suis absent", txt:"Tu as un <b>rendez-vous</b> demain matin. Tu préviens ton enseignante avant de partir."},
  ];
  const ROLE_SUJETS = ["Saluer et dire madame ou monsieur",
    "Dire « je n'ai pas compris »",
    "Demander de répéter, ou de parler plus lentement",
    "Redire la consigne dans tes mots",
    "Demander une permission : « Est-ce que je peux… ? »",
    "Annoncer un retard ou une absence, avec le jour",
    "Remercier et prendre congé"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Parle à ton enseignante</span></div>
     <p class="lead">L'assistant joue <b>madame Leduc, ton enseignante</b>. Elle parle lentement et dit deux ou trois phrases à la fois, pas plus. Si tu ne comprends pas, dis-le : « pouvez-vous répéter ? » fait partie du cours.</p>
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
         <button class="jr-opt" type="button" data-role="enseignante" onclick="jrChoisir('role','enseignante')">L'enseignante qui répond</button>
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
         <div><div class="jr-rappel-l">Dis que tu ne comprends pas</div><div class="jr-rappel-x">Excusez-moi, madame. <b>Je n'ai pas compris</b>.</div></div>
         <div><div class="jr-rappel-l">Demande une deuxième fois</div><div class="jr-rappel-x"><b>Pouvez-vous répéter</b>, s'il vous plaît ?</div></div>
         <div><div class="jr-rappel-l">Demande la permission</div><div class="jr-rappel-x"><b>Est-ce que je peux</b> prendre un crayon ?</div></div>
         <div><div class="jr-rappel-l">Annonce ton absence</div><div class="jr-rappel-x">Demain, je suis <b>absent</b>. J'ai un rendez-vous.</div></div>
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
     <h3 class="prod-tit">Explique ta classe à une personne qui arrive</h3>
     <p class="prod-lead">Une nouvelle personne entre dans ton groupe. Dis-lui l'heure du cours, l'heure de la pause, ce qu'il faut apporter, une chose permise et une chose interdite. Vouvoie-la du début à la fin.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Les heures</div><div class="plan-ex">« Le cours commence à huit heures et demie. La pause est à dix heures. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Ce qu'on apporte</div><div class="plan-ex">« Apportez un cahier, un crayon et une gomme à effacer. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Permis, interdit</div><div class="plan-ex">« L'eau est permise. Le téléphone est interdit en classe. »</div></div>
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
     <h3 class="prod-tit">Écris un mot à ton enseignante</h3>
     <p class="prod-lead">Tu vas être absent ou en retard. Écris un petit mot à ton enseignante : le jour, ce qui arrive, pourquoi, et ton prénom à la fin. De 3 à 5 phrases.</p>
     <div class="req">
       <div class="req-hd">Ton mot doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le nom de ton enseignante, au début</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le jour : demain, jeudi, lundi…</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span><em>Je suis absent</em>, <em>je suis absente</em> ou <em>je suis en retard</em></span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>La raison, en trois ou quatre mots</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ton prénom, sur la dernière ligne</span></div>
       </div>
       <div class="req-note">Attention à <em>absent</em> et <em>absente</em> : une femme écrit <em>absente</em>, avec un e à la fin.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">Pour</span><span class="mail-v">Madame Leduc</span></div>
       <div class="mail-row"><span class="mail-k">Groupe</span><span class="mail-v">Francisation, niveau 2 — local 114</span></div>
       <textarea id="peText" rows="7" aria-label="Ton mot" data-min="3" data-max="5" oninput="peCount()" placeholder="Bonjour madame Leduc,&#10;Demain, je suis…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 3 à 5</span>
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
    "Je peux nommer six objets de ma classe.",
    "Je peux dire la couleur d'un objet.",
    "Je peux comprendre une consigne dite par mon enseignante.",
    "Je peux dire « je n'ai pas compris » et demander de répéter.",
    "Je peux demander une permission avec « est-ce que je peux… ? ».",
    "Je peux lire l'avis affiché près de la porte.",
    "Je peux prévenir mon enseignante d'un retard ou d'une absence.",
    "Je peux expliquer le fonctionnement de ma classe à une personne qui arrive.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Les objets de la classe</div>
     <textarea rows="2" placeholder="Ex. : un cahier, un crayon, une feuille, une gomme à effacer, le tableau, un pupitre…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les consignes</div>
     <textarea rows="2" placeholder="Ex. : ouvrez, fermez, écoutez, regardez, écrivez, effacez, donnez…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Quand je ne comprends pas</div>
     <textarea rows="2" placeholder="Ex. : je n'ai pas compris, pouvez-vous répéter ? plus lentement…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">La permission, le retard, l'absence</div>
     <textarea rows="2" placeholder="Ex. : est-ce que je peux… ? c'est permis, c'est interdit, en retard, absent…"></textarea>
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
