const SECTIONS = [
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n5-degat/icons/play.svg" alt="">', title:'Je découvre', color:'#B45309',
   lead:"Nommer un dégât et ses dommages, dire ce qu'on voit avec précision, entendre le son [o] sous ses trois orthographes.",
   intro:"Mariama Baldé loue un quatre et demie au deuxième étage d'un immeuble de six logements, à Longueuil. Un matin de novembre, elle se lève à six heures et l'eau tombe du plafond de sa chambre. Au-dessus d'elle, chez sa voisine Kim, un chauffe-eau de quinze ans a lâché pendant la nuit. Ce qui commence là ne se réglera pas en un appel : il faudra décrire, prouver, lire un avis, puis demander — et savoir pourquoi on demande.",
   dialogue:'prep', next:{id:'t1', tit:'Défi 1 · Le constat', sub:"Raconter ce qui s'est passé et décrire les dommages, pièce par pièce."}},

  {id:'t1', no:'1', title:'Défi 1 · Le constat', color:'#1D6B8F',
   lead:"Relater un sinistre au passé composé et à l'imparfait, décrire les dommages sans rien oublier.",
   intro:"Défi 1 — Un dégât d'eau se raconte deux fois : à son propriétaire, puis à son assureur. Les deux fois, on demande la même chose — ce qui se passait, ce qui est arrivé, et ce qui est abîmé aujourd'hui. Ce sont trois temps différents dans la même histoire, et c'est là que tout se joue.",
   dialogue:'t1', next:{id:'t2', tit:"Défi 2 · L'avis", sub:"Lire l'avis affiché dans l'entrée et en tirer ce qu'on doit faire."}},

  {id:'t2', no:'2', title:"Défi 2 · L'avis", color:'#3B49A0',
   lead:"Lire un avis officiel jusqu'aux lignes en petit, et comprendre ce qu'il vous oblige à faire.",
   intro:"Défi 2 — Un avis affiché dans une entrée d'immeuble n'est pas écrit comme on parle. « Il est nécessaire que les occupants libèrent l'accès », ça veut dire « tassez vos meubles ». Ces tournures reviennent partout : dans un avis de travaux, une lettre d'école, un papier du gouvernement. Les lire, c'est le savoir-faire de ce défi.",
   dialogue:'t2', next:{id:'t3', tit:'Défi 3 · La réclamation', sub:"Argumenter, demander une compensation et suivre la démarche jusqu'au bout."}},

  {id:'t3', no:'3', title:'Défi 3 · La réclamation', color:'#A5335F',
   lead:"Mettre en avant ce qui compte, dire la cause et la conséquence, demander en justifiant.",
   intro:"Défi 3 — Demander, ce n'est pas se plaindre. Une demande qui aboutit dit trois choses : ce qu'on a perdu, pourquoi c'est arrivé, et ce qu'on veut. Mariama réclame à son assureur ce qui lui appartient, et à son propriétaire trois nuits de loyer. Ce sont deux démarches distinctes, et on ne les mélange pas.",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"Signaler un dégât à voix haute, puis écrire votre demande de réduction de loyer."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n5-degat/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"Mener l'appel des deux côtés, raconter le dégât à voix haute, puis écrire la lettre qui demande.",
   intro:"Je me lance — C'est à vous : vous signalez un dégât, vous le racontez à voix haute, puis vous écrivez au propriétaire pour demander une réduction de loyer."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#0D7A6F', custom:true,
   lead:"Rassembler les mots du dégât, du constat, de l'avis et de la réclamation.",
   intro:"Je retiens des mots — Notez vos mots utiles, révisez avec les cartes mémoire, puis évaluez ce que vous êtes maintenant capable de faire."},
];
