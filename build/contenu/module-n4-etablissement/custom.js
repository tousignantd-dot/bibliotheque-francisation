  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : l'appel au secrétariat avec l'assistant, le message
  // laissé dans la boîte vocale du centre, puis la note écrite remise au
  // comptoir. Le jeu de rôle vient en premier parce qu'il sert de
  // répétition aux deux autres — c'est là que l'élève découvre que « je ne
  // peux pas venir » ne dit ni la durée, ni la nature, ni la date.
  //
  // Le scénario `repondeur` a été ajouté à server.py pour ce module. Aucun
  // scénario existant ne convenait : `secretariat` (niveau 3) et `ecole`
  // (niveau 5) se passent au comptoir, `conge` s'adresse à un chef
  // d'équipe, et `absence` (niveau 2) est un échange de quatre répliques
  // avec l'enseignante. Ici, on téléphone, et la personne au bout du fil
  // n'a rien sous les yeux : ni le nom, ni le groupe, ni la date. Seule la
  // situation publique est ici ; ce que madame Sansregret voit à l'écran et
  // ce qu'elle exige avant d'inscrire quoi que ce soit vivent sur le
  // serveur.
  const ROLE_CAS = [
    {id:'garderie', titre:"L'enfant malade", txt:"Votre enfant de cinq ans a <b>une otite</b> et vous avez un rendez-vous à la clinique <b>ce matin à neuf heures</b>. Vous serez absente toute la journée. Vous voulez que l'absence soit inscrite comme motivée, savoir quel papier apporter et pour quand, et savoir ce que vous manquerez en classe."},
    {id:'autobus', titre:"L'autobus qui ne passe pas", txt:"Il neige depuis cinq heures du matin et <b>votre autobus n'est pas passé</b>. Vous arriverez vers <b>neuf heures et demie</b>, avec une heure et demie de retard. Vous voulez prévenir avant le début du cours, savoir si l'on vous attend quand même, et savoir ce qui aura été fait avant votre arrivée."},
    {id:'soir', titre:"Le cours du soir qu'on arrête", txt:"Vous suivez la francisation le jour <b>et</b> un cours d'informatique le soir. Vos horaires ont changé et <b>vous ne pouvez plus venir le soir</b>, à partir du 1er octobre. Vous voulez abandonner ce cours-là seulement, savoir si cela paraîtra à votre relevé, et savoir si vous pourrez vous réinscrire plus tard."},
  ];
  const ROLE_SUJETS = ["Se nommer et donner son groupe dans la première phrase",
    "Dire en un mot de quoi il s'agit : un retard, une absence ou un abandon",
    "Donner la date exacte, jamais « aujourd'hui » tout seul",
    "Donner le motif en une seule phrase, avec parce que ou à cause de",
    "Demander quel papier apporter, et pour quand",
    "Dire au futur ce que vous ferez : je serai là, je remettrai, je rattraperai",
    "Redire à voix haute ce que vous avez compris avant de raccrocher",
    "Laisser votre numéro si l'on doit vous rappeler",
    "Vouvoyer du début à la fin, et remercier"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Téléphoner au secrétariat</span></div>
     <p class="lead">Cette fois, quelqu'un décroche. L'assistant joue madame Murielle Sansregret, au secrétariat du Centre d'éducation des adultes de la Pointe-aux-Ormes. Elle est aimable et rapide : il y a deux autres lignes qui clignotent. Elle ne voit rien de vous — pas votre visage, pas votre dossier tant que vous ne vous êtes pas nommée. Elle ne devine rien non plus : si vous dites seulement « je ne peux pas venir », elle vous demandera si c'est un retard, une absence ou un abandon, et pour quelle date.</p>
     <p class="lead">Choisissez votre appel</p>
     <div class="jr-annonces" id="jrLogs">
       ${ROLE_CAS.map((c,i)=>`<button class="jr-opt jr-tuile${i===0?' on':''}" type="button" data-log="${c.id}" onclick="jrChoisir('log','${c.id}')">
         <span class="jr-band"><span class="jr-band-off">Choix ${i+1}</span><span class="jr-band-on"><svg viewBox="0 0 20 20" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 10.5l4 4 8-9"></path></svg> Votre choix</span></span>
         <span class="jr-tuile-c"><span class="jr-tuile-t">${esc(c.titre)}</span><span class="jr-tuile-d">${c.txt}</span></span>
       </button>`).join('')}
     </div>
     <div class="jr-reglages">
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
         <div class="jr-bande-t">Les neuf choses à faire avant de raccrocher</div>
         <p class="jr-bande-p">${ROLE_SUJETS.map((s,i)=>i?s.charAt(0).toLowerCase()+s.slice(1):s).join(', ')}.</p>
       </div>
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()">Composer le 450 555-0180</button>
     </div>
     <div class="jr-rappel">
       <div class="jr-rappel-t">Réutilisez ce que vous venez d'apprendre</div>
       <div class="jr-rappel-g">
         <div><div class="jr-rappel-l">Nommez la case, pas votre embarras</div><div class="jr-rappel-x">Je vous appelle pour signaler <b>une absence</b>. · J'aurai <b>un retard</b> d'une heure. · Je vous écris pour <b>abandonner</b> le cours du soir.</div></div>
         <div><div class="jr-rappel-l">Donnez la raison avec le bon outil</div><div class="jr-rappel-x">Je serai absente <b>parce que</b> mon fils est malade. · J'arriverai plus tard <b>à cause de</b> l'autobus. · <b>Grâce à</b> votre message, je l'ai su à temps.</div></div>
         <div><div class="jr-rappel-l">Promettez au futur simple</div><div class="jr-rappel-x">Je <b>serai</b> en classe demain. Je vous <b>remettrai</b> le papier jeudi. Je <b>rattraperai</b> la matière au local 214.</div></div>
         <div><div class="jr-rappel-l">Dites l'obligation comme il faut</div><div class="jr-rappel-x">Je <b>dois</b> vous remettre une note. · <b>Il faut</b> téléphoner avant huit heures. · <b>Il faudrait</b> que je passe au comptoir.</div></div>
         <div><div class="jr-rappel-l">Remplacez le nom par le pronom</div><div class="jr-rappel-x">Je <b>lui</b> remettrai la note jeudi. · Je vais <b>lui</b> demander. · Rappelez-<b>moi</b> avant midi.</div></div>
         <div><div class="jr-rappel-l">Rangez les choses dans le temps</div><div class="jr-rappel-x"><b>D'abord</b>, je me nomme. <b>Ensuite</b>, je dis quel jour. <b>Enfin</b>, je laisse mon numéro. · <b>Avant de</b> raccrocher, je redis ce que j'ai compris.</div></div>
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
     <h3 class="prod-tit">Le message laissé dans la boîte vocale du centre</h3>
     <p class="prod-lead">Il est sept heures dix. Vous ne pourrez pas être au cours aujourd'hui, ou vous arriverez très en retard. Le bureau du centre n'ouvre qu'à huit heures : vous tombez sur la boîte vocale. Vous avez une minute, personne ne vous voit, et personne ne pourra vous poser de question. Écrivez d'abord votre message, lisez-le à voix haute, puis enregistrez-le. De quarante-cinq à soixante secondes — cinq morceaux, dans l'ordre.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Qui vous êtes : nom complet, groupe, cours</div><div class="plan-ex">« Bonjour, ici Nourhane Ouazzani, groupe 6, francisation de jour. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Le mot du motif et la date exacte</div><div class="plan-ex">« Je vous appelle pour signaler mon absence aujourd'hui, lundi le 14 septembre. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">La raison, en une seule phrase</div><div class="plan-ex">« Mon fils a une otite et j'ai un rendez-vous à la clinique à neuf heures. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 4</div><div class="plan-t">Ce que vous ferez, au futur</div><div class="plan-ex">« Je serai en classe demain matin et je remettrai le papier de la clinique jeudi. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 5</div><div class="plan-t">Votre numéro, deux fois, lentement</div><div class="plan-ex">« Vous pouvez me rappeler au 450 555-0147. Je répète : 450 555-0147. Merci, bonne journée. »</div></div>
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
           <div class="rec-hint">De quarante-cinq à soixante secondes. Réécoutez-vous comme si vous étiez la personne du secrétariat, à huit heures, avec quarante messages à passer : savez-vous qui appelle dès la première phrase ? Avez-vous la date exacte ? Pourriez-vous écrire le numéro sans réécouter ?</div>
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
     <h3 class="prod-tit">La note que vous remettez au comptoir</h3>
     <p class="prod-lead">Le message enregistré a prévenu ; la note, elle, justifie. C'est le papier que le secrétariat classe dans votre dossier, et c'est lui qui fait passer votre absence de « signalée » à « motivée ». Cinq ou six lignes, datées et signées. De 6 à 9 phrases, avec « vous ».</p>
     <div class="req">
       <div class="req-hd">Votre note doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>La ville et la date sur la première ligne</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>À qui vous écrivez : « Madame, Monsieur » ou le secrétariat</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Votre nom complet et votre groupe</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le jour exact du retard, de l'absence ou de l'abandon</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le motif au passé composé, avec « parce que » ou « à cause de »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce que vous ferez, au futur simple : je remettrai, je rattraperai, je serai</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une formule de fin, votre nom écrit en toutes lettres, votre signature</span></div>
       </div>
       <div class="req-note">Relisez à voix haute avant de remettre : c'est ainsi que Nourhane a entendu son « je suis allé » sans e. Et faites-en une copie ou une photo — le jour où le dossier dira le contraire, c'est elle qui tranchera.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">Remis à</span><span class="mail-v">Secrétariat — Centre d'éducation des adultes de la Pointe-aux-Ormes</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Justification d'une absence — groupe 6, francisation de jour</span></div>
       <textarea id="peText" rows="10" aria-label="Votre note" data-min="6" data-max="9" oninput="peCount()" placeholder="Laval, le… &#10;&#10;Madame, Monsieur,&#10;&#10;Je suis… , du groupe 6 en francisation de jour. J'ai été absente le…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 6 à 9</span>
         <button class="btn-prod" id="peBtn" type="button" onclick="peCheck()">Vérifier ma note</button>
       </div>
     </div>
     <div class="fb" id="peFb" aria-live="polite"></div>
     <div class="status" id="peStatus">Analyse en cours…</div>
     <div class="err" id="peErr"></div>
   </div>`;
  const rb=document.getElementById('recBtn'); if(rb) rb.addEventListener('click',toggleRec);

  // JE RETIENS DES MOTS — notes + cartes mémoire + autoévaluation
  const SELF=[
    "Je connais les mots du téléphone : la ligne, le clavier, le poste, la boîte vocale.",
    "Je comprends un menu automatisé et je sais sur quelle touche appuyer.",
    "J'entends la différence entre le son de bonjour, celui d'absence et celui de matin.",
    "Je dis mon nom et mon groupe lentement, et je peux épeler mon nom.",
    "Je choisis le bon mot : un retard, une absence, un abandon, un empêchement.",
    "Je laisse un message complet en une minute, dans le bon ordre.",
    "Je donne la date exacte au lieu de dire seulement « aujourd'hui ».",
    "Je laisse mon numéro deux fois, par groupes de chiffres.",
    "Je comprends les consignes à l'impératif : appuyez, laissez, ne quittez pas.",
    "J'emploie « je dois », « il faut » et « il faudrait » sans les confondre.",
    "J'écoute un message et j'en tire qui appelle, pourquoi, et ce qu'il faut faire.",
    "Je donne une raison avec « parce que », « à cause de » ou « grâce à ».",
    "Je remplace le nom d'une personne par « lui » ou par « leur ».",
    "J'écris le passé composé avec être et j'accorde le participe passé.",
    "Je reconnais le futur simple et je l'emploie pour dire ce que je ferai.",
    "J'écris une note datée et signée, et j'en garde une copie.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Le téléphone et la ligne</div>
     <textarea rows="2" placeholder="Ex. : la boîte vocale, un répondeur, le clavier, la ligne, décrocher, raccrocher…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Le message qu'on laisse</div>
     <textarea rows="2" placeholder="Ex. : un poste, le signal sonore, un message, les coordonnées, épeler, rappeler…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les motifs</div>
     <textarea rows="2" placeholder="Ex. : un retard, une absence, un abandon, un empêchement, motivé, justifier…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">La note écrite</div>
     <textarea rows="2" placeholder="Ex. : une note, un motif, une signature, une copie, remettre, agréer…"></textarea>
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
