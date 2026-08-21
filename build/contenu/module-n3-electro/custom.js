  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, un court message de livraison écrit. Le jeu de rôle vient en
  // premier parce qu'il sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait le personnage
  // joué par l'assistant vit dans server.py.
  const ROLE_CAS = [
    {id:'laveuse', titre:'La laveuse de la circulaire', txt:"Ta laveuse est <b>brisée</b>. Tu as la circulaire dans la main : la Norlac LT 4200 est à 849 $ jusqu'à dimanche. Tu veux la voir, connaître sa largeur et la faire livrer."},
    {id:'microondes', titre:'Le micro-ondes du deuxième rayon', txt:"Tu cherches un <b>micro-ondes</b> pour une petite cuisine. Tu ne sais pas où il est dans le magasin, ni s'il entre entre le mur et le réfrigérateur."},
    {id:'livraison', titre:'Le camion de samedi', txt:"Tu as <b>payé</b> ton appareil. Il reste à demander la livraison : un jour, une heure, ton adresse — et savoir si le magasin emporte le vieux."},
  ];
  const ROLE_SUJETS = ["Saluer en entrant","Dire quel appareil tu cherches",
    "Demander où est le rayon","Montrer l'appareil et demander le prix",
    "Demander le format ou la couleur","Demander la livraison et un jour",
    "Remercier avant de partir"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Achète ton appareil</span></div>
     <p class="lead">L'assistant joue <b>le vendeur du magasin</b>. Il ne dit rien que tu ne lui demandes pas : le prix, le format, la livraison, tout se demande. À toi de poser tes questions.</p>
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
       Trouve le rayon :
       <span class='savoir-ex'><b>Où est</b> le rayon des laveuses ?</span>
       Montre l'appareil :
       <span class='savoir-ex'><b>Cette laveuse-là</b>, elle coûte combien ?</span>
       Demande le format :
       <span class='savoir-ex'>Elle fait <b>combien de large</b> ?</span>
       Conclus :
       <span class='savoir-ex'><b>Je la prends.</b> Vous pouvez la livrer samedi ?</span>
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
     <h3 class="prod-tit">Demande un appareil et fais-le livrer</h3>
     <p class="prod-lead">Choisis un appareil dont tu aurais besoin chez toi. Demande où est le rayon, demande le prix et le format, puis demande la livraison en donnant un jour.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Dire ce que tu cherches</div><div class="plan-ex">« Bonjour, où est le rayon des laveuses ? »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Demander le prix et le format</div><div class="plan-ex">« Cette laveuse-là coûte combien ? Elle fait combien de large ? »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Conclure et faire livrer</div><div class="plan-ex">« Je la prends. Vous pouvez la livrer samedi ? »</div></div>
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
     <h3 class="prod-tit">Écris ta demande de livraison</h3>
     <p class="prod-lead">Le magasin demande de confirmer la livraison par écrit. Écris un court message : ce que tu as acheté, le jour qui te convient, ton adresse. De 5 à 8 phrases.</p>
     <div class="req">
       <div class="req-hd">Ton message doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le nom de l'appareil et sa marque</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le jour et le moment qui te conviennent</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ton adresse et ton numéro de téléphone</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une phrase au futur proche : « Je vais être là… »</span></div>
       </div>
       <div class="req-note">Attention aux dates : on écrit <em>le 8 novembre</em>, jamais « novembre 8 », et les noms de jours ne prennent pas de majuscule.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">Comptoir de la livraison</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Ma livraison</span></div>
       <textarea id="peText" rows="7" aria-label="Ton message" data-min="5" data-max="8" oninput="peCount()" placeholder="Bonjour. J'ai acheté une laveuse Norlac hier.&#10;Je voudrais la livraison samedi…"></textarea>
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
    "Je peux nommer les appareils de la maison : laveuse, sécheuse, réfrigérateur, micro-ondes.",
    "Je trouve le prix, le prix régulier et les dates dans une circulaire.",
    "Je peux lire et écrire un prix de trois ou quatre chiffres.",
    "Je comprends « du mardi au dimanche » et « quantité limitée ».",
    "Je peux demander où est le rayon d'un appareil.",
    "Je peux montrer un appareil et demander son prix et son format.",
    "Je peux dire « je le prends » ou « je la prends » au vendeur.",
    "Je peux demander la livraison, donner un jour et garder mon bon.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Les appareils</div>
     <textarea rows="2" placeholder="Ex. : une laveuse, une sécheuse, un réfrigérateur, une cuisinière, un micro-ondes, un aspirateur…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">La circulaire et les prix</div>
     <textarea rows="2" placeholder="Ex. : la circulaire, un spécial, le prix régulier, la marque, quantité limitée, du mardi au dimanche…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Dans le magasin</div>
     <textarea rows="2" placeholder="Ex. : le rayon, une affichette, le modèle, vingt-sept pouces de large, Où est… ? C'est combien ?…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Payer et faire livrer</div>
     <textarea rows="2" placeholder="Ex. : la caisse, débit, comptant, la livraison, un bon de livraison, samedi matin, en sus…"></textarea>
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
