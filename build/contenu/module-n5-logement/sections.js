const SECTIONS = [
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n5-logement/icons/play.svg" alt="">', title:'Je découvre', color:'#A5335F',
   lead:"Nommer les parties d'un logement, comprendre un avis du propriétaire, entendre l'oral d'ici.",
   intro:"Nadège habite un trois et demie à Fleurimont avec sa fille de sept ans, qui dort dans le salon. En février, elle trouve dans sa boîte aux lettres un papier de son propriétaire : le loyer monte, et la case de stationnement disparaît. Elle a un mois pour répondre — et elle ne sait pas encore qu'elle a le droit de refuser.",
   dialogue:'prep', next:{id:'t1', tit:"Défi 1 · L'appel", sub:"Se renseigner par téléphone et noter ce qu'on vous répond."}},

  {id:'t1', no:'1', title:"Défi 1 · L'appel", color:'#1D6B8F',
   lead:"Poser les bonnes questions au téléphone, et garder une trace écrite des réponses.",
   intro:"Défi 1 — Au téléphone, on ne voit rien : ni le logement, ni le visage de la personne. Tout passe par ce qu'on demande et par ce qu'on note. Un appel de quatre minutes bien mené évite une visite inutile à l'autre bout de la ville.",
   dialogue:'t1', next:{id:'t2', tit:'Défi 2 · La visite', sub:"Comprendre les renseignements qu'on vous donne — et savoir les donner."}},

  {id:'t2', no:'2', title:'Défi 2 · La visite', color:'#B45309',
   lead:"Décrire un logement avec précision, comprendre ce qu'on vous en dit, poser la question qui reste.",
   intro:"Défi 2 — Une visite dure quinze minutes. C'est court pour voir un logement où on habitera un an. Ce qui se joue là, c'est de comprendre ce qu'on vous dit du chauffage et du bruit, et d'être capable, un jour, de le dire à votre tour.",
   dialogue:'t2', next:{id:'t3', tit:'Défi 3 · Le bail', sub:"Lire le contrat, l'annexe et l'avis de renouvellement avant de signer."}},

  {id:'t3', no:'3', title:'Défi 3 · Le bail', color:'#0D7A6F',
   lead:"Lire un bail et un avis de renouvellement, et savoir ce qu'on a le droit de faire.",
   intro:"Défi 3 — Le bail est le même formulaire pour tout le monde au Québec, et il est écrit pour être lu. La section G dit combien payait le locataire d'avant ; l'annexe dit ce qui est interdit dans l'immeuble ; et le renouvellement se fait tout seul, ce qui est une protection.",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"Faire visiter un logement à voix haute, puis écrire vos notes d'appel."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n5-logement/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"Mener une visite des deux côtés, puis transmettre par écrit ce que vous avez appris au téléphone.",
   intro:"Je me lance — C'est à vous : vous visitez un logement ou vous le faites visiter, puis vous écrivez le courriel de notes qui suit un appel."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#A5335F', custom:true,
   lead:"Rassembler les mots du logement, de l'appel, de la visite et du bail.",
   intro:"Je retiens des mots — Notez vos mots utiles, révisez avec les cartes mémoire, puis évaluez ce que vous êtes maintenant capable de faire."},
];
