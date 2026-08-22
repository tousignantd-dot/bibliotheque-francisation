const CARRIER_PHRASES = {
  // Les clés sont les mots et les expressions **exactement tels qu'ils sont
  // écrits** dans les listes `savoir[…][2]` de exos.js — accents et
  // apostrophes compris. Le gabarit fait `CARRIER_PHRASES[w]` sur le mot
  // affiché : une clé écrite en slug ne serait jamais trouvée, et la pastille
  // lirait le mot seul, mal prononcé.
  // Les 82 clés ci-dessous ont été relevées, pas écrites de mémoire.

  // ── Je découvre · le centre de quartier ──────────────────
  'un centre communautaire': "Il y a un centre communautaire sur la rue Galt.",
  'le quartier':             "Le centre, c'est le quartier qui le fait vivre.",
  'un babillard':            "Les annonces sont sur un babillard.",
  'une punaise':             "La feuille est tenue par une punaise.",
  'un feuillet':             "Le centre a publié un feuillet d'automne.",
  'une activité':            "Le badminton est une activité du mardi.",
  'une session':             "Une session dure une douzaine de semaines.",
  "l'automne":               "La session commence à l'automne.",
  'gratuit':                 "Le ciné-club du vendredi est gratuit.",
  'le tarif':                "Le tarif du quartier est de trois dollars.",

  // ── Je découvre · les jours ──────────────────────────────
  'mardi':                   "Mardi, j'essaie le badminton.",
  'jeudi':                   "Jeudi, il y a de la danse en ligne.",
  'le mardi':                "Le mardi, le gymnase est réservé au badminton.",
  'le samedi':               "Le samedi, le centre ouvre à neuf heures.",
  'le mardi soir':           "Le badminton libre, c'est le mardi soir.",
  'mercredi':                "Mercredi, la cuisine collective se réunit.",
  'vendredi':                "Vendredi, le ciné-club présente un film.",
  'dimanche':                "Dimanche, le centre est fermé.",
  'le samedi matin':         "L'heure des familles est le samedi matin.",
  'le jeudi soir':           "La danse en ligne a lieu le jeudi soir.",

  // ── Défi 1 · poser sa question ───────────────────────────
  "c'est quand":             "Le badminton, c'est quand ?",
  "c'est combien":           "Une séance, c'est combien ?",
  "c'est où":                "Le gymnase, c'est où ?",
  'est-ce que':              "Est-ce que le centre est ouvert ?",
  "est-ce qu'il faut apporter quelque chose": "Est-ce qu'il faut apporter quelque chose ?",
  "quand est-ce que ça commence":  "Quand est-ce que ça commence ?",
  "combien est-ce que ça coûte":   "Combien est-ce que ça coûte ?",
  'à quelle heure commence le cours': "À quelle heure commence le cours ?",
  'combien coûte la session': "Combien coûte la session ?",
  'ça commence-tu cette semaine': "Ça commence-tu cette semaine ?",
  "qu'est-ce qu'il faut apporter": "Qu'est-ce qu'il faut apporter ?",

  // ── Défi 1 · demander poliment ───────────────────────────
  'je voudrais':             "Bonjour, je voudrais un renseignement.",
  'je voudrais des renseignements': "Je voudrais des renseignements, s'il vous plaît.",
  "j'aimerais":              "J'aimerais essayer une fois.",
  "j'aimerais essayer":      "J'aimerais essayer le badminton.",
  'je pourrais':             "Je pourrais venir voir jeudi.",
  'est-ce que je pourrais':  "Est-ce que je pourrais venir voir ?",
  'vous pourriez':           "Vous pourriez m'aider, s'il vous plaît ?",
  'vous pourriez répéter':   "Vous pourriez répéter, s'il vous plaît ?",
  'il faudrait':             "Il faudrait apporter une preuve d'adresse.",
  'il faut':                 "Il faut des espadrilles propres.",
  'vous voudriez':           "Vous voudriez essayer une fois ?",

  // ── Défi 2 · l'heure ─────────────────────────────────────
  'dix-neuf heures trente':  "La séance est à dix-neuf heures trente.",
  "l'heure officielle":      "Le feuillet donne l'heure officielle.",
  'sept heures et demie':    "Le film commence à sept heures et demie.",
  'du soir':                 "C'est à sept heures du soir.",
  'neuf heures':             "Le badminton finit à neuf heures.",
  'midi':                    "Le centre ferme une heure à midi.",
  'et demie':                "Rendez-vous à sept heures et demie.",
  'et quart':                "La cuisine commence à une heure et quart.",
  'moins quart':             "Le centre ferme à neuf heures moins quart.",
  'de sept heures à neuf heures': "Le gymnase est libre de sept heures à neuf heures.",
  'du matin':                "L'heure des familles est à dix heures du matin.",

  // ── Défi 2 · l'adjectif ──────────────────────────────────
  'une séance courte':       "Le documentaire fait une séance courte.",
  'une histoire vraie':      "Ce film raconte une histoire vraie.",
  'des films courts':        "La soirée présente des films courts.",
  'un film drôle':           "La comédie est un film drôle.",
  'une histoire triste':     "Le drame raconte une histoire triste.",
  'une entrée gratuite':     "Les enfants ont une entrée gratuite.",
  'un gros chaudron':        "L'eau bout dans un gros chaudron.",
  'une belle soirée':        "Nous avons passé une belle soirée.",

  // ── Défi 3 · l'impératif de la recette ───────────────────
  'pelez':                   "Pelez six pommes de terre.",
  'coupez':                  "Coupez les légumes en morceaux.",
  'ajoutez':                 "Ajoutez soixante millilitres de lait.",
  'mélangez':                "Mélangez jusqu'à ce que ce soit lisse.",
  'coupe les oignons':       "Coupe les oignons, s'il te plaît.",
  'faites bouillir':         "Faites bouillir vingt minutes.",
  'mettez':                  "Mettez le chaudron sur le rond arrière.",
  'égouttez':                "Égouttez les pommes de terre.",
  'écrasez':                 "Écrasez le tout avec le presse-purée.",
  'coupez-les en gros morceaux': "Coupez-les en gros morceaux.",

  // ── Défi 3 · les quantités ───────────────────────────────
  'du lait':                 "La recette demande du lait.",
  'de la crème':             "On peut ajouter de la crème.",
  "de l'eau":                "Faites chauffer de l'eau.",
  'des pommes de terre':     "Pelez des pommes de terre.",
  'des oignons':             "Coupez des oignons en petits dés.",
  'un peu de sel':           "Mettez un peu de sel, pas plus.",
  "beaucoup d'eau":          "Il faut beaucoup d'eau dans le chaudron.",
  'pas de maïs':             "Camila ne veut pas de maïs.",
  "un peu d'huile":          "Ajoutez un peu d'huile dans la poêle.",
  'tout le lait':            "Ne versez pas tout le lait d'un coup.",
  'toutes les portions':     "Comptez toutes les portions avant de partir.",
};
