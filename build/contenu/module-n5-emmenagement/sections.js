const SECTIONS = [
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n5-emmenagement/icons/play.svg" alt="">', title:'Je découvre', color:'#A5335F',
   lead:"Nommer ce qu'on fait le jour où on reçoit les clés, entendre la différence entre « déménagement » et « camion ».",
   intro:"Amadou Sow vient de signer un bail pour un quatre et demie au deuxième étage, rue des Peupliers, à Limoilou. Monsieur Rondeau lui a remis les clés ce matin ; le déménagement, lui, est dans six semaines. Entre les deux, il y a tout ce que personne ne lui a expliqué : l'état des lieux, le camion à réserver, l'adresse à changer — et une voisine de soixante-douze ans qui, elle, sait comment l'immeuble fonctionne.",
   dialogue:'prep', next:{id:'t1', tit:'Défi 1 · Le camion', sub:"Réserver un service de déménagement, puis diriger les hommes le jour venu."}},

  {id:'t1', no:'1', title:'Défi 1 · Le camion', color:'#1D6B8F',
   lead:"S'informer par téléphone sur un service de déménagement, comprendre un tarif, puis dire où va chaque chose.",
   intro:"Défi 1 — Un tarif de déménagement n'est jamais un seul chiffre. Il y a l'heure, le minimum, le déplacement, l'homme de plus, l'assurance, le dépôt. Celui qui ne pose pas la deuxième question paie la différence. Et le jour venu, six heures de travail se dirigent en quelques phrases courtes : c'est vous qui savez où va le matelas.",
   dialogue:'t1', next:{id:'t2', tit:'Défi 2 · La nouvelle adresse', sub:"Ouvrir ses comptes, faire brancher ses services et prévenir tout le monde."}},

  {id:'t2', no:'2', title:'Défi 2 · La nouvelle adresse', color:'#B45309',
   lead:"Ouvrir un compte à son nom, faire brancher ses services et prévenir les organismes du changement d'adresse.",
   intro:"Défi 2 — Une adresse, ce n'est pas une ligne sur une enveloppe : c'est une douzaine d'endroits où votre nom est écrit. L'électricité, Internet, la banque, l'école, la SAAQ, la RAMQ. Ceux qui en oublient un ne s'en aperçoivent pas tout de suite — ils s'en aperçoivent chez le médecin, ou quand une facture arrive chez l'ancien locataire.",
   dialogue:'t2', next:{id:'t3', tit:'Défi 3 · Les voisins', sub:"Se présenter, s'excuser du bruit, comprendre les usages de l'immeuble."}},

  {id:'t3', no:'3', title:'Défi 3 · Les voisins', color:'#0D7A6F',
   lead:"Raconter sa journée de déménagement, demander comment ça fonctionne dans l'immeuble, accepter ou refuser une invitation.",
   intro:"Défi 3 — Un immeuble a des règles écrites dans le bail, et des usages qui ne sont écrits nulle part : l'heure de la salle de lavage, le jour du bac brun, ce qu'on fait quand la ville annonce le déneigement. Ces choses-là s'apprennent en parlant à quelqu'un — et la conversation commence souvent par des excuses pour le bruit de la veille.",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"Réserver un déménagement au téléphone, puis écrire au propriétaire."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n5-emmenagement/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"Mener l'appel au complet, se présenter à voix haute à une voisine, puis écrire au propriétaire.",
   intro:"Je me lance — C'est à vous : vous téléphonez à une compagnie de déménagement, vous vous présentez à votre nouvelle voisine, puis vous écrivez au propriétaire ce que l'état des lieux a montré."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#A5335F', custom:true,
   lead:"Rassembler les mots des clés, du camion, de l'adresse et de l'immeuble.",
   intro:"Je retiens des mots — Notez vos mots utiles, révisez avec les cartes mémoire, puis évaluez ce que vous êtes maintenant capable de faire."},
];
