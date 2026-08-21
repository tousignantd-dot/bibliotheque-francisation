const SECTIONS = [
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n5-urgence/icons/play.svg" alt="">', title:'Je découvre', color:'#A5335F',
   lead:"Reconnaître un vrai problème, savoir quel numéro composer, et répondre aux questions d'une infirmière au téléphone.",
   intro:"Marisol Quintero a trente-huit ans. Elle est arrivée de Colombie il y a trois ans et elle travaille dans une buanderie industrielle de Saint-Léonard. Sa mère Amparo, soixante et onze ans, vit chez elle depuis un an. Ce mercredi soir, Amparo fait de la fièvre pour la deuxième journée et répète que ce n'est rien.",
   dialogue:'prep', next:{id:'t1', tit:"Défi 1 · L'appel au 9-1-1", sub:"Donner l'endroit, dire ce qui se passe et suivre les consignes du répartiteur."}},

  {id:'t1', no:'1', title:"Défi 1 · L'appel au 9-1-1", color:'#B45309',
   lead:"Mener un appel d'urgence : l'adresse d'abord, une phrase pour dire ce qui se passe, puis répondre et exécuter.",
   intro:"Défi 1 — Il est deux heures du matin et Amparo est au bas de l'escalier. Un appel au 9-1-1 n'est pas une conversation : c'est le répartiteur qui mène, et chaque question qu'il pose sert à envoyer la bonne équipe au bon endroit. Ce qui se joue ici : dire où vous êtes avant tout le reste, répondre court, et faire exactement ce qu'on vous dit de faire.",
   dialogue:'t1', next:{id:'t2', tit:"Défi 2 · Le triage et l'attente", sub:"Raconter la chute à l'infirmière, comprendre la priorité et l'attente."}},

  {id:'t2', no:'2', title:"Défi 2 · Le triage et l'attente", color:'#1D6B8F',
   lead:"Raconter au passé ce qui est arrivé, répondre aux questions du triage et comprendre pourquoi on attend.",
   intro:"Défi 2 — À l'urgence, personne n'entre dans l'ordre d'arrivée. Une infirmière écoute votre récit pendant quatre minutes, prend des mesures, et donne un niveau de priorité de un à cinq. Ce que vous racontez là — ce qui se passait avant, ce qui est arrivé, à quelle heure — pèse dans la décision. Puis vient l'attente, et les questions qu'on ose enfin poser.",
   dialogue:'t2', next:{id:'t3', tit:"Défi 3 · L'étage et le congé", sub:"Comprendre une hospitalisation, préparer le retour à la maison et donner des nouvelles."}},

  {id:'t3', no:'3', title:"Défi 3 · L'étage et le congé", color:'#0D7A6F',
   lead:"Comprendre ce qui s'en vient, poser ses questions avant le jour du départ, et raconter à un proche.",
   intro:"Défi 3 — L'urgence est finie ; l'hospitalisation commence. Une chambre, un étage, des heures de visite, une opération, et une date de sortie que personne ne promet. C'est le moment de poser les questions du retour à la maison — pas le matin du congé, quand tout va vite. Et c'est le moment d'appeler la famille, qui ne sait encore rien.",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"Faire l'appel au 9-1-1, donner des nouvelles au téléphone, puis écrire à la famille."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n5-urgence/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"Mener un appel d'urgence du début à la fin, raconter la nuit en une minute, puis écrire à la famille.",
   intro:"Je me lance — C'est à vous : vous appelez le 9-1-1 pour quelqu'un d'autre, vous racontez au téléphone ce qui est arrivé, puis vous écrivez le message qui donne des nouvelles."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#A5335F', custom:true,
   lead:"Rassembler les mots du doute, de l'appel, du triage et de l'hôpital.",
   intro:"Je retiens des mots — Notez vos mots utiles, révisez avec les cartes mémoire, puis évaluez ce que vous êtes maintenant capable de faire."},
];
