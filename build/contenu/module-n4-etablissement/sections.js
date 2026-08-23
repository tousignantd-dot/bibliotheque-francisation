const SECTIONS = [
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n4-etablissement/icons/play.svg" alt="">', title:'Je découvre', color:'#A5335F',
   lead:"Nommer ce qu'il y a au bout du fil — la ligne, le clavier, le répondeur, la boîte vocale — et dire ce qui empêche de venir.",
   intro:"Nourhane Ouazzani a trente-six ans. Elle est arrivée du Maroc il y a un an et elle suit la francisation à temps plein, groupe 6, au Centre d'éducation des adultes de la Pointe-aux-Ormes, à Laval. Dimanche soir, son fils Ilyes, cinq ans, se réveille avec une otite. Demain matin, elle sera à la clinique et pas en classe. Le bureau du centre n'ouvre qu'à huit heures, et le cours commence à huit heures aussi. Personne ne décrochera.",
   dialogue:'prep', next:{id:'t1', tit:'Défi 1 · Le répondeur du centre', sub:"Traverser un menu automatisé, puis laisser un message que personne ne pourra faire répéter."}},

  {id:'t1', no:'1', title:'Défi 1 · Le répondeur du centre', color:'#1D6B8F',
   lead:"Comprendre un menu téléphonique à l'impératif, puis laisser un message complet en une minute : qui, quand, pourquoi, et quoi ensuite.",
   intro:"Défi 1 — Sept heures dix. Nourhane compose le 450 555-0180 et tombe sur une voix enregistrée qui donne cinq consignes à l'impératif : appuyez, composez, laissez, ne faites rien, raccrochez. Puis c'est à elle. Une minute, personne en face, aucune question possible. Un message qui commence par la raison et finit par le nom ne sert à rien : à huit heures, la personne qui l'écoute aura déjà appuyé sur « suivant ».",
   dialogue:'t1', next:{id:'t2', tit:"Défi 2 · Les messages qu'on me laisse", sub:"Écouter trois messages jusqu'au bout et noter ce qu'il faut faire, sans pouvoir demander de répéter."}},

  {id:'t2', no:'2', title:"Défi 2 · Les messages qu'on me laisse", color:'#B45309',
   lead:"Écouter un message téléphonique et en tirer trois choses : qui appelle, pourquoi, et ce qu'on attend de vous.",
   intro:"Défi 2 — Le soir venu, c'est le téléphone de Nourhane qui clignote : trois messages. Le secrétariat, l'enseignant, puis le secrétariat encore. Aucun des trois ne se répète, aucun ne pose de question. Écouter un message, ce n'est pas tout comprendre : c'est attraper le nom, la raison et la chose à faire — et savoir laquelle des trois manque, pour rappeler.",
   dialogue:'t2', next:{id:'t3', tit:'Défi 3 · La note à remettre', sub:"Écrire cinq lignes datées et signées, et savoir ce qui manque avant de les remettre."}},

  {id:'t3', no:'3', title:'Défi 3 · La note à remettre', color:'#3B49A0',
   lead:"Écrire une note courte qui justifie une absence : la date, à qui, le motif au passé composé, ce qu'on fera au futur, la signature.",
   intro:"Défi 3 — Un message enregistré s'efface ; une note reste. Le centre demande donc un papier, cinq lignes, daté et signé. Ce sont les cinq lignes les plus faciles à rater du module : on oublie à qui on écrit, on met le motif au présent, on signe sans mettre son groupe. Nourhane la lit à voix haute devant monsieur Corriveau — et c'est en la lisant qu'elle entend ce qui cloche.",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"Téléphoner au secrétariat, laisser votre message dans la boîte vocale, puis écrire votre note."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n4-etablissement/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"Justifier votre retard, votre absence ou votre abandon — au téléphone, dans une boîte vocale, puis par écrit.",
   intro:"Je me lance — C'est à vous : vous téléphonez d'abord au secrétariat avec l'assistant, qui décroche cette fois-là ; vous laissez ensuite votre propre message dans la boîte vocale du centre ; puis vous écrivez la note que vous remettrez au comptoir."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#A5335F', custom:true,
   lead:"Rassembler les mots du téléphone, ceux des motifs et ceux de la note écrite.",
   intro:"Je retiens des mots — Notez vos mots utiles, révisez avec les cartes mémoire, puis évaluez ce que vous êtes maintenant capable de faire."},
];
