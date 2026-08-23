const SECTIONS = [
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n8-actualite/icons/play.svg" alt="">', title:'Je découvre', color:'#1D6B8F',
   lead:"Nommer les genres de l'actualité, séparer un fait d'une opinion, et entendre ce que la voix ajoute aux mots.",
   intro:"Mirela Petrescu est technicienne en documentation à la bibliothèque municipale de Rivière-aux-Cèdres, vingt-quatre mille habitants, à quarante minutes de Sherbrooke. Lundi soir, le conseil a voté par quatre voix contre trois la cession du boisé Sainte-Perpétue à un promoteur, qui veut y bâtir cent quatre-vingts logements dont quarante-cinq abordables. Mirela a lu deux articles sur la même séance et n'a pas reconnu la même soirée. Ce matin, elle croise Régine Sauvé, porte-parole du comité de citoyens, au comptoir des retours.",
   dialogue:'prep', next:{id:'t1', tit:'Défi 1 · Deux versions du même fait', sub:"Comparer deux comptes rendus d'un même événement et voir ce que chacun choisit de taire."}},

  {id:'t1', no:'1', title:'Défi 1 · Deux versions du même fait', color:'#A83A22',
   lead:"Comprendre un reportage et un article d'information sur un sujet d'intérêt général, et comparer deux récits d'un même événement.",
   intro:"Défi 1 — Deux journalistes honnêtes racontent la même séance du conseil et vous n'y reconnaissez pas la même soirée. Ce n'est pas que l'un ment : c'est qu'ils n'ont pas choisi les mêmes phrases. Ce défi apprend à voir ce choix. Quel mot a été retenu pour nommer la chose — un boisé, un terrain vague, un actif. Quelle phrase efface celui qui a décidé. Quel chiffre est cité, et lequel manque. On n'apprend pas à décider qui a raison : on apprend à lire les deux et à savoir ce qu'on sait.",
   dialogue:'t1', next:{id:'t2', tit:"Défi 2 · L'éditorial et sa thèse", sub:"Démonter un texte d'opinion, et suivre une chronique qui parle vite."}},

  {id:'t2', no:'2', title:"Défi 2 · L'éditorial et sa thèse", color:'#0D7A6F',
   lead:"Comprendre un article d'opinion, une chronique ou un éditorial, et suivre un point de vue développé d'un seul tenant.",
   intro:"Défi 2 — Un texte d'opinion n'est pas une suite d'idées : c'est une construction. Une thèse, des arguments, une concession qui donne raison à l'adversaire pour mieux avancer, et une conclusion. Ce défi apprend à repérer chacune de ces pièces, puis à les manier soi-même. Il apprend aussi une chose qui ne s'entend nulle part ailleurs dans le dépôt : suivre douze minutes de chronique radio, sans interlocuteur, au débit d'un professionnel qui ne ralentit pour personne.",
   dialogue:'t2', next:{id:'t3', tit:'Défi 3 · Prendre position', sub:"Défendre son avis devant quelqu'un qui ne le partage pas, puis l'écrire."}},

  {id:'t3', no:'3', title:'Défi 3 · Prendre position', color:'#A5335F',
   lead:"Commenter l'actualité en justifiant son point de vue, puis écrire au courrier des lecteurs pour donner son opinion.",
   intro:"Défi 3 — Dire ce qu'on pense est facile ; le dire à quelqu'un qui pense le contraire et qui vous coupe la parole ne l'est pas. Ce défi apprend quatre gestes. Annoncer sa position en une phrase, avant de l'expliquer. Concéder ce que l'autre camp a de juste, ce qui vous rend écoutable au lieu de vous affaiblir. Dire ce qui aurait pu se passer autrement, au conditionnel passé. Et mettre en avant ce qui compte, au lieu de tout dire sur le même ton. Vous finirez par lire, découpée fonction par fonction, la lettre que vous allez écrire.",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"Appeler à la tribune, défendre votre avis à voix haute, puis écrire au journal."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n8-actualite/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"Appeler à une tribune téléphonique, commenter l'actualité à voix haute en justifiant son point de vue, puis écrire une lettre au courrier des lecteurs.",
   intro:"Je me lance — C'est à vous : vous appelez à la tribune et vous tenez votre bout devant un animateur qui vous contredit, vous enregistrez une intervention de deux minutes, puis vous écrivez la lettre au courrier des lecteurs — qui commence par résumer, en trois phrases, l'éditorial auquel elle répond."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#1D6B8F', custom:true,
   lead:"Rassembler les mots des médias, de l'opinion et de la vie municipale.",
   intro:"Je retiens des mots — Notez vos mots utiles, révisez avec les cartes mémoire, puis évaluez ce que vous êtes maintenant capable de faire."},
];
