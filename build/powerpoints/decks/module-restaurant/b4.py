# -*- coding: utf-8 -*-
"""B4 · Poser la question qui manque.
Bloc B · couleur acier · 55 min.
Source : exercice `t1question`, dialogue `t1`, cartes mémoire.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='acier',
        titre='Poser la question qui manque',
        chapeau="Six questions font le tour d'un repas, de l'entrée à "
                "l'addition. Chacune a son moment — et l'une d'elles ne "
                "supporte pas d'attendre.",
        duree='55 minutes')

    d.titre(notes="Séance de synthèse du bloc B. Elle prépare directement le jeu de rôle de "
                  "E1.")

    d.objectifs([
        "connaître les six questions et leur moment ;",
        "signaler une allergie ou un régime au bon moment ;",
        "demander ce qu'il y a dans un plat ;",
        "nommer les mots du menu et du repas.",
    ])

    d.tableau('Analyse', "Six questions, six moments",
              ['La question', 'Quand'],
              [["Il y a de la place ?", "à l'entrée"],
               ["Qu'est-ce qu'il y a dans la table d'hôte ?", "avant de choisir"],
               ["Le plat du jour, c'est quoi ?", "avant de choisir"],
               ["Il y a des arachides dedans ?", "au moment de commander"]],
              cle=3,
              note="Et : « est-ce que je pourrais avoir… ? » pendant le repas, « l'addition, s'il vous plaît » à la fin.",
              notes="Diapo à photographier. C'est la liste de vérification de tout le "
                    "module.")

    d.regle("La question qui ne peut pas attendre",
            "Une allergie ou un régime se signale à la commande.",
            precision="Quand l'assiette est devant vous, la cuisine ne peut plus rien "
                      "faire. À la commande, elle peut changer un ingrédient, proposer "
                      "autre chose, ou simplement vérifier. Andrés pose la question pour "
                      "le dessert dès la commande — c'est exactement le bon moment.",
            notes="Point de sécurité. Faire écrire à chacun la phrase qui correspond à sa "
                  "propre situation.")

    d.cartes("Comment formuler une restriction", "Quatre situations", [
        ("Une allergie",
         "« Est-ce qu'il y a des arachides dedans ? » · « Je suis allergique aux fruits de "
         "mer. » Direct et clair : ce n'est pas le moment d'être discret."),
        ("Un régime religieux ou personnel",
         "« Est-ce que c'est fait avec du porc ? » · « Je ne mange pas de viande. » Aucune "
         "explication n'est nécessaire."),
        ("Une préférence",
         "« Est-ce que ce serait possible sans sauce ? » — c'est une demande, pas une "
         "restriction, et elle peut être refusée."),
        ("Ce que le serveur fera",
         "Il vérifiera en cuisine si nécessaire. C'est une question qu'il reçoit tous les "
         "jours."),
    ], notes="Insister sur le fait qu'aucune explication n'est due. « Je ne mange pas de "
             "porc » est une phrase complète.")

    d.piege("Être trop discret sur une allergie",
            "Je pense que ça devrait aller.",
            "Je suis allergique aux arachides. Est-ce qu'il y en a dans ce plat ?",
            "Une allergie n'est pas une préférence, et la discrétion peut coûter très cher. "
            "Les restaurants sont habitués à ces questions et prennent le sujet au sérieux "
            "— c'est leur responsabilité légale autant que professionnelle.",
            notes="Ce point mérite du temps. Plusieurs élèves n'osent pas, par crainte de "
                  "déranger.")

    d.pratique('Pratique · 1 de 2', "Quelle question, à quel moment ?",
               "Dites quand on pose chaque question.", [
        ("« Il y a de la place ? »", "à l'entrée"),
        ("« Qu'est-ce qu'il y a dans la table d'hôte ? »", "avant de choisir"),
        ("« Est-ce qu'il y a des arachides dedans ? »", "au moment de commander"),
        ("« Est-ce que je pourrais avoir un peu de sel ? »", "pendant le repas"),
        ("« L'addition, s'il vous plaît. »", "à la fin"),
    ], corrige=True, cols=1,
       notes="Faire répondre à voix haute avant d'afficher.")

    d.pratique('Pratique · 2 de 2', "Le mot juste",
               "Complétez avec le mot du vocabulaire.", [
        ("La ___ donne tout ce que le restaurant sert.", "carte"),
        ("La table d'___ comprend trois services.", "hôte"),
        ("Soupe ou salade en ___ .", "entrée"),
        ("Le ___ principal arrive après.", "plat"),
        ("Le riz est servi comme ___ .", "accompagnement"),
        ("Une ___ d'eau pour deux, s'il vous plaît.", "carafe"),
    ], corrige=True,
       notes="Ces six mots sont dans le banc de vocabulaire du module.")

    d.billet(
        "Écrivez les six questions du tableau, en les adaptant à vous.",
        exemples=[
            "Ajoutez votre allergie, votre régime, ou une préférence.",
            "Écrivez-les comme vous les diriez.",
        ],
        notes="Corriger et rendre : cette page devient la fiche que l'élève emportera. "
              "Plusieurs la gardent dans leur téléphone.")

    return d.save(dossier)
