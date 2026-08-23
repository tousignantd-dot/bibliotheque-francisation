const FC_CARDS = [
// Seize mots, et quatre seulement portent une image.
//
// C'est un choix. Le lexique d'un dossier d'assurance refusé est en grande
// partie abstrait — une exclusion, une franchise, un motif, une révision, un
// transfert de dossier. Leur donner une photo aurait mis derrière chaque
// carte une vue générique de sous-sol inondé, c'est-à-dire le thème du module
// à la place de ce que dit la carte : c'est le quatrième défaut de la
// relecture du 22 août 2026. Les quatre mots illustrés sont les quatre
// objets qu'on peut montrer sans écrire un mot dessus.
//
// « Une facture acquittée » et « une décision motivée » avaient d'abord reçu
// une image, et elles l'ont perdue : ce sont des **documents**, c'est-à-dire
// des objets dont le texte est le sujet. Le cadrage hors champ, qui règle un
// répondeur ou un afficheur, ne règle pas une feuille — cadrer le texte hors
// du champ d'une facture, c'est ne plus montrer de facture du tout.

  {word:"un refoulement d'égout",
   def:"La remontée des eaux usées par les drains d'un bâtiment, souvent pendant une grosse pluie.",
   ex:"Le <strong>refoulement d'égout</strong> du 14 septembre a laissé quinze centimètres d'eau au sous-sol.",
   img:"/assets/interactive/module-n8-habitation/vocab/refoulement-egout.jpg",
   tache:'prep'},

  {word:"un sinistre",
   def:"L'événement qui cause les dommages et qui déclenche une réclamation.",
   ex:"La date du <strong>sinistre</strong> est le 14 septembre, à vingt et une heures quarante.",
   tache:'prep'},

  {word:"une réclamation",
   def:"La demande d'indemnité qu'un assuré adresse à son assureur après un sinistre.",
   ex:"Sa <strong>réclamation</strong> porte le numéro 2026-41837 et a été ouverte le lendemain matin.",
   tache:'prep'},

  {word:"un avenant",
   def:"Une protection ajoutée à un contrat d'assurance, en plus de celles qui y sont déjà.",
   ex:"L'<strong>avenant</strong> « eau du sol et égout » ne fait pas partie du contrat de base.",
   tache:'prep'},

  {word:"une franchise",
   def:"La part des dommages qui reste à la charge de l'assuré à chaque réclamation.",
   ex:"La <strong>franchise</strong> est de mille dollars par sinistre, quel que soit le montant réclamé.",
   tache:'prep'},

  {word:"un clapet antiretour",
   def:"Un petit dispositif installé sur un drain, qui laisse l'eau sortir mais l'empêche de revenir.",
   ex:"Un <strong>clapet antiretour</strong> homologué se pose sur le drain principal, au sous-sol.",
   img:"/assets/interactive/module-n8-habitation/vocab/clapet-antiretour.jpg",
   tache:'prep'},

  {word:"un expert en sinistre",
   def:"La personne qui examine les dommages, en cherche la cause et évalue ce qu'ils coûtent.",
   ex:"L'<strong>expert en sinistre</strong> mandaté par la Mutuelle est venu deux jours après l'orage.",
   img:"/assets/interactive/module-n8-habitation/vocab/expert-en-sinistre.jpg",
   tache:'t1'},

  {word:"une contre-expertise",
   def:"Un second examen, demandé par l'assuré, qui vient discuter les conclusions du premier.",
   ex:"La <strong>contre-expertise</strong> a coûté six cents dollars et a duré une heure et demie.",
   tache:'t1'},

  {word:"un drain de fondation",
   def:"Le tuyau perforé posé au pied des murs d'un bâtiment pour évacuer l'eau du sol.",
   ex:"Le <strong>drain de fondation</strong> a été remplacé par l'ancien propriétaire, en 2019.",
   img:"/assets/interactive/module-n8-habitation/vocab/drain-de-fondation.jpg",
   tache:'t1'},

  {word:"un constat",
   def:"Ce qu'une personne a vu de ses propres yeux et qu'elle écrit sans l'interpréter.",
   ex:"Le <strong>constat</strong> est solide : l'eau est montée par le drain de plancher, pas par la fenêtre.",
   tache:'t1'},

  {word:"une exclusion",
   def:"Un cas nommé dans le contrat pour lequel l'assureur ne paie pas.",
   ex:"L'<strong>exclusion</strong> invoquée est celle de l'article 7.3, sur le défaut d'entretien.",
   tache:'t2'},

  {word:"le défaut d'entretien",
   def:"Le reproche fait à quelqu'un de ne pas avoir entretenu ce dont il avait la charge.",
   ex:"Le refus tient en trois mots : <strong>défaut d'entretien</strong> du drain de plancher.",
   tache:'t2'},

  {word:"une facture acquittée",
   def:"Une facture accompagnée de la preuve qu'elle a bien été payée.",
   ex:"Elle a retrouvé la <strong>facture acquittée</strong> du nettoyage du drain, datée du 3 mai.",
   tache:'t2'},

  {word:"une réponse finale",
   def:"La dernière position écrite d'une entreprise sur une plainte, avec ses raisons.",
   ex:"La <strong>réponse finale</strong> doit lui parvenir par écrit dans les soixante jours.",
   tache:'t3'},

  {word:"un transfert de dossier",
   def:"L'envoi de tout le dossier d'une plainte à l'organisme public qui surveille l'entreprise.",
   ex:"Après la réponse finale, elle peut demander le <strong>transfert de dossier</strong> à l'Autorité des marchés financiers.",
   tache:'t3'},

  {word:"une décision motivée",
   def:"Une décision qui dit non seulement ce qui est décidé, mais sur quoi elle s'appuie.",
   ex:"Une <strong>décision motivée</strong> nomme l'article du contrat, le fait retenu et la conclusion.",
   tache:'t3'},
];
