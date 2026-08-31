  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, un court message écrit. Le jeu de rôle vient en premier
  // parce qu'il sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait madame
  // Bourgeois, jouée par l'assistant, vit dans server.py, scénario
  // « inscription ».
  const ROLE_CAS = [
    {id:'annonce', titre:"Je téléphone au sujet de l'annonce", txt:"Tu as vu une <b>annonce</b> : « Cours de français, tous les matins ». Elle ne dit ni la date, ni l'heure, ni le local. Tu appelles le secrétariat."},
    {id:'formulaire', titre:"Je remplis mon formulaire", txt:"Tu es au comptoir du <b>local 005</b>, avec un formulaire vide et un stylo. La secrétaire demande les cases une à une."},
    {id:'epeler', titre:"Comment ça s'écrit ?", txt:"La secrétaire écrit ton nom à l'ordinateur. Elle ne sait pas comment il s'écrit. Tu l'<b>épelles</b>, lettre par lettre."},
  ];
  const ROLE_SUJETS = ["Dire pourquoi tu viens : « je voudrais m'inscrire »",
    "Demander la date, l'heure et le lieu, une question à la fois",
    "Donner ton nom de famille, puis ton prénom",
    "Épeler ton nom lentement, lettre par lettre",
    "Donner ta date de naissance, ton adresse, ton téléphone",
    "Demander « c'est quoi, cette case ? » quand tu ne comprends pas",
    "Redire la date et l'heure pour vérifier, puis remercier"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Inscris-toi au cours</span></div>
     <p class="lead">L'assistant joue <b>madame Bourgeois, la secrétaire du Centre Delorme</b>. Elle demande une seule case à la fois et attend ta réponse. Si tu ne comprends pas un mot, dis-le : « c'est quoi, cette case ? » fait partie de l'inscription.</p>
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
         <button class="jr-opt" type="button" data-role="secretaire" onclick="jrChoisir('role','secretaire')">La secrétaire qui demande</button>
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
         <div><div class="jr-rappel-l">Dis pourquoi tu viens</div><div class="jr-rappel-x">Bonjour. <b>Je voudrais m'inscrire</b> au cours de français.</div></div>
         <div><div class="jr-rappel-l">Demande l'horaire</div><div class="jr-rappel-x">Le cours est <b>de</b> quelle heure <b>à</b> quelle heure ?</div></div>
         <div><div class="jr-rappel-l">Réponds au comptoir</div><div class="jr-rappel-x"><b>Mon nom de famille</b>, c'est… <b>Mon prénom</b>, c'est…</div></div>
         <div><div class="jr-rappel-l">Épelle</div><div class="jr-rappel-x">H, A, <b>deux D</b>, A, D. <b>D comme dimanche.</b></div></div>
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
     <h3 class="prod-tit">Inscris-toi au comptoir du secrétariat</h3>
     <p class="prod-lead">Tu entres au secrétariat pour t'inscrire au cours de français. Dis pourquoi tu viens, donne ton nom de famille et ton prénom, épelle ton nom lentement, puis donne ta date de naissance et ton adresse. Vouvoie la personne du début à la fin.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Pourquoi tu viens</div><div class="plan-ex">« Bonjour. Je voudrais m'inscrire au cours de français. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Ton nom, épelé</div><div class="plan-ex">« Mon nom de famille, c'est… H, A, deux D, A, D. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Tes renseignements</div><div class="plan-ex">« Ma date de naissance, c'est le 7 mars 1994. Mon adresse, c'est… »</div></div>
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
     <h3 class="prod-tit">Écris au secrétariat pour demander une place</h3>
     <p class="prod-lead">Tu ne peux pas passer au centre cette semaine. Écris un court message au secrétariat : dis que tu veux t'inscrire, donne ton nom, ta date de naissance et ton téléphone. De 3 à 5 phrases.</p>
     <div class="req">
       <div class="req-hd">Ton message doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>« Bonjour madame », au début</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce que tu veux : <em>je voudrais m'inscrire au cours de français</em></span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ton nom de famille et ton prénom</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ta date de naissance, écrite <em>année, mois, jour</em></span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ton numéro de téléphone, et « merci » à la fin</span></div>
       </div>
       <div class="req-note">Attention à <em>mon</em> et <em>ma</em> : on écrit <em>mon nom</em>, mais <em>ma date de naissance</em> — et <em>mon adresse</em>, jamais « ma adresse ».</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">Pour</span><span class="mail-v">Le secrétariat du Centre Delorme</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Inscription au cours de français</span></div>
       <textarea id="peText" rows="7" aria-label="Ton message" data-min="3" data-max="5" oninput="peCount()" placeholder="Bonjour madame,&#10;Je voudrais m'inscrire au…"></textarea>
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
    "Je peux nommer ce qu'il y a sur un formulaire d'inscription.",
    "Je peux dire « je voudrais m'inscrire au cours de français ».",
    "Je peux épeler mon nom de famille lettre par lettre.",
    "Je peux lire une date écrite en chiffres.",
    "Je peux trouver la date, l'heure et le lieu dans une petite annonce.",
    "Je peux écrire ces renseignements en quatre lignes.",
    "Je peux remplir les cases d'un formulaire d'inscription.",
    "Je peux demander « c'est quoi, cette case ? » quand je ne comprends pas.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Le secrétariat et le formulaire</div>
     <textarea rows="2" placeholder="Ex. : une inscription, un formulaire, une case, une signature, une pièce d'identité…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les cases : qui je suis</div>
     <textarea rows="2" placeholder="Ex. : le nom de famille, le prénom, la date de naissance, l'adresse, le courriel, la scolarité…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">L'annonce : quand et où</div>
     <textarea rows="2" placeholder="Ex. : une annonce, un cours, une date, un horaire, un lieu, du lundi au vendredi, de 8 h 30 à 12 h 30…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Épeler et vérifier</div>
     <textarea rows="2" placeholder="Ex. : comment ça s'écrit ? deux D, B comme bonjour, doucement, c'est bien écrit ?"></textarea>
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
