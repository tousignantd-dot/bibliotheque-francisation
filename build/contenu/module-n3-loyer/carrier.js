const CARRIER_PHRASES = {
  // Les clés sont les mots et les expressions **exactement tels qu'ils sont
  // écrits** dans les listes `savoir[…][2]` de exos.js — accents et
  // apostrophes compris. Le gabarit fait `CARRIER_PHRASES[w]` sur le mot
  // affiché : une clé écrite en slug ne serait jamais trouvée, et la pastille
  // lirait le mot seul, mal prononcé.
  //
  // Les clés de ce fichier ont été relevées sur exos.js, pas recopiées de
  // mémoire : `node build/releve_sons.js module-n3-loyer` les compare dans les
  // deux sens, et une clé manquante se voit à ce que la valeur du relevé est
  // le mot nu.

  // Les cinq mots du logement
  'un logement':             "Dilnoza cherche un logement plus grand.",
  'un loyer':                "Le loyer est de mille cent cinquante dollars.",
  'un quatre et demie':      "Un quatre et demie a deux chambres fermées.",
  'une chambre à coucher':   "Mon garçon veut sa chambre à coucher à lui.",
  'un balcon':               "La cuisine donne sur un balcon arrière.",

  // Le genre des pièces
  'un salon':                "Le logement a un salon et deux chambres.",
  'une cuisine':             "Il y a une cuisine avec un grand comptoir.",
  'une chambre':             "La deuxième pièce est une chambre fermée.",
  'une salle de bain':       "Au fond du couloir, il y a une salle de bain.",
  'un sous-sol':             "La buanderie est dans un sous-sol propre.",
  'des chambres':            "Ce logement a des chambres bien fermées.",

  // L'annonce, ligne par ligne
  'quatre et demie':         "C'est un quatre et demie, rue Chabot.",
  'deuxième étage':          "Le logement est au deuxième étage.",
  'chauffé et éclairé':      "Le logement est chauffé et éclairé.",
  'non meublé':              "L'annonce dit : non meublé.",
  'libre le premier juillet':"Le logement est libre le premier juillet.",
  'onze cent cinquante dollars': "Le loyer est de onze cent cinquante dollars.",

  // L'adjectif qui suit le nom
  'un logement chauffé':     "C'est un logement chauffé et éclairé.",
  'un balcon arrière':       "Il y a un balcon arrière, derrière la cuisine.",
  'une cuisine chauffée':    "C'est une cuisine chauffée, même en janvier.",
  'des logements chauffés':  "Ce sont des logements chauffés et éclairés.",
  'compris':                 "Le chauffage est compris dans le loyer.",
  'comprise':                "L'électricité est comprise dans le loyer.",
  'meublé':                  "Le deux et demie de la rue Saint-Hubert est meublé.",

  // Demander poliment, au téléphone
  'je voudrais':             "Je voudrais visiter le logement, s'il vous plaît.",
  "j'aimerais":              "J'aimerais poser trois questions.",
  'est-ce que je pourrais':  "Est-ce que je pourrais le visiter samedi ?",
  'est-ce que je peux':      "Est-ce que je peux vous rappeler demain ?",
  "s'il vous plaît":         "Pouvez-vous répéter, s'il vous plaît ?",

  // Les trois questions
  'est-ce que le chauffage est compris': "Est-ce que le chauffage est compris ?",
  'combien il y a de chambres': "Combien il y a de chambres fermées ?",
  "à quelle date c'est libre": "À quelle date est-ce que c'est libre ?",
  'est-ce que je pourrais visiter': "Est-ce que je pourrais visiter cette semaine ?",
  'pouvez-vous répéter':     "Pardon, pouvez-vous répéter, s'il vous plaît ?",

  // Le futur proche
  'je vais venir':           "Je vais venir samedi matin avec mon mari.",
  'je vais appeler':         "Je vais appeler la propriétaire aujourd'hui.",
  'nous allons visiter':     "Nous allons visiter le logement à dix heures.",
  'il va être libre':        "Le logement va être libre le premier juillet.",
  'je vais vous rappeler':   "Je vais vous rappeler demain matin.",
  'je vais visiter le logement': "Je vais visiter le logement samedi.",

  // Dire où
  'au fond du couloir':      "Les deux chambres sont au fond du couloir.",
  'à côté de la salle de bain': "La petite chambre est à côté de la salle de bain.",
  'au sous-sol':             "La buanderie est au sous-sol.",
  'au deuxième étage':       "Le logement est au deuxième étage.",
  'derrière la cuisine':     "Le balcon est derrière la cuisine.",
  "en bas de l'escalier":    "Les laveuses sont en bas de l'escalier.",

  // Répondre non
  "il n'y a pas de stationnement": "Il n'y a pas de stationnement dans la cour.",
  "il n'y a pas d'ascenseur":"Il n'y a pas d'ascenseur dans l'immeuble.",
  "il n'y a pas de meubles": "Le logement est vide : il n'y a pas de meubles.",
  "ce n'est pas compris":    "Internet, ce n'est pas compris dans le loyer.",
  "je n'ai pas d'auto":      "Ça ne fait rien, je n'ai pas d'auto.",

  // Avant de dire oui
  'le bail':                 "Le bail commence le premier juillet.",
  'douze mois':              "Le bail dure douze mois.",
  'un dépôt':                "Au Québec, un dépôt de garantie est interdit.",
  'le premier loyer':        "On paie le premier loyer le premier jour du bail.",
  'des enfants':             "On ne peut pas refuser un logement à des enfants.",
  'je vais y penser':        "Je vais y penser et je vous rappelle demain.",
};
