  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : la rencontre avec l'assistant, le récit oral corrigé,
  // puis la lettre personnelle. Le jeu de rôle vient en premier parce qu'il
  // sert de répétition aux deux autres.
  //
  // La production orale et le jeu de rôle viennent directement de la
  // situation du programme — « s'informer auprès d'un spécialiste à propos
  // d'un problème de santé », en production. La production écrite, elle,
  // vient des attentes de fin de cours du niveau, la situation n'ayant aucune
  // intention de production écrite : « il rédige également un courriel pour
  // donner des nouvelles à son entourage [...] ou bien pour décrire et
  // raconter un évènement d'une façon détaillée », et « l'adulte rédige un
  // court texte en organisant ses idées à l'aide de paragraphes ». Le savoir
  // de grammaire du texte « découper, disposer, formuler et présenter le
  // contenu d'une lettre personnelle » en fixe la forme — une lettre
  // personnelle, et non un courriel formel.
  //
  // Seule la situation publique est ici ; ce que sait la spécialiste jouée
  // par l'assistant vit dans server.py, scénario « specialiste ».
  const ROLE_CAS = [
    {id:'fatigue', titre:'Huit mois de fatigue', txt:"Tu as attendu <b>sept mois</b> ce rendez-vous. Ta fatigue a commencé en février et ne part pas. Tu as vingt minutes et tu ne sais pas quoi dire de plus que « je suis fatiguée »."},
    {id:'resultat', titre:'Un mot sur une feuille', txt:"On t'a dit le mot <b>anémie</b> au printemps, sans une ligne d'explication. Tu veux savoir ce que ce mot dit, ce qu'il ne dit pas, et ce qu'on va faire pour en savoir plus."},
    {id:'suite', titre:'Et après ?', txt:"La rencontre se termine. Tu n'as pas de diagnostic, et tu dois repartir en sachant <b>ce qui arrive ensuite</b>, avec quelles dates — et avec un papier pour ton employeur."},
  ];
  const ROLE_SUJETS = ["Raconter ton histoire dans l'ordre, avec des repères de temps",
    "Dire un changement plutôt qu'un état : avant je faisais ceci, maintenant non",
    "Donner un exemple précis, avec un lieu et un nombre",
    "Répondre à la question posée, sans minimiser ce que tu vis",
    "Demander qu'on te répète ou qu'on t'explique un mot que tu ne connais pas",
    "Poser au moins deux questions à toi, écrites d'avance",
    "Redire à la fin ce que tu as compris de la suite, avec les dates"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Vingt minutes avec la spécialiste</span></div>
     <p class="lead">L'assistant joue <b>une médecin spécialiste</b>. Elle répond à tout ce que tu demandes — mais elle ne devine rien : si tu ne racontes pas, elle n'a rien à chercher. Elle ne te donnera pas non plus de diagnostic aujourd'hui, et elle t'expliquera pourquoi.</p>
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
         <button class="jr-opt on" type="button" data-role="leyla" onclick="jrChoisir('role','leyla')">Celle qui consulte</button>
         <button class="jr-opt" type="button" data-role="specialiste" onclick="jrChoisir('role','specialiste')">La médecin spécialiste</button>
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
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()">Commencer la consultation</button>
     </div>
     <div class="jr-rappel">
       <div class="jr-rappel-t">Réutilise ce que tu viens d'apprendre</div>
       <div class="jr-rappel-g">
         <div><div class="jr-rappel-l">Recule d'un cran dans le temps</div><div class="jr-rappel-x">Mon médecin <b>avait envoyé</b> la demande en avril.</div></div>
         <div><div class="jr-rappel-l">Accroche le début à un moment</div><div class="jr-rappel-x">C'est le mois <b>où</b> mon fils a déménagé.</div></div>
         <div><div class="jr-rappel-l">Donne un exemple, et dis que c'en est un</div><div class="jr-rappel-x">Je monte moins bien, <b>par exemple</b> les douze marches de chez ma cliente.</div></div>
         <div><div class="jr-rappel-l">Reprends sans répéter</div><div class="jr-rappel-x">Une fatigue est arrivée en février. <b>Cette fatigue</b> n'est jamais repartie.</div></div>
         <div><div class="jr-rappel-l">Vérifie une consigne</div><div class="jr-rappel-x">Il faut <b>que je note</b> mes journées, c'est bien ça ?</div></div>
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
     <h3 class="prod-tit">Raconte le rendez-vous à un proche</h3>
     <p class="prod-lead">Quelqu'un qui t'aime attend de tes nouvelles depuis ce matin. Raconte-lui en 90 secondes environ : pourquoi tu y allais et depuis quand tu attendais, ce que la spécialiste a demandé et expliqué, puis ce qui arrive ensuite, avec les dates.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Pourquoi j'y allais, et depuis quand</div><div class="plan-ex">« Mon médecin avait envoyé la demande en avril. J'ai attendu sept mois. C'était pour une fatigue qui dure depuis février. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Ce qu'elle a demandé, ce qu'elle a expliqué</div><div class="plan-ex">« Elle m'a demandé de noter mes journées pendant six semaines. Elle a expliqué qu'une anémie, c'est un résultat et pas une cause. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Ce qui arrive ensuite, avec les dates</div><div class="plan-ex">« Je repasse au laboratoire cette semaine. Elle me rappelle le jour où elle aura les résultats, dans six à huit semaines. »</div></div>
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
     <h3 class="prod-tit">Écris à quelqu'un de ta famille, resté au pays</h3>
     <p class="prod-lead">Ta sœur attend de tes nouvelles depuis le printemps et elle sait que tu avais un rendez-vous aujourd'hui. Écris-lui un courriel de 8 à 12 phrases, en <b>trois paragraphes</b> : d'abord comment tu vas et pourquoi tu écris ; ensuite ce qui s'est passé ce matin, raconté dans l'ordre ; enfin ce qui arrive ensuite et ce que tu lui demandes.</p>
     <div class="req">
       <div class="req-hd">Ta lettre doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une formule d'appel et une formule de salutation, personnelles et non formelles</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Trois paragraphes séparés, un par idée principale</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un plus-que-parfait : « mon médecin avait envoyé la demande en avril »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un « le jour où », « le mois où » ou « au moment où »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un exemple annoncé : « par exemple », « comme », « notamment »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une reprise sans répétition : « cette fatigue », « ce rendez-vous », « ces examens »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une subordonnée infinitive : « elle m'a demandé de… », « j'ai commencé à… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une date, au moins : ce qui arrive ensuite et quand</span></div>
       </div>
       <div class="req-note">Écris avec tes mots à toi, pas avec ceux de la lettre du médecin. « J'ai une réduction de la tolérance à l'effort » ne dit rien à ta sœur ; « je monte les escaliers moins vite qu'avant » lui dit tout.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">ta sœur</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">À toi de le trouver — court, et qui donne déjà une nouvelle</span></div>
       <textarea id="peText" rows="10" aria-label="Ta lettre" data-min="8" data-max="12" oninput="peCount()" placeholder="Ma chère sœur,&#10;&#10;J'ai enfin vu la spécialiste ce matin. Je t'écris tout de suite parce que je sais que tu attendais…"></textarea>
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
    "Je sais ce qu'est une clinique externe et en quoi ce n'est pas l'urgence.",
    "Je sais ce qu'une demande de consultation déclenche, et ce qu'elle ne garantit pas.",
    "Je prépare mon sac la veille : carte, convocation, liste de tout ce que je prends.",
    "Je reconnais les trois cas où la lettre écrite ne dit pas le son entendu.",
    "J'amorce une conversation avec un inconnu sans lui demander ce qu'il a.",
    "Je raconte ce qui s'était passé avant, avec le plus-que-parfait.",
    "Je comprends « je suis après attendre » et « on a passé proche d'annuler ».",
    "Je reprends un mot déjà dit sans le répéter : cette fatigue, ce délai, ces examens.",
    "Je décris un changement plutôt qu'un état, avec un lieu et un nombre.",
    "Je demande qu'on m'explique un mot que je ne connais pas.",
    "J'emploie « de », « à » ou rien du tout devant un verbe à l'infinitif.",
    "J'emploie « où » pour un lieu et aussi pour un moment.",
    "J'entends qu'« il faudrait que » est une obligation et pas une suggestion.",
    "J'annonce un exemple avant de le donner.",
    "Je trouve dans un feuillet ce qu'on me demande d'apporter et le numéro à appeler.",
    "Je repère dans un compte rendu le paragraphe qui me demande quelque chose.",
    "Je reconnais ma propre phrase sous les mots du dossier.",
    "Je peux raconter un rendez-vous à voix haute, dans l'ordre et avec les dates.",
    "Je peux écrire à un proche en trois paragraphes pour donner des nouvelles.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Entrer à l'hôpital</div>
     <textarea rows="2" placeholder="Ex. : une clinique externe, une demande de consultation, la médecine interne, un délai d'attente, un dossier médical…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">L'attente, et ce qu'on s'y dit</div>
     <textarea rows="2" placeholder="Ex. : un malaise, la fatigue chronique, un proche aidant, les heures de visite, vous attendez depuis longtemps ?…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Dans le bureau</div>
     <textarea rows="2" placeholder="Ex. : un antécédent, un prélèvement, un diagnostic, une anémie, depuis février, avant je ne m'assoyais pas…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Ce qui s'écrit après</div>
     <textarea rows="2" placeholder="Ex. : un feuillet d'information, les effets secondaires, un suivi, la conduite proposée, d'étiologie à préciser…"></textarea>
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
