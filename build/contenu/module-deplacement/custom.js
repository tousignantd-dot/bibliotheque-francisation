  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, un itinéraire écrit. Le jeu de rôle vient en premier parce
  // qu'il sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait le personnage
  // joué par l'assistant vit dans server.py.
  const ROLE_CAS = [
    {id:'metro', titre:'Au terminus', txt:"Un <b>terminus d'autobus</b> au-dessus d'une station de métro. Quelqu'un cherche le <b>quai 12</b> et tourne en rond depuis dix minutes. Son autobus part bientôt."},
    {id:'rue', titre:'Au coin de la rue', txt:"Un <b>quartier résidentiel</b>, en après-midi. Quelqu'un vient de descendre de l'autobus et cherche le <b>340 d'une rue</b> qu'il n'a jamais vue."},
    {id:'edifice', titre:'À pied, jusqu\'au bureau', txt:"Depuis l'entrée d'un <b>centre de formation</b>. Il faut se rendre à pied à un bureau situé de l'autre côté d'un <b>parc</b>, à une dizaine de minutes."},
  ];
  const ROLE_SUJETS = ["Le point de départ et l'arrivée","Les étapes, dans l'ordre",
    "Les repères visuels","La direction à prendre",
    "La durée du trajet","Ce qu'il ne faut pas manquer",
    "Répéter pour vérifier"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Demande ton chemin, ou explique-le</span></div>
     <p class="lead">L'assistant joue <b>l'autre personne</b>. Il ne donne pas tout l'itinéraire d'un coup — une ou deux étapes à la fois, comme dans la vraie vie. Ton but : <b>arriver à destination</b> et savoir <b>combien de temps</b> ça prend.</p>
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
         <button class="jr-opt on" type="button" data-role="perdu" onclick="jrChoisir('role','perdu')">La personne qui cherche</button>
         <button class="jr-opt" type="button" data-role="guide" onclick="jrChoisir('role','guide')">La personne qui explique</button>
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
         <div><div class="jr-rappel-l">Donne les étapes à l'impératif</div><div class="jr-rappel-x"><b>Continuez</b> tout droit, puis <b>tournez</b> à gauche.</div></div>
         <div><div class="jr-rappel-l">Dis où on arrête, de quel côté, par où</div><div class="jr-rappel-x"><b>Jusqu'au</b> feu, <b>vers</b> le nord, <b>par</b> le corridor.</div></div>
         <div><div class="jr-rappel-l">Désigne sans répéter</div><div class="jr-rappel-x">Prenez <b>celui</b> qui va vers Saint-Hubert.</div></div>
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
     <h3 class="prod-tit">Explique un trajet que tu connais</h3>
     <p class="prod-lead">Choisis un trajet que tu fais souvent : de chez toi au centre de formation, à l'épicerie, chez le médecin. Explique-le comme à quelqu'un qui ne l'a jamais fait.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Le départ et l'arrivée</div><div class="plan-ex">« Tu pars de l'école et tu vas à la clinique, sur Chambly. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Les étapes, à l'impératif</div><div class="plan-ex">« Sors par la porte principale, tourne à droite, marche jusqu'au feu. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Les repères et la durée</div><div class="plan-ex">« C'est celui qui a une porte vitrée. Compte quinze minutes. »</div></div>
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
     <h3 class="prod-tit">Écris le chemin pour venir chez toi</h3>
     <p class="prod-lead">Quelqu'un vient chez toi pour la première fois, en autobus ou à pied. Écris-lui les indications, de 5 à 8 phrases.</p>
     <div class="req">
       <div class="req-hd">Ton message doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le point de départ</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Les étapes dans l'ordre</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Deux repères visuels</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>La durée du trajet</span></div>
       </div>
       <div class="req-note">Emploie au moins trois verbes à l'<em>impératif</em> et une fois <em>jusqu'à</em>, <em>vers</em> ou <em>par</em>.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">la personne qui vient chez toi</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Comment venir chez moi</span></div>
       <textarea id="peText" rows="7" aria-label="Tes indications" data-min="5" data-max="8" oninput="peCount()" placeholder="Descends à l'arrêt du coin de la rue Chambly.&#10;Ensuite, marche jusqu'au feu et…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 5 à 8</span>
         <button class="btn-prod" id="peBtn" type="button" onclick="peCheck()">Vérifier mes indications</button>
       </div>
     </div>
     <div class="fb" id="peFb" aria-live="polite"></div>
     <div class="status" id="peStatus">Analyse en cours…</div>
     <div class="err" id="peErr"></div>
   </div>`;
  const rb=document.getElementById('recBtn'); if(rb) rb.addEventListener('click',toggleRec);

  // JE RETIENS DES MOTS — notes + cartes mémoire + autoévaluation
  const SELF=[
    "Je peux demander mon chemin à quelqu'un dans la rue.",
    "Je peux comprendre un itinéraire du premier coup et le répéter pour vérifier.",
    "Je peux expliquer un trajet à l'impératif, étape par étape.",
    "Je peux employer jusqu'à, vers et par au bon endroit.",
    "Je peux désigner une chose parmi plusieurs avec celui, celle, ceux.",
    "Je comprends une annonce dans le métro ou l'autobus.",
    "Je peux lire un horaire et un plan de réseau sans me tromper de direction.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Dans la rue</div>
     <textarea rows="2" placeholder="Ex. : un coin de rue, un feu de circulation, un trottoir, traverser, en face de…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Dans le transport</div>
     <textarea rows="2" placeholder="Ex. : un terminus, un quai, une correspondance, la direction, un titre de transport…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Pour donner une direction</div>
     <textarea rows="2" placeholder="Ex. : continuez tout droit, tournez à gauche, jusqu'au feu, par le corridor, au bout de…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Sur un horaire ou un plan</div>
     <textarea rows="2" placeholder="Ex. : un horaire, un plan de réseau, une interruption de service, desservir un arrêt…"></textarea>
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
