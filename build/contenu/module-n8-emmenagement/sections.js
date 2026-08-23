const SECTIONS = [
  // Cinq sections pour deux défis. Aucune couleur de section n'est verte :
  // la forêt et le teal-vert sont sortis du repérage le 20 août 2026, et
  // `build/couleurs_sections.py --verifier` le vérifie.
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n8-emmenagement/icons/play.svg" alt="">', title:'Je découvre', color:'#1D6B8F',
   lead:"Nommer ce qui a été abîmé, distinguer ce qu'on concède de ce qu'on conteste, et entendre ce que la voix ajoute aux mots.",
   intro:"Amira Benkirane a emménagé ce matin au deuxième étage d'un triplex de la rue Sainte-Ursule, à Trois-Rivières. Le camion est reparti à onze heures. Il reste une rampe d'escalier tordue, deux boîtes de livres noyées par l'averse de dix heures, et le vaisselier de sa mère fendu sur tout un panneau. Le propriétaire de l'entreprise de déménagement, lui, a un contrat dans les mains et une réponse toute prête : soixante cents la livre.",
   dialogue:'prep', next:{id:'t1', tit:'Défi 1 · Ce qui est couvert', sub:"Se faire expliquer une police d'assurance habitation, faire clarifier ce qui est équivoque, et résumer pour vérifier."}},

  {id:'t1', no:'1', title:'Défi 1 · Ce qui est couvert', color:'#B45309',
   lead:"S'informer sur une police d'assurance habitation : les protections, les clauses, les exclusions, et le déroulement d'une réclamation.",
   intro:"Défi 1 — Une police d'assurance se lit rarement avant le sinistre, et c'est presque toujours trop tard. Trois protections qui n'ont rien à voir entre elles, une franchise qui se soustrait, deux façons d'indemniser qui ne donnent pas le même chiffre, des avenants qui ajoutent, des exclusions qui retirent. Le courtier Ghislain Marcotte reprend tout depuis le début — puis explique, d'une traite, comment une réclamation se déroule du premier appel jusqu'à la décision écrite.",
   dialogue:'t1', next:{id:'t2', tit:'Défi 2 · Faire valoir sa réclamation', sub:"Recevoir une décision partagée, accepter ce qui s'accepte, contester le reste et proposer un compromis chiffré."}},

  {id:'t2', no:'2', title:'Défi 2 · Faire valoir sa réclamation', color:'#A5335F',
   lead:"Défendre son point de vue devant l'experte en sinistre : exiger la clause, concéder, contester, appuyer sur une pièce datée, proposer un compromis.",
   intro:"Défi 2 — La lettre est arrivée : un point accepté, deux refusés. Ce qui se joue maintenant n'est plus une question de vocabulaire, c'est une question d'argumentation. Accepter tout de suite ce qui est juste — cela vous rend crédible sur le reste. Exiger la clause exacte de chaque refus. Lire cette clause de près : elle dit « pendant le transport », et le meuble a été fendu dans l'escalier. Puis proposer un chiffre, parce qu'une contestation sans proposition reste sur un bureau.",
   dialogue:'t2', next:{id:'appli', tit:'Je me lance', sub:"Défendre votre réclamation devant l'experte, la porter de vive voix au déménageur, puis l'écrire."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n8-emmenagement/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"Mener la conversation de révision au complet, porter la réclamation de vive voix, puis écrire la lettre.",
   intro:"Je me lance — C'est à vous : vous défendez votre dossier au téléphone devant l'experte en sinistre, vous portez ensuite la même réclamation de vive voix à l'entreprise de déménagement, puis vous écrivez la lettre qui restera."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#1D6B8F', custom:true,
   lead:"Rassembler les mots du sinistre, ceux du contrat et ceux de la contestation.",
   intro:"Je retiens des mots — Notez vos mots utiles, révisez avec les cartes mémoire, puis évaluez ce que vous êtes maintenant capable de faire."},
];
