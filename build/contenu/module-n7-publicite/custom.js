  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : l'appel au service à la clientèle avec l'assistant,
  // l'exposé qui démonte une publicité, puis la lettre de réclamation. Le jeu
  // de rôle vient en premier parce qu'il sert de répétition aux deux autres.
  //
  // D'où viennent ces tâches. La situation « Publicité » n'a AUCUNE intention
  // de production : ses deux intentions sont de compréhension — comprendre
  // une publicité comportant un message implicite, à l'oral et à l'écrit. Les
  // trois tâches se tirent donc des attentes de fin de cours du niveau 7, qui
  // sont communes à tout le cours et qui, elles, sont productives : « dans le
  // contexte d'achat de biens, il manifeste sa déception et son
  // mécontentement en formulant une réclamation ou en fournissant des
  // explications » (le jeu de rôle), « en classe, il fait un exposé informel
  // sur un thème concret en fonction de ses centres d'intérêts » (l'exposé),
  // et « à l'aide d'un modèle, il rédige une lettre de réclamation » (la
  // lettre). C'est écrit ici pour que le relecteur suivant ne prenne pas ces
  // tâches pour une invention hors programme.
  //
  // Seule la situation publique est côté client ; ce que sait la personne
  // jouée par l'assistant vit dans server.py, scénario « publicite ».
  const ROLE_CAS = [
    {id:'abonnement', titre:"L'abonnement à 9,99 $", txt:"L'annonce disait <b>neuf dollars quatre-vingt-dix-neuf par semaine</b>. Le premier relevé indique <b>cent quatorze dollars et quatre-vingt-treize cents</b>. Le dépliant portait un astérisque, et la condition en bas de page mentionnait douze mois et soixante dollars de frais d'adhésion."},
    {id:'trottinette', titre:"La trottinette « offerte »", txt:"Une vidéo présente une trottinette que la personne dit avoir <b>reçue de l'entreprise</b>. Rien n'indique nulle part qu'il s'agit d'une publicité, et un code de réduction est donné à la fin. Votre enfant de onze ans l'a vue."},
    {id:'affiche', titre:"L'affiche du commerce neuf", txt:"Un commerce a ouvert sur votre rue. Le nom, en anglais, occupe presque toute la devanture ; <b>trois mots de français</b> sont écrits en petit à côté. L'affichage est visible depuis le trottoir."},
  ];
  const ROLE_SUJETS = ["Vous présenter et dire pourquoi vous appelez",
    "Rappeler ce que l'annonce laissait croire, sans accuser",
    "Demander ce que l'annonce ne disait pas, en une question précise",
    "Faire préciser les montants, les durées et les dates",
    "Reformuler la réponse : « autrement dit… », « si je comprends bien… »",
    "Employer le conditionnel de politesse au moins deux fois",
    "Demander une confirmation écrite avant de raccrocher"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Appelez et faites préciser</span></div>
     <p class="lead">L'assistant joue <b>la personne du service à la clientèle</b>. Elle est polie et pressée, elle répond à ce qu'on lui demande — mais elle ne devine rien : à vous de nommer ce que l'annonce laissait croire et de poser la question précise.</p>
     <p class="lead">Choisissez votre situation et votre rôle</p>
     <div class="jr-annonces" id="jrLogs">
       ${ROLE_CAS.map((c,i)=>`<button class="jr-opt jr-tuile${i===0?' on':''}" type="button" data-log="${c.id}" onclick="jrChoisir('log','${c.id}')">
         <span class="jr-band"><span class="jr-band-off">Choix ${i+1}</span><span class="jr-band-on"><svg viewBox="0 0 20 20" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 10.5l4 4 8-9"></path></svg> Votre choix</span></span>
         <span class="jr-tuile-c"><span class="jr-tuile-t">${esc(c.titre)}</span><span class="jr-tuile-d">${c.txt}</span></span>
       </button>`).join('')}
     </div>
     <div class="jr-reglages">
       <div class="jr-carte">
         <div class="jr-champ-l">Vous jouez qui ?</div>
         <div class="jr-tuiles" id="jrRoles">
         <button class="jr-opt on" type="button" data-role="client" onclick="jrChoisir('role','client')">La personne qui réclame</button>
         <button class="jr-opt" type="button" data-role="conseiller" onclick="jrChoisir('role','conseiller')">Le service à la clientèle</button>
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
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()">Commencer l'appel</button>
     </div>
     <div class="jr-rappel">
       <div class="jr-rappel-t">Réutilisez ce que vous venez d'apprendre</div>
       <div class="jr-rappel-g">
         <div><div class="jr-rappel-l">Demandez poliment</div><div class="jr-rappel-x"><b>Pourriez-vous</b> me confirmer le montant total de la première année ?</div></div>
         <div><div class="jr-rappel-l">Reformulez pour faire confirmer</div><div class="jr-rappel-x"><b>Autrement dit</b>, je m'engage pour douze mois. C'est bien ça ?</div></div>
         <div><div class="jr-rappel-l">Accordez, puis maintenez</div><div class="jr-rappel-x"><b>Bien que</b> le tarif hebdomadaire <b>soit</b> exact, l'annonce ne mentionnait pas les frais.</div></div>
         <div><div class="jr-rappel-l">Limitez</div><div class="jr-rappel-x">L'annonce <b>ne</b> donnait <b>que</b> le prix par semaine.</div></div>
         <div><div class="jr-rappel-l">Dites le degré</div><div class="jr-rappel-x">La condition était écrite <b>trop</b> petit <b>pour que</b> je la <b>voie</b>.</div></div>
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
     <h3 class="prod-tit">Démontez une publicité devant la classe</h3>
     <p class="prod-lead">Deux minutes environ, debout, sans lire vos notes mot à mot. Choisissez une publicité que vous avez vue ou entendue cette semaine — à la radio, dans une circulaire, dans un abribus, dans une vidéo. Dites ce qu'elle montre, ce qu'elle promet sans le dire, ce qu'elle ne dit pas du tout, et nommez le procédé.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Ce que l'annonce montre, en deux phrases</div><div class="plan-ex">« J'ai entendu une annonce de matelas à la radio, jeudi matin. Elle dure trente secondes et finit par un slogan. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Ce qu'elle promet sans le dire, et ce qu'elle tait</div><div class="plan-ex">« Elle dit “jusqu'à quarante pour cent”. Autrement dit, un seul matelas peut suffire. Et elle ne donne jamais le prix de départ. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Le procédé, nommé, et ce que vous en concluez</div><div class="plan-ex">« Ce qui travaille ici, c'est le comparatif sans deuxième terme. Bien que rien ne soit faux, l'impression générale ne correspond pas à ce qu'on paie. »</div></div>
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
     <h3 class="prod-tit">Écrivez votre lettre de réclamation</h3>
     <p class="prod-lead">De 10 à 14 phrases, en trois paragraphes. Le premier expose les faits et les dates. Le deuxième dit précisément ce que l'annonce laissait croire et ce qu'elle ne disait pas. Le troisième formule votre demande et le délai que vous accordez. Le ton reste ferme et courtois du début à la fin : une lettre en colère se répond en une ligne.</p>
     <div class="req">
       <div class="req-hd">Votre lettre doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>La date de la signature et le montant réellement prélevé</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>La phrase exacte de l'annonce, entre guillemets</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une concession : « bien que… soit… » ou « même si… est… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une restriction : « l'annonce ne donnait que… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Deux conditionnels de politesse : je souhaiterais, pourriez-vous</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un connecteur de reformulation : autrement dit, en somme</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une demande précise : ce que vous voulez, exactement</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un délai de réponse, à la fin</span></div>
       </div>
       <div class="req-note">N'écrivez rien que vous ne puissiez prouver : le dépliant, le contrat et la date de l'annonce sont vos pièces. Et gardez une copie de votre lettre.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">Élan Cardio — service à la clientèle, rue Parent</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Demande d'annulation et de remboursement — abonnement signé le 2 février</span></div>
       <textarea id="peText" rows="12" aria-label="Votre lettre" data-min="10" data-max="14" oninput="peCount()" placeholder="Madame, Monsieur,&#10;&#10;J'ai signé un abonnement dans votre établissement le…"></textarea>
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
    "Je nomme les pièces d'une annonce : le slogan, la mention légale, l'astérisque, le public cible.",
    "Je distingue ce qu'une annonce affirme de ce qu'elle laisse seulement conclure.",
    "Je sais qu'au Québec une annonce se juge sur l'impression générale qu'elle donne.",
    "J'entends le « e » que le débit rapide fait disparaître, et je reconnais le mot quand même.",
    "J'écoute la fin d'une capsule, là où se trouve la mention légale.",
    "Je reconnais le conditionnel qui promet sans promettre.",
    "Je repère un comparatif qui n'a pas de deuxième terme.",
    "Je comprends « ne… que », et je ne le prends pas pour une négation.",
    "Je lis un dépliant en commençant par la plus petite ligne du bas.",
    "Je repère une phrase passive et je me demande qui a été effacé.",
    "J'emploie « bien que » avec le subjonctif et « même si » avec l'indicatif.",
    "Je reformule une condition écrite en français ordinaire : autrement dit…",
    "Je calcule le vrai total d'une première année, frais d'adhésion compris.",
    "Je sais qu'une publicité doit se présenter comme une publicité.",
    "Je sais que la publicité destinée aux moins de treize ans est interdite au Québec.",
    "Je sais à qui m'adresser : le prix, la forme du message, ou la langue de l'affichage.",
    "Je peux démonter une publicité à voix haute devant la classe.",
    "Je peux écrire une lettre de réclamation en trois paragraphes.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#0D7A6F">Je retiens des mots</span><span class="ctit" style="color:#0D7A6F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#0D7A6F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#0D7A6F;font-size:13px;margin:6px 0 4px">Les pièces d'une annonce</div>
     <textarea rows="2" placeholder="Ex. : un message implicite, un slogan, un public cible, un annonceur, un abribus, un panneau-réclame…"></textarea>
     <div style="font-weight:800;color:#0D7A6F;font-size:13px;margin:12px 0 4px">Ce qu'on entend</div>
     <textarea rows="2" placeholder="Ex. : une capsule publicitaire, une mention légale, le débit, un rabais, jusqu'à, pourrait…"></textarea>
     <div style="font-weight:800;color:#0D7A6F;font-size:13px;margin:12px 0 4px">Ce qu'on lit</div>
     <textarea rows="2" placeholder="Ex. : une circulaire, un dépliant, un astérisque, des frais d'adhésion, un engagement, le prix tout inclus…"></textarea>
     <div style="font-weight:800;color:#0D7A6F;font-size:13px;margin:12px 0 4px">Les règles et les portes</div>
     <textarea rows="2" placeholder="Ex. : un témoignage, une publicité déguisée, une commandite, l'affichage, l'impression générale…"></textarea>
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
