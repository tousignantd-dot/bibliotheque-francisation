const CARRIER_PHRASES = {
  // Les clés sont les mots et les expressions **exactement tels qu'ils sont
  // écrits** dans les listes `savoir[…][2]` de exos.js — accents et
  // apostrophes compris. Le gabarit fait `CARRIER_PHRASES[w]` sur le mot
  // affiché : une clé écrite en slug ne serait jamais trouvée, et la pastille
  // lirait le mot seul, mal prononcé.

  // Les lieux du casse-croûte
  'le comptoir':           "On fait la file devant le comptoir.",
  'le tableau du menu':    "Le tableau du menu est au-dessus de la caisse.",
  'un plateau':            "Prends un plateau au bout du comptoir.",
  'la caisse':             "On paie à la caisse avant de manger.",
  'un casse-croûte':       "Chez Marcel, c'est un casse-croûte.",

  // Les formats
  'petit':                 "Un petit, s'il vous plaît.",
  'moyen':                 "Le format moyen est celui du milieu.",
  'grand':                 "Un grand café pour emporter.",
  'une petite soupe':      "Une petite soupe, s'il vous plaît.",
  'une grande salade':     "Une grande salade suffit pour deux.",
  "un petit s'il vous plaît": "Un petit, s'il vous plaît.",
  'une portion':           "La portion de frites est grosse.",

  // Ce qu'il y a dans le plat
  'un sandwich au poulet': "Je voudrais un sandwich au poulet.",
  'une soupe à la tomate': "Une soupe à la tomate, format moyen.",
  "à l'oignon":            "Une salade à l'oignon, s'il vous plaît.",
  'une soupe aux légumes': "Une soupe aux légumes, s'il vous plaît.",
  'un sandwich aux œufs':  "Un sandwich aux œufs et un jus.",
  'sans mayonnaise':       "Un sandwich sans mayonnaise, s'il vous plaît.",

  // Montrer du doigt
  'ce sandwich':           "Ce sandwich coûte six dollars.",
  'cet accompagnement':    "Cet accompagnement est compris dans le prix.",
  'cette soupe':           "Cette soupe est aux légumes.",
  'ce sandwich-là':        "Ce sandwich-là, c'est quoi ?",

  // La formule polie
  'je voudrais un café':   "Je voudrais un café, s'il vous plaît.",
  'je voudrais':           "Je voudrais un trio au poulet.",
  "j'aimerais une soupe":  "J'aimerais une soupe, s'il vous plaît.",
  'est-ce que je peux avoir': "Est-ce que je peux avoir une serviette ?",
  "s'il vous plaît":       "Un jus de pomme, s'il vous plaît.",

  // Les questions du préposé
  "oui c'est tout":        "Oui, c'est tout, merci.",
  "avec salade s'il vous plaît": "Avec salade, s'il vous plaît.",
  'quel format':           "Quel format ? Petit, moyen ou grand ?",
  'pour ici ou pour emporter': "Pour ici ou pour emporter ?",
  'pour emporter':         "Un café pour emporter, s'il vous plaît.",
  'débit ou comptant':     "Débit ou comptant ?",

  // Les condiments et les ustensiles
  'du sel':                "Est-ce que je peux avoir du sel ?",
  'du ketchup':            "Je voudrais du ketchup pour mes frites.",
  'de la moutarde':        "Il y a de la moutarde au bout du comptoir.",
  "de l'eau":              "Est-ce qu'il y a de l'eau quelque part ?",
  'des serviettes':        "Prenez des serviettes, la soupe est pleine.",
  'des ustensiles':        "Les ustensiles sont dans les bacs.",
  'un peu de sel':         "Je mets un peu de sel sur ma soupe.",

  // Demander ce qui manque
  "je n'ai pas de cuillère": "Excusez-moi, je n'ai pas de cuillère.",
  'il manque le jus':      "Il manque le jus dans mon plateau.",
  'où sont les serviettes': "Où sont les serviettes, s'il vous plaît ?",
  'est-ce que je peux en prendre deux': "Est-ce que je peux en prendre deux ?",
  'servez-vous':           "Servez-vous, c'est en libre-service.",
  "ce n'est pas ma commande": "Excusez-moi, ce n'est pas ma commande.",
  'pouvez-vous répéter':   "Pouvez-vous répéter, s'il vous plaît ?",

  // Quand il n'en reste plus
  "il n'y a plus de soupe": "Il n'y a plus de soupe aujourd'hui.",
  'plus de frites':        "Il n'y a plus de frites ce midi.",
  "il n'en reste plus":    "Le jus de pomme ? Il n'en reste plus.",
  "qu'est-ce que vous avez d'autre": "Qu'est-ce que vous avez d'autre ?",
};
