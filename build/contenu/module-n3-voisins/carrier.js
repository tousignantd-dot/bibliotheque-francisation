const CARRIER_PHRASES = {
  // Les clés sont les mots et les expressions **exactement tels qu'ils sont
  // écrits** dans les listes `savoir[…][2]` de exos.js — accents, apostrophes
  // et ponctuation compris. Le gabarit fait `CARRIER_PHRASES[w]` sur le mot
  // affiché : une clé écrite en slug ne serait jamais trouvée, et la pastille
  // lirait le mot seul, mal prononcé.
  //
  // Les cinquante-sept clés ont été relevées sur `exos.js` par un script, pas
  // écrites de mémoire. Celles qui sont déjà des phrases entières reçoivent
  // quand même une porteuse : elle leur donne l'intonation d'un échange de
  // palier plutôt qu'une lecture plate.

  // Je découvre — les mots de l'immeuble
  'un voisin':          "Mon voisin du deuxième part travailler à six heures.",
  'un immeuble':        "Notre immeuble a six logements et un escalier en avant.",
  'le palier':          "On s'est parlé cinq minutes sur le palier du deuxième.",
  'le concierge':       "Le concierge passe le balai dans l'entrée le vendredi.",
  'faire connaissance': "On a fait connaissance devant les boîtes aux lettres.",

  // Je découvre — se présenter, présenter quelqu'un
  "je m'appelle Rachid Belkacem": "Bonjour, je m'appelle Rachid Belkacem.",
  "j'habite au troisième":        "J'habite au troisième, au 3A.",
  'je vous présente ma sœur':     "Madame Lachapelle, je vous présente ma sœur.",
  'voici ma sœur':                "Voici ma sœur. Elle vient donner un coup de main.",
  "c'est ma sœur":                "C'est ma sœur. Elle habite à Longueuil.",
  'enchanté':                     "Bonjour, enchanté !",
  'enchantée':                    "Bonjour, enchantée !",

  // Défi 1 — demander et donner la permission
  'est-ce que je peux mettre mon vélo dans la remise':
      "Est-ce que je peux mettre mon vélo dans la remise ?",
  "est-ce que je pourrais l'accrocher au mur":
      "Est-ce que je pourrais l'accrocher au mur du fond ?",
  'est-ce que vous permettez':  "Est-ce que vous permettez que je passe par la cour ?",
  'la permission':              "J'ai demandé la permission avant de toucher à la remise.",
  'demander la permission':     "Il vaut mieux demander la permission avant.",
  "ce n'est pas permis":        "Ce n'est pas permis de bloquer la sortie de secours.",

  // Défi 1 — les pronoms qui remplacent
  'je le mets dans la remise':  "Mon vélo ? Je le mets dans la remise.",
  'je la laisse passer':        "La tondeuse ? Je la laisse passer.",
  'je les remets ce soir':      "Les clés ? Je les remets ce soir.",
  'je lui parle':               "Monsieur Nadeau est en bas : je lui parle tout de suite.",
  'je lui demande la clé':      "Je lui demande la clé de la remise.",
  'accrochez-le au mur':        "Accrochez-le au mur du fond, s'il vous plaît.",

  // Défi 2 — l'invitation et ses trois renseignements
  "c'est samedi":                        "C'est samedi, chez nous.",
  'à deux heures':                       "Samedi, à deux heures.",
  'chez nous, au 3A':                    "Ça se passe chez nous, au 3A.",
  'qui vient ?':                         "Qui vient, finalement ?",
  'apportez seulement votre bonne humeur': "Apportez seulement votre bonne humeur.",

  // Défi 2 — le futur proche et le futur simple
  'je vais apporter mes biscuits': "Je vais apporter mes biscuits, j'insiste.",
  'elle va faire des gâteaux':     "Ma sœur, elle va faire des gâteaux.",
  'on va se voir samedi':          "Alors, on va se voir samedi !",
  'la fête aura lieu samedi':      "La fête aura lieu samedi, à deux heures.",
  'il y aura du café':             "Il y aura du café et des gâteaux.",
  'ce sera chez nous':             "Ce sera chez nous, au 3A.",
  'confirmez SVP':                 "Confirmez SVP avant vendredi.",

  // Défi 2 — les compliments
  "que c'est bon !":       "Que c'est bon, ces biscuits-là !",
  "comme c'est bon !":     "Comme c'est bon !",
  'vous cuisinez bien !':  "Vous cuisinez bien, madame !",
  'ça vous va bien !':     "Votre manteau neuf ? Ça vous va bien !",
  'ça te va bien !':       "Ta tuque rouge ? Ça te va bien !",
  'quelle belle porte !':  "Quelle belle porte ! C'est vous qui l'avez peinte ?",
  'quel beau salon !':     "Quel beau salon vous avez !",
  "merci, c'est gentil":   "Merci, c'est gentil.",

  // Défi 3 — l'adjectif qui décrit
  'un chat roux':                  "Caramel, c'est un chat roux.",
  'une porte bleue':               "Ils ont une porte bleue, au premier.",
  'des cheveux gris et courts':    "Elle a des cheveux gris et courts.",
  'des lunettes rouges':           "Elle porte des lunettes rouges.",
  'un ourson usé':                 "Il y a un ourson usé accroché aux clés.",
  'un petit ourson':               "Un petit ourson en tissu pend au trousseau.",
  'une grande dame':               "C'est une grande dame, du premier étage.",
  'roux, assez gros, avec une tache blanche':
      "Il est roux, assez gros, avec une tache blanche sous le menton.",

  // Défi 3 — les adverbes d'intensité
  'il est très peureux':                 "Il est très peureux avec les gens qu'il ne connaît pas.",
  'il est assez gros':                   "Il est assez gros, mon chat.",
  "l'ourson est un peu usé":             "L'ourson est un peu usé, il a servi longtemps.",
  'il prend trop de place':              "Mon vélo, il prend trop de place dans le corridor.",
  'très peureux, assez gros, un peu usé': "Très peureux, assez gros, un peu usé.",
};
