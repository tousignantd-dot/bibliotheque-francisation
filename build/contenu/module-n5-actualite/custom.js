  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : le récit joué avec l'assistant, le message vocal
  // laissé à Teresa, puis le courriel envoyé à quelqu'un qui est loin. Le jeu
  // de rôle vient en premier parce qu'il sert de répétition aux deux autres —
  // c'est là que l'élève découvre que « il y a eu un problème » ne fait
  // comprendre la nouvelle à personne.
  //
  // Le scénario `faitdivers` a été ajouté à server.py pour ce module. Le
  // scénario `actualite` existe déjà, mais il vient du niveau 7 : on y démêle
  // le reportage de la chronique et l'on intervient dans un blogue. Ici,
  // l'élève n'a qu'un genre — le fait divers — et une seule tâche : raconter
  // à quelqu'un qui n'a rien lu. Seule la situation publique est ici ; ce que
  // Sylvain ignore et ce que Teresa veut savoir vivent sur le serveur.
  const ROLE_CAS = [
    {id:'incendie', titre:"L'incendie de la rue Alexandre", txt:"La pause de dix heures, à la cafétéria. Vous venez de lire qu'<b>un incendie a détruit un immeuble de quatre logements</b> de la rue Alexandre, vers quatre heures du matin. Personne n'a été blessé, mais onze personnes n'ont plus de logement et la Croix-Rouge les héberge. Le Service de sécurité incendie dit que le feu serait parti de la cuisine du deuxième étage."},
    {id:'inondation', titre:"L'eau de la rue des Peupliers", txt:"Après trois jours de pluie, <b>la rivière Magog est sortie de son lit</b> et le sous-sol d'une dizaine de maisons de la rue des Peupliers a été inondé. La Ville a fermé une rue et distribué des sacs de sable dès lundi. Une résidente raconte qu'elle a tout perdu dans son sous-sol et demande si la Ville va refaire le fossé au bout de la rue."},
    {id:'velos', titre:"Les trente vélos du quartier", txt:"<b>Une trentaine de vélos ont été volés en un mois</b> dans le quartier, presque tous dans des cabanons et des garages laissés ouverts. Le Service de police de Sherbrooke demande aux gens de noter le numéro de série de leur vélo et de signaler tout vol, même petit. Un commerçant dit qu'il a vu passer trois vélos dans une remorque, tard le soir."},
  ];
  const ROLE_SUJETS = ["Dire ce qui est arrivé d'un seul tenant, avant tout détail",
    "Dire où et quand, avec un repère précis : rue Alexandre, vers quatre heures du matin",
    "Mettre le déroulement au passé composé : le feu a éclaté, les pompiers sont arrivés",
    "Mettre le décor à l'imparfait : il était quatre heures, tout le monde dormait",
    "Rapporter au moins une parole au présent, en nommant qui l'a dite",
    "Séparer ce que le journal dit de ce que vous en pensez",
    "Annoncer votre avis comme un avis : moi, ce qui me surprend, c'est…",
    "Justifier votre avis avec « parce que » ou après un deux-points",
    "Accorder à l'autre ce qu'il a de juste avant de dire pourquoi vous pensez autrement"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Raconter la nouvelle à quelqu'un qui ne l'a pas lue</span></div>
     <p class="lead">L'assistant joue Sylvain Ouellet, le cuisinier avec qui vous prenez votre pause. Il n'ouvre jamais un journal et il ne devine rien : si vous commencez par un détail, il vous demandera d'abord ce qui est arrivé — et il redemandera. Vers la fin, il vous donnera son avis à lui, un peu tranché, pour que vous ayez à répondre. Essayez ensuite l'autre interlocutrice : Teresa, au téléphone, qui ne voit rien et qui veut savoir qui a dit quoi.</p>
     <div class="jr-grid">
       ${ROLE_CAS.map(c=>`
       <div class="jr-log">
         <div class="jr-log-h">${esc(c.titre)}</div>
         <div class="jr-log-a">${c.txt}</div>
       </div>`).join('')}
     </div>
     <div class="jr-sub">Les neuf choses à faire avant la fin de la pause</div>
     <div class="jr-sujets">
       ${ROLE_SUJETS.map(s=>`<div class="jr-sujet"><span class="jr-box"></span>${esc(s)}</div>`).join('')}
     </div>
     <div class="jr-gram">
       <div class="jr-gram-t">Réutilisez ce que vous venez d'apprendre</div>
       Racontez les évènements au passé composé, l'un après l'autre :
       <span class='savoir-ex'>Le feu <b>a éclaté</b> vers quatre heures. Un locataire <b>s'est réveillé</b>. Les pompiers <b>sont arrivés</b> huit minutes plus tard.</span>
       Plantez le décor à l'imparfait :
       <span class='savoir-ex'>Il <b>était</b> quatre heures du matin, tout le monde <b>dormait</b>, et la rue <b>était</b> déserte.</span>
       Croisez les deux dans la même phrase :
       <span class='savoir-ex'>Il <b>dormait</b> quand il <b>a entendu</b> l'alarme.</span>
       Rapportez une parole au présent, en nommant qui parle :
       <span class='savoir-ex'>Le Service de sécurité incendie <b>dit que</b> le feu serait parti de la cuisine. · Une résidente <b>demande si</b> la Ville va refaire le fossé.</span>
       Annoncez votre avis comme un avis :
       <span class='savoir-ex'><b>Moi, ce qui me surprend, c'est</b> le nombre. · <b>Ce qui me dérange, c'est que</b> les gens laissent leur cabanon ouvert.</span>
       Accordez d'abord, tournez ensuite :
       <span class='savoir-ex'><b>C'est vrai que</b> ça aide de barrer sa porte. <b>Par contre</b>, ça n'excuse pas celui qui entre.</span>
     </div>

     <div class="jr-sep"></div>
     <div class="jr-sub">Choisissez votre nouvelle et qui vous avez en face</div>
     <div class="jr-choix">
       <div class="jr-choix-l">Quelle nouvelle ?</div>
       <div class="jr-opts" id="jrLogs">
         ${ROLE_CAS.map((c,i)=>`<button class="jr-opt${i===0?' on':''}" type="button" data-log="${c.id}" onclick="jrChoisir('log','${c.id}')">${esc(c.titre)}</button>`).join('')}
       </div>
       <div class="jr-choix-l">L'assistant joue qui ?</div>
       <div class="jr-opts" id="jrRoles">
         <button class="jr-opt on" type="button" data-role="sylvain" onclick="jrChoisir('role','sylvain')">Sylvain, à la pause</button>
         <button class="jr-opt" type="button" data-role="teresa" onclick="jrChoisir('role','teresa')">Teresa, au téléphone</button>
       </div>
       <div class="jr-choix-l">Comment ?</div>
       <div class="jr-opts" id="jrModes">
         <button class="jr-opt on" type="button" data-mode="texte" onclick="jrModeVoix(false)">✍️ Écrire</button>
         <button class="jr-opt" type="button" data-mode="voix" onclick="jrModeVoix(true)">🎤 Parler</button>
       </div>
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()" style="margin-top:14px">Commencer la pause</button>
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
     <h3 class="prod-tit">Le message laissé à Teresa</h3>
     <p class="prod-lead">Vous appelez votre belle-sœur à Granby pour lui raconter la nouvelle du jour. Elle ne répond pas : vous laissez un message. Elle n'a rien lu, elle ne connaît pas Sherbrooke, et elle voudra savoir qui a dit quoi. Écrivez d'abord votre message, lisez-le à voix haute, puis enregistrez-le. De quarante-cinq à soixante secondes — cinq morceaux, dans l'ordre.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">La nouvelle en une phrase : ce qui est arrivé, où, quand</div><div class="plan-ex">« Allô Teresa, c'est Marisol. J'ai lu dans le journal qu'un immeuble de quatre logements a passé au feu cette nuit, sur la rue Alexandre. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Le décor, à l'imparfait : l'heure, le temps, ce que les gens faisaient</div><div class="plan-ex">« Il était à peu près quatre heures du matin, tout le monde dormait et la rue était déserte. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Le déroulement, au passé composé : deux ou trois évènements qui se suivent</div><div class="plan-ex">« Un locataire s'est réveillé, il a cogné à toutes les portes, et les pompiers sont arrivés huit minutes après l'appel. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 4</div><div class="plan-t">Une parole rapportée, avec le nom de la personne qui l'a dite</div><div class="plan-ex">« Le Service de sécurité incendie dit que le feu serait parti de la cuisine du deuxième, mais que l'enquête se poursuit. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 5</div><div class="plan-t">Votre avis, annoncé comme un avis, et sa raison</div><div class="plan-ex">« Moi, ce qui me frappe, c'est qu'un seul locataire a réveillé tout l'immeuble : sans lui, il y aurait eu des blessés. Rappelle-moi ! »</div></div>
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
           <div class="rec-hint">De quarante-cinq à soixante secondes. Réécoutez-vous comme si vous étiez Teresa, à Granby, qui n'a rien lu : savez-vous ce qui est arrivé dès la première phrase ? Pouvez-vous dire qui a affirmé quoi ? Savez-vous où s'arrête le journal et où commence l'avis de la personne qui parle ?</div>
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
     <h3 class="prod-tit">Le courriel à quelqu'un qui est loin</h3>
     <p class="prod-lead">Vous écrivez à une personne de votre famille qui habite ailleurs et qui ne lit pas L'Écho des Cantons. Racontez-lui la nouvelle des vélos volés : ce qui est arrivé, ce que la police demande, et ce que vous en pensez. De 7 à 10 phrases, avec « tu ».</p>
     <div class="req">
       <div class="req-hd">Votre courriel doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une salutation, et la nouvelle en une phrase dès le début</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Deux phrases au passé composé : ce qui est arrivé, dans l'ordre</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une phrase à l'imparfait pour le décor : « les cabanons n'étaient pas… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une parole rapportée au présent, avec le nom de qui l'a dite</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une phrase impersonnelle : « il faut… », « il vaut mieux… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Votre avis annoncé comme un avis, avec sa raison, et une signature</span></div>
       </div>
       <div class="req-note">Une personne qui est loin ne connaît ni la rue, ni le quartier, ni le journal. Dites où c'est, dites d'où vient l'information, et séparez nettement ce que le journal rapporte de ce que vous en pensez : sans ça, elle répétera votre avis comme s'il était écrit noir sur blanc.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">Teresa</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Ce que j'ai lu dans le journal cette semaine</span></div>
       <textarea id="peText" rows="10" aria-label="Votre courriel" data-min="7" data-max="10" oninput="peCount()" placeholder="Allô Teresa,&#10;&#10;Je t'écris pour te raconter ce que j'ai lu mardi dans L'Écho des Cantons…"></textarea>
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
    "Je reconnais un fait divers dans un journal, et je sais où lire le chapeau.",
    "Je connais les mots du journal : un hebdomadaire, le chapeau, un témoin, un fait divers.",
    "J'entends la différence entre le son de « in » et le son de « on ».",
    "Je distingue la famille du sinistre — incendie, inondation, sinistré — de celle du délit — vol, suspect, plainte.",
    "Je raconte ce qui est arrivé d'un seul tenant, avant de donner les détails.",
    "J'emploie le passé composé pour les évènements, avec le bon auxiliaire.",
    "J'emploie l'imparfait pour le décor : l'heure, le temps qu'il faisait, ce que les gens faisaient.",
    "Je croise les deux dans une phrase : « il dormait quand le feu a éclaté ».",
    "Je rapporte une parole au présent avec « que », « si », « ce que ».",
    "Je change les pronoms et les déterminants quand je rapporte : je → il, mon → son.",
    "Je nomme toujours la personne ou le service qui a dit ce que je répète.",
    "Je reconnais une phrase qui ne porte aucune source : « il paraît que », « on dit que ».",
    "Je distingue un fait vérifiable d'une opinion.",
    "J'annonce mon avis comme un avis : « moi, ce qui me surprend, c'est… ».",
    "Je justifie mon avis avec « parce que » ou après un deux-points.",
    "Je réponds à quelqu'un qui pense autrement : j'accorde d'abord, puis je dis pourquoi.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Le journal et sa forme</div>
     <textarea rows="2" placeholder="Ex. : un fait divers, un hebdomadaire, le chapeau, un titre, une légende, un témoin…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Le sinistre et les secours</div>
     <textarea rows="2" placeholder="Ex. : un incendie, une inondation, évacuer, un sinistré, héberger, un avertissement…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">L'enquête et la parole rapportée</div>
     <textarea rows="2" placeholder="Ex. : une enquête, un enquêteur, une déclaration, un porte-parole, selon, il dit que…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Le vol et ce que j'en pense</div>
     <textarea rows="2" placeholder="Ex. : un vol, un suspect, un cabanon, la prévention, moi ce qui me surprend, par contre…"></textarea>
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
