const SECTIONS = [
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n8-emploi/icons/play.svg" alt="">', title:'Je découvre', color:'#A5335F',
   lead:"Comprendre une description de tâches détaillée, distinguer le ton du bureau de celui de la machine à café.",
   intro:"Nadia Kessab est adjointe administrative chez Portes et fenêtres Valmont, une PME de quarante employés à Laval. Elle est en poste depuis huit mois. Ce matin, sa superviseure Manon Trépanier lui reprend sa description de tâches au complet — quatre blocs, avec les heures et les montants. À la pause, Yves Boudreault lui explique ce qui n'est écrit nulle part.",
   dialogue:'prep', next:{id:'t1', tit:'Défi 1 · Une erreur sur la paie', sub:"Exposer un problème administratif, citer la norme, obtenir un engagement daté."}},

  {id:'t1', no:'1', title:'Défi 1 · Une erreur sur la paie', color:'#3B49A0',
   lead:"Régler un problème administratif au téléphone, puis le confirmer par une lettre d'affaires.",
   intro:"Défi 1 — Quarante-quatre heures travaillées, quarante-quatre heures payées au taux simple. Nadia a raison sur le fond ; encore faut-il le dire de manière à obtenir une correction plutôt qu'une discussion. Exposer les faits avec des dates, citer la norme sans accuser personne, et repartir avec une date : c'est tout le défi.",
   dialogue:'t1', next:{id:'t2', tit:'Défi 2 · La réunion', sub:"Faire valoir son point de vue, nuancer, proposer un compromis."}},

  {id:'t2', no:'2', title:'Défi 2 · La réunion', color:'#B45309',
   lead:"Intervenir dans une réunion de décision, justifier son avis, proposer un compromis, puis rédiger le compte rendu.",
   intro:"Défi 2 — Deux fournisseurs, quarante mille dollars d'écart, et une donnée que personne n'avait regardée. Dans une réunion de décision, celui qui parle le plus fort ne gagne pas : celui qui résume, qui chiffre et qui nuance, oui. Ensuite, il faut écrire le compte rendu — trois décisions, trois responsables, trois dates.",
   dialogue:'t2', next:{id:'t3', tit:'Défi 3 · Se perfectionner', sub:"S'informer sur la formation continue et demander un congé de formation."}},

  {id:'t3', no:'3', title:'Défi 3 · Se perfectionner', color:'#0D7A6F',
   lead:"S'informer sur les possibilités de perfectionnement, lire un texte informatif, formuler une demande à son employeur.",
   intro:"Défi 3 — « J'aimerais suivre un cours » n'obtient rien. « Voici ce que ça coûte, voici ce que ça vous rapporte, voici comment mon travail se fait quand même » obtient une réponse. Nadia rencontre une conseillère en formation, lit ce qui existe, puis écrit à sa superviseure.",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"Régler le problème au téléphone, intervenir en réunion, écrire sa demande."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n8-emploi/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"Régler un problème avec l'assistant, faire valoir son point de vue à voix haute, puis écrire sa demande de formation.",
   intro:"Je me lance — C'est à vous : vous réglez le problème au téléphone avec l'assistant, vous intervenez à voix haute dans la réunion, puis vous écrivez votre demande de congé de formation."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#A5335F', custom:true,
   lead:"Rassembler les mots des tâches, de la paie, de la réunion et de la formation.",
   intro:"Je retiens des mots — Notez vos mots utiles, révisez avec les cartes mémoire, puis évaluez ce que vous êtes maintenant capable de faire."},
];
