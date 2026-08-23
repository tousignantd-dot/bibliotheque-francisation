const CARRIER_PHRASES = {
  // Les clés sont les mots **accentués**, tels qu'ils paraissent dans la
  // troisième colonne des bandeaux `savoir` de `exos.js`. Une clé écrite en
  // slug n'est jamais trouvée par le gabarit, qui fait `CARRIER_PHRASES[w]`
  // sur le mot affiché — et la pastille lit alors le mot seul, mal prononcé.
  // Le relevé des deux sens (mots sans phrase, clés inutiles) se fait par
  // `node build/coherence.js module-n8-recherche`.
  //
  // Seize mots, seize phrases : ce sont exactement les seize cartes de
  // `fccards.js`, chacune reprise dans un bandeau de savoir.
  'un processus de sélection': "Le processus de sélection compte trois étapes.",
  'la présélection': "La présélection se fait par téléphone.",
  'un accusé de réception': "Elle a reçu un accusé de réception le soir même.",
  'un contremaître': "Le contremaître du soir arrive à quinze heures.",
  'un quart de soir': "Le quart de soir se termine à vingt-trois heures trente.",
  'une chaîne de production': "La chaîne de production s'est arrêtée deux fois.",
  'une mise en situation': "L'examen est une mise en situation de quatre-vingt-dix minutes.",
  'une entrevue de groupe': "L'entrevue de groupe réunit quatre candidats.",
  'le taux de roulement': "Le taux de roulement de l'usine est de onze pour cent.",
  'un carnet de commandes': "Leur carnet de commandes a doublé en dix-huit mois.",
  'une acquisition': "L'acquisition de l'usine remonte au mois de janvier.",
  "un temps d'arrêt": "Chaque temps d'arrêt coûte cher à la production.",
  'un échelon': "Elle demande un échelon de plus à l'embauche.",
  'une contrepartie': "Elle offre une contrepartie plutôt qu'une simple demande.",
  'le service continu': "Le service continu se compte chez un même employeur.",
  'un motif de discrimination': "L'âge est un motif de discrimination nommé par la Charte.",
};
