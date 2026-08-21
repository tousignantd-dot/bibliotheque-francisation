  // ── JE ME LANCE ──────────────────────────────────────────
  // Trois productions : un jeu de rôle avec l'assistant, une prise orale
  // corrigée, un court message écrit. Le jeu de rôle vient en premier
  // parce qu'il sert de répétition avant les deux autres.
  // Seule la situation publique est côté client ; ce que sait Roland,
  // joué par l'assistant, vit dans server.py, scénario « meteo ».
  const ROLE_CAS = [
    {id:'matin', titre:"Dans l'entrée de l'immeuble", txt:"Tu pars au cours. Ton voisin <b>rentre de dehors</b>, le manteau couvert de neige. Tu ne sais pas quel temps il fait."},
    {id:'bulletin', titre:"Je n'ai pas tout compris à la radio", txt:"Tu as entendu le <b>bulletin météo</b> de sept heures, mais trop vite. Ton voisin, lui, l'a écouté au complet."},
    {id:'tempete', titre:"Est-ce qu'il y a de l'école ?", txt:"Il tombe <b>trente centimètres de neige</b>. Tu veux savoir si ton cours a lieu aujourd'hui."},
  ];
  const ROLE_SUJETS = ["Saluer, puis demander le temps qu'il fait",
    "Demander la température, en degrés",
    "Répéter le nombre de degrés pour vérifier",
    "Demander le temps de demain",
    "Dire ce que tu mets pour sortir",
    "Demander de répéter quand ça va trop vite",
    "Remercier et souhaiter une bonne journée"];

  document.getElementById('exs-appli').innerHTML += `
   <div class="card custom" id="jeu-de-role">
     <div class="c-hdr"><span class="tag" style="background:#7E3F98">Jeu de rôle</span><span class="ctit" style="color:#7E3F98">Parle de la météo avec ton voisin</span></div>
     <p class="lead">L'assistant joue <b>Roland Pelchat, ton voisin retraité</b>. Il sort marcher tous les matins et il sait toujours quel temps il fait. Il répond en deux ou trois mots : à toi de poser les questions, une à la fois.</p>
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
       Demande le temps :
       <span class='savoir-ex'><b>Quel temps fait-il</b> aujourd'hui ? · <b>Est-ce qu'</b>il neige ?</span>
       Demande la température :
       <span class='savoir-ex'>Il fait <b>combien</b> de degrés ?</span>
       Vérifie le nombre :
       <span class='savoir-ex'><b>Moins douze</b> ? D'accord, merci.</span>
       Dis ce que tu mets :
       <span class='savoir-ex'><b>Je mets</b> ma tuque et mes mitaines.</span>
     </div>

     <div class="jr-sep"></div>
     <div class="jr-sub">Choisis ta situation et ton rôle</div>
     <div class="jr-choix">
       <div class="jr-choix-l">Quelle situation ?</div>
       <div class="jr-opts" id="jrLogs">
         ${ROLE_CAS.map((c,i)=>`<button class="jr-opt${i===0?' on':''}" type="button" data-log="${c.id}" onclick="jrChoisir('log','${c.id}')">${esc(c.titre)}</button>`).join('')}
       </div>
       <div class="jr-choix-l">Tu joues qui ?</div>
       <div class="jr-opts" id="jrRoles">
         <button class="jr-opt on" type="button" data-role="moi" onclick="jrChoisir('role','moi')">Moi, l'élève</button>
         <button class="jr-opt" type="button" data-role="voisin" onclick="jrChoisir('role','voisin')">Le voisin qui rentre de dehors</button>
       </div>
       <div class="jr-choix-l">Comment ?</div>
       <div class="jr-opts" id="jrModes">
         <button class="jr-opt on" type="button" data-mode="texte" onclick="jrModeVoix(false)">✍️ Écrire</button>
         <button class="jr-opt" type="button" data-mode="voix" onclick="jrModeVoix(true)">🎤 Parler</button>
       </div>
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()" style="margin-top:14px">Commencer la conversation</button>
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
     <div class="prod-eyebrow"><span class="prod-num">1</span><span class="prod-kind">Production orale</span></div>
     <h3 class="prod-tit">Dis le temps qu'il fait ce matin</h3>
     <p class="prod-lead">Tu sors de chez toi et tu croises un voisin. Dis le temps qu'il fait, donne la température en degrés, et dis ce que tu mets pour sortir. Vouvoie la personne du début à la fin.</p>
     <div class="plan">
       <div class="plan-step"><div class="plan-no">TEMPS 1</div><div class="plan-t">Le temps qu'il fait</div><div class="plan-ex">« Bonjour ! Aujourd'hui, il neige et il vente. »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 2</div><div class="plan-t">La température</div><div class="plan-ex">« Il fait moins douze degrés. C'est froid ! »</div></div>
       <div class="plan-step"><div class="plan-no">TEMPS 3</div><div class="plan-t">Ce que tu mets</div><div class="plan-ex">« Je mets mon manteau, ma tuque et mes mitaines. »</div></div>
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
           <div class="rec-hint">Parle environ 30 secondes. Tu pourras recommencer autant de fois que tu veux.</div>
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
     <h3 class="prod-tit">Écris la météo à quelqu'un de ta famille</h3>
     <p class="prod-lead">Quelqu'un de ta famille habite dans un pays chaud et ne connaît pas l'hiver. Écris-lui un court message : dis le temps qu'il fait, la température, et ce que tu mets pour sortir. De 3 à 5 phrases.</p>
     <div class="req">
       <div class="req-hd">Ton message doit contenir</div>
       <div class="req-grid">
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>« Bonjour », au début</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Le temps qu'il fait : <em>il neige, il pleut, il vente, il fait beau</em></span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>La température, avec <em>moins</em> ou <em>plus</em> devant</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>Deux vêtements que tu mets pour sortir</span></div>
         <div class="req-it"><span class="req-box" aria-hidden="true"></span><span>La saison, et « à bientôt » à la fin</span></div>
       </div>
       <div class="req-note">Attention au petit mot devant la saison : on écrit <em>en hiver</em>, mais <em>au printemps</em>. Et la météo prend toujours <em>il</em> : <em>il neige</em>, jamais « la neige neige ».</div>
     </div>
     <div class="mail">
       <div class="mail-row"><span class="mail-k">Pour</span><span class="mail-v">Quelqu'un de ma famille</span></div>
       <div class="mail-row"><span class="mail-k">Objet</span><span class="mail-v">Le temps qu'il fait ici</span></div>
       <textarea id="peText" rows="7" aria-label="Ton message" data-min="3" data-max="5" oninput="peCount()" placeholder="Bonjour,&#10;Ici, il neige. Il fait…"></textarea>
       <div class="mail-foot">
         <span class="mail-count" id="peCountLbl">0 phrase sur 3 à 5</span>
         <button class="btn-prod" id="peBtn" type="button" onclick="peCheck()">Vérifier mon message</button>
       </div>
     </div>
     <div class="fb" id="peFb" aria-live="polite"></div>
     <div class="status" id="peStatus">Analyse en cours…</div>
     <div class="err" id="peErr"></div>
   </div>`;
  const rb=document.getElementById('recBtn'); if(rb) rb.addEventListener('click',toggleRec);

  // JE RETIENS DES MOTS — notes + cartes mémoire + autoévaluation
  const SELF=[
    "Je peux nommer le temps qu'il fait : il neige, il pleut, il vente.",
    "Je peux dire « il fait froid » et « il fait beau ».",
    "Je peux lire une température avec « moins » ou « plus » devant.",
    "Je peux trouver la ville, le temps et la température dans un bulletin météo.",
    "Je peux écrire ces trois renseignements en trois mots.",
    "Je peux dire les quatre saisons avec le bon petit mot devant.",
    "Je peux dire ce que je mets pour sortir quand il fait moins vingt.",
    "Je peux demander « pouvez-vous répéter ? » quand ça va trop vite.",
  ];
  document.getElementById('exs-retiens').innerHTML = `
   <div class="card custom">
     <div class="c-hdr"><span class="tag" style="background:#A5335F">Je retiens des mots</span><span class="ctit" style="color:#A5335F">Mes mots utiles</span></div>
     <p class="lead">Note ici les mots et les expressions à retenir. Tu peux aussi <span style="font-weight:900;cursor:pointer;text-decoration:underline dotted;color:#A5335F" onclick="fcOpen(0)">réviser les cartes mémoire 🃏</span>.</p>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:6px 0 4px">Le temps qu'il fait</div>
     <textarea rows="2" placeholder="Ex. : la neige, la pluie, le vent, le soleil, un nuage, il neige, il pleut, il vente, il fait beau…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">La température et le bulletin</div>
     <textarea rows="2" placeholder="Ex. : la température, un degré, moins huit, zéro degré, un bulletin météo, une ville…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les saisons</div>
     <textarea rows="2" placeholder="Ex. : une saison, en hiver, au printemps, en été, en automne, en janvier…"></textarea>
     <div style="font-weight:800;color:#A5335F;font-size:13px;margin:12px 0 4px">Les vêtements de l'hiver</div>
     <textarea rows="2" placeholder="Ex. : un manteau, une tuque, des mitaines, des bottes, un foulard, une tempête…"></textarea>
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
