const CARRIER_PHRASES = {
  // Les clés sont les mots tels qu'ils sont écrits dans les tableaux `speak`
  // des blocs `savoir` et dans FC_CARDS, article retiré — au caractère près,
  // accents compris. Une clé écrite en slug (« cafeteria » pour « cafétéria »)
  // n'est jamais trouvée, et la pastille lit alors le mot seul, mal accentué.
  'corridor':         "L'escalier est au milieu du corridor.",
  'étage':            "Le local 214 est au deuxième étage.",
  'escalier':         "Prenez l'escalier et montez un étage.",
  'ascenseur':        "L'ascenseur est à côté de l'escalier.",
  'rez-de-chaussée':  "L'accueil est au rez-de-chaussée.",
  'local':            "Mon cours est dans le local 214.",
  'porte':            "Le numéro est écrit sur la porte.",
  'numéro':           "Le numéro 214 commence par un 2.",
  'plan':             "Le plan du centre est près de l'accueil.",
  'casier':           "Mon casier est au rez-de-chaussée, le 015.",
  'secrétariat':      "Le secrétariat est en face de l'accueil.",
  'accueil':          "Demandez à l'accueil : ils connaissent tous les locaux.",
  'cafétéria':        "La cafétéria est à côté des casiers.",
  'toilettes':        "Les toilettes sont en face de l'ascenseur.",
  'sortie':           "La sortie est à côté de l'accueil.",
  'bibliothèque':     "La bibliothèque, c'est le local 108.",
};
