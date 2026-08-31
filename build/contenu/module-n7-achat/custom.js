  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : la réclamation avec l'assistant, la description du
  // problème de fonctionnement, puis la mise en demeure. Le jeu de rôle vient
  // en premier parce qu'il sert de répétition aux deux autres.
  //
  // D'où viennent ces trois tâches. Les trois intentions de la situation
  // « Achat de biens de consommation durables », au niveau 7, les portent
  // toutes les trois directement, sans détour par les attentes de fin de
  // cours : « faire une réclamation » (CO/PO), « comprendre des
  // renseignements et décrire un problème portant sur le fonctionnement d'un
  // électroménager ou d'un véhicule » (CO/PO), « rédiger une lettre de
  // réclamation » (PE). C'est le cas le plus simple, et il vaut la peine
  // d'être noté : plusieurs situations du niveau 7 n'ont aucune intention de
  // production écrite et doivent aller la chercher ailleurs.
  //
  // Seule la situation publique est ici ; ce que sait le commerçant joué par
  // l'assistant vit dans server.py, scénario « reclamation ».
  const ROLE_CAS = [
    {id:'transmission', titre:'La transmission qui cogne', txt:"Vous avez acheté une <b>berline 2019</b> le <b>6 avril</b>, 11 400 $, chez le commerçant à qui vous parlez. Le <b>24 avril</b>, un cognement est apparu au passage des rapports ; le <b>30 avril</b>, le garage a écrit « fuite au carter de transmission ». Vingt-quatre jours, <b>900 km</b>. L'étiquette dit <b>catégorie C</b>."},
    {id:'garantie', titre:"La garantie qu'on ne vous a pas expliquée", txt:"On vous a vendu une <b>garantie prolongée de 1 200 $</b> financée avec le reste. Personne ne vous a parlé de la <b>garantie légale</b>, ni en paroles ni par écrit, et vous avez posé la question <b>deux fois</b> ce jour-là. Vous voulez que ce soit reconnu — et vous n'êtes pas sûr de vouloir garder cette garantie-là."},
    {id:'laveuse', titre:"La laveuse de quatorze mois", txt:"Ce n'est pas une auto : une <b>laveuse de 1 150 $</b>, achetée il y a <b>quatorze mois</b>, qui ne vidange plus. La garantie du fabricant est de douze mois et elle est expirée. Le commerçant vous l'a dit tout de suite. Il ne vous a pas dit un mot de la <b>durée raisonnable</b>."},
  ];
  const ROLE_SUJETS = ["Dire d'entrée la date d'achat, le bien et le montant",
    "Décrire le problème : le bruit ou le symptôme, le moment, la fréquence",
    "Citer le diagnostic écrit plutôt que votre impression",
    "Nommer la garantie que vous invoquez, et démontrer que vous étiez dedans",
    "Mettre en relief ce qui compte : ce que je demande, c'est…",
    "Demander au conditionnel : accepteriez-vous, pourriez-vous",
    "Refuser poliment « c'est de l'usure normale » en redonnant un chiffre",
    "Annoncer un délai, et ce que vous ferez ensuite — sans menacer"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Réclamez auprès du commerçant</span></div>
     <p class="lead">L'assistant joue <b>la personne au comptoir du service à la clientèle</b>. Elle n'est pas votre ennemie : elle applique ce qu'on lui a appris, et « c'est de l'usure normale » est la première phrase qu'elle a apprise. Elle cède devant un fait daté, jamais devant un ton. À vous de donner les dates, les chiffres et le nom de la garantie. Vouvoyez-la du début à la fin.</p>
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
         <button class="jr-opt on" type="button" data-role="ernestine" onclick="jrChoisir('role','ernestine')">Le client qui réclame</button>
         <button class="jr-opt" type="button" data-role="commercant" onclick="jrChoisir('role','commercant')">La personne au comptoir</button>
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
         <div class="jr-bande-t">Les huit sujets à couvrir</div>
         <p class="jr-bande-p">${ROLE_SUJETS.map((s,i)=>i?s.charAt(0).toLowerCase()+s.slice(1):s).join(', ')}.</p>
       </div>
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()">Commencer la discussion</button>
     </div>
     <div class="jr-rappel">
       <div class="jr-rappel-t">Réutilisez ce que vous venez d'apprendre</div>
       <div class="jr-rappel-g">
         <div><div class="jr-rappel-l">Décrivez avec les trois coordonnées</div><div class="jr-rappel-x">Un <b>cognement</b>, <b>à froid</b>, <b>systématiquement</b> au passage des rapports.</div></div>
         <div><div class="jr-rappel-l">Rangez les deux passés dans l'ordre</div><div class="jr-rappel-x">Quand j'ai vu la flaque, le bruit <b>avait</b> déjà <b>commencé</b>.</div></div>
         <div><div class="jr-rappel-l">Mettez en avant ce qui compte</div><div class="jr-rappel-x"><b>Ce que</b> je demande, <b>c'est</b> la réparation. · <b>C'est</b> la garantie légale <b>qui</b> s'applique.</div></div>
         <div><div class="jr-rappel-l">Demandez au conditionnel</div><div class="jr-rappel-x"><b>Accepteriez-vous</b> de faire réparer sans frais ? · Me <b>passeriez</b>-vous une autre voiture en attendant ?</div></div>
         <div><div class="jr-rappel-l">Annoncez la suite au futur, jamais en menace</div><div class="jr-rappel-x">Sans réponse d'ici vendredi, je vous <b>écrirai</b>.</div></div>
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
     <h3 class="prod-tit">Décrivez le problème, puis réclamez</h3>
     <p class="prod-lead">Vous vous présentez au comptoir. Parlez environ 90 secondes : annoncez d'abord de quoi il s'agit avec la date et le montant, décrivez ensuite le problème de fonctionnement en donnant le bruit, le moment et la fréquence, puis dites quelle garantie vous invoquez et ce que vous demandez.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Le dossier, en deux phrases</div><div class="plan-ex">« J'ai acheté chez vous une berline 2019 le 6 avril, au prix de 11 400 $. Je viens pour un problème de transmission apparu le 24 avril. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Le problème, en trois coordonnées</div><div class="plan-ex">« C'est un cognement, sous le plancher à droite. Il revient à froid, seulement le matin, et systématiquement au passage des rapports. Le 30 avril, le garage a établi une fuite au carter. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">La garantie invoquée, puis la demande</div><div class="plan-ex">« L'étiquette dit catégorie C : la garantie de bon fonctionnement courait jusqu'au 6 mai ou 1 700 kilomètres, et j'en avais fait 900. Ce que je demande, c'est la réparation, pièces et main-d'œuvre. Accepteriez-vous de me rappeler d'ici vendredi ? »</div></div>
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
     <h3 class="prod-tit">Écrivez votre mise en demeure</h3>
     <p class="prod-lead">Le vendredi est passé sans appel. Écrivez au commerçant un texte de 12 à 16 phrases, en <b>cinq paragraphes courts</b> : les faits de l'achat, la chronologie de la panne, la garantie que vous invoquez, votre demande, le délai et la suite. Un objet qui se comprend sans ouvrir le message.</p>
     <div class="req">
       <div class="req-hd">Votre lettre doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un objet court, sans phrase complète, avec le numéro du dossier</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>La date d'achat, le bien, le prix payé</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>La chronologie de la panne, une date par phrase</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le nom de la garantie invoquée, et la preuve que vous étiez dedans</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une seule demande, précise, avec « à vos frais »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un délai de dix jours et son point de départ</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Deux connecteurs en tête de paragraphe : en outre, en conséquence</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Un subjonctif après « je demande que » ou « il faut que »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>La liste des pièces jointes, sans commentaire</span></div>
       </div>
       <div class="req-note">N'écrivez pas ce que vous ressentez : écrivez ce qui s'est passé, à quelle date, et ce que vous demandez. Une mise en demeure qui donne des dates, un montant et un délai obtient une réparation ; une lettre qui accuse obtient une lettre en retour.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">service.clientele@autos-bulstrode.example</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">À vous de le trouver — court, et sans phrase complète</span></div>
       <textarea id="peText" rows="10" aria-label="Votre lettre" data-min="12" data-max="16" oninput="peCount()" placeholder="Madame, Monsieur,&#10;&#10;Le 6 avril, j'ai acheté chez vous une berline de l'année 2019, au prix de 11 400 $…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 12 à 16</span>
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
    "Je lis l'étiquette d'une auto d'occasion avant de lire le contrat.",
    "Je sais ce que la case « catégorie » de l'étiquette m'annonce.",
    "Je repère dans un contrat de crédit le taux, les frais et l'obligation totale.",
    "Je retrouve le verbe caché sous un nom en -tion ou en -ment.",
    "Je décris une panne avec un bruit, un moment et une fréquence.",
    "J'emploie systématiquement, par intermittence, seulement, à peine.",
    "Je range deux faits passés dans l'ordre avec le plus-que-parfait.",
    "Je distingue la garantie légale, celle de bon fonctionnement et la prolongée.",
    "Je sais qu'un commerçant doit m'informer de la garantie légale avant de m'en vendre une.",
    "Je réponds à « c'est de l'usure normale » par une date et un kilométrage.",
    "Je mets en relief ce qui compte : ce que je demande, c'est…",
    "Je demande au conditionnel : accepteriez-vous, pourriez-vous, j'aimerais.",
    "Je connais les six parties d'une mise en demeure et leur ordre.",
    "J'articule mes paragraphes avec en outre, or, en conséquence, à compter de.",
    "J'emploie le subjonctif après je demande que, j'exige que, il faut que.",
    "Je sais qu'aux petites créances on réclame soi-même jusqu'à 15 000 $.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Les mots du contrat</div>
     <textarea rows="2" placeholder="Ex. : une auto d'occasion, l'odomètre, les frais de crédit, l'obligation totale, le taux de crédit…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les mots de la panne</div>
     <textarea rows="2" placeholder="Ex. : la transmission, un cognement, une fuite, un témoin lumineux, un diagnostic…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les mots de la garantie</div>
     <textarea rows="2" placeholder="Ex. : la garantie légale, la garantie de bon fonctionnement, une garantie prolongée, une exclusion, l'usure normale…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les mots de la lettre</div>
     <textarea rows="2" placeholder="Ex. : une mise en demeure, un délai raisonnable, une pièce justificative, la Division des petites créances…"></textarea>
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
