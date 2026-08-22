const CARRIER_PHRASES = {
  // Une phrase porteuse par mot isolé à prononcer. Un mot envoyé seul à la
  // synthèse sort mal accentué, et parfois lu à l'anglaise. La phrase le
  // remet dans un contexte français ; seul le mot est ensuite découpé.
  //
  // Les clés sont les mots **accentués**, tels qu'ils paraissent dans les
  // listes savoir[…][2] de exos.js. Une clé écrite en slug — « prealable »
  // pour « un préalable » — ne serait jamais trouvée par le gabarit, qui fait
  // CARRIER_PHRASES[w] sur le mot affiché. Rien ne le signalerait : le build
  // passe, l'audio se paie, et le défaut ne s'entend qu'à l'écoute.

  // ── Les seize pastilles des bandeaux de savoir ────────────────────
  "une conseillère d'orientation": "La conseillère d'orientation reçoit le lundi et le jeudi.",
  'un dossier scolaire':          "Rien ne compte tant que ce n'est pas au dossier scolaire.",
  'un relevé de notes':           "Elle a demandé son relevé de notes au comptoir.",
  "l'enseignement individualisé": "Au centre, presque tout se fait en enseignement individualisé.",
  'une matière':                  "Il lui manque des unités dans deux matières.",

  "un programme d'études":        "Le programme d'études dure onze mois à temps plein.",
  'un préalable':                 "Le français est le préalable dont dépendent tous les autres.",
  'la formation professionnelle': "La formation professionnelle ne se donne pas dans le même édifice.",
  'une évaluation comparative':   "Son évaluation comparative tient sur deux pages.",
  'la reconnaissance des acquis': "Ses six ans de pharmacie valent quelque chose en reconnaissance des acquis.",

  'un avis officiel':             "L'avis officiel tenait sur une seule page.",
  'une admission conditionnelle': "Une admission conditionnelle réserve la place, elle ne la donne pas.",
  'un encadré':                   "Les préalables particuliers sont dans l'encadré gris de la page trois.",

  'une rencontre de suivi':       "La rencontre de suivi a duré une heure exactement.",
  'un plan de formation':         "Le plan de formation porte maintenant la date du six février.",
  'un compte rendu':              "Sans compte rendu, personne ne se rappellera les quatre dates.",

  // ── Les mots de l'exercice de graphie-phonie ──────────────────────
  // Ces clés-là sont **inutilisées par le moteur** et gardées pour mémoire :
  // pour un exercice `vf` à cards/listen, le gabarit lit le texte de la
  // rangée, pas la phrase porteuse. `node build/coherence.js` ne compte pas
  // une clé inutilisée comme un écart, et il a raison. Les mots partent donc
  // seuls à la synthèse — c'est `enrichir()` de build/voix.py qui leur pose
  // un contexte français, sans quoi « un short » et « un shampoing »
  // sortiraient à l'anglaise, et c'est exactement la prononciation française
  // que l'élève doit entendre.

  // « ch » et « ck » qui se disent comme un k
  'la psychologie':   "La psychologie fait partie des matières du programme.",
  'une chronologie':  "La première page donne une chronologie du centre.",
  'un orchestre':     "Un orchestre répète au sous-sol le mercredi soir.",
  'une chorale':      "La chorale du centre chante deux fois par année.",
  'un écho':          "On entend un écho dans le grand local du fond.",
  'la technologie':   "La technologie de laboratoire s'apprend en atelier.",

  // « x » qui se dit comme un s
  'six':              "Le stage dure six semaines.",
  'dix':              "Elle a rendez-vous à dix heures.",
  'soixante':         "Le centre a ouvert il y a soixante ans.",

  // « sh » et « sch » qui se disent comme un ch
  'un schéma':        "La brochure était accompagnée d'un schéma très clair.",
  'un shampoing':     "Un shampoing se vend moins cher en grand format.",
  'un short':         "Il faut apporter un short pour le cours d'éducation physique.",
};
