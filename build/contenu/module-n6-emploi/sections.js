const SECTIONS = [
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n6-emploi/icons/play.svg" alt="">', title:'Je découvre', color:'#A5335F',
   lead:"Reconnaître les quatre écrits du milieu de travail — l'affichage, la note de service, la politique, le compte rendu — et savoir d'avance ce que chacun donne.",
   intro:"Yaneth Mosquera a trente-six ans. Elle est arrivée de Colombie il y a quatre ans et elle travaille depuis deux ans à l'expédition, chez Emballages Bocage, à Saint-Hyacinthe. Un matin, un papier neuf paraît au babillard : un poste de vérificatrice à la qualité est affiché à l'interne, et il reste dix jours ouvrables. Son chef d'équipe, Ghislain Tanguay, lui explique que ce papier ne dit pas tout — et qu'il y en aura trois autres.",
   dialogue:'prep', next:{id:'t1', tit:"Défi 1 · On m'explique la démarche", sub:"Suivre une explication en cinq étapes et retrouver ce que reprennent « le », « en » et « y »."}},

  {id:'t1', no:'1', title:"Défi 1 · On m'explique la démarche", color:'#1D6B8F',
   lead:"Comprendre des explications sur les étapes d'une démarche administrative : l'ordre des étapes, ce qu'il faut faire, et les mots qui renvoient à ce qui vient d'être dit.",
   intro:"Défi 1 — Marie-Soleil Grenon explique la démarche en cinq étapes, sans papier, en quinze minutes. Ce qui est difficile n'est pas le vocabulaire : c'est que tout se tient. Elle dit « gardez-la », « je l'avise », « vous ne la perdez pas » — et chaque fois, le petit mot renvoie à quelque chose dit trente secondes plus tôt. Perdre le fil, ce n'est pas manquer un mot : c'est perdre à quoi il renvoie.",
   dialogue:'t1', next:{id:'t2', tit:'Défi 2 · Ce que disent les documents', sub:"Lire une note de service et un article de politique, et voir ce que la mise en page dit avant les phrases."}},

  {id:'t2', no:'2', title:'Défi 2 · Ce que disent les documents', color:'#B45309',
   lead:"Lire de la documentation interne reliée à son emploi : une note de service et un article de politique, avec ce que leur présentation matérielle indique.",
   intro:"Défi 2 — Deux documents, deux façons d'écrire. La note de service explique : elle a un objet, des puces, un encadré de rappel. La politique, elle, fixe des règles : elle a des articles numérotés, et une règle se nomme par son numéro. Ces deux textes-là disent la même démarche, mais ils ne se lisent pas de la même façon — et l'un des deux gagne sur l'autre le jour où ils ne s'accordent plus.",
   dialogue:'t2', next:{id:'t3', tit:'Défi 3 · Le compte rendu', sub:"Lire ce qui a été dit et décidé à une rencontre, puis poser une hypothèse en « si »."}},

  {id:'t3', no:'3', title:'Défi 3 · Le compte rendu', color:'#3B49A0',
   lead:"Lire un compte rendu de rencontre : ses parties, sa langue sans « je », ses décisions, et le rappel historique qu'il cite au passé simple.",
   intro:"Défi 3 — Vingt-deux personnes à la cafétéria, quarante minutes de rencontre, et deux pages de compte rendu le vendredi. Un compte rendu ne raconte pas comme une conversation : il ne dit jamais « je », il nomme les décisions au lieu de les raconter, et il cite parfois un passé qu'on n'entend nulle part ailleurs — celui du récit écrit, « elle ouvrit », « ils choisirent ». C'est le texte qui reste quand tout le monde est reparti.",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"Décrire la démarche à voix haute, puis écrire ton courriel aux ressources humaines."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n6-emploi/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"Expliquer la démarche à un collègue, la décrire à voix haute avec les détails nécessaires, puis écrire un courriel professionnel aux ressources humaines.",
   intro:"Je me lance — C'est à toi : tu expliques la démarche à l'assistant, qui n'a rien lu et qui doute ; tu en fais ensuite la description détaillée à voix haute ; puis tu écris ton courriel à Marie-Soleil Grenon."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#A5335F', custom:true,
   lead:"Rassembler les mots du babillard, des ressources humaines, des documents écrits et de la rencontre.",
   intro:"Je retiens des mots — Note tes mots utiles, révise avec les cartes mémoire, puis évalue ce que tu es maintenant capable de faire."},
];
