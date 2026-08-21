const CARRIER_PHRASES = {
  // Les clés sont les mots tels qu'ils sont écrits dans les tableaux `speak`
  // des blocs `savoir` — au caractère près, accents compris. Une clé écrite
  // en slug (« temperature » pour « température ») n'est jamais trouvée, et
  // la pastille lit alors le mot seul, mal accentué.
  'neige':          "Il y a vingt centimètres de neige sur le trottoir.",
  'pluie':          "Prends ton parapluie : il y a de la pluie.",
  'vent':           "Le vent est froid ce matin.",
  'soleil':         "Demain, il y a du soleil.",
  'nuage':          "Il y a beaucoup de nuages aujourd'hui.",
  'température':    "La température est de moins huit degrés.",
  'bulletin météo': "Zina écoute le bulletin météo à sept heures.",
  'degré':          "Il fait moins huit degrés à Montréal.",
  'hiver':          "En hiver, il fait souvent moins vingt.",
  'saison':         "L'été est ma saison préférée.",
  'ville':          "À Québec, la ville est plus froide qu'à Montréal.",
  'manteau':        "En janvier, je mets mon manteau d'hiver.",
  'tuque':          "Il vente : mets ta tuque !",
  'mitaines':       "Youssef cherche ses mitaines dans le sac.",
  'bottes':         "Avec la neige, je mets mes bottes.",
  'tempête':        "Le centre est fermé : il y a une tempête.",
};
