  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : l'explication de l'entrave jouée avec l'assistant, le
  // message de retard laissé sur une boîte vocale, puis le courriel qui
  // prévient l'équipe d'un chantier annoncé. Le jeu de rôle vient en premier
  // parce qu'il sert de répétition aux deux autres — c'est là que l'élève
  // découvre que « ça bloque » ne fait décider personne.
  //
  // Le scénario `circulation` a été ajouté à server.py pour ce module. Le
  // scénario `chemin` existe déjà, mais il vient du niveau 4 : on y demande
  // son chemin à quelqu'un qui sait, en six étapes, avec des noms de
  // terminus. Ici c'est l'inverse — c'est l'élève qui sait, parce qu'il a
  // écouté le bulletin, et il doit expliquer à quelqu'un qui n'a rien
  // entendu. Seule la situation publique est ici ; ce que le collègue ignore
  // et ce que la responsable veut savoir vivent sur le serveur.
  const ROLE_CAS = [
    {id:'pont', titre:"Le pont fermé, au stationnement", txt:"Six heures cinquante-cinq. Vous venez d'entendre que <b>le pont Jacques-Cartier est fermé</b> en direction de Montréal jusqu'à neuf heures. Votre collègue vous attend dans son auto, moteur en marche. Il n'a pas écouté la radio et il allait prendre ce pont-là."},
    {id:'carambolage', titre:"Le carambolage sur la 40", txt:"Sept heures vingt, dans l'auto. Le bulletin vient d'annoncer <b>un carambolage de quatre véhicules</b> sur l'autoroute 40 en direction ouest, à la hauteur de Côte-de-Liesse : deux voies sur trois bloquées, les remorqueuses sur place. Votre collègue approche de l'entrée de l'autoroute et il attend votre avis maintenant."},
    {id:'travaux', titre:"La bretelle en travaux", txt:"Vendredi, seize heures. Le bulletin annonce que <b>la bretelle qui mène de la 15 nord à la 40 ouest sera fermée toute la fin de semaine</b>, pour des travaux de réfection de la chaussée. Votre collègue doit aller chercher quelqu'un samedi matin et il passe toujours par là."},
  ];
  const ROLE_SUJETS = ["Dire ce qui bloque avec le mot juste : un accident, un carambolage, des travaux, une panne",
    "Dire où, sur quelle route, et avec quel repère : à la hauteur de, entre… et…",
    "Dire dans quel sens : en direction de, dans les deux sens",
    "Dire depuis quand ça dure, et pour combien de temps encore",
    "Dire combien de voies sont bloquées, et lesquelles restent ouvertes",
    "Proposer un autre chemin, dans l'ordre et jusqu'au bout",
    "Annoncer une heure d'arrivée en chiffres — jamais « bientôt »",
    "Redire le plan en une phrase à la fin, pour vérifier qu'on a compris la même chose"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Expliquer ce que la radio vient de dire</span></div>
     <p class="lead">L'assistant joue Amine Haddad, votre collègue de covoiturage. Il conduit, il est pressé, et il n'a rien entendu : si vous dites seulement « ça bloque », il vous demandera où — et il redemandera. Il ne proposera jamais le détour à votre place. Essayez ensuite l'autre situation : la responsable de l'atelier, au téléphone, qui veut trois choses et une heure.</p>
     <p class="lead">Choisissez votre situation et qui vous avez en face</p>
     <div class="jr-annonces" id="jrLogs">
       ${ROLE_CAS.map((c,i)=>`<button class="jr-opt jr-tuile${i===0?' on':''}" type="button" data-log="${c.id}" onclick="jrChoisir('log','${c.id}')">
         <span class="jr-band"><span class="jr-band-off">Choix ${i+1}</span><span class="jr-band-on"><svg viewBox="0 0 20 20" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 10.5l4 4 8-9"></path></svg> Votre choix</span></span>
         <span class="jr-tuile-c"><span class="jr-tuile-t">${esc(c.titre)}</span><span class="jr-tuile-d">${c.txt}</span></span>
       </button>`).join('')}
     </div>
     <div class="jr-reglages">
       <div class="jr-carte">
         <div class="jr-champ-l">L'assistant joue qui ?</div>
         <div class="jr-tuiles" id="jrRoles">
         <button class="jr-opt on" type="button" data-role="collegue" onclick="jrChoisir('role','collegue')">Votre collègue, au volant</button>
         <button class="jr-opt" type="button" data-role="responsable" onclick="jrChoisir('role','responsable')">Votre responsable, au téléphone</button>
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
         <div class="jr-bande-t">Les huit choses à dire avant que l'auto démarre</div>
         <p class="jr-bande-p">${ROLE_SUJETS.map((s,i)=>i?s.charAt(0).toLowerCase()+s.slice(1):s).join(', ')}.</p>
       </div>
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()">Monter dans l'auto</button>
     </div>
     <div class="jr-rappel">
       <div class="jr-rappel-t">Réutilisez ce que vous venez d'apprendre</div>
       <div class="jr-rappel-g">
         <div><div class="jr-rappel-l">Donnez l'endroit avec deux repères, jamais un seul</div><div class="jr-rappel-x">C'est <b>sur</b> la 40, <b>à la hauteur de</b> la sortie Côte-de-Liesse, <b>en direction</b> ouest.</div></div>
         <div><div class="jr-rappel-l">Dites le temps de deux façons</div><div class="jr-rappel-x">C'est bloqué <b>depuis</b> sept heures. · <b>Ça fait</b> presque une heure <b>que</b> ça ne bouge plus. · Le pont est fermé <b>jusqu'à</b> neuf heures.</div></div>
         <div><div class="jr-rappel-l">Collez deux idées avec un relatif</div><div class="jr-rappel-x">La bretelle <b>qui</b> mène à la 40 ouest est fermée. · La voie de droite est la seule <b>qui</b> reste ouverte.</div></div>
         <div><div class="jr-rappel-l">Dites le moyen avec le gérondif</div><div class="jr-rappel-x"><b>En sortant</b> à Marcel-Laurin et <b>en prenant</b> le boulevard, on évite tout le secteur.</div></div>
         <div><div class="jr-rappel-l">Annoncez l'heure avec un futur</div><div class="jr-rappel-x">On <b>va être</b> en retard d'un quart d'heure. J'<b>arriverai</b> vers huit heures quinze.</div></div>
         <div><div class="jr-rappel-l">Reprenez la directive du bulletin telle quelle</div><div class="jr-rappel-x">Ils disent d'<b>emprunter</b> le pont Victoria. · <b>On demande aux automobilistes de</b> réduire leur vitesse.</div></div>
       </div>
     </div>

     <div id="jrChat" class="hidden">
       <div class="jr-fil" id="jrFil" aria-live="polite"></div>
       <div class="jr-mic hidden" id="jrMicZone">
         <button id="jrMic" type="button" onclick="jrParler()" aria-label="Parler"><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="3" width="6" height="11" rx="3"></rect><path d="M5.5 11.5a6.5 6.5 0 0013 0M12 18v3"></path></svg></button>
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
     <h3 class="prod-tit">Le message de retard sur la boîte vocale</h3>
     <p class="prod-lead">Sept heures vingt-cinq. Vous êtes bloqué sur l'autoroute et personne ne décroche à l'atelier. Vous laissez un message à votre responsable. Écrivez-le d'abord, lisez-le à voix haute, puis enregistrez-le. De trente à quarante-cinq secondes — cinq morceaux, dans l'ordre.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Qui parle, et à qui — dès la première phrase</div><div class="plan-ex">« Bonjour madame Lachance, c'est Tereza Nogueira, de l'atelier d'assemblage. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Ce qui bloque, et où — avec deux repères</div><div class="plan-ex">« Il y a eu un carambolage sur la 40, en direction ouest, à la hauteur de Côte-de-Liesse. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Depuis quand, et ce que vous faites</div><div class="plan-ex">« C'est bloqué depuis sept heures. On a quitté l'autoroute et on passe par le boulevard. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 4</div><div class="plan-t">L'heure d'arrivée en chiffres, et ce que vous proposez</div><div class="plan-ex">« J'arriverai vers huit heures quinze. Farida peut prendre les clés : elle entre à sept heures et demie. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 5</div><div class="plan-t">Comment vous joindre, et la politesse</div><div class="plan-ex">« Vous pouvez me joindre au 450 555-0143. Merci, et à tout à l'heure. »</div></div>
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
           <div class="rec-hint">De trente à quarante-cinq secondes. Réécoutez-vous comme si vous étiez la responsable, à huit heures moins vingt, avec l'atelier à ouvrir : savez-vous qui parle ? Pouvez-vous noter une heure d'arrivée sans faire répéter ? Savez-vous quoi faire en attendant ?</div>
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
     <h3 class="prod-tit">Le courriel qui prévient l'équipe</h3>
     <p class="prod-lead">Le bulletin de vendredi annonce que la bretelle qui mène de la 15 nord à la 40 ouest sera fermée toute la fin de semaine, et que les travaux se poursuivront lundi matin jusqu'à neuf heures. Vous écrivez aux quatre personnes de votre équipe pour qu'elles ne se fassent pas prendre lundi. De 6 à 9 phrases, avec « vous ».</p>
     <div class="req">
       <div class="req-hd">Votre courriel doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une salutation, et une phrase qui dit pourquoi vous écrivez</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce qui sera fermé, avec une phrase relative : « la bretelle qui… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Quand exactement : « de… à… », « jusqu'à… », « pendant… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Deux phrases au futur simple : ce qui arrivera lundi matin</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le chemin de rechange, avec un gérondif : « en sortant à… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une consigne claire à la fin, et une signature</span></div>
       </div>
       <div class="req-note">Un courriel de ce genre se lit en dix secondes, debout, sur un téléphone. Mettez l'information la plus importante dans la première phrase et la consigne dans la dernière : ce sont les deux seules que tout le monde lira.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">l'équipe de l'atelier d'assemblage</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Travaux sur la 15 : partez plus tôt lundi</span></div>
       <textarea id="peText" rows="9" aria-label="Votre courriel" data-min="6" data-max="9" oninput="peCount()" placeholder="Bonjour à tous,&#10;&#10;Je vous écris au sujet des travaux annoncés ce matin au bulletin de circulation…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 6 à 9</span>
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
    "Je connais les mots de l'état de la route : un ralentissement, un bouchon, une entrave, l'accotement.",
    "J'entends la différence entre le son de « an » et le son de « on ».",
    "Je sais qu'un bulletin donne toujours quatre choses : quoi, où, dans quel sens, combien de temps.",
    "Je nomme ce qui bloque avec le mot juste : un accident, un carambolage, des travaux, une panne.",
    "Je dis l'endroit avec deux repères : sur la 40, à la hauteur de la sortie, entre… et…",
    "Je dis le sens : en direction de, dans les deux sens.",
    "Je dis depuis quand et pour combien de temps : depuis, il y a, ça fait… que, pendant, jusqu'à.",
    "Je reconnais si une entrave était prévue ou si elle vient d'arriver.",
    "Je suis un bulletin de quatre routes sans perdre le début.",
    "Je prends une note pendant que j'écoute : une ligne par route, le nom d'abord.",
    "Je sais dire si une entrave me concerne, en regardant ma route, mon sens et l'heure.",
    "Je comprends les directives : empruntez, il est recommandé de, on demande aux automobilistes de.",
    "Je colle deux idées avec qui, que, où, dont.",
    "Je dis par quel chemin je passerai, avec un gérondif : en sortant à, en prenant.",
    "J'annonce mon arrivée avec une heure en chiffres, au futur proche ou au futur simple.",
    "Je laisse un message de retard qui donne tout ce qu'il faut, sans faire rappeler.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#1D6B8F">Je retiens des mots</span><span class="ctit" style="color:#1D6B8F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#1D6B8F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:6px 0 4px">L'état de la route</div>
     <textarea rows="2" placeholder="Ex. : un ralentissement, un bouchon, une entrave, l'accotement, la chaussée…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">L'incident et les secours</div>
     <textarea rows="2" placeholder="Ex. : un carambolage, une remorqueuse, un véhicule d'urgence, une voie bloquée…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">Le bulletin et ses repères</div>
     <textarea rows="2" placeholder="Ex. : à la hauteur de, en direction de, dans les deux sens, jusqu'à, une bretelle…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">Le trajet refait et le retard</div>
     <textarea rows="2" placeholder="Ex. : un détour, un imprévu, prévenir, le covoiturage, un stationnement incitatif…"></textarea>
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
