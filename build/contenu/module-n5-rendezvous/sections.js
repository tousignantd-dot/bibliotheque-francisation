const SECTIONS = [
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n5-rendezvous/icons/play.svg" alt="">', title:'Je découvre', color:'#B45309',
   lead:"Nommer un problème de santé qui dure, dire depuis quand, et savoir à qui s'adresser.",
   intro:"Rachid Benali a cinquante-deux ans. Il est préposé à l'entretien dans une école de Longueuil et il n'a pas vu de médecin depuis quatre ans. Depuis le mois de mars, la tête lui tourne quand il se lève, et il est fatigué. Il appelle ça « rien ». Sa fille Nadia, elle, compte les mois.",
   dialogue:'prep', next:{id:'t1', tit:"Défi 1 · L'appel à la clinique", sub:"Téléphoner pour obtenir un rendez-vous, choisir un moment et noter tout ce qu'on vous dit."}},

  {id:'t1', no:'1', title:"Défi 1 · L'appel à la clinique", color:'#A5335F',
   lead:"Demander un rendez-vous au téléphone, s'identifier, choisir un moment et confirmer avant de raccrocher.",
   intro:"Défi 1 — Au bout du fil, il n'y a pas un médecin : il y a une agente administrative. Elle ne soigne personne, mais c'est elle qui décide si votre rendez-vous durera quinze minutes ou trente. Ce qui se joue dans cet appel : dire son affaire en une phrase, donner son numéro sans hésiter, et repartir avec une date, une heure et tout ce qui va avec.",
   dialogue:'t1', next:{id:'t2', tit:'Défi 2 · Dans le bureau', sub:"Raconter un problème qui dure, comprendre l'explication du médecin et poser ses questions."}},

  {id:'t2', no:'2', title:'Défi 2 · Dans le bureau', color:'#1D6B8F',
   lead:"Raconter trois mois en trois phrases, dire quand le malaise arrive, comprendre et questionner.",
   intro:"Défi 2 — Un médecin dispose de trente minutes et pose peu de questions : c'est vous qui racontez. Un problème qui dure ne se dit pas avec une liste de mots, il se raconte — ce qui se passait avant, ce qui est arrivé, ce que ça fait aujourd'hui, et à quel moment précis. Puis vient la partie que les élèves oublient : poser ses propres questions avant de sortir.",
   dialogue:'t2', next:{id:'t3', tit:'Défi 3 · Déplacer ou annuler', sub:"Changer un rendez-vous, l'annuler dans les règles et en reprendre un autre."}},

  {id:'t3', no:'3', title:'Défi 3 · Déplacer ou annuler', color:'#0D7A6F',
   lead:"Faire changer une date, annuler à temps, laisser un message d'annulation clair.",
   intro:"Défi 3 — Un rendez-vous pris n'est pas un rendez-vous gardé. Le travail change, un enfant tombe malade, l'autobus n'arrive pas. Ce qui distingue une annulation d'une absence, c'est un appel fait à temps — et une phrase qui dit ce qu'on annule, et ce qu'on veut à la place.",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"Téléphoner pour de vrai, raconter votre problème au médecin, puis écrire à la clinique."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n5-rendezvous/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"Mener un appel du début à la fin, raconter votre problème en une minute, puis écrire à la clinique.",
   intro:"Je me lance — C'est à vous : vous téléphonez à une clinique, vous racontez à un médecin un problème qui dure, puis vous écrivez à la clinique pour changer un rendez-vous."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#B45309', custom:true,
   lead:"Rassembler les mots de la clinique, de l'appel, du bureau et de l'annulation.",
   intro:"Je retiens des mots — Notez vos mots utiles, révisez avec les cartes mémoire, puis évaluez ce que vous êtes maintenant capable de faire."},
];
