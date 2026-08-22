const CARRIER_PHRASES = {
  // Les clés sont les mots tels qu'ils sont écrits dans les tableaux `speak`
  // des blocs `savoir` — au caractère près, accents et trait d'union compris.
  // Une clé écrite en slug (« rez-de-chaussee » pour « rez-de-chaussée ») n'est
  // jamais trouvée, et la pastille lit alors le mot seul, mal accentué.
  'secrétariat':      "Amel va au secrétariat pour demander une attestation.",
  'secrétaire':       "La secrétaire demande le nom et le groupe.",
  'concierge':        "Le concierge ouvre la porte à sept heures.",
  'enseignante':      "Mon enseignante s'appelle madame Dufresne.",
  'couloir':          "Le local 214 est au bout du couloir.",
  'rez-de-chaussée':  "Le secrétariat est au rez-de-chaussée.",
  'étage':            "Mon cours est au deuxième étage.",
  'local':            "Le local 214 est à droite de l'escalier.",
  'comptoir':         "Amel attend au comptoir du secrétariat.",
  'attestation':      "Mon attestation est prête jeudi.",
  'horaire':          "L'horaire du secrétariat est sur la porte.",
  'absence':          "Je préviens la secrétaire de mon absence.",
  'avis':             "L'avis dit que le centre est fermé lundi.",
  'congé':            "Lundi, c'est un congé : le centre est fermé.",
  'direction':        "La direction signe l'avis affiché sur la porte.",
  'porte fermée':     "À midi, c'est une porte fermée : le bureau ouvre à treize heures.",
};
