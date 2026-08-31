  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : la demande de congé jouée avec l'assistant, le
  // message d'accueil enregistré, puis le courriel de réponse automatique.
  // Le jeu de rôle vient en premier parce qu'il sert de répétition aux deux
  // autres — c'est là que l'élève découvre qu'on lui demandera deux dates.
  //
  // Le scénario `conge` a été ajouté à server.py pour ce module : aucun des
  // scénarios existants ne convenait. `entrevue` porte l'embauche et non la
  // vie du poste ; tous les autres mettent en scène un service qui répond à
  // la demande d'un client. Ici l'interlocuteur est un supérieur, il
  // n'accorde rien de vive voix, et c'est l'élève qui doit mener la démarche
  // jusqu'à la confirmation écrite. Seule la situation publique est ici — ce
  // que le chef d'équipe sait du calendrier, du délai et de ce qui est payé
  // vit sur le serveur.
  const ROLE_CAS = [
    {id:'vacances', titre:"Déplacer une semaine de vacances", txt:"Vous avez une semaine de vacances déjà inscrite au calendrier <b>en juillet</b>, et vous voulez la déplacer en août : votre sœur arrive de l'étranger le 12 août. Le calendrier de l'équipe est affiché derrière votre chef d'équipe. Vous ne savez pas encore que la semaine du 12 est déjà prise."},
    {id:'famille', titre:"Une convocation à l'école, lundi matin", txt:"L'école de votre fils vous convoque <b>lundi à neuf heures</b>. Vous travaillez ce jour-là de huit heures à seize heures. On est jeudi, il est quatre heures de l'après-midi, et vous croisez votre chef d'équipe dans le corridor."},
    {id:'sansolde', titre:"Quatre jours sans solde en février", txt:"Vous demandez <b>quatre jours sans solde</b> au mois de février, avant d'avoir une année complète dans le poste. Février est le mois le plus occupé de l'année à la coopérative, et vous le savez. Préparez une solution de remplacement avant d'entrer dans le bureau."},
  ];
  const ROLE_SUJETS = ["Dire ce que vous demandez en une phrase, avec les deux dates",
    "Donner la date du retour au travail, pas seulement la durée",
    "Proposer vous-même qui vous remplace, et pour quelle partie de la journée",
    "Demander ce qu'il faut remplir et à qui l'envoyer",
    "Demander le délai à respecter avant la date demandée",
    "Demander ce qui est payé et ce qui ne l'est pas",
    "Ne pas sortir du bureau sans avoir demandé une confirmation écrite"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Demander un congé à son chef d'équipe</span></div>
     <p class="lead">L'assistant joue Ghislain Marcoux, votre chef d'équipe. Il est cordial, mais il ne facilite rien : il ne donne aucun renseignement avant qu'on le lui demande, il veut les deux dates, il veut savoir qui vous remplace, et il n'accorde jamais un congé de vive voix. Essayez les deux rôles — au niveau 5, il faut savoir <b>demander</b> et savoir <b>répondre</b>.</p>
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
         <button class="jr-opt on" type="button" data-role="employe" onclick="jrChoisir('role','employe')">L'employé qui demande</button>
         <button class="jr-opt" type="button" data-role="chef" onclick="jrChoisir('role','chef')">Le chef d'équipe</button>
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
         <div class="jr-bande-t">Les sept choses à obtenir avant de sortir du bureau</div>
         <p class="jr-bande-p">${ROLE_SUJETS.map((s,i)=>i?s.charAt(0).toLowerCase()+s.slice(1):s).join(', ')}.</p>
       </div>
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()">Entrer dans le bureau</button>
     </div>
     <div class="jr-rappel">
       <div class="jr-rappel-t">Réutilisez ce que vous venez d'apprendre</div>
       <div class="jr-rappel-g">
         <div><div class="jr-rappel-l">Annoncez en une phrase, avec les deux dates</div><div class="jr-rappel-x">Je voudrais prendre congé <b>du lundi 19 au vendredi 23 août</b>, et revenir le lundi 26.</div></div>
         <div><div class="jr-rappel-l">Posez vos questions à l'intérieur d'une phrase</div><div class="jr-rappel-x">Je voudrais savoir <b>combien de jours il me reste</b>. · Pourriez-vous me dire <b>quand je recevrai la réponse</b>.</div></div>
         <div><div class="jr-rappel-l">Demandez ce qui est payé</div><div class="jr-rappel-x">J'aimerais savoir <b>si</b> cette journée-là est payée.</div></div>
         <div><div class="jr-rappel-l">Annoncez la suite au futur simple</div><div class="jr-rappel-x">Kevin <b>prendra</b> les appels de l'avant-midi et Amel <b>répondra</b> l'après-midi.</div></div>
         <div><div class="jr-rappel-l">Rapportez ce qu'on vous a dit</div><div class="jr-rappel-x">Sylvie <b>dit que</b> le formulaire doit être signé. · Elle <b>demande si</b> j'ai vérifié au registre.</div></div>
         <div><div class="jr-rappel-l">Réclamez la trace écrite</div><div class="jr-rappel-x">Est-ce que je recevrai une <b>confirmation par courriel</b> ? Dans combien de temps ?</div></div>
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
     <h3 class="prod-tit">Le message d'accueil de votre boîte vocale</h3>
     <p class="prod-lead">Vous enregistrez le message que tout le monde entendra en vous appelant. Vous l'écrivez d'abord, vous le lisez à voix haute, puis vous l'enregistrez. Environ trente secondes — six morceaux, dans l'ordre.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">L'établissement, puis vous</div><div class="plan-ex">« Vous êtes bien à la Coopérative d'aide à domicile de Rosemont. Ici Dorine Kabeya, à l'accueil. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Vous n'êtes pas là — sans dire pourquoi</div><div class="plan-ex">« Je ne suis pas disponible en ce moment. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Les trois choses que vous demandez, à l'impératif</div><div class="plan-ex">« Laissez-moi votre nom, votre numéro de téléphone et la raison de votre appel. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 4</div><div class="plan-t">Le rappel au futur simple, la porte de sortie, la politesse</div><div class="plan-ex">« Je vous rappellerai dans les meilleurs délais. Pour une urgence, faites le poste onze. Merci et bonne journée. »</div></div>
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
           <div class="rec-hint">Environ trente secondes. Écoutez-vous ensuite comme si vous étiez la personne qui appelle : savez-vous à qui vous parlez ? Savez-vous quoi laisser ? Savez-vous où aller si ça presse ?</div>
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
     <h3 class="prod-tit">Le courriel qui répondra à votre place</h3>
     <p class="prod-lead">Vous partez une semaine et vous ne lirez pas vos courriels. Écrivez la réponse automatique que recevra chaque personne qui vous écrira. De 5 à 8 phrases, avec « vous ». Elle doit se lire en dix secondes.</p>
     <div class="req">
       <div class="req-hd">Votre courriel doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une salutation, en une seule ligne</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Les dates de l'absence : le premier jour et le dernier</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Que vous ne lirez pas vos courriels — au futur simple</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une personne à joindre, avec son courriel ou son poste</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>La date du retour, avec le jour de la semaine</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une signature : votre nom et votre fonction</span></div>
       </div>
       <div class="req-note">Écrivez une date de retour, jamais une durée : <em>« Je serai de retour le lundi 26 août »</em>, et non <em>« Je suis absente une semaine »</em>. Une durée oblige le lecteur à calculer, et il calcule à partir du jour où il lit votre message.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">De</span><span class="mail-v">votre adresse au travail (réponse automatique)</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Absence du 19 au 23 août — réponse automatique</span></div>
       <textarea id="peText" rows="9" aria-label="Votre courriel" data-min="5" data-max="8" oninput="peCount()" placeholder="Bonjour,&#10;&#10;Je suis absente du 19 au 23 août…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 5 à 8</span>
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
    "Je comprends qu'à ce poste, ce qui n'est pas écrit n'a pas eu lieu.",
    "Je fais les liaisons obligatoires au téléphone, et je ne les fais pas après « et ».",
    "Je vouvoie au téléphone et par écrit, même les gens que je connais.",
    "Je peux enregistrer un message d'accueil de trente secondes, en six morceaux.",
    "Je donne un ordre à l'impératif et je place le pronom au bon endroit.",
    "Je rapporte au présent ce qu'une personne a dit : « elle dit que », « elle demande si ».",
    "Je peux écouter un message et en tirer une note de six lignes.",
    "J'emploie les abréviations que tout le monde comprend : RDV, tél., app., a.m.",
    "Je trouve dans un mode d'emploi la seule page qui me concerne.",
    "Je peux écrire une marche à suivre dans l'ordre : d'abord, ensuite, puis, enfin.",
    "Je choisis entre l'impératif et l'infinitif de consigne, et je m'y tiens.",
    "Je sais ce que je règle moi-même sur un appareil et ce que j'appelle.",
    "Je peux nommer dans l'ordre les six étapes d'une demande de congé.",
    "Je pose mes questions à l'intérieur d'une phrase : « je voudrais savoir si… ».",
    "J'annonce mon absence au futur simple et je réclame une confirmation écrite.",
    "Je peux écrire un courriel de réponse automatique en cinq lignes.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Le poste, les tâches, les directives</div>
     <textarea rows="2" placeholder="Ex. : l'accueil, une tâche, des directives, le registre des heures, le babillard…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">La boîte vocale et la note</div>
     <textarea rows="2" placeholder="Ex. : une boîte vocale, un message d'accueil, rappeler, une abréviation, RDV, tél.…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Le matériel et son mode d'emploi</div>
     <textarea rows="2" placeholder="Ex. : un photocopieur, un mode d'emploi, le bac à papier, un bourrage, appuyer, insérer…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">La démarche, le congé, l'absence</div>
     <textarea rows="2" placeholder="Ex. : un formulaire, une autorisation d'absence, la paie, une réponse automatique…"></textarea>
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
