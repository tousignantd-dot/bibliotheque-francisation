  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : la discussion avec l'assistant, la description orale
  // de la démarche, puis le courriel aux ressources humaines. Le jeu de rôle
  // vient en premier parce qu'il sert de répétition aux deux autres.
  //
  // Les deux productions viennent des intentions de la situation elle-même,
  // et non des attentes de fin de cours : « décrire les étapes d'une démarche
  // administrative » (PO) et « rédiger un courriel dans le contexte de
  // relations professionnelles » (PE).
  //
  // Seule la situation publique est ici ; ce que sait l'interlocuteur joué par
  // l'assistant vit dans server.py, scénario « demarcheinterne ».
  const ROLE_CAS = [
    {id:'affichage', titre:"L'affichage au babillard", txt:"Un poste de <b>vérificatrice à la qualité</b> est affiché à l'interne. Il reste <b>dix jours ouvrables</b> au babillard et descend le <b>vendredi 25 septembre, à 16 h</b>. Ton collègue ne l'a pas vu passer."},
    {id:'etapes', titre:'Les cinq étapes', txt:"Vérifier son admissibilité (<b>six mois d'ancienneté</b> et la formation sur les allergènes), remplir le <b>formulaire RH-04</b>, le remettre avant vendredi, rencontrer le <b>comité</b> trente minutes, recevoir une <b>réponse écrite</b> dans les cinq jours ouvrables."},
    {id:'essai', titre:"La période d'essai", txt:"Trente jours travaillés au nouveau poste, payés au <b>nouveau taux dès le premier jour</b>. Si ça ne convient pas — d'un côté comme de l'autre —, <b>droit de retour</b> à l'ancien poste, aux mêmes conditions."},
  ];
  const ROLE_SUJETS = ["Dire de quoi il s'agit et où tu l'as appris",
    "Résumer la démarche en trois ou quatre phrases",
    "Nommer les étapes dans l'ordre, sans en sauter",
    "Donner un délai précis pour au moins une étape",
    "Illustrer un point par un exemple annoncé",
    "Répondre à une objection sans rejeter la personne",
    "Poser une hypothèse avec « si »",
    "Distinguer ce que le document dit de ce que tu en penses"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Explique la démarche à un collègue qui doute</span></div>
     <p class="lead">L'assistant joue <b>un collègue qui n'a rien lu et qui n'y croit pas</b>. Il t'interrompt, il te demande d'où tu tiens ça, et il est certain que c'est l'ancienneté qui décide. À toi de résumer, d'ordonner les étapes et de citer ce qui est écrit.</p>
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
         <button class="jr-opt on" type="button" data-role="yaneth" onclick="jrChoisir('role','yaneth')">Celle qui a lu</button>
         <button class="jr-opt" type="button" data-role="sceptique" onclick="jrChoisir('role','sceptique')">Le collègue qui doute</button>
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
       <div class="jr-rappel-t">Réutilise ce que tu viens d'apprendre</div>
       <div class="jr-rappel-g">
         <div><div class="jr-rappel-l">Ne répète pas le mot, reprends-le</div><div class="jr-rappel-x">Le droit de retour ? Tout le monde <b>en</b> a un, et personne ne <b>le</b> sait.</div></div>
         <div><div class="jr-rappel-l">Place les étapes sans « ensuite »</div><div class="jr-rappel-x"><b>Avant de</b> rencontrer le comité, tu remplis le RH-04.</div></div>
         <div><div class="jr-rappel-l">Dis ce qu'il faut</div><div class="jr-rappel-x">Il faut <b>que</b> tu <b>aies</b> six mois d'ancienneté.</div></div>
         <div><div class="jr-rappel-l">Pose une condition</div><div class="jr-rappel-x"><b>Si</b> ça ne <b>convient</b> pas, tu reviens à ton poste.</div></div>
         <div><div class="jr-rappel-l">Cite au lieu d'affirmer</div><div class="jr-rappel-x">Ce n'est pas moi qui le dis : c'est l'<b>article 4.3</b>.</div></div>
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
     <h3 class="prod-tit">Décris les étapes de la démarche</h3>
     <p class="prod-lead">Quelqu'un de ton entourage veut se présenter à un poste affiché chez lui et ne sait pas comment ça marche. Explique-lui en 90 secondes environ : de quoi il s'agit et où tu l'as appris, les étapes dans l'ordre avec les détails nécessaires — les délais surtout —, un exemple, puis ce que tu ferais à sa place.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">De quoi il s'agit, et d'où tu le sais</div><div class="plan-ex">« Chez nous, un poste de vérificatrice a été affiché au babillard le 14 septembre. C'est écrit dans la note de service. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Les cinq étapes, dans l'ordre, avec les délais</div><div class="plan-ex">« D'abord, tu vérifies que tu as six mois d'ancienneté. Ensuite, tu remplis le formulaire RH-04. Avant de rencontrer le comité, tu dois l'avoir remis. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Un exemple, puis ce que tu ferais</div><div class="plan-ex">« Prenons la période d'essai : trente jours, et si ça ne convient pas, tu reviens à ton poste. À ta place, je me présenterais. »</div></div>
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
     <h3 class="prod-tit">Écris ton courriel aux ressources humaines</h3>
     <p class="prod-lead">Tu déposes ta candidature par courriel. Écris un message de 8 à 12 phrases, en <b>trois paragraphes</b> : d'abord pourquoi tu écris, ensuite ce que tu joins et ce qui te qualifie, enfin ce que tu demandes. Un seul sujet, et un objet qui se comprend sans ouvrir le message.</p>
     <div class="req">
       <div class="req-hd">Ton courriel doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un objet court et précis, sans phrase complète</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une formule d'appel qui nomme la personne, et une salutation</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Trois paragraphes séparés, un par idée</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une date précise : celle de l'affichage ou celle de la limite</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une demande au conditionnel : « Pourriez-vous… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un « il faut que » ou un « je souhaite que » suivi du subjonctif</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une reprise sans répétition : « cette formation », « ce poste »…</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une signature avec le nom, le service et le quart</span></div>
       </div>
       <div class="req-note">Sépare bien ce que tu demandes de ce que tu racontes. Un courriel qui mêle les deux se lit comme une confidence ; un courriel qui les sépare se lit comme une candidature — et c'est celui-là qui obtient une réponse.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">msgrenon@emballagesbocage.example</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">À toi de le trouver — court, et sans phrase complète</span></div>
       <textarea id="peText" rows="10" aria-label="Ton courriel" data-min="8" data-max="12" oninput="peCount()" placeholder="Bonjour Madame Grenon,&#10;&#10;Je vous écris au sujet du poste de vérificatrice à la qualité, affiché au babillard le 14 septembre…"></textarea>
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
    "Je reconnais les quatre écrits du travail : l'affichage, la note de service, la politique, le compte rendu.",
    "Je sais d'avance ce qu'un document va me donner, et ce qu'il ne me donnera pas.",
    "Je lis l'en-tête et l'encadré d'une note avant le reste.",
    "Je comprends ce que les puces, les numéros d'articles et le gras veulent dire.",
    "Je retiens les étapes d'une démarche dans l'ordre, avec leurs délais.",
    "Je reconnais l'ordre des étapes même sans « ensuite » : avant de, une fois, dès que.",
    "Je retrouve à quoi renvoient « le », « en » et « y » dans une explication suivie.",
    "J'emploie le subjonctif après « il faut que » et « je souhaite que ».",
    "Je réunis deux phrases avec « qui », « que » ou « où » — et j'écris « le jour où ».",
    "Je comprends qu'un plus-que-parfait dit « c'était déjà fait avant ».",
    "Je reconnais un passé simple dans un récit écrit et je le traduis.",
    "Je dis la même chose en trois mots, avec un nom au lieu d'un verbe.",
    "Je pose une hypothèse avec « si », sans mettre de futur après « si ».",
    "Je repère les six parties d'un compte rendu et je vais droit aux décisions.",
    "Je peux décrire à voix haute les étapes d'une démarche, avec les détails nécessaires.",
    "Je peux écrire un courriel professionnel : objet, appel, trois paragraphes, demande, signature.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Ce qu'on voit au babillard</div>
     <textarea rows="2" placeholder="Ex. : un babillard, un affichage interne, une mutation, une candidature interne…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Aux ressources humaines</div>
     <textarea rows="2" placeholder="Ex. : les ressources humaines, un formulaire, un comité de sélection, l'ancienneté, une période d'essai…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les documents écrits</div>
     <textarea rows="2" placeholder="Ex. : une note de service, une politique interne, les exigences du poste, un droit de retour…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">La rencontre</div>
     <textarea rows="2" placeholder="Ex. : un compte rendu, un ordre du jour, les qualifications, un suivi, une décision…"></textarea>
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
