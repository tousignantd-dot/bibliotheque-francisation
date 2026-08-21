  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : la conversation de voisinage jouée avec l'assistant,
  // le message laissé sur un répondeur, puis le courriel de nouvelles.
  // Le jeu de rôle vient en premier parce qu'il sert de répétition aux deux
  // autres — c'est là que l'élève découvre qu'un « on verra » ne passe pas.
  //
  // Le scénario `voisinage` a été ajouté à server.py pour ce module. Le
  // scénario `relations` existe déjà, mais il vient du niveau 4 : deux
  // inconnus s'y rencontrent dans une activité de loisir et se racontent
  // leurs semaines, sans rien à demander, à refuser ni à justifier. Ici les
  // deux personnes se connaissent de vue depuis des années, il y a une date,
  // une heure, un plat à apporter — et la conversation n'est réussie que si
  // l'élève dit clairement oui ou non, et pourquoi. Seule la situation
  // publique est ici ; ce que le voisin sait du calendrier, de la pluie et du
  // nombre d'invités vit sur le serveur.
  const ROLE_CAS = [
    {id:'invitation', titre:"L'invitation dans l'escalier", txt:"Votre voisin du rez-de-chaussée vous invite à <b>la fête de la ruelle</b>. Il ne vous a encore rien dit d'autre : ni la date, ni l'heure, ni ce qu'il faut apporter. Vous devez tout demander avant de répondre — puis répondre pour vrai."},
    {id:'refus', titre:"Le souper du vendredi", txt:"Votre voisin vous invite <b>à souper chez lui vendredi</b>, pour vous présenter sa fille qui arrive de Rimouski. Vous travaillez ce vendredi-là jusqu'à vingt et une heures. Vous ne pouvez pas y aller — et vous ne voulez pas fermer la porte."},
    {id:'felicitations', titre:"Devant les boîtes aux lettres", txt:"Vous venez d'apprendre que votre voisine du troisième a obtenu <b>sa citoyenneté canadienne</b> la semaine dernière. Vous la croisez pour la première fois depuis. Elle est discrète : elle ne racontera rien avant qu'on le lui demande."},
  ];
  const ROLE_SUJETS = ["Dire bonjour en nommant la personne : monsieur, madame, et le nom",
    "Demander la date, l'heure et l'endroit avant de répondre quoi que ce soit",
    "Demander ce qu'il faut apporter, et pour combien de personnes",
    "Demander ce qui arrive s'il pleut",
    "Donner un oui ou un non clair — jamais « on verra », jamais « je vais essayer »",
    "Dire pourquoi, en une seule phrase",
    "Si c'est non : proposer soi-même autre chose avant de partir",
    "Devant une bonne nouvelle : féliciter d'abord, poser ses questions ensuite"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Une conversation avec son voisin</span></div>
     <p class="lead">L'assistant joue Réjean Deslauriers, votre voisin du rez-de-chaussée. Il est chaleureux, mais il ne dit rien d'avance : ni la date, ni l'heure, ni ce qu'il faut apporter tant que vous ne le demandez pas. Et il veut une vraie réponse — un « peut-être », il vous le redemandera. Essayez les deux rôles : au niveau 5, il faut savoir <b>inviter</b> et savoir <b>répondre</b>.</p>
     <div class="jr-grid">
       ${ROLE_CAS.map(c=>`
       <div class="jr-log">
         <div class="jr-log-h">${esc(c.titre)}</div>
         <div class="jr-log-a">${c.txt}</div>
       </div>`).join('')}
     </div>
     <div class="jr-sub">Les huit choses à faire avant de remonter chez vous</div>
     <div class="jr-sujets">
       ${ROLE_SUJETS.map(s=>`<div class="jr-sujet"><span class="jr-box"></span>${esc(s)}</div>`).join('')}
     </div>
     <div class="jr-gram">
       <div class="jr-gram-t">Réutilisez ce que vous venez d'apprendre</div>
       Posez vos questions en laissant la voix monter :
       <span class='savoir-ex'>C'est quel jour, le 7 ? · Il faut apporter quelque chose ? · <b>Et s'il pleut ?</b></span>
       Acceptez en trois temps, avec le futur simple :
       <span class='savoir-ex'>C'est oui, avec plaisir. Merci de m'avoir invitée : j'<b>apporterai</b> un plat pour six.</span>
       Refusez en quatre temps :
       <span class='savoir-ex'>Merci beaucoup de l'invitation. Malheureusement, je ne pourrai pas venir, <b>parce que</b> je travaille ce jour-là. On se reprend cet été ?</span>
       Mettez la raison en tête quand elle explique tout :
       <span class='savoir-ex'><b>Comme</b> je travaille de midi à minuit, je ne pourrai pas être là.</span>
       Félicitez avant de poser vos questions :
       <span class='savoir-ex'><b>Quelle</b> bonne nouvelle ! Félicitations ! <b>Comme</b> je suis contente pour vous.</span>
       Racontez au passé, avec un décor :
       <span class='savoir-ex'>Samedi, j'<b>ai apporté</b> des empanadas. Il y <b>avait</b> vingt-deux personnes dans la ruelle.</span>
     </div>

     <div class="jr-sep"></div>
     <div class="jr-sub">Choisissez votre situation et votre rôle</div>
     <div class="jr-choix">
       <div class="jr-choix-l">Quelle situation ?</div>
       <div class="jr-opts" id="jrLogs">
         ${ROLE_CAS.map((c,i)=>`<button class="jr-opt${i===0?' on':''}" type="button" data-log="${c.id}" onclick="jrChoisir('log','${c.id}')">${esc(c.titre)}</button>`).join('')}
       </div>
       <div class="jr-choix-l">Vous jouez qui ?</div>
       <div class="jr-opts" id="jrRoles">
         <button class="jr-opt on" type="button" data-role="invitee" onclick="jrChoisir('role','invitee')">La personne invitée</button>
         <button class="jr-opt" type="button" data-role="organisateur" onclick="jrChoisir('role','organisateur')">Le voisin qui invite</button>
       </div>
       <div class="jr-choix-l">Comment ?</div>
       <div class="jr-opts" id="jrModes">
         <button class="jr-opt on" type="button" data-mode="texte" onclick="jrModeVoix(false)">✍️ Écrire</button>
         <button class="jr-opt" type="button" data-mode="voix" onclick="jrModeVoix(true)">🎤 Parler</button>
       </div>
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()" style="margin-top:14px">Descendre dans l'escalier</button>
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
     <h3 class="prod-tit">Le message que vous laissez sur son répondeur</h3>
     <p class="prod-lead">Votre voisine du troisième ne répond jamais : elle travaille de nuit. Vous lui laissez un message pour l'inviter à la fête de la ruelle et pour lui donner de vos nouvelles. Écrivez-le d'abord, lisez-le à voix haute, puis enregistrez-le. De trente à quarante-cinq secondes — cinq morceaux, dans l'ordre.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Qui vous êtes, et d'où — dès la première phrase</div><div class="plan-ex">« Bonjour madame Faye, c'est Marisol Vergara, votre voisine du deuxième. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Pourquoi vous appelez, en une phrase</div><div class="plan-ex">« Je vous appelle au sujet de la fête de la ruelle. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Les faits : la date, l'heure, l'endroit, ce qu'il faut apporter — lentement</div><div class="plan-ex">« C'est le samedi 7 juin, de midi à quatre heures, dans la ruelle. Chacun apporte un plat à partager et sa chaise. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 4</div><div class="plan-t">Une nouvelle de vous, au passé</div><div class="plan-ex">« J'ai changé d'horaire au mois de mars : je finis à trois heures maintenant. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 5</div><div class="plan-t">Ce que vous attendez, comment et quand vous joindre, la politesse</div><div class="plan-ex">« Rappelez-moi au 514 555-0112, après quatre heures. Merci, et bonne soirée. »</div></div>
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
           <div class="rec-hint">De trente à quarante-cinq secondes. Réécoutez-vous comme si vous étiez la voisine, réveillée à trois heures de l'après-midi : savez-vous qui parle ? Pouvez-vous noter la date sans faire répéter ? Avez-vous un numéro pour rappeler, et une heure ?</div>
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
     <h3 class="prod-tit">Le courriel qui donne de vos nouvelles</h3>
     <p class="prod-lead">Vous écrivez à une personne de votre cours de français que vous n'avez pas vue depuis des mois. Vous lui racontez la fête de la ruelle, vous la félicitez pour une bonne nouvelle qu'elle vous a annoncée, et vous lui demandez des nouvelles à votre tour. De 6 à 9 phrases, avec « tu ».</p>
     <div class="req">
       <div class="req-hd">Votre courriel doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une salutation, en une seule ligne</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Deux phrases au passé composé : ce qui est arrivé</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une phrase à l'imparfait : comment c'était, qui était là</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une félicitation avec « quel », « quelle » ou « comme »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une phrase au futur simple : ce que vous ferez cet été</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une question ouverte, et une signature</span></div>
       </div>
       <div class="req-note">Une nouvelle se raconte avec un décor : <em>« Il y avait vingt-deux personnes dans la ruelle »</em> en dit plus long que <em>« C'était le fun »</em>. Un événement, un décor, un détail — et votre lecteur voit la scène.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">une personne de votre cours de français</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Des nouvelles de la ruelle</span></div>
       <textarea id="peText" rows="9" aria-label="Votre courriel" data-min="6" data-max="9" oninput="peCount()" placeholder="Bonjour Amina,&#10;&#10;J'espère que tout va bien de ton côté. Samedi, je suis allée à la fête de la ruelle…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 6 à 9</span>
         <button class="btn-prod" id="peBtn" type="button" onclick="peCheck()">Vérifier mon courriel</button>
       </div>
     </div>
     <div class="fb" id="peFb" aria-live="polite"></div>
     <div class="status" id="peStatus">Analyse en cours…</div>
     <div class="err" id="peErr"></div>
   </div>`;
  const rb=document.getElementById('recBtn'); if(rb) rb.addEventListener('click',toggleRec);

  // JE RETIENS DES MOTS — notes + cartes mémoire + autoévaluation
  const SELF=[
    "Je connais les mots de l'immeuble : la ruelle, le hangar, le balcon d'en arrière, le bac brun.",
    "J'entends si la voix monte ou descend, et je sais si on me pose une question.",
    "Je vouvoie mes voisins, et je sais comment le tutoiement s'installe.",
    "Je sais ce qui se demande à un voisin et ce qui ne se demande pas.",
    "Je pose les cinq questions avant de répondre à une invitation : quand, où, quelle heure, quoi apporter, et s'il pleut.",
    "J'accepte une invitation en trois temps : le oui, le merci, ce que je ferai.",
    "Je refuse en quatre temps : merci, refus, raison, contre-proposition.",
    "Je donne ma raison avec « parce que », « comme », « puisque » ou « donc », à la bonne place.",
    "J'emploie le futur simple pour promettre : j'apporterai, je serai là, je vous répondrai.",
    "Je peux enregistrer le message d'accueil de mon répondeur sans donner mon adresse.",
    "Je peux laisser un message de quarante-cinq secondes qui donne tout ce qu'il faut pour me rappeler.",
    "Je remplace ce qui se répète par « le », « lui », « y » ou « en ».",
    "Je peux transformer un message entendu en un mot que quelqu'un d'autre comprendra.",
    "Je rapporte ce qu'on m'a dit : « elle dit que », « elle demande si », « elle demande de ».",
    "Je raconte au passé composé ce qui est arrivé, et à l'imparfait ce qui était là.",
    "Je félicite avec « quelle bonne nouvelle ! » avant de poser mes questions.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#1D6B8F">Je retiens des mots</span><span class="ctit" style="color:#1D6B8F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#1D6B8F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:6px 0 4px">L'immeuble, la ruelle, le voisinage</div>
     <textarea rows="2" placeholder="Ex. : une ruelle verte, un hangar, une corvée, le bac brun, le balcon d'en arrière…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">L'invitation et la réponse</div>
     <textarea rows="2" placeholder="Ex. : une invitation, un plat à partager, reporter, un empêchement, avec plaisir…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">Le répondeur, le message, le mot</div>
     <textarea rows="2" placeholder="Ex. : un répondeur, laisser un message, un mot, prévenir, arroser, rappeler après…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">Les nouvelles et les félicitations</div>
     <textarea rows="2" placeholder="Ex. : des félicitations, la citoyenneté, une cérémonie, fêter, quelle bonne nouvelle…"></textarea>
   </div>
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#1D6B8F">Autoévaluation</span><span class="ctit" style="color:#1D6B8F">Qu'est-ce que je suis capable de faire ?</span></div>
     <p class="lead">Pour chaque énoncé, choisissez : pas encore 😟, un peu 🙂, ou oui 😃.</p>
     ${SELF.map((s,i)=>`<div class="selfrow"><div class="self-txt">${s}</div><div class="self-opts">
        <button onclick="rate(${i},this)">😟</button><button onclick="rate(${i},this)">🙂</button><button onclick="rate(${i},this)">😃</button>
     </div></div>`).join('')}
     <div style="margin-top:16px"><button class="btn btn-pri" onclick="finishEval()">Terminer le module 🎉</button></div>
     <div id="evalDone" class="fb" aria-live="polite"></div>
   </div>`;
}
