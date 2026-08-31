  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : la rencontre d'équipe avec l'assistant, le compte
  // rendu oral corrigé, puis le texte écrit. Le jeu de rôle vient en premier
  // parce qu'il sert de répétition aux deux autres.
  //
  // La situation « Salle de classe » du niveau 6 n'a **aucune** intention de
  // production : elle est en compréhension écrite pure. Les trois blocs se
  // tirent donc des attentes de fin de cours du niveau, qui sont communes à
  // toutes ses situations — « il intervient dans une réunion d'information et
  // il saisit également les rapports entre les interlocuteurs » pour le jeu
  // de rôle, « durant un exposé, il décrit de façon détaillée » pour l'oral,
  // « l'adulte rédige un court texte en organisant ses idées à l'aide de
  // paragraphes » pour l'écrit.
  //
  // Seule la situation publique est ici ; ce que sait le coéquipier joué par
  // l'assistant vit dans server.py, scénario « travailequipe ».
  const ROLE_CAS = [
    {id:'repartir', titre:'Qui fait quoi', txt:"Vous êtes trois et il reste <b>onze jours</b>. Rien n'est encore partagé : personne ne sait qui lit quelle source, qui écrit quel paragraphe, ni qui parle en premier devant la classe. Tu arrives avec une proposition."},
    {id:'retard', titre:"La partie qui n'est pas faite", txt:"Il reste <b>quatre jours</b> et une des trois parties n'est pas écrite. Ce n'est pas la tienne. Tu ne veux ni la faire à la place de l'autre, ni remettre un travail troué : il faut décider quelque chose aujourd'hui."},
    {id:'desaccord', titre:'Les sources ne concordent pas', txt:"La page de la ville et la lettre de la lectrice disent le contraire l'une de l'autre. Ton coéquipier veut garder seulement la ville, « pour ne pas se compliquer ». Tu penses qu'il faut écrire les deux, et dire pourquoi elles s'opposent."},
  ];
  const ROLE_SUJETS = ["Dire d'entrée de jeu ce que tu proposes, en une phrase",
    "Exposer ce que tu as déjà fait, avec des détails vérifiables",
    "Justifier ta répartition : pourquoi cette partie-là à cette personne-là",
    "Reprendre ce que l'autre vient de dire sans le répéter mot pour mot",
    "Poser une condition avec « si », sans futur juste après « si »",
    "Fixer une date pour chaque partie, et la faire redire",
    "Récapituler à la fin : qui fait quoi, pour quand"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">La rencontre d'équipe</span></div>
     <p class="lead">L'assistant joue <b>ton coéquipier</b>. Il est de bonne foi, il travaille — mais il ne devine rien et il ne propose rien de lui-même : si tu n'arrives pas avec une répartition, la rencontre finit sans que rien ne soit décidé. C'est exactement ce qui se passe dans une vraie équipe.</p>
     <p class="lead">Choisis ta situation et ton rôle</p>
     <div class="jr-annonces" id="jrLogs">
       ${ROLE_CAS.map((c,i)=>`<button class="jr-opt jr-tuile${i===0?' on':''}" type="button" data-log="${c.id}" onclick="jrChoisir('log','${c.id}')">
         <span class="jr-band"><span class="jr-band-off">Choix ${i+1}</span><span class="jr-band-on"><svg viewBox="0 0 20 20" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 10.5l4 4 8-9"></path></svg> Votre choix</span></span>
         <span class="jr-tuile-c"><span class="jr-tuile-t">${esc(c.titre)}</span><span class="jr-tuile-d">${c.txt}</span></span>
       </button>`).join('')}
     </div>
     <div class="jr-reglages">
       <div class="jr-carte">
         <div class="jr-champ-l">Tu joues qui ?</div>
         <div class="jr-tuiles" id="jrRoles">
         <button class="jr-opt on" type="button" data-role="milagros" onclick="jrChoisir('role','milagros')">Celle qui propose</button>
         <button class="jr-opt" type="button" data-role="youssef" onclick="jrChoisir('role','youssef')">Le coéquipier</button>
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
       <div class="jr-rappel-t">Réutilise ce que tu viens d'apprendre</div>
       <div class="jr-rappel-g">
         <div><div class="jr-rappel-l">Demande une chose précise</div><div class="jr-rappel-x"><b>Envoie-les-moi</b> avant vendredi.</div></div>
         <div><div class="jr-rappel-l">Reprends sans répéter</div><div class="jr-rappel-x">J'ai lu la page de la ville. <b>Cette lecture</b> m'a pris deux heures.</div></div>
         <div><div class="jr-rappel-l">Renvoie à ce qui vient d'être dit</div><div class="jr-rappel-x">Tu dis que la lettre ne compte pas. Moi, je ne <b>le</b> pense pas.</div></div>
         <div><div class="jr-rappel-l">Accroche un moment</div><div class="jr-rappel-x">Le jour <b>où</b> on remet, il sera trop tard pour ça.</div></div>
         <div><div class="jr-rappel-l">Pose une condition</div><div class="jr-rappel-x"><b>Si</b> tu finis ta partie lundi, je relis tout mardi.</div></div>
       </div>
     </div>

     <div id="jrChat" class="hidden">
       <div class="jr-fil" id="jrFil" aria-live="polite"></div>
       <div class="jr-mic hidden" id="jrMicZone">
         <button id="jrMic" type="button" onclick="jrParler()" aria-label="Parler"><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="3" width="6" height="11" rx="3"></rect><path d="M5.5 11.5a6.5 6.5 0 0013 0M12 18v3"></path></svg></button>
         <span class="jr-mic-l" id="jrMicLbl">Touche pour parler</span>
       </div>
       <div class="jr-saisie">
         <input id="jrInput" type="text" placeholder="Écris ce que tu dis…" autocomplete="off"
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
     <h3 class="prod-tit">Présente ton compte rendu à la classe</h3>
     <p class="prod-lead">Cinq minutes par équipe, sans lire ta feuille. Ici, prépare ta part : environ 90 secondes. Dis d'abord ton sujet et pourquoi vous l'avez choisi, puis ce que les sources vous ont appris — en nommant chaque fois d'où ça vient —, et termine par ce que votre équipe en conclut, annoncé comme un avis.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Le sujet, et pourquoi celui-là</div><div class="plan-ex">« Notre sujet, c'est la collecte des matières organiques. On l'a choisi parce qu'aucun de nous ne savait ce qui a le droit d'aller dans le bac brun. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Ce que disent les sources, et qui les dit</div><div class="plan-ex">« La page de la ville explique que le plastique est refusé, même biodégradable. Le bulletin municipal, lui, raconte que les bacs avaient été distribués deux mois avant le début de la collecte. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Ce que l'équipe en conclut, annoncé comme un avis</div><div class="plan-ex">« À notre avis, ce n'est pas la règle qui manque : c'est l'explication. Les gens ont eu le bac avant de savoir quoi mettre dedans. »</div></div>
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
           <div class="rec-lbl" id="recLbl">Touche pour t'enregistrer</div>
           <div class="rec-hint">Parle environ 90 secondes. Tu pourras recommencer autant de fois que tu veux.</div>
         </div>
       </div>
     </div>
     <div id="poPrev" class="hidden prod-tools" style="display:flex;flex-direction:column;gap:12px">
       <audio id="poAudio" controls style="width:100%"></audio>
       <textarea id="poText" rows="2" placeholder="Transcription automatique (tu peux la corriger)…"></textarea>
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
     <h3 class="prod-tit">Écris l'introduction de ton travail</h3>
     <p class="prod-lead">Le début du texte que ton équipe remettra : 8 à 12 phrases, en <b>trois paragraphes séparés par un blanc</b>. Premier paragraphe : le sujet et la question à laquelle vous répondez. Deuxième : les trois sources, nommées, avec ce que chacune apporte. Troisième : ce que le texte va montrer, et dans quel ordre.</p>
     <div class="req">
       <div class="req-hd">Ton introduction doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Trois paragraphes, un par idée principale, séparés par un blanc</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le sujet posé comme une question précise, dès la première phrase</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Les trois sources nommées, avec leur genre : une page de la ville, un article, une lettre</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une distinction claire entre ce qu'un document affirme et ce que vous en pensez</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un connecteur d'exemplification : par exemple, notamment, c'est-à-dire</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une reprise sans répétition : « cette collecte », « ce ramassage », « ces plaintes »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un « où » de temps ou de lieu : l'année où, la page où</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Aucune phrase recopiée sans guillemets ni source</span></div>
       </div>
       <div class="req-note">Une introduction n'annonce pas ce que vous allez trouver : elle annonce ce que vous avez trouvé. Écris-la en dernier, une fois le reste écrit — c'est le seul paragraphe d'un travail qu'il vaut mieux rédiger à la fin.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">Travail</span><span class="mail-v">Recherche en équipe — groupe 402</span></div>
       <div class="mail-row"><span class="mail-k">Partie</span><span class="mail-v">Introduction — à toi de trouver le titre de ton sujet</span></div>
       <textarea id="peText" rows="10" aria-label="Ton introduction" data-min="8" data-max="12" oninput="peCount()" placeholder="Qu'est-ce qui a le droit d'aller dans le bac brun, et pourquoi ?&#10;&#10;Pour répondre à cette question, notre équipe a consulté trois documents…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 8 à 12</span>
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
    "Je sais ce qu'un travail de recherche demande, et en combien de temps.",
    "Je distingue un sujet de recherche d'un simple thème.",
    "Je reconnais les trois familles de lettres qui ne disent pas le son qu'on croit.",
    "Je lis une consigne une ligne à la fois, en soulignant ce qui m'oblige.",
    "Je retrouve l'ordre des étapes même sans « d'abord » ni « ensuite ».",
    "Je comprends qu'un futur simple, dans un document, donne un ordre.",
    "Je lis une grille d'évaluation avant d'écrire, pas après ma note.",
    "J'emploie « de », « à » ou rien du tout devant un verbe à l'infinitif.",
    "Je demande une chose à quelqu'un avec deux pronoms : donne-le-moi.",
    "Je repère dans un texte suivi le passage qui répond à une question précise.",
    "Je retrouve ce que remplacent « le », « en » et « y » dans un texte.",
    "J'emploie « où » pour un lieu et aussi pour un moment.",
    "Je reprends une idée déjà dite par un nom, sans la répéter.",
    "Je reconnais un passé simple dans un historique et je le traduis.",
    "Je vois lequel de deux faits passés est arrivé le premier.",
    "Je distingue ce qu'un document affirme de ce que quelqu'un en pense.",
    "Je peux proposer une répartition du travail dans une rencontre d'équipe.",
    "Je peux présenter un compte rendu de recherche à voix haute, en trois temps.",
    "Je peux écrire une introduction organisée en trois paragraphes.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Le travail lui-même</div>
     <textarea rows="2" placeholder="Ex. : un travail de recherche, un sujet de recherche, un compte rendu, un exposé, une échéance…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Ce que l'établissement demande</div>
     <textarea rows="2" placeholder="Ex. : une consigne de travail, une grille d'évaluation, un barème, un plan de travail, une idée principale…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les documents qu'on lit et qu'on cite</div>
     <textarea rows="2" placeholder="Ex. : une source, un article informatif, un bulletin municipal, le courrier des lecteurs, une bibliographie, une citation…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les mots qui relient les phrases</div>
     <textarea rows="2" placeholder="Ex. : par exemple, notamment, c'est-à-dire, cette distribution, ce ramassage, l'année où…"></textarea>
   </div>
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Autoévaluation</span><span class="ctit" style="color:#A5335F">Qu'est-ce que je suis capable de faire ?</span></div>
     <p class="lead">Pour chaque énoncé, choisis : pas encore 😟, un peu 🙂, ou oui 😃.</p>
     ${SELF.map((s,i)=>`<div class="selfrow"><div class="self-txt">${s}</div><div class="self-opts">
        <button onclick="rate(${i},this)">😟</button><button onclick="rate(${i},this)">🙂</button><button onclick="rate(${i},this)">😃</button>
     </div></div>`).join('')}
     <div style="margin-top:16px"><button class="btn btn-pri" onclick="finishEval()">Terminer le module 🎉</button></div>
     <div id="evalDone" class="fb" aria-live="polite"></div>
   </div>`;
}
