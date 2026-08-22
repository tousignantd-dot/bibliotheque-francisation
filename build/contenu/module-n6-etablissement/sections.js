const SECTIONS = [
  // La couleur d'une section n'est pas celle du module : chacune porte celle
  // de son travail, comme dans les séances. L'acier du niveau 6 tient
  // l'en-tête, pas les onglets.
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n6-etablissement/icons/play.svg" alt="">', title:'Je découvre', color:'#A5335F',
   lead:"Savoir qui fait quoi dans un établissement — le comptoir, l'orientation, l'enseignement, la direction — et ce que chaque papier du centre dit vraiment.",
   intro:"Bintou Sangaré a trente-quatre ans. Elle est arrivée du Mali il y a trois ans et elle est commis de soir dans une pharmacie de quartier, à Sherbrooke ; le soir, trois fois par semaine, elle suit sa francisation au Centre d'éducation des adultes des Deux-Ruisseaux. Elle termine en février, et elle ne sait pas ce qui vient après. Au comptoir de l'accueil, Réal Duquette lui apprend d'abord une chose que personne ne dit à voix haute : dans un établissement, ce qui compte finit toujours en papier, et chaque question a sa personne.",
   dialogue:'prep', next:{id:'t1', tit:"Défi 1 · La rencontre d'orientation", sub:"S'informer pour choisir un programme : poser des questions indirectes et retrouver ce que reprennent « le », « en » et « y »."}},

  {id:'t1', no:'1', title:"Défi 1 · La rencontre d'orientation", color:'#1D6B8F',
   lead:"Suivre un entretien d'une heure du début à la fin : les trois portes d'entrée d'un programme, ce qui compte et ce qui ne compte pas, et les mots qui renvoient à ce qui vient d'être dit.",
   intro:"Défi 1 — Un entretien d'orientation n'est pas une série de questions et de réponses : c'est un fil. Pascal Lachapelle dit « j'y pense », « ça ne compte pas », « celui qui vous concerne » — et chaque fois, un petit mot renvoie à quelque chose dit une minute plus tôt. Perdre le fil ici ne coûte pas un mot : ça coûte une année.",
   dialogue:'t1', next:{id:'t2', tit:'Défi 2 · Les papiers du centre', sub:"Lire une description de programme et un avis officiel : ce qui est décidé, par qui, et pour quand."}},

  {id:'t2', no:'2', title:'Défi 2 · Les papiers du centre', color:'#B45309',
   lead:"Lire un document scolaire officiel et une description de programme : trouver la condition, la date, l'encadré — et comprendre qui doit bouger quand personne n'est nommé.",
   intro:"Défi 2 — Deux feuilles, deux façons de ne rien dire clairement. L'avis officiel écrit « la candidate fournira » au futur pour donner un ordre, et « les documents se déposent » sans dire par qui. La description du programme, elle, commence par l'histoire du centre au passé simple — « le centre ouvrit ses portes en 1968 » — un temps que personne ne parle et que tout le monde écrit. Rien de tout cela n'est difficile ; tout cela s'apprend une fois.",
   dialogue:'t2', next:{id:'t3', tit:'Défi 3 · La rencontre du 14 novembre', sub:"Prendre sa place autour d'une table où quatre personnes parlent de votre dossier."}},

  {id:'t3', no:'3', title:'Défi 3 · La rencontre du 14 novembre', color:'#3B49A0',
   lead:"Participer à une rencontre scolaire : entendre qui décide quoi, s'introduire dans la discussion sans couper, poser une condition et annoncer son point de vue comme un point de vue.",
   intro:"Défi 3 — Quatre personnes, une heure, une table. Chacune a un pouvoir différent : l'une explique, l'une décide, l'une témoigne, et la quatrième, c'est vous. Ce qui est difficile n'est pas de comprendre les phrases : c'est d'entendre laquelle engage quelque chose, et de trouver le moment où l'on peut parler sans couper personne. Une rencontre bien suivie se termine par un écrit ; mal suivie, elle se termine par quatre dates que plus personne ne se rappelle.",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"S'informer auprès du conseiller, expliquer la démarche à voix haute, puis écrire au centre."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n6-etablissement/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"S'informer pour choisir un programme, expliquer la démarche à quelqu'un, puis écrire un courriel formel au centre.",
   intro:"Je me lance — C'est à toi : tu t'informes auprès du conseiller d'orientation, qui répond mais ne devine rien ; tu expliques ensuite la démarche à voix haute à un camarade ; puis tu écris ton courriel au secrétariat."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#A5335F', custom:true,
   lead:"Rassembler les mots des personnes, des programmes, des écrits officiels et des rencontres.",
   intro:"Je retiens des mots — Note tes mots utiles, révise avec les cartes mémoire, puis évalue ce que tu es maintenant capable de faire."},
];
