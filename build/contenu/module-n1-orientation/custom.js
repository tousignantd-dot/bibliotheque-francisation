  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, une petite liste écrite. Le jeu de rôle vient en premier
  // parce qu'il sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait le personnage
  // joué par l'assistant vit dans server.py.
  const ROLE_CAS = [
    {id:'toilettes', titre:"Devant deux portes", txt:"Tu cherches <b>les toilettes</b>. Il y a deux portes et deux dessins. Tu demandes si c'est ici."},
    {id:'garde', titre:"Le service de garde", txt:"Tu arrives avec ton enfant. Tu cherches le <b>service de garde</b> et tu lis les panneaux."},
    {id:'porte', titre:"La porte ne s'ouvre pas", txt:"Un mot est écrit sur la porte : <b>POUSSEZ</b> ou <b>TIREZ</b>. Tu ne sais pas lequel. Tu demandes."},
  ];
  const ROLE_SUJETS = ["Dire bonjour","Dire ce que tu cherches",
    "Dire ce que montre le dessin","Lire le mot du panneau à voix haute",
    "Demander « c'est ici ? »","Dire « ce n'est pas ici » quand ce n'est pas ça",
    "Dire merci"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Trouve la bonne porte</span></div>
     <p class="lead">L'assistant joue <b>quelqu'un du centre</b>. Il parle lentement et pose une question à la fois. Si tu ne comprends pas, dis-le : c'est permis.</p>
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
       Nomme l'endroit :
       <span class='savoir-ex'><b>C'est</b> la cafétéria.</span>
       Dis que non :
       <span class='savoir-ex'><b>Ce n'est pas</b> ici.</span>
       Demande :
       <span class='savoir-ex'>Les toilettes, <b>c'est ici</b> ?</span>
       Lis le panneau :
       <span class='savoir-ex'>C'est écrit <b>POUSSEZ</b>.</span>
     </div>

     <div class="jr-sep"></div>
     <div class="jr-sub">Choisis ta situation et ton rôle</div>
     <div class="jr-choix">
       <div class="jr-choix-l">Quelle situation ?</div>
       <div class="jr-opts" id="jrLogs">
         ${ROLE_CAS.map((c,i)=>`<button class="jr-opt${i===0?' on':''}" type="button" data-log="${c.id}" onclick="jrChoisir('log','${c.id}')">${esc(c.titre)}</button>`).join('')}
       </div>
       <div class="jr-choix-l">Tu joues qui ?</div>
       <div class="jr-opts" id="jrRoles">
         <button class="jr-opt on" type="button" data-role="eleve" onclick="jrChoisir('role','eleve')">Moi, l'élève</button>
         <button class="jr-opt" type="button" data-role="employe" onclick="jrChoisir('role','employe')">La personne du centre</button>
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
     <h3 class="prod-tit">Cinq panneaux de mon centre</h3>
     <p class="prod-lead">Fais le tour de ton centre. Regarde cinq panneaux. Pour chacun, dis ce que montre le dessin, lis le mot, et dis ce qu'on fait à cet endroit.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Dire ce que montre le dessin</div><div class="plan-ex">« Il y a un homme et une femme. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Lire le mot écrit à côté</div><div class="plan-ex">« C'est écrit TOILETTES. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Dire ce qu'on fait là</div><div class="plan-ex">« C'est les toilettes. On se lave les mains. »</div></div>
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
     <h3 class="prod-tit">Ma liste de panneaux</h3>
     <p class="prod-lead">Écris la liste des panneaux de ton centre. Une ligne par panneau : le mot du panneau, puis ce qu'on y fait. De 4 à 6 lignes.</p>
     <div class="req">
       <div class="req-hd">Ta liste doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le mot écrit sur le panneau, en MAJUSCULES</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le même mot en minuscules, avec le, la ou les</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce qu'on fait à cet endroit</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Au moins un panneau qui interdit quelque chose</span></div>
       </div>
       <div class="req-note">Écris comme ceci : <em>CAFÉTÉRIA — la cafétéria — on mange à midi.</em></div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">Liste</span><span class="mail-v">Les panneaux de mon centre</span></div>
       <div class="mail-row"><span class="mail-k">Centre</span><span class="mail-v">Francisation, niveau 1</span></div>
       <textarea id="peText" rows="7" aria-label="Ta liste" data-min="4" data-max="6" oninput="peCount()" placeholder="SORTIE — la sortie — on part par ici.&#10;TOILETTES — les toilettes — …"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 ligne sur 4 à 6</span>
         <button class="btn-prod" id="peBtn" type="button" onclick="peCheck()">Vérifier ma liste</button>
       </div>
     </div>
     <div class="fb" id="peFb" aria-live="polite"></div>
     <div class="status" id="peStatus">Analyse en cours…</div>
     <div class="err" id="peErr"></div>
   </div>`;
  const rb=document.getElementById('recBtn'); if(rb) rb.addEventListener('click',toggleRec);

  // JE RETIENS DES MOTS — notes + cartes mémoire + autoévaluation
  const SELF=[
    "Je peux dire ce que montre un dessin de panneau.",
    "Je peux lire les mots TOILETTES, CAFÉTÉRIA, SORTIE, ENTRÉE.",
    "Je peux reconnaître le même mot en grandes et en petites lettres.",
    "Je peux dire « c'est la cafétéria » avec le bon petit mot.",
    "Je peux comprendre POUSSEZ et TIREZ sur une porte.",
    "Je peux dire si un panneau permet ou interdit quelque chose.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Le panneau</div>
     <textarea rows="2" placeholder="Ex. : un panneau, un dessin, une flèche, un mot…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les lieux du centre</div>
     <textarea rows="2" placeholder="Ex. : les toilettes, la cafétéria, le vestiaire, l'accueil…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les panneaux qui disent quoi faire</div>
     <textarea rows="2" placeholder="Ex. : poussez, tirez, entrez, sonnez…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Ce qui est interdit</div>
     <textarea rows="2" placeholder="Ex. : défense de fumer, ne pas entrer, silence…"></textarea>
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
