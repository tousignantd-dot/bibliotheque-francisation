  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : la discussion avec l'assistant, le compte rendu oral
  // corrigé, puis le résumé écrit. Le jeu de rôle vient en premier parce
  // qu'il sert de répétition aux deux autres.
  // Seule la situation publique est ici ; ce que sait l'interlocuteur joué
  // par l'assistant vit dans server.py, scénario « cineclub ».
  const ROLE_CAS = [
    {id:'marees', titre:'Le film de ce soir', txt:"« Les Marées de novembre », d'Aurélie Pichette. Estelle revient vider la maison de sa mère en <b>trois jours</b>, et le film recule <b>quatre fois</b> jusqu'en novembre 1978. Trois signaux annoncent chaque retour en arrière : l'image, la musique, la mer."},
    {id:'critique', titre:'Les trois reproches du journal', txt:"Léo Charbonneau reproche au film sa <b>première demi-heure trop lente</b>, des <b>retours en arrière amenés trop discrètement</b>, et un <b>personnage de voisine qui arrive trop tard</b>. Il n'écrit jamais que c'est un mauvais film."},
    {id:'resume', titre:'Le résumé en deux paragraphes', txt:"Un résumé de film tient en <b>deux paragraphes</b> : le premier raconte l'histoire et <b>s'arrête avant le dénouement</b>, le second dit ce qu'on en pense et pourquoi. Mélanger les deux, c'est écrire une plainte."},
  ];
  const ROLE_SUJETS = ["Dire de quel film il s'agit et où tu l'as vu",
    "Raconter le déroulement dans l'ordre, sans dévoiler le dénouement",
    "Placer les retours en arrière au bon endroit",
    "Accorder un point à ton interlocuteur avant de lui répondre",
    "Appuyer chaque jugement sur un moment précis du film",
    "Poser une hypothèse avec « si », sans futur après « si »",
    "Annoncer ton avis comme un avis, et laisser la porte ouverte"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Discute du film avec quelqu'un qui ne l'a pas aimé</span></div>
     <p class="lead">L'assistant joue <b>quelqu'un qui a vu le film et qui l'a trouvé raté</b>. Il n'est pas de mauvaise foi : ses reproches sont précis et il attend les tiens. À toi de raconter, d'accorder ce qui est vrai, et de dire où tu n'es pas d'accord.</p>
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
         <button class="jr-opt on" type="button" data-role="therese" onclick="jrChoisir('role','therese')">Celle qui a aimé le film</button>
         <button class="jr-opt" type="button" data-role="critique" onclick="jrChoisir('role','critique')">Celui qui l'a trouvé raté</button>
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
         <div><div class="jr-rappel-l">Recule d'un cran</div><div class="jr-rappel-x">Elle arrive le soir : elle <b>avait pris</b> l'autobus du matin.</div></div>
         <div><div class="jr-rappel-l">Dis ce qui durait</div><div class="jr-rappel-x">Pendant qu'elle <b>vidait</b> la cuisine, la voisine <b>attendait</b>.</div></div>
         <div><div class="jr-rappel-l">Rattache un lieu ou un moment</div><div class="jr-rappel-x">Le village <b>où</b> elle avait grandi. L'année <b>où</b> le bateau est parti.</div></div>
         <div><div class="jr-rappel-l">Accorde avant de répondre</div><div class="jr-rappel-x"><b>C'est vrai que</b> le début est lent, <b>mais</b> c'est un parti pris.</div></div>
         <div><div class="jr-rappel-l">Annonce ton avis</div><div class="jr-rappel-x"><b>Pour ma part</b>, je trouve que la voisine arrive au bon moment.</div></div>
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
     <h3 class="prod-tit">Raconte le film à quelqu'un qui ne l'a pas vu</h3>
     <p class="prod-lead">Quelqu'un hésite à venir au ciné-club mercredi prochain. Raconte-lui le film en 90 secondes environ : de quel film il s'agit, le déroulement dans l'ordre — sans le dénouement —, puis ce que tu en as pensé, en bien et en moins bien.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">De quel film il s'agit, et où tu l'as vu</div><div class="plan-ex">« J'ai vu « Les Marées de novembre » mercredi soir, au ciné-club de la salle Beauchemin. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Le déroulement, dans l'ordre, sans la fin</div><div class="plan-ex">« Estelle revient vider la maison de sa mère. Elle avait pris l'autobus du matin, mais il est tombé en panne… »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Ce qui t'a convaincu, ce qui t'a moins convaincu</div><div class="plan-ex">« C'est vrai que le début est lent. Pour ma part, je trouve que c'est voulu, parce que… »</div></div>
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
     <h3 class="prod-tit">Écris ton résumé pour L'Écho de la Magog</h3>
     <p class="prod-lead">L'hebdomadaire publie deux ou trois réponses de lecteurs par semaine. Écris un texte de 8 à 12 phrases en <b>deux paragraphes séparés</b> : le premier raconte le film et s'arrête avant le dénouement ; le second dit ce que tu en penses, en accordant d'abord un point au critique.</p>
     <div class="req">
       <div class="req-hd">Ton texte doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Deux paragraphes séparés : l'histoire, puis l'avis</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le titre du film et l'endroit où tu l'as vu</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Aucun mot sur le dénouement</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un plus-que-parfait qui recule d'un cran</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un « où » qui rattache un lieu ou un moment</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une reprise sans répétition : ce film, cette scène, il en a…</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un point accordé au critique : c'est vrai que…, même si…</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un avis annoncé comme un avis : à mon avis, pour ma part…</span></div>
       </div>
       <div class="req-note">Sépare bien ce que le film raconte de ce que tu en penses. Un texte qui mêle les deux se lit comme une humeur ; un texte qui les sépare se lit comme un avis — et c'est celui-là que le journal publie.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">lecteurs@lechodelamagog.example</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">À toi de le trouver — court, et sans insulte</span></div>
       <textarea id="peText" rows="10" aria-label="Ton texte" data-min="8" data-max="12" oninput="peCount()" placeholder="Monsieur,&#10;&#10;J'ai vu « Les Marées de novembre » mercredi soir, au ciné-club de la salle Beauchemin…"></textarea>
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
    "Je reconnais les trois écrits qui entourent un film : la bande-annonce, la biographie, la critique.",
    "Je sais d'avance ce que chacun va me donner, et ce qu'il ne me donnera pas.",
    "Je choisis le mot précis : un long métrage, un court métrage, un documentaire, une série.",
    "Je repère un retour en arrière aux signaux du film, sans attendre qu'on me le dise.",
    "Je comprends qu'un plus-que-parfait recule d'un cran dans le passé.",
    "J'emploie l'imparfait pour ce qui était en train de se passer.",
    "Je remets les moments d'un film dans l'ordre de l'histoire.",
    "Je reconnais un passé simple dans une biographie et je le traduis dans ma tête.",
    "Je réunis deux phrases avec « où », pour un lieu comme pour un moment.",
    "Je retrouve à quoi renvoient « le », « en » et « y » dans un texte suivi.",
    "Je distingue l'idée principale d'un paragraphe de ses détails.",
    "Je lis ce qu'une critique dit vraiment, pas ce que je crois qu'elle dit.",
    "Je sais qu'un grand film et un film grand ne veulent pas dire la même chose.",
    "J'emploie le subjonctif après « il faut que », « je doute que », « il vaut mieux que ».",
    "J'accorde un point à quelqu'un avant de lui répondre.",
    "Je peux écrire un résumé de film en deux paragraphes, sans dévoiler la fin.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#3B49A0">Je retiens des mots</span><span class="ctit" style="color:#3B49A0">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#3B49A0" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#3B49A0;font-size:13px;margin:6px 0 4px">La salle et les formats</div>
     <textarea rows="2" placeholder="Ex. : un ciné-club, un long métrage, un court métrage, une bande-annonce, le générique…"></textarea>
     <div style="font-weight:800;color:#3B49A0;font-size:13px;margin:12px 0 4px">Le déroulement</div>
     <textarea rows="2" placeholder="Ex. : le déroulement, une scène, un retour en arrière, le dénouement…"></textarea>
     <div style="font-weight:800;color:#3B49A0;font-size:13px;margin:12px 0 4px">Faire un film</div>
     <textarea rows="2" placeholder="Ex. : une réalisatrice, un tournage, le montage, un premier rôle, une rétrospective…"></textarea>
     <div style="font-weight:800;color:#3B49A0;font-size:13px;margin:12px 0 4px">Dire ce qu'on en pense</div>
     <textarea rows="2" placeholder="Ex. : une critique, un reproche, convaincant, un parti pris, à mon avis, c'est vrai que…"></textarea>
   </div>
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#3B49A0">Autoévaluation</span><span class="ctit" style="color:#3B49A0">Qu'est-ce que je suis capable de faire ?</span></div>
     <p class="lead">Pour chaque énoncé, choisis : pas encore 😟, un peu 🙂, ou oui 😃.</p>
     ${SELF.map((s,i)=>`<div class="selfrow"><div class="self-txt">${s}</div><div class="self-opts">
        <button onclick="rate(${i},this)">😟</button><button onclick="rate(${i},this)">🙂</button><button onclick="rate(${i},this)">😃</button>
     </div></div>`).join('')}
     <div style="margin-top:16px"><button class="btn btn-pri" onclick="finishEval()">Terminer le module 🎉</button></div>
     <div id="evalDone" class="fb" aria-live="polite"></div>
   </div>`;
}
