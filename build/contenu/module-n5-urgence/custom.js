  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un appel au 9-1-1 joué avec l'assistant, l'appel de
  // nouvelles à un proche, puis le message écrit à la famille. Le jeu de rôle
  // vient en premier parce qu'il sert de répétition aux deux autres.
  //
  // Le scénario `urgence911` a été ajouté à server.py pour ce module : aucun
  // des scénarios existants ne convient à un appel d'urgence, où c'est
  // l'assistant qui mène l'échange, dans un ordre fixe, et où il donne des
  // consignes à exécuter. Seule la situation publique est ici — ce que le
  // répartiteur demande, dans quel ordre, et ce qu'il exige avant de laisser
  // raccrocher, vit sur le serveur.
  const ROLE_CAS = [
    {id:'chute', titre:"La chute dans l'escalier", txt:"Il est <b>deux heures du matin</b>. Votre mère de soixante et onze ans est tombée dans l'escalier intérieur. Elle est par terre, elle vous répond, elle a mal à la hanche droite et elle ne peut pas se relever. Vous êtes seule avec elle, au <b>5412, rue des Ormeaux, appartement 2</b>."},
    {id:'poitrine', titre:"La douleur à la poitrine", txt:"Votre voisin de soixante ans a une <b>forte douleur à la poitrine depuis dix minutes</b>. Il transpire et il dit que ça serre. Il refuse l'ambulance parce que « ça coûte cher ». Vous appelez quand même, depuis son logement, au <b>troisième étage sans ascenseur</b>."},
    {id:'dehors', titre:"Un inconnu dans la rue", txt:"En sortant du travail, vous trouvez une personne <b>par terre sur le trottoir</b>, devant le dépanneur du coin. Elle ne répond pas quand vous lui parlez. Vous ne connaissez pas son nom, vous n'êtes pas certain du numéro de la rue, et il fait noir."},
  ];
  const ROLE_SUJETS = ["Donner l'endroit exact, avant tout le reste",
    "Donner le numéro de téléphone d'où vous appelez",
    "Dire ce qui se passe en une seule phrase",
    "Répondre par oui ou par non : consciente ? respire-t-elle ?",
    "Dire ce que vous ne savez pas, plutôt que de l'inventer",
    "Exécuter les consignes reçues et le dire à voix haute",
    "Rester en ligne jusqu'à ce qu'on vous dise de raccrocher"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">L'appel au 9-1-1</span></div>
     <p class="lead">L'assistant joue le répartiteur. Il mène l'échange, il pose ses questions dans un ordre fixe et il ne vous laisse pas raccrocher tant qu'il n'a pas ce qu'il lui faut. Ce n'est pas une conversation : c'est un protocole. Essayez les deux rôles — au niveau 5, il faut savoir <b>répondre</b> et savoir <b>questionner</b>.</p>
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
         <button class="jr-opt on" type="button" data-role="appelant" onclick="jrChoisir('role','appelant')">La personne qui appelle</button>
         <button class="jr-opt" type="button" data-role="repartiteur" onclick="jrChoisir('role','repartiteur')">Le répartiteur du 9-1-1</button>
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
         <div><div class="jr-rappel-l">Donnez l'endroit, puis le détail</div><div class="jr-rappel-x">5412, rue des Ormeaux, appartement 2, <b>en bas de</b> l'escalier intérieur.</div></div>
         <div><div class="jr-rappel-l">Dites ce qui se passe en une phrase</div><div class="jr-rappel-x">Ma mère <b>est tombée</b> dans l'escalier et elle ne peut pas se relever.</div></div>
         <div><div class="jr-rappel-l">Répondez court</div><div class="jr-rappel-x">Oui, elle me répond. · Oui, elle respire. · <b>Je ne sais pas</b>, je ne l'ai pas vue tomber.</div></div>
         <div><div class="jr-rappel-l">Comprenez les ordres à l'impératif</div><div class="jr-rappel-x"><b>Restez</b> près d'elle. · <b>Ne la déplacez pas.</b> · <b>Couvrez-la.</b> · <b>Ne lui donnez rien</b> à boire.</div></div>
         <div><div class="jr-rappel-l">Dites ce que vous faites</div><div class="jr-rappel-x">Je <b>la</b> couvre. Je <b>lui</b> parle. Je descends déverrouiller la porte.</div></div>
         <div><div class="jr-rappel-l">Demandez ce que vous devez savoir</div><div class="jr-rappel-x">Est-ce que je <b>peux</b> lui donner ses médicaments ? Ils arrivent dans combien de temps ?</div></div>
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
     <h3 class="prod-tit">Donner des nouvelles au téléphone</h3>
     <p class="prod-lead">Vous êtes dans le corridor du cinquième étage. Vous appelez un proche qui ne sait encore rien. Vous avez une minute — et la première phrase décide de tout le reste de l'appel.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Rassurer avant de raconter</div><div class="plan-ex">« Écoute-moi d'abord : maman va bien. Elle est à l'hôpital, mais elle va bien. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Planter le décor à l'imparfait, raconter au passé composé</div><div class="plan-ex">« Elle avait de la fièvre depuis deux jours. Cette nuit, elle s'est levée et elle est tombée dans l'escalier. J'ai appelé le 9-1-1. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Rapporter ce qu'on vous a dit</div><div class="plan-ex">« La docteure dit que la douleur est contrôlée. Elle m'a demandé si maman avait des allergies. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 4</div><div class="plan-t">Annoncer la suite au futur simple, puis le pratique</div><div class="plan-ex">« Elle sortira dans trois ou quatre jours. Les visites sont de onze heures à vingt heures, cinquième étage, unité B. »</div></div>
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
           <div class="rec-hint">Environ une minute. Écoutez-vous ensuite comme si vous étiez la personne au bout du fil : est-ce que vous avez été rassuré dans les cinq premières secondes ? Savez-vous où aller et quand ?</div>
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
     <h3 class="prod-tit">Le message qui donne des nouvelles</h3>
     <p class="prod-lead">Cinq personnes de la famille attendent des nouvelles et vous ne pouvez pas appeler cinq fois. Écrivez un seul message, clair, que chacun pourra relire. De 7 à 11 phrases, avec « vous ».</p>
     <div class="req">
       <div class="req-hd">Votre message doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une première phrase qui rassure, avant tout récit</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce qui est arrivé : l'imparfait pour le décor, le passé composé pour les faits</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce que le personnel a dit, rapporté avec « dit que », « a demandé si »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce qui s'en vient, au futur simple</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le pratique : l'étage, l'unité, les heures de visite, ce qu'il faut apporter</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une demande précise adressée à quelqu'un, et un moment où vous joindre</span></div>
       </div>
       <div class="req-note">Écrivez des faits, pas des impressions : <em>« Elle a été opérée hier matin et tout s'est bien passé »</em>, et non <em>« ça a été une nuit épouvantable, je n'en peux plus »</em>. Un message factuel calme la famille ; un message d'émotion la fait téléphoner à l'hôpital.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">la famille — Julio, Rosa, les cousins</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Des nouvelles de maman — hôpital, 5e étage, unité B</span></div>
       <textarea id="peText" rows="9" aria-label="Votre message" data-min="7" data-max="11" oninput="peCount()" placeholder="Bonjour à tous,&#10;&#10;D'abord, maman va bien. Elle est à l'hôpital depuis la nuit de jeudi…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 7 à 11</span>
         <button class="btn-prod" id="peBtn" type="button" onclick="peCheck()">Vérifier mon message</button>
       </div>
     </div>
     <div class="fb" id="peFb" aria-live="polite"></div>
     <div class="status" id="peStatus">Analyse en cours…</div>
     <div class="err" id="peErr"></div>
   </div>`;
  const rb=document.getElementById('recBtn'); if(rb) rb.addEventListener('click',toggleRec);

  // JE RETIENS DES MOTS — notes + cartes mémoire + autoévaluation
  const SELF=[
    "Je sais quand composer le 8-1-1 et quand composer le 9-1-1.",
    "Je connais les cinq signes qui ne se discutent pas.",
    "Je peux décrire au téléphone l'état de quelqu'un d'autre : fièvre, respiration, conscience.",
    "Je donne l'endroit exact avant tout le reste : rue, numéro, appartement, étage.",
    "Je dis en une seule phrase ce qui se passe.",
    "Je réponds par oui ou par non, et je dis « je ne sais pas » quand c'est le cas.",
    "Je comprends les consignes à l'impératif et je les exécute sans les faire répéter.",
    "Je peux raconter au triage ce qui est arrivé : l'imparfait pour le décor, le passé composé pour les faits.",
    "Je comprends ce qu'est un niveau de priorité et pourquoi l'ordre d'arrivée ne compte pas.",
    "Je peux redire ce qu'on m'a demandé : « elle m'a demandé si… », « il m'a demandé où… ».",
    "Je rapporte ce que le médecin a dit sans le déformer.",
    "J'annonce la suite au futur simple et je pose mes questions avant le jour du congé.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Hésiter, et choisir le numéro</div>
     <textarea rows="2" placeholder="Ex. : un malaise, le 8-1-1, faire de la fièvre, perdre connaissance, une infirmière…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">L'appel au 9-1-1</div>
     <textarea rows="2" placeholder="Ex. : un répartiteur, les ambulanciers, une civière, l'endroit, rester en ligne…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Le triage et l'attente</div>
     <textarea rows="2" placeholder="Ex. : le triage, un niveau de priorité, les signes vitaux, une radiographie, une réévaluation…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">L'étage et le congé</div>
     <textarea rows="2" placeholder="Ex. : une fracture, une hospitalisation, les heures de visite, le congé, le CLSC, une marchette…"></textarea>
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
