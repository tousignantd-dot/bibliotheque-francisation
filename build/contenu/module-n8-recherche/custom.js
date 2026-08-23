  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : l'entrevue devant le comité avec l'assistant, le récit
  // oral d'une décision prise seul, puis le courriel de suivi. Le jeu de rôle
  // vient en premier parce qu'il sert de répétition aux deux autres.
  //
  // D'OÙ VIENNENT CES TÂCHES. La situation « Recherche d'emploi » du niveau 8
  // ne porte que trois intentions, et **aucune** de production écrite :
  // participer à une entrevue de sélection comportant plusieurs étapes
  // (comprise et produite), et s'informer sur une entreprise ou sur un emploi
  // (à l'oral et à l'écrit). Le jeu de rôle et la production orale sortent
  // donc directement de la première intention. Le courriel, lui, vient des
  // **attentes de fin de cours** du niveau 8 : « il rédige des lettres ou des
  // courriels d'affaires ayant des objectifs particuliers en s'assurant que
  // leur forme et leur contenu sont appropriés » et « il résume les propos de
  // son interlocuteur ». Sans cette note, un relecteur retirerait la tâche en
  // la croyant hors programme.
  //
  // Seule la situation publique est côté client ; ce que sait le comité joué
  // par l'assistant vit dans server.py, scénario « selection ».
  const ROLE_CAS = [
    {id:'superviseure', titre:'Le poste de superviseure', txt:"Vous êtes à la <b>troisième et dernière étape</b> : l'entrevue individuelle devant un comité de deux personnes. Vous avez réussi l'examen écrit et l'entrevue de groupe. Le poste est <b>superviseure ou superviseur de production, quart de soir</b>, dans une usine de deux cent dix employés. L'équipe du soir compte sept personnes sur seize prévues."},
    {id:'parcours', titre:"Onze ans qui ne comptent pas", txt:"Votre expérience de supervision a été acquise <b>à l'étranger</b>, et l'employeur ne sait pas comment la peser. Ici, vous occupez depuis cinq ans un poste d'exécution. L'annonce exige « cinq ans de supervision <b>ou toute expérience jugée équivalente</b> ». Personne ne vous posera la question directement."},
    {id:'echelon', titre:"L'échelon qui n'est pas affiché", txt:"L'échelle salariale compte <b>six échelons</b> et n'est communiquée à personne avant l'entrevue finale. Le comité a l'habitude de proposer le deuxième à quelqu'un qui vient de l'externe. Rien ne l'oblige à s'y tenir, et le directeur l'a dit publiquement : « on n'embauche pas obligatoirement au premier »."},
  ];
  const ROLE_SUJETS = ["Vous présenter en une phrase, puis laisser le comité mener",
    "Répondre par un exemple daté et chiffré, jamais par une qualité",
    "Nommer vous-même l'objection qu'on ne vous pose pas",
    "Raconter une décision difficile, ce qu'elle a coûté, la règle qui en est sortie",
    "Employer une hypothèse irréelle : si j'avais…, j'aurais…",
    "Concéder avant d'avancer : certes…, mais… · bien que… soit…",
    "Reconnaître une question qui porte sur un motif interdit, sans vous fâcher",
    "Demander un échelon en offrant une contrepartie datée et mesurable"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">L'entrevue devant le comité</span></div>
     <p class="lead">L'assistant joue <b>le directeur de la production</b>, qui mène l'entrevue avec la conseillère en acquisition de talents. Il est direct, il ne vous facilite rien, et il ne se contente pas d'une qualité annoncée : il redemande un exemple tant qu'il n'en a pas eu un. C'est aussi lui qui laissera passer, à un moment, une question qu'il n'a pas le droit de poser.</p>
     <div class="jr-grid">
       ${ROLE_CAS.map(c=>`
       <div class="jr-log">
         <div class="jr-log-h">${esc(c.titre)}</div>
         <div class="jr-log-a">${c.txt}</div>
       </div>`).join('')}
     </div>
     <div class="jr-sub">Les huit sujets à couvrir</div>
     <div class="jr-sujets">
       ${ROLE_SUJETS.map(s=>`<div class="jr-sujet"><span class="jr-box"></span>${esc(s)}</div>`).join('')}
     </div>
     <div class="jr-gram">
       <div class="jr-gram-t">Réutilisez ce que vous venez d'apprendre</div>
       Concédez, puis avancez :
       <span class='savoir-ex'><b>Certes</b> cette expérience a été acquise ailleurs, <b>mais</b> elle porte sur vingt-deux personnes.</span>
       Dites ce que vous feriez autrement :
       <span class='savoir-ex'><b>Si j'avais eu</b> les données de production, j'<b>aurais arrêté</b> la ligne plus tôt.</span>
       Mettez en avant ce qui compte :
       <span class='savoir-ex'><b>Ce que j'apporte, c'est</b> seize ans d'usine, dont onze en supervision.</span>
       Demandez poliment et fermement :
       <span class='savoir-ex'>J'<b>aimerais</b> qu'on <b>regarde</b> le quatrième échelon, et je vais vous dire pourquoi.</span>
       Refermez une question interdite :
       <span class='savoir-ex'>Je vous réponds sur ce qui vous intéresse : je suis disponible cinq soirs sur cinq. <b>Pour le reste, je préfère ne pas répondre.</b></span>
     </div>

     <div class="jr-sep"></div>
     <div class="jr-sub">Choisissez votre situation et votre rôle</div>
     <div class="jr-choix">
       <div class="jr-choix-l">Quel sujet ?</div>
       <div class="jr-opts" id="jrLogs">
         ${ROLE_CAS.map((c,i)=>`<button class="jr-opt${i===0?' on':''}" type="button" data-log="${c.id}" onclick="jrChoisir('log','${c.id}')">${esc(c.titre)}</button>`).join('')}
       </div>
       <div class="jr-choix-l">Vous jouez qui ?</div>
       <div class="jr-opts" id="jrRoles">
         <button class="jr-opt on" type="button" data-role="candidate" onclick="jrChoisir('role','candidate')">La personne qui passe l'entrevue</button>
         <button class="jr-opt" type="button" data-role="comite" onclick="jrChoisir('role','comite')">Le directeur de la production</button>
       </div>
       <div class="jr-choix-l">Comment ?</div>
       <div class="jr-opts" id="jrModes">
         <button class="jr-opt on" type="button" data-mode="texte" onclick="jrModeVoix(false)">✍️ Écrire</button>
         <button class="jr-opt" type="button" data-mode="voix" onclick="jrModeVoix(true)">🎤 Parler</button>
       </div>
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()" style="margin-top:14px">Commencer l'entrevue</button>
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
     <h3 class="prod-tit">Racontez une fois où vous avez dû décider seul</h3>
     <p class="prod-lead">Deux minutes environ, debout, sans lire vos notes mot à mot. C'est la question la plus fréquente d'une entrevue de sélection, et celle qu'on rate le plus souvent — parce qu'on répond par une qualité au lieu de raconter. Prenez une situation réelle de votre vie professionnelle, ici ou ailleurs, et menez-la en trois temps.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Annoncez en une phrase ce que vous allez raconter</div><div class="plan-ex">« Je vais vous parler d'un soir où j'ai dû arrêter une ligne sans pouvoir joindre personne. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">La situation, ce que vous avez fait vous-même, le résultat — avec un chiffre</div><div class="plan-ex">« Trois problèmes en même temps, quinze personnes qui attendaient. J'ai traité l'étiquetage d'abord, parce qu'une erreur d'étiquette sort de l'usine. Nous avons perdu quarante minutes, et aucune caisse n'est partie fausse. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Ce que vous feriez autrement, puis la règle que vous appliquez depuis</div><div class="plan-ex">« Si j'avais eu les données de production sous les yeux, j'aurais arrêté dix minutes plus tôt. Depuis, je note l'heure de chaque arrêt avant de faire quoi que ce soit. »</div></div>
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
     <h3 class="prod-tit">Écrivez le courriel du lendemain matin</h3>
     <p class="prod-lead">De 10 à 14 phrases, en trois paragraphes, envoyé dans les vingt-quatre heures. Le premier remercie, en une phrase. Le deuxième revient sur <b>un seul</b> point que vous avez mal expliqué en entrevue, le concède, et le complète par des faits vérifiables. Le troisième confirme ce qui a été convenu et vous rend joignable. On n'y ajoute jamais une demande qu'on n'a pas osé formuler de vive voix.</p>
     <div class="req">
       <div class="req-hd">Votre courriel doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un remerciement daté, en une seule phrase</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>L'annonce du point sur lequel vous revenez — un seul</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une concession : c'est vrai, mais… · certes…, mais…</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Deux faits vérifiables, avec un nombre</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un conditionnel de politesse : je souhaiterais, j'aimerais</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un connecteur de conclusion : par conséquent, ainsi</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une confirmation de ce qui a été convenu : comme convenu…</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une phrase de disponibilité, avec un numéro de téléphone</span></div>
       </div>
       <div class="req-note">Tenez le vouvoiement et le registre soutenu du début à la fin : on ne commence pas par « Madame, Monsieur » pour finir par « à bientôt ! ». Et n'écrivez rien que vos attestations ne puissent confirmer.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">Boréalis Emballages — comité de sélection, Sherbrooke</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Entrevue du 25 octobre — poste de superviseure ou superviseur de production, quart de soir</span></div>
       <textarea id="peText" rows="12" aria-label="Votre courriel" data-min="10" data-max="14" oninput="peCount()" placeholder="Madame, Monsieur,&#10;&#10;Je vous remercie du temps que vous m'avez accordé…"></textarea>
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
    "Je nomme les trois étapes d'un processus de sélection et je sais ce que chacune observe.",
    "Je sais que l'étape où l'on tombe le plus est l'entrevue de groupe, et je la prépare.",
    "J'entends ce qu'une voix ajoute aux mots : la surprise, l'incompréhension, la volonté.",
    "Je reprends un mot sans le répéter : ce rachat, cette acquisition, cet isolement.",
    "Je pose une question au conditionnel, sans supposer que tout est décidé.",
    "Je pose une question à l'inversion : le poste comporte-t-il… ?",
    "Je dis lequel des mots m'a échappé, au lieu de dire que je n'ai rien compris.",
    "Je reformule ce que j'ai compris avec mes propres mots, pour le vérifier.",
    "Je lis un profil d'entreprise et j'en tire un fait récent, un chiffre et une difficulté.",
    "Je distingue ce qui est exigé de ce qui est un atout, et je cherche « ou l'équivalent ».",
    "J'emploie les connecteurs de concession : certes…, mais… · bien que… soit…",
    "Je retrouve à quoi renvoient « dont », « auquel » et « à laquelle » dans une phrase longue.",
    "Je dis ce que j'aurais fait autrement, avec « si j'avais… j'aurais… ».",
    "J'emploie le subjonctif après ses déclencheurs, et l'indicatif après « même si ».",
    "Je mets en relief ce qui compte : ce que j'apporte, c'est… · c'est moi qui…",
    "Je reconnais une question qui porte sur un motif interdit, et j'y réponds sans me fâcher.",
    "Je demande une condition en offrant une contrepartie datée et mesurable.",
    "J'écris le courriel du lendemain : un remerciement, une reprise, une confirmation.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#1D6B8F">Je retiens des mots</span><span class="ctit" style="color:#1D6B8F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#1D6B8F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:6px 0 4px">Le processus de sélection</div>
     <textarea rows="2" placeholder="Ex. : la présélection, une mise en situation, une entrevue de groupe, un comité, un accusé de réception…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">L'usine et le quart de soir</div>
     <textarea rows="2" placeholder="Ex. : un contremaître, une chaîne de production, un temps d'arrêt, un carnet de commandes, le taux de roulement…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">Faire valoir son parcours</div>
     <textarea rows="2" placeholder="Ex. : certes… mais, ce que j'apporte c'est, si j'avais… j'aurais, une expérience équivalente…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">Conditions et négociation</div>
     <textarea rows="2" placeholder="Ex. : un échelon, une contrepartie, la période de probation, le service continu, un motif de discrimination…"></textarea>
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
