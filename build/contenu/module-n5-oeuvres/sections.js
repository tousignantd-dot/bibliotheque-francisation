const SECTIONS = [
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n5-oeuvres/icons/play.svg" alt="">', title:'Je découvre', color:'#A5335F',
   lead:"Nommer une œuvre et son support — un roman, un film, une série, une bande dessinée, une chanson — et comprendre ce qu'on attend de vous quand on vous demande d'en parler.",
   intro:"Mai Trinh a trente-huit ans. Elle est arrivée du Viêt Nam il y a trois ans et elle travaille de nuit dans une buanderie industrielle. Le jour, elle dort mal, alors elle lit. Un mardi, en rapportant ses livres à la bibliothèque de quartier, elle s'arrête devant une affiche collée sur la porte de la petite salle du fond : « Club du jeudi — 18 h 30. Apportez une œuvre que vous avez aimée. » Elle relit trois fois. Deux minutes toute seule devant des inconnus, en français : c'est exactement ce qui lui fait peur, et exactement ce dont elle a besoin.",
   dialogue:'prep', next:{id:'t1', tit:"Défi 1 · Ce que raconte l'histoire", sub:"Raconter une intrigue au présent, dans l'ordre, sans jamais dévoiler la fin."}},

  {id:'t1', no:'1', title:"Défi 1 · Ce que raconte l'histoire", color:'#1D6B8F',
   lead:"Raconter au présent ce qui arrive dans une œuvre : où ça se passe, qui est le personnage principal, ce qui le met en marche — et s'arrêter avant le dénouement.",
   intro:"Défi 1 — Raconter une histoire à quelqu'un qui ne la connaît pas, ce n'est pas la résumer : c'est en donner assez pour donner envie, et pas une phrase de plus. Le présent place l'autre à l'intérieur de l'histoire — « elle arrive, elle ouvre la maison, elle trouve une boîte » —, les relatives permettent de tout dire d'un personnage sans faire quatre phrases, et la règle du club tient en six mots : on ne raconte pas la fin.",
   dialogue:'t1', next:{id:'t2', tit:'Défi 2 · Lire une bande dessinée', sub:"Comprendre une planche, ses cases et ses bulles, et en parler sans se répéter."}},

  {id:'t2', no:'2', title:'Défi 2 · Lire une bande dessinée', color:'#B45309',
   lead:"Lire une planche de bande dessinée — l'ordre des cases, la pointe des bulles, les onomatopées — et en parler en reprenant l'œuvre sans répéter le même mot.",
   intro:"Défi 2 — Une bande dessinée ne se lit pas comme un roman : l'histoire est partagée entre ce qui est dessiné et ce qui est écrit, et il faut savoir dans quel ordre passer d'un carré à l'autre. Ce défi donne les mots du métier — une case, une bulle, une planche, une onomatopée, un album, un tome — puis apprend à reprendre l'œuvre autrement à chaque phrase : celui que j'ai lu, cet album-là, cette histoire, ce premier tome.",
   dialogue:'t2', next:{id:'t3', tit:"Défi 3 · Dire ce qu'on en pense", sub:"Donner son appréciation avec un adjectif précis, la justifier, et tenir devant un désaccord."}},

  {id:'t3', no:'3', title:"Défi 3 · Dire ce qu'on en pense", color:'#3B49A0',
   lead:"Dire ce qu'on a aimé d'une œuvre avec un adjectif précis, mettre son avis en avant, le justifier, et répondre à quelqu'un qui pense autrement.",
   intro:"Défi 3 — C'est ici que le module se joue. « C'est bon » n'apprend rien à personne : il faut un adjectif qui dise quoi — émouvant, lent, prévisible, drôle, dur —, une raison derrière, et une façon de mettre son avis en avant sans le faire passer pour un fait. Et comme quelqu'un finira par n'être pas d'accord, il faut aussi savoir lui accorder ce qu'il a de juste avant de dire pourquoi on pense autrement.",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"Présenter une œuvre pendant deux minutes, puis l'écrire pour le babillard."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n5-oeuvres/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"Parler d'une œuvre à quelqu'un qui ne la connaît pas, puis la recommander par écrit.",
   intro:"Je me lance — C'est à vous : vous parlez de votre œuvre à l'assistant, qui ne la connaît pas et qui vous fera préciser ; vous enregistrez ensuite votre présentation de deux minutes ; puis vous l'écrivez pour le babillard des coups de cœur, à l'entrée de la bibliothèque."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#A5335F', custom:true,
   lead:"Rassembler les mots de l'œuvre, de l'histoire, de la bande dessinée et de l'appréciation.",
   intro:"Je retiens des mots — Notez vos mots utiles, révisez avec les cartes mémoire, puis évaluez ce que vous êtes maintenant capable de faire."},
];
