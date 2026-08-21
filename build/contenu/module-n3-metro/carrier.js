const CARRIER_PHRASES = {
  // Les clés sont les mots et les expressions **exactement tels qu'ils sont
  // écrits** dans les listes `savoir[…][2]` de exos.js — accents et
  // apostrophes compris. Le gabarit fait `CARRIER_PHRASES[w]` sur le mot
  // affiché : une clé écrite en slug ne serait jamais trouvée, et la pastille
  // lirait le mot seul, mal prononcé.
  //
  // Les soixante clés de ce fichier ont été relevées sur exos.js, pas
  // recopiées à la main : `module-n3-epicerie` traîne encore douze clés en
  // slug pour l'avoir fait autrement.

  // La carte, le titre, le comptoir
  'une carte OPUS':          "Sur une carte OPUS, tu mets ton titre du mois.",
  'un titre de transport':   "Sans titre de transport, on ne peut pas monter.",
  'un passage':              "Un passage coûte trois dollars soixante-quinze.",
  'dix passages':            "J'achète dix passages chaque lundi matin.",
  'le point de service':     "Le point de service est à droite, dans la station.",
  'se renseigner':           "Je viens me renseigner sur les titres de transport.",
  'un titre mensuel':        "Un titre mensuel coûte cent dix dollars.",
  'un titre hebdomadaire':   "Un titre hebdomadaire va du lundi au dimanche.",
  'une soirée illimitée':    "Une soirée illimitée coûte six dollars soixante-quinze.",

  // Dire et demander un prix
  'trois dollars soixante-quinze': "Ça coûte trois dollars soixante-quinze.",
  'trois soixante-quinze':   "C'est trois soixante-quinze, madame.",
  'soixante-dix':            "Ça fait soixante-dix dollars en tout.",
  'quatre-vingt-dix':        "Il reste quatre-vingt-dix minutes sur ma correspondance.",
  'trois virgule soixante-quinze': "On écrit trois virgule soixante-quinze.",
  'ça coûte combien':        "Ça coûte combien, le titre mensuel ?",
  "c'est combien":           "C'est combien, un passage ?",
  'combien coûte le mensuel':"Combien coûte le mensuel, s'il vous plaît ?",
  'combien est-ce que je vous dois': "Combien est-ce que je vous dois ?",

  // Montrer : ce, cet, cette, ces
  'ce titre':                "Ce titre est bon jusqu'à la fin du mois.",
  'ce passage':              "Ce passage vient d'être validé.",
  'cet autobus':             "Cet autobus va vers le nord.",
  'cet appareil':            "Cet appareil lit ta carte en une seconde.",
  'cette carte':             "Cette carte est encore bonne.",
  'cette zone':              "Cette zone, c'est la zone A.",
  'ces titres':              "Ces titres coûtent le même prix.",
  'ces prix':                "Ces prix sont affichés au mur.",
  'ce titre-là':             "Combien coûte ce titre-là ?",
  'cette carte-là':          "Est-ce que cette carte-là est encore bonne ?",

  // Poser sa question au comptoir
  'est-ce que je peux payer par carte': "Est-ce que je peux payer par carte ?",
  'est-ce que je peux payer comptant':  "Est-ce que je peux payer comptant ?",
  "où est-ce qu'on fait la photo":      "Où est-ce qu'on fait la photo ?",
  "jusqu'à quand c'est bon":            "Jusqu'à quand c'est bon, ce titre-là ?",
  'pouvez-vous répéter':     "Pardon, pouvez-vous répéter, s'il vous plaît ?",
  "plus lentement s'il vous plaît":     "Plus lentement, s'il vous plaît.",

  // Les quatre verbes de la demande
  'je voudrais un titre mensuel': "Je voudrais un titre mensuel, s'il vous plaît.",
  'je voudrais acheter':     "Je voudrais acheter un titre pour le mois.",
  "je dois apporter une preuve d'âge": "Je dois apporter une preuve d'âge.",
  'il faut une carte avec photo': "Pour le tarif réduit, il faut une carte avec photo.",
  'il faut venir':           "Il faut venir avec elle au comptoir.",

  // Quand un titre est bon
  'valide de dix-huit heures à cinq heures': "C'est valide de dix-huit heures à cinq heures.",
  'du lundi au dimanche':    "L'hebdo est bon du lundi au dimanche.",
  "bon jusqu'à la fin du mois": "Ton titre est bon jusqu'à la fin du mois.",
  'à partir de seize heures':"Le titre commence à partir de seize heures.",
  'pendant cent vingt minutes': "La correspondance dure pendant cent vingt minutes.",

  // Comparer
  'moins cher que':          "L'hebdo est moins cher que le dix passages.",
  'plus cher que':           "Le mensuel est plus cher que l'hebdo.",
  'aussi cher que':          "Le dix passages est presque aussi cher que l'hebdo.",
  "moins cher que l'hebdo":  "Le mensuel n'est pas moins cher que l'hebdo.",
  'moins de douze ans':      "Les enfants de moins de douze ans voyagent gratuitement.",
  'plus de cinq enfants':    "On ne peut pas accompagner plus de cinq enfants.",
  'onze ans et moins':       "Onze ans et moins, c'est gratuit.",
  'soixante-cinq ans et plus':"Soixante-cinq ans et plus, c'est le tarif réduit.",

  // La grille, les places, le service adapté
  'une zone tarifaire':      "Montréal est une zone tarifaire à elle seule.",
  'une place réservée':      "Cette rangée est une place réservée.",
  'une personne à mobilité réduite': "Laisse la place à une personne à mobilité réduite.",
  'une femme enceinte':      "Une femme enceinte peut s'asseoir en avant.",
  'laisser sa place':        "Il faut laisser sa place quand quelqu'un monte.",
  'le transport adapté':     "Ma voisine se déplace avec le transport adapté.",
  'se déplacer':             "Je dois me déplacer cinq jours par semaine.",
  'se repérer':              "Avec le plan, on arrive à se repérer.",
};
