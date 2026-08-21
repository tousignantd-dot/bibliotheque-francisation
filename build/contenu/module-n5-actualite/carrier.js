const CARRIER_PHRASES = {
  // La clé est le mot LITTÉRAL, tel qu'il paraît dans FC_CARDS et dans la
  // troisième colonne des rangées `savoir` de exos.js : le gabarit fait
  // `CARRIER_PHRASES[w]` sans rien normaliser. Une clé écrite en slug, sans
  // article ou sans accent, ne serait jamais trouvée — la pastille lirait
  // alors le mot tout seul, mal accentué, et rien ne le signalerait avant
  // l'écoute.
  //
  // Trois clés portent une apostrophe ou un accent qui compte : « une
  // enquête », « un enquêteur », « la prévention ». Elles sont écrites ici
  // exactement comme dans exos.js et fccards.js.
  //
  // Les seize mots servent tous de pastille au moins une fois dans un bloc
  // `savoir` à `speak:true` — relevé fait sur exos.js.

  // Je découvre — le journal et sa forme
  'un fait divers':      "Elle lit les faits divers avant tout le reste du journal.",
  'un hebdomadaire':     "L'hebdomadaire de la région sort tous les mardis matin.",
  'le chapeau':          "Lis le chapeau : tu sauras la nouvelle en deux lignes.",
  'un témoin':           "Un témoin a vu trois vélos dans une remorque, vers minuit.",

  // Défi 1 — le sinistre et ses suites
  'un incendie':         "L'incendie a détruit les quatre logements de l'immeuble.",
  'évacuer':             "Les pompiers ont fait évacuer l'immeuble en pleine nuit.",
  'un sinistré':         "Onze sinistrés ont été hébergés par la Croix-Rouge.",
  'une inondation':      "L'inondation a rempli une dizaine de sous-sols de la rue.",

  // Défi 2 — la parole rapportée et l'enquête
  'une déclaration':     "Sa déclaration tient en une phrase, entre guillemets.",
  'une enquête':         "L'enquête dira si le feu est parti de la cuisine.",
  'un enquêteur':        "L'enquêteur a passé la matinée dans les décombres.",
  'un avertissement':    "Un avertissement de pluie abondante avait été émis la veille.",

  // Défi 3 — le délit et ce qu'on en pense
  'un vol':              "Le vol a eu lieu pendant la nuit, dans un cabanon ouvert.",
  'un suspect':          "Aucun suspect n'a été arrêté pour l'instant.",
  'un cabanon':          "Les voleurs sont entrés par la porte du cabanon.",
  'la prévention':       "Noter son numéro de série, c'est de la prévention.",
};
