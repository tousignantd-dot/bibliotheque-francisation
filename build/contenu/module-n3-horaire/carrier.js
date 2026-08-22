const CARRIER_PHRASES = {
  // Les clés sont les mots **exactement tels qu'ils sont écrits** dans les
  // listes `savoir[…][2]` de exos.js — accents et apostrophes compris. Le
  // gabarit fait `CARRIER_PHRASES[w]` sur le mot affiché : une clé écrite en
  // slug ne serait jamais trouvée, et la pastille lirait le mot seul, mal
  // prononcé. Les quarante-cinq clés ci-dessous ont été relevées sur exos.js,
  // pas écrites de mémoire.

  // Je découvre — les lieux, les objets, les moments
  'le vestiaire':      "Le vestiaire est la porte grise, à côté de la cuisine.",
  'un casier':         "Mon uniforme propre est dans un casier du vestiaire.",
  'un uniforme':       "Je mets un uniforme propre avant chaque quart.",
  'poinçonner':        "Il faut poinçonner avant d'entrer dans la cuisine.",
  'un horaire':        "Un horaire de la semaine est affiché sur le tableau.",
  'une tâche':         "Sortir les plateaux est une tâche du matin.",
  "un chef d'équipe":  "Le chef d'équipe répond à toutes mes questions.",
  'le matin':          "Je travaille le matin, à partir de six heures.",
  "l'après-midi":      "Miguel travaille l'après-midi, jusqu'à vingt-deux heures.",
  'le soir':           "Le soir, la cafétéria ferme à vingt-deux heures.",
  'lundi':             "Lundi, je commence à six heures comme d'habitude.",
  'un congé':          "Samedi, je suis en congé toute la journée.",
  'une pause':         "Ma pause dure trente minutes, avant midi.",

  // Défi 1 — les petits mots de l'heure et les questions
  'de':                "Je travaille de six heures à quatorze heures.",
  'à':                 "Mon quart finit à quatorze heures pile.",
  "jusqu'à":           "Je reste jusqu'à quatorze heures aujourd'hui.",
  'à partir de':       "La cuisine est ouverte à partir de cinq heures.",
  'pendant':           "Je travaille pendant huit heures, sans arrêter.",
  'à quelle heure':    "À quelle heure est-ce que je commence demain ?",
  'quand':             "Quand est-ce que je travaille, cette semaine ?",
  'combien de temps':  "Combien de temps est-ce que la pause dure ?",
  'qui':               "Qui est-ce qui me remplace jeudi matin ?",
  'où':                "Où est-ce que je poinçonne, le matin ?",

  // Défi 2 — demander, répondre
  'pouvoir':           "Le verbe pouvoir sert à demander une permission.",
  'je peux':           "Est-ce que je peux prendre ma pause maintenant ?",
  'devoir':            "Le verbe devoir dit une obligation, pas un choix.",
  'je dois':           "Jeudi, je dois aller à la clinique avec mon garçon.",
  'il faut':           "Il faut aviser le chef d'équipe trois jours avant.",
  'vous pouvez':       "Monsieur Roy, est-ce que vous pouvez m'aider ?",
  'bien sûr':          "Oui, bien sûr, je viens tout de suite.",
  'je regrette':       "Je regrette, je suis occupée jusqu'à midi.",
  'désolée':           "Désolée, je finis mon quart à quatorze heures.",
  'une minute':        "Une minute, j'arrive avec le chariot.",
  'jeudi':             "Jeudi, Miguel prend mon quart du matin.",
  'merci beaucoup':    "Merci beaucoup, monsieur Roy, ça m'aide vraiment.",

  // Défi 3 — la consigne et l'avancement de la tâche
  'sortez':            "Sortez les plateaux du chariot, s'il vous plaît.",
  'rangez':            "Rangez les boîtes dans la chambre froide.",
  "n'oubliez pas":     "N'oubliez pas le four à onze heures.",
  'éteignez':          "Éteignez le four avant votre pause.",
  'venez':             "Venez me voir avant de partir, ce midi.",
  'faites':            "Faites les plateaux en premier, ce matin.",
  'je viens de':       "Je viens de finir les plateaux du deuxième étage.",
  'je suis en train de': "Je suis en train de ranger les dernières boîtes.",
  'je vais':           "Je vais éteindre le four dans trente minutes.",
  "c'est fait":        "Les plateaux, c'est fait, monsieur Roy.",
};
