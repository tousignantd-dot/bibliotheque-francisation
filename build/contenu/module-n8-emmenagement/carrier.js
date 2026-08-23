const CARRIER_PHRASES = {
  // Les clés sont les mots ACCENTUÉS, tels qu'ils paraissent dans les listes
  // savoir[…][2] de exos.js — jamais des slugs. Le gabarit fait
  // CARRIER_PHRASES[w] sur le mot affiché : une clé écrite « depreciation »
  // ne serait jamais trouvée, et la pastille lirait le mot seul, mal
  // prononcé. C'est exactement ce que la phrase porteuse existe pour éviter.
  //
  // Elles ont été relevées, pas écrites de mémoire : les quinze clés
  // ci-dessous sortent d'un comparatif dans les deux sens entre les listes
  // de exos.js et ce fichier.

  "un inventaire":              "Le chauffeur a signé un inventaire à huit heures.",
  "un connaissement":           "Elle a signé un connaissement sans le lire.",
  "une déclaration de valeur":  "Personne ne lui a offert une déclaration de valeur.",
  "concéder":                   "Il faut savoir concéder le point qui ne tient pas.",
  "une mise en demeure":        "Elle a envoyé une mise en demeure au transporteur.",

  "une franchise":              "Sa police porte une franchise de cinq cents dollars.",
  "un avenant":                 "Le refoulement d'égout est couvert par un avenant.",
  "la valeur à neuf":           "Elle est indemnisée selon la valeur à neuf.",
  "la dépréciation":            "Au jour du sinistre, la dépréciation retranche l'âge du bien.",
  "une exclusion":              "Le refus s'appuie sur une exclusion du contrat.",

  "un compromis":               "Elle propose un compromis appuyé sur une estimation.",
  "une clause":                 "Un refus sans une clause n'est pas un refus.",
  "un expert en sinistre":      "Un expert en sinistre établit les faits pour l'assureur.",
  "la subrogation":             "Par la subrogation, l'assureur se retourne contre le transporteur.",
  "une révision":               "Elle a demandé une révision par écrit.",
};
