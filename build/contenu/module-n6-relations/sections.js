const SECTIONS = [
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n6-relations/icons/play.svg" alt="">', title:'Je découvre', color:'#A5335F',
   lead:"Ouvrir un long courriel de nouvelles sans s'y perdre : reconnaître ses parties, nommer les évènements qu'il annonce, et retrouver à quoi renvoient les petits mots.",
   intro:"Marisol Quintanilla a quarante et un ans. Elle est arrivée du Salvador il y a sept ans et elle est aide-pâtissière à la boulangerie Trottier, rue Girouard, à Saint-Hyacinthe. Ce matin, elle a reçu un courriel de quatre paragraphes d'Ousmane Diallo, un ami de sa classe de francisation parti vivre à Rouyn-Noranda il y a deux ans. Elle l'a lu deux fois et elle n'est toujours pas certaine de ce qu'elle a compris. Son voisin Ghislain Bourbeau lui montre par où on entre dans un texte long.",
   dialogue:'prep', next:{id:'t1', tit:"Défi 1 · Le courriel d'Ousmane", sub:"Suivre quatre paragraphes de nouvelles et remettre les évènements dans leur ordre."}},

  {id:'t1', no:'1', title:"Défi 1 · Le courriel d'Ousmane", color:'#1D6B8F',
   lead:"Recevoir des nouvelles : comprendre un courriel long, savoir ce que reprennent « le », « en » et « y », et reconnaître ce qui était déjà arrivé avant le reste.",
   intro:"Défi 1 — Deux ans de vie tiennent dans quatre paragraphes : une naissance, un déménagement, un accident, des funérailles, un mariage à venir. Rien n'y est difficile mot à mot. Ce qui est difficile, c'est que tout s'y tient : « on l'avait déjà vendue » renvoie à une maison nommée dix lignes plus haut, et « elle était arrivée depuis un mois » place une date que personne n'a écrite. Perdre le fil, ce n'est pas manquer un mot : c'est perdre à quoi il renvoie.",
   dialogue:'t1', next:{id:'t2', tit:'Défi 2 · La personne à reconnaître', sub:"Décrire quelqu'un assez précisément pour qu'un autre le retrouve dans une foule."}},

  {id:'t2', no:'2', title:'Défi 2 · La personne à reconnaître', color:'#B45309',
   lead:"Décrire quelqu'un : la silhouette d'abord, le visage ensuite, le signe particulier en dernier — et corriger ce qu'on a mal dit sans tout reprendre.",
   intro:"Défi 2 — Décrire quelqu'un pour le plaisir, c'est facile. Le décrire pour qu'un inconnu le reconnaisse dans un terminus un vendredi après-midi, c'est un autre métier : il faut choisir ce qui se voit de loin, donner le détail dans un ordre utile, et accepter d'être repris. « Une grande valise » ou « une grande femme » : le même adjectif, deux personnes différentes à chercher.",
   dialogue:'t2', next:{id:'t3', tit:"Défi 3 · L'article qu'on transmet", sub:"Lire un article d'intérêt général, puis en informer quelqu'un par courriel."}},

  {id:'t3', no:'3', title:"Défi 3 · L'article qu'on transmet", color:'#3B49A0',
   lead:"Lire un article de journal de quartier, reconnaître le temps du récit ancien, suivre ses connecteurs, et séparer ce que le journal dit de ce qu'on en pense.",
   intro:"Défi 3 — Un journal de quartier raconte une histoire de vingt ans dans un temps que personne ne parle : « tout commença », « elles se réunirent ». Il cite les gens entre guillemets, il en met d'autres autour d'un seul mot pour dire qu'il ne le prend pas à son compte, et il enchaîne ses idées avec cinq ou six petits mots qu'on saute en lisant vite. Transmettre cet article à quelqu'un, c'est le résumer sans le déformer — puis dire ce qu'on en pense, à part.",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"Décrire une personne à l'assistant, l'enregistrer, puis écrire ton courriel."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n6-relations/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"Faire reconnaître quelqu'un à l'assistant, décrire une personne à voix haute, puis écrire un courriel qui donne des nouvelles et transmet un article.",
   intro:"Je me lance — C'est à toi : tu décris quelqu'un à l'assistant, qui va le chercher au terminus et qui te demande des précisions ; tu fais ensuite la même description à voix haute ; puis tu écris ton courriel."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#A5335F', custom:true,
   lead:"Rassembler les mots des évènements de la vie, de la description physique et de l'organisme du quartier.",
   intro:"Je retiens des mots — Note tes mots utiles, révise avec les cartes mémoire, puis évalue ce que tu es maintenant capable de faire."},
];
