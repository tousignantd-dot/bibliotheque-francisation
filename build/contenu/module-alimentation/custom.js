  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, un courriel écrit. Le jeu de rôle vient en premier parce
  // qu'il sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait le personnage
  // joué par l'assistant vit dans server.py.
  const ROLE_CAS = [
    {id:'boucherie', titre:'La boucherie', txt:"Du <b>poulet pour quatre personnes</b> et du bœuf haché pour un plat. Tu ne sais pas combien de poids représentent quatre poitrines."},
    {id:'poisson', titre:'Le comptoir du poisson', txt:"Du <b>poisson frais</b>, mais tu ne le cuisineras pas ce soir. Truite ou saumon ? Et combien de temps ça se garde ?"},
    {id:'charcuterie', titre:'La charcuterie', txt:"Du <b>jambon tranché</b> pour les sandwichs de la semaine. Deux jambons, deux prix — et une douzaine de tranches à obtenir."},
  ];
  const ROLE_SUJETS = ["Le produit et sa sorte","La quantité, avec son unité",
    "La provenance","Combien de temps ça se garde",
    "Comment le conserver","Le prix, avant de repartir",
    "Une demande particulière"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Commande à un comptoir</span></div>
     <p class="lead">L'assistant joue <b>la personne au comptoir</b>. Elle demande ce que tu veux, puis la quantité — une chose à la fois. Elle ne dit pas d'où vient le produit ni combien de temps il se garde : c'est à toi de le demander.</p>
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
       Demande une quantité qu'on ne compte pas :
       <span class='savoir-ex'>Je voudrais <b>du</b> poulet et <b>de la</b> truite.</span>
       Ne répète pas le produit :
       <span class='savoir-ex'>J'<b>en</b> veux quatre. · J'<b>en</b> prends une livre.</span>
       Informe-toi sur la conservation :
       <span class='savoir-ex'>Ça <b>se garde</b> combien de temps ?</span>
       Vérifie le prix :
       <span class='savoir-ex'>Ça fait combien, <b>en tout</b> ?</span>
     </div>

     <div class="jr-sep"></div>
     <div class="jr-sub">Choisis ta situation et ton rôle</div>
     <div class="jr-choix">
       <div class="jr-choix-l">Quel comptoir ?</div>
       <div class="jr-opts" id="jrLogs">
         ${ROLE_CAS.map((c,i)=>`<button class="jr-opt${i===0?' on':''}" type="button" data-log="${c.id}" onclick="jrChoisir('log','${c.id}')">${esc(c.titre)}</button>`).join('')}
       </div>
       <div class="jr-choix-l">Tu joues qui ?</div>
       <div class="jr-opts" id="jrRoles">
         <button class="jr-opt on" type="button" data-role="client" onclick="jrChoisir('role','client')">Le client</button>
         <button class="jr-opt" type="button" data-role="commis" onclick="jrChoisir('role','commis')">La personne au comptoir</button>
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
     <h3 class="prod-tit">Explique un plat que tu sais préparer</h3>
     <p class="prod-lead">Choisis un plat que tu prépares souvent. Explique à quelqu'un ce qu'il faut acheter, en quelle quantité, et comment le préparer.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Ce qu'il faut acheter</div><div class="plan-ex">« Il faut du bœuf haché, des oignons et de la pâte de tomate. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Les quantités</div><div class="plan-ex">« Une livre de bœuf haché, deux oignons, une boîte de pâte de tomate. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">La préparation, et la conservation</div><div class="plan-ex">« Ça se cuisine en trente minutes. Ça se garde trois jours au frigo. »</div></div>
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
     <p class="prod-lead">Quelqu'un fait ton épicerie à ta place cette semaine. Écris-lui la liste en phrases complètes, avec les quantités et deux précisions — de 5 à 8 phrases.</p>
     <div class="req">
       <div class="req-hd">Ton message doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Au moins six produits</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une quantité pour chacun</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Deux précisions : sorte, coupe, format</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce qu'il ne faut PAS prendre</span></div>
       </div>
       <div class="req-note">Emploie <em>du</em>, <em>de la</em> et <em>des</em> au moins une fois chacun, et une phrase négative avec <em>pas de</em>.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">la personne qui fait ton épicerie</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Ma liste d'épicerie de la semaine</span></div>
       <textarea id="peText" rows="7" aria-label="Ton message" data-min="5" data-max="8" oninput="peCount()" placeholder="Bonjour,&#10;Il me faudrait du poulet — quatre poitrines — et de la…"></textarea>
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
    "Je peux trouver un produit dans un magasin, et demander quand je ne trouve pas.",
    "Je peux dire ce que je veux avec du, de la, des — et pas de à la forme négative.",
    "Je peux commander à un comptoir en donnant une quantité avec la bonne unité.",
    "Je peux employer « en » sans répéter le nom du produit.",
    "Je peux demander comment un aliment se garde et se prépare.",
    "Je peux lire les trois lignes qui comptent sur une étiquette.",
    "Je peux suivre un mode d'emploi de produit d'entretien sans me tromper de dose.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Dans le magasin</div>
     <textarea rows="2" placeholder="Ex. : une allée, une conserve, un comptoir, une étiquette, la provenance…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Commander et mesurer</div>
     <textarea rows="2" placeholder="Ex. : une livre, deux cents grammes, tranché mince, du bœuf haché, une poitrine…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Garder les aliments</div>
     <textarea rows="2" placeholder="Ex. : ça se garde deux jours, emballer, congeler, le bas du réfrigérateur…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Lire une étiquette</div>
     <textarea rows="2" placeholder="Ex. : la valeur nutritive, la portion, le sodium, meilleur avant, diluer, un avertissement…"></textarea>
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
