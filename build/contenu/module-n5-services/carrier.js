const CARRIER_PHRASES = {
  // La clé est le mot LITTÉRAL tel qu'il apparaît dans un tableau `mots` d'un
  // bloc `savoir` ou d'un bloc `ana` : le gabarit fait `CARRIER_PHRASES[w]`
  // sans normaliser. Une clé écrite autrement ne serait jamais trouvée, et le
  // mot partirait seul à la synthèse — mal accentué.

  // Je découvre — les trois bacs et les lieux
  'le bac gris':            "Le bac gris, c'est les ordures.",
  'le bac vert':            "Le bac vert se vide aux deux semaines.",
  'le bac brun':            "Le bac brun n'a pas été ramassé.",
  'un écocentre':           "Un écocentre reprend la vieille peinture.",
  'Info-collectes':         "Info-collectes donne l'horaire de votre rue.",
  'une brochure':           "La brochure est arrivée par la poste.",
  'les matières résiduelles': "La collecte des matières résiduelles change de jour.",
  'une preuve de résidence': "Il faut une preuve de résidence à l'entrée.",

  // Les trois voyelles nasales
  'attente':                "Le temps d'attente est de quatre minutes.",
  'résidence':              "Sa résidence principale est à Villeray.",
  'renseignement':          "Elle demande un renseignement au préposé.",
  'nom':                    "Je vous donne mon nom.",
  'réponse':                "La réponse arrive dans trois jours.",
  'information':            "Cette information vient du site de la Ville.",
  'matin':                  "Le camion passe le mardi matin.",
  'certain':                "Il est certain que le bac sera vidé.",
  'plein':                  "Le bac est plein depuis deux semaines.",

  // Défi 1 — l'appel
  'un préposé':             "Un préposé a fini par répondre.",
  'une requête':            "Elle a ouvert une requête au téléphone.",
  'un jour ouvrable':       "Comptez un jour ouvrable de plus.",
  'épeler':                 "Elle a dû épeler son code postal.",
  'un numéro de requête':   "Notez bien le numéro de requête.",
  'un délai':               "Le délai est de trois jours.",

  // Défi 2 — l'écran
  'un formulaire':          "Le formulaire se bloquait à la dernière page.",
  'en vigueur':             "Les tarifs en vigueur sont ceux d'avril.",
  'une matière refusée':    "Un pneu de camion est une matière refusée.",
  'un encadré':             "L'encadré gris dit l'essentiel.",
  'téléverser':             "Il faut téléverser une pièce justificative.",
  'une pièce justificative': "Joignez une pièce justificative à votre demande.",
  'le cas échéant':         "Indiquez votre ancien dossier, le cas échéant.",

  // Défi 3 — le guichet
  'un guichet':             "Elle s'est présentée au guichet.",
  'un billet de file d\'attente': "Prenez un billet de file d'attente en entrant.",
  'une pièce d\'identité':  "Apportez une pièce d'identité avec photo.",
  'un comptoir':            "Le comptoir trois est libre.",
  'il faut que':            "Il faut que vous apportiez deux pièces.",
  'il manque':              "Il manque une signature au bas de la page.",
  'il reste':               "Il reste dix minutes avant la fermeture.",
};
