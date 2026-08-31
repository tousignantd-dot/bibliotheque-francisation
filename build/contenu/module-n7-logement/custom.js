  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : la négociation avec l'assistant, l'exposé des deux
  // options, puis la lettre au propriétaire. Le jeu de rôle vient en premier
  // parce qu'il sert de répétition aux deux autres.
  //
  // D'où viennent ces trois tâches. Les deux intentions de la situation
  // « Location ou achat d'un logement », au niveau 7, sont **orales** :
  // négocier entre propriétaire et locataire, s'informer pour acheter une
  // habitation. Le jeu de rôle et la production orale les portent
  // directement. La production **écrite**, elle, vient des attentes de fin
  // de cours du niveau, qui sont productives — « il rédige un texte formel
  // simple », « à l'aide d'un modèle, il rédige une lettre d'affaires
  // courantes », « il organise ses idées à l'aide de paragraphes, entre
  // lesquels il établit des liens au moyen de connecteurs ». C'est écrit ici
  // et dans le manifeste pour que la tâche ne passe pas pour une invention
  // hors programme.
  //
  // Seule la situation publique est ici ; ce que sait le propriétaire joué
  // par l'assistant vit dans server.py, scénario « louerouacheter ».
  const ROLE_CAS = [
    {id:'avis', titre:"L'avis, à discuter", txt:"Vous avez reçu un <b>avis de modification</b> le 12 février : le loyer passerait de <b>940 $ à 1 024 $</b> le 1er juillet, et le stationnement, jusqu'ici compris, coûterait <b>25 $ de plus</b>. Vous avez <b>un mois</b> pour répondre par écrit. Votre propriétaire ne sait pas encore ce que vous en pensez."},
    {id:'fenetre', titre:'La fenêtre de la chambre', txt:"La fenêtre ne ferme plus depuis <b>février</b>. Vous l'avez signalé au téléphone, jamais par écrit — et c'est votre point faible. Les <b>travaux d'entretien</b> sont à la charge du propriétaire ; vous voulez une contrepartie, pas une bataille."},
    {id:'depart', titre:'Le projet qui change tout', txt:"Vous vous informez pour <b>acheter</b> un condo à 275 000 $. Rien n'est décidé. Vous ne voulez ni promettre de rester, ni annoncer un départ que vous ne ferez peut-être pas — et vous avez besoin que le loyer de l'an prochain reste supportable dans les deux cas."},
  ];
  const ROLE_SUJETS = ["Dire de quoi il s'agit avant d'entrer dans les détails",
    "Rappeler le délai d'un mois, sans en faire une menace",
    "Demander au conditionnel : pourriez-vous, accepteriez-vous",
    "Mettre en relief ce qui compte : ce qui me dérange, c'est…",
    "Concéder un argument de l'autre avant de présenter le vôtre",
    "Proposer un montant précis, jamais « c'est trop cher »",
    "Offrir une contrepartie qui ne vous coûte rien",
    "Demander que l'entente soit mise par écrit, avec la date"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Négociez avec votre propriétaire</span></div>
     <p class="lead">L'assistant joue <b>un propriétaire de six logements, ni méchant ni généreux</b>. Ses frais ont vraiment monté, il préfère s'entendre que d'aller au Tribunal, et il n'accorde rien à qui n'offre rien. À vous de discuter le montant sans discuter la personne, et de repartir avec quelque chose d'écrit. Vouvoyez-le du début à la fin.</p>
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
         <button class="jr-opt on" type="button" data-role="sokhna" onclick="jrChoisir('role','sokhna')">La locataire qui a lu son avis</button>
         <button class="jr-opt" type="button" data-role="proprietaire" onclick="jrChoisir('role','proprietaire')">Le propriétaire aux six logements</button>
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
         <div class="jr-bande-t">Les huit sujets à couvrir</div>
         <p class="jr-bande-p">${ROLE_SUJETS.map((s,i)=>i?s.charAt(0).toLowerCase()+s.slice(1):s).join(', ')}.</p>
       </div>
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()">Commencer la discussion</button>
     </div>
     <div class="jr-rappel">
       <div class="jr-rappel-t">Réutilisez ce que vous venez d'apprendre</div>
       <div class="jr-rappel-g">
         <div><div class="jr-rappel-l">Demandez au conditionnel</div><div class="jr-rappel-x"><b>Pourriez-vous</b> m'accorder une semaine ? · Je vous <b>proposerais</b> cinquante-cinq dollars.</div></div>
         <div><div class="jr-rappel-l">Mettez en avant ce qui compte</div><div class="jr-rappel-x"><b>Ce qui</b> me dérange, <b>ce n'est pas</b> que le loyer monte, <b>c'est</b> qu'il monte d'un coup.</div></div>
         <div><div class="jr-rappel-l">Concédez, puis tournez</div><div class="jr-rappel-x"><b>Je comprends que</b> vos taxes ont monté, <b>cela dit</b>…</div></div>
         <div><div class="jr-rappel-l">Posez votre condition au subjonctif</div><div class="jr-rappel-x">J'accepte, <b>à condition que</b> la fenêtre <b>soit</b> regardée en septembre.</div></div>
         <div><div class="jr-rappel-l">Liez vos phrases</div><div class="jr-rappel-x">La fenêtre <b>dont</b> je vous ai parlé en février · le jour <b>où</b> j'ai reçu l'avis</div></div>
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
     <h3 class="prod-tit">Rester locataire ou acheter : exposez les deux, puis décidez</h3>
     <p class="prod-lead">Quelqu'un de votre entourage vous demande où vous en êtes. Exposez-lui les deux options en 90 secondes environ : annoncez-les, donnez pour chacune deux avantages et deux inconvénients avec un chiffre à l'appui, comparez-les, puis dites ce que vous décidez et à quelle condition vous changeriez d'avis.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Les deux options, annoncées</div><div class="plan-ex">« J'ai deux possibilités : rester locataire à 995 $ par mois si mon entente tient, ou acheter un condo de 275 000 $ à Saint-Hyacinthe. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Deux avantages, deux inconvénients, avec des chiffres</div><div class="plan-ex">« En restant, je ne paie rien d'autre et je peux partir avec un avis ; par contre, le loyer peut monter chaque année et rien ne m'appartient. En achetant, une partie du paiement me revient, mais il faut 13 750 $ de mise de fonds et environ 600 $ de plus par mois. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">La comparaison, puis la décision datée</div><div class="plan-ex">« C'est d'autant plus difficile que les deux se défendent. Cette année, je reste locataire ; je reviendrai voir le jour où j'aurai 30 000 $ de côté. »</div></div>
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
           <div class="rec-hint">Parlez environ 90 secondes. Vous pourrez recommencer autant de fois que vous voulez.</div>
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
     <h3 class="prod-tit">Écrivez votre réponse à l'avis de modification</h3>
     <p class="prod-lead">Vous répondez par écrit à l'avis reçu le 12 février. Écrivez un message de 10 à 14 phrases, en <b>trois paragraphes</b> : d'abord ce que vous avez reçu et ce que vous répondez, ensuite les faits et votre contre-proposition chiffrée, enfin ce que vous demandez et sous quelle forme. Un objet qui se comprend sans ouvrir le message.</p>
     <div class="req">
       <div class="req-hd">Votre lettre doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un objet court et précis, sans phrase complète</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une formule d'appel qui nomme la personne, et une salutation fermée</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Trois paragraphes séparés, un par idée, liés par des connecteurs</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>La date de réception de l'avis et le montant proposé</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une concession, puis votre contre-proposition chiffrée</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une demande au conditionnel : « Accepteriez-vous… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une condition au subjonctif : « à condition que… soit… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une phrase emphatique : « Ce qui… , c'est… »</span></div>
       </div>
       <div class="req-note">N'écrivez pas ce que vous pensez de votre propriétaire : écrivez ce que vous avez reçu, ce que vous proposez, et ce que vous attendez de lui. Une réponse qui s'en tient aux faits, aux dates et à un montant est celle qui obtient un écrit en retour — et c'est l'écrit qui compte.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">g.lheureux@immeubles-bourdages.example</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">À vous de le trouver — court, et sans phrase complète</span></div>
       <textarea id="peText" rows="10" aria-label="Votre lettre" data-min="10" data-max="14" oninput="peCount()" placeholder="Monsieur Lheureux,&#10;&#10;J'ai bien reçu le 12 février votre avis de modification des conditions du bail du logement 2…"></textarea>
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
    "Je comprends ce qu'un avis de modification annonce et ce qu'il déclenche.",
    "Je sais que le délai court à partir du jour où j'ai reçu l'avis.",
    "Je sais que ne pas répondre à un avis de hausse équivaut à accepter.",
    "Je sais qu'après un refus, c'est au propriétaire d'aller au Tribunal.",
    "J'entends la différence entre demander, exiger et se renseigner.",
    "Je demande au conditionnel : pourriez-vous, j'aimerais, je proposerais.",
    "Je mets en avant ce qui compte : « ce qui me dérange, c'est… ».",
    "Je concède un argument avant de présenter le mien.",
    "Je propose un montant précis et une contrepartie, jamais une plainte.",
    "Je sais que le courtier du vendeur ne représente pas l'acheteur.",
    "Je pose des questions précises : combien, en quelle année, quel document.",
    "J'emploie lequel, auquel et duquel pour faire choisir dans un ensemble.",
    "Je lie mes phrases avec qui, que, dont et où.",
    "Je reconnais les conditions d'une promesse d'achat et leurs délais.",
    "J'emploie le subjonctif après à condition que, pour que et bien que.",
    "Je compare deux options avec des chiffres, puis je décide et je date ma décision.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Les mots de l'avis</div>
     <textarea rows="2" placeholder="Ex. : un avis de modification, une hausse de loyer, un délai de réponse, la fixation du loyer…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les mots de la négociation</div>
     <textarea rows="2" placeholder="Ex. : une contre-proposition, une contrepartie, un compromis, une entente écrite…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les mots de la visite</div>
     <textarea rows="2" placeholder="Ex. : un courtier immobilier, un contrat de courtage, les frais de copropriété, le fonds de prévoyance…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les mots de l'achat</div>
     <textarea rows="2" placeholder="Ex. : une promesse d'achat, la mise de fonds, une inspection préachat, les droits de mutation…"></textarea>
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
