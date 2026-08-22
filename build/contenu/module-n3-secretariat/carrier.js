const CARRIER_PHRASES = {
  // Les clés sont les mots **exactement tels qu'ils sont écrits** dans les
  // listes `savoir[…][2]` de exos.js — accents compris. Le gabarit fait
  // `CARRIER_PHRASES[w]` sur le mot affiché : une clé écrite en slug ne
  // serait jamais trouvée, et la pastille lirait le mot seul, mal prononcé.
  //
  // Ici, la phrase porteuse fait un second travail : la plupart de ces mots
  // sont des formules de comptoir, et une formule s'apprend dans le tour de
  // parole où elle se dit, jamais toute seule.

  // Le lieu et les gens
  'le secrétariat':        "Le secrétariat est en bas, à côté de la porte d'entrée.",
  'le comptoir':           "J'attends mon tour devant le comptoir.",
  'la secrétaire':         "La secrétaire écrit l'absence dans le dossier.",
  'mon groupe':            "Mon groupe, c'est le groupe douze, l'avant-midi.",
  'mon dossier':           "L'absence est écrite dans mon dossier.",

  // Saluer et s'adresser
  'bonjour madame':        "Bonjour, madame. Je viens pour une absence.",
  'bonjour monsieur':      "Bonjour, monsieur. Est-ce que je peux vous parler ?",
  'est-ce que vous pouvez':"Est-ce que vous pouvez répéter, s'il vous plaît ?",
  'votre nom':             "Votre nom, s'il vous plaît ?",
  'votre groupe':          "Quel est votre groupe, madame ?",
  "s'il vous plaît":       "Un instant, s'il vous plaît.",
  'merci beaucoup':        "Merci beaucoup, madame. Bonne journée.",
  'bonne journée':         "Bonne journée, et à demain.",

  // Le futur proche de l'annonce
  'je vais être absente':      "Je vais être absente jeudi matin.",
  'je vais arriver en retard': "Je vais arriver en retard demain.",
  'je ne vais pas être là':    "Je ne vais pas être là lundi.",
  "j'ai été absente":          "J'ai été absente la semaine passée.",

  // Les jours de la semaine
  'jeudi je vais être absente':"Jeudi, je vais être absente.",
  'le jeudi je travaille':     "Le jeudi, je travaille : c'est toutes les semaines.",
  'lundi mardi mercredi':      "Lundi, mardi, mercredi, jeudi, vendredi.",
  'jeudi prochain':            "Je serai absente jeudi prochain.",
  'jeudi le 12 mars':          "Jeudi, le douze mars, l'avant-midi.",

  // Situer une absence passée
  'hier':                    "J'ai manqué le cours hier.",
  'avant-hier':              "Je suis revenue avant-hier.",
  'la semaine passée':       "J'ai été absente la semaine passée.",
  'du lundi au mercredi':    "Le billet dit : du lundi au mercredi.",
  'pendant trois jours':     "Je n'ai pas pu venir pendant trois jours.",
  'depuis lundi':            "Je suis malade depuis lundi.",
  'lundi mardi et mercredi': "J'ai manqué lundi, mardi et mercredi.",

  // À qui est le papier
  'mon billet':      "Voici mon billet de la clinique.",
  'ma fille':        "Ma fille a un rendez-vous à la clinique.",
  'mes papiers':     "J'ai perdu mes papiers dans l'autobus.",
  'votre dossier':   "J'inscris l'absence dans votre dossier.",
  'vos journées':    "Vos journées d'absence sont justifiées.",
  'mon absence':     "Je viens annoncer mon absence.",
  'mon attestation': "Je viens chercher mon attestation.",

  // Mettre les démarches dans l'ordre
  'avant de partir':            "Avant de partir, demandez votre attestation.",
  'avant de signer':            "Avant de signer, lisez le formulaire au complet.",
  'avant le cours':             "Je passe au comptoir avant le cours.",
  'avant 9 heures':             "Il faut téléphoner avant neuf heures.",
  'après le cours':             "Après le cours, je vais voir mon enseignante.",
  'je demande mon attestation': "Je demande mon attestation aujourd'hui.",

  // Demander poliment
  "j'aimerais une attestation":      "J'aimerais une attestation de fréquentation, s'il vous plaît.",
  'est-ce que je peux':              "Est-ce que je peux garder l'original ?",
  'pourriez-vous':                   "Pourriez-vous faire une photocopie, s'il vous plaît ?",
  "qu'est-ce que je dois apporter":  "Qu'est-ce que je dois apporter ?",
  'quand est-ce que':                "Quand est-ce que l'attestation sera prête ?",
  'plus lentement':                  "Pouvez-vous répéter plus lentement, s'il vous plaît ?",
};
