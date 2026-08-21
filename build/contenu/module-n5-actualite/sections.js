const SECTIONS = [
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n5-actualite/icons/play.svg" alt="">', title:'Je découvre', color:'#A5335F',
   lead:"Reconnaître un fait divers dans un journal local et retrouver, en le lisant, ce qui est arrivé, où et quand.",
   intro:"Marisol Ferreira a quarante et un ans. Elle est arrivée du Portugal il y a quatre ans et elle prépare les salades à la cafétéria d'un cégep de Sherbrooke. Tous les mardis, l'hebdomadaire du secteur, « L'Écho des Cantons », traîne sur la table de la salle des employés. Elle a commencé à le lire pour pratiquer son français ; maintenant, c'est Sylvain Ouellet, le cuisinier, qui attend qu'elle lui raconte.",
   dialogue:'prep', next:{id:'t1', tit:"Défi 1 · Ce qui est arrivé", sub:"Raconter un évènement dans l'ordre, avec le passé composé et l'imparfait."}},

  {id:'t1', no:'1', title:"Défi 1 · Ce qui est arrivé", color:'#1D6B8F',
   lead:"Raconter un évènement à quelqu'un qui ne l'a pas lu : ce qui est arrivé d'abord, puis où, quand et comment.",
   intro:"Défi 1 — Un immeuble a brûlé pendant la nuit, à quatre rues d'ici. Sylvain n'a rien entendu et n'a rien lu. Pour qu'il comprenne, il ne suffit pas de connaître les faits : il faut les mettre en ordre. Ce qui bouge se dit au passé composé, ce qui était là autour se dit à l'imparfait, et les deux ne se remplacent pas.",
   dialogue:'t1', next:{id:'t2', tit:"Défi 2 · Ce que les gens ont dit", sub:"Rapporter au présent une parole lue dans le journal, en disant de qui elle vient."}},

  {id:'t2', no:'2', title:"Défi 2 · Ce que les gens ont dit", color:'#B45309',
   lead:"Rapporter au présent ce qu'une personne a déclaré, en nommant qui parle et en gardant le bon pronom.",
   intro:"Défi 2 — Un fait divers n'est jamais qu'une suite d'évènements : il fait parler du monde. La Ville affirme une chose, une résidente en demande une autre, les pompiers en expliquent une troisième. Répéter tout ça sans dire qui l'a dit, c'est transformer une nouvelle en rumeur. Ce défi apprend à rapporter la parole des autres et à la remettre à son propriétaire.",
   dialogue:'t2', next:{id:'t3', tit:"Défi 3 · Ce que j'en pense", sub:"Donner son avis, le présenter comme un avis et le défendre poliment."}},

  {id:'t3', no:'3', title:"Défi 3 · Ce que j'en pense", color:'#3B49A0',
   lead:"Dire ce qu'on pense d'une nouvelle, le distinguer des faits et répondre à quelqu'un qui pense autrement.",
   intro:"Défi 3 — Une fois la nouvelle racontée, il reste la vraie conversation : ce que ça vous fait. Et là, deux choses comptent. Annoncer son avis comme un avis, pour que personne ne le prenne pour un fait. Et savoir répondre quand l'autre n'est pas d'accord — en lui accordant d'abord ce qu'il a de juste, puis en disant pourquoi on pense autrement.",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"Raconter une nouvelle de vive voix, puis l'écrire pour quelqu'un d'autre."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n5-actualite/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"Raconter un fait divers à quelqu'un qui ne l'a pas lu, puis l'écrire dans un courriel.",
   intro:"Je me lance — C'est à toi : tu racontes ta nouvelle à l'assistant, qui n'a rien lu et qui va te faire préciser ; tu l'enregistres ensuite à voix haute ; puis tu l'écris à quelqu'un qui est loin."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#A5335F', custom:true,
   lead:"Rassembler les mots du journal, du sinistre, de l'enquête et du vol.",
   intro:"Je retiens des mots — Note tes mots utiles, révise avec les cartes mémoire, puis évalue ce que tu es maintenant capable de faire."},
];
