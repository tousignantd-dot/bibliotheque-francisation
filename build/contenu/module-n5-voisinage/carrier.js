const CARRIER_PHRASES = {
  // La clé est le mot LITTÉRAL tel qu'il apparaît dans la liste FC_CARDS ou
  // dans la troisième colonne d'une rangée `savoir` à pastilles : le gabarit
  // fait `CARRIER_PHRASES[w]` sans normaliser. Une clé écrite autrement — en
  // slug, sans article, sans accent — ne serait jamais trouvée, et le mot
  // partirait seul à la synthèse, mal accentué. Aucun des seize mots de ce
  // module ne contient d'apostrophe : les clés se lisent telles quelles.
  //
  // Les seize mots servent tous de pastille au moins une fois dans un bloc
  // `savoir` à `speak:true` — vérification faite sur exos.js.

  // Je découvre — l'immeuble, la ruelle, le voisinage
  'une ruelle verte':     "La ruelle verte a été aménagée avec l'arrondissement.",
  'un hangar':            "Il répare la clôture du hangar chaque printemps.",
  'une corvée':           "La corvée de printemps réunit six logements sur douze.",
  'le voisinage':         "En trois ans, elle n'avait parlé à personne du voisinage.",

  // Défi 1 — l'invitation, la réponse, la justification
  'une invitation':       "Son invitation tenait en trois phrases, dans l'escalier.",
  'un plat à partager':   "Chaque logement apporte un plat à partager et sa chaise.",
  'reporter':             "S'il pleut, on reporte la fête au dimanche.",
  'un empêchement':       "Elle a un empêchement : elle travaille ce jour-là.",

  // Défi 2 — le répondeur, le message, le mot écrit
  'un répondeur':         "Le voyant du répondeur clignotait en rentrant du travail.",
  'un mot':               "Elle a laissé un mot sur la table de la cuisine.",
  'prévenir':             "Elle l'a prévenue deux semaines avant son départ.",
  'arroser':              "Quelqu'un doit arroser ses plantes du 10 au 20 juillet.",

  // Défi 3 — les nouvelles, les félicitations, la fête
  'des félicitations':    "Ses félicitations sont arrivées avant même les questions.",
  'la citoyenneté':       "Elle a obtenu sa citoyenneté après sept ans d'attente.",
  'une cérémonie':        "La cérémonie réunissait deux cents personnes.",
  'fêter':                "Il faut fêter ça, ne serait-ce qu'avec un café.",
};
