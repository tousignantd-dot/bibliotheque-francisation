const CARRIER_PHRASES = {
  // Une phrase porteuse par mot isolé à prononcer. Un mot envoyé seul à la
  // synthèse sort mal accentué, et parfois lu à l'anglaise. La phrase le
  // remet dans un contexte français ; seul le mot est ensuite découpé.
  //
  // Les clés sont les mots **accentués**, tels qu'ils paraissent dans les
  // listes savoir[…][2] de exos.js. Une clé écrite en slug — « antecedent »
  // pour « un antécédent » — ne serait jamais trouvée par le gabarit, qui
  // fait CARRIER_PHRASES[w] sur le mot affiché. Rien ne le signalerait : le
  // build passe, l'audio se paie, et le défaut ne s'entend qu'à l'écoute.

  // ── Les seize pastilles des bandeaux de savoir ────────────────────
  'une clinique externe':          "La clinique externe ferme à seize heures et n'ouvre pas la fin de semaine.",
  'une demande de consultation':   "La demande de consultation est partie en avril et l'appel est venu en octobre.",
  'la médecine interne':           "Elle a été dirigée en médecine interne, au troisième étage.",
  "un délai d'attente":            "Le délai d'attente a été de sept mois, et ce n'était pas le plus long.",
  'un dossier médical':            "Ses résultats de mars étaient déjà au dossier médical.",

  'un malaise':                    "Elle est venue pour un malaise qui n'a ni endroit ni date précise.",
  'la fatigue chronique':          "Ce que le repos ne répare pas en trois nuits porte un nom : la fatigue chronique.",
  'un proche aidant':              "Il attend deux heures chaque mardi : c'est un proche aidant.",
  'les heures de visite':          "Les heures de visite sont affichées à côté de l'ascenseur.",

  'un antécédent':                 "Elle a mis ses antécédents sur une feuille pour ne plus les chercher de mémoire.",
  'un prélèvement':                "Le prélèvement se fait au rez-de-chaussée, sans rendez-vous.",
  'un diagnostic':                 "Elle est ressortie sans diagnostic et avec un plan.",
  'une anémie':                    "Le mot anémie était écrit sur la feuille de mars, sans une ligne d'explication.",

  'les effets secondaires':        "Le feuillet consacre un paragraphe entier aux effets secondaires.",
  "un feuillet d'information":     "Le feuillet d'information tient sur une page et se garde sur le réfrigérateur.",
  'un suivi':                      "Sans date écrite, un suivi est une intention et rien de plus.",

  // ── Les mots de l'exercice de graphie-phonie ──────────────────────
  // Ces clés-là sont **inutilisées par le moteur** et gardées pour mémoire :
  // pour un exercice `vf` à cards/listen, le gabarit lit le texte de la
  // rangée, pas la phrase porteuse. `node build/coherence.js` ne compte pas
  // une clé inutilisée comme un écart, et il a raison. Ces mots partent donc
  // **seuls** à la synthèse — c'est `enrichir()` de build/voix.py qui leur
  // pose un contexte français, sans quoi « un short » et « un shampoing »
  // sortiraient à l'anglaise, et c'est justement la prononciation française
  // que l'élève doit entendre ici.
  'une échographie':               "Une échographie se fait au deuxième étage.",
  'chronique':                     "Une fatigue chronique dure des mois.",
  'un psychiatre':                 "Le psychiatre reçoit au pavillon B.",
  'le cholestérol':                "Le cholestérol se mesure dans le même prélèvement.",
  'la technique':                  "La technique est expliquée sur le feuillet.",
  'un écho':                       "On entend un écho dans le long corridor.",
  'six':                           "Elle revient dans six semaines.",
  'dix':                           "Il reste dix personnes avant elle.",
  'soixante-dix':                  "La salle compte soixante-dix places.",
  'un schéma':                     "Le feuillet montre un schéma des étages.",
  'un shampoing':                  "Elle a noté même le shampoing sur sa liste.",
  'un short':                      "Apportez un short pour l'examen à l'effort.",
};
