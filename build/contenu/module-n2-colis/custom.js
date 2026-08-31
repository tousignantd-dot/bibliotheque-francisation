  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, une production écrite. Le jeu de rôle vient en premier
  // parce qu'il sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait Luc, joué par
  // l'assistant, vit dans server.py, scénario « colis ».
  const ROLE_CAS = [
    {id:'timbre', titre:"J'achète un timbre", txt:"Tu as une <b>lettre</b> à envoyer à Sherbrooke. Tu entres au comptoir postal de la pharmacie. Tu ne sais pas combien coûte un timbre."},
    {id:'colis', titre:"J'envoie un colis", txt:"Tu as une <b>boîte de deux kilos</b> à envoyer. Tu veux savoir le prix et ce qu'il faut écrire sur le formulaire."},
    {id:'avis', titre:"Je viens chercher mon colis", txt:"Tu as trouvé un <b>avis de livraison</b> dans ta boîte aux lettres. Tu viens chercher ton colis au comptoir."},
  ];
  const ROLE_SUJETS = ["Saluer, puis dire ce que tu veux en une phrase courte",
    "Demander le prix : « Combien ça coûte ? »",
    "Redire le montant que tu as entendu, pour vérifier",
    "Demander où écrire l'adresse ou où signer",
    "Demander de répéter quand ça va trop vite",
    "Demander ton reçu",
    "Remercier et souhaiter une bonne journée"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Fais ta démarche au comptoir postal</span></div>
     <p class="lead">L'assistant joue <b>Luc Tremblay, le préposé du comptoir postal</b>. Il répond en deux ou trois mots : à toi de dire ce que tu veux et de poser tes questions, une à la fois.</p>
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
         <button class="jr-opt" type="button" data-role="prepose" onclick="jrChoisir('role','prepose')">Le préposé du comptoir</button>
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
         <div><div class="jr-rappel-l">Dis ce que tu veux</div><div class="jr-rappel-x"><b>Un timbre</b>, s'il vous plaît. · <b>Je veux</b> envoyer ce colis.</div></div>
         <div><div class="jr-rappel-l">Demande le prix</div><div class="jr-rappel-x"><b>Combien</b> ça coûte ?</div></div>
         <div><div class="jr-rappel-l">Vérifie le montant</div><div class="jr-rappel-x"><b>Un dollar quarante-quatre</b> ? D'accord, merci.</div></div>
         <div><div class="jr-rappel-l">Demande où écrire</div><div class="jr-rappel-x">Je <b>signe</b> où ? · J'écris <b>mon</b> adresse où ?</div></div>
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
     <h3 class="prod-tit">Demande un timbre et le prix</h3>
     <p class="prod-lead">Tu entres au comptoir postal avec une lettre. Salue, dis ce que tu veux, demande le prix, redis le montant pour vérifier, puis remercie. Vouvoie la personne du début à la fin.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Ce que tu veux</div><div class="plan-ex">« Bonjour. Un timbre, s'il vous plaît. C'est pour Sherbrooke. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Le prix</div><div class="plan-ex">« Combien ça coûte ? … Un dollar quarante-quatre ? »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">La fin</div><div class="plan-ex">« Je le mets où ? … Merci beaucoup. Bonne journée. »</div></div>
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
     <h3 class="prod-tit">Écris l'adresse et remplis le formulaire</h3>
     <p class="prod-lead">Tu envoies un colis à quelqu'un que tu connais. Écris l'adresse complète du destinataire, puis ton adresse à toi, l'expéditeur. Une ligne par renseignement.</p>
     <div class="req">
       <div class="req-hd">Ton envoi doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le nom du destinataire : <em>prénom, puis nom de famille</em></span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le numéro, la rue et l'appartement : <em>145, rue King Ouest, app. 6</em></span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>La ville et la province : <em>Sherbrooke (Québec)</em></span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le code postal, six caractères</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ton nom et ton adresse, comme expéditeur</span></div>
       </div>
       <div class="req-note">Attention à l'ordre : le numéro vient <em>avant</em> la rue, et l'appartement vient <em>après</em>. Et devant une voyelle, on écrit <em>mon adresse</em>, jamais « ma adresse ».</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">Envoi</span><span class="mail-v">Un colis</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">L'adresse du destinataire et celle de l'expéditeur</span></div>
       <textarea id="peText" rows="8" aria-label="Ton adresse" data-min="5" data-max="8" oninput="peCount()" placeholder="Destinataire :&#10;Ousmane Diallo&#10;145, rue King Ouest, app. 6&#10;…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 5 à 8</span>
         <button class="btn-prod" id="peBtn" type="button" onclick="peCheck()">Vérifier mon adresse</button>
       </div>
     </div>
     <div class="fb" id="peFb" aria-live="polite"></div>
     <div class="status" id="peStatus">Analyse en cours…</div>
     <div class="err" id="peErr"></div>
   </div>`;
  const rb=document.getElementById('recBtn'); if(rb) rb.addEventListener('click',toggleRec);

  // JE RETIENS DES MOTS — notes + cartes mémoire + autoévaluation
  const SELF=[
    "Je peux nommer une lettre, une enveloppe, un timbre et un colis.",
    "Je peux dire ce que je veux en une phrase courte au comptoir.",
    "Je peux demander le prix avec « Combien ça coûte ? ».",
    "Je peux redire un montant en dollars pour vérifier.",
    "Je peux écrire les quatre lignes d'une adresse dans le bon ordre.",
    "Je peux écrire un code postal et le dire caractère par caractère.",
    "Je peux dire qui est l'expéditeur et qui est le destinataire.",
    "Je peux remplir les cases d'un formulaire et signer au bon endroit.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Les objets de la poste</div>
     <textarea rows="2" placeholder="Ex. : une lettre, une enveloppe, un timbre, un colis, une boîte aux lettres, un comptoir postal…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les mots de l'adresse</div>
     <textarea rows="2" placeholder="Ex. : une adresse, une rue, un appartement, un code postal, un expéditeur, un destinataire, app., boul., av.…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les mots du formulaire</div>
     <textarea rows="2" placeholder="Ex. : un formulaire, nom, prénom, ville, province, une signature, une date, un reçu…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les phrases du comptoir</div>
     <textarea rows="2" placeholder="Ex. : Un timbre, s'il vous plaît. · Combien ça coûte ? · Je signe où ? · Pouvez-vous répéter ?…"></textarea>
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
