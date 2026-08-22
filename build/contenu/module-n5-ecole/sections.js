const SECTIONS = [
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n5-ecole/icons/play.svg" alt="">', title:'Je découvre', color:'#A5335F',
   lead:"Savoir à qui s'adresser dans un centre, et nommer les gens, les lieux et les papiers du dossier d'un élève.",
   intro:"Amelia Dumitrescu a trente-huit ans. Elle est arrivée de Roumanie il y a deux ans et elle suit le cours de francisation de niveau 5 au Centre d'éducation des adultes des Trois-Ponts, à Trois-Rivières. Depuis trois jours, elle a une nouvelle qu'elle n'ose annoncer à personne : sa mère sera opérée à Bucarest au mois de mars, et il faudra qu'elle parte. Elle a compris le mot « absence ». Ce qu'elle ne sait pas, c'est à quelle porte frapper.",
   dialogue:'prep', next:{id:'t1', tit:"Défi 1 · Prévenir de son absence", sub:"Annoncer une absence prévue au comptoir, et poser ses questions sans les jeter en vrac."}},

  {id:'t1', no:'1', title:"Défi 1 · Prévenir de son absence", color:'#1D6B8F',
   lead:"Exposer une absence prévue au secrétariat : les dates d'abord, le motif ensuite, puis ce qu'on fera au retour.",
   intro:"Défi 1 — Au comptoir, on a environ deux minutes. Une absence de trois semaines s'annonce donc dans un ordre précis : qui vous êtes, à partir de quand, jusqu'à quand, et pourquoi. Le reste, ce sont vos questions — et une question polie ne se pose pas comme un interrogatoire. « Je voudrais savoir si… », « Pourriez-vous me dire quand… » : la question se glisse dans une phrase, et c'est là tout le défi.",
   dialogue:'t1', next:{id:'t2', tit:"Défi 2 · Lire l'avis du centre", sub:"Trouver l'échéance dans un avis officiel et comprendre ce que chaque paragraphe demande."}},

  {id:'t2', no:'2', title:"Défi 2 · Lire l'avis du centre", color:'#B45309',
   lead:"Lire un avis officiel jusqu'au bout : repérer les dates, distinguer une échéance d'un rappel, et savoir à quoi renvoie « celui-ci ».",
   intro:"Défi 2 — Trois jours plus tard, un avis arrive dans la boîte de courriels d'Amelia. Une page, quatre paragraphes, trois dates — et une seule de ces dates est une échéance. Un avis officiel n'explique rien : il annonce, il date, et il attend une signature. Il faut donc savoir lire les petits mots qui portent le temps, et retrouver de quoi parle « ce document », « celui-ci », « cette demande ».",
   dialogue:'t2', next:{id:'t3', tit:'Défi 3 · Demander un changement', sub:"Expliquer ce qui vous bloque et demander un changement, de vive voix puis par écrit."}},

  {id:'t3', no:'3', title:'Défi 3 · Demander un changement', color:'#3B49A0',
   lead:"Demander un transfert ou une attestation : dire ce qui bloque, dire ce qu'il faut, et l'écrire.",
   intro:"Défi 3 — Amelia est revenue, et sa vie a changé pendant qu'elle était partie : elle travaille le matin. Le cours de jour ne tient plus. Demander un changement, ce n'est pas se plaindre — c'est nommer ce qui bloque, proposer une solution, et accepter ce que la solution coûte. Puis l'écrire, parce qu'un dossier ne se souvient d'aucune conversation.",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"Régler votre affaire au comptoir, laisser un message au secrétariat, puis écrire votre demande."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n5-ecole/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"Exposer votre situation au personnel du centre, à l'oral puis par écrit.",
   intro:"Je me lance — C'est à vous : vous réglez d'abord votre affaire au comptoir avec l'assistant, qui joue le secrétariat ; vous laissez ensuite un message dans la boîte vocale du centre ; puis vous écrivez votre demande à la conseillère."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#A5335F', custom:true,
   lead:"Rassembler les mots du centre, de l'absence, de l'avis officiel et du changement de dossier.",
   intro:"Je retiens des mots — Notez vos mots utiles, révisez avec les cartes mémoire, puis évaluez ce que vous êtes maintenant capable de faire."},
];
