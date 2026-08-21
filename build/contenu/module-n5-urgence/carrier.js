const CARRIER_PHRASES = {
  // La clé est le mot LITTÉRAL tel qu'il apparaît dans la liste FC_CARDS ou
  // dans la troisième colonne d'une rangée `savoir` à pastilles : le gabarit
  // fait `CARRIER_PHRASES[w]` sans normaliser. Une clé écrite autrement — en
  // slug, sans article, sans accent — ne serait jamais trouvée, et le mot
  // partirait seul à la synthèse, mal accentué.

  // Je découvre — hésiter, et savoir quel numéro composer
  'un malaise':            "Sa mère a eu un malaise en se levant.",
  'le 8-1-1':              "Le huit un un répond jour et nuit, gratuitement.",
  'faire de la fièvre':    "Elle fait de la fièvre depuis mercredi.",
  'perdre connaissance':   "Si elle perd connaissance, composez le neuf un un.",
  'une infirmière':        "Une infirmière répond au huit un un.",

  // Défi 1 — l'appel au 9-1-1
  'le 9-1-1':              "Elle a composé le neuf un un à deux heures du matin.",
  'un répartiteur':        "Le répartiteur lui a demandé de ne pas raccrocher.",
  'les ambulanciers':      "Les ambulanciers sont montés avec une civière.",
  'une civière':           "On l'a installée sur une civière avant de sortir.",

  // Défi 2 — le triage et l'attente
  'le triage':             "Au triage, elle a raconté la chute depuis le début.",
  'un niveau de priorité': "Chaque personne reçoit un niveau de priorité, de un à cinq.",
  'les signes vitaux':     "L'infirmière prend les signes vitaux avant ses questions.",
  'une radiographie':      "La radiographie a montré une fracture de la hanche.",

  // Défi 3 — l'étage, l'hospitalisation, le congé
  'une fracture':          "Une fracture de la hanche s'opère souvent le lendemain.",
  'une hospitalisation':   "Son hospitalisation a duré quatre jours.",
  'les heures de visite':  "Les heures de visite sont de onze heures à vingt heures.",
  'le congé de l\'hôpital': "Au congé de l'hôpital, on remet un résumé et des ordonnances.",
};
