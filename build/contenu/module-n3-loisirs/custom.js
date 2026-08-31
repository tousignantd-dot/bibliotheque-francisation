  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, un court message écrit. Le jeu de rôle vient en premier
  // parce qu'il sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait Roxane, la
  // préposée jouée par l'assistant, vit dans server.py (scénario « loisirs »).
  const ROLE_CAS = [
    {id:'badminton', titre:'Le badminton du mardi', txt:"Tu veux essayer le <b>badminton libre</b> au gymnase. Tu ne sais pas encore quel soir, ni combien ça coûte, ni s'il faut apporter une raquette."},
    {id:'cine', titre:'Le ciné-club du vendredi', txt:"Tu veux aller voir un film avec <b>un enfant de huit ans</b>. Tu ne sais pas quel film convient, à quelle heure c'est, ni s'il faut réserver."},
    {id:'cuisine', titre:'La cuisine collective', txt:"Tu n'as jamais fait de <b>cuisine collective</b>. Tu veux comprendre comment ça marche : quel jour, combien ça coûte, et ce qu'il faut apporter."},
  ];
  const ROLE_SUJETS = ["Saluer et dire ce que tu cherches","Demander le jour et l'heure",
    "Demander le tarif","Demander ce qu'il faut apporter",
    "Demander où c'est dans le centre","Faire répéter ce que tu n'as pas compris",
    "Répéter les quatre renseignements avant de partir"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Renseigne-toi au comptoir</span></div>
     <p class="lead">L'assistant joue <b>Roxane, la préposée à l'accueil</b>. Elle ne dit rien que tu ne lui demandes pas : le jour, l'heure, le prix, ce qu'il faut apporter — tout se demande. À toi de poser tes quatre questions.</p>
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
         <button class="jr-opt on" type="button" data-role="visiteur" onclick="jrChoisir('role','visiteur')">La personne qui se renseigne</button>
         <button class="jr-opt" type="button" data-role="prepose" onclick="jrChoisir('role','prepose')">La préposée</button>
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
         <div><div class="jr-rappel-l">Ouvre poliment</div><div class="jr-rappel-x"><b>Je voudrais</b> des renseignements, s'il vous plaît.</div></div>
         <div><div class="jr-rappel-l">Pose tes quatre questions</div><div class="jr-rappel-x">C'est quand ? C'est combien ? C'est où ? <b>Qu'est-ce qu'il faut apporter ?</b></div></div>
         <div><div class="jr-rappel-l">Fais répéter</div><div class="jr-rappel-x"><b>Vous pourriez</b> répéter, s'il vous plaît ?</div></div>
         <div><div class="jr-rappel-l">Répète pour vérifier</div><div class="jr-rappel-x">Alors <b>le mardi</b>, à <b>sept heures</b>, trois dollars, des espadrilles.</div></div>
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
     <h3 class="prod-tit">Renseigne-toi sur une activité de ton quartier</h3>
     <p class="prod-lead">Choisis une activité que tu aimerais essayer près de chez toi. Salue, dis ce que tu cherches avec « je voudrais », puis pose tes quatre questions : quand, combien, où, quoi apporter. Termine en répétant ce que tu as compris.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Saluer et dire ce que tu cherches</div><div class="plan-ex">« Bonjour. Je voudrais des renseignements sur le badminton, s'il vous plaît. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Poser tes quatre questions</div><div class="plan-ex">« C'est quel jour ? C'est combien ? C'est où ? Qu'est-ce qu'il faut apporter ? »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Répéter pour vérifier</div><div class="plan-ex">« Alors le mardi, à sept heures, trois dollars, des espadrilles. Merci beaucoup ! »</div></div>
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
     <h3 class="prod-tit">Invite quelqu'un à venir avec toi</h3>
     <p class="prod-lead">Tu as choisi une activité. Écris un court message à une personne que tu veux emmener : dis ce que c'est, quel jour, à quelle heure, combien ça coûte et ce qu'il faut apporter. De 5 à 8 phrases.</p>
     <div class="req">
       <div class="req-hd">Ton message doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le nom de l'activité et l'endroit où elle a lieu</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le jour avec « le » si c'est toutes les semaines : le mardi soir</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>L'heure du début et de la fin : de sept heures à neuf heures</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le tarif, et ce qu'il faut apporter</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une question à la fin, pour savoir si la personne veut venir</span></div>
       </div>
       <div class="req-note">Attention aux petits mots : <em>le</em> mardi soir, <em>de</em> sept heures <em>à</em> neuf heures, <em>des</em> espadrilles.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">Pour</span><span class="mail-v">Une personne que tu veux emmener</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Une activité au centre du quartier</span></div>
       <textarea id="peText" rows="7" aria-label="Ton message" data-min="5" data-max="8" oninput="peCount()" placeholder="Bonjour ! J'ai trouvé une activité au centre communautaire de la rue Galt.&#10;C'est du badminton, le mardi soir…"></textarea>
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
    "Je peux nommer les endroits d'un centre communautaire : le gymnase, la cuisine, le babillard.",
    "Je comprends un feuillet de loisirs : le jour, l'heure, le tarif.",
    "Je fais la différence entre « mardi » et « le mardi ».",
    "Je peux poser mes quatre questions : quand, combien, où, quoi apporter.",
    "Je demande poliment avec « je voudrais » et « est-ce que je pourrais ».",
    "Je fais répéter quand je n'ai pas compris.",
    "Je comprends « dix-neuf heures trente » et je sais le dire autrement.",
    "Je lis une brève description de film : le genre, la durée, l'heure.",
    "Je comprends les consignes d'une recette : pelez, coupez, ajoutez, mélangez.",
    "Je comprends les quantités et les abréviations : 60 ml, c. à soupe, c. à thé.",
    "Je répète ce qu'on m'a répondu avant de partir.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Le centre de quartier</div>
     <textarea rows="2" placeholder="Ex. : un centre communautaire, un babillard, un feuillet, une session, le gymnase, une salle…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">L'horaire et le tarif</div>
     <textarea rows="2" placeholder="Ex. : le mardi soir, de sept heures à neuf heures, une séance, le tarif, gratuit, une preuve d'adresse…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Le ciné-club</div>
     <textarea rows="2" placeholder="Ex. : un ciné-club, un téléhoraire, un drame, une comédie, un documentaire, la durée, sous-titré…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">La cuisine collective</div>
     <textarea rows="2" placeholder="Ex. : une recette, un chaudron, une tasse à mesurer, peler, couper, égoutter, 60 ml, c. à soupe…"></textarea>
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
