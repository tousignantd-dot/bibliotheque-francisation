  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une visite guidée à
  // voix haute, un courriel de notes. Le jeu de rôle vient en premier parce
  // qu'il sert de répétition avant les deux autres.
  // Le scénario `louer` existe déjà dans server.py depuis le module de
  // niveau 4 : seule l'annonce est côté client, et c'est voulu — c'est le
  // seul document que les deux personnes ont sous les yeux. Ce que chaque
  // rôle ignore de l'autre reste sur le serveur.
  const ROLE_CAS = [
    {id:'A', titre:"Le 2 ½ du centre-ville", txt:"<b>2 ½ meublé</b>, troisième étage, rue Wellington Nord. Fenêtres neuves, arrêt d'autobus devant la porte. Libre le 1<sup>er</sup> octobre. <b>690 $ par mois.</b>"},
    {id:'B', titre:"Le 5 ½ de Fleurimont", txt:"<b>Grand 5 ½</b> dans un quartier familial, à dix minutes du CHUS. Trois chambres, sous-sol fini, grande cour arrière, deux stationnements. Libre le 1<sup>er</sup> juillet. <b>1 390 $ par mois.</b>"},
    {id:'C', titre:"Le 4 ½ du Vieux-Nord", txt:"<b>4 ½ au rez-de-chaussée</b> d'une maison centenaire. Planchers de bois, grandes fenêtres, balcon avant. Près du lac des Nations. Non-fumeur. Libre le 1<sup>er</sup> août. <b>1 050 $ par mois.</b>"},
  ];
  const ROLE_SUJETS = ["Ce qui est inclus dans le loyer","Le chauffage et l'électricité",
    "Les électroménagers et la buanderie","Le stationnement","Les animaux",
    "Le bruit et le voisinage","La date et la durée du bail"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">La visite du logement</span></div>
     <p class="lead">Vous avez tous les deux l'annonce sous les yeux — rien de plus. L'assistant joue l'autre personne et ne donne jamais un renseignement avant qu'on le lui demande. Essayez les deux rôles : au niveau 5, il faut savoir <b>demander</b> et savoir <b>donner</b>.</p>
     <p class="lead">Choisissez votre logement et votre rôle</p>
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
         <button class="jr-opt on" type="button" data-role="locataire" onclick="jrChoisir('role','locataire')">La personne qui visite</button>
         <button class="jr-opt" type="button" data-role="proprietaire" onclick="jrChoisir('role','proprietaire')">Le ou la propriétaire</button>
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
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()">Commencer la visite</button>
     </div>
     <div class="jr-rappel">
       <div class="jr-rappel-t">Réutilisez ce que vous venez d'apprendre</div>
       <div class="jr-rappel-g">
         <div><div class="jr-rappel-l">Posez une question précise</div><div class="jr-rappel-x">Est-ce que le chauffage <b>est inclus</b> dans le loyer ?</div></div>
         <div><div class="jr-rappel-l">Décrivez avec un relatif</div><div class="jr-rappel-x">C'est la chambre <b>qui</b> donne sur la cour.</div></div>
         <div><div class="jr-rappel-l">Dites la manière avec un gérondif</div><div class="jr-rappel-x">On voit la ruelle <b>en arrivant</b> par en arrière.</div></div>
         <div><div class="jr-rappel-l">Annoncez ce qui suivra</div><div class="jr-rappel-x">Le bail <b>se terminera</b> le 30 juin.</div></div>
         <div><div class="jr-rappel-l">Vérifiez avant de raccrocher</div><div class="jr-rappel-x">Donc 1 050 $, chauffage non inclus. <b>C'est bien ça ?</b></div></div>
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
     <h3 class="prod-tit">Faites visiter un logement</h3>
     <p class="prod-lead">Vous faites visiter le logement où vous habitez, ou celui que vous aimeriez louer. Décrivez les pièces, dites ce qui est inclus, et donnez les renseignements avant qu'on ait à les demander deux fois.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Accueillir et situer</div><div class="plan-ex">« Entrez. C'est un quatre et demie au deuxième étage, avec deux vraies chambres. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Décrire les pièces</div><div class="plan-ex">« Le salon est ensoleillé jusqu'à quatre heures, et c'est la pièce qui donne sur la cour. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Dire ce qui est inclus — et ce qui ne l'est pas</div><div class="plan-ex">« Le chauffage n'est pas inclus : comptez environ cent dollars par mois l'hiver. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 4</div><div class="plan-t">Annoncer les conditions du bail</div><div class="plan-ex">« Le bail se terminera le 30 juin, et il se renouvellera aux mêmes conditions. »</div></div>
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
     <h3 class="prod-tit">Le courriel de notes après un appel</h3>
     <p class="prod-lead">Vous venez de téléphoner au sujet d'un logement. Écrivez à la personne qui déménagera avec vous pour lui rapporter ce que vous avez appris. De 6 à 10 phrases.</p>
     <div class="req">
       <div class="req-hd">Votre courriel doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le loyer et la date d'occupation</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce qui est inclus et ce qui ne l'est pas</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Deux phrases rapportées : « Elle me dit que… », « Je lui ai demandé si… »</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Ce qui reste à vérifier pendant la visite</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>La date et l'heure du rendez-vous</span></div>
       </div>
       <div class="req-note">Rapportez, ne recopiez pas : <em>« Elle me dit que le chauffage n'est pas inclus »</em>, et non <em>« Le chauffage n'est pas inclus. »</em></div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">À</span><span class="mail-v">la personne qui déménagera avec vous</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Le logement de la rue Bowen — mes notes d'appel</span></div>
       <textarea id="peText" rows="9" aria-label="Votre courriel" data-min="6" data-max="10" oninput="peCount()" placeholder="Bonjour,&#10;&#10;J'ai appelé pour le quatre et demie. Elle me dit que le logement est libre le premier juillet…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 6 à 10</span>
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
    "Je peux lire une annonce de logement et comprendre ses abréviations.",
    "Je comprends un avis de modification du bail et je sais que j'ai un mois pour répondre.",
    "Je peux téléphoner pour un logement et poser huit questions précises.",
    "Je prends des notes pendant un appel, avec les chiffres et les dates.",
    "Je peux rapporter ce qu'on m'a dit : « Elle me dit que… », « Je lui demande si… ».",
    "Je comprends les renseignements qu'on me donne pendant une visite.",
    "Je peux décrire un logement avec « qui », « que » et « où ».",
    "Je peux faire visiter un logement et donner les renseignements sans qu'on me les demande deux fois.",
    "Je peux lire un bail, son annexe et sa section G.",
    "Je sais ce que je peux faire si je veux sous-louer ou céder mon bail.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Notez ici les mots et les expressions à retenir. Vous pouvez aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Le logement et l'annonce</div>
     <textarea rows="2" placeholder="Ex. : un 4 ½, chauffé et éclairé, libre imm., le loyer, la date d'occupation…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Au téléphone</div>
     <textarea rows="2" placeholder="Ex. : je vous appelle pour l'annonce, vous pouvez répéter ?, c'est noté, je prends des notes…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Pendant la visite</div>
     <textarea rows="2" placeholder="Ex. : ensoleillé, insonorisé, le bois franc, la remise, la buanderie, une case de stationnement…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Le bail et mes droits</div>
     <textarea rows="2" placeholder="Ex. : l'annexe, la section G, le renouvellement, sous-louer, céder son bail, le Tribunal…"></textarea>
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
