  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : la décision défendue devant le coordonnateur du
  // Centre, le message vocal laissé au groupe, puis l'avis affiché à la porte.
  // Le jeu de rôle vient en premier parce qu'il sert de répétition aux deux
  // autres — c'est là que l'élève découvre qu'une décision sans raison se fait
  // discuter jusqu'au bout de la conversation.
  //
  // Le scénario `saisons` a été ajouté à server.py pour ce module. Aucun des
  // scénarios existants ne convenait : `meteo`, au niveau 2, échange trois
  // mots sur le temps qu'il fait le matin même, et `circulation`, au niveau 5,
  // fait expliquer une entrave déjà en cours pour refaire son propre trajet.
  // Ici, ce qui est en jeu est une décision qui engage trente personnes pour
  // la semaine prochaine, prise à partir d'un avis qui annonce, et qui doit
  // être justifiée devant quelqu'un qui la conteste. Seule la situation
  // publique est ici ; ce que Réjean objecte et ce que madame Bérubé craint
  // vivent sur le serveur.
  const ROLE_CAS = [
    {id:'verglas', titre:"Le verglas de vendredi soir", txt:"Jeudi, dix-sept heures trente. Environnement Canada vient d'émettre un <b>avertissement de pluie verglaçante</b> pour le Bas-Saint-Laurent : de trois à cinq millimètres de glace, de vendredi soir à samedi matin. Votre marche à la promenade de la mer est prévue samedi à treize heures, avec trente personnes dont huit ont plus de soixante-dix ans."},
    {id:'crue', titre:"La crue printanière au parc du Bic", txt:"Mercredi, en fin d'avant-midi. Le dégel des derniers jours a fait monter l'eau : <b>les sentiers du bas du parc national du Bic sont inondés</b> et le parc annonce une réouverture dans deux semaines. Votre visite guidée est prévue dimanche, l'autobus est réservé mais pas encore payé, et vingt-deux personnes sont inscrites."},
    {id:'chaleur', titre:"La chaleur extrême de la fin de semaine", txt:"Jeudi midi, en juillet. Un <b>avertissement de chaleur extrême</b> est en vigueur de jeudi à dimanche : trente-deux degrés, humidex de trente-neuf, indice UV de neuf. Le tournoi de pétanque du Centre est prévu samedi à quatorze heures, en plein soleil, sur le terrain derrière l'édifice."},
  ];
  const ROLE_SUJETS = ["Dire quel avis est en vigueur, et lequel des trois mots il porte : veille ou avertissement",
    "Dire le phénomène, la région et le moment — les trois choses que l'avis donne toujours",
    "Dire l'effet attendu en chiffres : des millimètres de glace, des degrés, un indice UV",
    "Dire ce que l'effet devient au moment exact de l'activité, pas au moment du phénomène",
    "Annoncer la décision d'un seul tenant : maintenue, reportée ou annulée",
    "Donner la raison dans la même phrase, avec un connecteur de cause",
    "Donner la nouvelle date, l'heure et le lieu, si c'est un report",
    "Dire ce que les gens devront apporter, à l'impératif, et comment s'y prendre"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Défendre votre décision</span></div>
     <p class="lead">L'assistant joue Réjean Pelletier, le coordonnateur du Centre communautaire de la Pointe. Il n'a pas écouté la radio, il trouve que vous décidez vite, et il vous demandera pourquoi — deux fois s'il le faut. Il ne prendra jamais la décision à votre place. Essayez ensuite l'autre situation : madame Bérubé, au téléphone, qui a soixante-quinze ans, qui attendait cette sortie depuis un mois et qui veut surtout savoir ce qu'elle apporte.</p>
     <div class="jr-grid">
       ${ROLE_CAS.map(c=>`
       <div class="jr-log">
         <div class="jr-log-h">${esc(c.titre)}</div>
         <div class="jr-log-a">${c.txt}</div>
       </div>`).join('')}
     </div>
     <div class="jr-sub">Les huit choses à dire avant de raccrocher</div>
     <div class="jr-sujets">
       ${ROLE_SUJETS.map(s=>`<div class="jr-sujet"><span class="jr-box"></span>${esc(s)}</div>`).join('')}
     </div>
     <div class="jr-gram">
       <div class="jr-gram-t">Réutilisez ce que vous venez d'apprendre</div>
       Nommez l'avis avec le mot juste :
       <span class='savoir-ex'>Ce n'est plus une <b>veille</b>, c'est un <b>avertissement</b> : il est <b>en vigueur</b> jusqu'à samedi matin.</span>
       Annoncez la prévision au futur simple :
       <span class='savoir-ex'>La pluie verglaçante <b>débutera</b> vendredi en soirée et les trottoirs <b>deviendront</b> très glissants.</span>
       Employez une phrase impersonnelle :
       <span class='savoir-ex'><b>Il tombera</b> de trois à cinq millimètres de glace. · <b>Il y aura</b> de la glace au sol toute la journée.</span>
       Donnez la raison avec un connecteur de cause :
       <span class='savoir-ex'><b>Comme</b> les trottoirs seront glacés, la sortie est reportée. · Elle est reportée <b>parce qu'</b>un avertissement est en vigueur.</span>
       Dites la décision au présent, la suite au futur :
       <span class='savoir-ex'>La sortie <b>est reportée</b> ; elle <b>aura lieu</b> le samedi 22, à treize heures.</span>
       Donnez la consigne à l'impératif et la manière au gérondif :
       <span class='savoir-ex'><b>Apportez</b> vos crampons. Vous éviterez les chutes <b>en les attachant</b> avant de sortir.</span>
     </div>

     <div class="jr-sep"></div>
     <div class="jr-sub">Choisissez votre situation et qui vous avez en face</div>
     <div class="jr-choix">
       <div class="jr-choix-l">Quelle situation ?</div>
       <div class="jr-opts" id="jrLogs">
         ${ROLE_CAS.map((c,i)=>`<button class="jr-opt${i===0?' on':''}" type="button" data-log="${c.id}" onclick="jrChoisir('log','${c.id}')">${esc(c.titre)}</button>`).join('')}
       </div>
       <div class="jr-choix-l">L'assistant joue qui ?</div>
       <div class="jr-opts" id="jrRoles">
         <button class="jr-opt on" type="button" data-role="rejean" onclick="jrChoisir('role','rejean')">Réjean, le coordonnateur</button>
         <button class="jr-opt" type="button" data-role="participante" onclick="jrChoisir('role','participante')">Madame Bérubé, au téléphone</button>
       </div>
       <div class="jr-choix-l">Comment ?</div>
       <div class="jr-opts" id="jrModes">
         <button class="jr-opt on" type="button" data-mode="texte" onclick="jrModeVoix(false)">✍️ Écrire</button>
         <button class="jr-opt" type="button" data-mode="voix" onclick="jrModeVoix(true)">🎤 Parler</button>
       </div>
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()" style="margin-top:14px">Frapper à la porte du bureau</button>
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
     <h3 class="prod-tit">Le message laissé au groupe</h3>
     <p class="prod-lead">Jeudi, dix-huit heures. Vous avez tranché : la sortie de samedi ne se fera pas comme prévu. Vous laissez un message sur la boîte vocale du groupe — trente personnes l'écouteront une seule fois, sans pouvoir vous demander de répéter. Écrivez-le d'abord, lisez-le à voix haute, puis enregistrez-le. De trente à quarante-cinq secondes — cinq morceaux, dans l'ordre.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Qui parle, à qui, et de quelle activité</div><div class="plan-ex">« Bonjour à tous, c'est Marisol du Centre de la Pointe, au sujet de la marche de samedi. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">La décision, d'un seul tenant, dès la deuxième phrase</div><div class="plan-ex">« La sortie est reportée au samedi 22 février, à la même heure, au même endroit. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">La raison, avec un connecteur de cause et un futur</div><div class="plan-ex">« Comme un avertissement de pluie verglaçante est en vigueur, il y aura de la glace au sol toute la journée de samedi. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 4</div><div class="plan-t">Ce qu'il faudra apporter, à l'impératif, et comment</div><div class="plan-ex">« Apportez vos crampons et habillez-vous en trois couches : vous resterez confortable en enlevant une couche au café. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 5</div><div class="plan-t">Ce que les gens doivent faire, et comment vous joindre</div><div class="plan-ex">« Si la nouvelle date ne vous convient pas, appelez-moi avant jeudi au 418 555-0172. Merci, et à bientôt. »</div></div>
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
           <div class="rec-hint">De trente à quarante-cinq secondes. Réécoutez-vous comme si vous étiez madame Bérubé, soixante-quinze ans, qui écoute son répondeur jeudi soir : savez-vous tout de suite si la sortie a lieu ? Pouvez-vous noter une date sans faire répéter ? Savez-vous quoi mettre dans votre sac ?</div>
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
     <h3 class="prod-tit">L'avis affiché à la porte du Centre</h3>
     <p class="prod-lead">Le même soir, vous écrivez l'avis que les gens liront demain matin, en entrant, debout, leur manteau sur le bras. Il annonce le report, il dit pourquoi, il donne la nouvelle date et il rappelle ce qu'il faudra apporter. De 6 à 9 phrases, avec « vous ».</p>
     <div class="req">
       <div class="req-hd">Votre avis doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une première phrase qui dit la décision — pas la météo</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>La raison, avec « étant donné que », « comme » ou « parce que »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le nom exact de l'avis : veille ou avertissement, et de quel phénomène</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Deux phrases au futur simple : la nouvelle date, l'heure, le lieu</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Deux consignes à l'impératif, dont une avec un gérondif de manière</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce que doit faire la personne à qui la date ne convient pas, et votre nom</span></div>
       </div>
       <div class="req-note">Un avis affiché se lit en dix secondes, debout. Mettez la décision dans la première phrase et la marche à suivre dans la dernière : ce sont les deux seules que tout le monde lira jusqu'au bout.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">Affiché</span><span class="mail-v">à la porte du Centre communautaire de la Pointe</span></div>
       <div class="mail-row"><span class="mail-k">Titre</span><span class="mail-v">Marche du 8 février — nouvelle date</span></div>
       <textarea id="peText" rows="9" aria-label="Votre avis" data-min="6" data-max="9" oninput="peCount()" placeholder="AVIS AUX PARTICIPANTS&#10;&#10;La marche du samedi 8 février est reportée…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 6 à 9</span>
         <button class="btn-prod" id="peBtn" type="button" onclick="peCheck()">Vérifier mon avis</button>
       </div>
     </div>
     <div class="fb" id="peFb" aria-live="polite"></div>
     <div class="status" id="peStatus">Analyse en cours…</div>
     <div class="err" id="peErr"></div>
   </div>`;
  const rb=document.getElementById('recBtn'); if(rb) rb.addEventListener('click',toggleRec);

  // JE RETIENS DES MOTS — notes + cartes mémoire + autoévaluation
  const SELF=[
    "Je connais les trois avis d'Environnement Canada : le bulletin spécial, la veille, l'avertissement.",
    "Je sais qu'une veille annonce un phénomène possible et qu'un avertissement annonce un phénomène imminent.",
    "J'entends la différence entre le son de « é » et le son de « è ».",
    "Je nomme les phénomènes de l'hiver : la pluie verglaçante, la poudrerie, une bordée de neige.",
    "Je comprends le refroidissement éolien et je sais que c'est le vent qui décide, pas le thermomètre.",
    "Je repère dans un bulletin le phénomène, la région, le moment et l'effet attendu.",
    "Je dis si un avertissement touche mon activité, en regardant la région, l'heure et l'effet qui reste.",
    "J'emploie le futur simple pour annoncer ce qui arrivera : il tombera, il fera, il y aura.",
    "J'emploie les phrases impersonnelles du temps : il neige, il vente, il faut, il est possible que.",
    "Je choisis entre maintenir, reporter et annuler, selon qu'une date de rechange existe ou non.",
    "Je donne la raison de ma décision avec parce que, comme, puisque ou étant donné que.",
    "Je choisis entre le futur proche et le futur simple selon que la chose est toute proche ou au calendrier.",
    "Je donne une consigne à l'impératif sans avoir l'air de commander.",
    "Je dis la manière avec un gérondif : en buvant, en s'habillant, en partant plus tôt.",
    "Je sais ce qu'il faut apporter par grand froid comme par chaleur extrême.",
    "Je laisse au groupe un message qui donne la décision, la raison, la date et l'équipement.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#1D6B8F">Je retiens des mots</span><span class="ctit" style="color:#1D6B8F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#1D6B8F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:6px 0 4px">L'avis météo</div>
     <textarea rows="2" placeholder="Ex. : une veille, un avertissement, en vigueur, levé, les prévisions, une éclaircie…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">L'hiver</div>
     <textarea rows="2" placeholder="Ex. : la pluie verglaçante, la poudrerie, le refroidissement éolien, une bordée de neige…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">La décision</div>
     <textarea rows="2" placeholder="Ex. : maintenir, reporter, annuler, la crue printanière, le dégel, étant donné que…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">L'équipement des quatre saisons</div>
     <textarea rows="2" placeholder="Ex. : des crampons, trois couches, la chaleur extrême, l'indice UV, un coup de chaleur…"></textarea>
   </div>
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#1D6B8F">Autoévaluation</span><span class="ctit" style="color:#1D6B8F">Qu'est-ce que je suis capable de faire ?</span></div>
     <p class="lead">Pour chaque énoncé, choisissez : pas encore 😟, un peu 🙂, ou oui 😃.</p>
     ${SELF.map((s,i)=>`<div class="selfrow"><div class="self-txt">${s}</div><div class="self-opts">
        <button onclick="rate(${i},this)">😟</button><button onclick="rate(${i},this)">🙂</button><button onclick="rate(${i},this)">😃</button>
     </div></div>`).join('')}
     <div style="margin-top:16px"><button class="btn btn-pri" onclick="finishEval()">Terminer le module 🎉</button></div>
     <div id="evalDone" class="fb" aria-live="polite"></div>
   </div>`;
}
