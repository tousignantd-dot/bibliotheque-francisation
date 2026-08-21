  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un appel joué avec l'assistant, une présentation à
  // voix haute à une nouvelle voisine, un courriel au propriétaire. Le jeu de
  // rôle vient en premier parce qu'il sert de répétition avant les deux
  // autres.
  // Le scénario `demenagement` a été ajouté à server.py pour ce module : seule
  // la situation de départ est côté client. Les tarifs, les suppléments et les
  // conditions vivent sur le serveur — sinon l'élève lirait dans la page les
  // renseignements qu'il est justement censé aller chercher.
  const ROLE_CAS = [
    {id:'troisdemie', titre:"Le 3 ½ du deuxième", txt:"Vous videz un <b>3 ½ au deuxième étage</b>, sans ascenseur, escalier extérieur qui tourne. Une quinzaine de boîtes, un divan, un lit, une table et quatre chaises. <b>Le 1<sup>er</sup> juillet.</b>"},
    {id:'gros', titre:"Le 4 ½ avec un piano", txt:"Vous videz un <b>4 ½</b> qui contient un <b>piano droit</b> et un congélateur encore plein. Rez-de-chaussée des deux côtés, mais une porte d'entrée étroite. <b>Le 1<sup>er</sup> juillet.</b>"},
    {id:'camion', titre:"Le camion sans chauffeur", txt:"Vous voulez <b>louer un camion</b> et le conduire vous-même : trois amis viennent vous aider. Vous ne savez pas quelle grandeur prendre ni ce qui est compris dans le prix. <b>Le 1<sup>er</sup> juillet.</b>"},
  ];
  const ROLE_SUJETS = ["La date, l'heure et les deux adresses","La grandeur du logement, l'étage et l'escalier",
    "Ce qu'il y a de gros ou de fragile","Le tarif, et ce qui s'ajoute au tarif",
    "L'assurance","Le dépôt à verser pour réserver","La répétition de la date et de l'heure"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">L'appel à la compagnie de déménagement</span></div>
     <p class="lead">Vous avez la situation sous les yeux ; l'autre personne a les tarifs. L'assistant ne donne jamais un prix avant qu'on le lui demande. Essayez les deux rôles : au niveau 5, il faut savoir <b>aller chercher</b> un renseignement et savoir l'<b>expliquer</b>.</p>
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
       <div class="jr-gram-t">Réutilisez ce que vous venez d'apprendre</div>
       Allez chercher ce qu'on ne vous dit pas :
       <span class='savoir-ex'>Est-ce qu'il y a <b>autre chose qui s'ajoute</b> au tarif ?</span>
       Employez un pronom plutôt que de répéter :
       <span class='savoir-ex'>Le camion ? Je <b>le</b> réserve aujourd'hui. Des boîtes, j'<b>en</b> ai quinze.</span>
       Donnez la date avec la bonne préposition :
       <span class='savoir-ex'>Le logement est libre <b>à partir du</b> premier juillet.</span>
       Dites une durée :
       <span class='savoir-ex'>Ils ont tout monté <b>en</b> quatre heures, la dernière fois.</span>
       Vérifiez avant de raccrocher :
       <span class='savoir-ex'>Donc le premier juillet, huit heures, cent dollars de dépôt. <b>C'est bien ça ?</b></span>
     </div>

     <div class="jr-sep"></div>
     <div class="jr-sub">Choisissez votre situation et votre rôle</div>
     <div class="jr-choix">
       <div class="jr-choix-l">Quel déménagement ?</div>
       <div class="jr-opts" id="jrLogs">
         ${ROLE_CAS.map((c,i)=>`<button class="jr-opt${i===0?' on':''}" type="button" data-log="${c.id}" onclick="jrChoisir('log','${c.id}')">${esc(c.titre)}</button>`).join('')}
       </div>
       <div class="jr-choix-l">Vous jouez qui ?</div>
       <div class="jr-opts" id="jrRoles">
         <button class="jr-opt on" type="button" data-role="client" onclick="jrChoisir('role','client')">La personne qui déménage</button>
         <button class="jr-opt" type="button" data-role="repartitrice" onclick="jrChoisir('role','repartitrice')">La répartitrice de la compagnie</button>
       </div>
       <div class="jr-choix-l">Comment ?</div>
       <div class="jr-opts" id="jrModes">
         <button class="jr-opt on" type="button" data-mode="texte" onclick="jrModeVoix(false)">✍️ Écrire</button>
         <button class="jr-opt" type="button" data-mode="voix" onclick="jrModeVoix(true)">🎤 Parler</button>
       </div>
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()" style="margin-top:14px">Commencer l'appel</button>
     </div>

     <div id="jrChat" class="hidden">
       <div class="jr-fil" id="jrFil" aria-live="polite"></div>
       <div class="jr-mic hidden" id="jrMicZone">
         <button id="jrMic" type="button" onclick="jrParler()" aria-label="Parler">🎤</button>
         <span class="jr-mic-l" id="jrMicLbl">Touchez pour parler</span>
       </div>
       <div class="jr-saisie">
         <input id="jrInput" type="text" placeholder="Écrivez ce que vous dites…" autocomplete="off"
                onkeydown="if(event.key==='Enter'){event.preventDefault();jrEnvoyer();}">
         <button class="btn btn-pri" id="jrSend" type="button" onclick="jrEnvoyer()">Envoyer</button>
       </div>
       <div class="status" id="jrStatus">L'assistant réfléchit…</div>
       <div class="err" id="jrErr"></div>
       <div class="jr-fin">
         <button class="btn btn-ghost" type="button" onclick="jrRecommencer()">↺ Recommencer</button>
         <button class="btn btn-send" type="button" onclick="jrFini()">J'ai fini — corrigez mes phrases</button>
       </div>
       <div class="fb" id="jrFb" aria-live="polite"></div>
     </div>
   </div>

   <div class="card custom">
     <div class="prod-eyebrow"><span class="prod-num">1</span><span class="prod-kind">Production orale</span></div>
     <h3 class="prod-tit">Le lendemain, dans l'escalier</h3>
     <p class="prod-lead">Vous croisez votre nouvelle voisine le lendemain de votre emménagement. Excusez-vous du bruit de la veille en racontant ce qui s'est passé, demandez comment fonctionne l'immeuble, puis répondez à l'invitation qu'on vous fait.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Se présenter</div><div class="plan-ex">« Bonjour, je m'appelle Amadou Sow, je viens d'emménager dans le logement 4. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">S'excuser en racontant</div><div class="plan-ex">« Excusez-nous pour hier soir : le camion est arrivé en retard, et après, il pleuvait. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Demander comment ça fonctionne</div><div class="plan-ex">« La salle de lavage, ça marche comment ? Et le bac brun, c'est quel jour ? »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 4</div><div class="plan-t">Répondre à l'invitation</div><div class="plan-ex">« C'est gentil. Malheureusement, je travaille dimanche. Par contre, dimanche prochain, je serais libre. »</div></div>
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
           <div class="rec-lbl" id="recLbl">Touchez pour vous enregistrer</div>
           <div class="rec-hint">Parlez environ une minute. Vous pourrez recommencer autant de fois que vous voudrez.</div>
         </div>
       </div>
     </div>
     <div id="poPrev" class="hidden prod-tools" style="display:flex;flex-direction:column;gap:12px">
       <audio id="poAudio" controls style="width:100%"></audio>
       <textarea id="poText" rows="2" placeholder="Transcription automatique (vous pouvez la corriger)…"></textarea>
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
     <h3 class="prod-tit">Le courriel au propriétaire, trois jours après</h3>
     <p class="prod-lead">Vous avez emménagé et vous avez fini l'état des lieux. Écrivez à votre propriétaire pour confirmer votre entrée, signaler ce qui est à réparer et demander une date. De 6 à 10 phrases.</p>
     <div class="req">
       <div class="req-hd">Votre courriel doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Votre nom, le numéro du logement et la date de votre entrée</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Deux choses relevées à l'état des lieux, nommées et situées</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une préposition de temps : « à partir du », « d'ici », « jusqu'au »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une demande claire, sous forme de question polie</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une formule de fin et votre numéro de téléphone</span></div>
       </div>
       <div class="req-note">Nommez et situez, ne racontez pas : <em>« une égratignure de 40 cm près de la fenêtre du salon »</em>, et non <em>« le plancher est un peu magané »</em>.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">monsieur Rondeau, propriétaire</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Logement 4 — état des lieux et deux réparations</span></div>
       <textarea id="peText" rows="9" aria-label="Votre courriel" data-min="6" data-max="10" oninput="peCount()" placeholder="Bonjour monsieur Rondeau,&#10;&#10;Je suis Amadou Sow, le nouveau locataire du logement 4. J'ai emménagé le premier juillet…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 6 à 10</span>
         <button class="btn-prod" id="peBtn" type="button" onclick="peCheck()">Vérifier mon courriel</button>
       </div>
     </div>
     <div class="fb" id="peFb" aria-live="polite"></div>
     <div class="status" id="peStatus">Analyse en cours…</div>
     <div class="err" id="peErr"></div>
   </div>`;
  const rb=document.getElementById('recBtn'); if(rb) rb.addEventListener('click',toggleRec);

  // JE RETIENS DES MOTS — notes + cartes mémoire + autoévaluation
  const SELF=[
    "Je sais ce qu'est un état des lieux et je peux en écrire une ligne : nommer, situer, mesurer.",
    "Je distingue à l'oreille le son de « déménagement » et celui de « camion ».",
    "Je peux téléphoner à une compagnie de déménagement et donner ma situation en quelques phrases suivies.",
    "Je vais chercher ce qui s'ajoute au tarif : le minimum, le déplacement, les suppléments, l'assurance.",
    "J'emploie les pronoms « le », « lui », « y », « en » au lieu de tout répéter.",
    "Je peux diriger des déménageurs à l'impératif : « Montez-le », « Ne la posez pas là ».",
    "Je désigne les choses avec « ce », « cet », « cette », « ces » et « celui-là ».",
    "Je peux ouvrir un compte de services à mon nom et donner la bonne date.",
    "Je sais qui prévenir de mon changement d'adresse, et ce qui arrive si je l'oublie.",
    "Je peux raconter ma journée de déménagement au passé composé et à l'imparfait.",
    "Je peux demander à un voisin comment fonctionne l'immeuble.",
    "Je peux accepter ou refuser une invitation en donnant une raison et en proposant autre chose.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Les clés et l'état des lieux</div>
     <textarea rows="2" placeholder="Ex. : emménager, l'état des lieux, une égratignure, une fissure, une moustiquaire déchirée…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Le camion et les déménageurs</div>
     <textarea rows="2" placeholder="Ex. : un tarif horaire, le temps de déplacement, un dépôt, une couverture, un diable…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">L'adresse et les branchements</div>
     <textarea rows="2" placeholder="Ex. : brancher, un relevé de compteur, le réacheminement du courrier, à partir du…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">L'immeuble et les voisins</div>
     <textarea rows="2" placeholder="Ex. : la salle de lavage, le bac brun, le déneigement, rendre service, c'est gentil de me le proposer…"></textarea>
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
