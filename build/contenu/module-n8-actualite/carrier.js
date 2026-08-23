const CARRIER_PHRASES = {
  // Les clés sont les mots **accentués**, tels qu'ils paraissent dans la
  // troisième colonne des bandeaux `savoir` de `exos.js`. Une clé écrite en
  // slug n'est jamais trouvée par le gabarit, qui fait `CARRIER_PHRASES[w]`
  // sur le mot affiché — et la pastille lit alors le mot seul, mal prononcé.
  // Le relevé dans les deux sens (mots sans phrase, clés inutiles) se fait
  // par `node build/coherence.js module-n8-actualite`.
  //
  // Seize mots, seize phrases : ce sont exactement les seize cartes de
  // `fccards.js`, chacune reprise dans un bandeau de savoir.
  'un éditorial': "L'éditorial du Courant appuyait le projet.",
  'une chronique': "Sa chronique dure douze minutes chaque mercredi.",
  'le courrier des lecteurs': "Elle a écrit au courrier des lecteurs.",
  'un communiqué': "Les deux journaux ont reçu le même communiqué.",
  'une manchette': "La manchette parlait d'un terrain vague.",
  'une radio communautaire': "La radio communautaire couvre les séances du conseil.",
  'un parti pris': "Il annonce son parti pris dès le début.",
  'une source': "Le reportage cite deux sources différentes.",
  'un boisé': "Le boisé compte onze hectares.",
  'un remblai': "Le remblai occupe l'ancienne cour de voirie.",
  'une thèse': "La thèse de l'éditorial tient en une phrase.",
  'une concession': "Sa concession est franche et bien placée.",
  'une nuance': "Il ajoute une nuance importante.",
  'une assemblée de consultation': "L'assemblée de consultation a lieu jeudi soir.",
  'un registre référendaire': "Le registre référendaire ouvre mardi matin.",
  'une personne habile à voter': "Une personne habile à voter peut signer le registre.",
};
