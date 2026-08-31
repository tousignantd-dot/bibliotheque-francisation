  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, puis le carton d'invitation qu'on glisse sous les portes.
  // Le jeu de rôle vient en premier parce qu'il sert de répétition.
  // Seule la situation publique est côté client ; ce que sait la voisine
  // jouée par l'assistant vit dans server.py.
  const ROLE_CAS = [
    {id:'permission', titre:'La remise de la cour', txt:"Ton <b>vélo</b> dort dans le corridor et il gêne tout le monde. Ta voisine du dessous range le sien dans la petite remise, au fond de la cour. Tu descends lui demander si tu peux y mettre le tien."},
    {id:'invitation', titre:'Le café de samedi', txt:"Des voisins t'ont aidé à monter tes <b>boîtes</b>. Tu prépares un café et un dessert chez toi, samedi après-midi, et tu descends inviter ta voisine du deuxième de vive voix."},
    {id:'perdu', titre:"L'affiche dans l'entrée", txt:"Une <b>affiche</b> est apparue dans l'entrée : le chat de ta voisine n'est pas rentré depuis deux jours. Tu crois l'avoir vu hier soir dans la ruelle, et tu frappes chez elle pour le lui dire."},
  ];
  const ROLE_SUJETS = ["Saluer et dire pourquoi tu viens",
    "Demander la permission poliment","Comprendre la réponse : oui, oui mais, ou non",
    "Donner le jour, l'heure et l'endroit de ton invitation",
    "Faire un compliment ou remercier de l'aide reçue",
    "Décrire l'animal, l'objet ou la personne dont tu parles",
    "Remercier et saluer avant de partir"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Frappe chez ta voisine</span></div>
     <p class="lead">L'assistant joue <b>Manon Lachapelle, la voisine du deuxième</b>. Elle est aimable, mais elle ne dit rien que tu ne lui demandes pas : la permission, la couleur du chat, le nom du concierge, tout se demande. À toi de poser tes questions.</p>
     <p class="lead">Choisis ta situation et ton rôle</p>
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
         <button class="jr-opt on" type="button" data-role="voisine" onclick="jrChoisir('role','voisine')">La voisine du deuxième</button>
         <button class="jr-opt" type="button" data-role="voisin" onclick="jrChoisir('role','voisin')">Le nouveau voisin du troisième</button>
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
         <div><div class="jr-rappel-l">Annonce-toi</div><div class="jr-rappel-x">Excusez-moi de vous déranger, <b>je m'appelle</b> Rachid, du troisième.</div></div>
         <div><div class="jr-rappel-l">Demande la permission</div><div class="jr-rappel-x"><b>Est-ce que je pourrais</b> mettre mon vélo dans la remise ?</div></div>
         <div><div class="jr-rappel-l">Invite</div><div class="jr-rappel-x"><b>C'est samedi, à deux heures, chez nous</b>, au 3A.</div></div>
         <div><div class="jr-rappel-l">Décris</div><div class="jr-rappel-x">Il est <b>roux, assez gros</b>, avec une <b>tache blanche</b> sous le menton.</div></div>
         <div><div class="jr-rappel-l">Conclus</div><div class="jr-rappel-x"><b>Merci, c'est gentil.</b> Bonne journée !</div></div>
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
     <h3 class="prod-tit">Demande une permission, puis invite ta voisine</h3>
     <p class="prod-lead">Tu frappes chez ta voisine. Salue-la et dis en une phrase pourquoi tu viens. Demande ta permission poliment. Profites-en pour l'inviter : donne le jour, l'heure et l'endroit. Remercie avant de partir.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Saluer et dire pourquoi tu viens</div><div class="plan-ex">« Bonjour, madame. Excusez-moi de vous déranger : mon vélo gêne dans le corridor. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Demander la permission</div><div class="plan-ex">« Est-ce que je pourrais le mettre dans la remise, en arrière ? »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Inviter, puis remercier</div><div class="plan-ex">« On fait un petit café samedi, à deux heures, chez nous. Merci, c'est gentil ! »</div></div>
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
     <h3 class="prod-tit">Écris le carton que tu glisses sous les portes</h3>
     <p class="prod-lead">Tu invites les voisins de ton immeuble. Écris le carton que tu vas glisser sous chaque porte : dis à quelle occasion, donne le jour, l'heure et l'endroit, dis ce qu'il y aura, et demande une réponse. De 5 à 8 phrases.</p>
     <div class="req">
       <div class="req-hd">Ton carton doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>L'occasion : pourquoi tu invites</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le jour, l'heure et l'endroit — les trois</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce qu'il y aura, et ce qu'on apporte (ou pas)</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une phrase au futur simple : « La rencontre aura lieu… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une demande de réponse : « Confirmez SVP »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ton nom et ton numéro de porte</span></div>
       </div>
       <div class="req-note">Attention : les noms de jours ne prennent pas de majuscule — on écrit <em>samedi le 14</em>, jamais « Samedi ». Et l'heure s'écrit <em>14 h</em>, avec une espace avant le h.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">Mes voisins de l'immeuble</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Une invitation</span></div>
       <textarea id="peText" rows="7" aria-label="Ton carton d'invitation" data-min="5" data-max="8" oninput="peCount()" placeholder="Bonjour ! Nous venons d'arriver au 3A.&#10;Nous aimerions vous connaître…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 5 à 8</span>
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
    "Je peux nommer les lieux d'un immeuble : le palier, la remise, la cour, la ruelle, les boîtes aux lettres.",
    "Je peux me présenter à un voisin : mon nom, mon étage, depuis quand j'habite là.",
    "Je peux présenter quelqu'un et dire le lien qui nous unit.",
    "Je peux demander une permission poliment, avec « est-ce que je peux » ou « est-ce que je pourrais ».",
    "Je comprends la réponse à ma demande : « bien sûr », « oui, mais… », « je préfère que non ».",
    "Je peux inviter quelqu'un en donnant le jour, l'heure et l'endroit.",
    "Je peux répondre à une invitation : accepter, ou refuser en disant pourquoi.",
    "Je peux faire un compliment court et répondre à un compliment par un merci.",
    "Je peux décrire une personne, un animal ou un objet perdu : la couleur, la taille, le détail.",
    "Je peux écrire un carton d'invitation avec « la fête aura lieu » et « confirmez SVP ».",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#1D6B8F">Je retiens des mots</span><span class="ctit" style="color:#1D6B8F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#1D6B8F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:6px 0 4px">L'immeuble et ses gens</div>
     <textarea rows="2" placeholder="Ex. : un voisin, une voisine, un immeuble, le palier, le concierge, la cour, la ruelle, faire connaissance…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">Demander la permission</div>
     <textarea rows="2" placeholder="Ex. : la permission, une remise, une corde à linge, déranger, Est-ce que je peux… ? Bien sûr, allez-y. Je préfère que non…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">Inviter et remercier</div>
     <textarea rows="2" placeholder="Ex. : une invitation, fêter, apporter, un compliment, C'est samedi à deux heures, chez nous. Que c'est bon ! Merci, c'est gentil…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">Décrire ce qui manque</div>
     <textarea rows="2" placeholder="Ex. : une affiche, un collier, un trousseau de clés, roux, assez gros, une tache blanche, très peureux, un peu usé…"></textarea>
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
