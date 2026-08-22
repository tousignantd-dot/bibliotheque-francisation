const CARRIER_PHRASES = {
  // Les clés sont les mots et les expressions **exactement tels qu'ils sont
  // écrits** dans les listes `savoir[…][2]` de exos.js — accents, apostrophes
  // et ponctuation compris. Le gabarit fait `CARRIER_PHRASES[w]` sur le mot
  // affiché : une clé écrite en slug ne serait jamais trouvée, et la pastille
  // lirait le mot seul, mal prononcé.
  //
  // Les cinquante et une clés ont été relevées sur `exos.js` par un script,
  // pas écrites de mémoire. Celles qui sont déjà des phrases entières
  // reçoivent quand même une porteuse : elle leur donne l'intonation de
  // quelqu'un qui pousse la porte d'un commerce plutôt qu'une lecture plate.

  // Je découvre — les mots de l'affiche
  'une affiche':          "Une affiche « On embauche » est collée dans la vitrine.",
  'on embauche':          "C'est écrit en rouge : on embauche.",
  'embaucher':            "La boulangerie veut embaucher quelqu'un pour le matin.",
  'engager':              "Ils vont engager une personne cette semaine.",
  'offrir ses services':  "Elle entre à la boulangerie pour offrir ses services.",
  "l'expérience":         "L'expérience, c'est tout le travail qu'on a déjà fait.",
  'sans rendez-vous':     "On peut se présenter sans rendez-vous, le matin.",

  // Je découvre — les quatre choses qu'on dit en entrant
  "bonjour, j'ai vu votre affiche":  "Bonjour, j'ai vu votre affiche dans la vitrine.",
  'est-ce que vous engagez encore':  "Est-ce que vous engagez encore, monsieur ?",
  'je sais faire le ménage':         "Je sais faire le ménage et la vaisselle.",
  "j'ai de l'expérience en garde d'enfants": "J'ai de l'expérience en garde d'enfants.",
  'je suis libre le matin':          "Je suis libre le matin, du lundi au vendredi.",
  'vous pouvez me joindre au':       "Vous pouvez me joindre au 438 555-0192.",

  // Défi 1 — demander si ça engage
  'est-ce que vous engagez':               "Est-ce que vous engagez ?",
  "est-ce que vous cherchez quelqu'un":    "Est-ce que vous cherchez quelqu'un pour le matin ?",
  'est-ce que le poste est encore libre':  "Est-ce que le poste est encore libre ?",
  'à qui est-ce que je peux parler':       "À qui est-ce que je peux parler, s'il vous plaît ?",
  'on engage':                             "On engage encore, oui : entrez.",

  // Défi 1 — dire ce qu'on sait faire
  'je sais servir les clients':            "Je sais servir les clients au comptoir.",
  'pendant six ans':                       "J'ai gardé des enfants pendant six ans.",
  "je n'ai jamais travaillé au Québec":    "Je n'ai jamais travaillé au Québec, mais j'apprends vite.",
  'je peux apprendre vite':                "Je peux apprendre vite, monsieur.",

  // Défi 1 — les disponibilités
  'du lundi au vendredi':                  "Je travaille du lundi au vendredi.",
  'de neuf heures à une heure':            "Je suis libre de neuf heures à une heure.",
  'le matin':                              "Le matin, je suis toujours disponible.",
  'la fin de semaine':                     "La fin de semaine, je garde mes enfants.",
  'sauf le mercredi':                      "Du mardi au samedi, sauf le mercredi.",
  'je suis libre du lundi au vendredi, le matin': "Je suis libre du lundi au vendredi, le matin.",

  // Défi 2 — l'argent et le temps de l'annonce
  "seize dollars cinquante de l'heure":    "Le salaire est de seize dollars cinquante de l'heure.",
  'vingt heures par semaine':              "C'est un poste de vingt heures par semaine.",
  'payé aux deux semaines':                "Le salaire est payé aux deux semaines.",
  'de neuf heures à treize heures':        "L'horaire va de neuf heures à treize heures.",
  'six jours sur sept':                    "La boulangerie est ouverte six jours sur sept.",

  // Défi 2 — ce que l'annonce exige
  'il faut parler français':               "Il faut parler français pour ce poste.",
  'expérience exigée':                     "Deux ans d'expérience exigée, c'est écrit en bas.",
  'aucune expérience exigée':              "Aucune expérience exigée : je peux me présenter.",
  'un atout':                              "Parler anglais est un atout, mais ce n'est pas exigé.",
  'formation donnée sur place':            "Formation donnée sur place, dit l'annonce.",
  'se présenter en personne':              "Il faut se présenter en personne, entre neuf et onze heures.",

  // Défi 3 — les verbes du formulaire
  'écrivez en lettres moulées':            "Écrivez en lettres moulées, s'il vous plaît.",
  'cochez la bonne case':                  "Cochez la bonne case : oui ou non.",
  'signez ici':                            "Signez ici, au bas de la page.",
  'datez le formulaire':                   "Datez le formulaire avant de me le remettre.",
  'remplissez le formulaire':              "Remplissez le formulaire au complet.",
  'joignez une copie':                     "Joignez une copie de votre carte.",

  // Défi 3 — les lignes de la petite annonce
  "ménage et garde d'enfants":             "En haut de l'annonce : ménage et garde d'enfants.",
  "je m'appelle Fanta et j'habite dans Saint-Michel": "Je m'appelle Fanta et j'habite dans Saint-Michel.",
  "j'ai six ans d'expérience":             "J'ai six ans d'expérience en garde d'enfants.",
  'du lundi au vendredi, de huit heures à treize heures': "Du lundi au vendredi, de huit heures à treize heures.",
  "je demande vingt dollars de l'heure":   "Je demande vingt dollars de l'heure.",
  'appelez-moi au':                        "Appelez-moi au 438 555-0192.",
};
