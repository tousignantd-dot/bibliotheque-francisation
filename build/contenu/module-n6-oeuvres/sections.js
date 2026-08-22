const SECTIONS = [
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n6-oeuvres/icons/play.svg" alt="">', title:'Je découvre', color:'#3B49A0',
   lead:"Reconnaître les trois écrits qui entourent un film — la bande-annonce, la biographie, la critique — et savoir d'avance ce que chacun donne et ce qu'il ne donne pas.",
   intro:"Thérèse Ilboudo a quarante-six ans. Elle est arrivée du Burkina Faso il y a cinq ans et elle travaille comme aide-cuisinière à la résidence Les Quatre-Vents, à Sherbrooke. Depuis cinq ans, elle passe deux fois par jour devant la salle Beauchemin sans y entrer. Ce mercredi soir, elle s'inscrit au ciné-club. Bruno Salvail, qui l'anime depuis neuf ans, lui explique qu'un film n'arrive jamais tout seul : il y a toujours trois textes autour de lui, et ils ne servent pas au même travail.",
   dialogue:'prep', next:{id:'t1', tit:'Défi 1 · Le déroulement du film', sub:"Suivre l'ordre des choses malgré les retours en arrière, et savoir dire ce qui vient avant quoi."}},

  {id:'t1', no:'1', title:'Défi 1 · Le déroulement du film', color:'#1D6B8F',
   lead:"Regarder un film pour en repérer le déroulement : les trois jours d'aujourd'hui, les quatre retours en arrière, et les signaux qui préviennent du changement.",
   intro:"Défi 1 — Un film difficile n'est presque jamais difficile à cause de ses mots : il est difficile parce qu'il ne raconte pas dans l'ordre. « Les Marées de novembre » tient en trois jours, mais il recule quatre fois jusqu'en mil neuf cent soixante-dix-huit. Chaque fois, la question à se poser est la même, et il n'y en a qu'une : est-ce que ça, c'est avant ou après ? Le plus-que-parfait et l'imparfait sont ce qui répond.",
   dialogue:'t1', next:{id:'t2', tit:'Défi 2 · La biographie de la réalisatrice', sub:"Lire un texte suivi, reconnaître le passé simple et retrouver ce que reprend chaque petit mot."}},

  {id:'t2', no:'2', title:'Défi 2 · La biographie de la réalisatrice', color:'#B45309',
   lead:"Lire une biographie du début à la fin : les dates dans l'ordre, les verbes d'un temps qu'on ne parle jamais, et les mots qui renvoient à ce qui précède.",
   intro:"Défi 2 — La feuille verte du ciné-club tient en dix lignes et contient tout ce qui arrête un lecteur du niveau 6. Des verbes qu'on ne dit jamais à voix haute — elle naquit, elle entra, il fut. Un « où » qui parle tantôt d'un lieu, tantôt d'un moment. Et des « le », des « en », des « y » qui obligent à reculer d'une phrase pour savoir de quoi on parle. Lire une biographie, c'est tenir ce fil-là.",
   dialogue:'t2', next:{id:'t3', tit:'Défi 3 · La critique et le résumé', sub:"Lire un avis signé, accorder un point avant de répondre, puis écrire le sien."}},

  {id:'t3', no:'3', title:'Défi 3 · La critique et le résumé', color:'#A5335F',
   lead:"Lire une critique de journal, distinguer le reproche exact de ce qu'on croit qu'il dit, et formuler un avis nuancé qu'on peut discuter.",
   intro:"Défi 3 — Léo Charbonneau n'a pas aimé le film, et il l'écrit dans L'Écho de la Magog. Il ne dit pourtant jamais que c'est un mauvais film : il met un mot entre guillemets, il reproche un moment plutôt qu'un personnage, et il choisit ses adjectifs avec soin — un grand film et un film grand ne veulent pas dire la même chose. Répondre à ça demande la même finesse : accorder ce qui est vrai, puis dire où l'on n'est pas d'accord.",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"Discuter du film avec quelqu'un qui ne l'a pas aimé, en faire le compte rendu, puis écrire au journal."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n6-oeuvres/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"Défendre un avis nuancé devant quelqu'un qui n'est pas d'accord, faire le compte rendu détaillé d'un film à voix haute, puis écrire un résumé en deux paragraphes.",
   intro:"Je me lance — C'est à toi : tu discutes du film avec l'assistant, qui ne l'a pas aimé et qui a de bons arguments ; tu fais ensuite le compte rendu du déroulement à voix haute, sans dévoiler le dénouement ; puis tu écris ton résumé pour L'Écho de la Magog."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#3B49A0', custom:true,
   lead:"Rassembler les mots de la salle, du déroulement, de la fabrication d'un film et du jugement.",
   intro:"Je retiens des mots — Note tes mots utiles, révise avec les cartes mémoire, puis évalue ce que tu es maintenant capable de faire."},
];
