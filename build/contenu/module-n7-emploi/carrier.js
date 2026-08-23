const CARRIER_PHRASES = {
  // Une phrase porteuse par mot ou par groupe à écouter. Les clés sont les
  // mots **tels qu'ils paraissent** dans les listes `savoir[…][2]` de
  // `exos.js` — une clé écrite autrement n'est jamais trouvée et la pastille
  // lit le mot seul, mal prononcé.
  //
  // Particularité de ce module : le bandeau du premier exercice de prosodie
  // ne fait pas écouter des mots mais des **groupes rythmiques**. Leur phrase
  // porteuse est la phrase entière d'où le groupe est tiré : c'est justement
  // dans la phrase que s'entend la montée de la voix, et un groupe dit seul
  // descendrait toujours.
  "d'abord, on mesure":     "D'abord, on mesure, pendant deux semaines, chaque camion qui se présente.",
  'Il y a quatre étapes':   "Ensuite, les étapes. Il y a quatre étapes, et je vais les nommer dans l'ordre.",
  'Voilà. Des questions ?': "Deux mois et demi, quatre cents dollars pour savoir, et une décision en novembre. Voilà. Des questions ?",
  'la moins spectaculaire': "C'est la partie la moins spectaculaire du projet, et c'est la plus importante.",
  'une évaluation sommaire':"Il a présenté une évaluation sommaire, avec des ordres de grandeur.",

  // Les seize mots du banc de vocabulaire.
  'un projet':                "Elle a préparé son projet sur une seule feuille.",
  'un ordre du jour':         "Le réaménagement du quai est le premier point de l'ordre du jour.",
  'une réunion de production':"La réunion de production commence à huit heures le lundi.",
  'un échéancier':            "Selon l'échéancier, les relevés se terminent le dix-neuf septembre.",
  'une étape':                "La première étape, c'est de mesurer.",
  'la mise en œuvre':         "La mise en œuvre commencera après l'essai.",
  'un budget':                "Le budget de l'essai est de quatre cents dollars.",
  'la manutention':           "La manutention répétitive est la cause des maux de dos.",
  'un poste de travail':      "Le poste de travail numéro quatre sert à l'emballage.",
  'un correctif':             "La rotation des tâches est un correctif qui ne coûte rien.",
  'un programme de prévention':"Le programme de prévention se met à jour chaque année.",
  'une soumission':           "La soumission est valide jusqu'à la fin novembre.",
  'un fournisseur':           "Équipements Sorel est notre fournisseur depuis douze ans.",
  'une note de service':      "La note de service annonce la rotation à l'essai.",
  'un accusé de réception':   "Il a envoyé un accusé de réception le lendemain matin.",

  // Les mots des mini-leçons.
  'par conséquent':        "Le quai n'a pas changé ; par conséquent, les camions attendent.",
  'en revanche':           "L'essai est gratuit ; en revanche, l'installation coûte cher.",
  'en somme':              "En somme : on mesure, on trace, on essaie, on installe.",
  'notamment':             "Certains risques sont faciles à prévoir, notamment la circulation.",
  'nous aurons reçu':      "Quand nous aurons reçu le prix, nous prendrons la décision.",
  'le droit de refus':     "Le droit de refus est écrit dans la loi, pas dans une politique.",
  'un motif raisonnable':  "Il faut un motif raisonnable de croire qu'il y a un danger.",
  'un inspecteur':         "Un inspecteur de la commission décide s'il existe un danger.",
  'la vedette':            "La vedette d'une lettre porte le nom et l'adresse du destinataire.",
  "l'appel":               "L'appel d'une lettre se termine par une virgule.",
  'une pièce jointe':      "Une pièce jointe s'annonce par les lettres p, j, en bas de page.",
  'une salutation':        "La salutation reprend exactement les mots de l'appel.",
};
