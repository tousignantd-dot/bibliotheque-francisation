  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, un courriel écrit. Le jeu de rôle vient en premier parce
  // qu'il sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait le personnage
  // joué par l'assistant vit dans server.py.
  const ROLE_CAS = [
    {id:'commande', titre:'La commande', txt:"Assis, la carte devant toi. Tu ne connais pas les <b>formules</b>, tu hésites entre la table d'hôte et un plat seul — et tu as une <b>allergie</b> à signaler."},
    {id:'repas', titre:'Pendant le repas', txt:"Ton plat est <b>un peu froid</b> et tu hésites à le dire. Tu voudrais aussi du sel et de l'eau."},
    {id:'addition', titre:"L'addition", txt:"Vous êtes deux. <b>Ensemble ou séparé</b> ? Et le pourboire : combien, et est-ce qu'il est déjà sur l'addition ?"},
  ];
  const ROLE_SUJETS = ["Les formules du menu","Ce qu'il y a dans un plat",
    "Une allergie à signaler","Les boissons, et ce qui est gratuit",
    "Signaler ce qui ne va pas","L'addition et les taxes",
    "Le pourboire"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Commande un repas</span></div>
     <p class="lead">L'assistant joue <b>le serveur</b>. Il répond à ce que tu demandes, sans réciter le menu. Il ne parlera pas du pourboire avant que tu ne poses la question.</p>
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
       Commande poliment :
       <span class='savoir-ex'>Je <b>voudrais</b> la table d'hôte, avec la soupe.</span>
       Demande une précision :
       <span class='savoir-ex'>Qu'est-ce qu'il y a <b>dans</b> le plat du jour ?</span>
       Demande quelque chose pendant le repas :
       <span class='savoir-ex'><b>Est-ce que je pourrais avoir</b> un peu de sel ?</span>
       Signale ce qui ne va pas :
       <span class='savoir-ex'><b>Est-ce que ce serait possible de</b> le réchauffer ?</span>
     </div>

     <div class="jr-sep"></div>
     <div class="jr-sub">Choisis ta situation et ton rôle</div>
     <div class="jr-choix">
       <div class="jr-choix-l">Quel moment ?</div>
       <div class="jr-opts" id="jrLogs">
         ${ROLE_CAS.map((c,i)=>`<button class="jr-opt${i===0?' on':''}" type="button" data-log="${c.id}" onclick="jrChoisir('log','${c.id}')">${esc(c.titre)}</button>`).join('')}
       </div>
       <div class="jr-choix-l">Tu joues qui ?</div>
       <div class="jr-opts" id="jrRoles">
         <button class="jr-opt on" type="button" data-role="client" onclick="jrChoisir('role','client')">Le client</button>
         <button class="jr-opt" type="button" data-role="serveur" onclick="jrChoisir('role','serveur')">Le serveur</button>
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
     <h3 class="prod-tit">Raconte un repas au restaurant</h3>
     <p class="prod-lead">Choisis un repas au restaurant : ici, ou dans ton pays. Raconte-le à quelqu'un qui n'y était pas.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Où, avec qui, quelle occasion</div><div class="plan-ex">« C'était un petit restaurant du quartier, avec une collègue. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Ce que tu as commandé</div><div class="plan-ex">« J'ai pris la table d'hôte : la soupe, la truite, et un dessert. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Ce que tu en as pensé</div><div class="plan-ex">« C'était très bon. Le service était rapide. J'y retournerais. »</div></div>
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
     <h3 class="prod-tit">Recommande un restaurant</h3>
     <p class="prod-lead">Quelqu'un cherche un restaurant. Écris-lui pour lui recommander un endroit que tu connais, de 5 à 8 phrases.</p>
     <div class="req">
       <div class="req-hd">Ton message doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le nom et l'endroit</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce qu'on y mange, et une formule</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le prix, à peu près</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un conseil pratique</span></div>
       </div>
       <div class="req-note">Emploie au moins une formule du menu (<em>table d'hôte</em>, <em>menu du jour</em>, <em>à la carte</em>) et une forme polie.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">la personne qui cherche un restaurant</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Un restaurant que je te conseille</span></div>
       <textarea id="peText" rows="7" aria-label="Ton message" data-min="5" data-max="8" oninput="peCount()" placeholder="Bonjour,&#10;Je te conseille un petit restaurant sur la rue…"></textarea>
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
    "Je peux entrer dans un restaurant et répondre aux questions de l'accueil.",
    "Je comprends la différence entre la carte, le menu du jour et la table d'hôte.",
    "Je peux commander poliment : je voudrais, je prendrais.",
    "Je peux demander ce qu'il y a dans un plat, et signaler une allergie.",
    "Je peux demander quelque chose pendant le repas sans me sentir gêné.",
    "Je peux signaler poliment un plat froid ou une erreur de commande.",
    "Je sais calculer le pourboire et je comprends l'addition.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Le menu</div>
     <textarea rows="2" placeholder="Ex. : la carte, le menu du jour, la table d'hôte, à la carte, une entrée, le plat du jour…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Commander poliment</div>
     <textarea rows="2" placeholder="Ex. : je voudrais, je prendrais, pourriez-vous, est-ce que je pourrais avoir…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Pendant le repas</div>
     <textarea rows="2" placeholder="Ex. : une carafe, l'eau du robinet, un accompagnement, excusez-moi, le réchauffer…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">L'addition</div>
     <textarea rows="2" placeholder="Ex. : l'addition, taxes comprises, le pourboire, quinze pour cent, payer séparément…"></textarea>
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
