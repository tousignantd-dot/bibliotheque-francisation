  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, une courte note écrite. Le jeu de rôle vient en premier
  // parce qu'il sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait le personnage
  // joué par l'assistant vit dans server.py.
  const ROLE_CAS = [
    {id:'toux', titre:'La toux qui dure', txt:"Tu <b>tousses depuis quatre jours</b> et tu ne dors plus la nuit. Tu n'as pas de médecin de famille. Tu viens demander un conseil au pharmacien."},
    {id:'renouvellement', titre:"L'ordonnance finie", txt:"Il te reste <b>deux comprimés</b> et ton ordonnance est finie. Ton rendez-vous chez le médecin est seulement dans six semaines. Tu as ta carte d'assurance maladie."},
    {id:'posologie', titre:"L'étiquette à comprendre", txt:"Ton médicament est prêt. Sur l'étiquette : « <b>1 comprimé 3 fois par jour, avec de la nourriture, pendant 7 jours</b> ». Tu veux être certain de comprendre avant de partir."},
  ];
  const ROLE_SUJETS = ["Saluer et dire pourquoi tu viens","Dire ce qui ne va pas en une phrase",
    "Dire depuis quand ça dure","Répondre aux questions du pharmacien : la fièvre, tes autres médicaments",
    "Sortir ta carte d'assurance maladie","Demander combien de fois par jour et pendant combien de jours",
    "Répéter la posologie à voix haute avant de partir"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Parle au pharmacien</span></div>
     <p class="lead">L'assistant joue <b>le pharmacien</b>. Il ne dit rien que tu ne lui demandes pas : le prix, le temps d'attente, ce qu'il peut faire pour toi, tout se demande. À toi de poser tes questions.</p>
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
         <button class="jr-opt" type="button" data-role="pharmacien" onclick="jrChoisir('role','pharmacien')">Le pharmacien</button>
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
         <div><div class="jr-rappel-l">Dis où tu as mal</div><div class="jr-rappel-x">J'ai mal <b>à la</b> gorge le matin.</div></div>
         <div><div class="jr-rappel-l">Dis depuis quand</div><div class="jr-rappel-x">Je tousse <b>depuis</b> quatre jours.</div></div>
         <div><div class="jr-rappel-l">Demande poliment</div><div class="jr-rappel-x"><b>Est-ce que je peux</b> faire renouveler mon ordonnance ?</div></div>
         <div><div class="jr-rappel-l">Vérifie la posologie</div><div class="jr-rappel-x">Un comprimé, <b>trois fois par jour</b>, <b>pendant</b> sept jours ?</div></div>
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
     <h3 class="prod-tit">Explique ce qui ne va pas</h3>
     <p class="prod-lead">Tu es au comptoir des ordonnances. Salue, dis ce que tu as, dis depuis quand ça dure, réponds aux questions du pharmacien, puis demande combien de fois par jour prendre le médicament.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Dire ce qui ne va pas</div><div class="plan-ex">« Bonjour. Je tousse beaucoup et j'ai mal à la gorge. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Dire depuis quand</div><div class="plan-ex">« Ça dure depuis quatre jours. J'ai eu de la fièvre hier soir. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Demander la posologie</div><div class="plan-ex">« Combien de fois par jour ? Est-ce que je peux le prendre avec mon autre comprimé ? »</div></div>
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
     <h3 class="prod-tit">Écris la note pour ta voisine</h3>
     <p class="prod-lead">Tu ne peux pas sortir aujourd'hui et ta voisine ira chercher tes médicaments à la pharmacie. Écris-lui une note : ce qu'il faut demander, ce qu'elle doit apporter, et ce que tu veux savoir. De 5 à 8 phrases.</p>
     <div class="req">
       <div class="req-hd">Ta note doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce qu'il faut demander : un renouvellement, ou un conseil</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce qu'il faut apporter : la carte d'assurance maladie, le flacon vide</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une question à poser au pharmacien, avec « est-ce que »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>La posologie de ton autre médicament : combien de fois par jour</span></div>
       </div>
       <div class="req-note">Attention aux petits mots : <em>mon</em> ordonnance, <em>ma</em> carte, <em>mes</em> comprimés, trois fois <em>par</em> jour, <em>pendant</em> sept jours.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">Pour</span><span class="mail-v">Ma voisine</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Ce qu'il faut demander à la pharmacie</span></div>
       <textarea id="peText" rows="7" aria-label="Ta note" data-min="5" data-max="8" oninput="peCount()" placeholder="Bonjour. Merci beaucoup d'aller à la pharmacie pour moi.&#10;Mon ordonnance est finie : il faut demander un renouvellement…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 5 à 8</span>
         <button class="btn-prod" id="peBtn" type="button" onclick="peCheck()">Vérifier ma note</button>
       </div>
     </div>
     <div class="fb" id="peFb" aria-live="polite"></div>
     <div class="status" id="peStatus">Analyse en cours…</div>
     <div class="err" id="peErr"></div>
   </div>`;
  const rb=document.getElementById('recBtn'); if(rb) rb.addEventListener('click',toggleRec);

  // JE RETIENS DES MOTS — notes + cartes mémoire + autoévaluation
  const SELF=[
    "Je peux nommer les endroits d'une pharmacie : le comptoir des ordonnances, l'allée, la caisse.",
    "Je sais ce qu'il faut apporter : ma carte d'assurance maladie.",
    "Je peux dire où j'ai mal : j'ai mal à la tête, au dos, aux dents.",
    "Je peux nommer mon malaise : je tousse, j'ai de la fièvre, je me suis coupé.",
    "Je peux dire depuis quand ça dure, avec « depuis » ou « ça fait… que ».",
    "Je peux demander un renouvellement d'ordonnance poliment.",
    "Je comprends les questions du pharmacien et je réponds du premier coup.",
    "Je peux lire une posologie : combien, combien de fois, quand, pendant combien de jours.",
    "Je comprends les mises en garde : pas plus de, de moins de, au moins.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">La pharmacie</div>
     <textarea rows="2" placeholder="Ex. : le comptoir des ordonnances, l'allée, la caisse, le pharmacien, la carte d'assurance maladie…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Mon corps et mes malaises</div>
     <textarea rows="2" placeholder="Ex. : j'ai mal à la gorge, je tousse, j'ai de la fièvre, un rhume, je me suis coupé…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Demander</div>
     <textarea rows="2" placeholder="Ex. : est-ce que je peux…, faire renouveler, mon ordonnance, mon dossier, combien de temps…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">L'étiquette</div>
     <textarea rows="2" placeholder="Ex. : la posologie, un comprimé, trois fois par jour, avec de la nourriture, pendant sept jours, un effet secondaire…"></textarea>
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
