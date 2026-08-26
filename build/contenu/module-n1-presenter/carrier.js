const CARRIER_PHRASES = {
  // Les clés sont les mots tels qu'ils paraissent dans les listes `speak` des
  // blocs `savoir` de `exos.js`, article retiré, accents et espaces compris.
  // Une clé écrite en slug n'est jamais trouvée : la pastille lit alors le mot
  // seul — ce que la phrase porteuse existe précisément pour éviter. Trois
  // clés d'ici (`prenom`, `epeler`, `de_rien`) ont eu ce défaut.
  'nom':      "Quel est votre nom de famille ?",
  'prénom':   "Mon prénom, c'est Amina.",
  'épeler':   "Pouvez-vous épeler votre nom ?",
  'adresse':  "Mon adresse, c'est 4520, rue Bélanger.",
  'pays':     "Je viens d'un pays chaud.",
  'langue':   "Je parle deux langues.",
  'habiter':  "J'habite à Montréal.",
  'enfant':   "J'ai un enfant.",
  'metier':   "Mon métier, c'est mécanicien.",
  'bonjour':  "Bonjour, madame !",
  'merci':    "Merci beaucoup.",
  'pardon':   "Pardon ? Je ne comprends pas.",
  'bonsoir':  "Bonsoir ! À demain.",
  'de rien':  "De rien. Ça me fait plaisir.",
  'lentement':"Plus lentement, s'il vous plaît.",
};
