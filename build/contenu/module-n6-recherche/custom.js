  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : l'entrevue avec l'assistant, une prise orale corrigée,
  // puis la demande d'emploi écrite. Le jeu de rôle vient en premier parce
  // qu'il sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait l'employeur
  // joué par l'assistant vit dans server.py.
  const ROLE_CAS = [
    {id:'inventaire', titre:"Commis à l'inventaire", txt:"Vous postulez chez <b>Boisverte</b>, un fabricant de meubles de quarante employés. Le poste est permanent, 37,5 h. Deux ans d'expérience en entrepôt sont requis."},
    {id:'restauration', titre:"Aide-cuisinier", txt:"Vous postulez dans un <b>restaurant de quartier</b>. Le poste est à temps partiel, surtout les soirs et les fins de semaine. L'expérience est un atout, pas une exigence."},
    {id:'entretien', titre:"Préposé à l'entretien", txt:"Vous postulez dans un <b>immeuble de bureaux</b>. Horaire de soir, du lundi au vendredi. L'employeur demande de la ponctualité et de l'autonomie."},
  ];
  const ROLE_SUJETS = ["Saluer et vous présenter","Résumer votre parcours en trois phrases",
    "Donner un exemple précis, avec un chiffre","Dire ce que vous savez faire",
    "Dire honnêtement ce que vous ne connaissez pas encore",
    "Poser au moins une question sur le poste",
    "Remercier et demander la suite"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Passez l'entrevue</span></div>
     <p class="lead">L'assistant joue <b>l'employeur</b>. Il pose des questions ouvertes, comme dans une vraie entrevue : à vous de développer vos réponses au lieu de répondre en une phrase.</p>
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
       <div class="jr-gram-t">Réutilisez ce que vous venez d'apprendre</div>
       Développez avec un exemple :
       <span class='savoir-ex'>Je faisais plusieurs tâches, <b>par exemple</b> recevoir les livraisons.</span>
       Dites ce qui vient avant :
       <span class='savoir-ex'><b>Après avoir vérifié</b> les commandes, je préparais les bons de livraison.</span>
       Placez une information qu'on ne vous demande pas :
       <span class='savoir-ex'>J'aimerais que vous <b>sachiez</b> que j'ai déjà utilisé un logiciel semblable.</span>
       Parlez d'un lieu ou d'un moment :
       <span class='savoir-ex'>C'est l'entreprise <b>où</b> j'ai appris le métier.</span>
     </div>

     <div class="jr-sep"></div>
     <div class="jr-sub">Choisissez votre situation et votre rôle</div>
     <div class="jr-choix">
       <div class="jr-choix-l">Quel poste ?</div>
       <div class="jr-opts" id="jrLogs">
         ${ROLE_CAS.map((c,i)=>`<button class="jr-opt${i===0?' on':''}" type="button" data-log="${c.id}" onclick="jrChoisir('log','${c.id}')">${esc(c.titre)}</button>`).join('')}
       </div>
       <div class="jr-choix-l">Vous jouez qui ?</div>
       <div class="jr-opts" id="jrRoles">
         <button class="jr-opt on" type="button" data-role="candidat" onclick="jrChoisir('role','candidat')">Le candidat</button>
         <button class="jr-opt" type="button" data-role="employeur" onclick="jrChoisir('role','employeur')">L'employeur</button>
       </div>
       <div class="jr-choix-l">Comment ?</div>
       <div class="jr-opts" id="jrModes">
         <button class="jr-opt on" type="button" data-mode="texte" onclick="jrModeVoix(false)">✍️ Écrire</button>
         <button class="jr-opt" type="button" data-mode="voix" onclick="jrModeVoix(true)">🎤 Parler</button>
       </div>
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()" style="margin-top:14px">Commencer l'entrevue</button>
     </div>

     <div id="jrChat" class="hidden">
       <div class="jr-fil" id="jrFil" aria-live="polite"></div>
       <div class="jr-mic hidden" id="jrMicZone">
         <button id="jrMic" type="button" onclick="jrParler()" aria-label="Parler">🎤</button>
         <span class="jr-mic-l" id="jrMicLbl">Touchez pour parler</span>
       </div>
       <div class="jr-saisie">
         <input id="jrInput" type="text" placeholder="Écrivez ce que vous dites…" autocomplete="off"
                onkeydown="if(event.key==='Enter'){event.preventDefault();jrEnvoyer();}">
         <button class="btn btn-pri" id="jrSend" type="button" onclick="jrEnvoyer()">Envoyer</button>
       </div>
       <div class="status" id="jrStatus">L'assistant réfléchit…</div>
       <div class="err" id="jrErr"></div>
       <div class="jr-fin">
         <button class="btn btn-ghost" type="button" onclick="jrRecommencer()">↺ Recommencer</button>
         <button class="btn btn-send" type="button" onclick="jrFini()">J'ai fini — corrigez mes phrases</button>
       </div>
       <div class="fb" id="jrFb" aria-live="polite"></div>
     </div>
   </div>

   <div class="card custom">
     <div class="prod-eyebrow"><span class="prod-num">1</span><span class="prod-kind">Production orale</span></div>
     <h3 class="prod-tit">Offrez vos services</h3>
     <p class="prod-lead">Un employeur vous dit : « Parlez-moi de vous. » Répondez en 90 secondes environ : votre parcours, un exemple précis, et ce que vous cherchez.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Qui vous êtes et ce que vous avez fait</div><div class="plan-ex">« J'ai six ans d'expérience en gestion des stocks, dans le domaine du meuble. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Un exemple précis, avec un chiffre</div><div class="plan-ex">« Je tenais l'inventaire de 800 références, notamment les commandes urgentes. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Ce que vous cherchez et ce que vous offrez</div><div class="plan-ex">« Je suis prête à apprendre votre logiciel et disponible dès le mois prochain. »</div></div>
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
           <div class="rec-lbl" id="recLbl">Touchez pour vous enregistrer</div>
           <div class="rec-hint">Parlez environ 90 secondes. Vous pourrez recommencer autant de fois que vous voulez.</div>
         </div>
       </div>
     </div>
     <div id="poPrev" class="hidden prod-tools" style="display:flex;flex-direction:column;gap:12px">
       <audio id="poAudio" controls style="width:100%"></audio>
       <textarea id="poText" rows="2" placeholder="Transcription automatique (vous pouvez la corriger)…"></textarea>
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
     <h3 class="prod-tit">Remplissez la page trois de la demande d'emploi</h3>
     <p class="prod-lead">C'est la rubrique qui décide : « Décrivez vos fonctions et votre expérience. » Écrivez de 6 à 10 phrases, organisées en deux courts paragraphes.</p>
     <div class="req">
       <div class="req-hd">Votre texte doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le titre exact de votre dernier poste</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Au moins quatre verbes d'action à l'imparfait</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Au moins un chiffre (durée, quantité, nombre de personnes)</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une phrase avec « après avoir » ou « après être »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un connecteur d'exemple : par exemple, notamment, entre autres</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une phrase avec « où » : l'entreprise où…, l'année où…</span></div>
       </div>
       <div class="req-note">Évitez les phrases vides : « j'ai travaillé dans un entrepôt » ne dit rien. Dites <em>ce que vous faisiez</em>, <em>combien</em>, et <em>ce que ça a donné</em>.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">Formulaire</span><span class="mail-v">Demande d'emploi — page 3 de 4</span></div>
       <div class="mail-row"><span class="mail-k">Rubrique</span><span class="mail-v">Description des fonctions et de l'expérience</span></div>
       <textarea id="peText" rows="9" aria-label="Votre description" data-min="6" data-max="10" oninput="peCount()" placeholder="Responsable des stocks, Muebles del Valle, Medellín, 2017-2023.&#10;Je recevais les livraisons et je vérifiais les quantités…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 6 à 10</span>
         <button class="btn-prod" id="peBtn" type="button" onclick="peCheck()">Vérifier mon texte</button>
       </div>
     </div>
     <div class="fb" id="peFb" aria-live="polite"></div>
     <div class="status" id="peStatus">Analyse en cours…</div>
     <div class="err" id="peErr"></div>
   </div>`;
  const rb=document.getElementById('recBtn'); if(rb) rb.addEventListener('click',toggleRec);

  // JE RETIENS DES MOTS — notes + cartes mémoire + autoévaluation
  const SELF=[
    "Je peux nommer un poste et le secteur d'activité où on l'exerce.",
    "Je repère les quatre parties d'une offre d'emploi détaillée.",
    "Je fais la différence entre une exigence et un atout.",
    "Je comprends les mots en -able et en -ible : transférable, disponible, renouvelable.",
    "Je peux relier deux phrases avec « où » sans me tromper d'accent.",
    "Je peux décrire mes tâches passées avec des verbes d'action et des chiffres.",
    "J'emploie « après avoir » et « après être » pour dire ce qui vient avant.",
    "Je connais les formules d'une lettre de motivation, de l'appel à la salutation.",
    "Je peux développer une réponse d'entrevue avec un exemple précis.",
    "Je pose au moins une question à l'employeur à la fin d'une entrevue.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Le poste et le secteur</div>
     <textarea rows="2" placeholder="Ex. : un poste, un secteur d'activité, un ordre professionnel, le temps partiel, un curriculum vitæ…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Lire l'offre</div>
     <textarea rows="2" placeholder="Ex. : une offre d'emploi, une tâche, une exigence, requis, un atout, un poste permanent…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Écrire la demande</div>
     <textarea rows="2" placeholder="Ex. : une demande d'emploi, une lettre de motivation, une référence, les disponibilités, veuillez agréer…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Passer l'entrevue</div>
     <textarea rows="2" placeholder="Ex. : une entrevue, une compétence, l'assurance collective, par exemple, notamment, c'est-à-dire…"></textarea>
   </div>
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Autoévaluation</span><span class="ctit" style="color:#A5335F">Qu'est-ce que je suis capable de faire ?</span></div>
     <p class="lead">Pour chaque énoncé, choisissez : pas encore 😟, un peu 🙂, ou oui 😃.</p>
     ${SELF.map((s,i)=>`<div class="selfrow"><div class="self-txt">${s}</div><div class="self-opts">
        <button onclick="rate(${i},this)">😟</button><button onclick="rate(${i},this)">🙂</button><button onclick="rate(${i},this)">😃</button>
     </div></div>`).join('')}
     <div style="margin-top:16px"><button class="btn btn-pri" onclick="finishEval()">Terminer le module 🎉</button></div>
     <div id="evalDone" class="fb" aria-live="polite"></div>
   </div>`;
}
