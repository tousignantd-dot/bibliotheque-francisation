const FC_CARDS = [
// Seize mots, et seulement quatre portent une image.
//
// Le lexique de l'assurance est un lexique de clauses : une franchise, un
// avenant, une exclusion, la responsabilité civile, la dépréciation, la
// subrogation ne se photographient pas. Leur donner une photo aurait mis
// derrière chaque carte une vue générique de bureau ou de boîtes de carton,
// c'est-à-dire le thème du module à la place de ce que dit la carte — le
// quatrième défaut de la relecture du 22 août 2026. Les quatre illustrées
// sont celles qui désignent une chose visible : le sinistre, le dégât d'eau,
// l'inventaire et le connaissement, ce dernier étant un objet (une liasse
// posée sur le hayon d'un camion) et non un document à lire. Le poids visuel
// du module est porté par les deux `imgmatch`, dont les douze énoncés sont
// des scènes concrètes.

  {word:"une assurance habitation",
   def:"Le contrat qui protège ce qu'on possède chez soi et ce qu'on pourrait faire subir aux autres.",
   ex:"Amira a souscrit une <strong>assurance habitation</strong> onze jours avant d'emménager.",
   tache:'prep'},

  {word:"un sinistre",
   def:"L'événement qui cause le dommage et qui déclenche le contrat.",
   ex:"La franchise de cinq cents dollars s'applique une fois par <strong>sinistre</strong>, pas une fois par objet.",
   img:"/assets/interactive/module-n8-emmenagement/vocab/sinistre.jpg",
   tache:'prep'},

  {word:"un connaissement",
   def:"Le papier que le transporteur fait signer et qui dit ce qu'il prend en charge.",
   ex:"Elle n'a signé le <strong>connaissement</strong> qu'à la fin, dans le camion, sans le lire.",
   img:"/assets/interactive/module-n8-emmenagement/vocab/connaissement.jpg",
   tache:'prep'},

  {word:"un inventaire",
   def:"La liste écrite de tout ce qui est transporté ou de tout ce qui a été abîmé.",
   ex:"Le chauffeur a signé l'<strong>inventaire</strong> à huit heures et n'y a noté aucun dommage.",
   img:"/assets/interactive/module-n8-emmenagement/vocab/inventaire.jpg",
   tache:'prep'},

  {word:"une déclaration de valeur",
   def:"Le fait d'annoncer d'avance ce que vaut un objet, pour qu'il soit couvert à ce prix-là.",
   ex:"Sans <strong>déclaration de valeur</strong>, le meuble n'était couvert qu'à soixante cents la livre.",
   tache:'prep'},

  {word:"un dégât d'eau",
   def:"Le dommage causé par l'eau qui entre là où elle ne devrait pas.",
   ex:"Deux boîtes laissées sur le balcon ont subi un <strong>dégât d'eau</strong> pendant l'averse.",
   img:"/assets/interactive/module-n8-emmenagement/vocab/degat-eau.jpg",
   tache:'prep'},

  {word:"un courtier en assurance de dommages",
   def:"La personne qui vend le contrat, le compare et l'explique, sans travailler pour un seul assureur.",
   ex:"Son <strong>courtier en assurance de dommages</strong> lui a repris chaque clause au téléphone.",
   tache:'t1'},

  {word:"une franchise",
   def:"La part du dommage qui reste toujours à la charge de la personne assurée.",
   ex:"Avec une <strong>franchise</strong> de cinq cents dollars, un dommage de quatre cents ne se réclame pas.",
   tache:'t1'},

  {word:"la responsabilité civile",
   def:"La partie du contrat qui paie quand c'est vous qui causez le dommage à quelqu'un d'autre.",
   ex:"Sa <strong>responsabilité civile</strong> la couvre jusqu'à deux millions de dollars.",
   tache:'t1'},

  {word:"la valeur à neuf",
   def:"Le remboursement au prix d'un objet neuf équivalent, sans tenir compte de l'âge.",
   ex:"Elle a choisi la <strong>valeur à neuf</strong>, et c'est ce qui explique le montant de sa prime.",
   tache:'t1'},

  {word:"la dépréciation",
   def:"La perte de valeur d'un objet à mesure qu'il vieillit.",
   ex:"Au jour du sinistre, la <strong>dépréciation</strong> ramène un téléviseur de huit ans à presque rien.",
   tache:'t1'},

  {word:"un avenant",
   def:"Une protection ajoutée par écrit à un contrat qui ne l'offrait pas.",
   ex:"Deux <strong>avenants</strong> complètent sa police : le refoulement d'égout et les bijoux.",
   tache:'t1'},

  {word:"une exclusion",
   def:"Un cas que le contrat annonce d'avance ne pas couvrir.",
   ex:"Le refus s'appuie sur une <strong>exclusion</strong> qui vise le transport par un déménageur.",
   tache:'t1'},

  {word:"un expert en sinistre",
   def:"La personne qui établit les faits pour l'assureur et propose une décision.",
   ex:"L'<strong>expert en sinistre</strong> n'est ni votre adversaire ni votre allié.",
   tache:'t2'},

  {word:"la subrogation",
   def:"Le droit de l'assureur de se retourner contre celui qui a réellement causé le dommage.",
   ex:"Par <strong>subrogation</strong>, l'assureur peut réclamer lui-même au déménageur ce qu'il a versé.",
   tache:'t2'},

  {word:"une mise en demeure",
   def:"La lettre qui somme quelqu'un de faire quelque chose avant une date, sous peine de poursuite.",
   ex:"Elle a envoyé une <strong>mise en demeure</strong> au déménageur en gardant une preuve d'envoi.",
   tache:'t2'},
];
