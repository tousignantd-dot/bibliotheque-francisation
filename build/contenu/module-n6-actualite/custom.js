  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : la discussion avec l'assistant, le compte rendu oral
  // corrigé, puis le courriel au courrier des lecteurs. Le jeu de rôle vient
  // en premier parce qu'il sert de répétition aux deux autres.
  // Seule la situation publique est ici ; ce que sait l'interlocuteur joué par
  // l'assistant vit dans server.py, scénario « chroniquepratique ».
  const ROLE_CAS = [
    {id:'laveuse', titre:'La laveuse de Nadège', txt:"Une laveuse de <b>780 $</b> a cessé de vidanger après <b>trois ans et quatre mois</b>. La garantie du fabricant, d'un an, est expirée depuis longtemps. Le marchand dit qu'il n'y peut rien."},
    {id:'demarche', titre:'Les trois étapes', txt:"La chronique donnait une démarche : <b>retourner voir le commerçant</b> en nommant la garantie légale, puis <b>écrire une mise en demeure</b> avec un délai de dix jours, puis <b>les petites créances</b> pour 15 000 $ ou moins."},
    {id:'pieces', titre:"La pièce qui n'arrive pas", txt:"Le technicien est venu deux fois et attend une <b>pièce de rechange</b> depuis cinq semaines. L'appareil n'est pas mal fait : il est <b>irréparable faute de pièce</b>, ce qui n'est pas la même chose."},
  ];
  const ROLE_SUJETS = ["Dire de quoi il s'agit et où tu l'as entendu",
    "Résumer la chronique en trois ou quatre phrases",
    "Nommer les étapes dans l'ordre, sans en sauter",
    "Illustrer un point par un exemple",
    "Répondre à une objection sans rejeter la personne",
    "Poser une hypothèse avec « si »",
    "Terminer par ton point de vue, annoncé comme un point de vue"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Explique la démarche à quelqu'un qui doute</span></div>
     <p class="lead">L'assistant joue <b>un collègue qui n'a rien écouté et qui n'y croit pas</b>. Il t'interrompt, il te demande d'où tu tiens ça, et il trouve que c'est trop compliqué. À toi de résumer, d'ordonner les étapes et d'illustrer.</p>
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
         <button class="jr-opt on" type="button" data-role="nadege" onclick="jrChoisir('role','nadege')">Celle qui a écouté</button>
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
         <div class="jr-bande-t">Les sept sujets à couvrir</div>
         <p class="jr-bande-p">${ROLE_SUJETS.map((s,i)=>i?s.charAt(0).toLowerCase()+s.slice(1):s).join(', ')}.</p>
       </div>
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()">Commencer la discussion</button>
     </div>
     <div class="jr-rappel">
       <div class="jr-rappel-t">Réutilise ce que tu viens d'apprendre</div>
       <div class="jr-rappel-g">
         <div><div class="jr-rappel-l">Ne répète pas le mot, reprends-le</div><div class="jr-rappel-x">La garantie légale ? Tout le monde <b>en</b> a une, et personne ne <b>le</b> sait.</div></div>
         <div><div class="jr-rappel-l">Place les étapes</div><div class="jr-rappel-x">D'abord tu <b>retournes</b> voir le marchand ; <b>si</b> ça ne bouge pas, tu écris.</div></div>
         <div><div class="jr-rappel-l">Illustre</div><div class="jr-rappel-x"><b>Prenons</b> une laveuse de sept cent quatre-vingts dollars.</div></div>
         <div><div class="jr-rappel-l">Dis ce qu'il faut</div><div class="jr-rappel-x">Il faut <b>que</b> tu <b>gardes</b> ta facture.</div></div>
         <div><div class="jr-rappel-l">Annonce ton avis</div><div class="jr-rappel-x"><b>À mon avis</b>, trois ans, ce n'est pas une durée raisonnable.</div></div>
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
     <h3 class="prod-tit">Explique la démarche à un collègue</h3>
     <p class="prod-lead">Quelqu'un de ton entourage a un appareil brisé et ne sait pas quoi faire. Explique-lui en 90 secondes environ : de quoi il s'agit, les étapes dans l'ordre avec les détails nécessaires, un exemple, puis ce que tu en penses.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">De quoi il s'agit, et d'où tu le sais</div><div class="plan-ex">« J'ai écouté une chronique pratique mardi matin, à la radio, sur la garantie légale. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Les étapes, dans l'ordre, avec les détails</div><div class="plan-ex">« D'abord, tu retournes voir le commerçant. Si ça ne bouge pas, tu écris une mise en demeure avec un délai de dix jours. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Un exemple, puis ton point de vue</div><div class="plan-ex">« Prenons une laveuse de 780 $… À mon avis, trois ans, ce n'est pas une durée raisonnable. »</div></div>
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
     <h3 class="prod-tit">Écris au courrier des lecteurs</h3>
     <p class="prod-lead">Le Courrier de la Batture publie les lettres signées. Écris un courriel de 8 à 12 phrases, en <b>deux ou trois paragraphes</b> : d'abord ce que la chronique disait, pour ceux qui ne l'ont pas entendue ; ensuite ton point de vue ; enfin ce que tu demandes ou ce que tu proposes.</p>
     <div class="req">
       <div class="req-hd">Ton courriel doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une formule d'appel et une formule de salutation</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Deux ou trois paragraphes séparés, un par idée principale</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un résumé des étapes, dans l'ordre, avec au moins un chiffre</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un connecteur d'exemplification : par exemple, notamment, ainsi</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une hypothèse en « si » — sans futur après « si »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un connecteur de point de vue : à mon avis, pour ma part…</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une reprise sans répétition : « cette machine », « ce refus »…</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un « il faut que » suivi du subjonctif</span></div>
       </div>
       <div class="req-note">Sépare bien ce que la chronique disait de ce que tu en penses. Une lettre qui mêle les deux se lit comme une plainte ; une lettre qui les sépare se lit comme un point de vue — et c'est celle-là que le journal publie.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">courrier@lecourrierdelabatture.example</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">À toi de le trouver — court, et sans jugement</span></div>
       <textarea id="peText" rows="10" aria-label="Ton courriel" data-min="8" data-max="12" oninput="peCount()" placeholder="Monsieur le rédacteur en chef,&#10;&#10;J'ai écouté avec intérêt la chronique du 12 août sur la garantie légale…"></textarea>
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
    "Je reconnais les cinq genres : chronique pratique, entrevue, documentaire, fait divers, courrier des lecteurs.",
    "Je sais d'avance ce qu'un genre va me donner, et ce qu'il ne me donnera pas.",
    "Je lis le tiret et les guillemets sans me tromper de sens.",
    "Je retrouve à quoi renvoient « le », « en » et « y » dans un texte suivi.",
    "Je réunis deux phrases en une avec « qui », « que » ou « où ».",
    "Je repère les connecteurs qui annoncent un exemple.",
    "Je retiens l'ordre des étapes d'une démarche, même sans « ensuite ».",
    "Je comprends qu'un plus-que-parfait dit « c'était déjà fait ».",
    "Je reconnais un passé simple dans un documentaire et je le traduis.",
    "J'emploie le subjonctif après « il faut que », « je souhaite que ».",
    "Je choisis entre « de » et un infinitif, ou « que » et un subjonctif.",
    "Je pose une hypothèse avec « si », sans mettre de futur après « si ».",
    "J'annonce mon point de vue comme un point de vue.",
    "Je reprends un mot sans le répéter trois fois.",
    "Je peux expliquer une démarche en étapes à quelqu'un qui n'a rien écouté.",
    "Je peux écrire au courrier des lecteurs, en paragraphes.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Les genres de l'information</div>
     <textarea rows="2" placeholder="Ex. : une chronique pratique, un documentaire, une entrevue, un fait divers, le courrier des lecteurs…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">La garantie et les recours</div>
     <textarea rows="2" placeholder="Ex. : la garantie légale, une durée raisonnable, une pièce de rechange, une mise en demeure, un recours…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">L'enquête et le documentaire</div>
     <textarea rows="2" placeholder="Ex. : un témoignage, une enquête, l'obsolescence programmée, un organisme public…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Donner son point de vue</div>
     <textarea rows="2" placeholder="Ex. : une lettre ouverte, un point de vue, à mon avis, pour ma part, selon, paraît-il…"></textarea>
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
