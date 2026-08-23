  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : l'appel à l'employeur avec l'assistant, l'exposé oral
  // qui compare deux régions, puis la lettre d'accompagnement écrite. Le jeu
  // de rôle vient en premier parce qu'il sert de répétition aux deux autres.
  //
  // D'où viennent ces tâches. La production écrite est l'intention même du
  // programme pour la situation « Recherche d'emploi » : rédiger un curriculum
  // vitæ et une lettre d'accompagnement. La production orale et le jeu de rôle
  // n'ont, eux, aucune intention dans cette situation : ils se tirent des
  // attentes de fin de cours du niveau 7 — « il expose les avantages et les
  // inconvénients de deux situations ou contextes pour prendre une décision »,
  // « en classe, il fait un exposé informel sur un thème concret », et « au
  // cours d'une entrevue de sélection, il répond de façon complète à des
  // questions ouvertes concernant son expérience de travail, sa formation et
  // ses projets professionnels ».
  //
  // Seule la situation publique est côté client ; ce que sait l'interlocuteur
  // joué par l'assistant vit dans server.py, scénario « recherche ».
  const ROLE_CAS = [
    {id:'labo', titre:'Le poste au laboratoire', txt:"Deux postes de <b>technicienne ou technicien de laboratoire</b> sont affichés chez Alumico, à Jonquière, depuis février. Quart de jour, poste permanent, entrée en fonction en janvier. Le chef de laboratoire a dit à la radio qu'il préférait un appel avant de recevoir un dossier."},
    {id:'installation', titre:"L'aide à l'installation", txt:"L'offre mentionne un <b>programme d'aide à l'installation</b> pour les personnes venant d'une autre région. Ni le montant, ni les conditions, ni la durée ne sont écrits nulle part."},
    {id:'equivalence', titre:'Le diplôme obtenu ailleurs', txt:"Votre diplôme technique a été obtenu à l'étranger. Vous avez une <b>évaluation comparative</b> du gouvernement du Québec, mais ce n'est pas une équivalence. L'offre demande « un diplôme d'études collégiales <b>ou une expérience équivalente vérifiable</b> »."},
  ];
  const ROLE_SUJETS = ["Vous présenter et dire d'où vous appelez",
    "Dire où vous avez vu l'offre, et laquelle",
    "Poser une question ouverte sur les tâches réelles du poste",
    "Poser une question sur ce que l'annonce ne dit pas",
    "Relier votre expérience à ce que l'entreprise fait vraiment",
    "Employer le conditionnel de politesse au moins deux fois",
    "Demander comment et à qui faire parvenir votre dossier"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Appelez avant de postuler</span></div>
     <p class="lead">L'assistant joue <b>le chef du laboratoire d'une usine de région</b>. Il est occupé, il répond volontiers, mais il ne devine rien : à vous de poser des questions ouvertes et de faire le lien entre son usine et votre parcours.</p>
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
       Demandez poliment :
       <span class='savoir-ex'><b>Pourriez-vous</b> me préciser à quelle date l'entrée en fonction est prévue ?</span>
       Dites votre but :
       <span class='savoir-ex'>Je vous appelle <b>pour que vous ayez</b> mon nom en tête avant de recevoir mon dossier.</span>
       Mettez en avant ce qui compte :
       <span class='savoir-ex'><b>Ce que j'apporte, c'est</b> neuf ans de contrôle de conformité.</span>
       Restreignez :
       <span class='savoir-ex'>Je <b>n'</b>ai travaillé <b>qu'</b>en laboratoire industriel.</span>
       Changez de sujet proprement :
       <span class='savoir-ex'><b>Quant à</b> l'installation dans la région, j'aurais une question.</span>
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
         <button class="jr-opt on" type="button" data-role="candidat" onclick="jrChoisir('role','candidat')">La personne qui postule</button>
         <button class="jr-opt" type="button" data-role="conjoint" onclick="jrChoisir('role','conjoint')">La personne qui déménagerait avec elle</button>
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
     <h3 class="prod-tit">Comparez deux régions devant la classe</h3>
     <p class="prod-lead">Deux minutes environ, debout, sans lire vos notes mot à mot. Vous avez examiné deux régions du Québec où votre métier se pratique. Exposez les avantages et les inconvénients de chacune, avec des chiffres, puis annoncez votre décision et justifiez-la.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Les deux régions, et pourquoi celles-là</div><div class="plan-ex">« J'ai regardé le Saguenay–Lac-Saint-Jean et Chaudière-Appalaches, parce que mon métier se pratique dans les deux. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Les avantages et les inconvénients, chiffres à l'appui</div><div class="plan-ex">« Quant à la première, la fabrication y occupe onze virgule deux pour cent de l'emploi, contre sept pour cent ailleurs. En revanche, elle est plus loin de ma famille. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Votre décision, et la raison qui a pesé le plus</div><div class="plan-ex">« En somme, je choisis la première. Ce qui a pesé le plus, c'est qu'on y cherche des techniciens depuis six mois. »</div></div>
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
           <div class="rec-hint">Parlez environ deux minutes. Vous pourrez recommencer autant de fois que vous voulez.</div>
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
     <h3 class="prod-tit">Écrivez la lettre qui accompagnera votre curriculum vitæ</h3>
     <p class="prod-lead">De 10 à 14 phrases, en trois paragraphes. Le premier dit ce que vous demandez et où vous avez vu l'offre. Le deuxième relie votre expérience à ce que l'entreprise fait. Le troisième demande la rencontre. La lettre ne répète pas le curriculum vitæ : elle répond à une seule question — pourquoi vous, et pourquoi ici.</p>
     <div class="req">
       <div class="req-hd">Votre lettre doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le titre exact du poste, recopié de l'annonce</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Deux conditionnels de politesse : je souhaiterais, pourriez-vous</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une mise en avant : « ce que j'apporte, c'est… » ou « c'est… qui »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un but avec « pour que » et un subjonctif</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un connecteur qui change de sujet : quant à, en ce qui concerne</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une tâche précise avec un chiffre vérifiable</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une phrase sur votre disponibilité pour la région</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une demande de rencontre, à la fin</span></div>
       </div>
       <div class="req-note">Tenez le même ton du début à la fin : on ne commence pas en vouvoyant poliment pour finir par « à bientôt ! ». Et n'écrivez rien que votre curriculum vitæ ne puisse confirmer.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">Alumico — service des ressources humaines, Jonquière</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Candidature au poste de technicienne ou technicien de laboratoire — contrôle de la qualité</span></div>
       <textarea id="peText" rows="12" aria-label="Votre lettre" data-min="10" data-max="14" oninput="peCount()" placeholder="Madame, Monsieur,&#10;&#10;Je souhaiterais poser ma candidature au poste de…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 10 à 14</span>
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
    "Je nomme les outils de la recherche d'emploi : IMT en ligne, la salle multiservice, l'évaluation comparative.",
    "Je sais ce que l'évaluation comparative dit, et ce qu'elle ne dit pas.",
    "J'entends le « e » qui tombe au milieu d'un mot, et je reconnais le mot quand même.",
    "Je retrouve le verbe caché sous un nom : transformation, embauche, recrutement.",
    "J'écoute un reportage économique en plusieurs fois, sans me décourager.",
    "Je repère les connecteurs qui font tourner un long discours : quant à, par ailleurs, en somme.",
    "Je comprends « ne… que », et je ne le confonds pas avec une négation.",
    "Je compare deux régions avec des chiffres : plus de, moins de, le plus, meilleur.",
    "Je lis un portrait économique en vingt minutes, en posant trois questions au document.",
    "Je comprends une phrase passive et je sais qui n'y est pas nommé.",
    "Je repère un « ils » sans antécédent et je cherche son référent dans le paragraphe d'avant.",
    "Je mets en avant ce qui compte avec « c'est… qui » et « ce que…, c'est ».",
    "J'emploie le conditionnel de politesse dans une lettre, et le subjonctif après « pour que ».",
    "Je peux retailler mon curriculum vitæ pour une offre précise.",
    "Je peux écrire une lettre d'accompagnement en trois paragraphes.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#0D7A6F">Je retiens des mots</span><span class="ctit" style="color:#0D7A6F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#0D7A6F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#0D7A6F;font-size:13px;margin:6px 0 4px">Les outils de la recherche</div>
     <textarea rows="2" placeholder="Ex. : le marché du travail, la salle multiservice, une évaluation comparative, une perspective d'emploi…"></textarea>
     <div style="font-weight:800;color:#0D7A6F;font-size:13px;margin:12px 0 4px">L'économie d'une région</div>
     <textarea rows="2" placeholder="Ex. : un secteur d'activité, la transformation, une usine, la main-d'œuvre, la relève, un quart de travail…"></textarea>
     <div style="font-weight:800;color:#0D7A6F;font-size:13px;margin:12px 0 4px">Lire et comparer</div>
     <textarea rows="2" placeholder="Ex. : le produit intérieur brut, un portrait économique, l'embauche, quant à, en somme, contre…"></textarea>
     <div style="font-weight:800;color:#0D7A6F;font-size:13px;margin:12px 0 4px">Poser sa candidature</div>
     <textarea rows="2" placeholder="Ex. : une offre d'emploi, une candidature, un atout, je souhaiterais, pourriez-vous, ce que j'apporte, c'est…"></textarea>
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
