  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, un trajet écrit. Le jeu de rôle vient en premier parce qu'il
  // sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait le personnage
  // joué par l'assistant vit dans server.py, scénario « autobus ».
  const ROLE_CAS = [
    {id:'chemin', titre:"Dans la rue", txt:"Tu cherches la <b>bibliothèque</b>. Tu arrêtes quelqu'un sur le trottoir."},
    {id:'arret', titre:"À l'arrêt", txt:"Tu attends le <b>51</b>. Tu ne sais pas si c'est le bon arrêt, ni à quelle heure il passe."},
    {id:'correspondance', titre:"Dans l'autobus", txt:"Tu vas à l'<b>hôpital</b>. Tu n'es pas sûr d'avoir pris le bon autobus."},
  ];
  const ROLE_SUJETS = ["Dire où on veut aller","Demander le chemin",
    "Comprendre une direction","Demander l'heure du prochain autobus",
    "Faire répéter plus lentement","Répéter pour vérifier",
    "Dire merci"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Demande ton chemin</span></div>
     <p class="lead">L'assistant joue <b>la personne à qui tu demandes</b>. Elle parle lentement et donne une information à la fois. Si tu ne comprends pas, dis-le : c'est permis, et c'est même ce qu'il faut faire.</p>
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
       Dis où tu vas :
       <span class='savoir-ex'>Je vais <b>à la</b> bibliothèque.</span>
       Demande :
       <span class='savoir-ex'>Excusez-moi, <b>c'est loin</b> d'ici ?</span>
       Fais ralentir :
       <span class='savoir-ex'><b>Plus lentement</b>, s'il vous plaît.</span>
       Vérifie :
       <span class='savoir-ex'>Tout droit, à droite au feu. <b>C'est ça ?</b></span>
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
         <button class="jr-opt on" type="button" data-role="passager" onclick="jrChoisir('role','passager')">Moi, qui demande</button>
         <button class="jr-opt" type="button" data-role="habitant" onclick="jrChoisir('role','habitant')">La personne qui répond</button>
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
     <h3 class="prod-tit">Demande ton chemin</h3>
     <p class="prod-lead">Tu cherches un lieu de ton quartier. Arrête quelqu'un, demande le chemin, et répète ce qu'on te répond pour vérifier.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Aborder et dire où on va</div><div class="plan-ex">« Excusez-moi, madame. Je cherche la bibliothèque. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Demander la distance et faire ralentir</div><div class="plan-ex">« C'est loin d'ici ? Plus lentement, s'il vous plaît. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Répéter le chemin et remercier</div><div class="plan-ex">« Tout droit, à droite au feu. C'est ça ? Merci beaucoup. »</div></div>
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
     <h3 class="prod-tit">Écris ton trajet</h3>
     <p class="prod-lead">Écris le trajet que tu fais chaque semaine : d'où tu pars, où tu vas, quel autobus tu prends, combien de temps ça prend. De 4 à 6 phrases.</p>
     <div class="req">
       <div class="req-hd">Ton trajet doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le lieu où tu vas</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le numéro de l'autobus, ou « à pied »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Où se trouve l'arrêt</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>L'heure, ou le temps que ça prend</span></div>
       </div>
       <div class="req-note">Emploie <em>je vais à la / au / à l'</em>, et les mots du chemin : <em>tout droit</em>, <em>à droite</em>, <em>au coin</em>.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">Fiche</span><span class="mail-v">Mon trajet de la semaine</span></div>
       <div class="mail-row"><span class="mail-k">Centre</span><span class="mail-v">Francisation, niveau 2</span></div>
       <textarea id="peText" rows="7" aria-label="Ton trajet" data-min="4" data-max="6" oninput="peCount()" placeholder="Le lundi, je vais à l'école.&#10;Je prends le…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 4 à 6</span>
         <button class="btn-prod" id="peBtn" type="button" onclick="peCheck()">Vérifier mon trajet</button>
       </div>
     </div>
     <div class="fb" id="peFb" aria-live="polite"></div>
     <div class="status" id="peStatus">Analyse en cours…</div>
     <div class="err" id="peErr"></div>
   </div>`;
  const rb=document.getElementById('recBtn'); if(rb) rb.addEventListener('click',toggleRec);

  // JE RETIENS DES MOTS — notes + cartes mémoire + autoévaluation
  const SELF=[
    "Je peux dire où je veux aller.",
    "Je peux demander mon chemin à quelqu'un.",
    "Je peux comprendre une direction simple.",
    "Je peux demander à quelle heure passe l'autobus.",
    "Je peux comprendre l'heure qu'on me dit.",
    "Je peux répéter ce que j'ai compris pour vérifier.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Les lieux du quartier</div>
     <textarea rows="2" placeholder="Ex. : la bibliothèque, le parc, la pharmacie, le CLSC…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Le chemin</div>
     <textarea rows="2" placeholder="Ex. : tout droit, à droite, au coin, jusqu'au feu…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">L'autobus</div>
     <textarea rows="2" placeholder="Ex. : un arrêt, un horaire, une correspondance, le prochain…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Demander de l'aide</div>
     <textarea rows="2" placeholder="Ex. : excusez-moi, plus lentement, vous pouvez répéter, c'est ça ?…"></textarea>
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
