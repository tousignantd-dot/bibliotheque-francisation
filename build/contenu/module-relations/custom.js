  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, une carte corrigée. Le jeu de rôle vient en premier parce
  // qu'il sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait le personnage
  // joué par l'assistant vit dans server.py.
  const ROLE_CAS = [
    {id:'volleyball', titre:'Le volleyball du jeudi', txt:"La ligue du <b>centre communautaire</b>, le jeudi soir, avant l'entraînement. Les gens arrivent au vestiaire un à un. Quelqu'un s'est inscrit cette semaine."},
    {id:'cuisine', titre:'La cuisine collective', txt:"Un <b>samedi matin</b>. Six personnes préparent ensemble des plats à rapporter chez elles. C'est la première fois que l'une d'elles y participe."},
    {id:'marche', titre:'La marche du dimanche', txt:"Le groupe part à <b>neuf heures</b> et marche une heure et demie dans le parc. Quelqu'un s'est joint au groupe ce matin pour la première fois."},
  ];
  const ROLE_SUJETS = ["Ce que tu fais de tes semaines","Ton horaire de travail",
    "Depuis quand tu viens ici","Qui t'a amené la première fois",
    "Une expérience du passé","Ce que ça a changé pour toi",
    "Une prochaine occasion de se revoir"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Fais connaissance avec quelqu'un</span></div>
     <p class="lead">L'assistant joue <b>l'autre personne</b>. Il ne connaît pas ta vie et il ne racontera pas la sienne avant que tu poses des questions — comme dans une vraie rencontre. Ton but : <b>apprendre trois choses</b> sur l'autre et <b>raconter une chose</b> sur toi.</p>
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
       Colle deux phrases ensemble :
       <span class='savoir-ex'>C'est une collègue <b>qui</b> m'a parlé du centre.</span>
       <span class='savoir-ex'>Le gymnase <b>où</b> on joue est au sous-sol.</span>
       Raconte au passé :
       <span class='savoir-ex'>Je <b>portais</b> des sandales quand je <b>suis arrivée</b>.</span>
       Dis à qui tu dois quelque chose :
       <span class='savoir-ex'><b>Grâce à</b> ma voisine, j'ai aimé l'hiver.</span>
     </div>

     <div class="jr-sep"></div>
     <div class="jr-sub">Choisis ta situation et ton rôle</div>
     <div class="jr-choix">
       <div class="jr-choix-l">Quelle activité ?</div>
       <div class="jr-opts" id="jrLogs">
         ${ROLE_CAS.map((c,i)=>`<button class="jr-opt${i===0?' on':''}" type="button" data-log="${c.id}" onclick="jrChoisir('log','${c.id}')">${esc(c.titre)}</button>`).join('')}
       </div>
       <div class="jr-choix-l">Tu joues qui ?</div>
       <div class="jr-opts" id="jrRoles">
         <button class="jr-opt on" type="button" data-role="nouveau" onclick="jrChoisir('role','nouveau')">La personne qui arrive</button>
         <button class="jr-opt" type="button" data-role="membre" onclick="jrChoisir('role','membre')">La personne qui accueille</button>
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
     <h3 class="prod-tit">Raconte une expérience qui t'a marqué</h3>
     <p class="prod-lead">Choisis un moment de ta vie : une arrivée, un déménagement, un voyage, un mariage, une naissance. Raconte-le comme tu le raconterais à une personne rencontrée à une activité.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Le décor, à l'imparfait</div><div class="plan-ex">« C'était en janvier. Il faisait trente degrés chez moi et je portais des sandales. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Ce qui est arrivé, au passé composé</div><div class="plan-ex">« Je suis arrivée le douze janvier. J'ai eu mal aux oreilles en sortant. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Ce que ça a changé</div><div class="plan-ex">« Grâce à une voisine, j'ai compris qu'on pouvait aimer l'hiver. »</div></div>
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
     <h3 class="prod-tit">La carte que tu envoies</h3>
     <p class="prod-lead">Choisis : une <b>carte postale</b> à quelqu'un qui est loin, ou une <b>carte de vœux</b> pour une naissance, un mariage ou la nouvelle année. Écris de 5 à 8 phrases.</p>
     <div class="req">
       <div class="req-hd">Ta carte doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une salutation</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Où tu es, ou l'occasion</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce que tu as fait, ou ce que tu souhaites</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une fin et ta signature</span></div>
       </div>
       <div class="req-note">Emploie au moins une fois <em>qui</em>, <em>que</em> ou <em>où</em>, et un verbe au <em>passé composé</em>.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">la personne de ton choix</span></div>
       <div class="mail-row"><span class="mail-k">Occasion</span><span class="mail-v">Carte postale d'un voyage · ou carte de vœux</span></div>
       <textarea id="peText" rows="7" aria-label="Ta carte" data-min="5" data-max="8" oninput="peCount()" placeholder="Bonjour Fatou,&#10;Je t'écris de Québec. Il neige depuis hier et…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 5 à 8</span>
         <button class="btn-prod" id="peBtn" type="button" onclick="peCheck()">Vérifier ma carte</button>
       </div>
     </div>
     <div class="fb" id="peFb" aria-live="polite"></div>
     <div class="status" id="peStatus">Analyse en cours…</div>
     <div class="err" id="peErr"></div>
   </div>`;
  const rb=document.getElementById('recBtn'); if(rb) rb.addEventListener('click',toggleRec);

  // JE RETIENS DES MOTS — notes + cartes mémoire + autoévaluation
  const SELF=[
    "Je peux parler de mes journées : mon horaire, mon travail, le ménage, les repas.",
    "Je peux poser des questions à quelqu'un sur ses activités et ses loisirs.",
    "Je peux coller deux phrases ensemble avec qui, que et où.",
    "Je peux raconter une expérience du passé : le décor à l'imparfait, les évènements au passé composé.",
    "Je peux remplacer un lieu par y ou par là sans le répéter.",
    "Je comprends un message où quelqu'un me donne des nouvelles.",
    "Je peux écrire une carte postale et une carte de vœux avec la bonne formule.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Ma journée et ma semaine</div>
     <textarea rows="2" placeholder="Ex. : se lever, un quart de travail, une brassée, la balayeuse, le bac de recyclage, sortir les ordures…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Mes loisirs et le sport</div>
     <textarea rows="2" placeholder="Ex. : s'entraîner, disputer un match, marquer, battre, une coéquipière, un tournoi, le covoiturage…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les évènements de la vie</div>
     <textarea rows="2" placeholder="Ex. : une naissance, un mariage, un déménagement, un voyage, une arrivée…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Pour donner des nouvelles</div>
     <textarea rows="2" placeholder="Ex. : je t'écris de… · félicitations · meilleurs vœux · beaucoup de bonheur · tu me manques…"></textarea>
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
