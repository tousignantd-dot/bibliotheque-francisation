const CARRIER_PHRASES = {
  // Une phrase porteuse par mot isolé à prononcer. Un mot envoyé seul à la
  // synthèse sort mal accentué ; la phrase le remet dans un contexte
  // français, et seul le mot est découpé.
  //
  // Les clés sont les mots **accentués**, tels qu'ils paraissent dans les
  // listes savoir[…][2] de exos.js — jamais en slug. Une clé écrite « prealable »
  // ne serait jamais trouvée, la pastille lirait le mot seul, et cela ne
  // s'entendrait qu'une fois les MP3 payés.
  //
  // Seize clés pour seize pastilles : les quatre bandeaux `speak:true` du
  // module sont ceux des quatre exercices « Vrai ou Faux », un par section.
  //
  // Les cartes de `prE` (`cards:true listen:true`) n'ont pas de clé ici, et
  // c'est normal : pour ce type d'exercice, le moteur lit le texte de la
  // rangée et non une phrase porteuse. C'est d'ailleurs voulu — ce qui doit
  // s'entendre là, c'est le mot exact, avec son « e » gardé ou tombé.

  // ── Je découvre : ce qui décide qui entre ──
  "un préalable":            "Il lui manque un préalable, et un seul.",
  "un programme contingenté": "C'est un programme contingenté depuis des années.",
  "une entrevue de sélection": "Elle a passé une entrevue de sélection mardi matin.",
  "un relevé de notes":      "Son relevé de notes est traduit depuis l'automne.",

  // ── Défi 1 : le dossier et la lettre ──
  "un dossier de candidature": "Elle a déposé son dossier de candidature le 26 février.",
  "une lettre de motivation":  "Il a relu sa lettre de motivation avant le dépôt.",
  "une pièce justificative":   "L'attestation est une pièce justificative, pas une opinion.",
  "une formule de courtoisie": "La lettre se ferme sur une formule de courtoisie.",

  // ── Défi 2 : l'entrevue ──
  "un comité de sélection": "Le comité de sélection reçoit deux personnes à la fois.",
  "un plan de carrière":    "Son plan de carrière tient en deux étapes.",
  "une aptitude":           "Rester calme est une aptitude, pas un diplôme.",
  "un stage":               "Le premier stage a lieu avant les fêtes.",

  // ── Défi 3 : le suivi ──
  "une liste d'attente":          "Son nom est sur la liste d'attente du groupe d'août.",
  "un rang":                      "Le rang ne se communique pas aux personnes candidates.",
  "une mise à niveau":            "Une mise à niveau de quelques semaines suffirait.",
  "la reconnaissance des acquis": "La reconnaissance des acquis est gratuite au centre.",
};
