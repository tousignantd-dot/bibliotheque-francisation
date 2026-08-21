const CARRIER_PHRASES = {
  // Les clés sont les mots et les expressions **exactement tels qu'ils sont
  // écrits** dans les listes `savoir[…][2]` de exos.js — accents et
  // apostrophes compris. Le gabarit fait `CARRIER_PHRASES[w]` sur le mot
  // affiché : une clé écrite en slug ne serait jamais trouvée, et la pastille
  // lirait le mot seul, mal prononcé.
  //
  // Les quarante-trois clés ont été relevées sur `exos.js` par un script, pas
  // écrites de mémoire. Celles qui sont déjà des phrases entières reçoivent
  // quand même une porteuse : elle leur donne une intonation de comptoir
  // plutôt qu'une lecture plate.

  // Je découvre — les mots du bureau de poste
  'un bureau de poste':      "Le bureau de poste de la 3e Avenue ouvre à neuf heures.",
  'un préposé':              "Le préposé pèse la boîte avant de dire le prix.",
  'un envoi':                "Choisis ton envoi selon le temps que tu as devant toi.",
  'un timbre':               "Un timbre coûte moins cher quand on achète un carnet.",
  'affranchir':              "Une lettre sans timbre n'est pas affranchie.",

  // Je découvre — demander poliment
  'je voudrais envoyer ce colis':            "Bonjour. Je voudrais envoyer ce colis, s'il vous plaît.",
  "j'aimerais des timbres":                  "J'aimerais des timbres, s'il vous plaît.",
  'est-ce que je pourrais payer par carte':  "Est-ce que je pourrais payer par carte ?",
  'est-ce que vous pouvez répéter':          "Est-ce que vous pouvez répéter, s'il vous plaît ?",
  "s'il vous plaît":                         "Donnez-moi un carnet, s'il vous plaît.",
  'merci beaucoup':                          "Merci beaucoup, bonne journée.",

  // Défi 1 — les cinq questions
  'combien est-ce que ça coûte':             "Combien est-ce que ça coûte, pour Calgary ?",
  'combien de temps est-ce que ça prend':    "Combien de temps est-ce que ça prend ?",
  'est-ce que je peux payer par carte':      "Est-ce que je peux payer par carte de débit ?",
  'où est-ce que je mets mon adresse':       "Où est-ce que je mets mon adresse ?",
  "qu'est-ce que je dois écrire":            "Qu'est-ce que je dois écrire sur la boîte ?",

  // Défi 2 — dire ce qu'il y a dedans
  'il y a des vêtements et un livre':        "Il y a des vêtements et un livre.",
  'la boîte contient des vêtements':         "La boîte contient des vêtements.",
  "c'est un cadeau pour mon frère":          "C'est un cadeau pour mon frère.",
  "ce sont des vêtements d'hiver":           "Ce sont des vêtements d'hiver.",
  'rien de fragile':                         "Il n'y a rien de fragile là-dedans.",
  'rien de liquide':                         "Rien de liquide, rien de dangereux.",

  // Défi 2 — annoncer son choix
  'je vais le prendre':                      "Le standard ? Je vais le prendre.",
  'je vais la prendre':                      "Cette enveloppe-là ? Je vais la prendre.",
  'je vais les prendre':                     "Les deux carnets ? Je vais les prendre.",
  'je vais en prendre trois':                "Je vais en prendre trois, s'il vous plaît.",
  'je vais en prendre deux':                 "Je vais en prendre deux, s'il vous plaît.",

  // Défi 2 — demander au comptoir
  'donnez-moi un carnet de timbres':         "Donnez-moi un carnet de timbres, s'il vous plaît.",
  'montrez-moi les enveloppes':              "Montrez-moi les enveloppes, s'il vous plaît.",
  'répétez le prix':                         "Répétez le prix, s'il vous plaît.",
  "donnez-moi trois timbres, s'il vous plaît": "Donnez-moi trois timbres, s'il vous plaît.",
  'est-ce que vous pourriez me donner un carnet': "Est-ce que vous pourriez me donner un carnet ?",
  'donnez-moi une enveloppe':                "Donnez-moi une enveloppe, s'il vous plaît.",

  // Défi 3 — montrer ce qu'on a devant soi
  'ce carton':               "J'ai trouvé ce carton dans ma boîte aux lettres.",
  'ce colis':                "Je voudrais envoyer ce colis, s'il vous plaît.",
  'cet avis':                "Cet avis dit que mon colis est arrivé.",
  'cet envoi':               "Cet envoi part aujourd'hui.",
  'cette boîte':             "Cette boîte est trop grosse pour la boîte rouge.",
  'cette enveloppe':         "Combien coûte cette enveloppe ?",
  'ces timbres':             "Est-ce que ces timbres sont encore bons ?",
  'ces enveloppes':          "Je vais prendre ces enveloppes.",
  'ce carton-là':            "J'ai trouvé ce carton-là dans ma boîte aux lettres.",
  'cette boîte-là':          "Je voudrais envoyer cette boîte-là.",
};
