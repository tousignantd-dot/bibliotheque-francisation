const CARRIER_PHRASES = {
  // Une phrase porteuse par mot isolé : un mot envoyé seul à la synthèse sort
  // mal prononcé, et parfois lu à l'anglaise. Seul le mot est découpé ensuite.
  //
  // Les clés sont les mots ACCENTUÉS, tels qu'ils paraissent dans les listes
  // savoir[…][2] de exos.js et dans les cartes de fccards.js. Une clé écrite
  // en slug n'est jamais trouvée, et la pastille lit alors le mot tout seul —
  // le défaut ne s'entend qu'une fois les MP3 payés.

  // Les dix-neuf mots du banc de vocabulaire, dont dix-sept servent aussi de
  // pastille dans un bandeau de savoir
  'un message implicite':     "« Vous méritez mieux » ne promet rien : c'est un message implicite.",
  'un slogan':                "Le slogan revient à la fin de chaque annonce, sur la même musique.",
  'un public cible':          "Le public cible de cette annonce, ce sont les parents de jeunes enfants.",
  'un annonceur':             "L'annonceur est responsable de ce que son annonce laisse croire.",
  'un abribus':               "Elle a lu la même annonce trois soirs de suite dans l'abribus.",
  'un panneau-réclame':       "Le panneau-réclame de la sortie change de message toutes les deux semaines.",
  'une capsule publicitaire': "La capsule publicitaire dure trente secondes, pas une de plus.",
  'une mention légale':       "La mention légale est dite en quatre secondes, à la toute fin.",
  'le débit':                 "Le débit double dans les cinq dernières secondes de l'annonce.",
  'un rabais':                "Le rabais ne s'applique qu'aux deux premiers mois.",
  'une circulaire':           "La circulaire du jeudi remplit la boîte aux lettres à elle seule.",
  'un dépliant':              "Elle a rapporté le dépliant du centre et l'a posé sur la table.",
  'un astérisque':            "Il y a un astérisque après le prix : la condition est écrite en bas.",
  'des frais d\'adhésion':    "Les frais d'adhésion de soixante dollars n'étaient pas dans la grosse ligne.",
  'un engagement':            "L'engagement est de douze mois, même si l'on cesse d'y aller.",
  'un témoignage':            "Le témoignage doit refléter l'opinion véritable de la personne.",
  'une publicité déguisée':   "Une vidéo payée qui ne le dit pas est une publicité déguisée.",
  'une commandite':           "La commandite doit être annoncée dès le début de la vidéo.",
  'l\'affichage':             "L'affichage se fait en français, et le français doit y être prédominant.",

  // Les douze mots de l'exercice sur le « e » avalé par le débit
  'depuis':        "Depuis lundi, la même capsule passe trois fois par heure.",
  'seulement':     "Elle a payé seulement trente dollars la première semaine.",
  'devant':        "Devant le comptoir, personne ne lit les petits caractères.",
  'gratuitement':  "On lui a envoyé la trottinette gratuitement, contre une vidéo.",
  'autrement':     "Autrement dit, vous payez pendant douze mois.",
  'rapidement':    "La fin de l'annonce est dite très rapidement.",
  'tenir':         "Il faut tenir le dépliant à la lumière pour lire le bas de la page.",
  'la semaine':    "La semaine prochaine, la vente recommencera sous un autre nom.",
  'le premier':    "Le premier relevé indiquait cent quatorze dollars et quatre-vingt-treize cents.",
  'samedi':        "Samedi matin, elle est allée en parler à son voisin.",
  'un atelier':    "Un atelier sur le budget se donne le mardi soir au Carrefour.",
  'finalement':    "Finalement, elle a écrit une lettre au centre d'entraînement.",
};
