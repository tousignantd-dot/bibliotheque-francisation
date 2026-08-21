const SECTIONS = [
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n6-recherche/icons/play.svg" alt="">', title:'Je découvre', color:'#A5335F',
   lead:"Nommer un poste et un secteur, dire son expérience, reconnaître les mots du travail.",
   intro:"Marisol Aguirre est arrivée de Colombie il y a deux ans. Là-bas, elle était responsable des stocks dans une entreprise de meubles, pendant six ans. Ici, elle travaille trois jours par semaine dans un entrepôt. Elle pousse la porte du Tremplin-Emploi de Longueuil et demande à voir une conseillère.",
   dialogue:'prep', next:{id:'t1', tit:"Défi 1 · L'offre d'emploi", sub:"Lire une offre détaillée et s'informer sur l'entreprise."}},

  {id:'t1', no:'1', title:"Défi 1 · L'offre d'emploi", color:'#3B49A0',
   lead:"Lire une offre détaillée, distinguer une exigence d'un atout, s'informer sur l'entreprise.",
   intro:"Défi 1 — Une offre d'emploi détaillée, ce n'est pas un titre : c'est quatre parties, toujours les mêmes. L'entreprise, les tâches, les exigences, les conditions. Celui qui sait où regarder décide en deux minutes s'il postule ou non.",
   dialogue:'t1', next:{id:'t2', tit:'Défi 2 · La demande', sub:"Remplir un formulaire détaillé et écrire une lettre de motivation."}},

  {id:'t2', no:'2', title:'Défi 2 · La demande', color:'#B45309',
   lead:"Remplir un formulaire détaillé, décrire ses tâches passées, écrire une lettre de motivation.",
   intro:"Défi 2 — « Décrivez vos fonctions dans votre dernier emploi. » C'est la question qui arrête tout le monde. Répondre « j'ai travaillé dans un entrepôt » est vrai et sans effet ; il faut des verbes d'action, des chiffres et les bonnes formules.",
   dialogue:'t2', next:{id:'t3', tit:"Défi 3 · L'entrevue", sub:"Répondre à des questions ouvertes et offrir ses services."}},

  {id:'t3', no:'3', title:"Défi 3 · L'entrevue", color:'#0D7A6F',
   lead:"Comprendre les questions de l'employeur, développer sa réponse, poser ses propres questions.",
   intro:"Défi 3 — Vingt minutes, une table, et des questions ouvertes : « Parlez-moi de votre expérience. » Une réponse d'une phrase ferme la porte. Une réponse avec un exemple précis l'ouvre. Et à la fin, c'est vous qui posez une question.",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"Passer l'entrevue, offrir ses services, écrire sa demande d'emploi."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n6-recherche/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"Passer une courte entrevue, offrir ses services à voix haute, puis écrire sa demande d'emploi.",
   intro:"Je me lance — C'est à vous : vous passez l'entrevue avec l'assistant, vous offrez vos services à voix haute, puis vous décrivez par écrit vos fonctions et votre expérience."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#A5335F', custom:true,
   lead:"Rassembler les mots de l'offre, de la demande et de l'entrevue.",
   intro:"Je retiens des mots — Notez vos mots utiles, révisez avec les cartes mémoire, puis évaluez ce que vous êtes maintenant capable de faire."},
];
