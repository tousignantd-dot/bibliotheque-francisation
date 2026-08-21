  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, un court message écrit. Le jeu de rôle vient en premier : il
  // sert de répétition avant les deux autres.
  // Seule la situation publique est ici. Ce que sait l'employée jouée par
  // l'assistant vit dans server.py, scénario « guichet ».
  const ROLE_CAS = [
    {id:'retrait', titre:"Devant le guichet", txt:"Tu veux retirer <b>quarante dollars</b>. C'est ta première fois et tu n'es pas sûr de l'ordre des étapes."},
    {id:'frais', titre:"L'écran parle de frais", txt:"L'écran écrit <b>« des frais de 3 $ »</b>. Tu ne comprends pas pourquoi, et tu veux savoir si tu peux dire non."},
    {id:'carte', titre:"La carte ne sort pas", txt:"Tu as ton argent, mais <b>ta carte est restée</b> dans la machine. Tu demandes de l'aide à l'employé du hall."},
  ];
  const ROLE_SUJETS = ["Dire ce qu'on veut faire","Donner le montant en dollars",
    "Demander sur quoi appuyer","Répéter le montant pour vérifier",
    "Demander de répéter plus lentement","Dire ce qu'on reprend avant de partir",
    "Dire merci"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Demande de l'aide au guichet</span></div>
     <p class="lead">L'assistant joue <b>l'employé du hall des guichets</b>. Il parle lentement et donne une information à la fois. Si tu ne comprends pas, dis-le : c'est permis, et c'est même ce qu'il faut faire. <b>Ne dis jamais ton NIP à voix haute</b> — l'employé ne le demande jamais.</p>
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
       Dis ce que tu veux :
       <span class='savoir-ex'>Je veux <b>retirer quarante dollars</b>.</span>
       Demande :
       <span class='savoir-ex'>Sur quel bouton <b>est-ce que j'appuie</b> ?</span>
       Fais ralentir :
       <span class='savoir-ex'><b>Plus lentement</b>, s'il vous plaît.</span>
       Vérifie :
       <span class='savoir-ex'>Quarante dollars. <b>C'est ça ?</b></span>
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
         <button class="jr-opt on" type="button" data-role="moi" onclick="jrChoisir('role','moi')">Moi, au guichet</button>
         <button class="jr-opt" type="button" data-role="employe" onclick="jrChoisir('role','employe')">L'employé qui aide</button>
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
     <h3 class="prod-tit">Explique ton retrait</h3>
     <p class="prod-lead">Explique à quelqu'un qui n'a jamais utilisé un guichet ce que tu fais, une étape à la fois : ce que tu mets, ce que tu tapes, ce que tu choisis, ce que tu prends.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">La carte et le NIP</div><div class="plan-ex">« Je mets ma carte dans le guichet. Je tape mon NIP. Je cache le clavier. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Le choix et le montant</div><div class="plan-ex">« Je choisis le retrait. J'appuie sur quarante dollars. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Ce qu'on reprend avant de partir</div><div class="plan-ex">« Je prends ma carte, mon argent et mon relevé. »</div></div>
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
     <h3 class="prod-tit">Écris ce que tu as fait à la caisse</h3>
     <p class="prod-lead">Écris un court message à un ami : ce que tu as fait au guichet cette semaine, combien tu as retiré, et ce que tu as payé par chèque ou par carte. De 4 à 6 phrases.</p>
     <div class="req">
       <div class="req-hd">Ton message doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le jour où tu es allé au guichet</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le montant retiré, en dollars</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce que tu as pris avant de partir</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Comment tu as payé : chèque, carte ou comptant</span></div>
       </div>
       <div class="req-note">Emploie <em>je mets</em>, <em>je tape</em>, <em>je choisis</em>, <em>je prends</em>, et les mots de l'argent : <em>un billet</em>, <em>un relevé</em>, <em>des frais</em>.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">Fiche</span><span class="mail-v">Ma semaine à la caisse</span></div>
       <div class="mail-row"><span class="mail-k">Centre</span><span class="mail-v">Francisation, niveau 2</span></div>
       <textarea id="peText" rows="7" aria-label="Ton message" data-min="4" data-max="6" oninput="peCount()" placeholder="Lundi, je vais au guichet.&#10;Je retire…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 4 à 6</span>
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
    "Je peux nommer l'argent : un billet, une pièce, un montant.",
    "Je peux dire un montant en dollars sans me tromper.",
    "Je peux lire les phrases de l'écran d'un guichet.",
    "Je peux faire un retrait du début à la fin.",
    "Je peux comprendre ce que sont des frais et dire non.",
    "Je peux remplir un chèque au complet et le signer.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">L'argent</div>
     <textarea rows="2" placeholder="Ex. : un billet, une pièce, le comptant, un montant…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Le guichet</div>
     <textarea rows="2" placeholder="Ex. : une carte de débit, un NIP, un retrait, un dépôt, un relevé, des frais…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Le chèque</div>
     <textarea rows="2" placeholder="Ex. : la date, le montant en lettres, la signature, le mémo…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Demander de l'aide</div>
     <textarea rows="2" placeholder="Ex. : plus lentement, vous pouvez répéter, sur quel bouton, c'est ça ?…"></textarea>
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
