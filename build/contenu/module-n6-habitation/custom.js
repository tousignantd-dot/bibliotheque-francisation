  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : la discussion avec l'assistant, la description orale
  // du diagnostic, puis le courriel à l'entrepreneur. Le jeu de rôle vient en
  // premier parce qu'il sert de répétition aux deux autres.
  //
  // La production **orale** vient de l'intention de la situation elle-même —
  // « comprendre de l'information et poser des questions reliées à des travaux
  // de réparation ou de rénovation », qui est portée deux fois, en
  // compréhension et en production. La production **écrite** n'a aucune
  // intention dans cette situation : elle vient des **attentes de fin de
  // cours** du niveau 6 — « dans ses relations professionnelles, il rédige un
  // courriel ou une lettre en respectant les conventions habituelles » et
  // « il rédige un court texte en organisant ses idées à l'aide de
  // paragraphes ». C'est écrit ici pour que personne ne la retire en croyant
  // qu'elle sort de nulle part.
  //
  // Seule la situation publique est ici ; ce que sait l'interlocuteur joué par
  // l'assistant vit dans server.py, scénario « travauxrenovation ».
  const ROLE_CAS = [
    {id:'diagnostic', titre:'Le diagnostic', txt:"La fissure du mur nord est un <b>résultat</b>. La cause est dehors : une <b>descente de gouttière</b> qui se vide à 40 cm du mur, et une <b>pente de terrain</b> qui ramène l'eau. On rallonge, on reprofile, <b>puis</b> on injecte."},
    {id:'soumission', titre:'La soumission', txt:"<b>34 500 $</b> avant taxes, cinq postes, <b>six semaines</b> ouvrables séchage compris, <b>acompte de 30 %</b> à la signature. Exclusions : le permis, la peinture, les luminaires, la disposition des matériaux, et <b>toute condition non visible</b> au moment de la visite."},
    {id:'imprevu', titre:"L'imprévu du 8 avril", txt:"Aucune membrane sous la dalle, et un vieux <b>puisard condamné</b> avant l'achat. Deux solutions : casser et recouler — <b>6 800 $, neuf jours</b> — ou plancher flottant sur membrane — <b>1 900 $, deux jours</b>. La première demande un <b>plan modifié</b> au service des permis."},
  ];
  const ROLE_SUJETS = ["Redire ce que tu as compris, pour le faire confirmer",
    "Distinguer la cause du résultat, à voix haute",
    "Demander ce qu'un mot technique veut dire",
    "Poser une question avec « quel » ou « combien »",
    "Demander un délai en jours ouvrables, pas « bientôt »",
    "Poser une hypothèse avec « si », sans futur après « si »",
    "Demander que ce qui est dit soit mis par écrit",
    "Séparer ce que le document écrit de ce que tu en penses"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Pose tes questions à l'entrepreneur</span></div>
     <p class="lead">L'assistant joue <b>un entrepreneur général pressé et honnête</b>. Il ne ment pas, mais il va vite, il emploie ses mots de métier sans les expliquer, et il répond « ça dépend » à toute question vague. À toi de redire ce que tu as compris, de demander ce qui manque, et d'obtenir des chiffres.</p>
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
       <div class="jr-gram-t">Réutilise ce que tu viens d'apprendre</div>
       Ne répète pas le mot, reprends-le :
       <span class='savoir-ex'>La fissure ? Je ne veux pas qu'on <b>la</b> répare avant d'avoir réglé la gouttière.</span>
       Dis qui fait quoi :
       <span class='savoir-ex'>Vous <b>faites injecter</b> la fissure <b>par</b> un spécialiste, c'est bien ça ?</span>
       Demande précisément :
       <span class='savoir-ex'><b>Quel</b> délai en jours ouvrables entre l'injection et le gypse ?</span>
       Pose une condition :
       <span class='savoir-ex'><b>Si</b> le permis <b>sort</b> dans dix jours, est-ce que ce sera prêt le 12 ?</span>
       Demande que ce soit écrit :
       <span class='savoir-ex'>J'aimerais <b>que</b> vous m'<b>écriviez</b> ça dans la soumission.</span>
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
         <button class="jr-opt on" type="button" data-role="doina" onclick="jrChoisir('role','doina')">Celle qui fait faire</button>
         <button class="jr-opt" type="button" data-role="entrepreneur" onclick="jrChoisir('role','entrepreneur')">L'entrepreneur</button>
       </div>
       <div class="jr-choix-l">Comment ?</div>
       <div class="jr-opts" id="jrModes">
         <button class="jr-opt on" type="button" data-mode="texte" onclick="jrModeVoix(false)">✍️ Écrire</button>
         <button class="jr-opt" type="button" data-mode="voix" onclick="jrModeVoix(true)">🎤 Parler</button>
       </div>
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()" style="margin-top:14px">Commencer la discussion</button>
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
     <h3 class="prod-tit">Redis le diagnostic, puis pose tes questions</h3>
     <p class="prod-lead">Quelqu'un de ta famille n'était pas là quand l'entrepreneur est passé. Explique-lui en 90 secondes environ : ce qui a été trouvé et ce qui l'a causé, ce qu'on va faire faire et dans quel ordre, un chiffre précis — un montant, un délai, une mesure —, puis les deux questions que tu poseras avant de signer.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Ce qui a été trouvé, et ce qui l'a causé</div><div class="plan-ex">« Le mur de fondation est fendu. Mais la fissure, c'est le résultat : la cause est dehors, c'est la gouttière qui se vide au pied du mur. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Ce qu'on fait faire, dans l'ordre, avec un chiffre</div><div class="plan-ex">« On rallonge les gouttières, on refait la pente, et seulement après on fait injecter la fissure. Ensuite, on laisse sécher quatre semaines. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Les deux questions que tu poseras</div><div class="plan-ex">« Quel délai en jours ouvrables entre l'injection et le gypse ? Et si vous trouvez une condition non visible, qu'est-ce qui arrive ? »</div></div>
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
     <h3 class="prod-tit">Écris à l'entrepreneur après la rencontre</h3>
     <p class="prod-lead">Le soir du 8 avril, tu mets par écrit ce qui n'a été dit que de vive voix. Écris un courriel de 8 à 12 phrases, en <b>trois paragraphes</b> : d'abord de quelle rencontre tu parles, ensuite ce que tu as compris — les deux solutions, avec leurs prix et leurs délais —, enfin ce que tu demandes et pour quand. Une seule demande, et une date.</p>
     <div class="req">
       <div class="req-hd">Ton courriel doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un objet précis, avec une date, et sans phrase complète</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une formule d'appel qui nomme la personne, et une salutation</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Trois paragraphes séparés par une ligne vide, une idée chacun</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Les deux solutions redites avec leurs montants et leurs délais</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un « il faut que » ou un « j'aimerais que » suivi du subjonctif</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une hypothèse avec « si » — et pas de futur juste après « si »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une reprise sans répétition : « cette solution », « ces travaux », « en », « y »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une signature avec le nom et à quel titre tu écris</span></div>
       </div>
       <div class="req-note">Sépare ce que l'entrepreneur a dit de ce que tu en penses. Un courriel qui mêle les deux se discute ; un courriel qui les sépare se répond — et c'est celui-là qui obtient les deux prix par écrit.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">f.trudelle@renovation-trudelle.example</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">À toi de le trouver — une date, un sujet, et pas de phrase complète</span></div>
       <textarea id="peText" rows="10" aria-label="Ton courriel" data-min="8" data-max="12" oninput="peCount()" placeholder="Bonjour Monsieur Trudelle,&#10;&#10;Je vous écris à la suite de notre rencontre d'hier, au sous-sol…"></textarea>
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
    "Je sais dans quel ordre un chantier se prépare, et ce que chaque étape me met dans les mains.",
    "Je sais qu'un entrepreneur doit détenir une licence, et où elle se vérifie.",
    "Je sais que le permis se demande à ma municipalité, et à personne d'autre.",
    "Je distingue la cause du résultat quand on m'explique un problème.",
    "Je retrouve à quoi renvoient « le », « en » et « y » dans une explication suivie.",
    "Je comprends qu'un plus-que-parfait dit « c'était déjà fait avant ».",
    "Je fais la différence entre « faire faire » et « laisser faire ».",
    "Je lis un rapport d'inspection par sections, et je vais voir ses limites.",
    "Je trouve les exclusions d'une soumission avant de regarder le total.",
    "Je réunis deux phrases avec « où » — et j'écris « le jour où », jamais « le jour que ».",
    "J'emploie le subjonctif après « il faut que » et « j'aimerais que ».",
    "Je reconnais un passé simple dans un document et je le traduis.",
    "Je pose une hypothèse avec « si », sans mettre de futur juste après.",
    "Je pose une question précise, avec un chiffre, une date ou un document.",
    "Je peux redire à voix haute un diagnostic qu'on vient de m'expliquer.",
    "Je peux écrire un courriel en trois paragraphes qui met par écrit ce qui a été dit.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Les gens et les papiers du départ</div>
     <textarea rows="2" placeholder="Ex. : un entrepreneur général, une soumission, un corps de métier, un permis de rénovation…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Ce qui tient la maison debout</div>
     <textarea rows="2" placeholder="Ex. : la fondation, une fissure, une descente de gouttière, la pente du terrain…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Ce qu'on lit avant de signer</div>
     <textarea rows="2" placeholder="Ex. : un rapport d'inspection, le taux d'humidité, les exclusions, un échéancier…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Ce qu'on trouve en ouvrant</div>
     <textarea rows="2" placeholder="Ex. : une dalle de béton, une membrane, un imprévu, un acompte…"></textarea>
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
