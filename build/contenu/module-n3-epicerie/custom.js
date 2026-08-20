  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, une liste d'épicerie écrite. Le jeu de rôle vient en premier
  // parce qu'il sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait le personnage
  // joué par l'assistant vit dans server.py.
  const ROLE_CAS = [
    {id:'farine', titre:"La farine de maïs", txt:"Tu cherches un produit de <b>ton pays</b>. Il n'est pas avec les autres farines, et tu ne sais pas dans quelle allée regarder."},
    {id:'special', titre:"Le spécial de la semaine", txt:"La circulaire annonce le poulet à <b>trois dollars la livre</b>. Tu veux vérifier le prix et savoir jusqu'à quand le spécial dure."},
    {id:'entretien', titre:"Le produit d'entretien", txt:"Tu cherches un produit pour le <b>plancher</b>. Tu veux savoir où il est — et s'il est dangereux."},
  ];
  const ROLE_SUJETS = ["Attirer l'attention poliment","Dire ce que tu cherches",
    "Comprendre le numéro d'allée","Faire répéter si tu n'as pas compris",
    "Demander le prix ou le format","Vérifier avant de repartir",
    "Remercier"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Trouve ton produit</span></div>
     <p class="lead">L'assistant joue <b>le commis de l'épicerie</b>. Il répond vite, comme dans la vraie vie : à toi de faire répéter si tu n'as pas compris le numéro d'allée.</p>
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
       Attire l'attention, puis demande :
       <span class='savoir-ex'><b>Excusez-moi</b>, je cherche la farine de maïs.</span>
       Fais répéter le chiffre :
       <span class='savoir-ex'>Pardon, allée <b>cinq</b> ou allée <b>quinze</b> ?</span>
       Demande une quantité :
       <span class='savoir-ex'>Un <b>sac de</b> riz, le grand format.</span>
       Vérifie le prix :
       <span class='savoir-ex'>C'est bien <b>trois dollars la livre</b> ?</span>
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
         <button class="jr-opt" type="button" data-role="commis" onclick="jrChoisir('role','commis')">Le commis</button>
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
     <h3 class="prod-tit">Demande où se trouve un produit</h3>
     <p class="prod-lead">Choisis un produit que tu achètes souvent. Demande à un commis où il se trouve, puis informe-toi sur son format ou sur son prix.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Attirer l'attention et demander</div><div class="plan-ex">« Excusez-moi, je cherche de la farine de maïs. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Faire répéter et vérifier</div><div class="plan-ex">« Pardon, allée cinq ou allée quinze ? »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">S'informer sur le format ou le prix</div><div class="plan-ex">« Vous l'avez en grand format ? C'est combien ? »</div></div>
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
     <h3 class="prod-tit">Écris ta liste d'épicerie</h3>
     <p class="prod-lead">Écris la liste de ce que tu dois acheter cette semaine, avec les quantités. De 5 à 8 phrases.</p>
     <div class="req">
       <div class="req-hd">Ta liste doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Au moins six produits différents</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une quantité pour chacun</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un produit en spécial cette semaine</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un produit d'entretien</span></div>
       </div>
       <div class="req-note">Emploie un mot de quantité et « de » : <em>un paquet de</em>, <em>une boîte de</em>, <em>un kilo de</em>, <em>une bouteille d'</em>.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">Liste</span><span class="mail-v">Épicerie de la semaine</span></div>
       <div class="mail-row"><span class="mail-k">Budget</span><span class="mail-v">environ 40 $</span></div>
       <textarea id="peText" rows="7" aria-label="Ta liste" data-min="5" data-max="8" oninput="peCount()" placeholder="J'ai besoin d'un sac de riz de deux kilos.&#10;Je prends un paquet de pâtes…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 5 à 8</span>
         <button class="btn-prod" id="peBtn" type="button" onclick="peCheck()">Vérifier ma liste</button>
       </div>
     </div>
     <div class="fb" id="peFb" aria-live="polite"></div>
     <div class="status" id="peStatus">Analyse en cours…</div>
     <div class="err" id="peErr"></div>
   </div>`;
  const rb=document.getElementById('recBtn'); if(rb) rb.addEventListener('click',toggleRec);

  // JE RETIENS DES MOTS — notes + cartes mémoire + autoévaluation
  const SELF=[
    "Je peux demander où se trouve un produit dans un magasin.",
    "Je comprends une réponse qui donne un numéro d'allée.",
    "Je peux faire répéter quand je n'ai pas compris un chiffre.",
    "Je fais la différence entre treize et trente, quinze et cinquante.",
    "Je peux dire une quantité : un paquet de, un kilo de, une bouteille d'.",
    "Je peux lire une circulaire et comprendre un spécial.",
    "Je reconnais les dessins de mise en garde sur un produit d'entretien.",
    "Je peux répondre aux questions de la caisse et vérifier ma facture.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Dans le magasin</div>
     <textarea rows="2" placeholder="Ex. : une allée, une affichette, une tablette, un panier, un dépanneur…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Demander et comprendre</div>
     <textarea rows="2" placeholder="Ex. : excusez-moi, je cherche…, pardon ?, plus lentement, au fond, à côté de…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Choisir</div>
     <textarea rows="2" placeholder="Ex. : la circulaire, un spécial, une livre, un kilo, un paquet de, une mise en garde…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">À la caisse</div>
     <textarea rows="2" placeholder="Ex. : la carte de points, un sac réutilisable, débit ou crédit, le sous-total, la facture…"></textarea>
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
