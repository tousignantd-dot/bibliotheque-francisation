  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, un mot écrit de trois lignes. Le jeu de rôle vient en premier
  // parce qu'il sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait Gilles, joué
  // par l'assistant, vit dans server.py, scénario « couloirs ».
  const ROLE_CAS = [
    {id:'local', titre:"Je cherche le local 214", txt:"C'est ta <b>première journée</b> au centre. Sur ta feuille, il y a un numéro : 214. Tu ne sais pas où c'est."},
    {id:'casiers', titre:"Les casiers et les toilettes", txt:"C'est la <b>pause</b>. Tu cherches la salle des casiers, et tu voudrais aussi savoir où sont les toilettes."},
    {id:'indiquer', titre:"C'est moi qui explique", txt:"Une personne <b>arrive au centre</b> et cherche le secrétariat. Cette fois, c'est toi qui connais le bâtiment."},
  ];
  const ROLE_SUJETS = ["Dire « excusez-moi » avant de poser la question",
    "Demander avec « où est » ou « où sont »",
    "Écouter l'étage : rez-de-chaussée, premier, deuxième",
    "Écouter le côté : à gauche, à droite, tout droit, au bout",
    "Redire l'indication dans tes mots pour vérifier",
    "Demander de répéter quand ça va trop vite",
    "Remercier et prendre congé"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Demande ton chemin</span></div>
     <p class="lead">L'assistant joue <b>Gilles, le concierge du centre</b>. Il donne une seule indication à la fois : l'étage d'abord, le côté ensuite. Si tu ne comprends pas, dis-le : « pouvez-vous répéter ? » fait partie du corridor.</p>
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
         <button class="jr-opt" type="button" data-role="concierge" onclick="jrChoisir('role','concierge')">Le concierge qui répond</button>
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
         <div><div class="jr-rappel-l">Pose ta question</div><div class="jr-rappel-x">Excusez-moi, <b>où est</b> le local 214 ?</div></div>
         <div><div class="jr-rappel-l">Au pluriel</div><div class="jr-rappel-x"><b>Où sont</b> les toilettes, s'il vous plaît ?</div></div>
         <div><div class="jr-rappel-l">Redis l'indication</div><div class="jr-rappel-x"><b>Au deuxième étage</b>, au bout du corridor, à droite ?</div></div>
         <div><div class="jr-rappel-l">Indique à ton tour</div><div class="jr-rappel-x">C'est au premier étage. <b>Prenez l'escalier</b>, puis à gauche.</div></div>
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
     <h3 class="prod-tit">Fais visiter le centre à une personne qui arrive</h3>
     <p class="prod-lead">Une personne entre au centre pour la première fois. Dis-lui à quel étage est son local, où est l'escalier, où sont les toilettes et où est la cafétéria. Donne l'étage d'abord, le côté ensuite. Vouvoie-la du début à la fin.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">L'étage</div><div class="plan-ex">« Votre local, c'est le 214. C'est au deuxième étage. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Le chemin</div><div class="plan-ex">« Prenez l'escalier, au milieu du corridor. Puis à droite. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Deux repères utiles</div><div class="plan-ex">« Les toilettes sont en face de l'ascenseur. La cafétéria est au rez-de-chaussée. »</div></div>
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
     <h3 class="prod-tit">Écris où est ton local</h3>
     <p class="prod-lead">Une personne de ton groupe arrive demain et ne connaît pas le centre. Écris-lui un petit mot : le numéro du local, l'étage, et où c'est dans le corridor. De 3 à 5 phrases.</p>
     <div class="req">
       <div class="req-hd">Ton mot doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le prénom de la personne, au début</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le numéro du local, écrit en chiffres</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>L'étage : <em>au rez-de-chaussée</em>, <em>au premier étage</em>, <em>au deuxième étage</em></span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un repère : <em>à côté de</em>, <em>en face de</em>, <em>au bout du corridor</em></span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ton prénom, sur la dernière ligne</span></div>
       </div>
       <div class="req-note">Attention à <em>au</em> et <em>à la</em> : on écrit <em>au deuxième étage</em>, mais <em>à la cafétéria</em>.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">Pour</span><span class="mail-v">Une personne de mon groupe</span></div>
       <div class="mail-row"><span class="mail-k">Centre</span><span class="mail-v">Francisation, niveau 2 — Centre Bellevue</span></div>
       <textarea id="peText" rows="7" aria-label="Ton mot" data-min="3" data-max="5" oninput="peCount()" placeholder="Bonjour Amina,&#10;Notre local, c'est le…"></textarea>
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
    "Je peux nommer six endroits de mon centre.",
    "Je peux dire à quel étage est mon local.",
    "Je peux lire un numéro de porte et trouver l'étage.",
    "Je peux lire le plan affiché dans mon centre.",
    "Je peux demander « où est… ? » et « où sont… ? ».",
    "Je peux comprendre à gauche, à droite, tout droit, au bout du corridor.",
    "Je peux dire où est un endroit avec « à côté de » ou « en face de ».",
    "Je peux indiquer le chemin à une personne qui arrive au centre.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Les endroits du centre</div>
     <textarea rows="2" placeholder="Ex. : un corridor, un local, l'accueil, le secrétariat, la cafétéria, la bibliothèque…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Monter, descendre, changer d'étage</div>
     <textarea rows="2" placeholder="Ex. : un étage, le rez-de-chaussée, un escalier, un ascenseur, monter, descendre…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Demander son chemin</div>
     <textarea rows="2" placeholder="Ex. : excusez-moi, où est… ? où sont… ? c'est où ? pouvez-vous répéter ?"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Dire où c'est</div>
     <textarea rows="2" placeholder="Ex. : à gauche, à droite, tout droit, au bout du corridor, à côté de, en face de…"></textarea>
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
