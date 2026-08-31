  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : l'appel au service de la paie avec l'assistant, une
  // intervention orale en réunion, puis la demande de congé de formation.
  // Le jeu de rôle vient en premier parce qu'il sert de répétition.
  // Seule la situation publique est côté client ; ce que sait l'employé du
  // service joué par l'assistant vit dans server.py.
  const ROLE_CAS = [
    {id:'paie', titre:"Des heures supplémentaires non majorées", txt:"Vous avez travaillé <b>44 heures</b> la semaine du 10 août. Les 4 heures au-delà de 40 ont été payées au taux simple. Votre superviseure vous les avait demandées par courriel."},
    {id:'horaire', titre:"Un horaire changé sans avis", txt:"Votre horaire de la semaine prochaine a été modifié dans le système : trois soirs au lieu de deux. Personne ne vous a prévenue, et vous suivez un cours le mercredi soir."},
    {id:'facture', titre:"Une facture réglée deux fois", txt:"Le fournisseur <b>Ferrico</b> a été payé deux fois pour la même facture de <b>1 840 $</b>. L'erreur vient d'un doublon dans le système, et le crédit n'est toujours pas apparu après trois semaines."},
  ];
  const ROLE_SUJETS = ["Vous présenter et situer l'appel en une phrase",
    "Exposer le fait avec ses dates et ses chiffres",
    "Nommer l'écart sans accuser la personne au bout du fil",
    "Répondre à l'objection sans hausser le ton",
    "Citer la règle ou la pièce qui appuie votre demande",
    "Demander ce qu'il faut, de qui, et pour quand",
    "Obtenir une confirmation écrite et remercier"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Réglez le problème au téléphone</span></div>
     <p class="lead">L'assistant joue <b>l'employé du service administratif</b>. Il n'est pas de mauvaise foi, mais il a ses procédures et il objectera au moins une fois. À vous de tenir votre bout sans monter le ton.</p>
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
         <button class="jr-opt on" type="button" data-role="employe" onclick="jrChoisir('role','employe')">L'employée qui appelle</button>
         <button class="jr-opt" type="button" data-role="service" onclick="jrChoisir('role','service')">Le service administratif</button>
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
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()">Commencer l'appel</button>
     </div>
     <div class="jr-rappel">
       <div class="jr-rappel-t">Réutilisez ce que vous venez d'apprendre</div>
       <div class="jr-rappel-g">
         <div><div class="jr-rappel-l">Nommez l'écart sans accuser</div><div class="jr-rappel-x">La majoration <b>n'a pas été appliquée</b> sur les quatre heures.</div></div>
         <div><div class="jr-rappel-l">Dites ce qui doit arriver</div><div class="jr-rappel-x">Il faut que la demande <b>passe</b> par ma superviseure, je comprends.</div></div>
         <div><div class="jr-rappel-l">Admettez, puis objectez</div><div class="jr-rappel-x">Je comprends votre procédure. <b>Cependant</b>, le travail a été fait.</div></div>
         <div><div class="jr-rappel-l">Demandez sans exiger</div><div class="jr-rappel-x">Est-ce que vous <b>pourriez</b> me confirmer la date par écrit ?</div></div>
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
     <h3 class="prod-tit">Intervenez dans la réunion</h3>
     <p class="prod-lead">On vient de proposer de changer de fournisseur pour économiser huit pour cent. Vous savez que le délai de livraison passerait de quatre à dix jours. Prenez la parole : environ 90 secondes.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Résumez ce qui vient d'être dit</div><div class="plan-ex">« Si je résume, l'écart de prix est réel et il représente environ quarante mille dollars. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Introduisez l'objection avec un chiffre</div><div class="plan-ex">« Cependant, le délai passerait à dix jours ; le stock doublé mangerait la moitié de l'économie. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Proposez un compromis, au conditionnel</div><div class="plan-ex">« Je proposerais un partage : les pièces courantes chez l'un, l'urgent chez l'autre. »</div></div>
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
     <h3 class="prod-tit">Demandez votre congé de formation</h3>
     <p class="prod-lead">Écrivez à votre supérieur immédiat pour demander une demi-journée par semaine, pendant douze semaines. Arrivez avec le problème réglé, pas avec un souhait : de 8 à 12 phrases.</p>
     <div class="req">
       <div class="req-hd">Votre courriel doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un objet qui se lit seul, avec la période visée</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le nom exact de la formation et sa durée</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Au moins un chiffre qui dit ce que la lacune coûte</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une hypothèse au passé : « si j'avais… j'aurais… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une phrase au subjonctif : « il faudrait que… », « pour que… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Comment votre travail se fait pendant votre absence</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une demande unique et une échéance de réponse</span></div>
       </div>
       <div class="req-note">Ne demandez pas la permission d'avoir envie d'apprendre. Chiffrez ce que la formation rapporte, dites comment le travail se fait quand même, et fixez une date de réponse.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">Manon Trépanier, superviseure des opérations</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Demande de congé de formation — automne</span></div>
       <textarea id="peText" rows="10" aria-label="Votre courriel" data-min="8" data-max="12" oninput="peCount()" placeholder="Bonjour Manon,&#10;Je te soumets une demande de formation pour la session d'automne…"></textarea>
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
    "Je comprends une description de tâches détaillée, avec ses heures et ses montants.",
    "Je découpe une phrase longue en groupes de souffle quand je parle.",
    "Je fais la différence entre le registre de la machine à café et celui d'un courriel.",
    "Je peux exposer un problème de paie avec ses dates et ses chiffres.",
    "Je connais le seuil de quarante heures et la majoration de cinquante pour cent.",
    "J'emploie le subjonctif après « il faut que » et « il est important que ».",
    "Je sais nommer un écart à la voix passive, sans accuser personne.",
    "J'écris une lettre d'affaires en cinq parties, avec une échéance.",
    "Je résume les propos d'un collègue avant de donner mon avis.",
    "Je propose un compromis au conditionnel au lieu de l'imposer.",
    "Je rédige un compte rendu : décision, responsable, échéance.",
    "Je peux chiffrer ce qu'une lacune me coûte avec « si j'avais… j'aurais… ».",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Le poste et les tâches</div>
     <textarea rows="2" placeholder="Ex. : une description de tâches, un supérieur immédiat, faire le suivi, un imprévu…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">La paie et la réclamation</div>
     <textarea rows="2" placeholder="Ex. : un relevé de paie, les heures supplémentaires, la majoration, une réclamation, un accusé de réception…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">La réunion</div>
     <textarea rows="2" placeholder="Ex. : un ordre du jour, un compte rendu, un compromis, une échéance, cependant, en revanche, par conséquent…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">La formation</div>
     <textarea rows="2" placeholder="Ex. : le perfectionnement, une attestation, un congé de formation, la reconnaissance des acquis…"></textarea>
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
