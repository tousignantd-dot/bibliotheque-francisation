  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, un court message écrit. Le jeu de rôle vient en premier
  // parce qu'il sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait le personnage
  // joué par l'assistant vit dans server.py, scénario `titre`.
  const ROLE_CAS = [
    {id:'mensuel', titre:'Le titre du mois', txt:"Tu te déplaces <b>cinq jours par semaine</b>, matin et soir, dans la zone A. Tu achètes encore des titres à l'unité. Tu viens demander s'il existe mieux, et combien ça coûte."},
    {id:'reduit', titre:'Le tarif réduit de la famille', txt:"Ta fille a <b>quinze ans</b> et ta mère <b>soixante-huit ans</b>. Tu veux savoir si elles paient moins cher, ce qu'il faut apporter et où faire les cartes."},
    {id:'occasionnel', titre:'La visiteuse de trois jours', txt:"Une personne de ta famille arrive <b>samedi</b> et repart <b>lundi</b>. Elle veut visiter la ville et elle n'a <b>aucune carte</b>. Tu viens demander quel titre prendre."},
  ];
  const ROLE_SUJETS = ["Saluer et dire ce que tu viens chercher","Dire combien de fois par semaine tu te déplaces",
    "Dire dans quelle zone tu restes","Demander le prix du titre",
    "Demander si tu as droit au tarif réduit, et ce qu'il faut apporter",
    "Faire répéter si tu n'as pas compris un chiffre",
    "Répéter le titre et le prix à voix haute avant de payer"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Achète ton titre de transport</span></div>
     <p class="lead">L'assistant tient <b>le comptoir du point de service</b>. Il ne dit rien que tu ne lui demandes pas : le prix, la durée, le tarif réduit, la carte, tout se demande. À toi de poser tes questions.</p>
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
       Entre poliment :
       <span class='savoir-ex'><b>Je voudrais</b> un titre mensuel, s'il vous plaît.</span>
       Demande le prix :
       <span class='savoir-ex'><b>Combien</b> coûte ce titre-là ?</span>
       Demande la permission :
       <span class='savoir-ex'><b>Est-ce que je peux</b> payer par carte ?</span>
       Fais répéter :
       <span class='savoir-ex'>Pardon, <b>pouvez-vous répéter</b>, s'il vous plaît ?</span>
       Vérifie avant de payer :
       <span class='savoir-ex'>Un mensuel, zone A, cent dix dollars, bon <b>jusqu'à</b> la fin du mois. C'est ça ?</span>
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
         <button class="jr-opt on" type="button" data-role="client" onclick="jrChoisir('role','client')">Le client</button>
         <button class="jr-opt" type="button" data-role="prepose" onclick="jrChoisir('role','prepose')">La personne au comptoir</button>
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
     <h3 class="prod-tit">Achète le titre qu'il te faut</h3>
     <p class="prod-lead">Tu es devant le comptoir du point de service. Salue, dis ce que tu viens chercher, dis combien de fois par semaine tu te déplaces, demande le prix et le tarif réduit, puis répète le titre et le prix avant de payer.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Dire ce que tu viens chercher</div><div class="plan-ex">« Bonjour. Je voudrais un titre de transport, s'il vous plaît. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Demander le prix et le tarif réduit</div><div class="plan-ex">« Combien coûte le mensuel ? Est-ce que ma fille de quinze ans paie moins cher ? »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Répéter avant de payer</div><div class="plan-ex">« Un mensuel, zone A, cent dix dollars, bon jusqu'à la fin du mois. C'est ça ? »</div></div>
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
     <h3 class="prod-tit">Écris à la personne qui arrive</h3>
     <p class="prod-lead">Quelqu'un de ta famille arrive à Montréal la semaine prochaine et ne connaît rien au transport collectif. Écris-lui un court message : quel titre acheter, combien ça coûte, où l'acheter et ce qu'il faut savoir. De 5 à 8 phrases.</p>
     <div class="req">
       <div class="req-hd">Ton message doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le titre que tu conseilles, et pourquoi celui-là</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Son prix, écrit en chiffres avec une virgule et le signe $</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Où l'acheter : le point de service ou la borne de la station</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Jusqu'à quand il est bon, avec « jusqu'à », « du… au… » ou « pendant »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une chose à ne pas oublier : valider sa carte, ou la carte avec photo</span></div>
       </div>
       <div class="req-note">Attention aux petits mots : <em>ce</em> titre-là, <em>cette</em> carte-là, <em>du</em> lundi <em>au</em> dimanche, <em>jusqu'à</em> la fin du mois, moins cher <em>que</em> l'hebdo.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">Pour</span><span class="mail-v">La personne qui arrive</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Quel titre de transport acheter</span></div>
       <textarea id="peText" rows="7" aria-label="Ton message" data-min="5" data-max="8" oninput="peCount()" placeholder="Bonjour. Pour te déplacer à Montréal, je te conseille…&#10;Ça coûte…"></textarea>
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
    "Je peux nommer ce qu'on trouve dans une station : le point de service, la borne, le tourniquet.",
    "Je sais ce qu'est une carte OPUS et ce qu'on met dessus.",
    "Je comprends les quatre titres principaux : passage, dix passages, hebdo, mensuel.",
    "Je peux dire et écrire un prix : trois dollars soixante-quinze, 3,75 $.",
    "Je peux demander le prix d'un titre au comptoir.",
    "Je peux demander si j'ai droit au tarif réduit et ce qu'il faut apporter.",
    "J'ose faire répéter quand je n'ai pas compris un chiffre.",
    "Je peux lire la grille des tarifs : la ligne, la colonne, le prix.",
    "Je comprends jusqu'à quand un titre est bon : du lundi au dimanche, jusqu'à la fin du mois.",
    "Je sais qui a droit aux places réservées et ce qu'est le transport adapté.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">La station et la carte</div>
     <textarea rows="2" placeholder="Ex. : une carte OPUS, le point de service, la borne, le tourniquet, valider, recharger…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les titres et les prix</div>
     <textarea rows="2" placeholder="Ex. : un passage, dix passages, l'hebdo, le mensuel, 3,75 $, 110 $, le tarif réduit…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Demander au comptoir</div>
     <textarea rows="2" placeholder="Ex. : je voudrais…, combien coûte…, est-ce que je peux…, pouvez-vous répéter…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Lire la grille</div>
     <textarea rows="2" placeholder="Ex. : la zone A, de 18 h à 5 h, du lundi au dimanche, jusqu'à la fin du mois, 65 ans et plus…"></textarea>
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
