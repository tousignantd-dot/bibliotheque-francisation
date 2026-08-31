  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, un courriel écrit. Le jeu de rôle vient en premier parce
  // qu'il sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait le personnage
  // joué par l'assistant vit dans server.py.
  const ROLE_CAS = [
    {id:'manteau', titre:"Le manteau d'hiver", txt:"Trois hivers en <b>trois couches</b> de vêtements. Cette fois, tu veux un vrai manteau — mais tu ne connais pas ta taille dans les marques d'ici."},
    {id:'bottes', titre:"Les bottes", txt:"Tu fais du <b>neuf et demi</b>, mais tes souliers d'ici te semblent serrés. Et tu ne sais pas ce qui compte pour la neige et le verglas."},
    {id:'echange', titre:"L'échange", txt:"Un article qui ne fait pas la bonne taille, acheté il y a <b>douze jours</b>. Tu as la facture. Échange ou remboursement ?"},
  ];
  const ROLE_SUJETS = ["Ce que tu cherches, et pour quel usage","La taille ou la pointure",
    "Ce qui ne va pas en essayant","La couleur, la matière, la coupe",
    "Demander un avis","L'entretien du vêtement",
    "L'échange et les délais"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Achète un vêtement</span></div>
     <p class="lead">L'assistant joue <b>la personne du magasin</b>. Elle commence par demander pour quel usage et quelle taille. Elle ne parlera ni de l'entretien ni de la politique d'échange avant que tu ne poses la question.</p>
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
         <button class="jr-opt on" type="button" data-role="client" onclick="jrChoisir('role','client')">Le client</button>
         <button class="jr-opt" type="button" data-role="conseiller" onclick="jrChoisir('role','conseiller')">La personne du magasin</button>
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
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()">Commencer la conversation</button>
     </div>
     <div class="jr-rappel">
       <div class="jr-rappel-t">Réutilise ce que tu viens d'apprendre</div>
       <div class="jr-rappel-g">
         <div><div class="jr-rappel-l">Dis ce qui ne va pas, avec un endroit</div><div class="jr-rappel-x">Il est un peu <b>serré</b> <b>aux épaules</b>.</div></div>
         <div><div class="jr-rappel-l">Décris le vêtement</div><div class="jr-rappel-x">Un manteau <b>noir</b>, <b>en</b> duvet, aux genoux.</div></div>
         <div><div class="jr-rappel-l">Demande un avis</div><div class="jr-rappel-x"><b>Qu'est-ce que vous en pensez ?</b></div></div>
         <div><div class="jr-rappel-l">Informe-toi avant de payer</div><div class="jr-rappel-x">Ça <b>s'échange</b> combien de temps ?</div></div>
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
     <h3 class="prod-tit">Décris un vêtement que tu portes souvent</h3>
     <p class="prod-lead">Choisis un vêtement que tu portes souvent. Décris-le à quelqu'un qui ne l'a jamais vu, et dis pourquoi tu l'aimes.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Ce que c'est, sa couleur, sa matière</div><div class="plan-ex">« C'est un manteau noir, en duvet, qui descend aux genoux. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Comment il te va</div><div class="plan-ex">« Il est ample aux épaules, ce qui laisse la place pour un chandail. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Pourquoi tu l'aimes, et comment tu l'entretiens</div><div class="plan-ex">« Je le lave une fois par hiver, à l'eau froide. »</div></div>
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
     <h3 class="prod-tit">Écris au magasin pour un échange</h3>
     <p class="prod-lead">Tu as acheté un vêtement qui ne convient pas et tu ne peux pas te déplacer tout de suite. Écris au magasin, de 5 à 8 phrases.</p>
     <div class="req">
       <div class="req-hd">Ton message doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>L'article et la date d'achat</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce qui ne va pas, avec l'endroit</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>L'état : étiquettes, jamais porté dehors</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce que tu demandes : échange ou remboursement</span></div>
       </div>
       <div class="req-note">Décris l'article avec sa <em>couleur</em> et sa <em>matière</em>, et emploie une forme polie : <em>je voudrais</em>, <em>pourriez-vous</em>.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">service@magasin.qc.ca</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Demande d'échange — achat du…</span></div>
       <textarea id="peText" rows="7" aria-label="Ton message" data-min="5" data-max="8" oninput="peCount()" placeholder="Bonjour,&#10;J'ai acheté chez vous le 12 novembre un manteau noir, en duvet…"></textarea>
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
    "Je peux dire ce que je cherche et donner ma taille ou ma pointure.",
    "Je peux dire ce qui ne va pas en essayant : serré aux épaules, trop court.",
    "Je peux décrire un vêtement : couleur, matière, coupe, longueur.",
    "Je peux demander un avis et comprendre celui qu'on me donne.",
    "Je peux lire les symboles d'une étiquette d'entretien.",
    "Je sais ce qu'il faut pour échanger : la facture, le délai, l'état.",
    "Je connais la différence entre un échange, un remboursement et une mise de côté.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Dans le magasin</div>
     <textarea rows="2" placeholder="Ex. : un manteau, une cabine d'essayage, la taille, la pointure, une marque…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">En essayant</div>
     <textarea rows="2" placeholder="Ex. : serré aux épaules, trop large, les manches sont longues, aux genoux…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Décrire et donner un avis</div>
     <textarea rows="2" placeholder="Ex. : noir, en duvet, une coupe ample, ça te va bien, franchement…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Entretien et échange</div>
     <textarea rows="2" placeholder="Ex. : le mode d'entretien, la sécheuse, un échange, un remboursement, la mise de côté, un dépôt…"></textarea>
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
