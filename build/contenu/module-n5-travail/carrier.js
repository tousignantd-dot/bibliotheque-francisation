const CARRIER_PHRASES = {
  // La clé est le mot LITTÉRAL tel qu'il apparaît dans la liste FC_CARDS ou
  // dans la troisième colonne d'une rangée `savoir` à pastilles : le gabarit
  // fait `CARRIER_PHRASES[w]` sans normaliser. Une clé écrite autrement — en
  // slug, sans article, sans accent — ne serait jamais trouvée, et le mot
  // partirait seul à la synthèse, mal accentué.

  // Je découvre — le poste, les tâches, les directives
  'l\'accueil':               "Depuis lundi, elle travaille à l'accueil de la coopérative.",
  'une tâche':                "Répondre au téléphone est la première tâche de la journée.",
  'des directives':           "Les directives de l'appareil sont collées sur le mur.",
  'le registre des heures':   "Ghislain vérifie le registre des heures avant de répondre.",

  // Défi 1 — la boîte vocale et la note
  'une boîte vocale':         "Sa boîte vocale contenait quatre appels le lundi matin.",
  'un message d\'accueil':    "Elle a refait son message d'accueil trois fois.",
  'rappeler':                 "Elle promet de rappeler dans les meilleurs délais.",
  'une abréviation':          "RDV est une abréviation qui se comprend partout.",

  // Défi 2 — le mode d'emploi du matériel
  'un photocopieur':          "Le photocopieur du corridor a été remplacé jeudi.",
  'un mode d\'emploi':        "Le mode d'emploi de l'appareil fait quatre-vingts pages.",
  'le bac à papier':          "Le bac à papier du bas prend le format légal.",
  'un bourrage de papier':    "Un bourrage de papier se règle en trois gestes, sans forcer.",

  // Défi 3 — la démarche, le congé, l'absence
  'un formulaire':            "Le formulaire se prend au babillard, à côté du calendrier.",
  'une autorisation d\'absence': "Sans autorisation d'absence, la journée n'est pas payée.",
  'la paie':                  "C'est la paie qui envoie la confirmation par courriel.",
  'une réponse automatique':  "Sa réponse automatique donne la date du retour et un autre nom.",
};
