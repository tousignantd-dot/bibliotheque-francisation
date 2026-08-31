  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, un courriel corrigé. Le jeu de rôle vient en premier parce
  // qu'il sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait le personnage
  // joué par l'assistant vit dans server.py.
  const ROLE_CAS = [
    {id:'chauffage', titre:'Le chauffage', txt:"Le <b>calorifère du salon</b> ne chauffe plus. Il fait <b>14 °C</b> et le disjoncteur retombe chaque fois qu'on le remonte. On est au début de novembre."},
    {id:'moisissure', titre:'La moisissure', txt:"De la <b>moisissure noire</b> revient dans le coin de la salle de bain malgré les nettoyages. Le miroir reste embué longtemps et il n'y a <b>pas de ventilateur</b>."},
    {id:'bruit', titre:'Le bruit', txt:"Les voisins du dessous reçoivent des amis <b>tous les vendredis</b>. La musique dure jusqu'à <b>deux heures du matin</b>. Ça dure depuis cinq semaines."},
  ];
  const ROLE_SUJETS = ["Quel est le problème exactement","Depuis quand il dure",
    "La conséquence sur ta vie","Ce que tu as déjà essayé",
    "Qui fait faire la réparation","La date de l'intervention","Ce qui se passe en attendant"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Explique ton problème à ta propriétaire</span></div>
     <p class="lead">L'assistant joue <b>l'autre personne</b> au téléphone. Il ne connaît pas ta situation et il ne te donnera rien avant que tu l'expliques bien — comme dans un vrai appel. Ton but : obtenir <b>une date</b> et savoir <b>ce qui se passe en attendant</b>.</p>
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
         <button class="jr-opt on" type="button" data-role="locataire" onclick="jrChoisir('role','locataire')">Le locataire — j'appelle</button>
         <button class="jr-opt" type="button" data-role="proprietaire" onclick="jrChoisir('role','proprietaire')">La propriétaire — je réponds</button>
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
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()">Commencer l'appel</button>
     </div>
     <div class="jr-rappel">
       <div class="jr-rappel-t">Réutilise ce que tu viens d'apprendre</div>
       <div class="jr-rappel-g">
         <div><div class="jr-rappel-l">Dis depuis quand</div><div class="jr-rappel-x">Le calorifère ne chauffe plus <b>depuis</b> avant-hier.</div></div>
         <div><div class="jr-rappel-l">Demande une réparation</div><div class="jr-rappel-x">Pourriez-vous <b>faire venir</b> un électricien cette semaine ?</div></div>
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
     <h3 class="prod-tit">Décris ton problème en trois temps</h3>
     <p class="prod-lead">Choisis un problème de logement — le tien ou un problème inventé — et décris-le comme si tu parlais à ta propriétaire.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Le fait</div><div class="plan-ex">« Il y a une fuite sous l'évier de la cuisine. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Depuis quand, et l'effet sur toi</div><div class="plan-ex">« Ça fait deux semaines. Je ne peux plus utiliser ma cuisine. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Ta demande</div><div class="plan-ex">« Pourriez-vous faire venir un plombier cette semaine ? »</div></div>
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
           <div class="rec-hint">Parle environ 30 secondes. Tu pourras recommencer autant de fois que tu veux.</div>
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
     <h3 class="prod-tit">Le courriel qui laisse une trace</h3>
     <p class="prod-lead">Tu as téléphoné à madame Rioux, mais rien n'a bougé. Écris-lui un courriel de 5 à 8 phrases pour garder une trace de ta demande.</p>
     <div class="req">
       <div class="req-hd">Ton courriel doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le problème</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Depuis quand il dure</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>La conséquence sur ta vie</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une demande claire</span></div>
       </div>
       <div class="req-note">Emploie au moins une fois <em>faire</em> + un verbe à l'infinitif.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">madame.rioux@courriel.ca</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Le problème dans mon logement — suite à notre appel</span></div>
       <textarea id="peText" rows="7" aria-label="Ton courriel" data-min="5" data-max="8" oninput="peCount()" placeholder="Bonjour Madame Rioux,&#10;Je vous écris pour faire suite à notre conversation téléphonique du…"></textarea>
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
    "Je peux nommer un problème dans mon logement (fuite, dégât, bris, moisissure, insalubrité).",
    "Je peux dire depuis quand un problème dure avec depuis, depuis que et ça fait… que.",
    "Je peux dire qui je veux faire venir avec faire + un verbe à l'infinitif.",
    "Je peux mettre deux actions en ordre avec avant de et après avoir.",
    "Je peux me plaindre poliment : dire le fait, l'effet sur moi, puis ma demande.",
    "Je sais à qui m'adresser et quoi faire si rien ne bouge.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Différents problèmes dans un logement ou un immeuble</div>
     <textarea rows="2" placeholder="Ex. : une fuite, un dégât d'eau, une infiltration, un bris, une invasion de fourmis…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Des adjectifs pour décrire un problème</div>
     <textarea rows="2" placeholder="Ex. : défectueux, brisé, bouché, humide, insalubre, dangereux, inacceptable…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Des professionnels à contacter</div>
     <textarea rows="2" placeholder="Ex. : un plombier, une électricienne, un couvreur, une exterminatrice, le concierge…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Pour dire depuis quand et pour se plaindre</div>
     <textarea rows="2" placeholder="Ex. : ça fait deux semaines que… · depuis que… · je ne peux plus tolérer… · pourriez-vous faire venir…"></textarea>
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
