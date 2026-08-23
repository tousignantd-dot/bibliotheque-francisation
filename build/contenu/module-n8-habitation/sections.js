const SECTIONS = [
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n8-habitation/icons/play.svg" alt="">', title:'Je découvre', color:'#1D6B8F',
   lead:"Nommer les pièces d'un dossier d'assurance refusé, raconter ce qui s'était passé avant le sinistre, et entendre ce qu'une voix ajoute aux mots.",
   intro:"Teodora Vlaicu est technicienne en documentation au cégep de Trois-Rivières. Elle habite le haut d'un duplex de la rue Sainte-Julie et loue le bas. Le 14 septembre, pendant un orage, un refoulement d'égout a inondé son sous-sol fini : quinze centimètres d'eau, un plancher flottant à jeter, une chambre d'amis vidée. Elle a réclamé. Ce matin, l'agente au règlement des sinistres lui apprend au téléphone que sa réclamation est refusée, et lui dit pourquoi.",
   dialogue:'prep', next:{id:'t1', tit:'Défi 1 · Le rapport qu’on discute', sub:"Lire un rapport d'expertise et voir où il place la faute."}},

  {id:'t1', no:'1', title:"Défi 1 · Le rapport qu'on discute", color:'#0D7A6F',
   lead:"Lire le rapport de l'expert de l'assureur, distinguer ce qu'il a constaté de ce qu'il en conclut, et reconnaître les tournures qui imputent une faute sans nommer personne.",
   intro:"Défi 1 — Un refus tient en une ligne, mais il s'appuie sur un document de quatre pages que presque personne ne demande. Ce défi apprend à le lire. Un rapport d'expertise mélange trois choses : ce que l'expert a vu de ses yeux, ce qu'on lui a dit, et ce qu'il en déduit. Seule la première est difficile à contester. Vous apprendrez aussi à suivre ses phrases longues — celles où un « dont », un « auquel » ou un « à laquelle » renvoie à quelque chose écrit trois lignes plus haut — et à repérer le passif, qui est la façon polie de dire que c'est votre faute.",
   dialogue:'t1', next:{id:'t2', tit:"Défi 2 · L'appel qui conteste", sub:"Contester un refus au téléphone, sans se fâcher et sans lâcher."}},

  {id:'t2', no:'2', title:"Défi 2 · L'appel qui conteste", color:'#B45309',
   lead:"Échanger avec son assureur au téléphone à propos d'une réclamation : rappeler son dossier, opposer des faits, concéder ce qui est vrai, et demander une réponse écrite.",
   intro:"Défi 2 — C'est l'appel qui compte. Vous ne cherchez pas à avoir raison : vous cherchez à faire écrire quelque chose à quelqu'un. Ce défi apprend trois gestes de langue qui font toute la différence. Concéder avant d'avancer, parce qu'une contestation qui nie tout ne convainc personne. Dire ce qui serait arrivé si le motif invoqué avait été le bon — c'est l'hypothèse irréelle, et c'est l'arme la plus tranquille du français. Et demander une réponse finale écrite et motivée, en une phrase, sans menacer.",
   dialogue:'t2', next:{id:'t3', tit:'Défi 3 · Porter la décision plus haut', sub:"Suivre un exposé sur les recours, et écrire la demande de révision."}},

  {id:'t3', no:'3', title:'Défi 3 · Porter la décision plus haut', color:'#A5335F',
   lead:"Suivre le déroulement d'un exposé bien structuré sur les recours possibles, en retenir les étapes, les délais et les chiffres, et savoir devant qui porter quoi.",
   intro:"Défi 3 — Un refus n'est pas une fin. Il existe une suite, elle est écrite dans les règlements, et presque personne ne la connaît. Vous allez écouter une capsule d'information de l'Autorité des marchés financiers : quinze minutes d'un seul homme qui explique une procédure, avec des étapes, des délais et des chiffres. Ce n'est pas une conversation — c'est un exposé, et il s'écoute autrement. Trois écoutes, trois consignes différentes : le fait récent, puis les chiffres, puis ce qui est dit deux fois.",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"Contester avec l'assistant, raconter votre sinistre, écrire la demande de révision."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n8-habitation/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"Contester un refus au téléphone, raconter à voix haute une décision que vous avez trouvée injuste, puis écrire la lettre de demande de révision.",
   intro:"Je me lance — C'est à vous : vous menez l'appel de contestation avec l'assistant, vous racontez à voix haute une fois où l'on a décidé quelque chose à votre place, puis vous écrivez la lettre qui demande qu'on réexamine le dossier."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#1D6B8F', custom:true,
   lead:"Rassembler les mots du sinistre, du contrat d'assurance, de l'expertise et du recours.",
   intro:"Je retiens des mots — Notez vos mots utiles, révisez avec les cartes mémoire, puis évaluez ce que vous êtes maintenant capable de faire."},
];
