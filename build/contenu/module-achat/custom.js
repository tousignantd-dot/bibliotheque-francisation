  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, un courriel écrit. Le jeu de rôle vient en premier parce
  // qu'il sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait le personnage
  // joué par l'assistant vit dans server.py.
  const ROLE_CAS = [
    {id:'laveuse', titre:'La laveuse', txt:"Un local de sous-sol d'environ <b>un mètre de large</b>, trois brassées par semaine. Trois modèles alignés, presque identiques."},
    {id:'refrigerateur', titre:'Le réfrigérateur', txt:"Un petit réfrigérateur pour le sous-sol : <b>1,50 m de haut</b>, 60 cm de large, pas plus. Livraison ou transport soi-même ?"},
    {id:'cuisiniere', titre:'La cuisinière', txt:"La tienne est <b>brisée depuis trois jours</b>. Il faut décider vite, mais comprendre ce qu'on paie — et savoir si la prise convient."},
  ];
  const ROLE_SUJETS = ["Les dimensions et l'espace","La capacité et la consommation",
    "La différence entre deux modèles","Ce que couvre la garantie",
    "Le paiement et les taxes","La livraison et l'installation",
    "Le total, avant de décider"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#0F766E">Jeu de rôle</span><span class="ctit" style="color:#0F766E">Informe-toi sur un appareil</span></div>
     <p class="lead">L'assistant joue <b>le vendeur</b>. Il commence par te demander ton espace disponible. Il ne parlera ni de la livraison, ni de l'installation, ni de la garantie prolongée avant que tu ne poses la question.</p>
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
       Décris et compare :
       <span class='savoir-ex'>Une laveuse <b>silencieuse</b> et <b>économe</b> en eau.</span>
       Désigne l'un ou l'autre :
       <span class='savoir-ex'>La différence entre <b>ce</b> modèle-ci et <b>celui</b>-là ?</span>
       Demande une comparaison :
       <span class='savoir-ex'>Cinquante-deux décibels, <b>c'est beaucoup ou peu</b> ?</span>
       Vérifie le total :
       <span class='savoir-ex'>Avec les taxes et la livraison, <b>ça fait combien</b> ?</span>
     </div>

     <div class="jr-sep"></div>
     <div class="jr-sub">Choisis ta situation et ton rôle</div>
     <div class="jr-choix">
       <div class="jr-choix-l">Quel appareil ?</div>
       <div class="jr-opts" id="jrLogs">
         ${ROLE_CAS.map((c,i)=>`<button class="jr-opt${i===0?' on':''}" type="button" data-log="${c.id}" onclick="jrChoisir('log','${c.id}')">${esc(c.titre)}</button>`).join('')}
       </div>
       <div class="jr-choix-l">Tu joues qui ?</div>
       <div class="jr-opts" id="jrRoles">
         <button class="jr-opt on" type="button" data-role="acheteur" onclick="jrChoisir('role','acheteur')">L'acheteur</button>
         <button class="jr-opt" type="button" data-role="vendeur" onclick="jrChoisir('role','vendeur')">Le vendeur</button>
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
     <h3 class="prod-tit">Décris un appareil que tu connais</h3>
     <p class="prod-lead">Choisis un appareil que tu as chez toi : une laveuse, un réfrigérateur, une cuisinière, un four à micro-ondes. Décris-le à quelqu'un qui veut acheter le même.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Ce que c'est, et ses dimensions</div><div class="plan-ex">« C'est une laveuse frontale. Elle fait soixante-huit centimètres de large. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Ce qui la distingue, avec des adjectifs</div><div class="plan-ex">« Elle est silencieuse et économe en eau. C'est un modèle récent. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Ce que tu conseilles</div><div class="plan-ex">« Prends celle-là si ton local est petit. Elle sera livrée en une semaine. »</div></div>
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
     <h3 class="prod-tit">Écris au magasin</h3>
     <p class="prod-lead">Tu as acheté un appareil et quelque chose ne va pas : la livraison, l'installation, une pièce sous garantie. Écris au service à la clientèle, de 5 à 8 phrases.</p>
     <div class="req">
       <div class="req-hd">Ton message doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>L'appareil et la date d'achat</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce qui ne va pas, précisément</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce que tu as déjà vérifié</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce que tu demandes</span></div>
       </div>
       <div class="req-note">Emploie au moins deux adjectifs accordés et une phrase au <em>futur</em> : ce que tu attends du magasin.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">service@magasin.qc.ca</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Problème avec un appareil acheté le…</span></div>
       <textarea id="peText" rows="7" aria-label="Ton message" data-min="5" data-max="8" oninput="peCount()" placeholder="Bonjour,&#10;J'ai acheté une laveuse chez vous le 12 mars. Depuis la livraison,…"></textarea>
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
    "Je peux dire l'espace dont je dispose et demander si l'appareil y entre.",
    "Je peux décrire un appareil avec des adjectifs bien placés et bien accordés.",
    "Je peux désigner un modèle plutôt qu'un autre : ce modèle-ci, celui-là.",
    "Je peux demander ce que couvre la garantie, et ce qu'elle ne couvre pas.",
    "Je comprends ce qui s'ajoute au prix affiché : taxes, livraison, installation.",
    "Je comprends une date de livraison annoncée au futur.",
    "Je peux trouver les quatre pages utiles d'un mode d'emploi.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#166534">Je retiens des mots</span><span class="ctit" style="color:#166534">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#166534" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#166534;font-size:13px;margin:6px 0 4px">L'appareil</div>
     <textarea rows="2" placeholder="Ex. : un électroménager, une laveuse, la capacité, les dimensions, économe, silencieux…"></textarea>
     <div style="font-weight:800;color:#166534;font-size:13px;margin:12px 0 4px">La garantie</div>
     <textarea rows="2" placeholder="Ex. : pièces et main-d'œuvre, un défaut de fabrication, une garantie prolongée, le déplacement…"></textarea>
     <div style="font-weight:800;color:#166534;font-size:13px;margin:12px 0 4px">Payer et se faire livrer</div>
     <textarea rows="2" placeholder="Ex. : les taxes, un versement sans intérêt, la livraison, l'installation, le bon de livraison…"></textarea>
     <div style="font-weight:800;color:#166534;font-size:13px;margin:12px 0 4px">Le mode d'emploi</div>
     <textarea rows="2" placeholder="Ex. : un boulon de transport, être de niveau, un cycle à vide, le tableau des problèmes…"></textarea>
   </div>
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#166534">Autoévaluation</span><span class="ctit" style="color:#166534">Qu'est-ce que je suis capable de faire ?</span></div>
     <p class="lead">Pour chaque énoncé, choisis : pas encore 😟, un peu 🙂, ou oui 😃.</p>
     ${SELF.map((s,i)=>`<div class="selfrow"><div class="self-txt">${s}</div><div class="self-opts">
        <button onclick="rate(${i},this)">😟</button><button onclick="rate(${i},this)">🙂</button><button onclick="rate(${i},this)">😃</button>
     </div></div>`).join('')}
     <div style="margin-top:16px"><button class="btn btn-pri" onclick="finishEval()">Terminer le module 🎉</button></div>
     <div id="evalDone" class="fb" aria-live="polite"></div>
   </div>`;
}
