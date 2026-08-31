  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : la discussion avec l'assistant, la description orale
  // corrigée, puis le courriel. Le jeu de rôle vient en premier parce qu'il
  // sert de répétition aux deux autres.
  // Seule la situation publique est ici ; ce que sait l'interlocuteur joué
  // par l'assistant vit dans server.py, scénario « reconnaitre ».
  const ROLE_CAS = [
    {id:'terminus', titre:'Kadiatou au terminus', txt:"Une femme de <b>trente-deux ans</b>, de taille moyenne, visage allongé, <b>cheveux ondulés en chignon bas</b>, lunettes rondes à monture dorée. Foulard vert, longue veste grise, <b>grosse valise rouge</b> à roulettes. Elle arrive vendredi à 14 h 40."},
    {id:'ousmane', titre:'Ousmane, qu\'on a vu deux fois', txt:"Un homme <b>très grand</b>, presque six pieds trois, mince, les épaules larges. <b>Crâne rasé</b> et petite barbe taillée court. Ghislain l'a rencontré deux fois il y a trois ans, quand il avait encore les cheveux longs."},
    {id:'rendezvous', titre:"Se reconnaître à deux", txt:"Ghislain aussi doit être reconnu : <b>dans la soixantaine</b>, cheveux blancs, <b>casquette bleu marine</b>, ancien manteau de travail brun. Il attendra <b>près du banc qui fait face au guichet</b>, du côté où arrivent les autobus du Nord."},
  ];
  const ROLE_SUJETS = ["Donner la silhouette avant tout le reste",
    "Dire ce que la personne portera, et quel bagage elle aura",
    "Décrire le visage et les cheveux, en détail",
    "Garder le signe particulier pour la fin",
    "Répondre aux demandes de précision sans te contredire",
    "Corriger toi-même ce que tu as mal dit",
    "Dire où se placer, avec « où » : le banc où, la porte où…"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Fais reconnaître quelqu'un que tu es seul à connaître</span></div>
     <p class="lead">L'assistant joue <b>celui qui va au terminus</b>. Il n'a jamais vu la personne, il est pressé, et il te redemande tout ce qui reste vague. À toi de décrire dans un ordre utile et de tenir ce que tu as dit.</p>
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
         <button class="jr-opt on" type="button" data-role="marisol" onclick="jrChoisir('role','marisol')">Celle qui décrit</button>
         <button class="jr-opt" type="button" data-role="ghislain" onclick="jrChoisir('role','ghislain')">Celui qui va au terminus</button>
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
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()">Commencer la discussion</button>
     </div>
     <div class="jr-rappel">
       <div class="jr-rappel-t">Réutilise ce que tu viens d'apprendre</div>
       <div class="jr-rappel-g">
         <div><div class="jr-rappel-l">Accorde tes adjectifs</div><div class="jr-rappel-x">une longue veste <b>grise</b>, des cheveux <b>ondulés</b>, des lunettes <b>rondes</b>.</div></div>
         <div><div class="jr-rappel-l">Attache la description au nom</div><div class="jr-rappel-x">une femme de taille moyenne <b>qui</b> tire une grosse valise rouge.</div></div>
         <div><div class="jr-rappel-l">Dis où, avec « où »</div><div class="jr-rappel-x">près du banc <b>où</b> les gens attendent, celui <b>qui</b> fait face au guichet.</div></div>
         <div><div class="jr-rappel-l">Ne répète pas, reprends</div><div class="jr-rappel-x">La valise ? Elle <b>en</b> a une seule, et elle est rouge.</div></div>
         <div><div class="jr-rappel-l">Place l'adjectif</div><div class="jr-rappel-x">C'est son <b>ancien</b> manteau de travail, pas un manteau <b>ancien</b>.</div></div>
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
     <h3 class="prod-tit">Décris quelqu'un pour qu'on le reconnaisse</h3>
     <p class="prod-lead">Quelqu'un que tu connais arrive quelque part et une autre personne doit aller le chercher. Décris-le en 90 secondes environ, dans l'ordre : la silhouette, ce qu'il portera, le visage et les cheveux, puis le signe particulier. Tu peux décrire Kadiatou, ou quelqu'un de ta vie.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">La silhouette, et l'âge à peu près</div><div class="plan-ex">« C'est une femme de taille moyenne, plutôt mince, dans la trentaine. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Les vêtements et le bagage</div><div class="plan-ex">« Elle portera un foulard vert et une longue veste grise, et elle tire une grosse valise rouge. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Le visage, les cheveux, puis le signe particulier</div><div class="plan-ex">« Elle a le visage allongé, des cheveux ondulés attachés en chignon bas, des lunettes rondes… et une petite cicatrice au-dessus du sourcil gauche. »</div></div>
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
     <h3 class="prod-tit">Réponds à Ousmane, et parle-lui de l'article</h3>
     <p class="prod-lead">Écris un courriel de 10 à 14 phrases, en <b>trois ou quatre paragraphes</b> : d'abord tu réagis à ses nouvelles et tu donnes les tiennes ; ensuite tu lui racontes un évènement de ton côté ; enfin tu l'informes de l'article de L'Écho de la Yamaska et tu dis ce que tu en penses, dans un paragraphe à part.</p>
     <div class="req">
       <div class="req-hd">Ton courriel doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un objet de trois à six mots, et une formule d'appel</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Trois ou quatre paragraphes séparés, un par idée</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une réaction à la bonne nouvelle et une à la triste, chacune avec le mot juste</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un évènement raconté de ton côté, avec une date ou une durée</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un plus-que-parfait : ce qui était déjà arrivé avant le reste</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une reprise sans répétition : le, en, y, celui-là</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Deux connecteurs différents : pourtant, d'ailleurs, c'est pourquoi…</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le résumé de l'article avec sa source, puis ton avis annoncé comme un avis</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une subordonnée relative avec « où »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une salutation et une signature</span></div>
       </div>
       <div class="req-note">Garde l'article pour un paragraphe à part, et annonce ton avis comme un avis. Un courriel qui mêle ce que le journal a écrit et ce que tu en penses n'informe personne : il donne une opinion en la faisant passer pour une nouvelle.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">ousmane.diallo@example.ca</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">À toi de le trouver — trois à six mots</span></div>
       <textarea id="peText" rows="12" aria-label="Ton courriel" data-min="10" data-max="14" oninput="peCount()" placeholder="Cher Ousmane,&#10;&#10;Quelle joie d'avoir enfin de tes nouvelles…"></textarea>
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
    "Je reconnais les parties d'un courriel et je sais ce que chacune m'apprend.",
    "Je compte les paragraphes d'un long texte avant de le lire.",
    "Je nomme les grands évènements de la vie : naissance, déménagement, accident, funérailles, mariage.",
    "Je réponds à une bonne nouvelle et à une mauvaise avec le mot juste.",
    "Je retrouve à quoi renvoient « le », « en » et « y » dans un texte suivi.",
    "Je comprends qu'un plus-que-parfait dit « c'était déjà fait ».",
    "Je remets des évènements dans l'ordre même sans dates.",
    "Je décris quelqu'un de loin vers près : silhouette, vêtements, visage, signe particulier.",
    "J'accorde mes adjectifs, même quand l'accord ne s'entend pas.",
    "Je sais qu'un adjectif change de sens selon sa place.",
    "Je réunis deux phrases avec « qui », « que » ou « où ».",
    "J'emploie « où » pour un lieu et pour un moment.",
    "Je reconnais un passé simple et je le remplace par un passé composé.",
    "Je lis les connecteurs et je devine ce qui s'en vient.",
    "Je lis le tiret et les guillemets sans me tromper de sens.",
    "Je peux écrire un courriel qui donne des nouvelles et qui informe du contenu d'un article.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Les évènements de la vie</div>
     <textarea rows="2" placeholder="Ex. : une naissance, un déménagement, des funérailles, un faire-part, un accident de travail…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Ce qu'on écrit en retour</div>
     <textarea rows="2" placeholder="Ex. : félicitations, toutes mes condoléances, bon rétablissement, vous vous y plaisez ?…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Décrire une personne</div>
     <textarea rows="2" placeholder="Ex. : une silhouette, un visage allongé, des cheveux ondulés, un signe particulier, de taille moyenne…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Le quartier et son journal</div>
     <textarea rows="2" placeholder="Ex. : un jumelage, un organisme communautaire, un bénévole, une coordonnatrice, un duo…"></textarea>
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
