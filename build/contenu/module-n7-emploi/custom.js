  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions, dans l'ordre voulu par le projet : le jeu de rôle
  // sert de répétition, la production orale est l'intention PO du programme
  // (« présenter un projet, une évaluation sommaire ou un problème à ses
  // collègues »), la production écrite est la première intention PE
  // (« écrire une note de service »), la lettre d'affaires — seconde
  // intention PE — étant offerte en variante à celles qui vont plus vite.
  // Seule la situation publique est côté client ; ce que sait le chef de
  // production joué par l'assistant vit dans server.py, scénario « projet ».
  const ROLE_CAS = [
    {id:'poste4', titre:'Le poste 4', txt:"Trois personnes sur cinq du poste d'emballage ont consulté pour le dos depuis mars. <b>Quinze jours ouvrables</b> d'absence, un poste en tâches allégées depuis onze semaines. Vous proposez une rotation gratuite et une table élévatrice dont vous n'avez pas encore le prix."},
    {id:'rotation', titre:"L'essai de rotation", txt:"Vous demandez d'essayer la rotation <b>dès lundi</b>, quatre heures d'emballage et quatre heures ailleurs. Ça ne coûte rien, mais ça oblige à refaire l'horaire de cinq personnes et un chef d'équipe s'y oppose."},
    {id:'soumission', titre:'La demande de soumission', txt:"Vous voulez écrire à <b>Équipements Sorel</b> pour obtenir un prix. Il vous faut l'autorisation, le nom de la personne qui signe, et l'accord sur les mots : une demande de soumission, jamais une commande."},
  ];
  const ROLE_SUJETS = ["Dire de quoi il s'agit, en une phrase, avant tout détail",
    "Donner au moins deux chiffres que vous avez comptés vous-même",
    "Nommer la cause, pas un coupable",
    "Dire ce que le problème coûte si on ne fait rien",
    "Proposer d'abord ce qui ne coûte rien",
    "Dire clairement ce que vous ne savez pas encore",
    "Demander une suite précise : une date, un document, un nom"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Défendez votre projet</span></div>
     <p class="lead">L'assistant joue <b>votre chef de production</b>. Il n'est pas contre vous, mais il a un budget, un horaire et cinq autres dossiers : il vous demandera vos chiffres, il objectera le coût, et il ne vous accordera une suite que si vous la demandez précisément. Vous le vouvoyez.</p>
     <div class="jr-grid">
       ${ROLE_CAS.map(c=>`
       <div class="jr-log">
         <div class="jr-log-h">${esc(c.titre)}</div>
         <div class="jr-log-a">${c.txt}</div>
       </div>`).join('')}
     </div>
     <div class="jr-sub">Les sept sujets à couvrir</div>
     <div class="jr-sujets">
       ${ROLE_SUJETS.map(s=>`<div class="jr-sujet"><span class="jr-box"></span>${esc(s)}</div>`).join('')}
     </div>
     <div class="jr-gram">
       <div class="jr-gram-t">Réutilisez ce que vous venez d'apprendre</div>
       Enchaînez avec des connecteurs :
       <span class='savoir-ex'><b>D'abord</b> le constat, <b>ensuite</b> la cause. <b>Par conséquent</b>, je propose deux choses.</span>
       Mettez en avant ce qui compte :
       <span class='savoir-ex'><b>Ce qui</b> use le dos, <b>c'est</b> de se pencher quatre-vingt-deux fois.</span>
       Dites l'ordre des choses :
       <span class='savoir-ex'>Quand nous <b>aurons reçu</b> le prix, nous pourrons décider.</span>
       Proposez sans imposer :
       <span class='savoir-ex'>Nous <b>pourrions</b> commencer la rotation le 22 septembre.</span>
       Demandez sans exiger :
       <span class='savoir-ex'>Je <b>voudrais</b> l'autorisation d'écrire au fournisseur.</span>
     </div>

     <div class="jr-sep"></div>
     <div class="jr-sub">Choisissez votre situation et votre rôle</div>
     <div class="jr-choix">
       <div class="jr-choix-l">Quel dossier ?</div>
       <div class="jr-opts" id="jrLogs">
         ${ROLE_CAS.map((c,i)=>`<button class="jr-opt${i===0?' on':''}" type="button" data-log="${c.id}" onclick="jrChoisir('log','${c.id}')">${esc(c.titre)}</button>`).join('')}
       </div>
       <div class="jr-choix-l">Vous jouez qui ?</div>
       <div class="jr-opts" id="jrRoles">
         <button class="jr-opt on" type="button" data-role="aicha" onclick="jrChoisir('role','aicha')">Celle qui présente</button>
         <button class="jr-opt" type="button" data-role="chef" onclick="jrChoisir('role','chef')">Le chef de production</button>
       </div>
       <div class="jr-choix-l">Comment ?</div>
       <div class="jr-opts" id="jrModes">
         <button class="jr-opt on" type="button" data-mode="texte" onclick="jrModeVoix(false)">✍️ Écrire</button>
         <button class="jr-opt" type="button" data-mode="voix" onclick="jrModeVoix(true)">🎤 Parler</button>
       </div>
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()" style="margin-top:14px">Commencer la rencontre</button>
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
     <h3 class="prod-tit">Présentez votre projet à vos collègues</h3>
     <p class="prod-lead">Vous avez quinze minutes à l'ordre du jour ; prenez-en deux. Présentez un problème de votre milieu de travail — le vrai, ou celui du poste 4 — avec les cinq parties, dans l'ordre. Vous vouvoyez la salle.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Le constat, avec deux chiffres</div><div class="plan-ex">« Depuis le mois de mars, trois personnes sur cinq du poste 4 ont consulté pour le dos. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">La cause, puis ce que ça coûte</div><div class="plan-ex">« Ce qui use le dos, c'est de se pencher quatre-vingt-deux fois. Par conséquent, quinze jours d'absence depuis mars. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Deux correctifs, le gratuit d'abord, et une date</div><div class="plan-ex">« Nous pourrions commencer la rotation le 22 septembre. Quand nous aurons reçu le prix de la table, nous déciderons du reste. »</div></div>
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
     <h3 class="prod-tit">Écrivez la note de service</h3>
     <p class="prod-lead">La présentation est faite ; il faut maintenant l'annoncer à l'équipe. Écrivez la note de service qui met la rotation à l'essai : de 8 à 12 phrases, avec ses six parties. Vous dites « vous » à vos collègues.</p>
     <div class="req">
       <div class="req-hd">Votre note doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Les quatre lignes d'en-tête : destinataires, expéditeur, date, objet</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un objet sans verbe conjugué, de six à dix mots</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une ou deux phrases de contexte, sans reproche</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce qui change, avec une date de début et une durée</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce que vous demandez au lecteur de faire, et avant quand</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Au moins un connecteur : par conséquent, en revanche, en somme</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une phrase passive : « il vous est demandé de… », « aucune modification n'est apportée à… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Votre signature : prénom, nom, fonction — sans formule de politesse</span></div>
       </div>
       <div class="req-note">Si vous allez plus vite que prévu, écrivez ensuite la <b>lettre d'affaires</b> au fournisseur, avec ses sept parties : lieu et date, vedette, objet, appel, trois paragraphes, salutation qui reprend l'appel, signature. Demandez une soumission, jamais une commande.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">Document</span><span class="mail-v">Meubles Rive-du-Nord — note de service</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">À vous de l'écrire — six à dix mots, sans verbe conjugué</span></div>
       <textarea id="peText" rows="10" aria-label="Votre note de service" data-min="8" data-max="12" oninput="peCount()" placeholder="DESTINATAIRES :&#10;EXPÉDITRICE :&#10;DATE :&#10;OBJET :&#10;&#10;À la réunion de production du…"></textarea>
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
    "Je nomme les cinq parties d'un projet : constat, cause, conséquence, correctif, échéance.",
    "Je lis un ordre du jour et je sais ce qu'on attend de moi avant la réunion.",
    "J'entends si une phrase continue ou si elle est finie, et je le fais entendre quand je parle.",
    "Je suis une présentation de projet de douze minutes sans perdre le fil.",
    "Je repère les connecteurs qui organisent un exposé : d'abord, par conséquent, en revanche, en somme.",
    "J'emploie le futur antérieur pour dire ce qui sera fini avant autre chose.",
    "Je reprends une idée sans la répéter : le, en, y, ce constat, cette démarche.",
    "Je présente un problème avec des chiffres que j'ai comptés moi-même.",
    "Je dis clairement ce que je ne sais pas encore, au lieu d'inventer un chiffre.",
    "Je mets en avant ce qui compte : « ce qui… c'est », « c'est… qui ».",
    "Je reconnais une phrase passive et je vois qui n'y est pas nommé.",
    "Je sais ce qu'est un programme de prévention et à quoi sert le droit de refus.",
    "J'écris une note de service avec ses six parties.",
    "J'écris une lettre d'affaires courantes avec ses sept parties et ses formules.",
    "J'emploie le subjonctif après « je souhaite que » et le conditionnel pour demander.",
    "Je peux présenter un projet ou un problème à mes collègues, en réunion.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Le projet et la réunion</div>
     <textarea rows="2" placeholder="Ex. : un projet, une évaluation sommaire, un ordre du jour, une réunion de production, le varia, un procès-verbal…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Présenter et enchaîner</div>
     <textarea rows="2" placeholder="Ex. : un échéancier, une étape, la mise en œuvre, un budget, d'abord, par conséquent, en revanche, en somme…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Le poste de travail</div>
     <textarea rows="2" placeholder="Ex. : la manutention, un poste de travail, un correctif, un programme de prévention, le droit de refus…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les écrits d'affaires</div>
     <textarea rows="2" placeholder="Ex. : une note de service, une lettre d'affaires, une soumission, un fournisseur, un accusé de réception, p. j., c. c…."></textarea>
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
