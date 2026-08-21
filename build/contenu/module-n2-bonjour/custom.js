  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, une carte de vœux écrite. Le jeu de rôle vient en premier
  // parce qu'il sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait la voisine
  // jouée par l'assistant vit dans server.py, scénario « bonjour ».
  const ROLE_CAS = [
    {id:'entree', titre:"Dans l'entrée, le matin", txt:"Tu pars au centre. Ta <b>voisine</b> descend en même temps que toi. Vous avez trente secondes ensemble."},
    {id:'ascenseur', titre:"Devant l'ascenseur", txt:"Ta voisine a les <b>mains pleines</b> de sacs. Elle te demande quelque chose."},
    {id:'fete', titre:"Le jour de sa fête", txt:"C'est la <b>fête</b> de ta voisine. Tu frappes à sa porte avec une carte."},
  ];
  const ROLE_SUJETS = ["Dire bonjour","Demander « ça va ? »",
    "Répondre, puis redemander « et vous ? »",
    "Dire une chose qu'on fait dans sa journée",
    "Comprendre une demande d'aide, et répondre",
    "Remercier ou souhaiter",
    "Prendre congé : bonne journée, à demain"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Salue ta voisine</span></div>
     <p class="lead">L'assistant joue <b>madame Roy, ta voisine</b>. Elle parle lentement et dit deux ou trois phrases à la fois, pas plus. Si tu ne comprends pas, dis-le : « pouvez-vous répéter ? » fait partie de la conversation.</p>
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
       Salue :
       <span class='savoir-ex'><b>Bonjour</b>, madame Roy.</span>
       Demande, et renvoie la question :
       <span class='savoir-ex'>Ça va ? … Ça va bien, merci. <b>Et vous ?</b></span>
       Parle de ta journée :
       <span class='savoir-ex'>Le matin, je <b>déjeune</b>, puis je <b>marche</b> jusqu'au centre.</span>
       Prends congé :
       <span class='savoir-ex'><b>Bonne journée</b> ! À demain !</span>
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
         <button class="jr-opt on" type="button" data-role="moi" onclick="jrChoisir('role','moi')">Moi, qui salue</button>
         <button class="jr-opt" type="button" data-role="voisine" onclick="jrChoisir('role','voisine')">La voisine qui répond</button>
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
     <h3 class="prod-tit">Salue ton voisin et parle de ta journée</h3>
     <p class="prod-lead">Tu croises ton voisin le matin. Salue-le, demande comment ça va, dis deux ou trois choses que tu fais dans ta journée, puis prends congé. Vouvoie-le du début à la fin.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Saluer et demander</div><div class="plan-ex">« Bonjour, madame. Ça va ? »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Répondre et parler de sa journée</div><div class="plan-ex">« Ça va bien, merci. Et vous ? … Le matin, je déjeune, puis je marche jusqu'au centre. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Prendre congé</div><div class="plan-ex">« Bonne journée ! À demain ! »</div></div>
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
     <h3 class="prod-tit">Écris une carte de vœux</h3>
     <p class="prod-lead">Écris une carte à un voisin, à une voisine ou à un camarade de classe : un souhait, un merci, et ton prénom à la fin. De 3 à 5 phrases.</p>
     <div class="req">
       <div class="req-hd">Ta carte doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un souhait : bonne fête, bonne santé, bon voyage…</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un merci, avec le mot <em>pour</em></span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le nom de la personne à qui tu écris</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ton prénom, sur la dernière ligne</span></div>
       </div>
       <div class="req-note">Attention à <em>bon</em> et <em>bonne</em> : <em>bonne</em> fête, <em>bonne</em> santé, mais <em>bon</em> anniversaire, <em>bon</em> voyage.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">Carte</span><span class="mail-v">Ma carte de vœux</span></div>
       <div class="mail-row"><span class="mail-k">Centre</span><span class="mail-v">Francisation, niveau 2</span></div>
       <textarea id="peText" rows="7" aria-label="Ta carte" data-min="3" data-max="5" oninput="peCount()" placeholder="Bonne fête, madame Roy !&#10;Merci pour…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 3 à 5</span>
         <button class="btn-prod" id="peBtn" type="button" onclick="peCheck()">Vérifier ma carte</button>
       </div>
     </div>
     <div class="fb" id="peFb" aria-live="polite"></div>
     <div class="status" id="peStatus">Analyse en cours…</div>
     <div class="err" id="peErr"></div>
   </div>`;
  const rb=document.getElementById('recBtn'); if(rb) rb.addEventListener('click',toggleRec);

  // JE RETIENS DES MOTS — notes + cartes mémoire + autoévaluation
  const SELF=[
    "Je peux dire bonjour et bonsoir au bon moment.",
    "Je peux répondre à « ça va ? » et redemander « et vous ? ».",
    "Je peux dire « tu » ou « vous » à la bonne personne.",
    "Je peux dire trois choses que je fais dans ma journée.",
    "Je peux comprendre quelqu'un qui me demande de l'aide.",
    "Je peux demander de l'aide et remercier.",
    "Je peux écrire une courte carte de vœux.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Les salutations</div>
     <textarea rows="2" placeholder="Ex. : bonjour, bonsoir, salut, bonne journée, à demain…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Ma journée</div>
     <textarea rows="2" placeholder="Ex. : le matin, l'après-midi, le soir, déjeuner, travailler, à pied…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Demander de l'aide</div>
     <textarea rows="2" placeholder="Ex. : excusez-moi, pouvez-vous m'aider ? j'ai besoin d'aide…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Remercier et souhaiter</div>
     <textarea rows="2" placeholder="Ex. : merci pour…, ce n'est rien, bonne fête, bonne santé…"></textarea>
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
