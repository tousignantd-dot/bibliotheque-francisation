  // ── JE METS EN APPLICATION ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, un courriel corrigé. Le jeu de rôle vient en premier parce
  // qu'il sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait le personnage
  // joué par l'assistant vit dans server.py.
  const ROLE_CAS = [
    {id:'chauffage', titre:'Le chauffage', txt:"Le <b>calorifère du salon</b> ne chauffe plus. Il fait <b>14 °C</b> et le disjoncteur retombe chaque fois qu'on le remonte. On est au début de novembre."},
    {id:'moisissure', titre:'La moisissure', txt:"De la <b>moisissure noire</b> revient dans le coin de la salle de bain malgré les nettoyages. Le miroir reste embué longtemps et il n'y a <b>pas de ventilateur</b>."},
    {id:'bruit', titre:'Le bruit', txt:"Les voisins du dessous reçoivent des amis <b>tous les vendredis</b>. La musique dure jusqu'à <b>deux heures du matin</b>. Ça dure depuis cinq semaines."},
  ];
  const ROLE_SUJETS = ["Quel est le problème exactement","Depuis quand il dure",
    "La conséquence sur ta vie","Ce que tu as déjà essayé",
    "Qui fait faire la réparation","La date de l'intervention","Ce qui se passe en attendant"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#0F766E">Jeu de rôle</span><span class="ctit" style="color:#0F766E">Explique ton problème à ta propriétaire</span></div>
     <p class="lead">L'assistant joue <b>l'autre personne</b> au téléphone. Il ne connaît pas ta situation et il ne te donnera rien avant que tu l'expliques bien — comme dans un vrai appel. Ton but : obtenir <b>une date</b> et savoir <b>ce qui se passe en attendant</b>.</p>
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
       <div class="jr-gram-t">Réutilise ce que tu viens d'apprendre</div>
       Dis depuis quand :
       <span class='savoir-ex'>Le calorifère ne chauffe plus <b>depuis</b> avant-hier.</span>
       <span class='savoir-ex'><b>Ça fait</b> deux semaines <b>que</b> la tache grossit.</span>
       Demande une réparation :
       <span class='savoir-ex'>Pourriez-vous <b>faire venir</b> un électricien cette semaine ?</span>
     </div>

     <div class="jr-sep"></div>
     <div class="jr-sub">Choisis ta situation et ton rôle</div>
     <div class="jr-choix">
       <div class="jr-choix-l">Quel problème ?</div>
       <div class="jr-opts" id="jrLogs">
         ${ROLE_CAS.map((c,i)=>`<button class="jr-opt${i===0?' on':''}" type="button" data-log="${c.id}" onclick="jrChoisir('log','${c.id}')">${esc(c.titre)}</button>`).join('')}
       </div>
       <div class="jr-choix-l">Tu joues qui ?</div>
       <div class="jr-opts" id="jrRoles">
         <button class="jr-opt on" type="button" data-role="locataire" onclick="jrChoisir('role','locataire')">Le locataire — j'appelle</button>
         <button class="jr-opt" type="button" data-role="proprietaire" onclick="jrChoisir('role','proprietaire')">La propriétaire — je réponds</button>
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
     <div class="c-hdr"><span class="tag" style="background:#0D9488">Production orale</span><span class="ctit" style="color:#0D9488">Décris ton problème en trois temps</span></div>
     <p class="lead">Choisis un problème de logement — le tien ou un problème inventé — et <b>décris-le comme si tu parlais à ta propriétaire</b>. Suis les trois temps : <b>le fait</b>, <b>depuis quand et l'effet sur toi</b>, <b>ta demande</b>. Enregistre-toi, obtiens une rétroaction, puis envoie ta prise si tu le veux.</p>
     <div class="rec-zone"><button id="recBtn">🎤</button><div class="rec-lbl" id="recLbl">Touche pour t'enregistrer</div></div>
     <div id="poPrev" class="hidden" style="display:flex;flex-direction:column;gap:12px">
       <audio id="poAudio" controls style="width:100%"></audio>
       <textarea id="poText" rows="2" placeholder="Transcription automatique (tu peux la corriger)…"></textarea>
       <div style="display:flex;gap:10px;flex-wrap:wrap">
         <button class="btn btn-ghost" onclick="resetRec()">↺ Recommencer</button>
         <button class="btn btn-pri" id="poFbBtn" onclick="poGetFeedback()">💬 Obtenir une rétroaction</button>
       </div>
       <div class="fb" id="poFb" aria-live="polite"></div>
       <div id="poSend" style="display:none;gap:10px;flex-wrap:wrap;align-items:center">
         <button class="btn btn-send" id="poSendBtn" onclick="poSend()">📨 Envoyer à mon enseignant</button>
       </div>
     </div>
     <div class="status" id="poStatus">Analyse en cours…</div>
     <div class="err" id="poErr"></div>
   </div>

   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#0E7490">Production écrite</span><span class="ctit" style="color:#0E7490">Le courriel qui laisse une trace</span></div>
     <p class="lead">Tu as téléphoné à ta propriétaire, madame Rioux, mais rien n'a bougé depuis. <b>Écris-lui un courriel</b> pour garder une trace de ta demande. Ton message doit contenir : <b>le problème</b>, <b>depuis quand</b> il dure, <b>la conséquence</b> sur ta vie, et une <b>demande claire</b>. Emploie au moins une fois <em>faire</em> + infinitif. (5 à 8 phrases)</p>
     <textarea id="peText" rows="7" placeholder="Bonjour Madame Rioux,&#10;Je vous écris pour faire suite à notre conversation téléphonique du…"></textarea>
     <div style="margin-top:12px"><button class="btn btn-pri" id="peBtn" onclick="peCheck()">✍️ Vérifier mon message</button></div>
     <div class="fb" id="peFb" aria-live="polite"></div>
     <div class="status" id="peStatus">Analyse en cours…</div>
     <div class="err" id="peErr"></div>
   </div>`;
  const rb=document.getElementById('recBtn'); if(rb) rb.addEventListener('click',toggleRec);

  // JE RETIENS DES MOTS — notes + cartes mémoire + autoévaluation
  const SELF=[
    "Je peux nommer un problème dans mon logement (fuite, dégât, bris, moisissure, insalubrité).",
    "Je peux dire depuis quand un problème dure avec depuis, depuis que et ça fait… que.",
    "Je peux dire qui je veux faire venir avec faire + un verbe à l'infinitif.",
    "Je peux mettre deux actions en ordre avec avant de et après avoir.",
    "Je peux me plaindre poliment : dire le fait, l'effet sur moi, puis ma demande.",
    "Je sais à qui m'adresser et quoi faire si rien ne bouge.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#166534">Je retiens des mots</span><span class="ctit" style="color:#166534">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#166534" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#166534;font-size:13px;margin:6px 0 4px">Différents problèmes dans un logement ou un immeuble</div>
     <textarea rows="2" placeholder="Ex. : une fuite, un dégât d'eau, une infiltration, un bris, une invasion de fourmis…"></textarea>
     <div style="font-weight:800;color:#166534;font-size:13px;margin:12px 0 4px">Des adjectifs pour décrire un problème</div>
     <textarea rows="2" placeholder="Ex. : défectueux, brisé, bouché, humide, insalubre, dangereux, inacceptable…"></textarea>
     <div style="font-weight:800;color:#166534;font-size:13px;margin:12px 0 4px">Des professionnels à contacter</div>
     <textarea rows="2" placeholder="Ex. : un plombier, une électricienne, un couvreur, une exterminatrice, le concierge…"></textarea>
     <div style="font-weight:800;color:#166534;font-size:13px;margin:12px 0 4px">Pour dire depuis quand et pour se plaindre</div>
     <textarea rows="2" placeholder="Ex. : ça fait deux semaines que… · depuis que… · je ne peux plus tolérer… · pourriez-vous faire venir…"></textarea>
   </div>
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#166534">Autoévaluation</span><span class="ctit" style="color:#166534">Qu'est-ce que je suis capable de faire ?</span></div>
     <p class="lead">Pour chaque énoncé, choisis : pas encore 😟, un peu 🙂, ou oui 😃.</p>
     ${SELF.map((s,i)=>`<div class="selfrow"><div class="self-txt">${s}</div><div class="self-opts">
        <button onclick="rate(${i},this)">😟</button><button onclick="rate(${i},this)">🙂</button><button onclick="rate(${i},this)">😃</button>
     </div></div>`).join('')}
     <div style="margin-top:16px"><button class="btn btn-pri" onclick="finishEval()">Terminer le module 🎉</button></div>
     <div id="evalDone" class="fb" aria-live="polite"></div>
   </div>`;
}
