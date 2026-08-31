  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, une liste de linge d'hiver écrite. Le jeu de rôle vient en
  // premier parce qu'il sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait le personnage
  // joué par l'assistant vit dans server.py.
  const ROLE_CAS = [
    {id:'manteau', titre:"Le manteau d'hiver", txt:"C'est ton <b>premier hiver</b> ici. Tu cherches un manteau chaud, uni et foncé — et tu ne connais pas encore ta taille."},
    {id:'bottes', titre:"Les bottes en liquidation", txt:"Deux paires de <b>bottes</b> côte à côte. L'une est à 99 $, l'autre est en liquidation. Tu veux savoir laquelle coûte le moins cher."},
    {id:'chandail', titre:"Le chandail en rabais", txt:"Une affiche annonce <b>trente pour cent de rabais</b>. Tu veux savoir si le chandail que tu tiens est en rabais, et combien il coûtera à la caisse."},
  ];
  const ROLE_SUJETS = ["Saluer en entrant","Dire quel vêtement tu cherches",
    "Donner la couleur et le motif","Dire ou demander ta taille",
    "Demander à essayer, et où est la cabine","Comparer deux prix",
    "Remercier avant de partir"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Achète ton vêtement</span></div>
     <p class="lead">L'assistant joue <b>la conseillère du magasin</b>. Elle demande ta taille avant de te montrer quoi que ce soit : à toi de dire ce que tu cherches, et de comparer avant de choisir.</p>
     <p class="lead">Choisis ta situation et ton rôle</p>
     <div class="jr-annonces" id="jrLogs">
       ${ROLE_CAS.map((c,i)=>`<button class="jr-opt jr-tuile${i===0?' on':''}" type="button" data-log="${c.id}" onclick="jrChoisir('log','${c.id}')">
         <span class="jr-band"><span class="jr-band-off">Choix ${i+1}</span><span class="jr-band-on"><svg viewBox="0 0 20 20" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 10.5l4 4 8-9"></path></svg> Votre choix</span></span>
         <span class="jr-tuile-c"><span class="jr-tuile-t">${esc(c.titre)}</span><span class="jr-tuile-d">${c.txt}</span></span>
       </button>`).join('')}
     </div>
     <div class="jr-reglages">
       <div class="jr-carte">
         <div class="jr-champ-l">Tu joues qui ?</div>
         <div class="jr-tuiles" id="jrRoles">
         <button class="jr-opt on" type="button" data-role="client" onclick="jrChoisir('role','client')">Le client</button>
         <button class="jr-opt" type="button" data-role="conseiller" onclick="jrChoisir('role','conseiller')">La conseillère</button>
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
         <div><div class="jr-rappel-l">Nomme le vêtement, puis la couleur</div><div class="jr-rappel-x">Je cherche un <b>manteau noir</b>, uni.</div></div>
         <div><div class="jr-rappel-l">Donne ta taille</div><div class="jr-rappel-x">Je porte du <b>moyen</b>, je pense.</div></div>
         <div><div class="jr-rappel-l">Montre du doigt</div><div class="jr-rappel-x"><b>Celui-ci</b> est à combien ?</div></div>
         <div><div class="jr-rappel-l">Compare deux prix</div><div class="jr-rappel-x">Celui-là est <b>moins cher que</b> celui-ci.</div></div>
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
     <h3 class="prod-tit">Demande un vêtement et compare deux prix</h3>
     <p class="prod-lead">Choisis un vêtement dont tu as besoin cet hiver. Dis ce que tu cherches avec sa couleur, donne ta taille, puis compare le prix de deux articles à voix haute.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Dire ce que tu cherches</div><div class="plan-ex">« Bonjour, je cherche un manteau noir, uni. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">Donner ta taille et demander à essayer</div><div class="plan-ex">« Je porte du moyen. Je peux l'essayer ? »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Comparer deux prix et choisir</div><div class="plan-ex">« Celui-ci est moins cher que celui-là. Je prends celui-ci. »</div></div>
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
     <h3 class="prod-tit">Écris ta liste de linge d'hiver</h3>
     <p class="prod-lead">Écris la liste du linge dont tu as besoin cet hiver, pour toi ou pour ta famille. De 5 à 8 phrases.</p>
     <div class="req">
       <div class="req-hd">Ta liste doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Au moins cinq vêtements différents</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une couleur pour chacun</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une taille ou une pointure</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Une comparaison de prix : plus cher, moins cher</span></div>
       </div>
       <div class="req-note">Attention à la couleur : elle vient <em>après</em> le vêtement et elle s'accorde — <em>un manteau noir</em>, <em>une tuque noire</em>, <em>des bottes noires</em>.</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">Liste</span><span class="mail-v">Mon linge d'hiver</span></div>
       <div class="mail-row"><span class="mail-k">Budget</span><span class="mail-v">environ 250 $</span></div>
       <textarea id="peText" rows="7" aria-label="Ta liste" data-min="5" data-max="8" oninput="peCount()" placeholder="J'ai besoin d'un manteau noir, taille moyenne.&#10;Il me faut aussi des bottes brunes…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 5 à 8</span>
         <button class="btn-prod" id="peBtn" type="button" onclick="peCheck()">Vérifier ma liste</button>
       </div>
     </div>
     <div class="fb" id="peFb" aria-live="polite"></div>
     <div class="status" id="peStatus">Analyse en cours…</div>
     <div class="err" id="peErr"></div>
   </div>`;
  const rb=document.getElementById('recBtn'); if(rb) rb.addEventListener('click',toggleRec);

  // JE RETIENS DES MOTS — notes + cartes mémoire + autoévaluation
  const SELF=[
    "Je peux nommer les vêtements de l'hiver : manteau, tuque, chandail, bottes.",
    "Je peux dire une couleur et un motif : bleu foncé, uni, rayé.",
    "Je place la couleur après le vêtement et je l'accorde.",
    "Je peux dire ma taille, ou dire que je ne la connais pas encore.",
    "Je peux demander à essayer et trouver la cabine d'essayage.",
    "Je peux dire ce qui ne va pas : c'est trop serré, c'est trop long.",
    "Je peux comparer deux prix : plus cher que, moins cher que.",
    "Je comprends les dessins de l'étiquette d'entretien et je paie à la caisse.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Les vêtements</div>
     <textarea rows="2" placeholder="Ex. : un manteau, une tuque, un chandail, des bottes, des mitaines, un foulard…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les couleurs et les motifs</div>
     <textarea rows="2" placeholder="Ex. : pâle, foncé, uni, rayé, à pois, à carreaux, en laine, en coton…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">La taille et l'essayage</div>
     <textarea rows="2" placeholder="Ex. : petit, moyen, grand, la pointure, la cabine d'essayage, un cintre, trop serré…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Le prix et le paiement</div>
     <textarea rows="2" placeholder="Ex. : un rabais, la liquidation, le prix régulier, plus cher que, débit, comptant, la facture…"></textarea>
   </div>
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Autoévaluation</span><span class="ctit" style="color:#A5335F">Qu'est-ce que je suis capable de faire ?</span></div>
     <p class="lead">Pour chaque énoncé, choisis : pas encore 😟, un peu 🙂, ou oui 😃.</p>
     ${SELF.map((s,i)=>`<div class="selfrow"><div class="self-txt">${s}</div><div class="self-opts">
        <button onclick="rate(${i},this)">😟</button><button onclick="rate(${i},this)">🙂</button><button onclick="rate(${i},this)">😃</button>
     </div></div>`).join('')}
     <div style="margin-top:16px"><button class="btn btn-pri" onclick="finishEval()">Terminer le module 🎉</button></div>
     <div id="evalDone" class="fb" aria-live="polite"></div>
   </div>`;
}
