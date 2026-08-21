const CARRIER_PHRASES = {
  // La clé est le mot LITTÉRAL tel qu'il apparaît dans un tableau `mots` d'un
  // bloc `ana` ou dans la troisième colonne d'une rangée `savoir` à pastilles :
  // le gabarit fait `CARRIER_PHRASES[w]` sans normaliser. Une clé écrite
  // autrement ne serait jamais trouvée, et le mot partirait seul à la
  // synthèse — mal accentué, et parfois lu à l'anglaise.

  // Je découvre — les quatre portes du réseau de la santé
  'un GMF':                     "Sa clinique est devenue un GMF l'an dernier.",
  'le sans-rendez-vous':        "Le sans-rendez-vous ouvre à huit heures.",
  'une infirmière':             "Une infirmière répond au huit un un.",
  'une urgence':                "Une urgence, ça ne se prend pas en rendez-vous.",
  'un symptôme':                "Il a deux symptômes depuis le mois de mars.",

  // Je découvre — le vocabulaire de départ
  'la carte d\'assurance maladie': "Gardez la carte d'assurance maladie à côté de vous.",
  'un étourdissement':          "Un étourdissement passe en dix secondes.",
  'un médecin de famille':      "Un médecin de famille suit le même patient pendant des années.",

  // Défi 1 — l'appel
  'une disponibilité':          "Quelles sont vos disponibilités cette semaine ?",
  'un rendez-vous de suivi':    "Le rendez-vous de suivi est dans trois semaines.",
  'une agente administrative':  "Une agente administrative répond au téléphone.",
  'un rappel automatisé':       "Le rappel automatisé arrive la veille.",
  'une plage horaire':          "Je vous réserve une plage horaire de trente minutes.",

  // Défi 2 — dans le bureau
  'la tension artérielle':      "La tension artérielle se mesure avec un brassard.",
  'une prise de sang':          "La prise de sang se fait le matin.",
  'à jeun':                     "Il faut être à jeun douze heures avant.",
  'une ordonnance':             "Elle a signé l'ordonnance avant mon départ.",
  'un prélèvement':             "Le prélèvement dure deux minutes.",
  'un bilan sanguin':           "Le bilan sanguin vérifie le fer et la thyroïde.",

  // Défi 3 — déplacer ou annuler
  'déplacer un rendez-vous':    "Je voudrais déplacer un rendez-vous, s'il vous plaît.",
  'des frais d\'absence':       "La clinique facture des frais d'absence.",
  'une boîte vocale':           "L'annulation se laisse dans la boîte vocale.",
  'un délai d\'annulation':     "Le délai d'annulation est de vingt-quatre heures.",
};
