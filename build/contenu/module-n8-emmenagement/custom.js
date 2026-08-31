  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : la conversation de révision avec l'assistant, la
  // réclamation portée de vive voix au déménageur, puis la lettre écrite. Le
  // jeu de rôle vient en premier parce qu'il sert de répétition aux deux
  // autres.
  //
  // D'OÙ VIENNENT CES TÂCHES. La situation « Emménagement dans un nouveau
  // logement » du niveau 8 ne porte qu'**une** intention de communication :
  // s'informer sur les assurances (vol, responsabilité, incendie, dégâts),
  // en compréhension **et** en production **orales**. Le jeu de rôle et la
  // production orale en sortent directement. La lettre, elle, n'a aucune
  // intention derrière elle : elle vient des **attentes de fin de cours** du
  // niveau 8, qui demandent que l'adulte « rédige des lettres ou des
  // courriels d'affaires ayant des objectifs particuliers en s'assurant que
  // leur forme et leur contenu sont appropriés », qu'il « résume les propos
  // de son interlocuteur » et qu'il « négocie la solution d'un problème,
  // propose des compromis et donne son opinion en la justifiant à l'aide
  // d'arguments ». Sans cette note, un relecteur retirerait la tâche en la
  // croyant hors programme.
  //
  // Seule la situation publique est côté client ; ce que sait l'experte
  // jouée par l'assistant vit dans server.py, scénario « sinistre ».
  const ROLE_CAS = [
    {id:'vaisselier', titre:'Le vaisselier refusé', txt:"Votre assureur a rendu sa décision : les livres et les albums sont acceptés pour <b>neuf cent quarante dollars</b> moins la franchise de cinq cents, la rampe est refusée parce qu'elle appartient au bâtiment, et le <b>vaisselier est refusé</b> en vertu d'une clause d'exclusion. Vous appelez l'experte en sinistre pour contester ce seul troisième point."},
    {id:'clause', titre:"« Pendant leur transport »", txt:"La clause 7.3 exclut « les dommages causés aux biens meubles <b>pendant leur transport</b> par un déménageur professionnel ». Or l'inventaire signé à <b>huit heures</b> ne note aucun dommage, et votre photographie horodatée à <b>onze heures vingt-deux</b> montre la fente. Entre les deux, il n'y a eu que le <b>portage</b> dans un escalier extérieur en colimaçon."},
    {id:'compromis', titre:'Le chiffre et la contrepartie', txt:"Un ébéniste de la rue Bonaventure a examiné la fente lundi et l'a évaluée par écrit ; vous avez aussi trois annonces de meubles comparables, datées de la semaine dernière. Vous voulez proposer <b>huit cent cinquante dollars</b>, soit la moitié de la valeur estimée, <b>contre votre renonciation</b> à toute autre réclamation dans ce dossier. Vous savez aussi que la <b>subrogation</b> permettrait à l'assureur de se retourner contre le transporteur."},
  ];
  const ROLE_SUJETS = ["Annoncer en une phrase l'objet de votre appel et votre numéro de dossier",
    "Découper : reprendre les trois éléments l'un après l'autre",
    "Accepter tout de suite, à voix haute, ce que vous ne contestez pas",
    "Demander la clause exacte, puis la faire relire mot pour mot",
    "Concéder, puis retourner : certes… mais · bien que… soit · or",
    "Appuyer chaque affirmation sur une pièce datée et numérotée",
    "Employer une hypothèse irréelle : si on m'avait… j'aurais…",
    "Mettre en relief votre demande : ce que je conteste, c'est…",
    "Proposer un chiffre justifié et une contrepartie",
    "Demander la décision par écrit, avec sa clause, et un délai"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">La conversation de révision</span></div>
     <p class="lead">L'assistant joue <b>l'experte en sinistre</b> qui vient de refuser une partie de votre réclamation. Elle n'est ni votre adversaire ni votre alliée : elle applique un texte, elle a la possibilité — non l'obligation — de porter votre cas au réviseur, et elle ne le fera que si vous lui en donnez les moyens. Elle ne cite une clause que si on la lui demande.</p>
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
         <button class="jr-opt on" type="button" data-role="assuree" onclick="jrChoisir('role','assuree')">La personne assurée</button>
         <button class="jr-opt" type="button" data-role="experte" onclick="jrChoisir('role','experte')">L'experte en sinistre</button>
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
         <div class="jr-bande-t">Les dix sujets à couvrir</div>
         <p class="jr-bande-p">${ROLE_SUJETS.map((s,i)=>i?s.charAt(0).toLowerCase()+s.slice(1):s).join(', ')}.</p>
       </div>
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()">Commencer l'appel</button>
     </div>
     <div class="jr-rappel">
       <div class="jr-rappel-t">Réutilisez ce que vous venez d'apprendre</div>
       <div class="jr-rappel-g">
         <div><div class="jr-rappel-l">Découpez la conversation</div><div class="jr-rappel-x"><b>Reprenons</b> les trois points l'un après l'autre.</div></div>
         <div><div class="jr-rappel-l">Concédez, puis retournez</div><div class="jr-rappel-x"><b>Certes</b> la clause existe. <b>Or</b> elle parle du transport, et le meuble a été fendu dans l'escalier.</div></div>
         <div><div class="jr-rappel-l">Faites préciser</div><div class="jr-rappel-x"><b>Sur quelle clause</b> vous appuyez-vous ? Pouvez-vous me la relire ? Je veux les mots exacts.</div></div>
         <div><div class="jr-rappel-l">Dites ce qui aurait pu être évité</div><div class="jr-rappel-x"><b>Si on m'avait offert</b> une déclaration de valeur, j'en <b>aurais fait</b> une.</div></div>
         <div><div class="jr-rappel-l">Mettez en relief ce qui compte</div><div class="jr-rappel-x"><b>Ce que je conteste, c'est</b> le refus complet, <b>pas</b> votre évaluation.</div></div>
         <div><div class="jr-rappel-l">Résumez pour vérifier</div><div class="jr-rappel-x"><b>Je résume, pour être certaine :</b> vous soumettez le troisième point au réviseur, et j'envoie les quatre pièces aujourd'hui.</div></div>
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
     <h3 class="prod-tit">Portez votre réclamation au déménageur, de vive voix</h3>
     <p class="prod-lead">Environ deux minutes. Ce n'est plus l'assureur : c'est l'entreprise qui a causé le dommage, et qui a un contrat dans les mains. Vous n'appelez pas pour vous plaindre, vous appelez pour poser des faits, concéder ce qui doit l'être et annoncer ce que vous allez faire. Le ton reste posé du début à la fin — c'est la moitié de l'exercice.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Annoncez l'objet de l'appel en une phrase, et combien de points vous avez</div><div class="plan-ex">« Je vous appelle au sujet du déménagement du 4. J'ai trois points, et je vous les donne dans l'ordre. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Les faits, avec une heure et un montant — et le point que vous concédez</div><div class="plan-ex">« L'inventaire a été signé à huit heures sans aucune mention. La photo est datée de onze heures vingt-deux. Les boîtes du balcon, je vous l'accorde : personne ne les surveillait, et je ne vous les réclame pas. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Ce que vous demandez, mis en relief, et ce que vous ferez ensuite</div><div class="plan-ex">« Ce que je demande, c'est le vaisselier. Si une déclaration de valeur m'avait été offerte, nous discuterions du montant et non du principe. Je vous envoie une lettre cette semaine avec les pièces. »</div></div>
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
     <h3 class="prod-tit">Écrivez votre demande de révision</h3>
     <p class="prod-lead">De 12 à 16 phrases, en cinq paragraphes courts. Vous avez lu le modèle à l'exercice 6 du défi 2 : gardez les sept fonctions dans le même ordre, et n'en contestez <b>qu'un seul</b> point. Le ton reste posé du début à la fin — l'indignation se lit comme du bruit et donne une raison de refuser.</p>
     <div class="req">
       <div class="req-hd">Votre lettre doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un objet portant le numéro de dossier</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un paragraphe qui dit ce que vous acceptez, avant tout le reste</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une phrase qui énonce le point contesté — un seul</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une concession : certes… · bien que… soit…</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un retournement par « or », suivi du fait qui décide</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Deux pièces datées et numérotées, citées dans le texte</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une hypothèse irréelle : si on m'avait…, j'aurais…</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une phrase emphatique : ce que je conteste, c'est…</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une proposition chiffrée, avec une contrepartie</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une demande de décision écrite, avec sa clause, et une formule soutenue</span></div>
       </div>
       <div class="req-note">Tenez le vouvoiement et le registre soutenu du début à la fin. N'écrivez rien que vos pièces ne puissent confirmer, et n'ajoutez aucune demande que vous n'avez pas formulée au téléphone.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">Mutuelle du Saint-Maurice — service des sinistres</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Demande de révision — dossier 8-4-1-7-2-6</span></div>
       <textarea id="peText" rows="14" aria-label="Votre lettre" data-min="12" data-max="16" oninput="peCount()" placeholder="Madame,&#10;&#10;La présente fait suite à votre lettre de décision reçue le 12…"></textarea>
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
    "Je pose les trois gestes du premier jour : la copie signée, les photos datées, rien d'accepté de vive voix.",
    "Je sais qu'un bien réparé ou jeté avant l'examen de l'expert n'est plus indemnisable.",
    "Je nomme les trois protections d'une police de locataire et je sais ce que chacune paie.",
    "Je calcule ce que je toucherai : le dommage retenu, moins la franchise, une fois par sinistre.",
    "Je distingue la valeur à neuf de la valeur au jour du sinistre, et je sais laquelle j'ai.",
    "Je repère une sous-limite et je sais qu'il faut un avenant pour la dépasser.",
    "Je lis les exclusions avant les protections.",
    "Je fais clarifier un mot une seule fois, sur le mot qui décide de quelque chose.",
    "Je résume avec mes propres mots pour vérifier que j'ai bien compris.",
    "Je découpe une conversation longue en points annoncés, et je mène par là.",
    "J'emploie le subjonctif après ses déclencheurs : il faut que, j'aimerais que, bien que.",
    "Je sais que « bien que » veut le subjonctif et « même si » l'indicatif.",
    "Je retrouve à quoi renvoient « dont », « auquel » et « sur laquelle » dans une phrase longue.",
    "Je repère un passif qui cache celui qui agit, et je demande par qui.",
    "J'exige la clause exacte de tout refus, et je la fais relire mot pour mot.",
    "Je concède d'abord ce qui est juste, à voix haute, avant de contester le reste.",
    "Je dis ce qui aurait pu être évité : si on m'avait…, j'aurais…",
    "Je mets en relief ma demande : ce que je conteste, c'est…",
    "Je propose un chiffre justifié par une pièce extérieure, avec une contrepartie.",
    "J'écris une demande de révision en sept fonctions, et je n'y conteste qu'un seul point.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#1D6B8F">Je retiens des mots</span><span class="ctit" style="color:#1D6B8F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#1D6B8F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:6px 0 4px">Le jour du déménagement</div>
     <textarea rows="2" placeholder="Ex. : un inventaire, un connaissement, une déclaration de valeur, le portage, la garde du bien…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">Le contrat d'assurance</div>
     <textarea rows="2" placeholder="Ex. : une prime, une franchise, un plafond, une sous-limite, un avenant, une exclusion…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">Le sinistre et la réclamation</div>
     <textarea rows="2" placeholder="Ex. : déclarer, un dégât d'eau, un expert en sinistre, le dommage retenu, la subrogation…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">Défendre son point de vue</div>
     <textarea rows="2" placeholder="Ex. : certes… mais, or, il n'en demeure pas moins que, ce que je conteste c'est, une mise en demeure…"></textarea>
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
