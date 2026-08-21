  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : la discussion avec l'assistant, un compte rendu oral
  // corrigé, puis le billet de blogue écrit. Le jeu de rôle vient en premier
  // parce qu'il sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait l'interlocuteur
  // joué par l'assistant vit dans server.py, scénario « actualite ».
  const ROLE_CAS = [
    {id:'depot', titre:'Le point de dépôt', txt:"Le comité exécutif recommande le local de la <b>rue Boisjoli</b> pour le futur point de dépôt de consigne. Le conseil tranche le 14 octobre. Les heures d'ouverture ne sont pas fixées."},
    {id:'stationnement', titre:'Les huit places', txt:"Deux des <b>huit places</b> devant le dépanneur seraient réservées aux usagers du dépôt, avec une limite de quinze minutes. Le commerçant craint de perdre des clients."},
    {id:'chronique', titre:'La chronique de samedi', txt:"Une chroniqueuse écrit que le projet a été « <b>imposé</b> au quartier ». Les chiffres qu'elle cite sont exacts ; le mot « imposé », lui, se discute."},
  ];
  const ROLE_SUJETS = ["Résumer la nouvelle en deux ou trois phrases",
    "Dire d'où vient votre information","Séparer ce qui est confirmé de ce qui ne l'est pas",
    "Écouter l'avis de l'autre sans l'interrompre",
    "Lui accorder un point avant de donner le vôtre",
    "Donner votre opinion en la présentant comme une opinion",
    "Poser la question que personne n'a posée"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Discutez de la nouvelle</span></div>
     <p class="lead">L'assistant joue <b>un voisin qui n'a pas le même avis que vous</b>. Il connaît le dossier et il ne se laisse pas convaincre en une phrase : à vous de résumer, de nuancer et de concéder avant d'objecter.</p>
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
       Marquez ce qui n'est pas confirmé :
       <span class='savoir-ex'>Selon ce que j'ai entendu, le local <b>serait</b> loué pour cinq ans.</span>
       Rapportez ce que quelqu'un a dit :
       <span class='savoir-ex'>La conseillère a dit que la décision <b>serait prise</b> le 14 octobre.</span>
       Accordez un point avant d'objecter :
       <span class='savoir-ex'><b>Bien que</b> le projet <b>soit</b> utile, personne ne connaît les heures.</span>
       Mettez en avant ce qui compte :
       <span class='savoir-ex'><b>Ce qui</b> m'inquiète, <b>c'est</b> l'heure de fermeture.</span>
       Restreignez :
       <span class='savoir-ex'>La Ville <b>ne</b> fournit <b>que</b> le local.</span>
     </div>

     <div class="jr-sep"></div>
     <div class="jr-sub">Choisissez votre situation et votre rôle</div>
     <div class="jr-choix">
       <div class="jr-choix-l">Quel sujet ?</div>
       <div class="jr-opts" id="jrLogs">
         ${ROLE_CAS.map((c,i)=>`<button class="jr-opt${i===0?' on':''}" type="button" data-log="${c.id}" onclick="jrChoisir('log','${c.id}')">${esc(c.titre)}</button>`).join('')}
       </div>
       <div class="jr-choix-l">Vous jouez qui ?</div>
       <div class="jr-opts" id="jrRoles">
         <button class="jr-opt on" type="button" data-role="citoyen" onclick="jrChoisir('role','citoyen')">Le citoyen informé</button>
         <button class="jr-opt" type="button" data-role="voisin" onclick="jrChoisir('role','voisin')">Le voisin sceptique</button>
       </div>
       <div class="jr-choix-l">Comment ?</div>
       <div class="jr-opts" id="jrModes">
         <button class="jr-opt on" type="button" data-mode="texte" onclick="jrModeVoix(false)">✍️ Écrire</button>
         <button class="jr-opt" type="button" data-mode="voix" onclick="jrModeVoix(true)">🎤 Parler</button>
       </div>
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()" style="margin-top:14px">Commencer la discussion</button>
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
     <h3 class="prod-tit">Faites le compte rendu de la nouvelle</h3>
     <p class="prod-lead">Quelqu'un de votre entourage n'a rien suivi de l'affaire. Racontez-lui en 90 secondes environ : ce dont il s'agit, ce qui est établi, ce qui ne l'est pas, et ce que vous en pensez.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">De quoi il s'agit, et d'où vous le savez</div><div class="plan-ex">« Il y a un reportage à la radio du quartier sur un point de dépôt de consigne, rue Boisjoli. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Les faits établis, puis ce qui ne l'est pas</div><div class="plan-ex">« Le comité a retenu le local. Par contre, les heures d'ouverture ne seraient pas encore fixées. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Votre opinion, annoncée comme une opinion</div><div class="plan-ex">« Bien que le projet soit une bonne chose, je trouve qu'il manque une réponse sur l'horaire. »</div></div>
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
           <div class="rec-hint">Parlez environ 90 secondes. Vous pourrez recommencer autant de fois que vous voulez.</div>
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
     <h3 class="prod-tit">Écrivez votre billet dans Le fil du Ruisseau</h3>
     <p class="prod-lead">Suzie vous ouvre le blogue du quartier. Écrivez de 8 à 12 phrases, en deux ou trois courts paragraphes : les faits, votre opinion présentée comme telle, et la question que personne n'a posée.</p>
     <div class="req">
       <div class="req-hd">Votre billet doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Au moins deux faits vérifiables, avec un chiffre ou une date</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une information non confirmée, marquée au conditionnel</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une parole rapportée : « la conseillère a dit que… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une concession avec « bien que » ou « même si »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une mise en relief : « ce qui… c'est » ou « c'est… qui »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un connecteur de topicalisation : quant à, en ce qui concerne</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une question posée aux lecteurs, à la fin</span></div>
       </div>
       <div class="req-note">Nommez vos sources et écrivez « à ma connaissance » quand vous n'êtes pas certain. On ne reproche jamais à quelqu'un d'avoir dit ce qu'il ignorait ; on lui reproche d'avoir affirmé sans vérifier.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">Blogue</span><span class="mail-v">Le fil du Ruisseau — nouveau billet</span></div>
       <div class="mail-row"><span class="mail-k">Titre</span><span class="mail-v">À vous de le trouver — court, et sans jugement</span></div>
       <textarea id="peText" rows="10" aria-label="Votre billet" data-min="8" data-max="12" oninput="peCount()" placeholder="Depuis lundi, on parle beaucoup du local de la rue Boisjoli.&#10;Voici ce que j'ai compris, et la question que je me pose…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 8 à 12</span>
         <button class="btn-prod" id="peBtn" type="button" onclick="peCheck()">Vérifier mon texte</button>
       </div>
     </div>
     <div class="fb" id="peFb" aria-live="polite"></div>
     <div class="status" id="peStatus">Analyse en cours…</div>
     <div class="err" id="peErr"></div>
   </div>`;
  const rb=document.getElementById('recBtn'); if(rb) rb.addEventListener('click',toggleRec);

  // JE RETIENS DES MOTS — notes + cartes mémoire + autoévaluation
  const SELF=[
    "Je nomme les genres de l'information : reportage, chronique, éditorial, billet.",
    "Je distingue un fait d'une opinion, et je repère un jugement déguisé en constat.",
    "J'écoute un reportage de trois minutes en plusieurs fois, sans me décourager.",
    "Je reconnais le conditionnel de l'information non confirmée.",
    "Je repère les connecteurs qui organisent un long discours : quant à, par ailleurs, en somme.",
    "Je comprends une phrase passive et je sais qui n'y est pas nommé.",
    "Je rapporte au passé ce que quelqu'un a dit, en changeant les temps.",
    "Je retrouve le verbe caché derrière un nom : ouverture, décision, report.",
    "J'accorde un point avec « bien que » ou « même si » avant de donner mon avis.",
    "Je mets en avant ce qui compte avec « ce qui… c'est » et « c'est… qui ».",
    "Je peux faire le compte rendu d'un fait d'actualité à quelqu'un de mon entourage.",
    "Je peux écrire un billet de blogue qui sépare les faits de mon opinion.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Les genres de l'information</div>
     <textarea rows="2" placeholder="Ex. : un reportage, une chronique, un éditorial, un billet de blogue, une manchette, une source…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Écouter le reportage</div>
     <textarea rows="2" placeholder="Ex. : un fait, une opinion, un porte-parole, un extrait sonore, la consigne, selon nos informations…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Lire l'article</div>
     <textarea rows="2" placeholder="Ex. : une entrevue, un communiqué, une séance du conseil, la période de questions, a été retenu…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Discuter et donner son avis</div>
     <textarea rows="2" placeholder="Ex. : un argument, une nuance, un commentaire, bien que, même si, ce qui… c'est, ne… que…"></textarea>
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
