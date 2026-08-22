const CARRIER_PHRASES = {
  // Une phrase porteuse par mot isolé à prononcer. Un mot envoyé seul à la
  // synthèse sort mal accentué, et parfois lu à l'anglaise — « un short » et
  // « un shérif » en sont deux candidats évidents. La phrase le remet dans un
  // contexte français ; seul le mot est découpé ensuite.
  //
  // Les clés sont les mots **accentués**, tels qu'ils paraissent dans les
  // listes savoir[…][2] de exos.js et dans les rangées de l'exercice à cartes.
  // Une clé écrite en slug ne serait jamais trouvée.

  // ── Les pastilles des bandeaux de savoir ──────────────────────────
  'une chronique pratique': "La chronique pratique du mardi dure huit minutes.",
  'une entrevue':           "L'entrevue avec la conseillère a duré vingt minutes.",
  'un documentaire':        "Le documentaire de dimanche durait cinquante-deux minutes.",
  'un fait divers':         "Le fait divers de la page cinq tenait en quinze lignes.",
  'le courrier des lecteurs': "Elle lit le courrier des lecteurs avant le reste du journal.",

  'la garantie légale':     "La garantie légale ne s'achète pas : elle est déjà là.",
  'une durée raisonnable':  "Trois ans, pour une laveuse de ce prix, n'est pas une durée raisonnable.",
  'une pièce de rechange':  "Le technicien attend une pièce de rechange depuis cinq semaines.",
  'une mise en demeure':    "Sa mise en demeure tenait sur une seule page.",
  'un recours':             "Beaucoup de gens jettent l'appareil sans savoir qu'ils ont un recours.",

  'un témoignage':          "L'émission commençait par le témoignage d'une retraitée.",
  'une enquête':            "Cette enquête a demandé deux ans de travail.",
  "l'obsolescence programmée": "L'expression obsolescence programmée sert aujourd'hui à tout expliquer.",
  'un organisme public':    "L'Office est un organisme public : l'appel ne coûte rien.",

  'une lettre ouverte':     "Sa lettre ouverte a paru le jeudi suivant.",
  'un point de vue':        "Les deux lettres défendent un point de vue opposé.",

  // ── Les mots de l'exercice de graphie-phonie ──────────────────────
  // « ch » qui se dit comme un k
  'une chronique':          "La chronique de Claudine Rousseau passe le mardi.",
  'une chronique du samedi': "Une chronique du samedi ne parle jamais du même sujet.",
  'la technique':           "La technique de réparation n'a pas changé depuis vingt ans.",
  'un chœur':               "Un chœur de voisins a signé la même lettre.",
  'la psychologie':         "La psychologie du consommateur intéresse les fabricants.",

  // « x » qui se dit comme un s
  'dix':                    "Le délai habituel est de dix jours.",
  'six':                    "Le commerçant a rappelé six jours plus tard.",
  'soixante':               "La laveuse pesait soixante kilos.",
  'Bruxelles':              "Le documentaire montrait aussi une usine près de Bruxelles.",

  // « sh » et « sch » qui se disent comme un ch
  'un schéma':              "La chronique était accompagnée d'un schéma très clair.",
  'un shérif':              "Le film racontait l'histoire d'un shérif de village.",
  'un short':               "Elle a rapporté un short au magasin la semaine passée.",
};
