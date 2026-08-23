const SECTIONS = [
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n8-oeuvres/icons/play.svg" alt="">', title:'Je découvre', color:'#1D6B8F',
   lead:"Séparer le fait, l'interprétation et le jugement, entendre ce qu'une voix ajoute aux mots, et redire avec d'autres mots ce que quelqu'un vient de dire.",
   intro:"Fatoumata Sidibé est technicienne en documentation à la bibliothèque du quartier Jacques-Cartier, à Sherbrooke. Arrivée du Mali il y a sept ans, elle anime depuis l'automne le cercle du mardi soir : dix-huit personnes, une œuvre par mois, au sous-sol. Le cercle marche, et pourtant il tourne à vide — chacun raconte ce qu'il a vu, chacun dit s'il a aimé, et à neuf heures moins quart tout le monde se lève. Ce mardi-là, elle demande à Josyane Deschatelets, qui enseigne la littérature au cégep et tient une chronique à la radio communautaire, de venir. Josyane accepte à une condition : ce ne sera pas elle qui parlera en premier.",
   dialogue:'prep', next:{id:'t1', tit:'Défi 1 · La dernière scène', sub:"Comprendre une télésérie dont la fin ne conclut pas, et appuyer sa lecture sur des détails de l'image."}},

  {id:'t1', no:'1', title:'Défi 1 · La dernière scène', color:'#A83A22',
   lead:"Comprendre un film, une télésérie ou une pièce de théâtre : suivre ce qui s'y passe, puis dire ce qu'on en tire et pourquoi.",
   intro:"Défi 1 — La finale des « Eaux basses » a été regardée par tout le cercle, et personne n'en a tiré la même chose. Ce défi apprend trois gestes. Décrire une scène sans l'interpréter — ce qui est beaucoup plus difficile qu'il n'y paraît, parce qu'on interprète sans s'en apercevoir. Nommer ce qui aurait pu se passer et ne s'est pas passé : c'est le premier outil de l'interprétation, et il tient dans un temps de verbe. Et mettre en avant l'indice qui porte votre lecture, au lieu de la répéter plus fort.",
   dialogue:'t1', next:{id:'t2', tit:"Défi 2 · Ce qui n'est pas écrit", sub:"Lire une nouvelle et un poème dont l'essentiel est dit une seule fois, et discrètement."}},

  {id:'t2', no:'2', title:"Défi 2 · Ce qui n'est pas écrit", color:'#0D7A6F',
   lead:"Comprendre une nouvelle et un texte poétique : suivre un récit littéraire, repérer l'endroit où tout bascule, et lire une image.",
   intro:"Défi 2 — Deux textes courts, écoutés d'abord à la radio puis lus. Une nouvelle de six pages où l'essentiel est dit une seule fois, entre parenthèses. Un poème de vingt-deux vers dont le dernier mot change le sens de tous les autres. Ce défi apprend à lire la langue de la littérature — le passé simple et le plus-que-parfait, qu'on ne parle jamais mais qu'on lit partout — et à dire son doute sans le déguiser en certitude : il se peut que, il est possible que, il semble que.",
   dialogue:'t2', next:{id:'t3', tit:'Défi 3 · Défendre une lecture', sub:"Tenir sa lecture devant quelqu'un qui n'a pas la même, et discuter une critique sans avoir vu l'œuvre."}},

  {id:'t3', no:'3', title:'Défi 3 · Défendre une lecture', color:'#A5335F',
   lead:"Émettre des commentaires sur une œuvre en les justifiant, résumer les propos de quelqu'un d'autre sans les déformer, et discuter un texte d'opinion.",
   intro:"Défi 3 — Au cercle, deux lectures s'affrontent, et Josyane pose la seule question qui les départage : est-ce que votre lecture explique aussi l'indice de l'autre ? Ce défi apprend à citer un passage sans le répéter en entier, à concéder avant de répondre, et à reconnaître la frontière entre citer, résumer et déformer. Il se termine sur une critique de journal que personne n'a les moyens de contredire — personne n'a vu la pièce — mais que tout le monde peut examiner : où décrit-elle, où juge-t-elle, et où devine-t-elle ?",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"Discuter la fin avec l'assistant, proposer une lecture à voix haute, écrire au courrier des lecteurs."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n8-oeuvres/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"Discuter une fin ouverte avec quelqu'un qui ne la lit pas comme vous, proposer une lecture à voix haute, puis écrire deux cents mots au courrier des lecteurs.",
   intro:"Je me lance — C'est à vous : vous discutez la dernière scène avec quelqu'un qui a vu exactement la même chose et n'en tire pas la même histoire, vous proposez ensuite une lecture à voix haute devant le cercle, puis vous répondez par écrit à une critique de journal."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#1D6B8F', custom:true,
   lead:"Rassembler les mots de l'interprétation, du récit, du poème et de la critique.",
   intro:"Je retiens des mots — Notez vos mots utiles, révisez avec les cartes mémoire, puis évaluez ce que vous êtes maintenant capable de faire."},
];
