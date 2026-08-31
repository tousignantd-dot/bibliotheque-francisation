  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : l'appel de contestation avec l'assistant, le récit
  // oral d'une décision subie, puis la demande de révision écrite. Le jeu de
  // rôle vient en premier parce qu'il sert de répétition aux deux autres.
  //
  // D'OÙ VIENNENT CES TÂCHES. La situation « Problèmes reliés à l'habitation »
  // du niveau 8 ne porte qu'**une** intention, en compréhension et en
  // production orales : échanger avec son assureur à l'occasion d'une
  // réclamation par téléphone. Le jeu de rôle et la production orale en
  // sortent directement. La lettre, elle, vient des **attentes de fin de
  // cours** du niveau 8 : « il rédige des lettres ou des courriels d'affaires
  // ayant des objectifs particuliers en s'assurant que leur forme et leur
  // contenu sont appropriés » et « il résume les propos de son
  // interlocuteur ». Sans cette note, un relecteur retirerait la tâche en la
  // croyant hors programme.
  //
  // Seule la situation publique est côté client ; ce que sait l'agente jouée
  // par l'assistant vit dans server.py, scénario « refusassurance ».
  const ROLE_CAS = [
    {id:'refus', titre:'Le refus, et son motif', txt:"Votre réclamation pour un <b>refoulement d'égout</b> a été refusée par écrit. Motif retenu : <b>défaut d'entretien du drain de plancher</b>, exclusion de l'article 7.3 du contrat. Les dommages ont été évalués à <b>19 400 $</b>, franchise de 1 000 $. Vous téléphonez au service du règlement des sinistres."},
    {id:'contradiction', titre:"Deux documents, deux tuyaux", txt:"La <b>lettre</b> parle du drain de <b>plancher</b> ; le <b>rapport d'expertise</b> du même assureur, lui, décrit une obstruction du drain de <b>fondation</b>. Ce ne sont pas les mêmes tuyaux, l'un est dedans et l'autre dehors, et personne chez l'assureur ne l'a remarqué avant vous."},
    {id:'contrexpertise', titre:"La contre-expertise", txt:"Vous avez payé <b>600 $</b> un expert en sinistre public. Onze pages, vingt-deux photographies datées, une caméra passée dans le drain de fondation : <b>aucune racine, aucun affaissement, écoulement libre</b>. Vous avez aussi la <b>facture acquittée</b> du nettoyage du drain de plancher, datée du 3 mai."},
  ];
  const ROLE_SUJETS = ["Vous nommer, donner le numéro du dossier et la date du sinistre",
    "Annoncer combien de points vous allez présenter, puis vous y tenir",
    "Citer le motif du refus dans les mots exacts de la lettre",
    "Opposer un fait daté et vérifiable, avec la pièce qui l'appuie",
    "Concéder ce qui est vrai : certes…, mais… · il n'en reste pas moins que…",
    "Dérouler l'hypothèse irréelle : si… avait été…, … se serait produit",
    "Demander trois choses précises, dont une réponse écrite et motivée",
    "Demander le délai, et le répéter avant de raccrocher"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">L'appel qui conteste</span></div>
     <p class="lead">L'assistant joue <b>l'agente au règlement des sinistres</b>. Elle est polie, elle connaît son dossier, et elle ne décide rien : tout ce qu'elle peut faire, c'est inscrire quelque chose au registre — encore faut-il que ce soit inscriptible. Elle ne s'énervera pas et ne cédera pas non plus ; ce qu'elle attend, ce sont des faits datés et une demande précise.</p>
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
         <button class="jr-opt on" type="button" data-role="assuree" onclick="jrChoisir('role','assuree')">La personne qui conteste</button>
         <button class="jr-opt" type="button" data-role="agente" onclick="jrChoisir('role','agente')">L'agente au règlement des sinistres</button>
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
         <div><div class="jr-rappel-l">Concédez, puis avancez</div><div class="jr-rappel-x"><b>Certes</b>, ce n'est pas vous qui avez rendu la décision ; <b>il n'en reste pas moins que</b> c'est à vous que je peux parler.</div></div>
         <div><div class="jr-rappel-l">Déroulez l'hypothèse</div><div class="jr-rappel-x"><b>Si</b> le drain <b>avait été</b> bouché depuis des années, l'eau <b>serait remontée</b> bien avant.</div></div>
         <div><div class="jr-rappel-l">Mettez en avant ce que vous contestez</div><div class="jr-rappel-x"><b>Ce que je conteste, c'est</b> le motif, non le montant.</div></div>
         <div><div class="jr-rappel-l">Demandez au subjonctif</div><div class="jr-rappel-x">Je demande <b>que</b> le dossier <b>soit</b> rouvert et <b>qu'</b>une réponse motivée me <b>parvienne</b> par écrit.</div></div>
         <div><div class="jr-rappel-l">Fixez l'ordre des choses</div><div class="jr-rappel-x"><b>Quand</b> vous <b>aurez reçu</b> ma lettre, le délai de soixante jours commencera à courir.</div></div>
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
     <h3 class="prod-tit">Racontez une décision que vous avez trouvée injuste</h3>
     <p class="prod-lead">Deux minutes environ, sans lire vos notes mot à mot. Une décision qu'on a prise à votre place — un refus, un montant, un délai, un dossier fermé — ici ou dans votre pays. Ne racontez pas votre colère : racontez les faits dans l'ordre, et dites ce que vous avez fait ensuite. C'est l'exercice qui prépare l'appel et la lettre.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Annoncez en une phrase de quoi vous allez parler, avec une date</div><div class="plan-ex">« Je vais vous parler d'un refus que j'ai reçu au mois d'octobre, après une inondation chez moi. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Ce qui s'était passé avant, ce qui s'est passé, et le motif — avec un chiffre</div><div class="plan-ex">« Le drain avait été nettoyé cinq mois plus tôt. L'orage a duré trois heures et l'eau est montée de quinze centimètres. On m'a répondu : défaut d'entretien. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Ce que vous auriez fait autrement, puis la démarche que vous avez entreprise</div><div class="plan-ex">« Si j'avais su qu'il fallait tout écrire, j'aurais envoyé la facture le premier jour. Depuis, je garde une copie de tout ce que j'envoie. »</div></div>
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
     <h3 class="prod-tit">Écrivez la demande de révision</h3>
     <p class="prod-lead">De 12 à 16 phrases. Ce n'est pas une lettre de plainte : c'est une demande adressée à une entreprise pour qu'elle réexamine une décision, en lui donnant des raisons qu'elle n'avait pas. Rappelez le dossier en une ligne, citez le motif dans ses mots, concédez ce qui est vrai, opposez des faits datés avec leurs pièces, puis demandez trois choses précises. Rien d'autre — ni votre semaine, ni ce que vous pensez de l'expert.</p>
     <div class="req">
       <div class="req-hd">Votre lettre doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le numéro du dossier, la date du sinistre et celle de la décision</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une phrase qui dit ce que la lettre est : une demande de révision</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le motif cité entre guillemets, après deux points</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une concession : certes… ; il n'en reste pas moins que…</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Deux faits datés, chacun avec la pièce qui l'appuie</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une hypothèse irréelle : si… avait été…, … se serait produit</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Trois demandes au subjonctif : que le dossier soit… que… et que…</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un rappel du délai et un numéro de téléphone</span></div>
       </div>
       <div class="req-note">Tenez le vouvoiement et le registre soutenu du début à la fin. N'écrivez aucun fait qu'une pièce jointe ne puisse confirmer, et ne menacez de rien : le délai de soixante jours suffit à faire avancer un dossier.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">Mutuelle Saint-Maurice — service du traitement des plaintes</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Demande de révision — réclamation 2026-41837, sinistre du 14 septembre 2026, décision du 12 octobre 2026</span></div>
       <textarea id="peText" rows="14" aria-label="Votre lettre" data-min="12" data-max="16" oninput="peCount()" placeholder="Madame, Monsieur,&#10;&#10;Je vous adresse par la présente une demande de révision de la décision rendue le…"></textarea>
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
    "Je distingue être couvert et être indemnisé : une exclusion peut s'appliquer malgré la protection.",
    "Je demande le rapport d'expertise complet, et non le résumé de la lettre.",
    "J'entends ce qu'une voix ajoute aux mots : la surprise, l'incompréhension, la volonté.",
    "Je raconte au plus-que-parfait ce qui s'était passé avant le sinistre.",
    "Je distingue dans un rapport ce qui a été vu, ce qui a été dit et ce qui est déduit.",
    "Je reconnais « il appert que » et « laisse supposer » comme des déductions.",
    "Je retrouve à quoi renvoient « dont », « auquel » et « sur laquelle » dans une phrase longue.",
    "Devant un passif, je demande « par qui ? » — et j'écris moi-même à la voix active.",
    "Je repère dans une lettre de refus la disposition invoquée et le paragraphe des recours.",
    "Je concède avant d'avancer : certes…, mais… · bien que… soit… · même si… est…",
    "J'emploie l'hypothèse irréelle : si… avait été…, … se serait produit.",
    "J'ajoute le fait qui montre que la conséquence ne s'est pas produite.",
    "Je suis un exposé en repérant son plan, ses étapes et ce qui est dit deux fois.",
    "Je connais les quatre portes du recours et l'ordre dans lequel on y frappe.",
    "Je ne confonds pas l'Autorité des marchés financiers et le Tribunal administratif du logement.",
    "J'emploie le subjonctif après « je demande que » et « afin que ».",
    "Je mets en avant l'essentiel : ce que je conteste, c'est… · c'est… que…",
    "J'écris une demande de révision : trois dates, le motif cité, des faits, trois demandes.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#1D6B8F">Je retiens des mots</span><span class="ctit" style="color:#1D6B8F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#1D6B8F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:6px 0 4px">Le sinistre</div>
     <textarea rows="2" placeholder="Ex. : un refoulement d'égout, un dégât d'eau, une ligne de mouillure, un sous-sol fini, un drain de plancher…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">Le contrat d'assurance</div>
     <textarea rows="2" placeholder="Ex. : un avenant, une franchise, une exclusion, une garantie, le défaut d'entretien…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">L'expertise</div>
     <textarea rows="2" placeholder="Ex. : un expert en sinistre, un constat, une déduction, une contre-expertise, une facture acquittée…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">Le recours</div>
     <textarea rows="2" placeholder="Ex. : une demande de révision, une réponse finale, un transfert de dossier, une décision motivée, la conciliation…"></textarea>
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
