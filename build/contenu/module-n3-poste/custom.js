  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, une courte note écrite. Le jeu de rôle vient en premier
  // parce qu'il sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait la préposée
  // jouée par l'assistant vit dans server.py, scénario `poste`.
  const ROLE_CAS = [
    {id:'colis', titre:'Le colis pour Calgary', txt:"Tu as une boîte sous le bras : un <b>cadeau d'anniversaire</b> pour ton frère, à Calgary. Tu ne sais pas combien ça coûte, combien de temps ça prend, ni ce qu'il faut écrire dessus."},
    {id:'avis', titre:"Le carton dans la boîte aux lettres", txt:"Tu as trouvé un <b>avis de livraison</b> dans ta boîte aux lettres : un colis est arrivé pendant que tu étais au travail. Tu te présentes au comptoir avec le carton à la main."},
    {id:'adresse', titre:'Le déménagement du premier juillet', txt:"Tu déménages le <b>premier juillet</b>, dans le même quartier. Tu viens demander ce qu'il faut faire pour continuer de recevoir ton courrier à la nouvelle adresse."},
  ];
  const ROLE_SUJETS = ["Saluer et dire en une phrase pourquoi tu viens",
    "Poser ta question poliment : je voudrais, j'aimerais, est-ce que je pourrais",
    "Demander le prix, puis le répéter à voix haute pour vérifier",
    "Demander le délai : combien de temps est-ce que ça prend",
    "Dire ce qu'il y a dans ton colis, et si c'est fragile",
    "Annoncer ton choix : je vais le prendre, je vais en prendre trois",
    "Demander ton reçu avant de partir"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Parle à la préposée</span></div>
     <p class="lead">L'assistant joue <b>la préposée du bureau de poste</b>. Elle ne dit rien que tu ne lui demandes pas : le prix, le délai, ce qu'il faut apporter, tout se demande. À toi de poser tes questions avant de choisir.</p>
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
       Ouvre poliment :
       <span class='savoir-ex'><b>Je voudrais</b> envoyer ce colis, s'il vous plaît.</span>
       Demande le prix et le délai :
       <span class='savoir-ex'><b>Combien de temps</b> est-ce que ça prend ?</span>
       Dis ce qu'il y a dedans :
       <span class='savoir-ex'><b>Il y a</b> des vêtements. <b>Rien de</b> fragile.</span>
       Annonce ton choix :
       <span class='savoir-ex'>Je vais <b>le</b> prendre. Je vais <b>en</b> prendre trois.</span>
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
         <button class="jr-opt on" type="button" data-role="client" onclick="jrChoisir('role','client')">Le client</button>
         <button class="jr-opt" type="button" data-role="prepose" onclick="jrChoisir('role','prepose')">La préposée</button>
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
     <h3 class="prod-tit">Demande avant de choisir</h3>
     <p class="prod-lead">Tu es au comptoir du bureau de poste avec ta boîte. Salue, dis en une phrase ce que tu viens faire, demande le prix et le délai, dis ce qu'il y a dans la boîte, puis annonce ton choix et répète le prix à voix haute.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Dire pourquoi tu viens</div><div class="plan-ex">« Bonjour. Je voudrais envoyer ce colis à Calgary, s'il vous plaît. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Demander le prix et le délai</div><div class="plan-ex">« Combien est-ce que ça coûte ? Et combien de temps est-ce que ça prend ? »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Répondre et choisir</div><div class="plan-ex">« Il y a des vêtements et un livre, rien de fragile. Je vais le prendre. »</div></div>
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
     <h3 class="prod-tit">La note glissée dans le colis</h3>
     <p class="prod-lead">Tu mets une courte note dans la boîte, pour la personne qui va la recevoir. Dis-lui ce qu'il y a dedans, quand le colis devrait arriver, et pose-lui une question. De 5 à 8 phrases.</p>
     <div class="req">
       <div class="req-hd">Ta note doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce qu'il y a dans le colis, avec « il y a » ou « c'est »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le service choisi et le temps que ça prend</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une chose à faire attention : fragile, à ne pas plier</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une question posée avec « est-ce que »</span></div>
       </div>
       <div class="req-note">Attention aux petits mots : <em>ce</em> colis, <em>cet</em> avis, <em>cette</em> boîte, <em>ces</em> timbres — et <em>rien de</em> fragile.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">Pour</span><span class="mail-v">La personne qui reçoit le colis</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Ce qu'il y a dans la boîte</span></div>
       <textarea id="peText" rows="7" aria-label="Ta note" data-min="5" data-max="8" oninput="peCount()" placeholder="Bonjour ! J'espère que tout va bien.&#10;Dans la boîte, il y a des vêtements et un livre…"></textarea>
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
    "Je peux nommer ce qu'on trouve dans un bureau de poste : le comptoir, les timbres, les colis.",
    "Je peux dire en une phrase pourquoi je viens, poliment : « Je voudrais… »",
    "Je peux demander le prix et le délai avant de choisir.",
    "Je répète le prix à voix haute pour vérifier que j'ai bien compris.",
    "Je peux demander à quelqu'un de répéter ou de parler moins vite.",
    "Je peux dire ce qu'il y a dans mon colis, et dire si c'est fragile.",
    "Je peux annoncer mon choix : « Je vais le prendre », « Je vais en prendre trois ».",
    "Je sais où écrire l'adresse de l'expéditeur et celle du destinataire.",
    "Je comprends un avis de livraison : quoi apporter et jusqu'à quand.",
    "Je peux demander à faire suivre mon courrier quand je déménage.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#1D6B8F">Je retiens des mots</span><span class="ctit" style="color:#1D6B8F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#1D6B8F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:6px 0 4px">Le bureau de poste</div>
     <textarea rows="2" placeholder="Ex. : le comptoir, un préposé, un timbre, un carnet, affranchir, la boîte rouge…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">Mon envoi</div>
     <textarea rows="2" placeholder="Ex. : un colis, le colis standard, l'Xpresspost, le repérage, un reçu, fragile…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">Demander</div>
     <textarea rows="2" placeholder="Ex. : je voudrais, j'aimerais, est-ce que je pourrais, combien de temps, donnez-moi…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">L'adresse et les services</div>
     <textarea rows="2" placeholder="Ex. : l'expéditeur, le destinataire, le code postal, un avis de livraison, faire suivre…"></textarea>
   </div>
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#1D6B8F">Autoévaluation</span><span class="ctit" style="color:#1D6B8F">Qu'est-ce que je suis capable de faire ?</span></div>
     <p class="lead">Pour chaque énoncé, choisis : pas encore 😟, un peu 🙂, ou oui 😃.</p>
     ${SELF.map((s,i)=>`<div class="selfrow"><div class="self-txt">${s}</div><div class="self-opts">
        <button onclick="rate(${i},this)">😟</button><button onclick="rate(${i},this)">🙂</button><button onclick="rate(${i},this)">😃</button>
     </div></div>`).join('')}
     <div style="margin-top:16px"><button class="btn btn-pri" onclick="finishEval()">Terminer le module 🎉</button></div>
     <div id="evalDone" class="fb" aria-live="polite"></div>
   </div>`;
}
