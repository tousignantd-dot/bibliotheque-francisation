const SECTIONS = [
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n5-transport/icons/play.svg" alt="">', title:'Je découvre', color:'#1D6B8F',
   lead:"Nommer l'état d'une route avec les mots du bulletin, entendre la différence entre le son de « an » et le son de « on », et savoir ce qu'un bulletin de circulation dit toujours.",
   intro:"Tereza Nogueira a quarante et un ans. Elle est arrivée du Brésil il y a quatre ans et elle habite à Longueuil. Elle travaille comme aide-technicienne dans un atelier d'assemblage de Saint-Laurent, à l'autre bout de l'île. Tous les matins à six heures cinquante, elle retrouve Amine Haddad au stationnement incitatif : ils font la route ensemble depuis deux ans. La radio est ouverte, la chronique de circulation commence — et depuis deux ans, Tereza n'en comprend que trois mots sur dix.",
   dialogue:'prep', next:{id:'t1', tit:'Défi 1 · Ce qui bloque la route', sub:"Comprendre ce qui bloque, où exactement, et pour combien de temps."}},

  {id:'t1', no:'1', title:'Défi 1 · Ce qui bloque la route', color:'#B45309',
   lead:"Repérer dans un bulletin ce qui bloque, l'endroit exact et la durée annoncée, puis le redire avec les bonnes prépositions de lieu et de temps.",
   intro:"Défi 1 — Un bulletin de circulation dit toujours les mêmes quatre choses, dans le même ordre : quoi, où, depuis quand, pour combien de temps. Ce qui se joue ici : entendre ces quatre choses au passage, sans pouvoir faire répéter, et les redire à quelqu'un — parce que « ça bloque » n'a jamais fait décider personne.",
   dialogue:'t1', next:{id:'t2', tit:'Défi 2 · Le bulletin de 6 h 50', sub:"Suivre un bulletin entier et en tirer ce qui touche votre trajet à vous."}},

  {id:'t2', no:'2', title:'Défi 2 · Le bulletin de 6 h 50', color:'#A5335F',
   lead:"Suivre un bulletin complet de quatre ou cinq routes, prendre en note ce qui vous concerne, et comprendre les directives qu'on donne aux automobilistes.",
   intro:"Défi 2 — Un vrai bulletin ne parle pas d'une route : il en fait quatre en cinquante secondes, et la vôtre est peut-être la troisième. Ce qui se joue ici : tenir jusqu'au bout sans perdre le début, écrire pendant qu'on écoute, et reconnaître les phrases toutes faites du métier — « on demande aux automobilistes de », « il est recommandé de », « empruntez le pont ».",
   dialogue:'t2', next:{id:'t3', tit:'Défi 3 · Le trajet refait', sub:"Expliquer l'imprévu, proposer un autre chemin, annoncer son retard."}},

  {id:'t3', no:'3', title:'Défi 3 · Le trajet refait', color:'#0D7A6F',
   lead:"Expliquer un imprévu de la route à quelqu'un qui n'a rien entendu, dire par où l'on passera à la place, et annoncer son heure d'arrivée de vive voix comme par écrit.",
   intro:"Défi 3 — Comprendre le bulletin ne sert à rien si l'on n'en fait rien. Sept heures vingt, l'autoroute est bloquée, l'atelier ouvre à huit heures et c'est Tereza qui a les clés. Ce qui se joue ici : expliquer en trois phrases ce qui se passe, dire par où l'on passera en marquant le moyen — en passant par le boulevard, en évitant l'autoroute —, et donner une heure d'arrivée en chiffres.",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"Expliquer l'entrave à votre collègue, appeler l'atelier, écrire le mot du matin."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n5-transport/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"Expliquer une entrave du début à la fin, laisser un message de retard sur une boîte vocale, puis écrire le mot qui dit à l'équipe ce qui se passe.",
   intro:"Je me lance — C'est à vous : vous expliquez à votre collègue ce que la radio vient d'annoncer et vous proposez un autre chemin, vous laissez un message sur la boîte vocale de votre responsable pour annoncer votre retard, puis vous écrivez le mot que l'équipe trouvera en arrivant."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#1D6B8F', custom:true,
   lead:"Rassembler les mots de l'état des routes, de l'incident, du bulletin et du trajet refait.",
   intro:"Je retiens des mots — Notez vos mots utiles, révisez avec les cartes mémoire, puis évaluez ce que vous êtes maintenant capable de faire."},
];
