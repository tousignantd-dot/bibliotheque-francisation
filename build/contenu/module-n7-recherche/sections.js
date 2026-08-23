const SECTIONS = [
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n7-recherche/icons/play.svg" alt="">', title:'Je découvre', color:'#0D7A6F',
   lead:"Nommer les outils de la recherche d'emploi, comprendre ce qu'un avis d'évaluation dit et ne dit pas, entendre le « e » qui tombe.",
   intro:"Hafida Zerouali est préposée à l'entretien dans un centre de la petite enfance de Longueuil. En Algérie, elle a été technicienne de laboratoire pendant neuf ans. Depuis janvier, elle a envoyé trente-quatre candidatures et reçu trois refus. Ce matin, elle pousse pour la première fois la porte de la salle multiservice d'un bureau de Services Québec, où Sylvain Desbiens lui montre que le Québec n'est pas un marché du travail, mais dix-sept.",
   dialogue:'prep', next:{id:'t1', tit:'Défi 1 · Où travaille-t-on, là-bas ?', sub:"Écouter un reportage économique en trois fois et en retenir les chiffres."}},

  {id:'t1', no:'1', title:'Défi 1 · Où travaille-t-on, là-bas ?', color:'#3B49A0',
   lead:"S'informer sur les activités économiques d'une région du Québec en écoutant un reportage long.",
   intro:"Défi 1 — Une émission de radio sur l'économie d'une région ne se comprend pas d'un seul coup : elle est pleine de pourcentages, de milliards et de comparaisons. On l'écoute une première fois pour le sujet, une deuxième pour les chiffres, une troisième pour ce qui se cache derrière — et surtout on apprend à suivre les mots qui font tourner un long discours : « quant à », « en ce qui concerne », « en somme ».",
   dialogue:'t1', next:{id:'t2', tit:'Défi 2 · Lire un portrait de région', sub:"Lire un portrait économique écrit et le comparer à un autre."}},

  {id:'t2', no:'2', title:'Défi 2 · Lire un portrait de région', color:'#B45309',
   lead:"S'informer sur les activités économiques des régions du Québec en lisant, et comparer deux territoires.",
   intro:"Défi 2 — Un portrait économique écrit est court, froid et difficile pour une raison précise : il nomme des activités au lieu de raconter ce que les gens font. « La transformation des ressources naturelles » plutôt que « on transforme le bois ». Il dit « ils » sans dire qui, et « a été agrandie » sans dire par qui. Savoir lire ces trois procédés, c'est pouvoir comparer deux régions en une heure.",
   dialogue:'t2', next:{id:'t3', tit:'Défi 3 · Mon curriculum vitæ parle à cette région', sub:"Retailler son curriculum vitæ et écrire sa lettre d'accompagnement."}},

  {id:'t3', no:'3', title:'Défi 3 · Mon curriculum vitæ parle à cette région', color:'#A5335F',
   lead:"Choisir, organiser et mettre en valeur les informations d'un curriculum vitæ, puis rédiger une lettre d'accompagnement.",
   intro:"Défi 3 — Un curriculum vitæ ne se rédige pas une fois pour toutes : il se retaille pour chaque offre. La personne qui reçoit quarante dossiers ne lit d'abord que les premières lignes de chacun. Ce défi apprend à ranger son expérience dans l'ordre de l'utilité, à mettre en avant ce qui compte avec « c'est… qui » et « ce que… c'est », et à demander poliment ce qu'on veut vraiment.",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"Téléphoner à l'employeur, comparer deux régions à voix haute, écrire sa lettre."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n7-recherche/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"S'informer par téléphone avant de postuler, exposer les avantages et les inconvénients de deux régions, rédiger sa lettre d'accompagnement.",
   intro:"Je me lance — C'est à vous : vous appelez l'employeur pour poser vos questions, vous comparez deux régions à voix haute devant la classe, puis vous écrivez la lettre qui accompagnera votre curriculum vitæ."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#0D7A6F', custom:true,
   lead:"Rassembler les mots de la recherche d'emploi, de l'économie régionale et de la candidature écrite.",
   intro:"Je retiens des mots — Notez vos mots utiles, révisez avec les cartes mémoire, puis évaluez ce que vous êtes maintenant capable de faire."},
];
