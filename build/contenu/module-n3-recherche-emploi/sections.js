const SECTIONS = [
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n3-recherche-emploi/icons/play.svg" alt="">', title:'Je découvre', color:'#1D6B8F',
   lead:"Comprendre une affiche d'embauche et savoir ce qu'on va dire en entrant.",
   intro:"Fanta Traoré a trente et un ans. Elle est arrivée de Conakry il y a un an et elle habite dans Saint-Michel, à Montréal. L'après-midi, elle est à l'école de français ; le matin, elle est libre, et elle veut travailler. Elle n'a jamais eu d'emploi au Québec. Ce matin-là, elle marche rue Jarry avec Sylvie Ouimet, l'agente du centre d'emploi du quartier, et un papier rouge est collé dans la vitrine de la boulangerie.",
   dialogue:'prep', next:{id:'t1', tit:"Défi 1 · Est-ce que vous engagez ?", sub:"Entrer, offrir ses services de vive voix et laisser son nom."}},

  {id:'t1', no:'1', title:"Défi 1 · Est-ce que vous engagez ?", color:'#B45309',
   lead:"Offrir ses services en personne, dire ce qu'on sait faire et laisser ses coordonnées.",
   intro:"Défi 1 — Une affiche dans une vitrine ne se répond pas par écrit : on pousse la porte. Ce défi apprend les quatre choses qu'on dit en entrant — pourquoi je viens, ce que je sais faire, quand je suis libre, où on me joint — et les trois façons de poser la question qui compte : « Est-ce que vous engagez ? »",
   dialogue:'t1', next:{id:'t2', tit:"Défi 2 · L'annonce dit quoi ?", sub:"Lire une offre d'emploi simple et comprendre ce qu'elle demande."}},

  {id:'t2', no:'2', title:"Défi 2 · L'annonce dit quoi ?", color:'#A5335F',
   lead:"Lire une offre d'emploi simple : le poste, l'horaire, le salaire, à qui parler.",
   intro:"Défi 2 — Une offre d'emploi tient en huit lignes, et chaque ligne répond à une question. Ce défi apprend à les lire dans l'ordre : quel poste, combien d'heures, quels jours, combien de l'heure, quelle expérience il faut, et à qui il faut s'adresser. Une offre qu'on lit mal, c'est un matin perdu.",
   dialogue:'t2', next:{id:'t3', tit:'Défi 3 · Mon nom sur le papier', sub:"Remplir un formulaire de demande d'emploi et écrire sa petite annonce."}},

  {id:'t3', no:'3', title:'Défi 3 · Mon nom sur le papier', color:'#0D7A6F',
   lead:"Remplir un formulaire simple de demande d'emploi et rédiger une courte annonce.",
   intro:"Défi 3 — Il reste toujours un papier à remplir, et il se remplit d'une seule façon : en lettres moulées, case par case, sans en sauter une. Ce défi apprend à lire les consignes du formulaire — écrivez, cochez, signez, datez —, à mettre la bonne réponse dans la bonne case, puis à écrire soi-même la petite annonce qu'on punaise pour offrir ses services.",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"Offrir tes services à voix haute, puis écrire ta propre annonce."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n3-recherche-emploi/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"Entrer quelque part, offrir tes services à voix haute, puis écrire ton annonce.",
   intro:"Je me lance — C'est à toi : tu pousses la porte, tu demandes si ça engage, tu dis ce que tu sais faire et quand tu es libre, tu laisses ton nom et ton numéro. Ensuite, tu écris la petite annonce que tu vas punaiser au babillard de ton quartier."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#1D6B8F', custom:true,
   lead:"Rassembler les mots de l'affiche, de l'offre d'emploi, de l'horaire et du formulaire.",
   intro:"Je retiens des mots — Note tes mots utiles, révise avec les cartes mémoire, puis évalue ce que tu es maintenant capable de faire."},
];
