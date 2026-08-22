const SECTIONS = [
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n6-actualite/icons/play.svg" alt="">', title:'Je découvre', color:'#A5335F',
   lead:"Reconnaître les cinq genres de l'actualité — la chronique pratique, l'entrevue, le documentaire, le fait divers, le courrier des lecteurs — et savoir d'avance ce que chacun donne.",
   intro:"Nadège Beauplan a quarante-quatre ans. Elle est arrivée d'Haïti il y a six ans et elle tient le comptoir d'accueil de la bibliothèque de la Batture, à Trois-Rivières. Sa laveuse a cessé de vidanger après trois ans et quatre mois, et le marchand lui a répondu que la garantie était expirée. Son collègue Raphaël Choquette lui dit qu'une chronique de radio a déjà répondu à cette question — et, au passage, que les cinq façons de parler d'un sujet dans les médias ne se ressemblent pas du tout.",
   dialogue:'prep', next:{id:'t1', tit:'Défi 1 · La chronique pratique', sub:"Suivre une explication en étapes et retrouver ce que reprennent « le », « en » et « où »."}},

  {id:'t1', no:'1', title:'Défi 1 · La chronique pratique', color:'#1D6B8F',
   lead:"Comprendre une chronique pratique du début à la fin : les étapes dans l'ordre, les exemples qui les illustrent, et les mots qui renvoient à ce qui précède.",
   intro:"Défi 1 — Une chronique pratique n'est pas difficile à cause de son vocabulaire : elle est difficile parce que tout s'y tient. Claudine Rousseau dit « je vous en parle », « c'est là qu'on les trouve », « je le sais » — et chaque fois, le petit mot renvoie à quelque chose dit trente secondes plus tôt. Perdre le fil, ce n'est pas manquer un mot : c'est perdre à quoi il renvoie.",
   dialogue:'t1', next:{id:'t2', tit:"Défi 2 · L'entrevue et le documentaire", sub:"Entendre ce qui s'est passé avant, et ce que quelqu'un souhaite qu'il arrive."}},

  {id:'t2', no:'2', title:"Défi 2 · L'entrevue et le documentaire", color:'#B45309',
   lead:"Suivre une entrevue longue et un extrait de documentaire : ce qui précède le passé, et ce qu'on demande, exige ou souhaite.",
   intro:"Défi 2 — Deux genres, deux difficultés. Le documentaire raconte au passé simple, un temps qu'on ne parle jamais mais qu'on lit et qu'on entend : « ils se réunirent », « l'entente dura ». L'entrevue, elle, empile les époques — ce que les gens avaient fait avant d'appeler, ce qu'ils ont appris ensuite — et ajoute ce que l'invitée voudrait qu'il arrive. Trois temps différents dans la même minute.",
   dialogue:'t2', next:{id:'t3', tit:'Défi 3 · Le courrier des lecteurs', sub:"Lire des opinions signées, poser une hypothèse en « si » et annoncer son point de vue."}},

  {id:'t3', no:'3', title:'Défi 3 · Le courrier des lecteurs', color:'#3B49A0',
   lead:"Lire des lettres de lecteurs et un fait divers, distinguer une opinion appuyée d'une opinion nue, et formuler la sienne.",
   intro:"Défi 3 — Dans la même double page, le journal met ce qu'il y a de plus sec et ce qu'il y a de plus personnel : quinze lignes de fait divers d'un côté, des lettres signées de l'autre. Les lettres se ressemblent toutes de loin ; de près, l'une s'appuie sur une date et un résultat, l'autre sur une crainte. Et presque toutes emploient « si » — la petite conjonction qui pose une condition et permet de discuter sans se fâcher.",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"Expliquer la démarche à quelqu'un, l'enregistrer, puis écrire au journal."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n6-actualite/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"Expliquer à quelqu'un ce qu'on a compris, en faire le compte rendu détaillé à voix haute, puis écrire au courrier des lecteurs.",
   intro:"Je me lance — C'est à toi : tu expliques la démarche à l'assistant, qui n'a rien écouté et qui doute ; tu en fais ensuite le compte rendu à voix haute ; puis tu écris ton courriel au Courrier de la Batture."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#A5335F', custom:true,
   lead:"Rassembler les mots des genres, de la garantie, de l'enquête et de l'opinion.",
   intro:"Je retiens des mots — Note tes mots utiles, révise avec les cartes mémoire, puis évalue ce que tu es maintenant capable de faire."},
];
