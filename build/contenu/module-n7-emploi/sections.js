const SECTIONS = [
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n7-emploi/icons/play.svg" alt="">', title:'Je découvre', color:'#0D7A6F',
   lead:"Nommer les cinq parties d'un projet, entendre où une phrase continue et où elle finit, lire un ordre du jour.",
   intro:"Aïcha Traoré est coordonnatrice adjointe à l'expédition chez Meubles Rive-du-Nord, une usine de soixante-deux personnes à Terrebonne. Depuis le mois de mars, trois de ses collègues du poste d'emballage se sont fait mal au dos. Elle a tout compté sur une feuille, chez elle, un soir. Sa collègue Thérèse Lapointe, représentante en santé et en sécurité, lui apprend ce matin la différence entre se plaindre et présenter un projet.",
   dialogue:'prep', next:{id:'t1', tit:'Défi 1 · La réunion de production', sub:"Écouter la présentation d'un projet et en retenir les cinq parties."}},

  {id:'t1', no:'1', title:'Défi 1 · La réunion de production', color:'#3B49A0',
   lead:"Suivre une présentation de projet du début à la fin : l'objectif, les étapes, l'échéancier, le budget, les risques.",
   intro:"Défi 1 — Le lundi matin, le chef de production présente son projet de quai pendant douze minutes. Personne ne le répète et il n'y a pas de document. Comprendre une présentation, ce n'est pas retenir chaque mot : c'est reconnaître dans quelle partie on est rendu. « D'abord », « ensuite », « en somme » ne sont pas des mots de remplissage — ce sont les panneaux de la route.",
   dialogue:'t1', next:{id:'t2', tit:'Défi 2 · Le poste 4', sub:"Présenter un problème et son évaluation sommaire à ses collègues."}},

  {id:'t2', no:'2', title:'Défi 2 · Le poste 4', color:'#B45309',
   lead:"Présenter un problème avec des chiffres, en nommer la cause, dire ce qu'il coûte et proposer un correctif daté.",
   intro:"Défi 2 — Deux semaines plus tard, c'est Aïcha qui a quinze minutes. Elle ne va pas se plaindre du poste 4 : elle va l'exposer. Le constat, la cause, la conséquence chiffrée, le correctif, l'échéance. Et quand on veut qu'une chose soit entendue plutôt qu'une autre, on ne parle pas plus fort : on la met en avant dans la phrase.",
   dialogue:'t2', next:{id:'t3', tit:'Défi 3 · Les deux écrits', sub:"La note de service pour l'équipe, la lettre d'affaires pour le fournisseur."}},

  {id:'t3', no:'3', title:'Défi 3 · Les deux écrits', color:'#1D6B8F',
   lead:"Lire et construire une note de service, puis une lettre d'affaires courantes, avec leurs formules et leur mise en page.",
   intro:"Défi 3 — Ce qui a été dit doit maintenant s'écrire, et pas de la même façon selon à qui on écrit. À l'équipe, une note de service : courte, directe, elle dit « vous ». À un fournisseur qu'on ne connaît pas, une lettre d'affaires : elle a sept parties, des formules qui ne se choisissent pas au hasard, et une politesse qui n'est pas de la décoration — c'est de la précision.",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"Défendre son projet, le présenter à voix haute, puis écrire la note de service."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n7-emploi/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"Défendre un projet devant son chef de production, le présenter en cinq temps, puis l'écrire.",
   intro:"Je me lance — C'est à vous : vous défendez votre projet auprès de l'assistant, vous le présentez à voix haute en cinq temps, puis vous écrivez la note de service qui l'annonce à l'équipe."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#A5335F', custom:true,
   lead:"Rassembler les mots du projet, de la réunion, du poste de travail et des écrits d'affaires.",
   intro:"Je retiens des mots — Notez vos mots utiles, révisez avec les cartes mémoire, puis évaluez ce que vous êtes maintenant capable de faire."},
];
