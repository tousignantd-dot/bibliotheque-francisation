const SECTIONS = [
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n6-habitation/icons/play.svg" alt="">', title:'Je découvre', color:'#A5335F',
   lead:"Savoir dans quel ordre un chantier se prépare — l'inspection, la soumission, la licence, le permis — et entendre trois groupes de lettres qui trompent l'oreille.",
   intro:"Doïna Petrescu a quarante-six ans. Elle est arrivée de Roumanie il y a cinq ans et elle est aide-cuisinière dans une résidence pour aînés, à Saint-Jérôme. Avec Marius, son conjoint, elle a acheté il y a deux ans une petite maison de 1961, rue des Mésanges. Sa mère, Aurica, arrive de Roumanie le 12 mai : ils veulent lui aménager le sous-sol. Doïna traverse la rue pour demander à son voisin Léandre par où on commence — et la réponse la surprend, parce que ça ne commence pas par les travaux.",
   dialogue:'prep', next:{id:'t1', tit:'Défi 1 · Le diagnostic', sub:"Suivre une explication technique jusqu'au bout et distinguer la cause du résultat."}},

  {id:'t1', no:'1', title:'Défi 1 · Le diagnostic', color:'#1D6B8F',
   lead:"Comprendre de l'information reliée à des travaux de réparation : ce qui a été trouvé, ce qui l'a causé, et ce qu'on va faire faire, dans l'ordre.",
   intro:"Défi 1 — Un homme de métier ne raconte pas : il diagnostique. Il commence par ce qu'il a vu, il remonte à ce qui s'était produit avant, puis il annonce ce qu'il va faire faire, et par qui. Trois mouvements, trois temps de verbe. Ce qui est difficile ici n'est pas le vocabulaire technique — Fernand Trudelle l'explique de lui-même. C'est de ne pas perdre à quoi renvoient « elle », « la », « en » quand ils reviennent trois répliques plus loin.",
   dialogue:'t1', next:{id:'t2', tit:'Défi 2 · Les papiers du chantier', sub:"Lire un rapport d'inspection et une soumission, et trouver ce qu'ils ne disent pas de la même façon."}},

  {id:'t2', no:'2', title:'Défi 2 · Les papiers du chantier', color:'#B45309',
   lead:"Lire deux écrits techniques : un rapport qui décrit ce qui est, une soumission qui décrit ce qui sera fait — et repérer la ligne des exclusions.",
   intro:"Défi 2 — Deux papiers arrivent la même semaine, et ils ne se lisent pas de la même façon. Le rapport d'inspection décrit : il numérote ses sections, il chiffre, il raconte l'histoire du bâtiment dans une langue qu'on n'entend jamais parler. La soumission propose : elle aligne des postes, un prix par ligne, et surtout une colonne d'exclusions où se cachent les mauvaises surprises. Savoir lire, ici, c'est savoir quoi chercher dans lequel des deux.",
   dialogue:'t2', next:{id:'t3', tit:'Défi 3 · Quand le plan change', sub:"Poser les questions qui manquent devant quatre personnes qui parlent en même temps."}},

  {id:'t3', no:'3', title:'Défi 3 · Quand le plan change', color:'#3B49A0',
   lead:"Poser des questions reliées à des travaux de rénovation : deux prix, deux délais, quatre interlocuteurs — et une décision à prendre le jour même.",
   intro:"Défi 3 — On ouvre le plancher, et on trouve autre chose. C'est le moment où le chantier cesse d'être une affaire de spécialistes et devient la vôtre : personne ne décidera à votre place, et personne ne vous posera vos questions. Quatre personnes parlent, chacune de son point de vue — l'entrepreneur du sien, l'inspectrice du sien, le service des permis du sien. Ce qu'il faut savoir faire tient en trois gestes : redire ce qu'on a compris, demander ce qui manque, dire ce qu'on choisit.",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"Mener l'échange avec l'entrepreneur, redire le diagnostic à voix haute, puis écrire ton courriel."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n6-habitation/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"Poser tes questions à un homme de métier, redire un diagnostic à voix haute avec les détails nécessaires, puis écrire un courriel en trois paragraphes.",
   intro:"Je me lance — C'est à toi : tu mènes l'échange avec l'entrepreneur, tu redis ensuite le diagnostic à quelqu'un qui n'était pas là, puis tu écris le courriel qui met par écrit ce qui n'a été dit que de vive voix."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#A5335F', custom:true,
   lead:"Rassembler les mots des gens et des papiers, de ce qui tient la maison debout, de ce qu'on lit avant de signer et de ce qu'on trouve en ouvrant.",
   intro:"Je retiens des mots — Note tes mots utiles, révise avec les cartes mémoire, puis évalue ce que tu es maintenant capable de faire."},
];
