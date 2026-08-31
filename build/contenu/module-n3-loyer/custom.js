  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, un court message écrit. Le jeu de rôle vient en premier
  // parce qu'il sert de répétition avant les deux autres.
  // Seule la situation publique est côté client — l'annonce, que les deux
  // ont sous les yeux. Ce que sait la propriétaire vit dans server.py,
  // scénario `visite`.
  const ROLE_CAS = [
    {id:'chabot', titre:'Le 4 ½ de la rue Chabot', txt:"<b>4 ½ à louer, rue Chabot, Villeray. 2e étage.</b> Deux chambres fermées, cuisine avec balcon arrière. Chauffé, éclairé. Non meublé. Buanderie au sous-sol. Pas de stationnement. Libre le 1er juillet. <b>1 150 $ par mois.</b>"},
    {id:'soussol', titre:'Le 3 ½ au sous-sol', txt:"<b>3 ½ au sous-sol, rue de Bellechasse, Rosemont.</b> Une chambre fermée. Laveuse et sécheuse incluses. <b>Non chauffé.</b> Chat accepté. Libre le 1er août. <b>850 $ par mois.</b>"},
    {id:'meuble', titre:'Le 2 ½ meublé', txt:"<b>2 ½ meublé, rue Saint-Hubert, près du métro.</b> Meublé et chauffé, électricité comprise. Internet non compris. Libre immédiatement. <b>780 $ par mois.</b>"},
  ];
  const ROLE_SUJETS = ["Saluer et dire que tu viens pour l'annonce",
    "Dire combien de personnes vont habiter le logement",
    "Demander ce qui est compris dans le loyer",
    "Demander combien il y a de chambres fermées",
    "Demander où sont la buanderie et le stationnement",
    "Demander à quelle date le logement est libre",
    "Faire répéter si tu n'as pas compris un chiffre ou une date",
    "Répéter le loyer et la date à voix haute avant de partir"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Visite le logement et pose tes questions</span></div>
     <p class="lead">L'assistant tient <b>le rôle de la personne qui fait visiter</b>. Elle ne dit rien que tu ne lui demandes pas : le chauffage, les chambres, la buanderie, la date, tout se demande. À toi de poser tes questions.</p>
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
         <button class="jr-opt on" type="button" data-role="locataire" onclick="jrChoisir('role','locataire')">La personne qui visite</button>
         <button class="jr-opt" type="button" data-role="proprietaire" onclick="jrChoisir('role','proprietaire')">La propriétaire</button>
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
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()">Commencer la conversation</button>
     </div>
     <div class="jr-rappel">
       <div class="jr-rappel-t">Réutilise ce que tu viens d'apprendre</div>
       <div class="jr-rappel-g">
         <div><div class="jr-rappel-l">Entre poliment</div><div class="jr-rappel-x"><b>Je voudrais</b> visiter le logement, s'il vous plaît.</div></div>
         <div><div class="jr-rappel-l">Demande ce qui est compris</div><div class="jr-rappel-x"><b>Est-ce que</b> le chauffage <b>est compris</b> dans le loyer ?</div></div>
         <div><div class="jr-rappel-l">Demande où</div><div class="jr-rappel-x">Les chambres sont <b>au fond du</b> couloir ?</div></div>
         <div><div class="jr-rappel-l">Comprends une réponse négative</div><div class="jr-rappel-x"><b>Il n'y a pas de</b> stationnement.</div></div>
         <div><div class="jr-rappel-l">Annonce ce que tu vas faire</div><div class="jr-rappel-x"><b>Je vais</b> y penser et <b>je vais</b> vous rappeler demain.</div></div>
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
         <button class="btn btn-send" type="button" onclick="jrFini()">J'ai fini — corrige mes phrases</button>
       </div>
       <div class="fb" id="jrFb" aria-live="polite"></div>
     </div>
   </div>

   <div class="card custom">
     <div class="prod-eyebrow"><span class="prod-num">1</span><span class="prod-kind">Production orale</span></div>
     <h3 class="prod-tit">Téléphone pour l'annonce</h3>
     <p class="prod-lead">Tu appelles au sujet d'une petite annonce de logement. Salue, dis pourquoi tu appelles, pose tes trois questions — ce qui est compris, combien de chambres, à quelle date c'est libre —, demande un rendez-vous, puis répète le jour et l'heure avant de raccrocher.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Dire pourquoi tu appelles</div><div class="plan-ex">« Bonjour, madame. Je vous appelle pour l'annonce du quatre et demie. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Poser tes trois questions</div><div class="plan-ex">« Est-ce que le chauffage est compris ? Combien il y a de chambres ? À quelle date c'est libre ? »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Prendre rendez-vous et répéter</div><div class="plan-ex">« Est-ce que je pourrais le visiter samedi ? … Samedi, dix heures, rue Chabot. C'est bien ça ? »</div></div>
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
           <div class="rec-hint">Parle environ 45 secondes. Tu pourras recommencer autant de fois que tu veux.</div>
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
     <h3 class="prod-tit">Écris à quelqu'un de ta famille</h3>
     <p class="prod-lead">Tu viens de visiter le logement. Écris un court message à une personne de ta famille pour lui dire ce que tu as vu : le nombre de pièces, le loyer, ce qui est compris, la date, et une chose qui manque. De 5 à 8 phrases.</p>
     <div class="req">
       <div class="req-hd">Ton message doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le nombre de pièces : un 3 ½, un 4 ½</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le loyer, écrit en chiffres avec le signe $ après le nombre</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce qui est compris, avec « chauffé », « éclairé » ou « compris »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Où se trouve une pièce, avec « au fond de », « à côté de » ou « au »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une chose qui manque, avec « il n'y a pas de… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce que tu vas faire, avec « je vais… »</span></div>
       </div>
       <div class="req-note">Attention aux petits mots : <em>une</em> cuisine, <em>un</em> balcon, la cuisine est chauffé<em>e</em>, il n'y a pas <em>de</em> stationnement, il n'y a pas <em>d'</em>ascenseur.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">Pour</span><span class="mail-v">Ma famille</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Le logement que j'ai visité</span></div>
       <textarea id="peText" rows="7" aria-label="Ton message" data-min="5" data-max="8" oninput="peCount()" placeholder="Bonjour. Aujourd'hui, j'ai visité un…&#10;Le loyer est de…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 5 à 8</span>
         <button class="btn-prod" id="peBtn" type="button" onclick="peCheck()">Vérifier mon message</button>
       </div>
     </div>
     <div class="fb" id="peFb" aria-live="polite"></div>
     <div class="status" id="peStatus">Analyse en cours…</div>
     <div class="err" id="peErr"></div>
   </div>`;
  const rb=document.getElementById('recBtn'); if(rb) rb.addEventListener('click',toggleRec);

  // JE RETIENS DES MOTS — notes + cartes mémoire + autoévaluation
  const SELF=[
    "Je peux nommer les pièces d'un logement : le salon, la cuisine, la chambre, la salle de bain, le balcon.",
    "Je sais ce qu'est un trois et demie et un quatre et demie.",
    "Je comprends les abréviations d'une petite annonce : 4 ½, 2e ét., ch. et écl., s.-sol, stat.",
    "Je comprends « chauffé », « éclairé » et « non meublé ».",
    "Je peux dire et écrire un loyer : mille cent cinquante dollars, 1 150 $.",
    "Je peux téléphoner et dire pourquoi j'appelle.",
    "Je peux poser mes trois questions : ce qui est compris, les chambres, la date.",
    "Je peux demander un rendez-vous et répéter le jour et l'heure.",
    "Je peux dire où se trouve une pièce : au fond du couloir, à côté de la salle de bain, au sous-sol.",
    "Je comprends une réponse négative : il n'y a pas de stationnement, il n'y a pas d'ascenseur.",
    "Je sais qu'un dépôt de garantie est interdit et qu'un bail dure douze mois.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Les pièces du logement</div>
     <textarea rows="2" placeholder="Ex. : un salon, une cuisine, une chambre à coucher, une salle de bain, un balcon, un sous-sol…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">L'annonce et le prix</div>
     <textarea rows="2" placeholder="Ex. : une petite annonce, un 4 ½, chauffé, éclairé, non meublé, libre le 1er juillet, 1 150 $…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Téléphoner</div>
     <textarea rows="2" placeholder="Ex. : je vous appelle pour l'annonce, je voudrais…, j'aimerais…, est-ce que je pourrais…, je vais venir…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Pendant la visite</div>
     <textarea rows="2" placeholder="Ex. : au fond du couloir, à côté de la salle de bain, au sous-sol, il n'y a pas de…, le bail, le premier loyer…"></textarea>
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
