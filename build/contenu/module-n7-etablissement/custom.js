  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : l'entrevue avec l'assistant, la présentation du projet
  // de formation à voix haute, puis la lettre de motivation. Le jeu de rôle
  // vient en premier parce qu'il sert de répétition aux deux autres.
  //
  // D'où viennent ces trois tâches. Les trois intentions de la situation
  // « Communication avec le personnel de l'établissement », au niveau 7, sont
  // « participer à une entrevue de sélection pour suivre une formation »
  // (CO et PO), « téléphoner après une entrevue pour faire un suivi » (CO et
  // PO) et « rédiger une lettre de motivation en vue de participer à une
  // formation » (PE). Les trois productions sont donc les trois intentions
  // elles-mêmes : rien ici ne sort des attentes de fin de cours faute de
  // mieux, contrairement à la plupart des modules du niveau 6.
  //
  // Seule la situation publique est ici ; ce que savent le conseiller et
  // l'enseignant joués par l'assistant vit dans server.py, scénario
  // « admission ».
  const ROLE_CAS = [
    {id:'entrevue', titre:"L'entrevue de sélection", txt:"Vous êtes convoquée à une <b>entrevue de sélection</b> pour un programme <b>contingenté</b> : <b>24 places</b>, <b>68 candidatures</b>. Devant vous, le conseiller pédagogique et un enseignant du programme. Vingt-cinq minutes pour dire d'où vous venez, ce que vous apportez et où vous allez — sans réciter."},
    {id:'trou', titre:"La formation qui n'a pas été finie", txt:"Votre dossier porte une <b>formation interrompue</b> : deux années faites, aucun diplôme. Le comité va y venir. Vous voulez l'expliquer <b>en une phrase</b>, sans vous excuser, puis montrer ce que ces deux années vous ont laissé — et ne plus y revenir."},
    {id:'suivi', titre:"Le suivi, après la décision", txt:"Vous êtes <b>retenue</b> mais sur la <b>liste d'attente</b>, et la lettre ne dit ni votre rang, ni jusqu'à quand. Vous rappelez le conseiller, comme il vous l'avait demandé. Vous voulez repartir avec une chose à faire et une date pour rappeler."},
  ];
  const ROLE_SUJETS = ["Saluer, se nommer et dire en une phrase pourquoi vous êtes là",
    "Répondre de façon complète à une question ouverte : deux ou trois phrases, jamais un mot",
    "Donner un fait daté plutôt qu'un adjectif : cinq ans, douze résidents, depuis janvier",
    "Expliquer en une phrase ce qui manque au parcours, sans s'excuser",
    "Concéder une difficulté, puis dire comment elle est organisée",
    "Mettre en avant l'essentiel : « ce que je veux, c'est… », « c'est en… que… »",
    "Poser au conditionnel les deux ou trois questions que vous avez préparées",
    "Demander avant de partir quand la décision sera communiquée, et par quel moyen"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Passez l'entrevue de sélection</span></div>
     <p class="lead">L'assistant joue <b>le conseiller pédagogique du centre</b> : courtois, pressé, et habitué aux réponses apprises par cœur. Il ne cherche pas à vous prendre en défaut, mais il ne remplit pas les silences à votre place, et il n'invente rien de ce que vous ne dites pas. À vous de répondre par des faits, de concéder ce qui manque et de poser vos questions avant de partir. Vouvoyez-le du début à la fin.</p>
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
         <button class="jr-opt on" type="button" data-role="rania" onclick="jrChoisir('role','rania')">La personne qui pose sa candidature</button>
         <button class="jr-opt" type="button" data-role="conseiller" onclick="jrChoisir('role','conseiller')">Le conseiller pédagogique</button>
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
         <div><div class="jr-rappel-l">Demandez au conditionnel</div><div class="jr-rappel-x"><b>Pourriez-vous</b> me préciser la date de la décision ? · <b>Auriez-vous</b> un exemple à me donner ?</div></div>
         <div><div class="jr-rappel-l">Supposez sans promettre</div><div class="jr-rappel-x"><b>Si j'étais</b> admise en janvier, je <b>garderais</b> mes deux quarts de fin de semaine.</div></div>
         <div><div class="jr-rappel-l">Mettez en avant ce qui compte</div><div class="jr-rappel-x"><b>Ce que</b> je veux, <b>c'est</b> être celle qu'on va chercher. · <b>C'est en</b> travaillant de nuit <b>que</b> j'ai appris à observer.</div></div>
         <div><div class="jr-rappel-l">Concédez, puis répondez</div><div class="jr-rappel-x"><b>Bien que</b> je n'<b>aie</b> pas encore mon préalable, je suis inscrite à la mise à niveau. · <b>Même si</b> l'horaire <b>est</b> serré, il est prévu.</div></div>
         <div><div class="jr-rappel-l">Annoncez votre sujet</div><div class="jr-rappel-x"><b>Quant à</b> mes disponibilités, elles sont réglées depuis février.</div></div>
         <div><div class="jr-rappel-l">Rapportez ce qui a été dit</div><div class="jr-rappel-x">Vous m'<b>aviez dit</b> que le stage <b>arriverait</b> avant Noël.</div></div>
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
     <h3 class="prod-tit">Présentez votre projet de formation, comme devant un comité</h3>
     <p class="prod-lead">On vous demande : « Parlez-nous de votre projet. » Répondez en 90 secondes environ, en trois temps : ce que vous visez et depuis quand, ce que vous apportez avec deux faits datés, puis où vous allez après le diplôme et ce que vous faites déjà pour y arriver. Concédez une difficulté en chemin, et ne vous diminuez pas.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Ce que je vise, et depuis quand</div><div class="plan-ex">« Je pose ma candidature au diplôme en santé, assistance et soins infirmiers. J'y pense depuis deux ans, et j'ai attendu d'avoir réglé mon horaire avant de déposer un dossier. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Ce que j'apporte : deux faits datés, une aptitude prouvée</div><div class="plan-ex">« Je suis préposée depuis cinq ans à l'unité prothétique, où j'accompagne douze résidents. C'est en travaillant de nuit que j'ai appris à observer : la nuit, personne ne vient vous dire ce qui se passe. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Où je vais, ce que je fais déjà, et l'obstacle organisé</div><div class="plan-ex">« Après le diplôme, je veux mon permis de l'Ordre et travailler en longue durée. Bien que je n'aie pas encore mon préalable de mathématiques, je suis inscrite à la mise à niveau de septembre. »</div></div>
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
     <h3 class="prod-tit">Écrivez votre lettre de motivation</h3>
     <p class="prod-lead">Écrivez la lettre qui accompagne votre dossier de candidature : 10 à 14 phrases, en <b>trois paragraphes</b>. Le premier dit ce que vous demandez et pourquoi cet établissement-là ; le deuxième donne les faits datés qui le prouvent, et explique en une phrase ce qui manque à votre parcours s'il y a lieu ; le troisième dit où vous allez après le diplôme et ce que vous faites déjà pour y arriver.</p>
     <div class="req">
       <div class="req-hd">Votre lettre doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un objet de six ou sept mots, sans verbe conjugué</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une formule d'appel, et la formule de courtoisie qui la reprend à la fin</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Trois paragraphes séparés, un par idée</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une raison qui ne pourrait pas être écrite pour un autre établissement</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Deux faits datés : une durée, un nombre, un lieu — pas des adjectifs</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un connecteur qui annonce un sujet : quant à, en ce qui concerne</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une concession : bien que + subjonctif, ou même si + indicatif</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une phrase qui dit ce que vous faites déjà, avant d'être admis</span></div>
       </div>
       <div class="req-note">N'écrivez pas pourquoi le métier est beau : le comité le sait, et les soixante-sept autres candidatures l'écrivent aussi. Écrivez ce que vous avez fait, quand, où — et ce qui, dans cette page-là, n'aurait pas pu être écrit par quelqu'un d'autre.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">admission@ruisseau-vert.example</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">À vous de le trouver — six ou sept mots, sans phrase complète</span></div>
       <textarea id="peText" rows="10" aria-label="Votre lettre" data-min="10" data-max="14" oninput="peCount()" placeholder="Madame, Monsieur,&#10;&#10;Je vous soumets ma candidature au programme…"></textarea>
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
    "Je lis une fiche de programme jusqu'au bas de la page : préalables, durée, ce qui vient après le diplôme.",
    "Je sais qu'un programme contingenté compare les dossiers entre eux, et non à une note de passage.",
    "Je connais les trois portes de l'admission à un diplôme d'études professionnelles.",
    "Je reconnais le niveau de langue de mon interlocuteur et je choisis le mien.",
    "Je garde le « e » de « nous serions », de « tenir » et de « demander ».",
    "J'écris une lettre de motivation en trois paragraphes, un par idée.",
    "Je remplace un adjectif par un fait daté : une durée, un nombre, un lieu.",
    "J'explique en une phrase ce qui manque à mon parcours, sans m'excuser.",
    "J'annonce le sujet d'un paragraphe : quant à, en ce qui concerne, à l'égard de.",
    "J'emploie le nom à la place du verbe quand la lettre le demande.",
    "Je demande au conditionnel, et je ne mets jamais de conditionnel après « si ».",
    "Je mets en avant l'essentiel : c'est… qui, c'est… que, ce que… c'est.",
    "Je concède avec « bien que » et le subjonctif, ou « même si » et l'indicatif.",
    "Je lis un avis administratif en y cherchant la décision, la date et le nom.",
    "Je rapporte au passé ce qu'on m'a dit : arrivait, arriverait, avait déposé.",
    "Je fais un appel de suivi en trois temps : je me présente, j'expose le motif, je conclus sur une date.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Les mots de l'admission</div>
     <textarea rows="2" placeholder="Ex. : un préalable, un programme contingenté, une entrevue de sélection, un relevé de notes…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les mots du dossier et de la lettre</div>
     <textarea rows="2" placeholder="Ex. : un dossier de candidature, une lettre de motivation, une pièce justificative, une formule de courtoisie…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les mots de l'entrevue</div>
     <textarea rows="2" placeholder="Ex. : un comité de sélection, un plan de carrière, une aptitude, un stage…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les mots du suivi</div>
     <textarea rows="2" placeholder="Ex. : une liste d'attente, un rang, une mise à niveau, la reconnaissance des acquis…"></textarea>
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
