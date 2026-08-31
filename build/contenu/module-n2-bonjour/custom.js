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
         <button class="jr-opt on" type="button" data-role="moi" onclick="jrChoisir('role','moi')">Moi, qui salue</button>
         <button class="jr-opt" type="button" data-role="voisine" onclick="jrChoisir('role','voisine')">La voisine qui répond</button>
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
         <div><div class="jr-rappel-l">Salue</div><div class="jr-rappel-x"><b>Bonjour</b>, madame Roy.</div></div>
         <div><div class="jr-rappel-l">Demande, et renvoie la question</div><div class="jr-rappel-x">Ça va ? … Ça va bien, merci. <b>Et vous ?</b></div></div>
         <div><div class="jr-rappel-l">Parle de ta journée</div><div class="jr-rappel-x">Le matin, je <b>déjeune</b>, puis je <b>marche</b> jusqu'au centre.</div></div>
         <div><div class="jr-rappel-l">Prends congé</div><div class="jr-rappel-x"><b>Bonne journée</b> ! À demain !</div></div>
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
