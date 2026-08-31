  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : la discussion avec quelqu'un qui n'est pas d'accord,
  // l'exposé devant la classe, puis le compte rendu écrit. Le jeu de rôle
  // vient en premier parce qu'il sert de répétition aux deux autres.
  //
  // D'où viennent ces tâches. La situation « Découverte d'œuvres » du
  // niveau 7 porte quatre intentions, toutes orales : comprendre une œuvre ou
  // un évènement culturel et faire un commentaire à ce sujet (en CO et en
  // PO), écouter un sketch humoristique, comprendre une chanson, résumer un
  // film. Le jeu de rôle et la production orale sortent donc directement de
  // la situation, sans détour. La production ÉCRITE, elle, n'y est pas : elle
  // se tire des attentes de fin de cours du niveau 7, communes à tout le
  // cours et productives — « il rédige un court texte d'opinion en appuyant
  // son point de vue sur des arguments » et « il rend compte par écrit d'une
  // discussion à laquelle il a participé ». C'est écrit ici pour que le
  // relecteur suivant ne prenne pas le compte rendu pour une invention hors
  // programme.
  //
  // Seule la situation publique est côté client ; ce que sait la personne
  // jouée par l'assistant vit dans server.py, scénario « oeuvres ».
  const ROLE_CAS = [
    {id:'humour', titre:"Le spectacle d'humour", txt:"Vous avez écouté un extrait de <b>« Tout est correct »</b>, de Réjean Cadorette. L'humoriste dit qu'il <b>adore attendre</b> et personne ne le croit : tout le spectacle fonctionne par ironie. Votre interlocuteur, lui, a pris la phrase au premier degré et il a trouvé ça <b>« pas si drôle »</b>."},
    {id:'chanson', titre:"Le tour de chant", txt:"Vous avez entendu <b>« Le troisième étage »</b>, de Nadia Ferron. La chanson raconte une femme qui monte trois étages avec ses sacs, et elle parle en réalité d'autre chose. Votre interlocuteur trouve que <b>le refrain monte trop haut</b> et que l'auteure <b>« chante faux à la fin »</b>."},
    {id:'film', titre:"Le long métrage", txt:"Vous avez vu <b>« Onze heures moins quart »</b>, de Marie-Soleil Brouillette : une boulangerie de nuit, huit nuits de travail, presque aucune parole avant la douzième minute. Votre interlocuteur trouve que <b>deux heures dans le noir</b> ne sont pas une sortie de fin d'année, et qu'on peut regarder un film chez soi."},
  ];
  const ROLE_SUJETS = ["Dire de quelle œuvre vous parlez, et où vous l'avez vue ou entendue",
    "Résumer en deux ou trois phrases, sans dévoiler la fin",
    "Annoncer votre avis comme un avis : je trouve, il m'a semblé, je propose",
    "Donner un moment précis qui appuie ce que vous dites",
    "Accorder un point vrai à l'autre avant de lui répondre",
    "Employer « bien que » avec le subjonctif, ou « même si » avec l'indicatif",
    "Poser une hypothèse avec « si » suivi de l'imparfait",
    "Reconnaître, s'il y a lieu, que l'autre vient de soulever un bon argument"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Discutez avec quelqu'un qui n'est pas d'accord</span></div>
     <p class="lead">L'assistant joue <b>un collègue du comité</b>. Il a vu ou entendu la même œuvre que vous, et il n'en pense pas la même chose. Il n'est ni méchant ni bête : il donne ses raisons, et il en a de bonnes. Il ne changera d'avis que si vous appuyez le vôtre sur un moment précis — et si vous lui accordez d'abord ce qu'il a de juste.</p>
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
         <button class="jr-opt on" type="button" data-role="marilou" onclick="jrChoisir('role','marilou')">La personne qui défend son avis</button>
         <button class="jr-opt" type="button" data-role="gaetan" onclick="jrChoisir('role','gaetan')">Le collègue qui n'est pas d'accord</button>
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
         <div><div class="jr-rappel-l">Accordez, puis maintenez</div><div class="jr-rappel-x"><b>Bien que</b> le début <b>soit</b> lent, la deuxième heure tient sans effort.</div></div>
         <div><div class="jr-rappel-l">Ou, plus simplement</div><div class="jr-rappel-x"><b>Même si</b> le début <b>est</b> lent, le film tient.</div></div>
         <div><div class="jr-rappel-l">Mettez en avant ce qui compte</div><div class="jr-rappel-x"><b>Ce qui</b> m'a convaincue, <b>c'est</b> la quatrième nuit.</div></div>
         <div><div class="jr-rappel-l">Dites le degré et sa conséquence</div><div class="jr-rappel-x">Le film est <b>assez</b> lent <b>pour que</b> la moitié de la salle <b>décroche</b>.</div></div>
         <div><div class="jr-rappel-l">Supposez, sans contredire personne</div><div class="jr-rappel-x"><b>Si</b> le budget <b>était</b> plus grand, je <b>proposerais</b> l'humour.</div></div>
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
     <h3 class="prod-tit">Présentez une œuvre à la classe</h3>
     <p class="prod-lead">Deux minutes environ, debout, sans lire vos notes mot à mot. Choisissez une œuvre que vous avez vue, lue ou entendue — un film, une série, une chanson, un livre, un spectacle. Résumez-la sans dévoiler la fin, donnez votre avis, appuyez-le sur un moment précis, et accordez un point à ceux qui pourraient penser autrement.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">De quoi il s'agit, en deux ou trois phrases</div><div class="plan-ex">« J'ai vu un film qui s'appelle Onze heures moins quart. Ça se passe dans une boulangerie de nuit, à Gatineau, sur huit nuits de travail. Je ne dirai pas la fin. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Votre avis, annoncé comme un avis, et le moment qui l'appuie</div><div class="plan-ex">« Ce qui m'a convaincue, c'est la quatrième nuit : il la laisse pétrir seule et il sort fumer. En dix secondes, on comprend qu'il lui fait confiance, et personne n'a eu besoin de le dire. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Ce que vous accordez, et ce que vous maintenez</div><div class="plan-ex">« Bien que le premier quart d'heure soit très lent, la deuxième heure tient sans effort. Si le film durait trois heures, je ne le recommanderais pas — mais il en dure moins de deux. »</div></div>
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
     <h3 class="prod-tit">Écrivez le compte rendu de la discussion</h3>
     <p class="prod-lead">De 10 à 14 phrases, en trois paragraphes. Le premier dit quelle œuvre a été discutée et ce qu'elle raconte. Le deuxième rapporte les deux avis — le vôtre et celui de la personne qui n'était pas d'accord —, chacun avec sa raison. Le troisième dit ce qui a été décidé et pourquoi. Un compte rendu qui ne garde que l'avis du gagnant n'est plus un compte rendu.</p>
     <div class="req">
       <div class="req-hd">Votre compte rendu doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le titre de l'œuvre et un résumé de deux phrases, sans la fin</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Votre avis, annoncé comme un avis, et le moment précis qui l'appuie</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>L'avis contraire, rapporté honnêtement, avec sa raison</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une concession : « bien que… soit… » ou « malgré… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une mise en relief : « ce qui… c'est… » ou « c'est… qui… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un connecteur qui annonce : quant à, en ce qui concerne</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un connecteur qui ramasse : en somme, par conséquent</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une décision, à la fin, et la raison qui l'a emportée</span></div>
       </div>
       <div class="req-note">Écrivez au registre standard ou soutenu : ce texte sera lu par des gens qui n'étaient pas là. Et citez entre guillemets seulement ce dont vous êtes sûr des mots.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">Les huit membres du comité social</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Compte rendu — choix de la sortie de fin d'année</span></div>
       <textarea id="peText" rows="12" aria-label="Votre compte rendu" data-min="10" data-max="14" oninput="peCount()" placeholder="Bonjour à tous,&#10;&#10;Le comité s'est réuni jeudi pour choisir…"></textarea>
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
    "Je nomme les pièces d'un spectacle : la première partie, le rappel, le tour de chant, la chute.",
    "Je distingue un goût, un avis et un argument.",
    "Je choisis le registre de langue que la situation demande.",
    "Je reconnais l'ironie quand quelqu'un dit le contraire de ce qu'il pense.",
    "Je nomme les procédés : ironie, sarcasme, caricature, burlesque, absurde, autodérision.",
    "Je reconnais une parole rapportée mot pour mot et une parole racontée.",
    "J'emploie une incise : « dit-elle », « ajoute-t-il », « reprend le gérant ».",
    "Je mets un mot en avant : c'est… qui, c'est… que, ce qui… c'est.",
    "Je repère le refrain, les couplets et les images d'une chanson.",
    "Je retrouve ce que reprennent « ils », « le », « en » et « y ».",
    "Je dis un degré et sa conséquence : tellement… que, trop… pour que.",
    "Je distingue « la musique, ça me calme » de « la musique de ce film ».",
    "Je sépare les faits des jugements dans une critique.",
    "J'accorde un point à l'autre avant de lui répondre.",
    "J'emploie « bien que » avec le subjonctif et « même si » avec l'indicatif.",
    "Je pose une hypothèse : si + imparfait, puis conditionnel.",
    "J'emploie quant à, autrement dit, en somme, par conséquent.",
    "Je peux présenter une œuvre à la classe en une minute trente.",
    "Je peux écrire un compte rendu qui garde les deux avis.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#0D7A6F">Je retiens des mots</span><span class="ctit" style="color:#0D7A6F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#0D7A6F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#0D7A6F;font-size:13px;margin:6px 0 4px">Les œuvres et les lieux</div>
     <textarea rows="2" placeholder="Ex. : une œuvre, un long métrage, un tour de chant, une salle de spectacle, la première partie, un rappel…"></textarea>
     <div style="font-weight:800;color:#0D7A6F;font-size:13px;margin:12px 0 4px">Ce qui fait rire</div>
     <textarea rows="2" placeholder="Ex. : un sketch, l'ironie, le sarcasme, une caricature, le burlesque, l'absurde, une chute…"></textarea>
     <div style="font-weight:800;color:#0D7A6F;font-size:13px;margin:12px 0 4px">La chanson</div>
     <textarea rows="2" placeholder="Ex. : un refrain, un couplet, une image, un vers, une auteure-compositrice…"></textarea>
     <div style="font-weight:800;color:#0D7A6F;font-size:13px;margin:12px 0 4px">Discuter et écrire</div>
     <textarea rows="2" placeholder="Ex. : une appréciation, un argument, une concession, une critique, un compte rendu, un registre de langue…"></textarea>
   </div>
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#0D7A6F">Autoévaluation</span><span class="ctit" style="color:#0D7A6F">Qu'est-ce que je suis capable de faire ?</span></div>
     <p class="lead">Pour chaque énoncé, choisissez : pas encore 😟, un peu 🙂, ou oui 😃.</p>
     ${SELF.map((s,i)=>`<div class="selfrow"><div class="self-txt">${s}</div><div class="self-opts">
        <button onclick="rate(${i},this)">😟</button><button onclick="rate(${i},this)">🙂</button><button onclick="rate(${i},this)">😃</button>
     </div></div>`).join('')}
     <div style="margin-top:16px"><button class="btn btn-pri" onclick="finishEval()">Terminer le module 🎉</button></div>
     <div id="evalDone" class="fb" aria-live="polite"></div>
   </div>`;
}
