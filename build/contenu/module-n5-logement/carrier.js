const CARRIER_PHRASES = {
  // La clé est le mot LITTÉRAL tel qu'il apparaît dans un tableau `mots` d'un
  // bloc `savoir` : le gabarit fait `CARRIER_PHRASES[w]` sans normaliser. Une
  // clé écrite en style de nom de fichier (`avis_modification`) ne serait
  // jamais trouvée, et le mot partirait seul à la synthèse — mal accentué.
  'bail':                  "Le bail est signé pour un an.",
  'avis de modification':  "L'avis de modification arrive en février.",
  'loyer':                 "Le loyer se paie le premier du mois.",
  'quatre et demie':       "Elle cherche un quatre et demie.",
  'chauffé et éclairé':    "Le logement est chauffé et éclairé.",
  'date d\'occupation':    "La date d'occupation est le premier juillet.",
  'électroménagers':       "Les électroménagers sont fournis.",
  'buanderie':             "La buanderie est au sous-sol.",
  'case de stationnement': "Une case de stationnement vient avec le loyer.",
  'insonorisé':            "L'immeuble n'est pas insonorisé.",
  'ensoleillé':            "Le salon est ensoleillé le matin.",
  'bois franc':            "Il y a du bois franc dans le corridor.",
  'remise':                "La remise prend deux vélos.",
  'renouvellement':        "Le renouvellement se fait tout seul.",
  'sous-louer':            "Elle a le droit de sous-louer.",
  'tribunal':              "Le Tribunal administratif du logement tranchera.",
};
