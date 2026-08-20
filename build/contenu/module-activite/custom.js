  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, un courriel écrit. Le jeu de rôle vient en premier parce
  // qu'il sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait le personnage
  // joué par l'assistant vit dans server.py.
  const ROLE_CAS = [
    {id:'natation', titre:'La natation', txt:"Inscrire un enfant de <b>neuf ans</b> à un cours de natation, pour la session d'automne. Deux groupes sont offerts, et l'enfant ne sait pas nager."},
    {id:'chorale', titre:'La chorale', txt:"Une <b>chorale le jeudi soir</b>, annoncée dans le dépliant de la ville. Il ne reste que quelques places, et on ne sait pas lire la musique."},
    {id:'soccer', titre:'Le soccer', txt:"Inscrire une fille de <b>onze ans</b> au soccer pour l'été. Une pratique le mercredi, un match le samedi — et de l'équipement à acheter."},
  ];
  const ROLE_SUJETS = ["Le jour, l'heure et la durée","Le tarif, résident ou non",
    "Les documents à fournir","Le matériel à apporter",
    "Les conditions d'admission","La façon de s'inscrire",
    "Récapituler avant de partir"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#0F766E">Jeu de rôle</span><span class="ctit" style="color:#0F766E">Informe-toi sur une activité</span></div>
     <p class="lead">L'assistant joue <b>l'autre personne</b>. Au comptoir, on ne vous déroule pas toute la fiche : c'est à vous d'aller chercher chaque renseignement. Ton but : <b>tout savoir avant de partir</b>, pour ne pas avoir à revenir.</p>
     <div class="jr-grid">
       ${ROLE_CAS.map(c=>`
       <div class="jr-log">
         <div class="jr-log-h">${esc(c.titre)}</div>
         <div class="jr-log-a">${c.txt}</div>
       </div>`).join('')}
     </div>
     <div class="jr-sub">Les sept sujets à couvrir</div>
     <div class="jr-sujets">
       ${ROLE_SUJETS.map(s=>`<div class="jr-sujet"><span class="jr-box"></span>${esc(s)}</div>`).join('')}
     </div>
     <div class="jr-gram">
       <div class="jr-gram-t">Réutilise ce que tu viens d'apprendre</div>
       Demande les conditions :
       <span class='savoir-ex'>Est-ce qu'<b>il faut</b> une preuve de résidence ?</span>
       <span class='savoir-ex'><b>Il est important d'</b>arriver d'avance ?</span>
       Compare avant de choisir :
       <span class='savoir-ex'>C'est <b>la moins chère</b> des deux ?</span>
       Fais répéter un montant :
       <span class='savoir-ex'>Quatre-vingt-cinq, <b>c'est bien ça</b> ?</span>
     </div>

     <div class="jr-sep"></div>
     <div class="jr-sub">Choisis ta situation et ton rôle</div>
     <div class="jr-choix">
       <div class="jr-choix-l">Quelle activité ?</div>
       <div class="jr-opts" id="jrLogs">
         ${ROLE_CAS.map((c,i)=>`<button class="jr-opt${i===0?' on':''}" type="button" data-log="${c.id}" onclick="jrChoisir('log','${c.id}')">${esc(c.titre)}</button>`).join('')}
       </div>
       <div class="jr-choix-l">Tu joues qui ?</div>
       <div class="jr-opts" id="jrRoles">
         <button class="jr-opt on" type="button" data-role="parent" onclick="jrChoisir('role','parent')">La personne qui s'informe</button>
         <button class="jr-opt" type="button" data-role="prepose" onclick="jrChoisir('role','prepose')">La personne au comptoir</button>
       </div>
       <div class="jr-choix-l">Comment ?</div>
       <div class="jr-opts" id="jrModes">
         <button class="jr-opt on" type="button" data-mode="texte" onclick="jrModeVoix(false)">✍️ Écrire</button>
         <button class="jr-opt" type="button" data-mode="voix" onclick="jrModeVoix(true)">🎤 Parler</button>
       </div>
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()" style="margin-top:14px">Commencer la conversation</button>
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
         <button class="btn btn-send" type="button" onclick="jrFini()">J'ai fini — corrige mes phrases</button>
       </div>
       <div class="fb" id="jrFb" aria-live="polite"></div>
     </div>
   </div>

   <div class="card custom">
     <div class="prod-eyebrow"><span class="prod-num">1</span><span class="prod-kind">Production orale</span></div>
     <h3 class="prod-tit">Explique une activité que tu connais</h3>
     <p class="prod-lead">Choisis une activité que tu sais faire : un sport, un jeu, une danse, une recette. Explique-la à quelqu'un qui la découvre, en donnant de vraies consignes.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Ce qu'il faut avoir</div><div class="plan-ex">« Il faut un ballon et deux équipes de cinq. Il est important d'avoir de bons souliers. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Les consignes, à l'impératif</div><div class="plan-ex">« Prends le ballon à deux mains. Ne le lâche pas. Regarde-moi. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Ce qu'il ne faut pas faire</div><div class="plan-ex">« Ne cours pas sur le bord. Sortez par l'échelle, pas par le bord. »</div></div>
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
     <h3 class="prod-tit">Écris à ta ville pour t'informer</h3>
     <p class="prod-lead">Une activité du dépliant t'intéresse, mais il te manque des renseignements. Écris au service des loisirs de ta ville, de 5 à 8 phrases.</p>
     <div class="req">
       <div class="req-hd">Ton message doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>L'activité qui t'intéresse</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Pour qui : toi, ton enfant, son âge</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Trois questions précises</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une formule pour terminer</span></div>
       </div>
       <div class="req-note">Emploie au moins une fois <em>il faut</em> ou <em>il est important de</em>, et une comparaison avec <em>le plus</em> ou <em>le moins</em>.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">loisirs@ville.qc.ca</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Renseignements sur une activité du dépliant</span></div>
       <textarea id="peText" rows="7" aria-label="Ton message" data-min="5" data-max="8" oninput="peCount()" placeholder="Bonjour,&#10;J'ai vu dans votre dépliant l'activité… et j'aimerais savoir…"></textarea>
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
    "Je peux m'informer sur une activité : horaire, tarif, matériel, documents.",
    "Je comprends un montant et une heure du premier coup, et je les fais répéter au besoin.",
    "Je reconnais une condition quand j'entends « il faut » ou « il est important de ».",
    "Je peux comparer deux activités et dire laquelle est la moins chère.",
    "Je comprends les consignes d'un moniteur, même dites vite.",
    "Je peux donner une consigne à l'impératif, avec un pronom : prends-la, ne la lâche pas.",
    "Je peux lire un dépliant de ma ville et trouver ce que je cherche.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#166534">Je retiens des mots</span><span class="ctit" style="color:#166534">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#166534" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#166534;font-size:13px;margin:6px 0 4px">S'inscrire</div>
     <textarea rows="2" placeholder="Ex. : une inscription, un dépliant, le tarif, une preuve de résidence, une session…"></textarea>
     <div style="font-weight:800;color:#166534;font-size:13px;margin:12px 0 4px">À la piscine et au gymnase</div>
     <textarea rows="2" placeholder="Ex. : un moniteur, un maillot, un bonnet de bain, un vestiaire, une planche, l'échelle…"></textarea>
     <div style="font-weight:800;color:#166534;font-size:13px;margin:12px 0 4px">Les consignes</div>
     <textarea rows="2" placeholder="Ex. : prenez-la à deux mains, ne la lâchez pas, mets-toi là, sortez par l'échelle…"></textarea>
     <div style="font-weight:800;color:#166534;font-size:13px;margin:12px 0 4px">Lire le dépliant</div>
     <textarea rows="2" placeholder="Ex. : la légende, les places disponibles, le tarif résident, la moins chère, chaque cours…"></textarea>
   </div>
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#166534">Autoévaluation</span><span class="ctit" style="color:#166534">Qu'est-ce que je suis capable de faire ?</span></div>
     <p class="lead">Pour chaque énoncé, choisis : pas encore 😟, un peu 🙂, ou oui 😃.</p>
     ${SELF.map((s,i)=>`<div class="selfrow"><div class="self-txt">${s}</div><div class="self-opts">
        <button onclick="rate(${i},this)">😟</button><button onclick="rate(${i},this)">🙂</button><button onclick="rate(${i},this)">😃</button>
     </div></div>`).join('')}
     <div style="margin-top:16px"><button class="btn btn-pri" onclick="finishEval()">Terminer le module 🎉</button></div>
     <div id="evalDone" class="fb" aria-live="polite"></div>
   </div>`;
}
