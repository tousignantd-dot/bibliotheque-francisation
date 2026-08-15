# -*- coding: utf-8 -*-
"""A3 · Ce qu'il faut vérifier avant de signer.
Bloc A · couleur acier (compréhension) · 75 min.
Source : exercice `pr3` — douze sujets à vérifier pendant une visite.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='acier',
        titre='Avant de signer',
        chapeau="Douze choses à vérifier, dont la moitié ne se voit pas pendant une "
                "visite de dix minutes. Celles-là, il faut les demander — et pour les "
                "demander, il faut savoir qu'elles existent.",
        duree='75 minutes')

    d.titre(notes="Séance de préparation pratique. Écrire au tableau : CE QUI SE VOIT, CE "
                  "QUI SE DEMANDE. C'est la structure de la séance.")

    d.objectifs([
        "connaître les douze sujets à vérifier avant de signer un bail ;",
        "distinguer ce qui se voit de ce qui se demande ;",
        "associer une phrase entendue au sujet dont elle relève ;",
        "préparer sa liste de questions avant une visite.",
    ])

    d.tableau('Analyse · 1 de 2', "Ce qui se prépare avant la visite",
              ['Le sujet', 'La question à poser'],
              [["la durée du bail", "Le bail dure combien de temps ?"],
               ["le quartier", "Y a-t-il des commerces et des familles autour ?"],
               ["la luminosité", "Le salon reçoit-il le soleil ?"],
               ["le nombre de pièces", "Combien de chambres fermées ?"],
               ["les étages", "À quel étage, et y a-t-il un ascenseur ?"],
               ["les services à proximité", "L'arrêt d'autobus est-il loin ?"]],
              cle=0, props=[0.32, 0.68],
              notes="Ces six sujets se préparent à la maison, avant même de se déplacer. "
                    "Beaucoup d'entre eux se vérifient sur une carte.")

    d.tableau('Analyse · 2 de 2', "Ce qui se vérifie sur place",
              ['Le sujet', 'La question à poser'],
              [["l'insonorisation", "Est-ce qu'on entend la rue ou les voisins ?"],
               ["le stationnement", "Où est-ce que je laisse mon auto la nuit ?"],
               ["les animaux permis", "Est-ce que les chats sont acceptés ?"],
               ["l'état des lieux", "Les fenêtres ont-elles été changées ?"],
               ["les inclusions", "La cuisinière et le réfrigérateur restent-ils ?"],
               ["les coûts", "Est-ce que je recevrai une facture d'électricité ?"]],
              cle=0, props=[0.3, 0.7],
              notes="Ces six-là exigent d'être sur place, ou de poser la question à la "
                    "propriétaire. Ce sont ceux qu'on oublie.")

    d.regle('La règle de la visite',
            "Écrivez vos questions avant de partir. Sur place, on oublie.",
            precision="Dix minutes de visite, une propriétaire qui parle, un logement à "
                      "regarder : personne ne se souvient de ses douze questions. Une "
                      "liste sur papier ou dans le téléphone change tout.",
            notes="Faire écrire la liste dans le cahier, en deux colonnes. C'est un outil "
                  "à garder longtemps après le module.")

    d.pratique('Pratique · 1 de 4', "De quoi parle-t-on ?",
               "Associez la phrase au sujet.", [
        ("Je dors le matin, après mon quart de soir.", "l'insonorisation"),
        ("Ma sœur vient souvent : il me faudrait une deuxième chambre.",
         "le nombre de pièces"),
        ("Est-ce que je recevrai une facture d'Hydro chaque deux mois ?",
         "les coûts d'électricité et de chauffage"),
        ("Le contrat court jusqu'au 31 août prochain.", "la durée du bail"),
        ("Il faudra monter le divan jusqu'en haut de l'escalier.", "les étages"),
        ("Je laisse mon auto où, la nuit ?", "le stationnement"),
    ], corrige=True,
       notes="Faire nommer le sujet avant de le lire. Les phrases sont concrètes : c'est "
             "ce qui rend l'exercice facile.")

    d.pratique('Pratique · 2 de 4', "Six autres phrases",
               "Associez la phrase au sujet.", [
        ("Y a-t-il des familles et des commerces dans les environs ?", "le quartier"),
        ("La cuisinière et le réfrigérateur restent-ils dans le logement ?",
         "les inclusions"),
        ("Le salon reçoit-il le soleil en fin de journée ?", "la luminosité"),
        ("La pharmacie et l'arrêt d'autobus sont-ils loin d'ici ?",
         "les services à proximité"),
        ("J'aimerais adopter un chat cet automne.", "les animaux permis"),
        ("Les fenêtres ont-elles été changées récemment ?", "l'état des lieux"),
    ], corrige=True,
       notes="Douze sujets en tout. Les faire cocher au fur et à mesure : le groupe verra "
             "la liste se compléter.")

    d.cartes('Analyse', "Quatre choses qu'on ne voit pas en dix minutes", [
        ("Le bruit du matin",
         "Une visite se fait le jour, quand tout est calme. Le camion de farine de cinq "
         "heures ne se devine pas. Il faut demander."),
        ("Le froid en janvier",
         "Un logement visité en juin peut être glacial en hiver. Demandez le montant "
         "des factures d'électricité de l'année précédente."),
        ("Les voisins",
         "Personne ne les voit pendant la visite. Demandez qui habite au-dessus et "
         "en dessous, et depuis combien de temps."),
        ("Le déneigement",
         "Qui déneige l'entrée, l'escalier, la place de stationnement ? La réponse "
         "n'est presque jamais dans l'annonce."),
    ], notes="Ces quatre questions sont celles que personne ne pose et que tout le monde "
             "regrette. Les faire copier.")

    d.piege("Le piège de la visite en été",
            "Le logement est parfait, je le prends.",
            "Demandez les factures d'électricité de l'hiver dernier.",
            "Un logement visité en juin ne montre rien de l'hiver : ni le froid, ni les "
            "fenêtres qui laissent passer l'air, ni le coût du chauffage. Les factures "
            "de l'année précédente sont la seule preuve, et on a le droit de les "
            "demander.",
            notes="Point pratique important, surtout au Québec où l'écart entre les "
                  "saisons est extrême.")

    d.piege("Le piège de la question non posée",
            "Je n'ose pas demander, ça fait méfiant.",
            "Une bonne propriétaire préfère répondre avant qu'après.",
            "Poser des questions n'est pas de la méfiance : c'est ce que fait toute "
            "personne qui s'engage pour douze mois. Ginette répond franchement sur le "
            "camion de farine — parce qu'elle préfère un locataire informé à un "
            "locataire déçu.",
            notes="Point culturel utile : au Québec, poser des questions pendant une "
                  "visite est attendu, pas mal vu.")

    d.pratique('Pratique · 3 de 4', "Se voit ou se demande ?",
               "Pendant une visite de dix minutes.", [
        ("La luminosité du salon", "se voit — si on visite de jour"),
        ("Le bruit du camion de farine", "se demande"),
        ("Le nombre de chambres", "se voit"),
        ("Le coût de l'électricité en janvier", "se demande"),
        ("L'état des fenêtres", "se voit et se demande — quand ont-elles été changées ?"),
        ("Qui déneige l'entrée", "se demande"),
    ], corrige=True,
       notes="Le cinquième item est double : on voit l'état, on demande la date. C'est "
             "souvent le cas.")

    d.pratique('Pratique · 4 de 4', "Écrivez votre liste",
               "Six questions à poser lors de votre prochaine visite.", [
        ("Deux sur le logement lui-même", "pièces, luminosité, état"),
        ("Deux sur les coûts", "ce qui est inclus, ce qui ne l'est pas"),
        ("Une sur le bruit", "voisins, rue, commerces au rez-de-chaussée"),
        ("Une sur la vie quotidienne", "stationnement, déneigement, animaux, buanderie"),
    ], corrige=False,
       notes="Quinze minutes. Ramasser : cette liste sera reprise en B4, dans le jeu de "
             "rôle de la visite.")

    d.billet(
        "Écrivez les trois questions que vous ne poseriez pas spontanément.",
        exemples=[
            "Celles auxquelles vous n'auriez pas pensé avant cette séance.",
            "Écrivez-les comme vous les diriez à une propriétaire.",
        ],
        notes="Ce sont ces trois-là qui comptent. Les relever et en faire une liste "
              "collective au tableau.")

    return d.save(dossier)
