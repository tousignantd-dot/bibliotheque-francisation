const SECTIONS = [
  // La couleur d'une section n'est pas celle du module : chacune porte celle
  // de son travail. L'acier du niveau 6 tient l'en-tête, pas les onglets.
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n6-classe/icons/play.svg" alt="">', title:'Je découvre', color:'#A5335F',
   lead:"Savoir ce qu'est un travail de recherche, ce qu'on en attend, et reconnaître les mots qui reviennent partout dans une classe où l'on cherche.",
   intro:"Marisol Ferreyra a quarante et un ans. Elle est arrivée du Pérou il y a cinq ans, où elle était technicienne de laboratoire, et elle suit sa francisation le jour au Centre d'éducation des adultes des Trois-Chênes, à Sainte-Angèle-des-Prés. Un lundi matin, son enseignante annonce un travail de recherche en équipe : trois semaines, un sujet à choisir, trois sources au minimum, un texte à remettre et cinq minutes devant la classe. Marisol prend le bac brun de son balcon — deux ans qu'elle ne sait pas ce qui a le droit d'aller dedans.",
   dialogue:'prep', next:{id:'t1', tit:'Défi 1 · Ce que le travail demande', sub:"Lire une consigne d'une page et demie et la grille qui l'évalue : ce qu'il faut faire, dans quel ordre, et sur quoi on sera noté."}},

  {id:'t1', no:'1', title:'Défi 1 · Ce que le travail demande', color:'#B45309',
   lead:"Comprendre un écrit qui ordonne : retrouver l'ordre des étapes sans connecteurs de temps, reconnaître un futur qui donne un ordre, et lire une grille d'évaluation ligne à ligne.",
   intro:"Défi 1 — Une consigne de travail n'est pas un texte qu'on lit : c'est un texte qu'on démonte. Rien n'y est dit deux fois, l'ordre des étapes se cache dans des mots de deux syllabes — « une fois », « avant de », « dès que » —, et la phrase la plus importante de la page est presque toujours celle qu'on saute. Marisol et Youssef ne s'entendent même pas sur le nombre de documents à remettre. Ils ont raison tous les deux d'être venus poser la question.",
   dialogue:'t1', next:{id:'t2', tit:'Défi 2 · Ce que disent les sources', sub:"Trois documents sur le même sujet, et pas un qui dise la même chose que l'autre. Suivre le fil sans perdre qui parle."}},

  {id:'t2', no:'2', title:'Défi 2 · Ce que disent les sources', color:'#1D6B8F',
   lead:"Comprendre de l'information liée à un sujet de recherche : lire un texte suivi, retrouver ce que reprennent les petits mots, et distinguer ce qu'un document affirme de ce que quelqu'un en pense.",
   intro:"Défi 2 — La ville explique une règle, le bulletin raconte ce qui est arrivé, une lectrice donne son avis. Aucun des trois ne ment, et pourtant ils ne s'accordent pas. Ce qui est difficile ici n'est plus le mot : c'est de savoir ce que « en » vient de remplacer, quelle année « où » rattache, et lequel de deux faits passés est arrivé le premier. Perdre ce fil-là, dans un travail de recherche, c'est écrire le contraire de sa source sans s'en apercevoir.",
   dialogue:'t2', next:{id:'appli', tit:'Je me lance', sub:"Se répartir le travail avec son équipe, présenter son compte rendu à la classe, puis écrire son texte."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n6-classe/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"Se partager un travail dans une rencontre d'équipe, rendre compte d'une recherche à voix haute, puis écrire un texte organisé en paragraphes.",
   intro:"Je me lance — C'est à toi : tu tiens d'abord la rencontre d'équipe, où il faut proposer une répartition et l'obtenir ; tu présentes ensuite ton compte rendu à la classe ; puis tu écris l'introduction de ton travail, en trois paragraphes."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#A5335F', custom:true,
   lead:"Rassembler les mots du travail de recherche, de la consigne et des documents qu'on cite.",
   intro:"Je retiens des mots — Note tes mots utiles, révise avec les cartes mémoire, puis évalue ce que tu es maintenant capable de faire."},
];
