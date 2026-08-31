  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, le récit du problème
  // au médecin, un courriel pour déplacer un rendez-vous. Le jeu de rôle vient
  // en premier parce qu'il sert de répétition avant les deux autres.
  //
  // Le scénario `rendezvous` a été ajouté à server.py pour ce module : aucun
  // des scénarios existants ne convient à un appel à une clinique, où l'agente
  // n'est pas soignante et ne donne rien sans qu'on le demande. Seule la
  // situation publique est ici — ce que l'agente sait, et ce qu'elle ne dira
  // que si on l'interroge, vit sur le serveur, sinon l'élève lirait les
  // réponses dans la source de la page.
  const ROLE_CAS = [
    {id:'premier', titre:"Le premier rendez-vous", txt:"Vous avez des <b>étourdissements le matin en vous levant</b>, et ça dure <b>depuis trois mois</b>. Vous êtes fatigué tout le temps. Vous appelez votre clinique pour obtenir un rendez-vous avec votre médecin de famille — pas au sans-rendez-vous."},
    {id:'deplacer', titre:"Le rendez-vous qui ne marche plus", txt:"Votre <b>horaire de travail a changé</b> : vous commencez maintenant à sept heures et vous finissez à quinze heures. Votre rendez-vous de suivi est le <b>mardi 8 juillet à onze heures</b>. Vous voulez le garder, mais à un autre moment."},
    {id:'annuler', titre:"L'annulation de dernière minute", txt:"Votre rendez-vous est <b>demain à seize heures trente</b> et votre garçon est malade : vous devez rester avec lui. Vous voulez annuler sans être noté absent, savoir s'il y a des frais, et reprendre un rendez-vous le plus tôt possible."},
  ];
  const ROLE_SUJETS = ["Dire en une seule phrase pourquoi vous appelez",
    "Donner votre nom, l'épeler, et votre numéro de carte d'assurance maladie",
    "Dire ce que vous avez et depuis quand, en deux phrases",
    "Dire quand vous êtes libre, et pourquoi les autres moments ne marchent pas",
    "Demander l'heure d'arrivée et ce qu'il faut apporter",
    "Demander le délai d'annulation",
    "Répéter la date, l'heure et le lieu pour confirmer"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">L'appel à la clinique</span></div>
     <p class="lead">L'assistant joue l'agente administrative. Elle est polie et efficace — et elle ne donne jamais un renseignement avant qu'on le lui demande. Comme au vrai téléphone : ce que vous n'aurez pas demandé, vous ne le saurez pas. Essayez les deux rôles : au niveau 5, il faut savoir <b>demander</b> et savoir <b>renseigner</b>.</p>
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
         <button class="jr-opt on" type="button" data-role="patient" onclick="jrChoisir('role','patient')">La personne qui appelle</button>
         <button class="jr-opt" type="button" data-role="agente" onclick="jrChoisir('role','agente')">L'agente de la clinique</button>
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
         <div class="jr-bande-t">Les sept choses à faire pendant l'appel</div>
         <p class="jr-bande-p">${ROLE_SUJETS.map((s,i)=>i?s.charAt(0).toLowerCase()+s.slice(1):s).join(', ')}.</p>
       </div>
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()">Commencer l'appel</button>
     </div>
     <div class="jr-rappel">
       <div class="jr-rappel-t">Réutilisez ce que vous venez d'apprendre</div>
       <div class="jr-rappel-g">
         <div><div class="jr-rappel-l">Dites depuis quand</div><div class="jr-rappel-x">J'ai des étourdissements <b>depuis trois mois</b>.</div></div>
         <div><div class="jr-rappel-l">Placez le rendez-vous dans le temps</div><div class="jr-rappel-x">Vous avez quelque chose <b>d'ici</b> vendredi ? Je suis libre <b>à partir de</b> seize heures.</div></div>
         <div><div class="jr-rappel-l">Prenez un engagement au futur simple</div><div class="jr-rappel-x">Je <b>serai</b> là quinze minutes avant, et j'<b>apporterai</b> ma carte.</div></div>
         <div><div class="jr-rappel-l">Dites l'obligation</div><div class="jr-rappel-x"><b>Il faut que je sois</b> au travail à sept heures ce jour-là.</div></div>
         <div><div class="jr-rappel-l">Ne répétez pas tout</div><div class="jr-rappel-x">Mon rendez-vous du mardi ? Je voudrais <b>le</b> déplacer. · La clinique, j'<b>y</b> vais en autobus.</div></div>
         <div><div class="jr-rappel-l">Confirmez avant de raccrocher</div><div class="jr-rappel-x">Jeudi 19 juin, dix-sept heures, arriver à seize heures quarante-cinq. <b>C'est bien ça ?</b></div></div>
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
     <h3 class="prod-tit">Raconter votre problème au médecin</h3>
     <p class="prod-lead">Vous êtes assis dans le bureau. Le médecin dit : « Racontez-moi ce qui se passe. » Vous avez une minute — et personne ne vous posera de questions avant que vous ayez fini. Racontez, ne récitez pas une liste.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Dire le problème et depuis quand</div><div class="plan-ex">« J'ai des étourdissements depuis le mois de mars. Ça fait trois mois. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Planter le décor à l'imparfait, et dire à quel moment ça arrive</div><div class="plan-ex">« Je me levais le matin et tout tournait pendant quelques secondes. Ça m'arrive en me levant du lit, et parfois en montant l'escalier. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Raconter ce qui a changé, au passé composé</div><div class="plan-ex">« Au début, c'était une fois par semaine. La semaine dernière, j'ai dû m'asseoir par terre. J'ai arrêté le soccer en avril. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 4</div><div class="plan-t">Poser vos deux questions</div><div class="plan-ex">« J'ai deux questions : est-ce que je dois arrêter de travailler ? Et qu'est-ce que je fais si ça empire ? »</div></div>
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
           <div class="rec-hint">Environ une minute. Écoutez-vous ensuite comme si vous étiez le médecin : est-ce que vous sauriez quand ça a commencé, à quel moment ça arrive, et si ça empire ?</div>
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
     <h3 class="prod-tit">Le courriel pour déplacer un rendez-vous</h3>
     <p class="prod-lead">La ligne est occupée depuis deux jours et votre rendez-vous approche. Écrivez à la clinique pour le faire déplacer. De 6 à 10 phrases, avec « vous ».</p>
     <div class="req">
       <div class="req-hd">Votre courriel doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Votre nom, votre date de naissance et le rendez-vous visé (date, heure, professionnel)</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce que vous demandez, dit clairement : déplacer, et non annuler</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>La raison, en une phrase, à l'imparfait et au passé composé</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Vos disponibilités, avec « à partir de », « avant », « d'ici »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une obligation avec « il faut que » et un engagement au futur simple</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un numéro où vous joindre, et le moment où vous êtes joignable</span></div>
       </div>
       <div class="req-note">Restez factuel et court : <em>« Mon horaire de travail a changé le 1er juillet »</em>, et non <em>« ça fait trois fois que j'essaie de vous appeler, c'est impossible de vous joindre »</em>. Une demande claire se traite plus vite qu'une plainte.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">l'accueil de la Clinique de la Rive</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Demande de déplacement — rendez-vous du 8 juillet, 11 h</span></div>
       <textarea id="peText" rows="9" aria-label="Votre courriel" data-min="6" data-max="10" oninput="peCount()" placeholder="Bonjour,&#10;&#10;Je m'appelle Rachid Benali, né le 4 novembre 1974. J'ai un rendez-vous de suivi avec la docteure Fongang le mardi 8 juillet à onze heures, et je voudrais le déplacer…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 6 à 10</span>
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
    "Je peux dire depuis quand un problème dure, avec « depuis » ou « ça fait… que ».",
    "Je sais quand aller au sans-rendez-vous et quand demander mon médecin de famille.",
    "Je peux téléphoner à une clinique et dire en une phrase pourquoi j'appelle.",
    "Je donne mon nom, je l'épelle, et je donne mon numéro de carte d'assurance maladie.",
    "Je dis mes disponibilités et j'explique pourquoi les autres moments ne marchent pas.",
    "Je note la date, l'heure, l'heure d'arrivée, ce qu'il faut apporter et le délai d'annulation.",
    "Je répète l'essentiel avant de raccrocher pour le confirmer.",
    "Je peux raconter un problème de santé au passé : l'imparfait pour le décor, le passé composé pour ce qui est arrivé.",
    "Je dis à quel moment le malaise arrive, avec un gérondif : « en me levant », « en montant l'escalier ».",
    "Je pose mes questions au médecin avant de sortir du bureau.",
    "Je demande qu'on me redise autrement un mot que je n'ai pas compris.",
    "Je peux déplacer un rendez-vous, l'annuler à temps et laisser un message d'annulation complet.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#B45309">Je retiens des mots</span><span class="ctit" style="color:#B45309">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#B45309" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#B45309;font-size:13px;margin:6px 0 4px">Où s'adresser</div>
     <textarea rows="2" placeholder="Ex. : un GMF, le sans-rendez-vous, Info-Santé, la carte d'assurance maladie, un symptôme…"></textarea>
     <div style="font-weight:800;color:#B45309;font-size:13px;margin:12px 0 4px">Au téléphone</div>
     <textarea rows="2" placeholder="Ex. : une disponibilité, une agente administrative, un rappel automatisé, épeler, c'est bien ça ?…"></textarea>
     <div style="font-weight:800;color:#B45309;font-size:13px;margin:12px 0 4px">Dans le bureau</div>
     <textarea rows="2" placeholder="Ex. : la tension artérielle, une ordonnance, une prise de sang, à jeun, un bilan, un suivi…"></textarea>
     <div style="font-weight:800;color:#B45309;font-size:13px;margin:12px 0 4px">Déplacer ou annuler</div>
     <textarea rows="2" placeholder="Ex. : déplacer, annuler, des frais d'absence, une boîte vocale, un délai de vingt-quatre heures…"></textarea>
   </div>
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#B45309">Autoévaluation</span><span class="ctit" style="color:#B45309">Qu'est-ce que je suis capable de faire ?</span></div>
     <p class="lead">Pour chaque énoncé, choisissez : pas encore 😟, un peu 🙂, ou oui 😃.</p>
     ${SELF.map((s,i)=>`<div class="selfrow"><div class="self-txt">${s}</div><div class="self-opts">
        <button onclick="rate(${i},this)">😟</button><button onclick="rate(${i},this)">🙂</button><button onclick="rate(${i},this)">😃</button>
     </div></div>`).join('')}
     <div style="margin-top:16px"><button class="btn btn-pri" onclick="finishEval()">Terminer le module 🎉</button></div>
     <div id="evalDone" class="fb" aria-live="polite"></div>
   </div>`;
}
