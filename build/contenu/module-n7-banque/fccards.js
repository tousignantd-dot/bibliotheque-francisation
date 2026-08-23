const FC_CARDS = [
  // Seize mots, quatre par section. C'est la seule liste de mots du module :
  // « Je retiens des mots », ses cartes mémoire et l'exercice `prVocab` en
  // dérivent tous.
  //
  // **Quatre cartes seulement portent une image, et c'est délibéré.** Le
  // vocabulaire d'une situation bancaire est abstrait — un solde, un taux,
  // une cote, un rendement, une protection ne se photographient pas. Leur
  // donner une image reviendrait à mettre derrière chaque mot une vue
  // générique de comptoir de caisse, c'est-à-dire le thème du module à la
  // place de ce que dit la carte : exactement le quatrième défaut relevé
  // le 22 août 2026. Les quatre images retenues montrent un objet réel,
  // décrit par la phrase d'exemple de sa carte.

  // ── Je découvre : ce que dit le papier ──
  {word:"un relevé de compte",
   def:"Le document que l'institution envoie chaque mois et qui montre tout ce qui est entré et sorti.",
   ex:"Le <strong>relevé de compte</strong> est resté trois jours sur la table de la cuisine, plié en trois.",
   img:"/assets/interactive/module-n7-banque/vocab/releve-de-compte.jpg",
   tache:"prep"},

  {word:"le solde",
   def:"Ce qui reste à devoir, ou ce qui reste dans le compte, à un moment donné.",
   ex:"Après douze paiements, le <strong>solde</strong> avait baissé de quatre cents dollars seulement.",
   tache:"prep"},

  {word:"le paiement minimum",
   def:"La plus petite somme qu'il faut verser dans le mois pour que le compte reste en règle.",
   ex:"Payer le <strong>paiement minimum</strong> garde le dossier propre, mais ne rembourse presque rien.",
   tache:"prep"},

  {word:"les frais de crédit",
   def:"Ce que coûte l'argent emprunté, en plus de la somme empruntée elle-même.",
   ex:"Sur neuf mille dollars à dix-neuf pour cent, les <strong>frais de crédit</strong> dépassent mille huit cents dollars par année.",
   img:"/assets/interactive/module-n7-banque/vocab/frais-de-credit.jpg",
   tache:"prep"},

  // ── Défi 1 : les mots de l'emprunt ──
  {word:"le taux d'intérêt",
   def:"Le prix de l'argent emprunté, dit en pourcentage et calculé pour une année.",
   ex:"Le <strong>taux d'intérêt</strong> de la marge est de neuf et quarante-cinq, celui de la carte de dix-neuf et quatre-vingt-dix.",
   tache:"t1"},

  {word:"une marge de crédit",
   def:"Une réserve d'argent où l'on prend ce qu'on veut, quand on veut, et où l'on ne paie d'intérêt que sur ce qui est pris.",
   ex:"Une <strong>marge de crédit</strong> coûte moins cher qu'une carte, mais elle n'oblige à rien.",
   tache:"t1"},

  {word:"un prêt personnel",
   def:"Une somme prêtée d'un coup, remboursée par versements égaux jusqu'à une date écrite dans le contrat.",
   ex:"Le <strong>prêt personnel</strong> se termine au quatre-vingtième versement, et la date est au contrat.",
   img:"/assets/interactive/module-n7-banque/vocab/pret-personnel.jpg",
   tache:"t1"},

  {word:"la cote de crédit",
   def:"Le chiffre, entre 300 et 900, qui résume la façon dont une personne a remboursé ses dettes jusqu'ici.",
   ex:"C'est la <strong>cote de crédit</strong> qui décide du taux qu'une institution accepte d'offrir.",
   tache:"t1"},

  // ── Défi 2 : les mots de l'épargne ──
  {word:"un placement",
   def:"De l'argent mis quelque part pour qu'il rapporte, au lieu de dormir dans un compte.",
   ex:"Un <strong>placement</strong> qui promet beaucoup sans aucun risque n'existe pas.",
   tache:"t2"},

  {word:"le rendement",
   def:"Ce que rapporte l'argent placé, sur une période donnée.",
   ex:"Le <strong>rendement</strong> d'un dépôt à terme est connu d'avance : c'est ce qui le distingue des autres placements.",
   tache:"t2"},

  {word:"un dépôt à terme",
   def:"De l'argent laissé à l'institution pour une durée fixée, à un taux connu dès le départ.",
   ex:"Elle a choisi un <strong>dépôt à terme</strong> de deux ans, parce que son projet a une date.",
   tache:"t2"},

  {word:"l'assurance-dépôts",
   def:"La protection publique qui rembourse l'argent déposé si l'institution fait faillite.",
   ex:"L'<strong>assurance-dépôts</strong> ne se demande pas et ne se paie pas : elle s'applique toute seule.",
   tache:"t2"},

  // ── Défi 3 : les mots de la contestation ──
  {word:"une opération non autorisée",
   def:"Une entrée ou une sortie d'argent que le titulaire du compte n'a pas faite et n'a pas permise.",
   ex:"Sept cent quatre-vingts dollars le quatorze : une <strong>opération non autorisée</strong>, chez un commerçant inconnu.",
   tache:"t3"},

  {word:"une contestation",
   def:"La démarche par laquelle on demande à l'institution de retirer une opération du relevé et d'enquêter.",
   ex:"La <strong>contestation</strong> a été ouverte le jour même de l'appel.",
   tache:"t3"},

  {word:"l'hameçonnage",
   def:"Le faux message qui imite une institution pour faire donner un numéro ou un mot de passe.",
   ex:"Le message annonçait une carte bloquée et demandait de cliquer : c'était de l'<strong>hameçonnage</strong>.",
   img:"/assets/interactive/module-n7-banque/vocab/hameconnage.jpg",
   tache:"t3"},

  {word:"un numéro de dossier",
   def:"Le code que l'institution attribue à une démarche et qui permet de la retrouver plus tard.",
   ex:"Sans <strong>numéro de dossier</strong>, il faut tout raconter de nouveau à chaque appel.",
   tache:"t3"},
];
