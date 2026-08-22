const CARRIER_PHRASES = {
  // Une phrase porteuse par mot isolé à prononcer. Un mot envoyé seul à la
  // synthèse sort mal accentué, et parfois lu à l'anglaise. La phrase le
  // remet dans un contexte français ; seul le mot est ensuite découpé.
  //
  // Les clés sont les mots **accentués**, tels qu'ils paraissent dans les
  // listes savoir[…][2] de exos.js : le gabarit fait CARRIER_PHRASES[w] sur
  // le mot affiché. Une clé écrite en slug ne serait jamais trouvée, rien ne
  // le signalerait, et le défaut ne s'entendrait qu'une fois les MP3 payés.

  // ── Les seize pastilles des bandeaux de savoir ────────────────────
  'un travail de recherche':  "Le travail de recherche se fait en équipe de trois.",
  'un sujet de recherche':    "Leur sujet de recherche tient en une seule question.",
  'un compte rendu':          "Chaque équipe présente son compte rendu en cinq minutes.",
  'un exposé':                "Son exposé tenait en trois temps, sans une feuille lue.",
  'une échéance':             "L'échéance est le vingt-quatre novembre pour tout le monde.",

  'une consigne de travail':  "La consigne de travail tient sur une page et demie.",
  "une grille d'évaluation":  "La grille d'évaluation est donnée en même temps que la consigne.",
  'un barème':                "Selon le barème, le contenu vaut huit points sur vingt.",
  'un plan de travail':       "Ils ont écrit leur plan de travail avant la première phrase.",
  'une idée principale':      "Chaque paragraphe ne porte qu'une idée principale.",

  'une source':               "Le travail demande trois sources, et pas trois fois la même.",
  'un article informatif':    "L'article informatif raconte la première année de la collecte.",
  'un bulletin municipal':    "Le bulletin municipal paraît quatre fois par année.",
  'le courrier des lecteurs': "Une lettre parue dans le courrier des lecteurs dit le contraire.",
  'une bibliographie':        "Leur bibliographie compte trois entrées, chacune avec sa date.",
  'une citation':             "Une citation sans guillemets n'est plus une citation.",

  // ── Les mots de l'exercice de graphie-phonie ──────────────────────
  // Ces clés-là sont **inutilisées par le moteur** et gardées pour mémoire :
  // pour un exercice `vf` à cards/listen, le gabarit lit le texte de la
  // rangée, pas la phrase porteuse. `node build/coherence.js` ne compte pas
  // une clé inutilisée comme un écart, et il a raison. Les mots partent donc
  // seuls à la synthèse — c'est `enrichir()` de build/voix.py qui leur pose
  // un contexte français, sans quoi « un short » et « un shampoing »
  // sortiraient à l'anglaise, et c'est justement la prononciation française
  // que l'élève doit entendre.

  // « ch » qui se dit comme un k
  'le chlore':       "Le chlore de la piscine se sent dès l'entrée.",
  'un chronomètre':  "Elle répète son exposé avec un chronomètre.",
  "l'archéologie":   "L'archéologie était l'un des huit sujets de la liste.",
  'le chaos':        "Le dernier jour, c'est le chaos dans toutes les équipes.",
  'la technique':    "La technique du plan s'apprend une fois pour toutes.",
  'une orchidée':    "Une orchidée est posée sur le comptoir de la bibliothèque.",

  // « x » qui se dit comme un s
  'six':             "Le travail vaut six points de plus que le précédent.",
  'dix':             "Ils ont dix jours pour trouver leur troisième source.",
  'soixante':        "La liste comptait soixante titres au catalogue.",

  // « sh » et « sch » qui se disent comme un ch
  'un schéma':       "La page de la ville était accompagnée d'un schéma très clair.",
  'un shampoing':    "Un shampoing se vend moins cher en grand format.",
  'un short':        "Il faut apporter un short pour le cours d'éducation physique.",
};
