const SECTIONS = [
  // La couleur d'une section n'est pas celle du module : chacune porte celle
  // de son travail, comme dans les séances. L'acier du niveau 6 tient
  // l'en-tête, pas les onglets.
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n6-sante/icons/play.svg" alt="">', title:'Je découvre', color:'#A5335F',
   lead:"Se retrouver dans un rendez-vous en spécialité : où l'on entre, ce qu'on présente, ce qu'on apporte, et ce qui vous attend à la sortie.",
   intro:"Leyla Demirci a quarante et un ans. Elle est arrivée de Turquie il y a cinq ans et elle est aide à domicile à Rimouski : elle entre chez les gens à sept heures du matin, sept jours sur quatorze. Depuis février, elle est fatiguée d'une fatigue qui ne part pas. Son médecin de famille a envoyé une demande de consultation en médecine interne au mois d'avril ; l'appel est venu en octobre, et le rendez-vous est ce matin, à neuf heures quarante. Au comptoir de la clinique externe, Mariette Pouliot lui apprend en trois minutes ce que sept mois d'attente ne lui avaient pas appris : ce qu'il faut avoir dans son sac, et pourquoi on n'ouvre pas son enveloppe chez soi.",
   dialogue:'prep', next:{id:'t1', tit:'Défi 1 · Deux heures dans la salle d\'attente', sub:"Amorcer une conversation avec un inconnu, raconter ce qui s'était passé avant, et entendre le parler d'ici."}},

  {id:'t1', no:'1', title:"Défi 1 · Deux heures dans la salle d'attente", color:'#1D6B8F',
   lead:"Échanger avec quelqu'un dans une salle d'attente : entrer en conversation sans déranger, raconter dans l'ordre ce qui a mené là, et suivre quelqu'un qui parle vite et québécois.",
   intro:"Défi 1 — Une salle d'attente est le seul endroit d'un hôpital où personne n'est obligé de vous parler. C'est aussi celui où l'on apprend le plus : Gilles Ferron attend sa femme depuis deux heures, il ne vous doit rien, et en vingt minutes il vous donne le conseil que sept mois d'attente ne vous avaient pas donné. Pour l'entendre, il faut suivre un fil : ce qui s'était passé avant, ce que reprend « cette affaire-là », et ce que veut dire quelqu'un qui dit « je suis après attendre ».",
   dialogue:'t1', next:{id:'t2', tit:'Défi 2 · Vingt minutes avec la spécialiste', sub:"Décrire ce qui a changé, comprendre une consigne, poser ses propres questions."}},

  {id:'t2', no:'2', title:'Défi 2 · Vingt minutes avec la spécialiste', color:'#B45309',
   lead:"S'informer auprès d'une spécialiste : décrire précisément ce qui a changé, comprendre une consigne, poser ses propres questions et repartir en sachant ce qui vient ensuite.",
   intro:"Défi 2 — Vingt minutes, et c'est vous qui parlez. La docteure Charest a votre dossier devant elle et elle préfère l'entendre de vous : elle ne demande pas comment vous allez, elle demande ce qui a changé. Ce qui se joue là n'est pas du courage, c'est de la précision — « je suis fatiguée » ne se travaille pas, « avant je montais les douze marches en parlant, maintenant j'arrête de parler » se travaille. Et quand elle dit « il faudrait que vous notiez », il faut entendre que ce n'est pas une suggestion.",
   dialogue:'t2', next:{id:'t3', tit:"Défi 3 · Ce qui s'écrit après", sub:"Lire un feuillet d'information et un compte rendu de consultation, et s'y reconnaître."}},

  {id:'t3', no:'3', title:"Défi 3 · Ce qui s'écrit après", color:'#3B49A0',
   lead:"Comprendre de l'information écrite sur un problème de santé : un feuillet qui explique la marche à suivre, et un compte rendu qui dit en d'autres mots ce que vous avez raconté.",
   intro:"Défi 3 — Trois feuilles dans une enveloppe. La première explique comment ça marche ici ; la deuxième est une lettre d'une médecin à une autre, et vous n'en êtes que la copie ; la troisième est un rendez-vous au laboratoire. Ce qui est difficile n'est pas le vocabulaire savant : c'est de reconnaître, sous « fatigue persistante d'apparition progressive », la phrase que vous avez dite vous-même il y a vingt minutes.",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"Poser vos questions à la spécialiste, raconter la journée à voix haute, puis écrire à votre sœur."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n6-sante/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"S'informer auprès de la spécialiste, raconter le rendez-vous à un proche, puis donner des nouvelles par écrit.",
   intro:"Je me lance — C'est à toi : tu t'informes auprès d'une médecin qui répond à tout mais ne devine rien ; tu racontes ensuite ta journée à voix haute, dans l'ordre et avec les mots justes ; puis tu écris à ta sœur, restée au pays, qui attend de tes nouvelles depuis le printemps."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#A5335F', custom:true,
   lead:"Rassembler les mots de l'hôpital, de l'attente, de l'entretien et de l'écrit qui reste.",
   intro:"Je retiens des mots — Rassemble ici les mots de la matinée de Leyla, révise-les avec les cartes mémoire, puis fais le point sur ce que tu sais faire."},
];
