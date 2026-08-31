  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : l'affaire réglée au comptoir avec l'assistant, le
  // message laissé dans la boîte vocale du secrétariat, puis la demande
  // écrite envoyée au conseiller. Le jeu de rôle vient en premier parce
  // qu'il sert de répétition aux deux autres — c'est là que l'élève
  // découvre qu'« il y a un problème avec mon horaire » ne fait rien
  // avancer du tout.
  //
  // Le scénario `ecole` a été ajouté à server.py pour ce module. Aucun
  // scénario existant ne convenait : `inscription` (niveau 2) remplit un
  // formulaire au comptoir et `procedure` (niveau 4) fait expliquer une
  // marche à suivre. Ici, c'est l'élève qui expose une situation qui dure
  // et qui repart avec une échéance. Seule la situation publique est ici ;
  // ce que Jocelyne Paradis a le droit de décider et ce que monsieur
  // Gauthier exige avant de bouger vivent sur le serveur.
  const ROLE_CAS = [
    {id:'absence', titre:"L'absence de trois semaines", txt:"Vous devez vous absenter <b>du 9 au 27 mars inclusivement</b> : un proche est opéré à l'étranger et vous êtes la seule personne qui puisse s'y rendre. Vous voulez garder votre place dans le groupe, savoir quel papier remplir et pour quand, et savoir ce qui arrive à votre allocation de participation. Vous n'aurez la pièce justificative qu'à votre retour."},
    {id:'transfert', titre:"Le passage au groupe du soir", txt:"Vous avez commencé un emploi qui <b>débute à sept heures le matin</b>. Le cours de jour finit à midi et demi : l'horaire ne tient plus. Vous voulez passer au groupe du soir, quatre soirs par semaine, à partir du 20 avril. Vous voulez aussi savoir combien de temps prend un changement de groupe et si vous restez dans le même cours."},
    {id:'attestation', titre:"La preuve pour l'employeur", txt:"Votre employeur exige <b>une preuve écrite que vous suivez bien un cours ici</b>, avec le nombre d'heures par semaine, avant vendredi. Vous ne savez pas si c'est une attestation de fréquentation ou le relevé des apprentissages qu'il vous faut, ni lequel des deux le centre peut imprimer."},
  ];
  const ROLE_SUJETS = ["Se nommer et donner son groupe dès la première phrase",
    "Dire en une phrase ce qu'on vient faire, avant tout détail",
    "Donner les dates avant le motif : à partir du…, jusqu'au… inclusivement",
    "Donner le motif en une seule phrase, sans raconter le détail",
    "Poser au moins deux questions glissées : je voudrais savoir si…, pourriez-vous me dire quand…",
    "Annoncer au futur simple ce qu'on fera : je reviendrai…, je vous apporterai…",
    "Demander le délai de traitement avant de partir",
    "Redire à voix haute ce qu'on doit faire et pour quand, avant de quitter le comptoir",
    "Vouvoyer du début à la fin, et remercier"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Régler votre affaire au comptoir</span></div>
     <p class="lead">L'assistant joue madame Jocelyne Paradis, au secrétariat du Centre d'éducation des adultes des Trois-Ponts. Elle est aimable et pressée : elle a du monde derrière vous. Elle ne devine rien — si vous commencez par une explication, elle vous demandera d'abord votre nom et votre groupe. Elle ne décide pas non plus de tout : ce qui touche à votre horaire ou à votre parcours, elle vous renverra à monsieur Gauthier. Essayez ensuite l'autre interlocuteur : monsieur Rémi Gauthier, le conseiller en formation, qui reçoit à son bureau et qui exige une demande écrite avant de bouger quoi que ce soit.</p>
     <p class="lead">Choisissez votre affaire et qui vous avez en face</p>
     <div class="jr-annonces" id="jrLogs">
       ${ROLE_CAS.map((c,i)=>`<button class="jr-opt jr-tuile${i===0?' on':''}" type="button" data-log="${c.id}" onclick="jrChoisir('log','${c.id}')">
         <span class="jr-band"><span class="jr-band-off">Choix ${i+1}</span><span class="jr-band-on"><svg viewBox="0 0 20 20" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 10.5l4 4 8-9"></path></svg> Votre choix</span></span>
         <span class="jr-tuile-c"><span class="jr-tuile-t">${esc(c.titre)}</span><span class="jr-tuile-d">${c.txt}</span></span>
       </button>`).join('')}
     </div>
     <div class="jr-reglages">
       <div class="jr-carte">
         <div class="jr-champ-l">L'assistant joue qui ?</div>
         <div class="jr-tuiles" id="jrRoles">
         <button class="jr-opt on" type="button" data-role="jocelyne" onclick="jrChoisir('role','jocelyne')">Madame Paradis, au comptoir</button>
         <button class="jr-opt" type="button" data-role="remi" onclick="jrChoisir('role','remi')">Monsieur Gauthier, à son bureau</button>
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
         <div class="jr-bande-t">Les neuf choses à faire avant de quitter le comptoir</div>
         <p class="jr-bande-p">${ROLE_SUJETS.map((s,i)=>i?s.charAt(0).toLowerCase()+s.slice(1):s).join(', ')}.</p>
       </div>
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()">Me présenter au comptoir</button>
     </div>
     <div class="jr-rappel">
       <div class="jr-rappel-t">Réutilisez ce que vous venez d'apprendre</div>
       <div class="jr-rappel-g">
         <div><div class="jr-rappel-l">Glissez vos questions dans une phrase</div><div class="jr-rappel-x">Je voudrais savoir <b>si</b> je garde ma place. · Pourriez-vous me dire <b>quand</b> je dois remettre le formulaire. · Je ne sais pas <b>ce qu'</b>il faut écrire dans la case du motif.</div></div>
         <div><div class="jr-rappel-l">Placez vos dates avec le bon petit mot</div><div class="jr-rappel-x">Je serai absente <b>à partir du</b> 9 mars, <b>jusqu'au</b> 27 <b>inclusivement</b>. · Le formulaire doit être remis <b>d'ici le</b> 6.</div></div>
         <div><div class="jr-rappel-l">Promettez au futur simple</div><div class="jr-rappel-x">Je <b>reviendrai</b> le 30 mars. Je vous <b>apporterai</b> la pièce justificative. Je <b>m'inscrirai</b> au rattrapage.</div></div>
         <div><div class="jr-rappel-l">Expliquez sans vous plaindre, avec le subjonctif</div><div class="jr-rappel-x"><b>Il faut que</b> je travaille le matin. · <b>Pour que</b> le transfert <b>se fasse</b>, que dois-je remplir ?</div></div>
         <div><div class="jr-rappel-l">Mettez devant ce qui compte, une seule fois</div><div class="jr-rappel-x"><b>Ce qui me bloque, c'est</b> l'horaire, pas le cours. · <b>Ce que je demande, c'est</b> un transfert au groupe du soir.</div></div>
         <div><div class="jr-rappel-l">Enchaînez vos raisons</div><div class="jr-rappel-x"><b>Comme</b> j'ai commencé un emploi, mon horaire a changé ; <b>c'est pourquoi</b> je vous demande un changement de groupe. <b>Par contre</b>, je ne pourrai pas commencer avant le 20.</div></div>
       </div>
     </div>

     <div id="jrChat" class="hidden">
       <div class="jr-fil" id="jrFil" aria-live="polite"></div>
       <div class="jr-mic hidden" id="jrMicZone">
         <button id="jrMic" type="button" onclick="jrParler()" aria-label="Parler"><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="3" width="6" height="11" rx="3"></rect><path d="M5.5 11.5a6.5 6.5 0 0013 0M12 18v3"></path></svg></button>
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
     <h3 class="prod-tit">Le message laissé dans la boîte vocale du centre</h3>
     <p class="prod-lead">Il est sept heures du matin et vous ne pouvez pas passer au centre aujourd'hui. Vous appelez le secrétariat : personne ne répond, et la boîte vocale se déclenche. Vous avez une minute, personne ne vous voit, et personne ne pourra vous poser de question. Écrivez d'abord votre message, lisez-le à voix haute, puis enregistrez-le. De quarante-cinq à soixante secondes — cinq morceaux, dans l'ordre.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Qui vous êtes : nom complet, groupe, cours</div><div class="plan-ex">« Bonjour, ici Amelia Dumitrescu, groupe 4, en francisation, cours de niveau 5. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Ce que vous appelez annoncer, en une phrase</div><div class="plan-ex">« Je vous appelle pour vous annoncer une absence prévue de trois semaines. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Les dates, puis le motif en une phrase</div><div class="plan-ex">« Je serai absente à partir du 9 mars, jusqu'au 27 mars inclusivement. Ma mère est opérée à l'étranger et je suis la seule à pouvoir m'y rendre. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 4</div><div class="plan-t">Ce que vous ferez, au futur simple</div><div class="plan-ex">« Je reviendrai en classe le lundi 30 mars et je vous apporterai la pièce justificative dès mon retour. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 5</div><div class="plan-t">Une question glissée, puis un numéro où vous rappeler</div><div class="plan-ex">« Je voudrais savoir si je dois remplir un formulaire avant mon départ. Vous pouvez me rappeler au 819 555-0142. Merci beaucoup, bonne journée. »</div></div>
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
           <div class="rec-hint">De quarante-cinq à soixante secondes. Réécoutez-vous comme si vous étiez la personne du secrétariat, à huit heures, avec onze messages à écouter : savez-vous qui appelle dès la première phrase ? Avez-vous les deux dates ? Savez-vous s'il faut rappeler, et à quel numéro ?</div>
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
     <h3 class="prod-tit">La demande écrite au conseiller</h3>
     <p class="prod-lead">Vous écrivez à monsieur Rémi Gauthier, conseiller en formation scolaire, pour demander un changement à votre dossier : un transfert au groupe du soir, ou une attestation pour votre employeur. Rien ne bouge tant que ce courriel n'est pas envoyé — c'est lui qui entre au dossier, pas la conversation d'hier. De 7 à 10 phrases, avec « vous ».</p>
     <div class="req">
       <div class="req-hd">Votre courriel doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une salutation, votre nom et votre groupe dans la première phrase</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce que vous demandez, dit avant toute explication</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une phrase emphatique : « Ce qui me bloque, c'est… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une raison, introduite par « Comme » en tête de phrase</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une phrase au subjonctif : « il faut que… » ou « pour que… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une date d'effet avec « à partir du », et une question glissée sur le délai</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une formule de fin, votre nom, votre groupe et un numéro de téléphone</span></div>
       </div>
       <div class="req-note">Un conseiller lit quarante courriels par jour et ne se souvient d'aucune conversation. Mettez donc la demande avant l'explication, une seule raison plutôt que trois, et une date : sans date, il devra vous rappeler pour l'obtenir, et vous aurez perdu la semaine.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">r.gauthier@ceatroisponts.example</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Demande de changement — groupe 4, francisation</span></div>
       <textarea id="peText" rows="10" aria-label="Votre courriel" data-min="7" data-max="10" oninput="peCount()" placeholder="Bonjour monsieur Gauthier,&#10;&#10;Je m'appelle… , du groupe 4 en francisation, et je vous écris pour demander…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 7 à 10</span>
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
    "Je sais à qui m'adresser dans un centre : l'enseignante, le secrétariat ou la conseillère.",
    "Je connais les mots du dossier : un avis, un formulaire, une attestation, un relevé.",
    "J'entends la différence entre le son « é » de relevé et le son « è » de conseillère.",
    "Je dis « je voudrais » avec un « è », et non « je voudrai ».",
    "Je me nomme et je donne mon groupe dès la première phrase, au comptoir.",
    "Je donne les dates avant le motif, et le motif en une seule phrase.",
    "Je glisse mes questions dans une phrase : « je voudrais savoir si… ».",
    "Je remplace « est-ce que » par « si », et « qu'est-ce que » par « ce que ».",
    "J'emploie le futur simple pour dire ce que je ferai à mon retour.",
    "Je lis un avis officiel et j'y trouve l'échéance parmi les autres dates.",
    "Je comprends « à partir du », « jusqu'au », « d'ici le », « avant le », « en cas de ».",
    "Je sais à quoi renvoient « ce document », « celui-ci » et « y » dans un avis.",
    "J'emploie le subjonctif après « il faut que », « pour que » et « bien que ».",
    "Je mets en avant ce qui compte : « Ce qui me bloque, c'est… ».",
    "J'enchaîne mes raisons avec « comme », « donc », « c'est pourquoi » et « par contre ».",
    "J'écris une demande complète en sept à dix phrases, avec une date et une question.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Le centre et ses gens</div>
     <textarea rows="2" placeholder="Ex. : le secrétariat, une conseillère, un local, une session, l'accueil, un rendez-vous…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">L'absence et ce qui la justifie</div>
     <textarea rows="2" placeholder="Ex. : une absence, un motif, une pièce justificative, un rattrapage, motivé, annoncer…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">L'avis officiel et ses dates</div>
     <textarea rows="2" placeholder="Ex. : un avis, une échéance, un formulaire, une prolongation, d'ici le, jusqu'au, inclusivement…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Le changement et la preuve</div>
     <textarea rows="2" placeholder="Ex. : un transfert, une attestation, un relevé, un délai, une demande écrite, une copie…"></textarea>
   </div>
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Autoévaluation</span><span class="ctit" style="color:#A5335F">Qu'est-ce que je suis capable de faire ?</span></div>
     <p class="lead">Pour chaque énoncé, choisissez : pas encore 😟, un peu 🙂, ou oui 😃.</p>
     ${SELF.map((s,i)=>`<div class="selfrow"><div class="self-txt">${s}</div><div class="self-opts">
        <button onclick="rate(${i},this)">😟</button><button onclick="rate(${i},this)">🙂</button><button onclick="rate(${i},this)">😃</button>
     </div></div>`).join('')}
     <div style="margin-top:16px"><button class="btn btn-pri" onclick="finishEval()">Terminer le module 🎉</button></div>
     <div id="evalDone" class="fb" aria-live="polite"></div>
   </div>`;
}
