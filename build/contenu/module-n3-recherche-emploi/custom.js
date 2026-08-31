  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, puis la petite annonce qu'on punaise au babillard.
  // Le jeu de rôle vient en premier parce qu'il sert de répétition : on
  // pousse la porte pour de faux avant de la pousser pour de vrai.
  // Seule la situation publique est ici ; ce que sait le gérant joué par
  // l'assistant vit dans server.py, scénario « embauche ».
  const ROLE_CAS = [
    {id:'affiche', titre:'La boulangerie', txt:"Une <b>affiche rouge</b> est collée dans la vitrine de la boulangerie : « On embauche ». Tu pousses la porte à neuf heures et demie, quand le comptoir est calme, et tu demandes si ça engage encore."},
    {id:'centre', titre:'Le centre communautaire', txt:"Le <b>centre Léo-Bourdon</b> cherche quelqu'un pour l'entretien. Il n'y a pas d'affiche : c'est une voisine qui te l'a dit. Tu entres à l'accueil et tu demandes à qui parler."},
    {id:'babillard', titre:"L'épicerie", txt:"Une petite annonce est punaisée au <b>babillard</b> de l'épicerie, près des paniers. Elle demande une personne pour remplir les tablettes, le matin. Tu l'apportes à la caisse et tu offres tes services."},
  ];
  const ROLE_SUJETS = ["Saluer et dire en une phrase pourquoi tu viens",
    "Demander si ça engage encore",
    "Dire ce que tu sais faire et ce que tu as déjà fait",
    "Comprendre le poste : les tâches, l'horaire, le salaire",
    "Donner tes disponibilités avec des jours et des heures",
    "Épeler ton nom et donner ton numéro de téléphone",
    "Demander quand on te rappellera, puis remercier"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Pousse la porte</span></div>
     <p class="lead">Tu joues la personne qui cherche du travail. L'assistant joue <b>le gérant du commerce</b> : il est occupé, il est correct, mais il ne donne que ce que tu lui demandes. L'horaire, le salaire, les tâches, la date du rappel — tout se demande. À toi de poser tes questions.</p>
     <p class="lead">Choisis ta situation et ton rôle</p>
     <div class="jr-annonces" id="jrLogs">
       ${ROLE_CAS.map((c,i)=>`<button class="jr-opt jr-tuile${i===0?' on':''}" type="button" data-log="${c.id}" onclick="jrChoisir('log','${c.id}')">
         <span class="jr-band"><span class="jr-band-off">Choix ${i+1}</span><span class="jr-band-on"><svg viewBox="0 0 20 20" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 10.5l4 4 8-9"></path></svg> Votre choix</span></span>
         <span class="jr-tuile-c"><span class="jr-tuile-t">${esc(c.titre)}</span><span class="jr-tuile-d">${c.txt}</span></span>
       </button>`).join('')}
     </div>
     <div class="jr-reglages">
       <div class="jr-carte">
         <div class="jr-champ-l">Toi, tu joues qui ?</div>
         <div class="jr-tuiles" id="jrRoles">
         <button class="jr-opt on" type="button" data-role="candidat" onclick="jrChoisir('role','candidat')">La personne qui offre ses services</button>
         <button class="jr-opt" type="button" data-role="gerant" onclick="jrChoisir('role','gerant')">Le gérant du commerce</button>
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
         <div><div class="jr-rappel-l">Annonce-toi</div><div class="jr-rappel-x">Bonjour. Excusez-moi de vous déranger, <b>j'ai vu votre affiche</b> dans la vitrine.</div></div>
         <div><div class="jr-rappel-l">Pose la question</div><div class="jr-rappel-x"><b>Est-ce que vous engagez</b> encore ?</div></div>
         <div><div class="jr-rappel-l">Dis ce que tu sais faire</div><div class="jr-rappel-x"><b>Je sais faire</b> le ménage. <b>J'ai de l'expérience en</b> garde d'enfants.</div></div>
         <div><div class="jr-rappel-l">Donne tes disponibilités</div><div class="jr-rappel-x">Je suis libre <b>du lundi au vendredi</b>, le matin, <b>de 8 h à 13 h</b>.</div></div>
         <div><div class="jr-rappel-l">Laisse tes coordonnées</div><div class="jr-rappel-x"><b>Vous pouvez me joindre au</b> 438 555-0192. Je peux vous l'écrire ?</div></div>
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
     <h3 class="prod-tit">Entre et offre tes services</h3>
     <p class="prod-lead">Tu pousses la porte d'un commerce de ton quartier. Salue et dis en une phrase pourquoi tu viens. Demande si ça engage. Dis ce que tu sais faire et quand tu es libre. Laisse ton nom, épelle-le, et donne ton numéro de téléphone chiffre par chiffre. Remercie avant de partir.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Saluer, dire pourquoi tu viens, demander si ça engage</div><div class="plan-ex">« Bonjour. J'ai vu votre affiche dans la vitrine. Est-ce que vous engagez encore ? »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Dire ce que tu sais faire et quand tu es libre</div><div class="plan-ex">« Je sais faire le ménage et j'ai de l'expérience en cuisine. Je suis libre du lundi au vendredi, le matin. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Laisser ton nom et ton numéro, puis remercier</div><div class="plan-ex">« Je m'appelle… T-R-A-O-R-É. Vous pouvez me joindre au 438 555-0192. Merci, bonne journée ! »</div></div>
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
     <h3 class="prod-tit">Écris la petite annonce que tu vas punaiser</h3>
     <p class="prod-lead">Tu offres tes services au babillard de ton quartier. Écris l'annonce que tu vas punaiser : un titre en haut, ce que tu sais faire, quand tu es libre, ce que tu demandes de l'heure, et ton numéro de téléphone en bas. De 5 à 8 phrases.</p>
     <div class="req">
       <div class="req-hd">Ton annonce doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un titre court, en haut : le service que tu offres</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ton prénom et ton quartier — jamais ton adresse complète</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce que tu sais faire, et depuis combien de temps</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Tes disponibilités : « du lundi au vendredi, de 8 h à 13 h »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce que tu demandes : « 20 $ de l'heure »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ton numéro de téléphone, tout en bas</span></div>
       </div>
       <div class="req-note">Attention : les noms de jours ne prennent pas de majuscule — on écrit <em>du lundi au vendredi</em>, jamais « Lundi ». L'heure s'écrit <em>8 h</em>, avec une espace avant le h, et le montant <em>20 $</em>, avec le signe après le nombre.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">Où</span><span class="mail-v">Le babillard de l'épicerie du quartier</span></div>
       <div class="mail-row"><span class="mail-k">Titre</span><span class="mail-v">Le service que tu offres</span></div>
       <textarea id="peText" rows="7" aria-label="Ta petite annonce" data-min="5" data-max="8" oninput="peCount()" placeholder="MÉNAGE ET GARDE D'ENFANTS&#10;Je m'appelle… et j'habite dans le quartier…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 5 à 8</span>
         <button class="btn-prod" id="peBtn" type="button" onclick="peCheck()">Vérifier mon annonce</button>
       </div>
     </div>
     <div class="fb" id="peFb" aria-live="polite"></div>
     <div class="status" id="peStatus">Analyse en cours…</div>
     <div class="err" id="peErr"></div>
   </div>`;
  const rb=document.getElementById('recBtn'); if(rb) rb.addEventListener('click',toggleRec);

  // JE RETIENS DES MOTS — notes + cartes mémoire + autoévaluation
  const SELF=[
    "Je peux lire une affiche d'embauche et comprendre ce qu'elle demande.",
    "Je peux entrer dans un commerce et dire en une phrase pourquoi je viens.",
    "Je peux demander si ça engage : « Est-ce que vous engagez ? »",
    "Je peux dire ce que je sais faire avec « je sais faire » et « j'ai de l'expérience en ».",
    "Je peux donner mes disponibilités avec des jours et des heures.",
    "Je peux épeler mon nom et donner mon numéro de téléphone chiffre par chiffre.",
    "Je peux lire une offre d'emploi simple : le poste, l'horaire, le salaire, à qui parler.",
    "Je comprends « de l'heure », « par semaine » et « payé aux deux semaines ».",
    "Je comprends « expérience exigée », « aucune expérience exigée » et « un atout ».",
    "Je peux remplir un formulaire de demande d'emploi en lettres moulées, sans laisser de case vide.",
    "Je peux écrire une petite annonce de six lignes pour offrir mes services.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#1D6B8F">Je retiens des mots</span><span class="ctit" style="color:#1D6B8F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#1D6B8F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:6px 0 4px">L'affiche et le métier</div>
     <textarea rows="2" placeholder="Ex. : un emploi, embaucher, engager, un métier, un patron, une affiche, On embauche, un curriculum vitæ…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">Offrir ses services</div>
     <textarea rows="2" placeholder="Ex. : offrir ses services, un commis, l'expérience, les disponibilités, Est-ce que vous engagez ? Je sais faire… Je suis libre…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">Lire une offre d'emploi</div>
     <textarea rows="2" placeholder="Ex. : une offre d'emploi, un babillard, le salaire, un horaire, le temps partiel, de l'heure, par semaine, aucune expérience exigée, un atout…"></textarea>
     <div style="font-weight:800;color:#1D6B8F;font-size:13px;margin:12px 0 4px">Le formulaire et l'annonce</div>
     <textarea rows="2" placeholder="Ex. : un formulaire, les lettres moulées, une petite annonce, écrivez, cochez, signez, datez, joignez une copie…"></textarea>
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
