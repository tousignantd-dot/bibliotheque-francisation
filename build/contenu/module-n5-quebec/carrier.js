const CARRIER_PHRASES = {
  // La clé est le mot LITTÉRAL tel qu'il apparaît dans FC_CARDS et dans la
  // troisième colonne d'une rangée `savoir` à pastilles : le gabarit fait
  // `CARRIER_PHRASES[w]` sans normaliser. Une clé écrite autrement — en slug,
  // sans article, sans accent — ne serait jamais trouvée, et le mot partirait
  // seul à la synthèse, mal accentué.
  //
  // Les seize clés ont été relevées sur `fccards.js` + `exos.js`, pas écrites
  // de mémoire : seize mots, seize phrases porteuses, aucune clé en trop ni
  // manquante, et les quinze bandeaux `savoir` à pastilles portent tous
  // `speak:true`. Aucun des seize mots ne contient d'apostrophe.
  //
  // Les nombres sont écrits en toutes lettres : la synthèse lit « 90 $ » de
  // façon imprévisible, et une phrase porteuse n'existe que pour bien poser
  // l'accent du mot qu'elle porte.

  // Je découvre — la région et ce qu'on y va voir
  'un attrait':          "Le principal attrait de la région, c'est le parc au bord du fleuve.",
  'un dépliant':         "Elle a pris un dépliant du parc au comptoir d'accueil.",
  'le fleuve':           "À Rimouski, le fleuve est si large qu'on ne voit pas l'autre rive.",
  'un phare':            "Le phare se visite du mois de juin au mois d'octobre.",

  // Défi 1 — le comptoir : le billet, l'horaire, les bagages
  'un aller-retour':     "Un aller-retour coûte moins cher que deux billets simples.",
  'un horaire':          "L'horaire du lundi n'est pas le même que celui du dimanche.",
  'une correspondance':  "Il y a une correspondance à Québec, avec quarante minutes d'attente.",
  'la soute':            "Deux valises par personne sont acceptées dans la soute.",

  // Défi 2 — ce qui est écrit : le parc, le gîte, le fleuve
  'un gîte':             "Le gîte ne compte que quatre chambres, alors elle a réservé tôt.",
  'un sentier':          "Le sentier du bord de l'eau fait cinq kilomètres.",
  'la marée':            "À marée basse, on marche jusqu'à l'île à pied sec.",
  'le prêt-à-camper':    "Elle a choisi le prêt-à-camper : elle n'a ni tente ni sac de couchage.",

  // Défi 3 — sur place : les gens, la saison, la conversation
  'un vacancier':        "Au mois d'août, il y a plus de vacanciers que d'habitants dans le village.",
  'un belvédère':        "Du belvédère, on voit les îles et les bateaux qui passent.",
  'la basse saison':     "En basse saison, le gîte demande vingt dollars de moins par nuit.",
  'jaser':               "Ils ont jasé une demi-heure sur le quai, sans se connaître.",
};
