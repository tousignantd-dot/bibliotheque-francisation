  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, un message dans une
  // boîte vocale, un courriel de relance. Le jeu de rôle vient en premier
  // parce qu'il sert de répétition avant les deux autres.
  //
  // Le scénario `services` a été ajouté à server.py pour ce module : aucun
  // des douze scénarios existants ne convient à un appel à un service public.
  // Seule la situation publique est ici — ce que le préposé sait et ne dira
  // que si on le lui demande vit sur le serveur, sinon l'élève lirait les
  // réponses dans la source de la page.
  const ROLE_CAS = [
    {id:'bac', titre:"Le bac qui n'est plus ramassé", txt:"Votre <b>bac brun</b> n'a pas été vidé depuis deux semaines. Vous ne savez pas si c'est le jour de collecte qui a changé, ou si le camion vous a oubliés. Vous voulez comprendre <b>et</b> faire vider le bac."},
    {id:'ecocentre', titre:"Le vieux réfrigérateur", txt:"Vous devez vous débarrasser d'un <b>vieux réfrigérateur</b> et de deux pots de peinture. Vous ne savez pas si l'écocentre les accepte, ce qu'il faut apporter comme preuve, ni si c'est payant."},
    {id:'carte', titre:"La demande restée bloquée", txt:"Votre demande de <b>carte de citoyenne</b> s'est bloquée en ligne à la dernière page. Vous voulez savoir s'il faut recommencer, si vous pouvez la faire par téléphone, ou s'il faut vous déplacer."},
  ];
  const ROLE_SUJETS = ["Dire pourquoi vous appelez, en une seule phrase",
    "Donner votre adresse et votre code postal, en épelant au besoin",
    "Poser au moins trois questions précises",
    "Demander le délai, en jours ouvrables",
    "Demander qu'on ouvre une requête",
    "Noter le numéro de requête et le répéter",
    "Demander ce qu'il faut apporter ou préparer"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">L'appel au service</span></div>
     <p class="lead">L'assistant joue le préposé. Il est poli, il connaît son affaire — et il ne donne jamais un renseignement avant qu'on le lui demande. Comme au vrai téléphone : ce que vous n'aurez pas demandé, vous ne le saurez pas. Essayez les deux rôles : au niveau 5, il faut savoir <b>demander</b> et savoir <b>renseigner</b>.</p>
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
         <button class="jr-opt on" type="button" data-role="citoyen" onclick="jrChoisir('role','citoyen')">La personne qui appelle</button>
         <button class="jr-opt" type="button" data-role="prepose" onclick="jrChoisir('role','prepose')">Le préposé du service</button>
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
         <div><div class="jr-rappel-l">Demandez sans questionner</div><div class="jr-rappel-x"><b>Pouvez-vous me dire</b> quand le camion passe dans ma rue ?</div></div>
         <div><div class="jr-rappel-l">Posez une question fermée avec « si »</div><div class="jr-rappel-x">Je <b>voudrais savoir si</b> le bac sera vidé cette semaine.</div></div>
         <div><div class="jr-rappel-l">Demandez ce qu'il faut</div><div class="jr-rappel-x">Pouvez-vous me dire <b>ce qu'</b>il faut apporter ?</div></div>
         <div><div class="jr-rappel-l">Employez le mot juste</div><div class="jr-rappel-x">Est-ce que vous ouvrez une <b>requête</b> ? Quel est le <b>délai</b> ?</div></div>
         <div><div class="jr-rappel-l">Faites répéter sans gêne</div><div class="jr-rappel-x">Un instant, je prends une feuille. <b>Pouvez-vous répéter plus lentement ?</b></div></div>
         <div><div class="jr-rappel-l">Confirmez avant de raccrocher</div><div class="jr-rappel-x">24-118-7690, trois jours ouvrables. <b>C'est bien ça ?</b></div></div>
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
     <h3 class="prod-tit">Le message dans la boîte vocale</h3>
     <p class="prod-lead">Vous rappelez le service, et cette fois personne ne répond : vous tombez sur la boîte vocale. Laissez un message complet en une minute. Vous n'aurez pas de deuxième chance — on ne rappelle pas quelqu'un pour lui faire répéter son numéro.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Se nommer et donner son numéro de requête</div><div class="plan-ex">« Bonjour, ici Leïla Haddad, au sujet de la requête 24-118-7690. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Rappeler la situation en deux phrases</div><div class="plan-ex">« J'ai appelé mardi dernier parce que mon bac brun n'était pas ramassé. On m'avait annoncé un délai de trois jours ouvrables. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Dire clairement ce que vous attendez</div><div class="plan-ex">« Je voudrais savoir si la requête est toujours ouverte, et quand le ramassage est prévu. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 4</div><div class="plan-t">Laisser un numéro et un moment pour vous joindre</div><div class="plan-ex">« Vous pouvez me rappeler au 514 555-0182, de préférence l'après-midi. Je répète : 514 555-0182. Merci beaucoup. »</div></div>
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
           <div class="rec-hint">Environ une minute. Écoutez-vous ensuite comme si vous étiez le préposé : est-ce que vous auriez pu rappeler cette personne ?</div>
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
     <h3 class="prod-tit">Le courriel de relance</h3>
     <p class="prod-lead">Une semaine a passé et rien n'est arrivé. Écrivez au service pour relancer votre demande. De 6 à 10 phrases, avec « vous ».</p>
     <div class="req">
       <div class="req-hd">Votre courriel doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Votre numéro de requête et la date de votre appel</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le rappel de la situation au passé composé et à l'imparfait</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le délai qu'on vous avait annoncé</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Deux demandes en subordonnée : « Je voudrais savoir si… », « Pouvez-vous me dire… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce que vous ferez si rien ne bouge, et vos coordonnées</span></div>
       </div>
       <div class="req-note">Restez factuel : <em>« Le bac n'a toujours pas été vidé »</em>, et non <em>« Ça fait trois fois que je vous écris, c'est inadmissible »</em>. Un courriel qui accuse se traite moins vite qu'un courriel qui informe.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">le service à la clientèle de la Ville</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Requête 24-118-7690 — collecte non effectuée, suivi</span></div>
       <textarea id="peText" rows="9" aria-label="Votre courriel" data-min="6" data-max="10" oninput="peCount()" placeholder="Bonjour,&#10;&#10;Je vous écris au sujet de la requête 24-118-7690, ouverte le mardi 12 mai. J'avais appelé parce que mon bac brun n'était pas ramassé…"></textarea>
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
    "Je peux lire une brochure de ma ville et comprendre ce qu'elle me demande de faire.",
    "Je sais ce qui va dans chaque bac, et ce qui s'apporte à l'écocentre.",
    "Je peux téléphoner à un service public et dire en une phrase pourquoi j'appelle.",
    "Je peux donner mon adresse et l'épeler si on ne me comprend pas.",
    "Je pose mes questions avec « Pouvez-vous me dire… » et « Je voudrais savoir si… ».",
    "Je note un numéro de requête et je le répète pour le confirmer.",
    "Je comprends la différence entre trois jours et trois jours ouvrables.",
    "Je peux lire une page de service public et trouver l'encadré qui compte.",
    "Je comprends les mots d'un formulaire : champ obligatoire, pièce justificative, le cas échéant.",
    "Je peux me présenter à un guichet et raconter ce que j'ai déjà essayé.",
    "Je comprends ce qui manque à mon dossier et ce qu'il faut que j'apporte.",
    "Je peux écrire à un service public pour relancer une demande.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">La brochure et les collectes</div>
     <textarea rows="2" placeholder="Ex. : les matières résiduelles, le bac brun, l'écocentre, Info-collectes, une preuve de résidence…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Au téléphone</div>
     <textarea rows="2" placeholder="Ex. : un préposé, une requête, un délai, un jour ouvrable, épeler, pouvez-vous répéter ?…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Devant l'écran</div>
     <textarea rows="2" placeholder="Ex. : un formulaire, un champ obligatoire, une pièce justificative, téléverser, le cas échéant, en vigueur…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Au guichet</div>
     <textarea rows="2" placeholder="Ex. : un billet de file d'attente, un comptoir, une pièce d'identité, il manque…, il faut que…"></textarea>
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
