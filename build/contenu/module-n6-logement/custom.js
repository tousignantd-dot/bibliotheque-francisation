  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : la discussion avec l'assistant, la description orale
  // de la démarche, puis le courriel au locateur. Le jeu de rôle vient en
  // premier parce qu'il sert de répétition aux deux autres.
  //
  // La situation « Location d'un logement » n'a, au niveau 6, **aucune**
  // intention de production : elle n'en a qu'une, de compréhension écrite.
  // Les deux tâches ci-dessous viennent donc des **attentes de fin de
  // cours**, qui sont communes au niveau et qui, elles, sont productives —
  // « il décrit les étapes d'une démarche administrative en donnant les
  // détails nécessaires » pour l'oral, « il rédige un court texte en
  // organisant ses idées à l'aide de paragraphes » et « dans ses relations
  // professionnelles, il rédige un courriel ou une lettre en respectant les
  // conventions habituelles » pour l'écrit. C'est écrit ici et dans le
  // manifeste pour que ces deux tâches ne passent pas pour une invention
  // hors programme.
  //
  // Seule la situation publique est ici ; ce que sait l'interlocuteur joué
  // par l'assistant vit dans server.py, scénario « souslocation ».
  const ROLE_CAS = [
    {id:'projet', titre:"Le projet, annoncé", txt:"Vous partez <b>six mois à Sept-Îles</b>, du 6 janvier au 30 juin. Vous voulez sous-louer votre logement du <b>5 janvier au 28 juin</b> à <b>Nicolas Trudel</b>, étudiant, dont vous avez le nom et l'adresse. Votre locateur ne sait encore rien."},
    {id:'refus', titre:'Le refus, à peser', txt:"Il a répondu le 29 novembre, <b>dans le délai</b>. Il invoque deux motifs : la personne est aux études, et elle a eu un <b>défaut de paiement</b> chez son ancien locateur. L'un des deux se vérifie, l'autre est une préférence."},
    {id:'frais', titre:'Les deux cents dollars', txt:"Il exige <b>200 $ de frais d'ouverture de dossier</b> avant d'examiner une autre candidature. La page du Tribunal parle du remboursement des <b>dépenses raisonnables que la sous-location occasionne</b> — pas d'un montant fixe décidé d'avance."},
  ];
  const ROLE_SUJETS = ["Dire de quoi il s'agit avant d'entrer dans les détails",
    "Nommer la personne proposée, avec son adresse",
    "Donner les dates exactes de la sous-location",
    "Rappeler le délai de quinze jours, sans menacer",
    "Dire que vous restez responsable du loyer",
    "Répondre à une objection sans hausser le ton",
    "Distinguer ce que le site écrit de ce que vous en pensez",
    "Proposer une suite concrète : une vérification, un rendez-vous, un écrit"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Défendez votre projet devant votre locateur</span></div>
     <p class="lead">L'assistant joue <b>un locateur méfiant qui a déjà été échaudé</b>. Il coupe, il demande où c'est écrit, et il est persuadé qu'un étudiant est un problème. À vous d'exposer la démarche, de donner vos dates et de tenir votre position sans vous fâcher. Vouvoyez-le du début à la fin.</p>
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
       Ne répétez pas le mot, reprenez-le :
       <span class='savoir-ex'>Le délai ? Vous <b>en</b> disposez jusqu'au 3 décembre, et vous <b>le</b> savez.</span>
       Rattachez un moment :
       <span class='savoir-ex'>Le 3 décembre est le jour <b>où</b> le délai prend fin.</span>
       Dites ce qu'il faut :
       <span class='savoir-ex'>Il faut <b>que</b> votre refus <b>soit</b> écrit.</span>
       Posez une condition :
       <span class='savoir-ex'><b>Si</b> vous ne <b>répondez</b> pas, la loi considère que vous consentez.</span>
       Citez au lieu d'affirmer :
       <span class='savoir-ex'>Ce n'est pas moi qui le dis : <b>selon</b> la page du Tribunal…</span>
     </div>

     <div class="jr-sep"></div>
     <div class="jr-sub">Choisissez votre situation et votre rôle</div>
     <div class="jr-choix">
       <div class="jr-choix-l">Quel moment ?</div>
       <div class="jr-opts" id="jrLogs">
         ${ROLE_CAS.map((c,i)=>`<button class="jr-opt${i===0?' on':''}" type="button" data-log="${c.id}" onclick="jrChoisir('log','${c.id}')">${esc(c.titre)}</button>`).join('')}
       </div>
       <div class="jr-choix-l">Vous jouez qui ?</div>
       <div class="jr-opts" id="jrRoles">
         <button class="jr-opt on" type="button" data-role="farida" onclick="jrChoisir('role','farida')">La locataire qui a lu</button>
         <button class="jr-opt" type="button" data-role="locateur" onclick="jrChoisir('role','locateur')">Le locateur méfiant</button>
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
     <h3 class="prod-tit">Décrivez les étapes de la démarche</h3>
     <p class="prod-lead">Quelqu'un de votre entourage doit s'absenter six mois et ne sait pas quoi faire de son logement. Expliquez-lui la démarche en 90 secondes environ : de quoi il s'agit et où vous l'avez lu, les étapes dans l'ordre avec les détails nécessaires — les dates surtout —, un exemple annoncé, puis ce que vous feriez à sa place.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">De quoi il s'agit, et d'où vous le savez</div><div class="plan-ex">« Quand on part pour un temps, on peut sous-louer son logement au lieu de le perdre. C'est écrit sur le site du Tribunal administratif du logement. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Les étapes, dans l'ordre, avec les délais</div><div class="plan-ex">« D'abord, vous trouvez quelqu'un. Ensuite, vous écrivez un avis avec son nom et son adresse. À partir du jour où le locateur le reçoit, il a quinze jours pour répondre. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Un exemple, puis ce que vous feriez</div><div class="plan-ex">« Prenons le refus : il faut un motif sérieux, par exemple un défaut de paiement au dossier. À votre place, je ferais signer la copie de l'avis. »</div></div>
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
     <h3 class="prod-tit">Écrivez le courriel qui accompagne votre avis</h3>
     <p class="prod-lead">Vous envoyez votre avis de sous-location à votre locateur et vous l'accompagnez d'un courriel. Écrivez un message de 8 à 12 phrases, en <b>trois paragraphes</b> : d'abord pourquoi vous écrivez, ensuite les faits — la personne, les dates, votre engagement —, enfin ce que vous demandez. Un objet qui se comprend sans ouvrir le message.</p>
     <div class="req">
       <div class="req-hd">Votre courriel doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un objet court et précis, sans phrase complète</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une formule d'appel qui nomme la personne, et une salutation fermée</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Trois paragraphes séparés, un par idée</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le nom et l'adresse de la personne proposée</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Les dates exactes de la sous-location</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une demande au conditionnel : « Pourriez-vous… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un « il faut que » ou un « je souhaite que » suivi du subjonctif</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une reprise sans répétition : « cet avis », « celui-ci », « en »</span></div>
       </div>
       <div class="req-note">N'écrivez pas ce que vous pensez du locateur : écrivez ce que vous faites, quand, et ce que vous attendez de lui. Un courriel qui s'en tient aux faits et aux dates est celui qui obtient une réponse écrite — et c'est la réponse écrite qui compte.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">l.tardif@immeubles-canardiere.example</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">À vous de le trouver — court, et sans phrase complète</span></div>
       <textarea id="peText" rows="10" aria-label="Votre courriel" data-min="8" data-max="12" oninput="peCount()" placeholder="Monsieur Tardif,&#10;&#10;Je vous transmets ci-joint mon avis de sous-location pour le logement 2, daté du 18 novembre…"></textarea>
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
    "Je distingue sous-louer, céder son bail et résilier son bail.",
    "Je sais qu'en sous-location, le bail reste à mon nom et que j'en réponds.",
    "Je reconnais les mots du contrat : locateur, clause, avis, délai, reconduction.",
    "J'entends la différence entre ch qui dit k, x qui dit s et sh qui dit ch.",
    "Je retrouve le verbe caché sous un nom : la résiliation, le consentement.",
    "Je lis les intertitres et l'encadré d'une page de droits avant le reste.",
    "Je repère le délai dans un texte officiel, même quand il est au milieu.",
    "Je retrouve à quoi renvoient « en » et « le » dans un texte suivi.",
    "J'écris « le jour où », « l'endroit où », et je choisis entre qui, que et où.",
    "Je reconnais un passé simple dans un texte écrit et je le dis autrement.",
    "J'annonce un exemple et j'annonce un avis avec le bon connecteur.",
    "Je comprends qu'un plus-que-parfait dit « c'était déjà fait avant ».",
    "J'emploie le subjonctif après « il faut que » et « je souhaite que ».",
    "Je pose une hypothèse avec « si », sans mettre de futur après « si ».",
    "Je peux décrire à voix haute les étapes d'une démarche, avec ses délais.",
    "Je peux écrire un courriel formel : objet, appel, trois paragraphes, demande, signature.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Les mots du contrat</div>
     <textarea rows="2" placeholder="Ex. : un locateur, un bail, une clause, un avis, un délai, la reconduction…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les trois démarches</div>
     <textarea rows="2" placeholder="Ex. : la sous-location, la cession de bail, la résiliation…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Ce que dit le site</div>
     <textarea rows="2" placeholder="Ex. : un motif sérieux, les obligations, les dépenses raisonnables, le consentement…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Quand ça se discute</div>
     <textarea rows="2" placeholder="Ex. : un accusé de réception, une indemnité, des dommages, un défaut de paiement…"></textarea>
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
