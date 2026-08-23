const CARRIER_PHRASES = {
  // Les clés sont les mots **accentués**, tels qu'ils paraissent dans la
  // troisième colonne des bandeaux `savoir` de `exos.js`. Une clé écrite en
  // slug n'est jamais trouvée par le gabarit, qui fait `CARRIER_PHRASES[w]`
  // sur le mot affiché — et la pastille lit alors le mot seul, mal prononcé.
  // Le relevé dans les deux sens (mots sans phrase, clés inutiles) se fait
  // par `node build/coherence.js module-n8-oeuvres`.
  //
  // Dix-sept mots, dix-sept phrases : ce sont exactement les dix-sept cartes
  // de `fccards.js`, chacune reprise dans un bandeau de savoir.
  'une interprétation': "Son interprétation tient sur trois détails.",
  'une lecture': "Sa lecture explique presque toute la scène.",
  "l'implicite": "Tout le texte repose sur l'implicite.",
  'un jugement de valeur': "« C'est raté » est un jugement de valeur.",
  'un fait vérifiable': "Le téléphone qui sonne est un fait vérifiable.",
  'une fin ouverte': "La série se termine sur une fin ouverte.",
  'un plan fixe': "Les bottes occupent un plan fixe très long.",
  'un indice': "La corde attachée est son meilleur indice.",
  'un dénouement': "Le dénouement tient en quatre gestes.",
  'une nouvelle littéraire': "Une nouvelle littéraire fait quelques pages.",
  'un recueil': "Ce texte ouvre un recueil paru l'automne dernier.",
  'une strophe': "La troisième strophe change tout le poème.",
  'une métaphore': "Le pare-brise gelé devient une métaphore.",
  'le narrateur': "Le narrateur ne juge personne.",
  'une critique': "Sa critique mêle des faits et des jugements.",
  'un argument': "Un argument sans détail précis ne convainc pas.",
  'le courrier des lecteurs': "Elle a écrit au courrier des lecteurs.",
};
