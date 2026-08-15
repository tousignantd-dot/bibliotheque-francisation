# -*- coding: utf-8 -*-
"""A4 · Trois petites annonces.
Bloc A · couleur acier (compréhension écrite) · 60 min.
Source : exercice `aAnnonces` — trois logements à louer à Sherbrooke.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='acier',
        titre='Trois petites annonces',
        chapeau="Trois logements, trois prix, trois vies possibles. Aucun n'est meilleur "
                "que les autres : tout dépend de qui cherche.",
        duree='60 minutes')

    d.titre(notes="Distribuer les trois annonces et laisser cinq minutes de lecture "
                  "silencieuse avant toute question.")

    d.objectifs([
        "lire trois annonces et en tirer les informations essentielles ;",
        "comparer trois logements sur plusieurs critères ;",
        "choisir un logement selon une situation donnée ;",
        "justifier son choix.",
    ])

    d.cartes('Les trois annonces', "À louer à Sherbrooke", [
        ("Annonce 1 · un 3 ½ à 780 $",
         "Rez-de-chaussée, quartier Jacques-Cartier. Cour clôturée, entrée pour "
         "laveuse-sécheuse. Chauffé et éclairé. Non-fumeur. Libre immédiatement."),
        ("Annonce 2 · un 5 ½ à 1 250 $",
         "Grand logement dans un triplex, deux salles de bain, à cinq minutes d'une "
         "école primaire et d'un parc. Stationnement pour deux autos. Électroménagers "
         "non fournis. Bail d'un an."),
        ("Annonce 3 · un 4 ½ à 890 $",
         "Repeint, au deuxième étage, au-dessus d'une boulangerie, rue Galt. Chauffage "
         "et eau chaude inclus. Buanderie commune au sous-sol. Chats acceptés. Libre le "
         "1er septembre."),
    ], notes="La troisième annonce est celle qu'Ibrahim a visitée. Le faire remarquer : "
             "on lit maintenant ce qu'il a lu avant d'appeler.")

    d.tableau('Analyse', "Les trois annonces, comparées",
              ['Le critère', '3 ½', '5 ½', '4 ½'],
              [["le loyer", "780 $", "1 250 $", "890 $"],
               ["les chambres", "une", "trois", "deux"],
               ["le chauffage", "inclus", "non", "inclus"],
               ["les électros", "non précisé", "non fournis", "non précisé"],
               ["libre", "immédiatement", "non précisé", "1er septembre"]],
              cle=0, props=[0.28, 0.24, 0.24, 0.24],
              notes="Faire remplir ce tableau par les élèves avant de l'afficher. C'est "
                    "l'exercice le plus formateur de la séance.")

    d.pratique('Pratique · 1 de 4', "Cinq questions sur les annonces",
               "Répondez d'après les textes.", [
        ("Quel logement coûte le moins cher par mois ?", "le 3 ½ à 780 $"),
        ("Dans quelle annonce faut-il apporter ses électroménagers ?",
         "l'annonce 2, le 5 ½ en triplex"),
        ("Quelle annonce conviendrait à une famille de quatre ?",
         "l'annonce 2 : trois chambres, deux salles de bain, école et parc tout près"),
        ("Quel logement accepte les animaux, et lesquels ?",
         "le 4 ½ de la rue Galt accepte les chats"),
        ("Lequel est libre tout de suite ?", "le 3 ½ du quartier Jacques-Cartier"),
    ], corrige=True,
       notes="Faire pointer la phrase exacte pour chaque réponse. Les annonces sont "
             "courtes : l'information est vite trouvée si on sait quoi chercher.")

    d.regle('La règle du choix',
            "Le meilleur logement dépend de qui cherche.",
            precision="Le 3 ½ est le moins cher, le 5 ½ le plus grand, le 4 ½ le plus "
                      "tranquille. Aucun n'est meilleur en soi. Une personne seule, une "
                      "famille et un travailleur de nuit ne choisiront pas le même.",
            notes="Diapo centrale du module. C'est aussi le sujet du défi 3 : quatre "
                  "personnes, quatre besoins.")

    d.pratique('Pratique · 2 de 4', "Quel logement pour qui ?",
               "Et pourquoi celui-là ?", [
        ("Une personne seule avec un petit budget.", "le 3 ½ — le moins cher, chauffé"),
        ("Une famille de quatre avec deux enfants d'âge scolaire.",
         "le 5 ½ — trois chambres, école et parc à cinq minutes"),
        ("Un travailleur de soir qui dort le matin.",
         "le 4 ½ — la chambre donne sur la cour"),
        ("Quelqu'un qui a un chat.", "le 4 ½ — le seul qui les accepte"),
    ], corrige=True,
       notes="Faire justifier chaque choix par un mot de l'annonce. Ne jamais accepter "
             "« parce que c'est mieux ».")

    d.piege("Le piège du plus grand",
            "Le 5 ½ est le meilleur, il est plus grand.",
            "Il coûte 1 250 $, sans chauffage, et sans électroménagers.",
            "Plus grand veut dire plus cher à louer, à chauffer et à meubler. Pour une "
            "personne seule, un 5 ½ est une mauvaise affaire, même s'il est plus beau. "
            "Le bon logement est celui qui correspond au nombre de personnes.",
            notes="Faire calculer le coût réel du 5 ½ : loyer, électricité, achat des "
                  "électroménagers. L'écart avec le 3 ½ est considérable.")

    d.piege("Le piège de « non précisé »",
            "L'annonce ne parle pas des électroménagers, donc ils sont fournis.",
            "Ce qui n'est pas écrit doit être demandé.",
            "Une annonce ne dit jamais tout. « Non précisé » ne veut dire ni oui ni "
            "non : cela veut dire qu'il faut poser la question avant de visiter. C'est "
            "un appel de deux minutes qui évite un déplacement inutile.",
            notes="Relier à la séance A3 : ce qui n'est pas écrit fait partie de la "
                  "liste des questions à poser.")

    d.pratique('Pratique · 3 de 4', "Qu'est-ce qui manque dans chaque annonce ?",
               "Une information non précisée par annonce.", [
        ("Annonce 1 — le 3 ½", "les animaux, le stationnement, les électroménagers"),
        ("Annonce 2 — le 5 ½", "le chauffage, la date de disponibilité, les animaux"),
        ("Annonce 3 — le 4 ½", "les électroménagers, le stationnement, le bruit"),
    ], corrige=True,
       notes="Faire écrire, pour chaque annonce, la première question qu'on poserait au "
             "téléphone. C'est l'exercice utile.")

    d.pratique('Pratique · 4 de 4', "Choisissez et justifiez",
               "Lequel prendriez-vous, et pourquoi ?", [
        ("Votre choix", "un seul des trois"),
        ("Votre raison principale", "une phrase, en lien avec votre situation"),
        ("Ce qui vous manque pour décider", "une question à poser au propriétaire"),
        ("Ce que vous accepteriez de perdre", "un compromis, en une phrase"),
    ], corrige=False,
       notes="Dix minutes, puis quelques présentations à voix haute. Les choix diffèrent "
             "beaucoup et les justifications sont instructives.")

    d.billet(
        "Choisissez une des trois annonces et justifiez votre choix en trois phrases.",
        exemples=[
            "Votre situation, votre raison, votre compromis.",
            "Employez « parce que » au moins une fois.",
        ],
        notes="Ramasser. Ces justifications préparent le défi 2, où l'on dira ce qui "
              "plaît et ce qui inquiète.")

    return d.save(dossier)
