const CARRIER_PHRASES = {
  // Les clés sont les mots tels qu'ils sont écrits dans les tableaux `speak`
  // des blocs `savoir` — au caractère près, accents compris. Une clé écrite
  // en slug (« piece » pour « pièce ») n'est jamais trouvée, et la pastille
  // lit alors le mot seul, mal accentué.
  'argent':             "Amadou met son argent dans son portefeuille.",
  'billet':             "Le guichet donne deux billets de vingt dollars.",
  'pièce':              "J'ai trois pièces dans ma poche.",
  'carte de débit':     "Sa carte de débit est dans son portefeuille.",
  'compte':             "Amadou a un compte depuis trois semaines.",
  'guichet automatique':"Le guichet automatique est libre : il n'y a personne.",
  'NIP':                "On ne dit jamais son NIP à voix haute.",
  'retrait':            "Il fait un retrait de quarante dollars.",
  'dépôt':              "Elle fait un dépôt de sa paie le vendredi.",
  'relevé':             "Amadou prend son relevé avant de partir.",
  'frais':              "Ce guichet demande des frais pour un retrait.",
  'chèque':             "Le centre sportif prend un chèque, pas le comptant.",
  'montant':            "Le montant du cours est de quarante-cinq dollars.",
  'signature':          "Sans signature, le chèque ne vaut rien.",
  'paiement direct':    "À l'épicerie, elle paie par paiement direct.",
  'comptant':           "Le centre sportif ne prend pas le comptant.",
};
