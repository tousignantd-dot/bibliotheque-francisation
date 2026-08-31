  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : la conversation avec l'assistant, l'exposé des deux
  // produits, puis la lettre de contestation. Le jeu de rôle vient en
  // premier parce qu'il sert de répétition aux deux autres.
  //
  // D'où viennent ces trois tâches. Les trois intentions de la situation
  // « Transactions bancaires », au niveau 7, sont « s'informer sur des
  // produits financiers liés au crédit ou à l'épargne », en compréhension
  // orale, en production orale et en compréhension écrite. Le jeu de rôle et
  // la production orale portent donc directement l'intention de production
  // orale. La production **écrite**, elle, vient des attentes de fin de
  // cours du niveau, qui sont productives — « l'adulte rédige un texte
  // formel simple pour transmettre à différents destinataires un message
  // parfois complexe », « à l'aide d'un modèle, il rédige une lettre de
  // réclamation ». C'est écrit ici et dans le manifeste pour que la tâche ne
  // passe pas pour une invention hors programme.
  //
  // Seule la situation publique est ici ; ce que sait le conseiller joué par
  // l'assistant vit dans server.py, scénario « produitfinancier ».
  const ROLE_CAS = [
    {id:'marge', titre:'La dette de carte', txt:"Vous devez <b>9 412 $</b> sur une carte à <b>19,90 %</b> et vous payez le minimum depuis trois ans. On vous propose une <b>marge à 9,45 %</b> ou un <b>prêt personnel à 11,20 %</b> sur quatre-vingts versements. Vous voulez comprendre lequel vous coûte le moins, et surtout lequel vous finirez de payer."},
    {id:'celi', titre:"Les six mille deux cents dollars", txt:"Il y a <b>6 200 $</b> dans votre compte chèque, pour un projet qui a une date : le cégep de votre fille, <b>dans deux ans</b>. On vous parle de CELI, de REER et de dépôt à terme. Vous voulez savoir lequel convient à un projet aussi court, et jusqu'où cet argent est protégé."},
    {id:'operation', titre:"L'opération de 780 $", txt:"Une opération de <b>780 $</b> apparaît sur votre relevé, le <b>14</b>, chez un commerçant que vous ne connaissez pas. Votre carte n'a jamais quitté votre portefeuille. Vous voulez faire bloquer la carte, faire retirer le montant, et repartir avec un <b>numéro de dossier</b>."},
  ];
  const ROLE_SUJETS = ["Dire d'entrée ce que vous voulez savoir, avant d'entrer dans les détails",
    "Demander le taux, et demander s'il est fixe ou variable",
    "Reprendre le mot que vous n'avez pas compris : « quand vous dites…, ça veut dire quoi ? »",
    "Reformuler pour vérifier : « donc si je comprends bien… »",
    "Demander un exemple chiffré appliqué à votre montant à vous",
    "Faire répéter un chiffre plutôt que de faire oui de la tête",
    "Demander ce qui arrive si vous remboursez plus vite, ou si vous retirez plus tôt",
    "Repartir avec un écrit, et ne rien signer pendant le rendez-vous"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Informez-vous auprès d'un conseiller</span></div>
     <p class="lead">L'assistant joue <b>un conseiller en finances personnelles</b> : compétent, pressé, et habitué à ce que les gens hochent la tête sans comprendre. Il ne vous cache rien, mais il ne devine pas ce que vous n'avez pas saisi. À vous de le faire ralentir, de reprendre les mots qui vous échappent et de repartir avec un papier plutôt qu'une signature. Vouvoyez-le du début à la fin.</p>
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
         <button class="jr-opt on" type="button" data-role="marlene" onclick="jrChoisir('role','marlene')">La cliente qui vient s'informer</button>
         <button class="jr-opt" type="button" data-role="conseiller" onclick="jrChoisir('role','conseiller')">Le conseiller de la caisse</button>
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
         <div><div class="jr-rappel-l">Demandez au conditionnel</div><div class="jr-rappel-x"><b>Pourriez-vous</b> me le mettre sur un papier ? · Sur mille dollars, ça <b>ferait</b> combien ?</div></div>
         <div><div class="jr-rappel-l">Reprenez le mot qui vous a échappé</div><div class="jr-rappel-x">Quand vous dites <b>« capitalisé »</b>, ça veut dire quoi exactement ?</div></div>
         <div><div class="jr-rappel-l">Vérifiez en reformulant</div><div class="jr-rappel-x"><b>Donc si je comprends bien</b>, je ne paie de l'intérêt <b>que</b> sur ce que je prends ?</div></div>
         <div><div class="jr-rappel-l">Comparez avec des chiffres</div><div class="jr-rappel-x">La marge coûte <b>moins cher que</b> la carte, <b>tandis que</b> le prêt, lui, se termine.</div></div>
         <div><div class="jr-rappel-l">Mettez en avant ce qui compte</div><div class="jr-rappel-x"><b>Ce que</b> je veux savoir, <b>c'est</b> dans combien de temps j'aurai fini de payer.</div></div>
         <div><div class="jr-rappel-l">Posez votre condition au subjonctif</div><div class="jr-rappel-x">J'accepte, <b>à condition que</b> le taux <b>reste</b> fixe jusqu'à la fin.</div></div>
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
     <h3 class="prod-tit">Deux produits, deux colonnes : exposez, puis décidez</h3>
     <p class="prod-lead">Quelqu'un de votre entourage vous demande ce que vous avez décidé. Choisissez deux produits du module — la marge et le prêt, ou le dépôt à terme et le compte d'épargne — et exposez-les en 90 secondes environ : annoncez-les, donnez pour chacun deux avantages et deux inconvénients avec un chiffre à l'appui, comparez-les, puis dites ce que vous décidez et à quelle condition vous changeriez d'avis.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Les deux produits, annoncés</div><div class="plan-ex">« J'ai deux façons de régler la carte : une marge de crédit à 9,45 % ou un prêt personnel à 11,20 % sur quatre-vingts versements. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Deux avantages, deux inconvénients, avec des chiffres</div><div class="plan-ex">« La marge coûte moins cher et je ne paie que sur ce que je prends ; par contre, rien ne m'oblige à la finir. Le prêt coûte un peu plus, mais il se termine à une date écrite, et il n'y a aucune pénalité si je rembourse plus vite. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">La comparaison, puis la décision datée</div><div class="plan-ex">« C'est d'autant plus difficile que les deux se défendent. Je prends le prêt, parce que je n'ai jamais remboursé une marge de ma vie ; je reverrai la question le jour où la carte sera à zéro. »</div></div>
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
     <h3 class="prod-tit">Écrivez la lettre qui conteste l'opération de 780 $</h3>
     <p class="prod-lead">Trente jours ont passé depuis votre appel et le montant est toujours sur votre relevé. Écrivez une lettre de 10 à 14 phrases, en <b>trois paragraphes</b> : d'abord ce qui s'est passé et quand, ensuite les faits qui appuient votre contestation, enfin ce que vous demandez et pour quelle date. Un objet qui se comprend sans ouvrir la lettre.</p>
     <div class="req">
       <div class="req-hd">Votre lettre doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un objet court, avec le numéro de dossier et le montant</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une formule d'appel, et une salutation fermée à la fin</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Trois paragraphes séparés, un par idée, liés par des connecteurs</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>La date de l'opération, celle de l'appel et le nom de la personne</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Deux faits qui appuient : la carte en votre possession, le commerçant inconnu</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une phrase emphatique : « Ce que je conteste, c'est… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une demande au subjonctif : « Je demande que le montant soit… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une date de réponse demandée, jamais un souhait</span></div>
       </div>
       <div class="req-note">N'écrivez pas ce que vous pensez du service : écrivez ce qui s'est passé, ce que vous avez déjà fait, et ce que vous demandez. Une lettre qui s'en tient aux dates, aux montants et à un numéro de dossier est celle qui obtient une réponse écrite — et c'est l'écrit qui compte.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">securite.cartes@norlande.example</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">À vous de le trouver — court, et sans phrase complète</span></div>
       <textarea id="peText" rows="10" aria-label="Votre lettre" data-min="10" data-max="14" oninput="peCount()" placeholder="Madame, Monsieur,&#10;&#10;Le 14 mars, une opération de 780 $ que je n'ai pas faite est apparue sur mon relevé…"></textarea>
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
    "Je trouve sur un relevé le solde, le paiement minimum, le taux et la date d'échéance.",
    "Je sais que le paiement minimum garde le compte en règle sans rembourser la dette.",
    "Je sais qu'un taux annoncé est toujours annuel, jamais mensuel.",
    "Je dis quel mot je n'ai pas compris au lieu de faire oui de la tête.",
    "Je reformule ce qu'on vient de me dire pour vérifier que j'ai bien compris.",
    "Je demande un exemple chiffré appliqué à mon propre montant.",
    "Je demande au conditionnel : pourriez-vous, je voudrais, ça ferait.",
    "Je compare deux produits avec plus… que, moins… que, ne… que, d'autant plus… que.",
    "Je sais ce qu'est une marge de crédit et en quoi elle diffère d'un prêt personnel.",
    "Je sais que mon dossier de crédit est gratuit et que le consulter ne me nuit pas.",
    "Je distingue un abri fiscal — CELI, REER — d'un placement.",
    "Je sais jusqu'à quel montant mes dépôts sont protégés, et par qui.",
    "Je reconnais une phrase passive et j'accorde le participe avec le sujet.",
    "J'organise une comparaison avec tandis que, en revanche, de plus, en somme.",
    "Je sais quoi faire, et dans quel ordre, devant une opération que je n'ai pas faite.",
    "J'écris une lettre de réclamation en trois paragraphes, avec une date de réponse demandée.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Les mots du relevé</div>
     <textarea rows="2" placeholder="Ex. : un relevé de compte, le solde, le paiement minimum, les frais de crédit…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les mots de l'emprunt</div>
     <textarea rows="2" placeholder="Ex. : le taux d'intérêt, une marge de crédit, un prêt personnel, la cote de crédit…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les mots de l'épargne</div>
     <textarea rows="2" placeholder="Ex. : un placement, le rendement, un dépôt à terme, l'assurance-dépôts…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les mots de la contestation</div>
     <textarea rows="2" placeholder="Ex. : une opération non autorisée, une contestation, l'hameçonnage, un numéro de dossier…"></textarea>
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
