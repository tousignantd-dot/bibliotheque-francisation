const CARRIER_PHRASES = {
  // La clé est le mot LITTÉRAL tel qu'il apparaît dans FC_CARDS et dans la
  // troisième colonne d'une rangée `savoir` à pastilles : le gabarit fait
  // `CARRIER_PHRASES[w]` sans normaliser. Une clé écrite autrement — en slug,
  // sans article, sans accent — ne serait jamais trouvée, et le mot partirait
  // seul à la synthèse, mal accentué.
  //
  // Deux clés de ce module portent une apostrophe — « l'accotement » et
  // « un véhicule d'urgence ». Elles sont écrites ici entre guillemets
  // doubles, exactement comme dans exos.js et fccards.js.
  //
  // Les seize mots servent tous de pastille au moins une fois dans un bloc
  // `savoir` à `speak:true` — vérification faite sur exos.js.

  // Je découvre — l'état de la route
  'un ralentissement':   "On annonce un ralentissement de vingt minutes entre les deux sorties.",
  'un bouchon':          "À sept heures, le bouchon commençait avant même le pont.",
  "l'accotement":        "Un camion est immobilisé sur l'accotement, à la hauteur de la sortie.",
  'une entrave':         "Aucune entrave à signaler dans le tunnel ce matin.",

  // Défi 1 — l'incident, l'endroit, les secours
  'un carambolage':      "Le carambolage de quatre véhicules bloque deux voies sur trois.",
  'une remorqueuse':     "Deux remorqueuses sont sur place depuis dix minutes.",
  'une voie':            "La voie de droite reste ouverte, les deux autres sont bloquées.",
  "un véhicule d'urgence": "On demande de laisser passer les véhicules d'urgence par la gauche.",

  // Défi 2 — le bulletin complet
  'la chaussée':         "La chaussée est glissante entre les deux ponts.",
  'un nid-de-poule':     "Un nid-de-poule important est signalé dans la voie de droite.",
  'un détour':           "Le détour par le boulevard ajoute quinze minutes.",
  'une bretelle':        "La bretelle qui mène de la quinze nord à la quarante ouest est fermée.",

  // Défi 3 — l'imprévu, le retard annoncé
  'un imprévu':          "Un imprévu sur la route, ça s'annonce tout de suite.",
  'le covoiturage':      "Le covoiturage leur coûte moins cher que deux autos.",
  'un stationnement incitatif': "Ils se rejoignent au stationnement incitatif à six heures cinquante.",
  'prévenir':            "Elle a prévenu l'atelier avant même de quitter l'autoroute.",
};
