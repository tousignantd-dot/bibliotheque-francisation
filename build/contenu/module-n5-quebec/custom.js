  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : la demande de renseignements jouée avec l'assistant,
  // le message de réservation laissé sur la boîte vocale d'un gîte, puis le
  // courriel qui invite quelqu'un à venir. Le jeu de rôle vient en premier
  // parce qu'il sert de répétition aux deux autres — c'est là que l'élève
  // découvre qu'une demande dite d'un seul tenant reçoit une seule réponse,
  // et qu'une demande en morceaux en reçoit six.
  //
  // Le scénario `regions` a été ajouté à server.py pour ce module. Aucun des
  // treize scénarios existants ne convenait : `chemin` et `autobus` se jouent
  // dans une ville et font demander son chemin ; `titre` se joue devant un
  // guichet de transport urbain, pour un trajet du jour même ; `circulation`,
  // du module voisin de niveau 5, fait expliquer une entrave à quelqu'un qui
  // n'a rien entendu. Ici, l'élève prépare un séjour d'une semaine à cinq
  // cents kilomètres de chez lui : il y a des dates, une région, des bagages
  // et un hébergement. Seule la situation publique est ici ; ce que le
  // préposé sait de son horaire et ce que l'hôtesse du gîte connaît de sa
  // région vivent sur le serveur.
  const ROLE_CAS = [
    {id:'depart', titre:"Réserver l'aller-retour", txt:"Vous êtes au comptoir de la <b>Gare d'autocars de Montréal</b>, rue Berri. Vous voulez aller passer une semaine dans une région du Québec : vous savez laquelle, vous savez à peu près quand, et vous n'avez encore rien réservé. Il y a trois personnes derrière vous."},
    {id:'retour', titre:"Changer la date du retour", txt:"Vous êtes en région depuis quatre jours et vous voudriez <b>rester deux jours de plus</b>. Votre billet de retour est daté de dimanche. Vous téléphonez pour savoir si c'est possible, ce que ça coûte, et s'il reste de la place."},
    {id:'region', titre:"Se renseigner sur la région", txt:"Vous êtes arrivé hier soir et vous avez <b>six jours devant vous</b>, sans auto. Vous voulez savoir ce qu'il y a à voir, ce qui est encore ouvert à cette date-ci, comment s'y rendre à pied ou en autobus, et ce qu'il ne faut surtout pas manquer."},
  ];
  const ROLE_SUJETS = ["Dire où vous allez, avec la région : à Rimouski, dans le Bas-Saint-Laurent",
    "Dire les dates, avec le jour de la semaine et le chiffre : le lundi 28 septembre",
    "Dire combien de temps vous restez, et combien vous êtes de personnes",
    "Poser vos questions poliment : Pourriez-vous me dire… · Je voudrais savoir si…",
    "Demander la durée du trajet et s'il y a une correspondance",
    "Demander ce que vous pouvez apporter comme bagages",
    "Comparer deux possibilités, puis dire laquelle vous prenez et pourquoi",
    "Redire à la fin ce que vous avez retenu, pour vérifier que vous avez compris la même chose"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Préparer son voyage de vive voix</span></div>
     <p class="lead">L'assistant joue Serge Ouellet, préposé au comptoir des autocars. Il connaît son horaire par cœur, il est aimable et il est pressé : si vous ne dites pas où, quand et combien de personnes, il vous le demandera — trois fois. Essayez ensuite l'autre rôle : Rose-Aimée Bélanger, qui tient un gîte au bord du fleuve et qui connaît sa région mieux que n'importe quel site Internet.</p>
     <p class="lead">Choisissez votre situation et qui vous avez en face</p>
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
         <button class="jr-opt on" type="button" data-role="prepose" onclick="jrChoisir('role','prepose')">Le préposé, au comptoir</button>
         <button class="jr-opt" type="button" data-role="habitante" onclick="jrChoisir('role','habitante')">L'hôtesse du gîte, en région</button>
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
         <div class="jr-bande-t">Les huit choses à dire avant de repartir du comptoir</div>
         <p class="jr-bande-p">${ROLE_SUJETS.map((s,i)=>i?s.charAt(0).toLowerCase()+s.slice(1):s).join(', ')}.</p>
       </div>
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()">Prendre son tour au comptoir</button>
     </div>
     <div class="jr-rappel">
       <div class="jr-rappel-t">Réutilisez ce que vous venez d'apprendre</div>
       <div class="jr-rappel-g">
         <div><div class="jr-rappel-l">Dites le lieu avec la bonne préposition</div><div class="jr-rappel-x">Je vais <b>à</b> Rimouski, <b>au</b> Bas-Saint-Laurent. · Ma sœur habite <b>en</b> Gaspésie. · On skie <b>dans les</b> Laurentides.</div></div>
         <div><div class="jr-rappel-l">Posez vos questions poliment</div><div class="jr-rappel-x"><b>Pourriez-vous me dire</b> combien de temps ça prend ? · <b>Je voudrais savoir s'</b>il faut changer d'autocar.</div></div>
         <div><div class="jr-rappel-l">Dites le temps avec le mot juste</div><div class="jr-rappel-x">On fait le trajet <b>en</b> huit heures. Je pars <b>pour</b> une semaine. Le départ est <b>à</b> sept heures, on arrive <b>vers</b> trois heures.</div></div>
         <div><div class="jr-rappel-l">Collez deux idées avec un relatif</div><div class="jr-rappel-x">L'autocar <b>qui</b> part à sept heures est direct. · Le gîte <b>dont</b> on m'a parlé n'a que quatre chambres.</div></div>
         <div><div class="jr-rappel-l">Comparez, puis concluez</div><div class="jr-rappel-x">Le train est <b>plus</b> confortable <b>que</b> l'autocar, mais il passe <b>moins</b> souvent : je prends l'autocar.</div></div>
         <div><div class="jr-rappel-l">Dites le moyen avec le gérondif</div><div class="jr-rappel-x"><b>En réservant</b> après le quinze septembre, je paie le tarif de basse saison.</div></div>
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
     <h3 class="prod-tit">Le message de réservation au gîte</h3>
     <p class="prod-lead">Vous téléphonez au gîte pour réserver et personne ne décroche : c'est une petite maison de quatre chambres, pas un hôtel. Vous laissez un message. Écrivez-le d'abord, lisez-le à voix haute, puis enregistrez-le. De trente à quarante-cinq secondes — cinq morceaux, dans l'ordre.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Qui parle, et pourquoi vous appelez</div><div class="plan-ex">« Bonjour, c'est Thuy Pham, je vous appelle de Montréal au sujet d'une réservation. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Les dates et le nombre de nuits, en chiffres</div><div class="plan-ex">« Je voudrais une chambre du lundi 28 septembre au dimanche 4 octobre, six nuits. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Combien de personnes, et comment vous arriverez</div><div class="plan-ex">« Une personne. J'arriverai en autocar, vers quinze heures trente. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 4</div><div class="plan-t">Deux questions, posées poliment</div><div class="plan-ex">« Je voudrais savoir si le déjeuner est compris, et pourriez-vous me dire s'il y a moyen de se rendre au parc sans auto ? »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 5</div><div class="plan-t">Votre numéro, dit lentement, et la politesse</div><div class="plan-ex">« Vous pouvez me rappeler au 514 555-0172. Merci beaucoup, bonne journée. »</div></div>
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
           <div class="rec-hint">De trente à quarante-cinq secondes. Réécoutez-vous comme si vous teniez le gîte : pouvez-vous noter un nom, des dates et un numéro de téléphone sans réécouter le message une deuxième fois ?</div>
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
     <h3 class="prod-tit">Le courriel qui donne envie de venir</h3>
     <p class="prod-lead">Vous avez tout préparé et il reste une place dans la chambre. Vous écrivez à une amie pour l'inviter à venir avec vous : où vous irez, quand, comment vous vous rendrez, ce que vous ferez là-bas, et ce que ça coûtera. De 6 à 9 phrases, au futur simple, avec « tu ».</p>
     <div class="req">
       <div class="req-hd">Votre courriel doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une salutation, et une phrase qui dit tout de suite ce que vous proposez</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>La région et la ville, avec la bonne préposition : « à… », « au… », « en… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Les dates et la durée du trajet : « du… au… », « en huit heures », « pour six nuits »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Trois phrases au futur simple : ce que vous ferez là-bas</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une comparaison qui justifie votre choix : « moins cher que… », « plus pratique que… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une question à la fin, et une date de réponse</span></div>
       </div>
       <div class="req-note">Une invitation qui ne dit pas ce que ça coûte ni jusqu'à quand on peut répondre force l'autre à écrire un deuxième courriel pour le demander. Mettez le prix et la date dans les deux dernières phrases : c'est ce qui fait qu'on répond oui du premier coup.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">une amie que vous invitez</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Une semaine au bord du fleuve à la fin septembre ?</span></div>
       <textarea id="peText" rows="9" aria-label="Votre courriel" data-min="6" data-max="9" oninput="peCount()" placeholder="Bonjour Camille,&#10;&#10;J'ai une idée à te proposer pour la semaine du 28 septembre…"></textarea>
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
    "Je connais les mots de la région : un attrait, le fleuve, un phare, un dépliant.",
    "J'entends la différence entre le son de « ou » et le son de « u ».",
    "Je place quelques régions du Québec sur une carte et je sais combien de temps il faut pour s'y rendre.",
    "Je dis où je vais avec la bonne préposition : à Rimouski, en Gaspésie, au Saguenay, dans les Laurentides.",
    "J'expose ma demande d'un seul tenant : où, quand, combien de temps, combien de personnes.",
    "Je pose une question polie : Pourriez-vous me dire… · Je voudrais savoir si…",
    "Je dis le temps avec le mot juste : en huit heures, pour une semaine, à sept heures, vers trois heures.",
    "Je sais ce qui va dans la soute et ce qui reste avec moi à mon siège.",
    "Je lis un horaire de ligne interurbaine et j'y trouve les heures et les correspondances.",
    "Je lis une page de région et j'en tire les cinq renseignements qui me concernent.",
    "Je colle deux idées avec qui, que, où, dont.",
    "Je compare deux possibilités et je dis laquelle je prends, et pourquoi.",
    "Je salue et je réponds comme on le fait ici : bon voyage, bon séjour, bienvenue chez nous.",
    "Je sais quand vouvoyer et quand attendre qu'on me propose le tutoiement.",
    "Je raconte ce que j'ai fait au passé composé et ce qu'il y avait autour à l'imparfait.",
    "Je dis par quel moyen j'y arrive, avec un gérondif : en passant par, en réservant.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#B45309">Je retiens des mots</span><span class="ctit" style="color:#B45309">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#B45309" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#B45309;font-size:13px;margin:6px 0 4px">La région et ses attraits</div>
     <textarea rows="2" placeholder="Ex. : un attrait, le fleuve, un phare, un dépliant, une région touristique…"></textarea>
     <div style="font-weight:800;color:#B45309;font-size:13px;margin:12px 0 4px">Le départ : le billet, l'horaire, les bagages</div>
     <textarea rows="2" placeholder="Ex. : un aller-retour, un horaire, une correspondance, la soute, un bagage à main…"></textarea>
     <div style="font-weight:800;color:#B45309;font-size:13px;margin:12px 0 4px">Ce qui est écrit : dormir, marcher, la marée</div>
     <textarea rows="2" placeholder="Ex. : un gîte, un sentier, la marée, le prêt-à-camper, la basse saison…"></textarea>
     <div style="font-weight:800;color:#B45309;font-size:13px;margin:12px 0 4px">Sur place : les gens et la conversation</div>
     <textarea rows="2" placeholder="Ex. : un vacancier, un belvédère, jaser, bon séjour, bienvenue chez nous…"></textarea>
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
