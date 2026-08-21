const SECTIONS = [
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n5-services/icons/play.svg" alt="">', title:'Je découvre', color:'#A5335F',
   lead:"Nommer les services de sa ville, comprendre une brochure officielle, entendre l'oral d'ici.",
   intro:"Leïla Haddad habite Villeray depuis huit mois. Dans sa boîte aux lettres, elle a reçu une brochure de la Ville qu'elle a prise pour de la publicité et rangée avec les circulaires. Il y a dedans trois bacs, un horaire, un mot qu'elle n'a jamais vu — « écocentre » — et la réponse à la question qu'elle se pose depuis deux semaines.",
   dialogue:'prep', next:{id:'t1', tit:"Défi 1 · L'appel", sub:"Téléphoner à un service public, demander des renseignements précis et noter un numéro de requête."}},

  {id:'t1', no:'1', title:"Défi 1 · L'appel", color:'#1D6B8F',
   lead:"Poser des questions précises au téléphone, donner ses coordonnées, noter et confirmer ce qu'on vous répond.",
   intro:"Défi 1 — Un service public commence presque toujours par un menu automatisé et une attente. Ce qui décide de la suite, c'est la première phrase : dire pourquoi on appelle en une seule phrase claire. Après, tout se joue sur les questions qu'on pense à poser — et sur le numéro qu'on note avant de raccrocher.",
   dialogue:'t1', next:{id:'t2', tit:"Défi 2 · L'écran", sub:"Lire une page de service public et un formulaire complexe sans se perdre."}},

  {id:'t2', no:'2', title:"Défi 2 · L'écran", color:'#B45309',
   lead:"Trouver l'information utile dans un site Web, une brochure et un formulaire complexe.",
   intro:"Défi 2 — Une page de service public n'est pas faite pour être lue de haut en bas. Elle est faite pour qu'on y cherche une réponse. Les colonnes, les encadrés et les listes disent chacun quelque chose de différent — et l'encadré « avant de vous déplacer » évite plus de voyages inutiles que le reste de la page réuni.",
   dialogue:'t2', next:{id:'t3', tit:'Défi 3 · Le guichet', sub:"Se présenter au comptoir, expliquer sa démarche et savoir ce qu'il faut apporter."}},

  {id:'t3', no:'3', title:'Défi 3 · Le guichet', color:'#0D7A6F',
   lead:"Raconter une démarche déjà commencée, comprendre ce qui manque, repartir avec ce qu'on est venu chercher.",
   intro:"Défi 3 — Au comptoir, on arrive rarement les mains vides : on a déjà essayé en ligne, déjà téléphoné, déjà attendu. Il faut donc raconter ce qui s'est passé avant, comprendre ce qui manque au dossier, et repartir avec la réponse — pas avec une quatrième démarche à faire.",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"Téléphoner pour de vrai, laisser un message dans une boîte vocale, puis écrire au service."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n5-services/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"Mener un appel du début à la fin, laisser un message clair, puis relancer un service par écrit.",
   intro:"Je me lance — C'est à vous : vous appelez un service public, vous laissez un message dans sa boîte vocale, puis vous lui écrivez pour relancer votre demande."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#A5335F', custom:true,
   lead:"Rassembler les mots de la brochure, de l'appel, du site Web et du guichet.",
   intro:"Je retiens des mots — Notez vos mots utiles, révisez avec les cartes mémoire, puis évaluez ce que vous êtes maintenant capable de faire."},
];
