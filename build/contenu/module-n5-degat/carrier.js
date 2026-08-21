const CARRIER_PHRASES = {
  // La clé est le mot LITTÉRAL tel qu'il apparaît dans un tableau `mots` d'un
  // bloc `savoir` ou dans une carte de vocabulaire : le gabarit fait
  // `CARRIER_PHRASES[w]` sans normaliser. Un mot envoyé seul à la synthèse
  // sort mal accentué ; la phrase porteuse le remet dans un contexte, et seul
  // le mot est découpé.

  // Les seize mots du banc de vocabulaire
  "un dégât d'eau":         "Il y a eu un dégât d'eau dans la chambre.",
  'un cerne':               "Un cerne brun est apparu au plafond.",
  'le plafond':             "Le plafond de la chambre a coulé.",
  'une chaudière':          "Elle a mis une chaudière sous la fuite.",
  'gondoler':               "Le plancher a commencé à gondoler.",
  'un chauffe-eau':         "Le chauffe-eau du dessus a lâché.",
  'une fuite':              "Le plombier a trouvé la fuite tout de suite.",
  'une infiltration':       "Une infiltration a traversé le plancher.",
  'les dommages':           "Elle a décrit les dommages pièce par pièce.",
  'un avis':                "Un avis était affiché dans l'entrée.",
  "l'assèchement":          "L'assèchement a duré trois jours.",
  'un asséchateur':         "Un asséchateur souffle jour et nuit.",
  "l'accès au logement":    "L'avis demande de prévoir l'accès au logement.",
  'une réclamation':        "Elle a ouvert une réclamation le lendemain.",
  'une franchise':          "La franchise est de cinq cents dollars.",
  'une réduction de loyer': "Elle demande une réduction de loyer.",
  'une mise en demeure':    "La mise en demeure donne dix jours pour répondre.",

  // Les mots des encadrés de savoir
  'une photo':              "Prenez une photo avant que ça sèche.",
  'ne rien jeter':          "Il ne faut rien jeter avant le constat.",
  'ne jetez rien':          "Ne jetez rien avant le constat.",
  'avertir':               "Il faut avertir le propriétaire sans attendre.",
  'le bâtiment':            "Le bâtiment appartient au propriétaire.",
  'vos biens':              "Vos biens sont couverts par votre assurance.",
};
