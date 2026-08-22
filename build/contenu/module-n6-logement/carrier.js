const CARRIER_PHRASES = {
  // Une phrase porteuse par mot isolé à prononcer. Un mot envoyé seul à la
  // synthèse sort mal accentué ; la phrase le remet dans un contexte
  // français, et seul le mot est découpé.
  //
  // Les clés sont les mots **accentués**, tels qu'ils paraissent dans les
  // listes savoir[…][2] de exos.js. Une clé écrite en slug ne serait jamais
  // trouvée, et la pastille lirait le mot seul sans que rien ne le signale.

  // ── Les pastilles des bandeaux de savoir (les seize mots du module) ──
  'un locateur':             "Le locateur habite le rez-de-chaussée du même immeuble.",
  'un bail':                 "Son bail se termine le trente juin.",
  'une clause':              "Aucune clause du bail ne parle de la sous-location.",
  'un avis':                 "Elle a remis son avis en main propre le dix-huit novembre.",
  'un délai':                "Le délai de réponse est de quinze jours.",
  'la reconduction':         "La reconduction se fait sans papier si personne n'écrit.",

  'la sous-location':        "Pendant la sous-location, elle reste responsable du loyer.",
  'la cession de bail':      "Une cession de bail ne se reprend pas.",
  'la résiliation':          "La résiliation met fin au bail avant son terme.",
  'un motif sérieux':        "Un refus doit s'appuyer sur un motif sérieux.",
  'les obligations':         "Payer le premier du mois fait partie de ses obligations.",

  'le consentement':         "Son silence pendant quinze jours vaut consentement.",
  'un accusé de réception':  "Elle a demandé un accusé de réception signé sur sa copie.",
  'une indemnité':           "Il réclame une indemnité pour ses frais réels.",
  'des dommages':            "Les dommages au plancher ont été photographiés.",
  'le défaut de paiement':   "Un défaut de paiement laisse une trace au dossier.",

  // ── Les douze mots de l'exercice de graphie-phonie ──────────────────
  // Le pilote du niveau 6 l'a vérifié : pour un `vf` à cards + listen, le
  // relevé de `build/releve_sons.js` rend le **texte de la rangée**, pas la
  // phrase porteuse. Ces douze clés ne sont donc pas lues par le moteur, et
  // `node build/coherence.js` a raison de ne pas les compter comme un écart.
  // Elles restent ici pour deux raisons : elles disent au lecteur dans quel
  // sens le mot doit s'entendre, et le générateur audio, lui, fait passer ces
  // mots par `enrichir()` de `build/voix.py` — « un flash », « un sushi » et
  // « un t-shirt » existent en anglais et sortiraient à l'anglaise sans
  // contexte français, alors que c'est justement leur prononciation française
  // que l'élève doit entendre.
  'une chorale':             "Une chorale répète au sous-sol de l'église.",
  'la technologie':          "La technologie n'a rien changé au délai de quinze jours.",
  'un psychologue':          "Un psychologue reçoit au deuxième étage.",
  'le chaos':                "Le chaos du déménagement dure deux jours.",
  'dix-huit':                "L'avis est daté du dix-huit novembre.",
  'soixante-quinze':         "Le chèque était de soixante-quinze dollars.",
  'six mois':                "Elle part six mois à Sept-Îles.",
  'dix jours':               "Il lui restait dix jours pour répondre.",
  'un schéma':               "Un schéma de l'immeuble est affiché dans le hall.",
  'un sushi':                "Un sushi coûte moins cher qu'un déménagement.",
  'un flash':                "Un flash de caméra éclaire le plancher abîmé.",
  'un t-shirt':              "Elle portait un t-shirt gris le jour du déménagement.",
};
