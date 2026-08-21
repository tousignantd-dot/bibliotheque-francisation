const CARRIER_PHRASES = {
  // Les clés sont les mots et les expressions **exactement tels qu'ils sont
  // écrits** dans les listes `savoir[…][2]` de exos.js — accents et
  // apostrophes compris. Le gabarit fait `CARRIER_PHRASES[w]` sur le mot
  // affiché : une clé écrite en slug ne serait jamais trouvée, et la pastille
  // lirait le mot seul, mal prononcé.

  // Les lieux et les objets de la pharmacie
  'le comptoir des ordonnances': "Le comptoir des ordonnances est au fond, à droite.",
  'une ordonnance':          "Il me faut une ordonnance pour ce médicament.",
  "la carte d'assurance maladie": "Voici ma carte d'assurance maladie.",
  'un médicament en vente libre': "Le sirop est un médicament en vente libre.",
  'le pharmacien':           "Le pharmacien répond à tes questions gratuitement.",

  // Dire où on a mal
  "j'ai mal":                "J'ai mal depuis ce matin.",
  "j'ai mal au dos":         "J'ai mal au dos quand je travaille.",
  "j'ai mal au ventre":      "J'ai mal au ventre après les repas.",
  "j'ai mal à la tête":      "J'ai mal à la tête depuis ce matin.",
  "j'ai mal à la gorge":     "J'ai mal à la gorge le matin.",
  "j'ai mal à l'oreille":    "J'ai mal à l'oreille gauche.",
  "j'ai mal à l'estomac":    "J'ai mal à l'estomac le soir.",
  "j'ai mal aux dents":      "J'ai mal aux dents depuis deux jours.",
  "j'ai mal aux yeux":       "J'ai mal aux yeux devant l'écran.",

  // Nommer son malaise
  'je tousse':               "Je tousse beaucoup la nuit.",
  "j'ai de la fièvre":       "J'ai de la fièvre depuis hier soir.",
  'je me suis coupé':        "Je me suis coupé le doigt avec un couteau.",
  'je me suis fait mal':     "Je suis tombée et je me suis fait mal au genou.",
  'ça persiste':             "La toux persiste depuis une semaine.",
  'ça continue':             "Ça continue, même avec le sirop.",
  'consulter un médecin':    "Il faut consulter un médecin cette semaine.",
  "s'étouffer":              "Le petit a failli s'étouffer avec un comprimé.",
  'rincer':                  "Il faut rincer sa bouche après chaque dose.",

  // Depuis quand ça dure
  'depuis quatre jours':     "Je tousse depuis quatre jours.",
  'ça fait quatre jours que je tousse': "Ça fait quatre jours que je tousse.",
  'il y a deux jours':       "Je me suis coupé il y a deux jours.",
  'pendant sept jours':      "Prenez ce médicament pendant sept jours.",
  'dans six semaines':       "Mon rendez-vous est dans six semaines.",

  // Demander et comprendre l'obligation
  'est-ce que je peux':      "Est-ce que je peux faire renouveler mon ordonnance ?",
  'faire renouveler mon ordonnance': "Je voudrais faire renouveler mon ordonnance.",
  'est-ce que vous pouvez':  "Est-ce que vous pouvez regarder mon dossier ?",
  'je dois':                 "Je dois prendre un comprimé le matin.",
  'vous devez':              "Vous devez finir les sept jours.",
  'il faut':                 "Il faut apporter sa carte chaque fois.",

  // À qui c'est
  'mon dossier':             "Le pharmacien regarde mon dossier.",
  'mon médicament':          "Mon médicament est prêt depuis midi.",
  'ma carte':                "Voici ma carte, s'il vous plaît.",
  'mon ordonnance':          "Mon ordonnance est finie depuis samedi.",
  'mes comprimés':           "Je prends mes comprimés le matin.",
  'votre carte':             "Votre carte d'assurance maladie, s'il vous plaît ?",
  'vos médicaments':         "Vos médicaments seront prêts dans vingt minutes.",

  // Quand et combien de fois
  'trois fois par jour':     "Un comprimé, trois fois par jour.",
  'une fois par jour':       "Une fois par jour, le soir.",
  'deux fois par semaine':   "Ce comprimé se prend deux fois par semaine.",
  'aux huit heures':         "Prenez ce médicament aux huit heures.",
  'avant les repas':         "Ce sirop se prend avant les repas.",
  'après les repas':         "Ce comprimé se prend après les repas.",
  'avec de la nourriture':   "Prenez-le avec de la nourriture.",
  'le matin':                "Un comprimé le matin, un le soir.",
  'au coucher':              "Une fois par jour, au coucher.",

  // Les phrases de l'étiquette
  'prenez un comprimé':      "Prenez un comprimé trois fois par jour.",
  "agitez avant d'ouvrir":   "Agitez la bouteille avant d'ouvrir.",
  'ne prenez pas deux comprimés': "Ne prenez pas deux comprimés en même temps.",
  'ne pas donner aux enfants': "Ne pas donner aux enfants de moins de six ans.",
  'rincez votre bouche':     "Rincez votre bouche après chaque dose.",
  'terminez le traitement':  "Terminez le traitement, même si ça va mieux.",

  // Les mises en garde chiffrées
  'pas plus de quatre comprimés': "Pas plus de quatre comprimés par jour.",
  'de moins de six ans':     "Ne pas donner aux enfants de moins de six ans.",
  'de plus de dix-huit ans': "Ce sirop est pour les adultes de plus de dix-huit ans.",
  'au moins quatre heures':  "Attendez au moins quatre heures entre deux doses.",
};
