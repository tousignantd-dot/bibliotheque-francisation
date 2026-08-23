  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : la conversation avec le voisin, le compte rendu de
  // cette conversation à un tiers, puis la mise en demeure. Le jeu de rôle
  // vient en premier parce que les deux autres en dépendent — on ne peut
  // rapporter que ce qu'on a dit, et on n'écrit qu'après avoir parlé.
  //
  // D'où viennent ces trois tâches. **De la situation elle-même**, sans
  // détour par les attentes de fin de cours : « Problèmes reliés à
  // l'habitation », au niveau 7, porte trois intentions — régler un problème
  // de voisinage en compréhension orale, le régler en production orale, et
  // rédiger une lettre pour régler un problème en production écrite. Le jeu
  // de rôle et la production orale portent les deux premières ; la lettre
  // porte la troisième. Les attentes de fin de cours ne font que préciser le
  // découpage : « il mène une conversation pour résoudre le problème et
  // rapporte aussi les éléments essentiels des propos de quelqu'un du
  // voisinage », et « il rédige une lettre en vue de régler un problème de
  // voisinage ». C'est écrit ici et dans le manifeste pour que la tâche ne
  // passe pas pour une invention hors programme.
  //
  // Seule la situation publique est ici ; ce que sait le voisin joué par
  // l'assistant vit dans server.py, scénario « voisinage ».
  const ROLE_CAS = [
    {id:'tapis', titre:'Le tapis roulant du matin', txt:"Depuis le <b>4 février</b>, l'appareil tourne de <b>5 h 45 à 6 h 25</b>, tous les matins de semaine, directement au-dessus de votre chambre. Vous rentrez du travail à minuit et quart. Vous avez <b>quinze matins notés</b> dans un carnet, avec l'heure du début et l'heure de la fin. Vous montez pour la première fois."},
    {id:'escalier', titre:'Le vélo dans la cage d\'escalier', txt:"Vers <b>6 h 30</b>, le guidon du vélo frappe la rampe à chaque marche. Cela dure <b>vingt secondes</b>, mais cela arrive juste au moment où vous veniez de vous rendormir. Votre voisin, lui, ne s'est jamais rendu compte que ça faisait du bruit — il n'y a rien à lui reprocher, seulement quelque chose à lui apprendre."},
    {id:'apres', titre:'Deux semaines plus tard', txt:"Le <b>caoutchouc a été posé le 26 février</b> et le vélo se descend à l'épaule depuis le lendemain de votre conversation. Mais l'appareil n'a <b>pas été déplacé</b>, et vous êtes réveillée <b>neuf matins sur quatorze</b>. Vous remontez : il faut reconnaître ce qui a été fait avant de redemander ce qui manque."},
  ];
  const ROLE_SUJETS = ["Saluer, se nommer, et dire pourquoi vous venez avant tout détail",
    "Décrire le bruit avec une heure, une durée et un nombre de jours",
    "Dire la conséquence sur votre vie : cela m'empêche de…, cela m'oblige à…",
    "Concéder quelque chose : même si votre horaire…, bien que je comprenne…",
    "Demander au conditionnel : accepteriez-vous, pourriez-vous",
    "Restreindre pour désamorcer : je ne me plains que du matin",
    "Proposer une solution précise, jamais « faites quelque chose »",
    "Faire confirmer ce qui est convenu, et fixer un moment pour se reparler"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Montez parler à votre voisin</span></div>
     <p class="lead">L'assistant joue <b>un voisin de vingt-neuf ans qui n'a rien fait de mal</b>. Il est poli, il ne se doutait qu'à moitié du problème, et il a de vraies contraintes : il part travailler à sept heures moins le quart. Il ne cédera rien à qui arrive avec un reproche, et il proposera de lui-même des solutions à qui arrive avec des heures. Vouvoyez-le du début à la fin.</p>
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
       Demandez au conditionnel :
       <span class='savoir-ex'><b>Accepteriez-vous</b> de mettre un tapis de caoutchouc ? · <b>Pourriez-vous</b> regarder si l'appareil rentre dans le couloir ?</span>
       Concédez d'abord, demandez ensuite :
       <span class='savoir-ex'><b>Même si</b> votre horaire est difficile, le mien l'est aussi. · <b>Bien que</b> je comprenne, je ne dors plus.</span>
       Dites la conséquence, pas l'émotion :
       <span class='savoir-ex'>Cela m'<b>empêche de</b> dormir plus de quatre heures. · Cela m'<b>oblige à</b> me lever à cinq heures trente.</span>
       Dites jusqu'où ça va :
       <span class='savoir-ex'>C'est <b>tellement</b> régulier <b>que</b> je me réveille avant. · C'est <b>assez</b> fort <b>pour</b> faire bouger le luminaire.</span>
       Restreignez pour désamorcer :
       <span class='savoir-ex'>Je <b>ne</b> me plains <b>que</b> du matin. · Je <b>ne</b> demande <b>qu'</b>une heure de sommeil de plus.</span>
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
         <button class="jr-opt on" type="button" data-role="ruslana" onclick="jrChoisir('role','ruslana')">La locataire qui ne dort plus</button>
         <button class="jr-opt" type="button" data-role="cedric" onclick="jrChoisir('role','cedric')">Le voisin qui court le matin</button>
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
     <h3 class="prod-tit">Racontez à quelqu'un ce que votre voisin vous a répondu</h3>
     <p class="prod-lead">Vous appelez votre propriétaire — ou vous en parlez à une collègue. Racontez en 90 secondes environ : ce qui se passe, ce que votre voisin vous a dit quand vous êtes montée le voir, et ce que vous comptez faire. Rapportez ses paroles au discours indirect au passé, et dites clairement ce qui est un fait et ce qui est votre conclusion.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">La situation, en trois phrases et avec des heures</div><div class="plan-ex">« Depuis le 4 février, le voisin du dessus fait fonctionner un tapis roulant de cinq heures quarante-cinq à six heures vingt-cinq, tous les matins de semaine. Cela m'empêche de dormir plus de quatre heures, et je travaille de quinze heures trente à vingt-trois heures trente. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Ce qu'il a dit, rapporté au passé</div><div class="plan-ex">« Je suis montée lui parler le 19 février. Il m'a dit qu'il avait acheté l'appareil en janvier et qu'il ne pouvait pas changer son heure de départ. Il m'a dit aussi qu'il mettrait du caoutchouc cette semaine-là, qu'il regarderait s'il pouvait le déplacer, et qu'il allait descendre son vélo à l'épaule. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Le fait, votre conclusion, puis la suite datée</div><div class="plan-ex">« Deux mesures sur trois ont été prises ; l'appareil n'a pas bougé. J'en conclus qu'il a oublié, mais ce n'est que ma lecture. Je lui réécris cette semaine et, s'il n'y a rien au 30 mars, je vous envoie une lettre. »</div></div>
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
     <h3 class="prod-tit">Écrivez la lettre qui demande à votre propriétaire d'intervenir</h3>
     <p class="prod-lead">Vous avez parlé au voisin, deux mesures sur trois ont été prises, et vous êtes encore réveillée neuf matins sur quatorze. Écrivez à votre propriétaire une lettre de 10 à 14 phrases, en <b>trois paragraphes</b> : ce qui se passe, ce que vous avez déjà fait vous-même, ce que vous demandez et dans quel délai. Un objet qui se comprend sans ouvrir la lettre.</p>
     <div class="req">
       <div class="req-hd">Votre lettre doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un objet court et précis, sans phrase complète</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Trois paragraphes séparés, un par idée</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Au moins quatre dates ou heures exactes</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une conséquence : « cela m'empêche de… » ou « cela m'oblige à… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une concession : « bien que… » ou « même si… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une citation exacte entre guillemets, annoncée par deux-points</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un connecteur de topicalisation : « quant à… », « en ce qui concerne… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une demande précise et un délai en toutes lettres</span></div>
       </div>
       <div class="req-note">N'écrivez pas ce que vous pensez de votre voisin, et n'écrivez pas que vous êtes épuisée : écrivez ce qui s'est passé, à quelles dates, ce que vous avez déjà tenté, et ce que vous demandez. Une lettre qui s'en tient aux faits et à un délai obtient une réponse ; une lettre qui raconte une fatigue se classe. Relisez-la trois fois et enlevez un adjectif à chaque fois.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">g.ostiguy@immeubles-8e-avenue.example</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">À vous de le trouver — court, et sans phrase complète</span></div>
       <textarea id="peText" rows="10" aria-label="Votre lettre" data-min="10" data-max="14" oninput="peCount()" placeholder="Madame Ostiguy,&#10;&#10;Depuis le 4 février, l'occupant du logement 6 fait fonctionner un tapis roulant chaque matin de semaine, de 5 h 45 à 6 h 25 environ, directement au-dessus de ma chambre…"></textarea>
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
    "Je sais nommer un trouble de voisinage sans accuser personne.",
    "Je distingue un inconvénient normal d'un trouble : l'heure, la durée, la répétition, l'endroit.",
    "Je sais qu'un registre tenu chaque jour vaut plus que tout ce que je pourrais raconter plus tard.",
    "Je dis la conséquence — cela m'empêche de…, cela m'oblige à… — plutôt que mon émotion.",
    "J'entends si le « e » du milieu se garde ou s'il tombe.",
    "Je demande au conditionnel : accepteriez-vous, pourriez-vous, je voudrais.",
    "Je concède avant de demander : même si…, bien que…, malgré…",
    "Je dis jusqu'où ça va : tellement… que, assez… pour, trop… pour.",
    "J'emploie « ne… que » pour restreindre sans nier.",
    "Je rapporte au passé ce qu'on m'a dit : il m'a dit qu'il avait…, qu'il ferait…, qu'il allait…",
    "Je reprends mon sujet autrement plutôt que de le répéter.",
    "Je sépare ce qui a été dit de ce que j'en conclus.",
    "Je sais que ma propriétaire est concernée parce que le voisin est aussi son locataire.",
    "Je sais ce que contient une mise en demeure : le problème, la demande, le délai.",
    "Je structure ma lettre en paragraphes et je la lie avec des connecteurs.",
    "Je cite exactement entre guillemets, ou je résume honnêtement sans guillemets.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Les mots du problème</div>
     <textarea rows="2" placeholder="Ex. : un trouble de voisinage, une nuisance sonore, la jouissance paisible, un inconvénient normal…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les mots de la conversation</div>
     <textarea rows="2" placeholder="Ex. : un palier, un arrangement à l'amiable, une concession, un reproche…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les mots de la preuve</div>
     <textarea rows="2" placeholder="Ex. : un registre des bruits, un témoin, la médiation citoyenne, le règlement municipal…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les mots de la lettre</div>
     <textarea rows="2" placeholder="Ex. : une mise en demeure, un délai raisonnable, un courrier recommandé, une diminution de loyer…"></textarea>
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
