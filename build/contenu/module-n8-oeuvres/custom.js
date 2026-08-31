  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : la discussion d'une fin ouverte avec l'assistant, la
  // lecture proposée à voix haute devant le cercle, puis la lettre au courrier
  // des lecteurs. Le jeu de rôle vient en premier parce qu'il sert de
  // répétition aux deux autres.
  //
  // D'OÙ VIENNENT CES TÂCHES. La situation « Découverte d'œuvres littéraires,
  // musicales, cinématographiques et télévisuelles » du niveau 8 ne porte que
  // DEUX intentions, et toutes deux de RÉCEPTION : comprendre un film, une
  // télésérie, un téléroman ou une pièce de théâtre (CO) ; comprendre une
  // nouvelle ou un texte poétique (CE). Aucune production, ni orale ni écrite.
  // Les trois tâches ci-dessous viennent donc des ATTENTES DE FIN DE COURS du
  // niveau 8, qui sont productives et communes à tout le cours : à l'oral,
  // « au cours d'une discussion, il émet des commentaires en les justifiant à
  // l'aide d'arguments » et « il résume les propos de son interlocuteur et
  // emploie des paraphrases pour vérifier l'information reçue » ; à l'écrit,
  // « il rédige une lettre destinée au courrier des lecteurs pour donner son
  // opinion sur un évènement tout en la justifiant » et « il résume un texte
  // d'opinion ». La lettre au courrier des lecteurs est nommée mot pour mot
  // par le programme. Sans cette note, un relecteur retirerait les trois
  // tâches en les croyant hors programme.
  //
  // Seule la situation publique est côté client ; ce que sait Léandre, joué
  // par l'assistant, vit dans server.py, scénario « interpretation ».
  const ROLE_CAS = [
    {id:'finale', titre:'La dernière scène', txt:"Vous avez vu tous les deux le dernier épisode des « Eaux basses ». Estelle sort du chalet à la nuit tombante, <b>met les bottes de caoutchouc de sa mère</b>, descend au quai, retourne la chaloupe et la remet à l'eau. Elle s'assoit dedans. <b>La corde reste attachée au taquet.</b> Le téléphone sonne sur le quai ; elle ne le prend pas. La lumière du quai s'allume toute seule. Écran noir."},
    {id:'nouvelle', titre:'La chaise du fond', txt:"Vous avez lu tous les deux la nouvelle d'Odile Brassard-Vézina. Gisèle arrive à son propre pot de départ, <b>prend la chaise du fond</b> alors qu'une place l'attendait au centre, laisse le contremaître l'appeler deux fois Ginette, <b>demande à sa voisine de lire la carte à sa place</b> en prétextant des lunettes oubliées — et le narrateur précise entre parenthèses qu'elle ne les avait pas oubliées. À la fin, elle plie la nappe de papier et la met dans son sac."},
    {id:'critique', titre:"Une pièce que personne n'a vue", txt:"Gaspard Thivierge signe dans « L'Écho des Deux-Rives » une critique du « Troisième rang », qui se joue au Vieux-Presbytère jusqu'au 14. <b>Ni vous ni votre interlocuteur n'avez vu la pièce.</b> Le texte donne quatre faits vérifiables, onze jugements, une supposition marquée « on devine que », et un aveu : « je n'ai pas pu le vérifier avant l'heure de tombée ». Vous ne discutez donc pas la pièce : vous discutez le texte."},
  ];
  const ROLE_SUJETS = ["Décrire la scène sans l'interpréter, avant toute chose",
    "Proposer votre lecture en une phrase, et l'annoncer comme une lecture",
    "L'appuyer sur deux détails précis qu'on peut montrer",
    "Reformuler la lecture de l'autre avant d'y répondre",
    "Sortir vous-même l'indice qui gêne votre lecture, et le retourner",
    "Concéder avec « bien que » + subjonctif, opposer avec « même si » + indicatif",
    "Poser une hypothèse irréelle : si elle avait…, elle aurait…",
    "Dire ce que l'autre lecture explique mieux que la vôtre"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Deux lectures, une seule scène</span></div>
     <p class="lead">L'assistant joue <b>Léandre Pinsonneault</b>, 67 ans, membre du cercle depuis six ans. Il a vu et lu exactement la même chose que vous, il s'entend avec vous sur tous les faits — et il n'en tire pas la même histoire. Il ne se laisse pas convaincre par la conviction : il demande un détail, chaque fois.</p>
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
         <button class="jr-opt on" type="button" data-role="fatoumata" onclick="jrChoisir('role','fatoumata')">La personne qui propose une lecture</button>
         <button class="jr-opt" type="button" data-role="leandre" onclick="jrChoisir('role','leandre')">Le membre du cercle qui n'est pas d'accord</button>
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
         <div><div class="jr-rappel-l">Séparez le fait de la lecture</div><div class="jr-rappel-x">Elle <b>s'assoit</b> dans la chaloupe — ça, on le voit. Qu'elle <b>renonce</b>, c'est moi qui l'ajoute.</div></div>
         <div><div class="jr-rappel-l">Mettez en avant l'indice qui porte tout</div><div class="jr-rappel-x"><b>Ce qui compte, c'est</b> le téléphone qu'elle laisse sonner.</div></div>
         <div><div class="jr-rappel-l">Dites ce qui ne s'est pas passé</div><div class="jr-rappel-x"><b>Si</b> elle <b>avait voulu</b> partir, elle <b>aurait détaché</b> la corde.</div></div>
         <div><div class="jr-rappel-l">Concédez, puis avancez</div><div class="jr-rappel-x"><b>Bien que</b> la corde <b>soit</b> attachée, c'est elle qui l'a remise à l'eau.</div></div>
         <div><div class="jr-rappel-l">Laissez la porte ouverte</div><div class="jr-rappel-x"><b>Il se peut qu</b>'elle <b>soit</b> simplement en train d'attendre.</div></div>
         <div><div class="jr-rappel-l">Reformulez avant de répondre</div><div class="jr-rappel-x"><b>Si je vous suis bien</b>, vous y voyez un piège plutôt qu'un choix ?</div></div>
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
     <h3 class="prod-tit">Proposez une lecture devant le cercle</h3>
     <p class="prod-lead">Deux ou trois minutes, debout, sans lire vos notes mot à mot. Prenez une œuvre que vous avez vue, lue ou entendue et dont la fin ne conclut pas — un film, une télésérie, une pièce, une nouvelle, une chanson. Ne la racontez pas : le cercle la connaît. Proposez-en une lecture, et menez-la en trois temps.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Les faits seuls, en trois ou quatre phrases</div><div class="plan-ex">« À la fin, elle met les bottes de sa mère, elle remet la chaloupe à l'eau, elle s'assoit dedans. La corde reste attachée. Le téléphone sonne sur le quai ; elle ne le prend pas. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Votre lecture, annoncée comme une lecture, et deux indices qui l'appuient</div><div class="plan-ex">« Je crois qu'elle choisit de rester, et que c'est son premier choix de toute la série. Ce qui me le fait dire, c'est le téléphone : elle le porte jusqu'au quai pour pouvoir le laisser. Et les bottes : quatorze secondes de plan fixe, c'est une décision de réalisatrice. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">L'autre lecture, ce qu'elle explique mieux, et ce que vous en gardez</div><div class="plan-ex">« Bien sûr, on peut lire l'inverse : la corde reste attachée, et une chaloupe attachée n'emmène personne. Cette lecture-là explique mieux les six épisodes de promesses. Il se peut donc qu'elle soit prise et qu'elle l'accepte — ce qui, au fond, reste un choix. »</div></div>
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
           <div class="rec-hint">Parlez deux ou trois minutes. Vous pourrez recommencer autant de fois que vous voulez.</div>
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
     <h3 class="prod-tit">Écrivez au courrier des lecteurs</h3>
     <p class="prod-lead">Deux cents mots environ, soit de 12 à 16 phrases, en trois paragraphes, adressés à « L'Écho des Deux-Rives » au sujet de la critique du « Troisième rang ». Le premier paragraphe résume en deux phrases ce que le critique soutient — fidèlement, il doit pouvoir l'approuver. Le deuxième concède ce qui tient, puis nomme <b>un seul</b> endroit où un jugement n'est accroché à aucun fait. Le troisième dit ce que vous auriez voulu lire, et se signe. Vous n'avez pas vu la pièce : ne faites jamais semblant du contraire.</p>
     <div class="req">
       <div class="req-hd">Votre lettre doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un résumé fidèle de la critique, en deux phrases</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un verbe introducteur neutre : il écrit, il soutient, il explique</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une concession : certes…, mais… · bien que… + subjonctif</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une citation exacte entre guillemets, avec deux-points</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un relatif à préposition : dont, sur lequel, à laquelle</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une phrase emphatique : ce que je lui reproche, c'est…</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un conditionnel passé : on aurait aimé, j'aurais voulu lire…</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>La mention que vous n'avez pas assisté à la représentation</span></div>
       </div>
       <div class="req-note">Tenez le vouvoiement et un registre soutenu du début à la fin. Ne mettez jamais en cause la personne du critique : on discute un texte, ses appuis et ses trous — c'est la seule chose qu'un journal publie.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">L'Écho des Deux-Rives — courrier des lecteurs</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">À propos de la critique du « Troisième rang », parue jeudi</span></div>
       <textarea id="peText" rows="14" aria-label="Votre lettre" data-min="12" data-max="16" oninput="peCount()" placeholder="Madame, Monsieur,&#10;&#10;Dans son texte de jeudi, monsieur Thivierge soutient que…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 12 à 16</span>
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
    "Je sépare le fait, l'interprétation et le jugement dans une même phrase.",
    "Je reconnais une interprétation déguisée en fait : « elle est triste », « évidemment ».",
    "J'entends ce que la voix ajoute : l'admiration, la déception, l'incompréhension.",
    "Je redis avec d'autres mots ce que quelqu'un vient de dire, pour le vérifier.",
    "Je distingue une fin ouverte d'une fin à laquelle il manquerait quelque chose.",
    "Je dis ce qui aurait pu se passer et ne s'est pas passé : elle aurait pu…",
    "Je pose une hypothèse irréelle du passé : si elle avait…, elle aurait…",
    "Je mets en avant l'indice qui porte ma lecture : ce qui compte, c'est…",
    "Je sais qu'une lecture se juge au nombre d'indices dont elle rend compte.",
    "Je lis un récit littéraire au passé simple sans buter dessus.",
    "Je repère au plus-que-parfait ce qui s'était décidé avant la scène.",
    "Je cherche dans une nouvelle le seul endroit où le narrateur sort de la scène.",
    "Je lis un poème en comptant les strophes et en relisant après le dernier vers.",
    "Je distingue une comparaison d'une métaphore.",
    "J'emploie le subjonctif après « il se peut que », l'indicatif après « il me semble que ».",
    "Je cite un passage avec « dont », « auquel », « sur lequel ».",
    "Je concède avec « bien que » + subjonctif et j'oppose avec « même si » + indicatif.",
    "Je distingue citer, résumer et déformer, et je choisis un verbe introducteur neutre.",
    "Je discute une critique sans avoir vu l'œuvre : je regarde ses appuis, pas ses conclusions.",
    "J'écris deux cents mots au courrier des lecteurs pour défendre une lecture.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#1D6B8F">Je retiens des mots</span><span class="ctit" style="color:#1D6B8F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#1D6B8F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:6px 0 4px">Comprendre une œuvre</div>
     <textarea rows="2" placeholder="Ex. : une interprétation, une lecture, l'implicite, un fait vérifiable, un jugement de valeur…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">L'image et l'écran</div>
     <textarea rows="2" placeholder="Ex. : une fin ouverte, un plan fixe, un dénouement, un indice, une scène…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">Le livre et le poème</div>
     <textarea rows="2" placeholder="Ex. : une nouvelle littéraire, un recueil, une strophe, un vers, une métaphore, le narrateur…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">Discuter et écrire</div>
     <textarea rows="2" placeholder="Ex. : une critique, un argument, le courrier des lecteurs, bien que, autrement dit, il se peut que…"></textarea>
   </div>
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#1D6B8F">Autoévaluation</span><span class="ctit" style="color:#1D6B8F">Qu'est-ce que je suis capable de faire ?</span></div>
     <p class="lead">Pour chaque énoncé, choisissez : pas encore 😟, un peu 🙂, ou oui 😃.</p>
     ${SELF.map((s,i)=>`<div class="selfrow"><div class="self-txt">${s}</div><div class="self-opts">
        <button onclick="rate(${i},this)">😟</button><button onclick="rate(${i},this)">🙂</button><button onclick="rate(${i},this)">😃</button>
     </div></div>`).join('')}
     <div style="margin-top:16px"><button class="btn btn-pri" onclick="finishEval()">Terminer le module 🎉</button></div>
     <div id="evalDone" class="fb" aria-live="polite"></div>
   </div>`;
}
