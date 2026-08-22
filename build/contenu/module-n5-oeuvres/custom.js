  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : la conversation jouée avec l'assistant, la
  // présentation de deux minutes enregistrée au club, puis le carton du
  // babillard des coups de cœur. Le jeu de rôle vient en premier parce qu'il
  // sert de répétition aux deux autres — c'est là que l'élève découvre qu'un
  // « c'était bon » ne fait lire personne.
  //
  // Le scénario `oeuvres` a été ajouté à server.py pour ce module : aucun
  // scénario existant ne convenait, parce qu'aucun ne demandait à l'élève de
  // porter un jugement et de le défendre. Les trois cas — le trottoir devant
  // le cinéma, le comptoir de la bibliothèque, la salle du fond le jeudi
  // soir — reprennent les trois lieux du module. Seule la situation publique
  // est ici ; ce que Karim ignore, ce que Nadia veut savoir et ce que
  // Gilberte demande toujours après une présentation vivent sur le serveur.
  const ROLE_CAS = [
    {id:'film', titre:"Devant le cinéma, un mardi soir", txt:"Vous sortez d'un film que la personne à qui vous parlez <b>n'a pas vu</b> et qu'elle hésite à aller voir. Elle veut savoir de quoi ça parle et si ça vaut la peine — mais elle ne veut surtout pas qu'on lui dise comment ça finit. Racontez le début, donnez votre avis, et tenez-le : elle n'aime pas les histoires qui se passent dans le passé, et elle vous le dira."},
    {id:'bd', titre:"Au comptoir de la bibliothèque", txt:"Vous avez lu <b>une seule bande dessinée</b> dans votre vie et vous en voudriez une autre, mais vous ne savez pas quoi demander. La personne au comptoir peut vous en conseiller une — à condition que vous lui disiez ce que vous avez lu, ce que vous en avez pensé et ce que vous cherchez cette fois-ci. Servez-vous des mots du Défi 2 : une case, une bulle, une planche, un album, un tome."},
    {id:'club', titre:"Le club du jeudi, dans la salle du fond", txt:"Dix-huit heures trente, une dizaine de chaises en cercle. Chacun présente en <b>deux minutes</b> une œuvre — un livre, un film, une chanson, une série — et dit pourquoi il la conseille. C'est votre tour. On ne raconte pas la fin, on justifie ce qu'on avance, et quelqu'un dans le groupe ne sera pas d'accord avec vous."},
  ];
  const ROLE_SUJETS = ["Dire de quelle œuvre vous parlez : le titre, le genre et le support",
    "Situer l'histoire en une phrase : où et quand ça se passe",
    "Présenter le personnage principal et ce qu'il veut, avec « qui » ou « que »",
    "Raconter au présent ce qui met l'histoire en marche",
    "Vous arrêter au moment du choix, sans jamais dévoiler le dénouement",
    "Reprendre l'œuvre autrement à chaque fois : cet album, cette histoire, cette œuvre",
    "Donner votre avis avec un adjectif précis, jamais avec « c'est bon »",
    "Mettre votre avis en avant : « moi, ce qui m'a touché, c'est… »",
    "Justifier votre avis par au moins une raison, avec « parce que » ou un deux-points",
    "Accorder à l'autre ce qu'il a de juste, puis dire pourquoi vous pensez autrement",
    "Dire à qui vous recommandez l'œuvre, et pourquoi à cette personne-là"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Parler d'une œuvre à quelqu'un qui ne la connaît pas</span></div>
     <p class="lead">L'assistant joue la personne en face de vous : Karim Belkacem sur le trottoir devant le cinéma, Nadia Ferland au comptoir de la bibliothèque, ou Gilberte Sanschagrin qui anime le club du jeudi. Aucun des trois ne connaît votre œuvre, aucun ne devine, et aucun ne se contentera d'un « c'était bon » : on vous demandera une fois pourquoi. Vous pouvez aussi renverser les rôles et tenir vous-même le comptoir, pendant que l'assistant joue un membre du club qui s'exprime mal.</p>
     <div class="jr-grid">
       ${ROLE_CAS.map(c=>`
       <div class="jr-log">
         <div class="jr-log-h">${esc(c.titre)}</div>
         <div class="jr-log-a">${c.txt}</div>
       </div>`).join('')}
     </div>
     <div class="jr-sub">Les onze choses à faire avant la fin de la rencontre</div>
     <div class="jr-sujets">
       ${ROLE_SUJETS.map(s=>`<div class="jr-sujet"><span class="jr-box"></span>${esc(s)}</div>`).join('')}
     </div>
     <div class="jr-gram">
       <div class="jr-gram-t">Réutilisez ce que vous venez d'apprendre</div>
       Racontez l'histoire au présent, un moment après l'autre :
       <span class='savoir-ex'>Elle <b>arrive</b> au village. Elle <b>ouvre</b> la maison de sa mère. Elle <b>trouve</b> une boîte de lettres.</span>
       Recollez vos phrases avec qui, que, où :
       <span class='savoir-ex'>C'est une femme <b>qui</b> revient dans le village <b>qu'</b>elle a quitté il y a vingt ans. · Le jour <b>où</b> elle ouvre la boîte, tout change.</span>
       Reprenez l'œuvre sans vous répéter :
       <span class='savoir-ex'>C'est un album de bande dessinée. <b>Ce livre</b> compte cinquante planches. <b>Cette œuvre</b> m'a pris deux soirées.</span>
       Désignez sans nommer chaque fois :
       <span class='savoir-ex'>J'ai lu deux albums ; <b>celui que</b> je préfère est le deuxième. · <b>Celle qui</b> a la couverture bleue.</span>
       Mettez votre avis en avant, et donnez la raison :
       <span class='savoir-ex'><b>Moi, ce qui m'a touchée, c'est</b> le silence entre les deux sœurs, <b>parce que</b> le temps du livre est le temps du village.</span>
       Accordez d'abord, tournez ensuite :
       <span class='savoir-ex'><b>C'est vrai que</b> c'est lent. <b>Par contre</b>, c'est justement ce que j'ai aimé.</span>
       Et posez la limite, avec le sourire :
       <span class='savoir-ex'><b>Je m'arrête ici</b> : je ne vous dis pas ce qu'elle choisit. <b>Lisez-le</b>, vous verrez.</span>
     </div>

     <div class="jr-sep"></div>
     <div class="jr-sub">Choisissez la situation et qui vous avez en face</div>
     <div class="jr-choix">
       <div class="jr-choix-l">Quelle situation ?</div>
       <div class="jr-opts" id="jrLogs">
         ${ROLE_CAS.map((c,i)=>`<button class="jr-opt${c.id==='club'?' on':''}" type="button" data-log="${c.id}" onclick="jrChoisir('log','${c.id}')">${esc(c.titre)}</button>`).join('')}
       </div>
       <div class="jr-choix-l">L'assistant joue qui ?</div>
       <div class="jr-opts" id="jrRoles">
         <button class="jr-opt on" type="button" data-role="interlocuteur" onclick="jrChoisir('role','interlocuteur')">La personne en face</button>
         <button class="jr-opt" type="button" data-role="membre" onclick="jrChoisir('role','membre')">Un membre du club (c'est vous qui animez)</button>
       </div>
       <div class="jr-choix-l">Comment ?</div>
       <div class="jr-opts" id="jrModes">
         <button class="jr-opt on" type="button" data-mode="texte" onclick="jrModeVoix(false)">✍️ Écrire</button>
         <button class="jr-opt" type="button" data-mode="voix" onclick="jrModeVoix(true)">🎤 Parler</button>
       </div>
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()" style="margin-top:14px">Commencer la rencontre</button>
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
     <h3 class="prod-tit">Vos deux minutes au club du jeudi</h3>
     <p class="prod-lead">C'est votre tour. Dix personnes vous écoutent, personne ne vous coupe, et personne ne connaît l'œuvre dont vous parlez. Prenez une œuvre que vous avez vraiment lue, vue ou écoutée — dans n'importe quelle langue, vous la présentez en français. Écrivez d'abord votre présentation, lisez-la à voix haute, puis enregistrez-la. De cent à cent trente secondes — cinq temps, dans l'ordre.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">De quoi vous parlez : le titre, le genre, le support</div><div class="plan-ex">« Bonsoir. Je vous apporte un roman, une histoire de famille, à peu près trois cents pages. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Le cadre et le personnage, au présent, avec « qui » ou « que »</div><div class="plan-ex">« Ça se passe aujourd'hui, dans un village au bord de la mer. C'est une femme qui revient dans le village qu'elle a quitté il y a vingt ans. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Ce qui met l'histoire en marche — et l'endroit où vous vous arrêtez</div><div class="plan-ex">« Elle vient vendre la maison de sa mère et repartir le jour même. Mais elle ouvre la maison et elle trouve une boîte de lettres. Je m'arrête ici. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 4</div><div class="plan-t">Votre avis, mis en avant, avec un adjectif précis et sa raison</div><div class="plan-ex">« Moi, ce qui m'a touchée, c'est le silence entre les deux sœurs : elles ne se disent presque rien, et on comprend tout quand même. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 5</div><div class="plan-t">Une réserve, puis à qui vous le recommandez</div><div class="plan-ex">« Ce que j'ai le moins aimé, c'est la longueur du début. Par contre, je le recommande à quelqu'un qui a quitté un pays : il va reconnaître quelque chose. »</div></div>
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
           <div class="rec-hint">De cent à cent trente secondes. Réécoutez-vous comme si vous étiez dans le cercle de chaises : savez-vous dès la première phrase s'il s'agit d'un livre ou d'un film ? Est-ce que l'histoire avance sans qu'on sache comment elle finit ? Est-ce qu'il y a un adjectif précis quelque part, et une raison derrière lui ?</div>
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
     <h3 class="prod-tit">Le carton du babillard des coups de cœur</h3>
     <p class="prod-lead">À l'entrée de la bibliothèque, un babillard porte les coups de cœur des membres du club. Chacun tient sur un carton, écrit à la main, et les gens s'arrêtent devant en attendant leur tour au comptoir. Écrivez le vôtre pour la même œuvre que votre présentation. De 7 à 10 phrases, avec « vous » : vous ne savez pas qui le lira.</p>
     <div class="req">
       <div class="req-hd">Votre carton doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le support et le genre dès la première phrase</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Deux phrases au présent qui racontent le début, sans la fin</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une phrase avec « qui », « que » ou « où »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une reprise de l'œuvre par un autre mot : cette histoire, ce livre, cette œuvre</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Votre avis mis en avant : « ce qui m'a touché, c'est… », avec sa raison</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une exclamation avec « quel », « quelle », « quels » ou « quelles »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>À qui vous le recommandez, et votre prénom au bas du carton</span></div>
       </div>
       <div class="req-note">Le carton est lu par quelqu'un qui passe et qui ne vous connaît pas. Il n'a pas trente secondes : la première phrase doit dire ce que c'est, et la dernière doit dire à qui c'est. Entre les deux, ne racontez jamais la fin — le babillard est à l'entrée d'une bibliothèque, et tout le monde y a droit à sa surprise.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">Babillard</span><span class="mail-v">Les coups de cœur du club du jeudi</span></div>
       <div class="mail-row"><span class="mail-k">Titre du carton</span><span class="mail-v">Mon coup de cœur du mois</span></div>
       <textarea id="peText" rows="10" aria-label="Votre carton" data-min="7" data-max="10" oninput="peCount()" placeholder="C'est un roman, une histoire de famille, à peu près trois cents pages…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 7 à 10</span>
         <button class="btn-prod" id="peBtn" type="button" onclick="peCheck()">Vérifier mon carton</button>
       </div>
     </div>
     <div class="fb" id="peFb" aria-live="polite"></div>
     <div class="status" id="peStatus">Analyse en cours…</div>
     <div class="err" id="peErr"></div>
   </div>`;
  const rb=document.getElementById('recBtn'); if(rb) rb.addEventListener('click',toggleRec);

  // JE RETIENS DES MOTS — notes + cartes mémoire + autoévaluation
  const SELF=[
    "Je nomme une œuvre et son support : un roman, un film, une série, une bande dessinée, une chanson.",
    "Je connais les mots du club : une œuvre, un extrait, un coup de cœur, l'intrigue, le dénouement.",
    "J'entends la différence entre le son de « j » et le son de « ch ».",
    "Je dis en une phrase de quoi je parle : le titre, le genre et le support.",
    "Je raconte une histoire au présent, un moment après l'autre.",
    "Je distingue une action en cours d'une action habituelle en ajoutant un repère de temps.",
    "Je relie mes phrases avec « qui », « que » et « où » au lieu de les mettre bout à bout.",
    "Je sais où m'arrêter : je ne raconte jamais le dénouement.",
    "Je connais les mots de la bande dessinée : une case, une bulle, une planche, une onomatopée, un album.",
    "Je désigne sans répéter le nom : celui que j'ai lu, celle qui m'a marquée, ceux du début.",
    "Je reprends l'œuvre autrement à chaque phrase : cet album, ce livre, cette histoire, cette œuvre.",
    "Je distingue un fait vérifiable d'un avis qui m'appartient.",
    "Je donne mon avis avec un adjectif précis plutôt qu'avec « c'est bon ».",
    "Je mets mon avis en avant : « moi, ce qui m'a touché, c'est… ».",
    "Je justifie mon avis avec « parce que », « puisque » ou après un deux-points.",
    "Je m'exclame en accordant le déterminant : quel personnage, quelle histoire, quelles couleurs.",
    "Je réponds à quelqu'un qui pense autrement : j'accorde d'abord, puis je dis pourquoi.",
    "Je dis à qui je recommande l'œuvre, et pourquoi à cette personne-là.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">L'œuvre et son support</div>
     <textarea rows="2" placeholder="Ex. : une œuvre, un roman, une série, un album, un extrait, un coup de cœur…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">L'histoire</div>
     <textarea rows="2" placeholder="Ex. : l'intrigue, un personnage, le dénouement, ça se passe, elle revient, elle découvre…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">La bande dessinée</div>
     <textarea rows="2" placeholder="Ex. : une case, une bulle, une planche, une onomatopée, un album, un tome…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Mon avis et ma raison</div>
     <textarea rows="2" placeholder="Ex. : émouvant, prévisible, recommander, moi ce qui m'a touché c'est, parce que, par contre…"></textarea>
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
