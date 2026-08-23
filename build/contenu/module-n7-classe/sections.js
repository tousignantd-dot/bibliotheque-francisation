const SECTIONS = [
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n7-classe/icons/play.svg" alt="">', title:'Je découvre', color:'#0D7A6F',
   lead:"Nommer les rôles d'une équipe de travail, entendre la différence entre parler à un ami et parler devant la classe, et savoir ce qu'on attend d'une animatrice.",
   intro:"Neusa Marinho est couturière dans un atelier de Rivière-Noire. Le soir, elle suit sa francisation au Centre d'éducation des adultes de la Pointe-aux-Ormes. Ce lundi, son enseignante Ghislaine Turcotte confie à chaque équipe un sujet de recherche et un rôle. Neusa n'a pas le rôle qu'elle espérait : elle voulait chercher les sources, on lui demande d'animer. Trois semaines, trois coéquipiers, un exposé à la fin — et c'est elle qui devra faire parler les autres.",
   dialogue:'prep', next:{id:'t1', tit:'Défi 1 · Écouter quelqu\'un qui sait', sub:"Suivre une personne invitée en classe, prendre des notes, et distinguer un fait d'une estimation."}},

  {id:'t1', no:'1', title:"Défi 1 · Écouter quelqu'un qui sait", color:'#1D6B8F',
   lead:"Comprendre de l'information reliée à un sujet de recherche, présentée oralement par une personne-ressource.",
   intro:"Défi 1 — Une personne invitée en classe ne parle pas comme un dialogue. Elle annonce un plan, elle le suit, elle le referme ; elle donne des chiffres dont certains sont mesurés et d'autres seulement estimés ; et elle répond mal aux questions vagues. Ce défi apprend à suivre le plan par ses connecteurs, à entendre le conditionnel qui signale un chiffre non confirmé, à séparer le fait de l'estimation et de l'opinion — et à poser la question qui obtient une réponse utilisable.",
   dialogue:'t1', next:{id:'t2', tit:'Défi 2 · Lire, trier, résumer', sub:"Retrouver l'information dans un écrit, puis la redire en dix lignes sans la recopier."}},

  {id:'t2', no:'2', title:'Défi 2 · Lire, trier, résumer', color:'#B45309',
   lead:"Comprendre de l'information écrite reliée à un sujet de recherche, et la résumer.",
   intro:"Défi 2 — Résumer n'est pas raccourcir. Un résumé garde ce qui répond à la question de départ et jette le reste, même quand le reste est intéressant ; il redit avec ses mots à soi, sinon c'est du copiage ; et il tient ensemble par des connecteurs, sinon c'est une liste. Ce défi apprend à lire une fiche d'information pour y prendre ce qu'on cherche, à remplacer un groupe de mots par un nom, et à reformuler sans trahir.",
   dialogue:'t2', next:{id:'t3', tit:"Défi 3 · Faire parler l'équipe", sub:"Animer une rencontre, tenir un désaccord, et rapporter ce que chacun a dit."}},

  {id:'t3', no:'3', title:"Défi 3 · Faire parler l'équipe", color:'#A5335F',
   lead:"Conduire une rencontre de travail, exprimer un désaccord sans rompre, et rapporter les propos du groupe.",
   intro:"Défi 3 — Animer, ce n'est pas parler le plus. C'est ouvrir, distribuer, faire préciser, reformuler ce qu'on vient d'entendre, et fermer avec des décisions que tout le monde reconnaît. Ce défi arrive au moment où l'équipe de Neusa ne s'entend plus : Youssouf veut compter les arbres de la rue, Miguel trouve que ça ne prouve rien. Vous y apprendrez la concession, la mise en relief, et surtout le discours indirect au passé — parce qu'à la fin, il faut écrire ce que les autres ont dit.",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"Animer une rencontre avec l'assistant, faire votre exposé, écrire au camarade absent."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n7-classe/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"Conduire une rencontre d'équipe, présenter son sujet devant la classe, écrire à un camarade qui n'était pas là.",
   intro:"Je me lance — C'est à vous : vous animez la rencontre avec l'assistant, vous faites votre exposé devant la classe, puis vous écrivez au camarade absent la lettre qui lui dit ce que le groupe a décidé."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#0D7A6F', custom:true,
   lead:"Rassembler les mots du travail d'équipe, de la recherche et du compte rendu.",
   intro:"Je retiens des mots — Notez vos mots utiles, révisez avec les cartes mémoire, puis évaluez ce que vous êtes maintenant capable de faire."},
];
