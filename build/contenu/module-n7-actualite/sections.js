const SECTIONS = [
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n7-actualite/icons/play.svg" alt="">', title:'Je découvre', color:'#A5335F',
   lead:"Nommer les genres de l'information, distinguer un fait d'une opinion, reconnaître les mots de l'actualité.",
   intro:"Farida Benali est éducatrice dans un centre de la petite enfance. Elle est arrivée d'Algérie il y a trois ans et, jusqu'à cet automne, elle laissait la radio parler sans l'écouter vraiment. Puis une nouvelle a touché sa rue. Sa voisine Suzie Lamontagne, qui anime le blogue du quartier, lui explique ce matin qu'un reportage, une chronique et un éditorial ne racontent pas du tout la même chose.",
   dialogue:'prep', next:{id:'t1', tit:'Défi 1 · Le reportage', sub:"Écouter un reportage long en plusieurs fois et en retenir l'essentiel."}},

  {id:'t1', no:'1', title:'Défi 1 · Le reportage', color:'#3B49A0',
   lead:"Suivre un reportage informatif du début à la fin, repérer ce qui est confirmé et ce qui ne l'est pas.",
   intro:"Défi 1 — Un reportage de radio dure trois minutes et personne ne le répète. On ne le comprend pas d'un coup : on l'écoute une première fois pour savoir de quoi il parle, une deuxième pour les faits, une troisième pour les détails. Et on apprend à entendre le mot qui change tout : « ouvrirait » n'est pas « ouvre ».",
   dialogue:'t1', next:{id:'t2', tit:"Défi 2 · L'article", sub:"Lire un article informatif et écouter l'entrevue qui l'accompagne."}},

  {id:'t2', no:'2', title:"Défi 2 · L'article", color:'#B45309',
   lead:"Lire un article informatif, écouter une entrevue, rapporter ce que quelqu'un a dit.",
   intro:"Défi 2 — Le lendemain, la nouvelle est écrite. Un article informatif ne dit pas « je » : il dit qui a décidé, quand, et il fait parler les autres. C'est pour ça qu'il est plein de phrases passives et de paroles rapportées. Savoir les lire, c'est savoir qui parle dans un texte où personne ne semble parler.",
   dialogue:'t2', next:{id:'t3', tit:"Défi 3 · L'opinion", sub:"Démêler le fait de l'opinion dans une chronique, puis répondre."}},

  {id:'t3', no:'3', title:"Défi 3 · L'opinion", color:'#0D7A6F',
   lead:"Reconnaître une opinion, comprendre un argument, concéder un point et donner le sien.",
   intro:"Défi 3 — Une chronique, ce n'est pas une nouvelle : c'est quelqu'un qui pense tout haut et qui signe. Le piège, c'est qu'elle contient aussi des faits vrais. Apprendre à séparer les deux, c'est pouvoir répondre sans se tromper de cible — et répondre commence toujours par accorder quelque chose à l'autre.",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"Discuter d'une nouvelle, en faire le compte rendu, puis écrire dans le blogue."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n7-actualite/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"Échanger sur une nouvelle, faire le compte rendu d'un fait d'actualité, intervenir dans un blogue.",
   intro:"Je me lance — C'est à vous : vous discutez d'une nouvelle avec l'assistant, vous en faites le compte rendu à voix haute, puis vous écrivez votre billet dans le blogue du quartier."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#A5335F', custom:true,
   lead:"Rassembler les mots des genres, des faits, des sources et de l'opinion.",
   intro:"Je retiens des mots — Notez vos mots utiles, révisez avec les cartes mémoire, puis évaluez ce que vous êtes maintenant capable de faire."},
];
