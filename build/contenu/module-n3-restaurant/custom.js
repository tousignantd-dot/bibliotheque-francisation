  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, une courte commande écrite. Le jeu de rôle vient en premier
  // parce qu'il sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait le personnage
  // joué par l'assistant vit dans server.py.
  const ROLE_CAS = [
    {id:'trio', titre:'Le trio du midi', txt:"Tu as une heure pour dîner. Tu veux un <b>trio</b> : un sandwich, un accompagnement et un breuvage. Tu ne sais pas encore ce qu'il y a dans les sandwichs, ni ce que le trio comprend."},
    {id:'soupe', titre:'La soupe du jour', txt:"Tu veux une <b>soupe</b> et un café. Tu ne sais pas quelle est la soupe du jour, ni quels formats existent. Tu manges sur place."},
    {id:'emporter', titre:'Deux repas pour emporter', txt:"Tu commandes pour toi et pour une camarade, et vous mangez au centre. Il te faut deux repas <b>pour emporter</b>, des ustensiles et des serviettes."},
  ];
  const ROLE_SUJETS = ["Saluer en arrivant au comptoir","Dire ce que tu veux avec « je voudrais »",
    "Demander ce qu'il y a dans un plat","Choisir un format : petit, moyen ou grand",
    "Répondre à « pour ici ou pour emporter ? »","Demander un ustensile ou un condiment",
    "Retenir ton numéro et remercier"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Commande ton repas</span></div>
     <p class="lead">L'assistant joue <b>le préposé du comptoir</b>. Il ne dit rien que tu ne lui demandes pas : ce qu'il y a dans le sandwich, les formats, le prix, tout se demande. À toi de poser tes questions.</p>
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
         <button class="jr-opt on" type="button" data-role="client" onclick="jrChoisir('role','client')">Le client</button>
         <button class="jr-opt" type="button" data-role="prepose" onclick="jrChoisir('role','prepose')">Le préposé</button>
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
         <div><div class="jr-rappel-l">Commande poliment</div><div class="jr-rappel-x"><b>Je voudrais</b> un trio au poulet, s'il vous plaît.</div></div>
         <div><div class="jr-rappel-l">Montre sur le tableau</div><div class="jr-rappel-x"><b>Ce sandwich-là</b>, c'est quoi ?</div></div>
         <div><div class="jr-rappel-l">Choisis un format</div><div class="jr-rappel-x"><b>Petit</b>, s'il vous plaît.</div></div>
         <div><div class="jr-rappel-l">Demande ce qui manque</div><div class="jr-rappel-x">Est-ce que je peux avoir <b>du sel</b> et <b>des serviettes</b> ?</div></div>
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
     <h3 class="prod-tit">Commande ton repas au comptoir</h3>
     <p class="prod-lead">Choisis ce que tu mangerais ce midi. Salue, dis ce que tu veux avec « je voudrais », choisis un format, réponds à « pour ici ou pour emporter ? », puis demande un ustensile ou un condiment.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Dire ce que tu veux</div><div class="plan-ex">« Bonjour. Je voudrais un trio au poulet, s'il vous plaît. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Choisir et répondre</div><div class="plan-ex">« Avec salade, s'il vous plaît. Petit format. Pour ici. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Demander ce qui manque</div><div class="plan-ex">« Est-ce que je peux avoir une cuillère et du sel ? »</div></div>
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
     <h3 class="prod-tit">Écris la commande du groupe</h3>
     <p class="prod-lead">Trois personnes de ta classe t'envoient chercher le dîner. Écris la commande sur un papier, pour ne rien oublier au comptoir : le plat de chacun, le format, le breuvage. De 5 à 8 phrases.</p>
     <div class="req">
       <div class="req-hd">Ta commande doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le plat de chaque personne, avec « au », « à la » ou « aux »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un format pour ce qui en a un : petit, moyen ou grand</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un breuvage par personne</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une ligne pour ce qui manque souvent : ustensiles, serviettes, condiments</span></div>
       </div>
       <div class="req-note">Attention aux petits mots : un sandwich <em>au</em> poulet, une soupe <em>aux</em> légumes, <em>du</em> sel, <em>des</em> serviettes.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">Pour</span><span class="mail-v">Le comptoir de chez Marcel</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Notre commande du midi</span></div>
       <textarea id="peText" rows="7" aria-label="Ta commande" data-min="5" data-max="8" oninput="peCount()" placeholder="Bonjour. Je voudrais trois repas, pour emporter.&#10;Un trio sandwich au poulet, avec salade…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 5 à 8</span>
         <button class="btn-prod" id="peBtn" type="button" onclick="peCheck()">Vérifier ma commande</button>
       </div>
     </div>
     <div class="fb" id="peFb" aria-live="polite"></div>
     <div class="status" id="peStatus">Analyse en cours…</div>
     <div class="err" id="peErr"></div>
   </div>`;
  const rb=document.getElementById('recBtn'); if(rb) rb.addEventListener('click',toggleRec);

  // JE RETIENS DES MOTS — notes + cartes mémoire + autoévaluation
  const SELF=[
    "Je peux nommer les endroits d'un casse-croûte : le comptoir, la caisse, le plateau.",
    "Je trouve un plat, son prix et son format sur le tableau du menu.",
    "Je comprends « servi avec » et je sais ce qu'un trio comprend.",
    "Je peux dire ce qu'il y a dans un plat : au poulet, à la tomate, aux légumes.",
    "Je peux commander poliment avec « je voudrais » et « s'il vous plaît ».",
    "Je peux choisir un format : petit, moyen ou grand.",
    "Je comprends les questions du préposé et je réponds du premier coup.",
    "Je peux demander un ustensile, une serviette ou un condiment.",
    "Je comprends « il n'en reste plus » et je sais quoi répondre.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Le casse-croûte</div>
     <textarea rows="2" placeholder="Ex. : le comptoir, la caisse, le tableau du menu, un plateau, la file, le poste de ramassage…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Le menu et les formats</div>
     <textarea rows="2" placeholder="Ex. : un trio, un accompagnement, un breuvage, une portion, petit, moyen, grand, servi avec…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Commander</div>
     <textarea rows="2" placeholder="Ex. : Je voudrais…, s'il vous plaît, pour ici, pour emporter, débit ou comptant, Ce sera tout ?…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Sur le plateau</div>
     <textarea rows="2" placeholder="Ex. : un ustensile, une cuillère, une serviette de table, un condiment, du sel, du ketchup, un couvercle…"></textarea>
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
