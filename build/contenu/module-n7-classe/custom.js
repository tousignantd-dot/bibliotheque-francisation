  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : animer une rencontre avec l'assistant, l'exposé
  // devant la classe, puis la lettre au camarade absent. Le jeu de rôle vient
  // en premier parce qu'il sert de répétition aux deux autres.
  //
  // D'où viennent ces tâches. Contrairement à beaucoup de situations du
  // niveau 7, celle-ci est productive : sur ses cinq intentions, trois le
  // sont. « Faire un exposé sur un sujet concret » donne la production orale ;
  // « rédiger une lettre personnelle destinée à un camarade de classe » donne
  // la production écrite, mot pour mot ; et « résumer un texte relié à son
  // champ d'intérêt » a été travaillé au défi 2, parce qu'il est l'outil de la
  // lettre et non sa concurrence. Le jeu de rôle prolonge l'attente de fin de
  // cours « il présente un projet, une évaluation sommaire ou un problème à
  // des collègues ».
  //
  // Seule la situation publique est côté client ; ce que sait la personne
  // jouée par l'assistant vit dans server.py, scénario « equipe ».
  const ROLE_CAS = [
    {id:'desaccord', titre:"Le désaccord sur la méthode", txt:"Votre coéquipier veut <b>compter les arbres</b> de deux rues samedi matin. Un autre membre de l'équipe trouve que ce chiffre ne mesure pas ce que vous cherchez. Vous animez : personne n'a tort, et il faut sortir de la rencontre avec une méthode que les deux accepteront."},
    {id:'part', titre:"La part qui n'a pas été faite", txt:"Votre coéquipier devait <b>lire la fiche de la ville</b> et en tirer cinq renseignements pour ce soir. Il arrive les mains vides, et la remise est dans huit jours. Vous animez : il faut que le travail se fasse, et il faut aussi qu'il reste dans l'équipe."},
    {id:'silence', titre:"Celui qui ne dit rien", txt:"Depuis trois rencontres, un membre de l'équipe <b>ne dit presque rien</b>. Il fait ce qu'on lui demande, jamais plus. Vous animez : vous voulez son avis sur la méthode, et vous ne voulez pas le mettre mal à l'aise devant les autres."},
  ];
  const ROLE_SUJETS = ["Ouvrir la rencontre : rappeler la question et le temps dont vous disposez",
    "Donner la parole à votre coéquipier en le nommant",
    "Faire préciser : une question factuelle, jamais un jugement",
    "Reformuler sa position jusqu'à ce qu'il s'y reconnaisse",
    "Accorder un point avec « bien que » ou « même si », puis maintenir le vôtre",
    "Mettre en relief ce qui compte : « ce qu'on cherche, c'est… »",
    "Fermer sur des décisions, avec un nom et une date pour chacune"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Animez la rencontre</span></div>
     <p class="lead">L'assistant joue <b>votre coéquipier</b>. Il a ses raisons, il ne les donne pas toutes du premier coup, et il n'aime pas beaucoup se faire dire qu'il a tort. Il répond bien aux questions précises et aux reformulations — beaucoup moins aux reproches.</p>
     <p class="lead">Choisissez votre situation et votre rôle</p>
     <div class="jr-annonces" id="jrLogs">
       ${ROLE_CAS.map((c,i)=>`<button class="jr-opt jr-tuile${i===0?' on':''}" type="button" data-log="${c.id}" onclick="jrChoisir('log','${c.id}')">
         <span class="jr-band"><span class="jr-band-off">Choix ${i+1}</span><span class="jr-band-on"><svg viewBox="0 0 20 20" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 10.5l4 4 8-9"></path></svg> Votre choix</span></span>
         <span class="jr-tuile-c"><span class="jr-tuile-t">${esc(c.titre)}</span><span class="jr-tuile-d">${c.txt}</span></span>
       </button>`).join('')}
     </div>
     <div class="jr-reglages">
       <div class="jr-carte">
         <div class="jr-champ-l">Vous jouez qui ?</div>
         <div class="jr-tuiles" id="jrRoles">
         <button class="jr-opt on" type="button" data-role="animateur" onclick="jrChoisir('role','animateur')">La personne qui anime</button>
         <button class="jr-opt" type="button" data-role="coequipier" onclick="jrChoisir('role','coequipier')">Le coéquipier</button>
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
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()">Commencer la rencontre</button>
     </div>
     <div class="jr-rappel">
       <div class="jr-rappel-t">Réutilisez ce que vous venez d'apprendre</div>
       <div class="jr-rappel-g">
         <div><div class="jr-rappel-l">Demandez poliment</div><div class="jr-rappel-x"><b>Pourrais-tu</b> préciser ce que tu comptes, exactement ?</div></div>
         <div><div class="jr-rappel-l">Reformulez pour faire confirmer</div><div class="jr-rappel-x"><b>Autrement dit</b>, tu préfères une donnée à nous plutôt qu'un chiffre repris ailleurs.</div></div>
         <div><div class="jr-rappel-l">Accordez, puis maintenez</div><div class="jr-rappel-x"><b>Bien que</b> ta méthode <b>soit</b> plus rapide, elle ne mesure pas ce qu'on cherche.</div></div>
         <div><div class="jr-rappel-l">Mettez en relief</div><div class="jr-rappel-x"><b>Ce qu'</b>on cherche, <b>c'est</b> une différence entre deux rues.</div></div>
         <div><div class="jr-rappel-l">Changez de point</div><div class="jr-rappel-x"><b>Quant au</b> partage des rues, on décidera samedi matin.</div></div>
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
     <h3 class="prod-tit">Présentez votre sujet devant la classe</h3>
     <p class="prod-lead">Trois ou quatre minutes, debout, sans lire vos notes mot à mot. Choisissez un sujet concret que vous avez cherché — celui de l'équipe de Neusa ou le vôtre. Annoncez votre plan, présentez ce que vous avez trouvé, rapportez ce que les autres ont dit, puis concluez. Vous vouvoyez votre auditoire.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Annoncez où vous allez, en une phrase</div><div class="plan-ex">« Avant de commencer, je vous dis où je m'en vais : d'abord ce que nous cherchions, ensuite ce que nous avons trouvé, et enfin ce qui nous a surpris. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Ce que vous avez trouvé, avec vos sources</div><div class="plan-ex">« La canopée serait de dix-sept pour cent, selon la fiche de la ville. Quant à notre secteur, il serait sous les dix pour cent. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Ce que l'équipe a dit, rapporté au passé</div><div class="plan-ex">« Un coéquipier a proposé de compter les arbres ; un autre a répondu que ce chiffre ne mesurait pas la bonne chose. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 4</div><div class="plan-t">Concluez en mettant en relief l'essentiel</div><div class="plan-ex">« En somme, ce qui compte, ce n'est pas le nombre d'arbres : c'est la surface que leurs cimes couvrent. »</div></div>
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
           <div class="rec-hint">Parlez trois ou quatre minutes. Vous pourrez recommencer autant de fois que vous voulez.</div>
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
     <h3 class="prod-tit">Écrivez au camarade qui n'était pas là</h3>
     <p class="prod-lead">De 10 à 14 phrases. Ce n'est pas une lettre officielle : vous écrivez à quelqu'un de votre classe, que vous tutoyez. Mais il doit pouvoir travailler dès demain sans appeler personne. Dites qui était là et combien de temps, rapportez ce que chacun a proposé, nommez le désaccord et la façon dont il s'est réglé, donnez les décisions, puis demandez-lui ce que vous attendez de lui.</p>
     <div class="req">
       <div class="req-hd">Votre lettre doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le cadre : le jour, les heures, qui était présent</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Deux positions rapportées, chacune avec le nom de qui l'a portée</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Quatre verbes au discours indirect passé : a dit que, a proposé que…</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un « le lendemain » ou un « ce jour-là » à la place de « demain »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le désaccord, nommé, et la façon dont il s'est réglé</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une concession : « bien que… soit… » ou « même si… est… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une mise en relief : « ce qu'on a décidé, c'est… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Deux engagements avec un nom et une date, et une demande à l'absent</span></div>
       </div>
       <div class="req-note">Une page, jamais deux. Et envoyez-la le soir même : une décision qu'on apprend trois jours plus tard n'est plus une décision, c'est une nouvelle.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">Un camarade de votre équipe, absent à la dernière rencontre</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Ce qu'on a décidé mardi soir — et ce qu'on attend de toi</span></div>
       <textarea id="peText" rows="12" aria-label="Votre lettre" data-min="10" data-max="14" oninput="peCount()" placeholder="Salut,&#10;&#10;On s'est vus mardi de 19 h à…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 10 à 14</span>
         <button class="btn-prod" id="peBtn" type="button" onclick="peCheck()">Vérifier mon texte</button>
       </div>
     </div>
     <div class="fb" id="peFb" aria-live="polite"></div>
     <div class="status" id="peStatus">Analyse en cours…</div>
     <div class="err" id="peErr"></div>
   </div>`;
  const rb=document.getElementById('recBtn'); if(rb) rb.addEventListener('click',toggleRec);

  // JE RETIENS DES MOTS — notes + cartes mémoire + autoévaluation
  const SELF=[
    "Je nomme les rôles d'une équipe : animer, prendre les notes, surveiller le temps, tenir les sources.",
    "Je sais ce qu'on attend d'une personne qui anime, et que ce n'est pas de parler le plus.",
    "Je reconnais le parler familier et la langue standard, et je choisis selon la situation.",
    "Je garde ou je laisse tomber le petit « e » selon sa place dans le mot.",
    "Je repère les connecteurs qui annoncent le plan d'un exposé et ceux qui changent de sujet.",
    "J'entends le conditionnel qui signale un chiffre non confirmé.",
    "Je sépare un fait d'une estimation quand je prends des notes.",
    "Je pose une question précise à une personne invitée en classe.",
    "Je lis une fiche d'information par ses titres, sans la lire au complet.",
    "Je garde dans mon résumé ce qui répond à ma question, et je jette le reste.",
    "Je remplace un morceau de phrase par un nom : la plantation, l'arrosage, la perte.",
    "Je reprends une même idée sans répéter le même mot.",
    "J'emploie « autrement dit », « quant à » et « en somme » à la bonne place.",
    "J'ouvre une rencontre en rappelant la question et le temps qui reste.",
    "Je reformule la position de quelqu'un jusqu'à ce qu'il s'y reconnaisse.",
    "J'accorde un point avec « bien que » ou « même si », puis je maintiens le mien.",
    "Je mets en relief ce qui compte : « c'est… qui », « ce qu'on cherche, c'est… ».",
    "Je rapporte au passé ce que les autres ont dit, avec la bonne concordance.",
    "Je peux faire un exposé de trois ou quatre minutes devant la classe.",
    "Je peux écrire un compte rendu d'une page à un camarade absent.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#0D7A6F">Je retiens des mots</span><span class="ctit" style="color:#0D7A6F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#0D7A6F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#0D7A6F;font-size:13px;margin:6px 0 4px">Le travail d'équipe</div>
     <textarea rows="2" placeholder="Ex. : un mandat, la répartition des rôles, un échéancier, animer une rencontre, un tour de parole…"></textarea>
     <div style="font-weight:800;color:#0D7A6F;font-size:13px;margin:12px 0 4px">Écouter et chercher</div>
     <textarea rows="2" placeholder="Ex. : une personne-ressource, la prise de notes, une estimation, une source fiable, la question de départ…"></textarea>
     <div style="font-weight:800;color:#0D7A6F;font-size:13px;margin:12px 0 4px">Le sujet de recherche</div>
     <textarea rows="2" placeholder="Ex. : un îlot de chaleur, la canopée, l'évapotranspiration, un arbre de rue, une surface minéralisée…"></textarea>
     <div style="font-weight:800;color:#0D7A6F;font-size:13px;margin:12px 0 4px">Rendre compte</div>
     <textarea rows="2" placeholder="Ex. : un résumé, un compte rendu, un désaccord, un consensus, une décision, un engagement…"></textarea>
   </div>
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#0D7A6F">Autoévaluation</span><span class="ctit" style="color:#0D7A6F">Qu'est-ce que je suis capable de faire ?</span></div>
     <p class="lead">Pour chaque énoncé, choisissez : pas encore 😟, un peu 🙂, ou oui 😃.</p>
     ${SELF.map((s,i)=>`<div class="selfrow"><div class="self-txt">${s}</div><div class="self-opts">
        <button onclick="rate(${i},this)">😟</button><button onclick="rate(${i},this)">🙂</button><button onclick="rate(${i},this)">😃</button>
     </div></div>`).join('')}
     <div style="margin-top:16px"><button class="btn btn-pri" onclick="finishEval()">Terminer le module 🎉</button></div>
     <div id="evalDone" class="fb" aria-live="polite"></div>
   </div>`;
}
