const CARRIER_PHRASES = {
  // Une phrase porteuse par mot isolé : un mot envoyé seul à la synthèse sort
  // mal accentué, et parfois lu à l'anglaise. Seul le mot est découpé ensuite.
  //
  // Les clés sont les mots ACCENTUÉS, exactement comme ils paraissent dans les
  // listes savoir[…][2] de exos.js et dans fccards.js. Une clé écrite en slug
  // n'est jamais trouvée : la pastille lit alors le mot tout seul, et le
  // défaut ne s'entend qu'une fois les MP3 payés.

  // Les cinq mots du bandeau de « Je découvre »
  'un sujet de recherche':       "Chaque équipe reçoit un sujet de recherche différent et trois semaines.",
  'un mandat':                   "Le mandat tient en trois lignes : chercher, présenter, remettre un texte.",
  'animer une rencontre':        "Animer une rencontre, ce n'est pas parler le plus longtemps.",
  'la répartition des rôles':    "La répartition des rôles se fait avant la première rencontre.",
  'un échéancier':               "Notre échéancier tient sur une feuille : trois rencontres et une remise.",

  // Les mots du défi 1 — la personne-ressource et son sujet
  'une personne-ressource':      "La personne-ressource est venue un mardi soir et elle est restée une heure.",
  'la prise de notes':           "Sa prise de notes tient sur une page et il retrouve tout.",
  'une estimation':              "Dix degrés d'écart, c'est une estimation : la mesure vient d'une seule journée.",
  'un îlot de chaleur':          "Le stationnement du centre commercial est le plus gros îlot de chaleur du quartier.",
  'la canopée':                  "La canopée de ce secteur reste sous les dix pour cent.",
  "l'évapotranspiration":        "L'évapotranspiration refroidit l'air même quand on n'est pas sous l'arbre.",
  'un arbre de rue':             "Un arbre de rue mal arrosé meurt en silence, souvent au troisième été.",

  // Les mots du défi 2 — lire et résumer
  'la question de départ':       "Si la phrase ne répond pas à la question de départ, elle sort du résumé.",
  'une source fiable':           "Une source fiable porte une date : sans date, on ne sait pas ce qu'on cite.",
  "une fiche d'information":     "La fiche d'information de la ville tient sur deux écrans.",
  'un résumé':                   "Un résumé de dix lignes qui contient trois citations n'est pas un résumé.",

  // Les mots du défi 3 — animer et rendre compte
  'un tour de parole':           "Elle a donné un tour de parole à chacun avant d'ouvrir la discussion.",
  'un désaccord':                "Le désaccord portait sur ce qu'on note, pas sur le fait d'y aller.",
  'un consensus':                "On est arrivés à un consensus en reformulant les deux positions.",
  'un compte rendu':             "Le compte rendu part le soir même à ceux qui n'étaient pas là.",
};
