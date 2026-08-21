  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, le récit du dégât à
  // voix haute, la lettre de demande de réduction de loyer. Le jeu de rôle
  // vient en premier parce qu'il sert de répétition aux deux autres.
  // Le scénario `degat` a été ajouté à server.py pour ce module : celui du
  // niveau 4 (`probleme`) s'arrête au signalement, alors qu'ici la démarche
  // va jusqu'à la compensation. Seule la situation publique est ici ; ce que
  // le personnage joué par l'assistant sait de son côté vit sur le serveur.
  const ROLE_CAS = [
    {id:'plafond', titre:"Le plafond de la chambre", txt:"<b>Un cerne brun d'un mètre</b> au plafond de la chambre, apparu pendant la nuit. Le plancher gondole sur trois lattes le long du mur. Le matelas est humide sur un coin. La fuite venait du <b>chauffe-eau du logement du dessus</b>."},
    {id:'soussol', titre:"Le refoulement au sous-sol", txt:"<b>Cinq centimètres d'eau sale</b> dans le logement du sous-sol après un gros orage. Le drain a refoulé. Les boîtes rangées au fond sont perdues, le tapis est à jeter, et <b>l'odeur ne part pas</b>."},
    {id:'laveuse', titre:"Le boyau de la laveuse", txt:"<b>Le boyau de la laveuse du voisin</b> a cédé pendant qu'il était au travail. L'eau a traversé le plancher et coulé le long du mur de la cuisine d'en dessous. <b>La peinture cloque</b> et l'armoire du bas est gonflée."},
  ];
  const ROLE_SUJETS = ["Ce qui est arrivé, et quand","Ce qu'on voit aujourd'hui, pièce par pièce",
    "Ce qu'on a déjà fait pour limiter les dommages","La cause, si on la connaît",
    "Ce qu'on ne peut plus faire chez soi","La date de l'intervention",
    "Ce qui est demandé — et pourquoi"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Le signalement du dégât</span></div>
     <p class="lead">Vous avez tous les deux la même situation sous les yeux — rien de plus. L'assistant joue l'autre personne et ne donne jamais un renseignement avant qu'on le lui demande. Essayez les deux rôles : au niveau 5, il faut savoir <b>exposer</b> et savoir <b>questionner</b>.</p>
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
       Plantez le décor à l'imparfait :
       <span class='savoir-ex'>Il <b>faisait</b> encore noir et l'eau <b>coulait</b> déjà.</span>
       Racontez l'événement au passé composé :
       <span class='savoir-ex'>Je <b>me suis levée</b> à six heures et j'<b>ai mis</b> une chaudière.</span>
       Dites la simultanéité avec un gérondif :
       <span class='savoir-ex'><b>En rentrant</b> du travail, j'ai vu que la tache avait doublé.</span>
       Mettez en avant l'essentiel :
       <span class='savoir-ex'><b>Ce qui</b> m'inquiète, <b>c'est</b> l'humidité dans le matelas.</span>
       Terminez par une demande justifiée :
       <span class='savoir-ex'>Trois nuits sans chambre : <b>par conséquent</b>, je demande une réduction de loyer.</span>
     </div>

     <div class="jr-sep"></div>
     <div class="jr-sub">Choisissez votre situation et votre rôle</div>
     <div class="jr-choix">
       <div class="jr-choix-l">Quel dégât ?</div>
       <div class="jr-opts" id="jrLogs">
         ${ROLE_CAS.map((c,i)=>`<button class="jr-opt${i===0?' on':''}" type="button" data-log="${c.id}" onclick="jrChoisir('log','${c.id}')">${esc(c.titre)}</button>`).join('')}
       </div>
       <div class="jr-choix-l">Vous jouez qui ?</div>
       <div class="jr-opts" id="jrRoles">
         <button class="jr-opt on" type="button" data-role="locataire" onclick="jrChoisir('role','locataire')">La personne qui a le dégât</button>
         <button class="jr-opt" type="button" data-role="proprietaire" onclick="jrChoisir('role','proprietaire')">Le ou la propriétaire</button>
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
     <h3 class="prod-tit">Racontez un dégât</h3>
     <p class="prod-lead">Racontez un dégât d'eau — celui de Mariama, ou un que vous avez vécu. Plantez le décor, dites ce qui est arrivé, décrivez ce qui reste abîmé, et terminez par ce que vous demandez.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Planter le décor à l'imparfait</div><div class="plan-ex">« Il faisait encore noir. L'eau coulait déjà du plafond et je ne savais pas d'où ça venait. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Raconter au passé composé</div><div class="plan-ex">« Je me suis levée à six heures, j'ai mis une chaudière, puis j'ai appelé le propriétaire. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Décrire ce qui reste, pièce par pièce</div><div class="plan-ex">« Il y a un cerne d'un mètre au plafond, et le plancher gondole sur trois lattes. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 4</div><div class="plan-t">Demander, en disant pourquoi</div><div class="plan-ex">« Je n'ai pas pu coucher dans ma chambre pendant trois nuits : par conséquent, je demande une réduction de loyer. »</div></div>
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
     <h3 class="prod-tit">La demande de réduction de loyer</h3>
     <p class="prod-lead">Écrivez au propriétaire pour demander une réduction de loyer. Rappelez les faits, dites ce que vous avez perdu, donnez la cause, chiffrez votre demande et fixez un délai. De 8 à 12 phrases.</p>
     <div class="req">
       <div class="req-hd">Votre lettre doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Les faits datés, à l'imparfait et au passé composé</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce que vous n'avez pas pu faire, avec une durée chiffrée</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>La cause, avec « étant donné que » ou « puisque »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une phrase emphatique : « Ce que je demande, c'est… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le montant demandé et la date limite de réponse</span></div>
       </div>
       <div class="req-note">Demandez, ne menacez pas : <em>« Je vous saurais gré de me répondre avant le 30 novembre »</em>, et non <em>« Sinon j'irai au Tribunal. »</em></div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">le propriétaire de votre immeuble</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Demande de réduction de loyer — dégât d'eau du 10 novembre</span></div>
       <textarea id="peText" rows="10" aria-label="Votre lettre" data-min="8" data-max="12" oninput="peCount()" placeholder="Monsieur,&#10;&#10;Le 10 novembre au matin, un dégât d'eau est survenu dans ma chambre. L'eau coulait du plafond depuis plusieurs heures quand je me suis levée…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 8 à 12</span>
         <button class="btn-prod" id="peBtn" type="button" onclick="peCheck()">Vérifier ma lettre</button>
       </div>
     </div>
     <div class="fb" id="peFb" aria-live="polite"></div>
     <div class="status" id="peStatus">Analyse en cours…</div>
     <div class="err" id="peErr"></div>
   </div>`;
  const rb=document.getElementById('recBtn'); if(rb) rb.addEventListener('click',toggleRec);

  // JE RETIENS DES MOTS — notes + cartes mémoire + autoévaluation
  const SELF=[
    "Je peux nommer les dommages d'un dégât d'eau avec le mot juste : un cerne, gondoler, cloquer.",
    "Je sais quels gestes poser dans les premières heures, et dans quel ordre.",
    "Je peux raconter un sinistre en mêlant l'imparfait et le passé composé.",
    "Je peux dire deux choses à la fois avec un gérondif : « en rentrant », « en ouvrant ».",
    "Je peux signaler un dégât au téléphone et décrire les dommages pièce par pièce.",
    "Je comprends un avis affiché dans un immeuble, jusqu'aux lignes en petit.",
    "Je reconnais les tournures d'un avis officiel : « il est nécessaire que », « veuillez », « à défaut ».",
    "Je peux employer le subjonctif après « il faut que », « pour que » et « avant que ».",
    "Je sais à qui m'adresser : au propriétaire, à mon assureur, ou au Tribunal.",
    "Je peux écrire une demande de réduction de loyer avec sa cause, son montant et son délai.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#0D7A6F">Je retiens des mots</span><span class="ctit" style="color:#0D7A6F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#0D7A6F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#0D7A6F;font-size:13px;margin:6px 0 4px">Le dégât et ce qu'on voit</div>
     <textarea rows="2" placeholder="Ex. : un dégât d'eau, un cerne, le plafond coule, le plancher gondole, la peinture cloque…"></textarea>
     <div style="font-weight:800;color:#0D7A6F;font-size:13px;margin:12px 0 4px">Le constat et l'appel</div>
     <textarea rows="2" placeholder="Ex. : une fuite, une infiltration, un chauffe-eau, les dommages, faire constater…"></textarea>
     <div style="font-weight:800;color:#0D7A6F;font-size:13px;margin:12px 0 4px">L'avis et les travaux</div>
     <textarea rows="2" placeholder="Ex. : veuillez prévoir un accès, à défaut, l'assèchement, un asséchateur, le cas échéant…"></textarea>
     <div style="font-weight:800;color:#0D7A6F;font-size:13px;margin:12px 0 4px">La demande et la démarche</div>
     <textarea rows="2" placeholder="Ex. : une réclamation, une franchise, une réduction de loyer, une mise en demeure, par conséquent…"></textarea>
   </div>
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#0D7A6F">Autoévaluation</span><span class="ctit" style="color:#0D7A6F">Qu'est-ce que je suis capable de faire ?</span></div>
     <p class="lead">Pour chaque énoncé, choisissez : pas encore 😟, un peu 🙂, ou oui 😃.</p>
     ${SELF.map((s,i)=>`<div class="selfrow"><div class="self-txt">${s}</div><div class="self-opts">
        <button onclick="rate(${i},this)">😟</button><button onclick="rate(${i},this)">🙂</button><button onclick="rate(${i},this)">😃</button>
     </div></div>`).join('')}
     <div style="margin-top:16px"><button class="btn btn-pri" onclick="finishEval()">Terminer le module 🎉</button></div>
     <div id="evalDone" class="fb" aria-live="polite"></div>
   </div>`;
}
