  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, une fiche écrite. Le jeu de rôle vient en premier parce qu'il
  // sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait la personne
  // jouée par l'assistant vit dans server.py.
  const ROLE_CAS = [
    {id:'table', titre:"À la table", txt:"On te demande les cases de ta fiche, <b>une à la fois</b> : nom, prénom, date de naissance."},
    {id:'adresse', titre:"L'adresse", txt:"On te demande où tu <b>habites</b> : le numéro, la rue, l'appartement, la ville."},
    {id:'chiffres', titre:"Les chiffres", txt:"On te demande ton <b>téléphone</b>, ton code postal et ton courriel. Ça va vite."},
  ];
  const ROLE_SUJETS = ["Dire son nom de famille","Dire son prénom",
    "Épeler son nom","Dire sa date de naissance",
    "Dire son adresse","Dire son numéro de téléphone",
    "Faire répéter plus lentement"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Réponds aux questions de la fiche</span></div>
     <p class="lead">L'assistant joue <b>la personne qui remplit ta fiche</b>. Elle parle lentement et pose une question à la fois. Si tu ne comprends pas, dis-le : c'est permis.</p>
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
         <button class="jr-opt" type="button" data-role="commis" onclick="jrChoisir('role','commis')">La personne au comptoir</button>
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
         <div><div class="jr-rappel-l">On te demande</div><div class="jr-rappel-x"><b>Quel</b> est votre nom de famille ?</div></div>
         <div><div class="jr-rappel-l">Tu réponds et tu épelles</div><div class="jr-rappel-x">Daoud. D - A - O - U - D.</div></div>
         <div><div class="jr-rappel-l">La date, dans l'ordre</div><div class="jr-rappel-x">Le <b>12</b> mars <b>1992</b>.</div></div>
         <div><div class="jr-rappel-l">Les chiffres, un par un</div><div class="jr-rappel-x">Cinq, un, quatre…</div></div>
         <div><div class="jr-rappel-l">Si ça va trop vite</div><div class="jr-rappel-x"><b>Plus lentement</b>, s'il vous plaît.</div></div>
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
     <h3 class="prod-tit">Donne tes renseignements</h3>
     <p class="prod-lead">On remplit ta fiche. Dis ton nom de famille et épelle-le, dis ta date de naissance dans l'ordre, puis ton adresse et ton téléphone.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Le nom et le prénom</div><div class="plan-ex">« Mon nom de famille est Daoud. D - A - O - U - D. Mon prénom est Yusuf. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">La date de naissance</div><div class="plan-ex">« Je suis né le 12 mars 1992. Douze, zéro trois, mille neuf cent quatre-vingt-douze. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">L'adresse et le téléphone</div><div class="plan-ex">« J'habite au 3120, avenue Papineau, appartement 4. Mon numéro est le 514 555 0198. »</div></div>
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
           <div class="rec-hint">Parle environ 40 secondes, lentement. Tu pourras recommencer autant de fois que tu veux.</div>
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
     <h3 class="prod-tit">Remplis ta fiche</h3>
     <p class="prod-lead">Écris tes vrais renseignements, une case par ligne. De 4 à 6 lignes.</p>
     <div class="req">
       <div class="req-hd">Ta fiche doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ton nom de famille, en lettres majuscules</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ton prénom</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ta date de naissance : jour / mois / année</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ton adresse, avec les abréviations</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ton numéro de téléphone</span></div>
       </div>
       <div class="req-note">Écris le jour <em>avant</em> le mois, l'année en quatre chiffres, et sers-toi de <em>app.</em>, <em>av.</em>, <em>boul.</em>, <em>QC</em>.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">Fiche</span><span class="mail-v">Inscription — nouvel élève</span></div>
       <div class="mail-row"><span class="mail-k">Centre</span><span class="mail-v">Francisation, niveau 1</span></div>
       <textarea id="peText" rows="7" aria-label="Ta fiche" data-min="4" data-max="6" oninput="peCount()" placeholder="NOM DE FAMILLE :&#10;PRÉNOM :&#10;DATE DE NAISSANCE :&#10;ADRESSE :&#10;TÉL. :"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 ligne sur 4 à 6</span>
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
    "Je peux comprendre la question « quel est votre nom de famille ? ».",
    "Je peux dire mon nom de famille et mon prénom, et les épeler.",
    "Je peux dire ma date de naissance dans l'ordre : jour, mois, année.",
    "Je peux dire mon adresse et lire les abréviations app., av., boul., QC.",
    "Je peux dire mon numéro de téléphone, un chiffre à la fois.",
    "Je peux écrire mes renseignements dans les cases d'une fiche.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">La fiche</div>
     <textarea rows="2" placeholder="Ex. : une inscription, une fiche, une case, remplir, en lettres majuscules…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Mon identité</div>
     <textarea rows="2" placeholder="Ex. : le nom de famille, le prénom, madame, monsieur, F, H…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Ma date de naissance</div>
     <textarea rows="2" placeholder="Ex. : le jour, le mois, l'année, 12 / 03 / 1992…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Où me joindre</div>
     <textarea rows="2" placeholder="Ex. : l'adresse, app., av., boul., QC, le code postal, Tél., le courriel…"></textarea>
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
