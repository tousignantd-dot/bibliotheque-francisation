const SECTIONS = [
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n3-loyer/icons/play.svg" alt="">', title:'Je découvre', color:'#A5335F',
   lead:"Nommer les pièces d'un logement et comprendre ce qu'est un trois et demie, un quatre et demie.",
   intro:"Dilnoza est arrivée d'Ouzbékistan il y a quatorze mois. Elle habite un deux et demie avec son mari et son garçon de six ans, qui dort dans le salon. Dans le corridor du centre, son camarade Rachid lui dit d'aller voir le babillard : il y a des petites annonces. Elle les a déjà regardées, et elle n'a compris presque aucun mot.",
   dialogue:'prep', next:{id:'t1', tit:'Défi 1 · Lire la petite annonce', sub:"Décoder une annonce de six lignes : les abréviations, le loyer, ce qui est compris."}},

  {id:'t1', no:'1', title:'Défi 1 · Lire la petite annonce', color:'#1D6B8F',
   lead:"Décoder une annonce de six lignes : les abréviations, le loyer, ce qui est compris.",
   intro:"Défi 1 — Une petite annonce tient en six lignes et elle est écrite en abrégé. « 4 ½ · 2e ét. · ch. et écl. · s.-sol · libre 1er juill. » : sept mots coupés qui décident si le logement vous convient ou non. On les lit une fois pour toutes.",
   dialogue:'t1', next:{id:'t2', tit:'Défi 2 · Téléphoner pour visiter', sub:"Appeler, poser trois questions, prendre rendez-vous et répéter le jour et l'heure."}},

  {id:'t2', no:'2', title:'Défi 2 · Téléphoner pour visiter', color:'#B45309',
   lead:"Appeler, poser trois questions, prendre rendez-vous et répéter le jour et l'heure.",
   intro:"Défi 2 — Au téléphone, on ne voit personne et on ne peut rien montrer du doigt. Trois questions bien préparées valent mieux que dix questions improvisées : ce qui est compris dans le loyer, combien il y a de chambres, à quelle date c'est libre. Ensuite, on demande à visiter.",
   dialogue:'t2', next:{id:'t3', tit:'Défi 3 · Poser mes questions sur place', sub:"Pendant la visite : demander, comprendre la réponse, et vérifier avant de partir."}},

  {id:'t3', no:'3', title:'Défi 3 · Poser mes questions sur place', color:'#0D7A6F',
   lead:"Pendant la visite : demander, comprendre la réponse, et vérifier avant de partir.",
   intro:"Défi 3 — Une visite dure quinze minutes. La propriétaire montre les pièces, mais elle ne dit pas tout : elle répond à ce qu'on lui demande. Le stationnement, la buanderie, la date, l'argent à donner aujourd'hui — quatre choses qui ne se voient pas et qui se demandent.",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"Visiter un logement à voix haute, puis écrire à quelqu'un ce que vous avez vu."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n3-loyer/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"Visiter un logement à voix haute, puis écrire à quelqu'un ce que vous avez vu.",
   intro:"Je me lance — C'est à toi : tu visites un logement à louer, tu poses tes questions et tu vérifies ce que tu as compris, puis tu écris un court message à une personne de ta famille pour lui décrire le logement."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#A5335F', custom:true,
   lead:"Rassembler les mots des pièces, de l'annonce, de l'appel et de la visite.",
   intro:"Je retiens des mots — Note tes mots utiles, révise avec les cartes mémoire, puis évalue ce que tu es maintenant capable de faire."},
];
