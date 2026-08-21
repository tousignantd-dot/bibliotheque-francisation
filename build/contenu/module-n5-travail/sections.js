const SECTIONS = [
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n5-travail/icons/play.svg" alt="">', title:'Je découvre', color:'#A5335F',
   lead:"Comprendre ce qu'un poste demande par écrit, nommer le matériel et les tâches, et tenir le bon registre au téléphone.",
   intro:"Dorine Kabeya a quarante et un ans. Elle est arrivée de Kinshasa il y a deux ans et elle travaille depuis dix-huit mois à la Coopérative d'aide à domicile de Rosemont. Lundi, elle passe de l'entretien à l'accueil : un poste permanent, un bureau, un téléphone à elle. Son chef d'équipe, Ghislain Marcoux, lui explique ce qui change — et presque tout ce qui change s'écrit.",
   dialogue:'prep', next:{id:'t1', tit:"Défi 1 · La boîte vocale et la note", sub:"Enregistrer un message d'accueil, écouter un appel et en tirer une note utile."}},

  {id:'t1', no:'1', title:"Défi 1 · La boîte vocale et la note", color:'#B45309',
   lead:"Enregistrer un message d'accueil clair, puis transformer un message entendu en une note que quelqu'un d'autre pourra lire.",
   intro:"Défi 1 — Une boîte vocale parle à votre place quand vous n'êtes pas là : ce que vous y avez enregistré une fois se répète cent fois. Et à l'accueil, on ne prend pas des appels pour soi : on prend des messages pour les autres. Ce qui se joue ici : dire l'essentiel en trente secondes, puis écrire en six lignes ce qu'une personne a raconté en deux minutes.",
   dialogue:'t1', next:{id:'t2', tit:"Défi 2 · Le mode d'emploi", sub:"Lire les directives d'un appareil, puis écrire celles que les autres liront."}},

  {id:'t2', no:'2', title:"Défi 2 · Le mode d'emploi", color:'#1D6B8F',
   lead:"Comprendre des directives d'utilisation dans l'ordre, et écrire les siennes pour le collègue qui viendra après.",
   intro:"Défi 2 — Le photocopieur du corridor a été remplacé un jeudi, sans que personne soit prévenu. Le livret livré avec l'appareil fait quatre-vingts pages et personne ne le lira. Ce qui se joue ici : trouver dans un mode d'emploi la seule phrase qui vous concerne, puis écrire vous-même la demi-page que vos collègues, eux, liront vraiment.",
   dialogue:'t2', next:{id:'t3', tit:"Défi 3 · La demande de congé", sub:"Nommer les étapes d'une démarche, la mener au bout et préparer son absence."}},

  {id:'t3', no:'3', title:"Défi 3 · La demande de congé", color:'#0D7A6F',
   lead:"Comprendre et nommer les étapes d'une démarche administrative, poser ses questions, puis régler son courriel d'absence.",
   intro:"Défi 3 — Demander un congé n'est pas demander une permission : c'est suivre une procédure. Six étapes, un formulaire, deux signatures, une confirmation écrite. Ce qui se joue ici : comprendre l'ordre de ces étapes quand quelqu'un vous les explique une seule fois, savoir les redire ensuite, et ne pas partir en congé en laissant derrière vous un téléphone et une boîte de courriels qui ne disent rien.",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"Demander votre congé, enregistrer votre message d'accueil, écrire votre courriel d'absence."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n5-travail/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"Mener une demande de congé du début à la fin, enregistrer un message d'accueil, puis écrire son courriel d'absence.",
   intro:"Je me lance — C'est à vous : vous demandez votre congé à votre chef d'équipe, vous enregistrez le message d'accueil de votre boîte vocale, puis vous écrivez le courriel qui répondra à votre place."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#A5335F', custom:true,
   lead:"Rassembler les mots du poste, du téléphone, du matériel et de la démarche.",
   intro:"Je retiens des mots — Notez vos mots utiles, révisez avec les cartes mémoire, puis évaluez ce que vous êtes maintenant capable de faire."},
];
