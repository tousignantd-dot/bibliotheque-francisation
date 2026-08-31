  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : l'appel à la tribune avec l'assistant, l'intervention
  // enregistrée, puis la lettre au courrier des lecteurs. Le jeu de rôle vient
  // en premier parce qu'il sert de répétition aux deux autres.
  //
  // D'OÙ VIENNENT CES TÂCHES. Contrairement à `module-n8-recherche` (119), rien
  // ici n'a besoin d'être emprunté aux attentes de fin de cours : les trois
  // tâches sortent directement des sept intentions de la situation « Suivi de
  // l'actualité » au niveau 8. Le jeu de rôle et la production orale viennent
  // de l'unique intention de production orale — « commenter l'actualité en
  // justifiant son point de vue » —, à laquelle s'ajoute l'intention hors
  // situation « participer à une tribune téléphonique », qui en donne la forme.
  // La lettre porte les **deux** intentions de production écrite d'un coup :
  // « rédiger une lettre pour le courrier des lecteurs pour donner son
  // opinion » et « résumer un texte d'opinion » — d'où l'exigence que son
  // premier paragraphe résume l'éditorial auquel elle répond. Les deux ne se
  // séparent pas : une lettre qui ne résume pas ce qu'elle conteste n'a aucune
  // prise, et un résumé sans réponse n'est pas une lettre.
  //
  // Seule la situation publique est côté client ; ce que sait l'animateur joué
  // par l'assistant vit dans server.py, scénario « tribune ».
  const ROLE_CAS = [
    {id:'boise', titre:'Le boisé Sainte-Perpétue', txt:"Le conseil a cédé <b>onze hectares</b> de terrain municipal à un promoteur pour un dollar, en échange de <b>quarante-cinq logements abordables</b> sur cent quatre-vingts. Le vote a été pris <b>à vingt-deux heures cinquante, par quatre voix contre trois, devant onze personnes</b>. L'évaluation du terrain n'a pas été publiée. Un registre référendaire s'ouvre dans six jours et il faut sept cent quatre-vingt-douze signatures."},
    {id:'arena', titre:"Le terrain derrière l'aréna", txt:"Un <b>second terrain municipal</b>, déjà déboisé et desservi, existe derrière l'aréna. La Ville répond qu'il est zoné industriel et que le rezonage prendrait <b>vingt et un mois</b>, alors que le financement du promoteur <b>expire en mars</b>. Ce délai est une estimation du service de l'urbanisme ; aucune étude n'a été demandée, et rien de tout cela n'est écrit."},
    {id:'arbres', titre:"Quatre-vingt-dix, ou trois cent quarante-deux", txt:"Le promoteur annonce <b>quatre-vingt-dix arbres</b> abattus avec replantation à deux pour un. Le comité de citoyens en a compté <b>trois cent quarante-deux</b> un samedi, à six personnes, et a remis ses feuilles à la Ville sans recevoir de réponse. Les deux comptages existent ; le désaccord porte sur ce qu'on appelle un arbre."},
  ];
  const ROLE_SUJETS = ["Annoncer votre position en une phrase, avant de l'expliquer",
    "Résumer le fait en deux phrases, sans le déformer",
    "Donner deux arguments, dont un chiffré et un vécu",
    "Séparer ce que vous savez de ce qu'on vous a rapporté",
    "Concéder un point à l'autre camp : certes…, mais… · bien que… soit…",
    "Employer une hypothèse irréelle : si la Ville avait…, personne n'aurait…",
    "Refuser une rumeur qu'on vous tend, sans vous fâcher",
    "Terminer par une demande précise, adressée à quelqu'un qui peut agir"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">L'appel à la tribune</span></div>
     <p class="lead">L'assistant joue <b>l'animateur de la tribune téléphonique</b>. Il est courtois et il ne vous laisse rien passer : il vous demande vos sources, il vous oppose l'argument du camp adverse, et il vous tend au moins une fois une rumeur pour voir si vous la reprenez. Vous avez deux minutes d'antenne, comme tout le monde.</p>
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
         <button class="jr-opt on" type="button" data-role="auditeur" onclick="jrChoisir('role','auditeur')">La personne qui appelle</button>
         <button class="jr-opt" type="button" data-role="animateur" onclick="jrChoisir('role','animateur')">L'animateur de la tribune</button>
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
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()">Commencer l'appel</button>
     </div>
     <div class="jr-rappel">
       <div class="jr-rappel-t">Réutilisez ce que vous venez d'apprendre</div>
       <div class="jr-rappel-g">
         <div><div class="jr-rappel-l">Concédez, puis avancez</div><div class="jr-rappel-x"><b>Certes</b> le besoin de logements est réel, <b>mais</b> une décision prise devant onze personnes ne tiendra pas.</div></div>
         <div><div class="jr-rappel-l">Concédez en un bloc, au subjonctif</div><div class="jr-rappel-x"><b>Bien que</b> le projet <b>soit</b> nécessaire, je vais signer le registre.</div></div>
         <div><div class="jr-rappel-l">Dites ce qui aurait pu se passer autrement</div><div class="jr-rappel-x"><b>Si</b> la Ville <b>avait publié</b> l'évaluation, je n'<b>aurais</b> pas <b>eu</b> besoin d'appeler.</div></div>
         <div><div class="jr-rappel-l">Mettez en avant ce qui compte</div><div class="jr-rappel-x"><b>Ce que je demande, c'est</b> la publication de l'évaluation avant mardi.</div></div>
         <div><div class="jr-rappel-l">Renversez avec un fait</div><div class="jr-rappel-x">On nous dit que tout a été étudié. <b>Or</b>, le terrain de l'aréna ne l'a jamais été.</div></div>
         <div><div class="jr-rappel-l">Refusez une rumeur</div><div class="jr-rappel-x"><b>Je n'en sais rien, et ce n'est pas mon argument.</b></div></div>
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
     <h3 class="prod-tit">Commentez la nouvelle en justifiant votre point de vue</h3>
     <p class="prod-lead">Deux minutes environ, comme si la ligne venait de s'ouvrir. Ce n'est pas un exposé : c'est une intervention, et une intervention se juge à sa première et à sa dernière phrase. Vous pouvez prendre le dossier du boisé ou un sujet d'actualité qui vous touche, à condition d'en avoir les faits.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Annoncez votre position, puis résumez le fait en deux phrases</div><div class="plan-ex">« Je suis pour le projet, et je vais quand même signer le registre. Le conseil a cédé onze hectares pour un dollar, lundi soir, par quatre voix contre trois. L'évaluation du terrain n'a jamais été publiée. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Deux arguments — un vécu, un chiffré — puis une concession</div><div class="plan-ex">« Trois de mes collègues ont quitté la ville faute de logement : le besoin, je ne le conteste pas. Mais un vote pris à vingt-deux heures cinquante devant onze personnes ne tiendra pas dix ans. Certes un report mettrait le financement en péril, et je ne fais pas semblant de l'ignorer. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Ce qui aurait pu se passer autrement, puis votre demande</div><div class="plan-ex">« Si la Ville avait publié l'évaluation la semaine dernière, je n'aurais pas eu besoin d'appeler ce matin. Ce que je demande, c'est qu'elle la publie avant l'ouverture du registre, mardi. »</div></div>
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
           <div class="rec-hint">Parlez environ deux minutes. Vous pourrez recommencer autant de fois que vous voulez.</div>
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
     <p class="prod-lead">De 12 à 16 phrases, en quatre paragraphes. Le premier rattache votre lettre à l'éditorial et le <b>résume en trois phrases honnêtes</b> — c'est un exercice à part entière, et c'est ce qui vous rend crédible pour la suite. Le deuxième annonce votre position et l'appuie. Le troisième concède ce que votre position coûte, puis y répond. Le quatrième demande, à quelqu'un qui peut agir. Vous signez de votre nom et de votre ville.</p>
     <div class="req">
       <div class="req-hd">Votre lettre doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le rattachement : le titre de l'éditorial et sa date</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un résumé de la thèse adverse en trois phrases, sans caricature</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Votre position, annoncée en une seule phrase</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Deux arguments, dont un chiffré et un tiré de votre expérience</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une concession : certes…, mais… · bien que… + subjonctif</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une hypothèse irréelle : si… avait…, … aurait…</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une mise en relief : ce que je demande, c'est… · c'est… qui…</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une demande précise, adressée à quelqu'un qui peut agir</span></div>
       </div>
       <div class="req-note">Vous écrivez à la rédaction, sur une question publique — jamais à une personne. Séparez ce que vous savez, ce qu'on vous a rapporté et ce que vous en pensez : mêler les trois vous rend attaquable en une ligne. Et ne reprenez aucune rumeur, même pour la nuancer.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">Le Courant de la Rive — courrier des lecteurs</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">En réaction à l'éditorial « Un terrain qui ne rapportait rien », 14 octobre</span></div>
       <textarea id="peText" rows="14" aria-label="Votre lettre" data-min="12" data-max="16" oninput="peCount()" placeholder="Madame, Monsieur,&#10;&#10;En réaction à l'éditorial paru dans votre édition du 14 octobre…"></textarea>
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
    "Je nomme les genres de l'actualité : l'éditorial, la chronique, le reportage, le courrier des lecteurs.",
    "Je sais qu'un communiqué de la Ville se retrouve tel quel dans plusieurs journaux.",
    "J'entends ce qu'une voix ajoute aux mots : la surprise, la déception, la volonté.",
    "Je distingue un fait, une opinion et un propos rapporté.",
    "Je reconnais le conditionnel journalistique et je ne le reprends pas à mon compte.",
    "Je lis deux articles sur un même fait et je vois ce que chacun choisit de taire.",
    "Je repère une phrase passive et je me demande qui elle efface.",
    "Je remarque le mot choisi pour nommer la chose, et ce qu'il fait entendre.",
    "Je retrouve la thèse, les arguments, la concession et l'appel d'un texte d'opinion.",
    "Je suis une chronique de douze minutes en trois écoutes : la position, les chiffres, ce qui revient.",
    "J'emploie les connecteurs de concession : certes…, mais… · bien que… soit… · même si… est…",
    "J'emploie « or » pour introduire le fait qui renverse.",
    "J'emploie le subjonctif après un verbe d'opinion nié, un sentiment ou une appréciation.",
    "Je dis ce qui aurait pu se passer autrement : si… avait…, … aurait…",
    "Je mets en relief ce qui compte : ce que je demande, c'est… · c'est… qui…",
    "J'emploie « dont », « auquel », « pour lesquelles » et je sais à quoi ils renvoient.",
    "Je réponds à une objection en concédant ou en rectifiant, jamais en esquivant.",
    "Je refuse une rumeur qu'on me tend : je n'en sais rien, et ce n'est pas mon argument.",
    "Je résume un texte d'opinion en trois phrases que son auteur signerait.",
    "J'écris une lettre au courrier des lecteurs qui se termine par une demande précise.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#1D6B8F">Je retiens des mots</span><span class="ctit" style="color:#1D6B8F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#1D6B8F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:6px 0 4px">Les genres et les médias</div>
     <textarea rows="2" placeholder="Ex. : un éditorial, une chronique, une manchette, un communiqué, le courrier des lecteurs, une radio communautaire…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">Lire deux versions d'un même fait</div>
     <textarea rows="2" placeholder="Ex. : une source, un parti pris, un boisé, un remblai, une phrase passive, une reprise…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">Argumenter</div>
     <textarea rows="2" placeholder="Ex. : une thèse, une concession, une nuance, certes… mais, bien que, or, il n'en reste pas moins que…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">La vie municipale</div>
     <textarea rows="2" placeholder="Ex. : une assemblée de consultation, un registre référendaire, une personne habile à voter, un règlement, un avis public…"></textarea>
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
