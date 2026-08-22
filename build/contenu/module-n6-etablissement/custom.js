  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : la rencontre avec l'assistant, le compte rendu oral
  // corrigé, puis le courriel formel au centre. Le jeu de rôle vient en
  // premier parce qu'il sert de répétition aux deux autres.
  //
  // La production orale vient directement de la situation du programme
  // (« s'informer pour choisir un programme d'études », en production). La
  // production écrite, elle, vient des attentes de fin de cours du niveau —
  // « dans ses relations professionnelles, il rédige un courriel ou une
  // lettre en respectant les conventions habituelles » — et du savoir de
  // grammaire du texte « découper, disposer, formuler et présenter le
  // contenu d'un courriel formel ».
  //
  // Seule la situation publique est ici ; ce que sait le conseiller joué par
  // l'assistant vit dans server.py, scénario « orientationscolaire ».
  const ROLE_CAS = [
    {id:'programme', titre:'Quel programme ?', txt:"Tu termines ta francisation en <b>février</b>. Tu as travaillé six ans dans une pharmacie avant d'arriver ici, et tu voudrais y revenir. Tu ne sais pas <b>quel programme</b> mène à ce métier, ni combien de temps il dure."},
    {id:'prealables', titre:'Ce qui me manque', txt:"Tu sais quel programme tu vises. Tu ne sais pas <b>quels préalables</b> il te manque, ni comment on les obtient : un cours ? un test ? un papier de ton pays ? Tu viens le faire calculer."},
    {id:'papiers', titre:'Mes papiers de là-bas', txt:"Tu as un diplôme et un relevé de notes de ton pays, plus une <b>évaluation comparative</b> du ministère de l'Immigration. On t'a dit que c'était « une équivalence ». Tu veux savoir ce que ça vaut vraiment ici."},
  ];
  const ROLE_SUJETS = ["Exposer ta situation en quelques phrases suivies, pas en mots isolés",
    "Dire ce que tu cherches précisément, dès le début",
    "Poser au moins deux questions indirectes : je me demande si…, je voudrais savoir…",
    "Reprendre ce qui vient d'être dit sans le répéter mot pour mot",
    "Demander de répéter ou de préciser quand un mot t'échappe",
    "Noter les dates, et les redire à voix haute pour vérifier",
    "Reformuler la démarche à la fin, dans l'ordre, avant de partir"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Une heure avec le conseiller d'orientation</span></div>
     <p class="lead">L'assistant joue <b>un conseiller d'orientation</b>. Il connaît son affaire et il répond à tout — mais il ne devine rien : si tu ne dis pas ta situation, il ne peut rien calculer. Il ne t'admettra nulle part non plus : ce n'est pas lui qui décide.</p>
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
       <div class="jr-gram-t">Réutilise ce que tu viens d'apprendre</div>
       Pose ta question sans la poser :
       <span class='savoir-ex'><b>Je me demande si</b> mes années de travail comptent.</span>
       Ne répète pas, reprends :
       <span class='savoir-ex'>J'ai une évaluation comparative. On m'a dit que je pouvais m'en servir, mais je ne sais pas ce qu'elle vaut.</span>
       Désigne sans répéter le nom :
       <span class='savoir-ex'>Des trois voies, <b>celle</b> qui me concerne demande un test.</span>
       Pose une condition :
       <span class='savoir-ex'><b>Si</b> je réussis le test en novembre, est-ce que ça suffit ?</span>
       Annonce ton avis :
       <span class='savoir-ex'><b>Pour ma part</b>, je préférerais commencer en mars.</span>
     </div>

     <div class="jr-sep"></div>
     <div class="jr-sub">Choisis ta situation et ton rôle</div>
     <div class="jr-choix">
       <div class="jr-choix-l">Quel sujet ?</div>
       <div class="jr-opts" id="jrLogs">
         ${ROLE_CAS.map((c,i)=>`<button class="jr-opt${i===0?' on':''}" type="button" data-log="${c.id}" onclick="jrChoisir('log','${c.id}')">${esc(c.titre)}</button>`).join('')}
       </div>
       <div class="jr-choix-l">Tu joues qui ?</div>
       <div class="jr-opts" id="jrRoles">
         <button class="jr-opt on" type="button" data-role="bintou" onclick="jrChoisir('role','bintou')">Celle qui s'informe</button>
         <button class="jr-opt" type="button" data-role="conseiller" onclick="jrChoisir('role','conseiller')">Le conseiller d'orientation</button>
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
     <h3 class="prod-tit">Explique la démarche à un camarade de classe</h3>
     <p class="prod-lead">Quelqu'un de ta classe termine sa francisation en même temps que toi et ne sait pas quoi faire ensuite. Explique-lui en 90 secondes environ : de quoi il s'agit et auprès de qui tu t'es informé, les étapes dans l'ordre avec les détails nécessaires, puis ce que tu en penses.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">De quoi il s'agit, et d'où tu le tiens</div><div class="plan-ex">« J'ai rencontré le conseiller d'orientation la semaine passée. Il y a trois façons d'entrer dans un programme de formation professionnelle. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Les étapes, dans l'ordre, avec les détails</div><div class="plan-ex">« D'abord, tu finis ta francisation. Ensuite, tu t'inscris au test au comptoir. Dès que le résultat arrive, tu le déposes au secrétariat. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Ce que tu en penses, annoncé comme un avis</div><div class="plan-ex">« À mon avis, le plus important, c'est la date : si la preuve n'est pas au dossier le 6 février, la place repart. »</div></div>
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
     <h3 class="prod-tit">Écris au secrétariat du centre</h3>
     <p class="prod-lead">Tu as reçu un avis d'admission conditionnelle et il te reste une question. Écris un courriel de 8 à 12 phrases, en <b>trois paragraphes</b> : d'abord qui tu es et de quel dossier tu parles ; ensuite ta situation et ta question, précisément ; enfin ce que tu t'engages à faire, avec une date.</p>
     <div class="req">
       <div class="req-hd">Ton courriel doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une formule d'appel et une formule de salutation</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ton nom et ton numéro de dossier dès le premier paragraphe</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Trois paragraphes séparés, un par idée principale</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une question indirecte : « je voudrais savoir si… », « j'aimerais savoir ce qui… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une hypothèse en « si » — sans futur juste après « si »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un « il faut que » ou un « j'aimerais que » suivi du subjonctif</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une reprise sans répétition : « cette demande », « ce document », « celui que »…</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un engagement daté : « Je déposerai la preuve la semaine du… »</span></div>
       </div>
       <div class="req-note">Ne demande pas une faveur : expose une situation et propose une date. Un courriel qui demande une exception reçoit un non poli ; un courriel qui annonce ce qu'on va faire et quand reçoit un « c'est noté » — et c'est ce que tu cherches.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">secretariat@cfp-jean-bertaud.example</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">À toi de le trouver — court, avec le numéro de dossier</span></div>
       <textarea id="peText" rows="10" aria-label="Ton courriel" data-min="8" data-max="12" oninput="peCount()" placeholder="Madame,&#10;&#10;Je vous écris au sujet de l'avis d'admission conditionnelle que j'ai reçu le 4 novembre…"></textarea>
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
    "Je sais à qui poser quelle question dans un établissement.",
    "Je sais qu'une chose dite au comptoir ne compte pas tant qu'elle n'est pas écrite.",
    "Je reconnais les trois cas où la lettre écrite ne dit pas le son entendu.",
    "Je retrouve à quoi renvoient « le », « en » et « y » dans une conversation suivie.",
    "J'emploie « celui », « celle », « ceux » et « celles » avec « qui », « que » ou « où ».",
    "Je pose une question indirecte : je me demande si…, je voudrais savoir ce que…",
    "Je repère dans un texte suivi la phrase qui répond à une question précise.",
    "Je trouve la condition et la date limite d'un avis officiel.",
    "Je comprends qu'un futur simple, dans un document, donne un ordre.",
    "Je comprends que « les documents se déposent » veut dire que c'est à moi de les déposer.",
    "Je reconnais un passé simple dans un historique et je le traduis en passé composé.",
    "J'entends, dans une rencontre, qui explique, qui décide et qui témoigne.",
    "Je prends la parole sans couper : si je peux me permettre, si je comprends bien…",
    "J'emploie le subjonctif après « il faut que », « j'aimerais que », « elle exige que ».",
    "Je pose une condition avec « si », sans mettre de futur juste après « si ».",
    "J'annonce mon point de vue comme un point de vue, et pas comme un fait.",
    "Je peux expliquer une démarche d'admission en étapes, à voix haute.",
    "Je peux écrire un courriel formel au secrétariat, en trois paragraphes.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Les personnes et les papiers du centre</div>
     <textarea rows="2" placeholder="Ex. : une conseillère d'orientation, un dossier scolaire, un relevé de notes, l'enseignement individualisé, une matière…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Choisir un programme</div>
     <textarea rows="2" placeholder="Ex. : un programme d'études, un préalable, la formation professionnelle, une évaluation comparative, la reconnaissance des acquis…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les écrits officiels</div>
     <textarea rows="2" placeholder="Ex. : un avis officiel, une admission conditionnelle, un encadré, une date limite, un numéro de dossier…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Prendre sa place dans une rencontre</div>
     <textarea rows="2" placeholder="Ex. : une rencontre de suivi, un plan de formation, un compte rendu, si je peux me permettre, pour ma part…"></textarea>
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
