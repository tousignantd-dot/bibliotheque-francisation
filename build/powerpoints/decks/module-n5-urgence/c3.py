# -*- coding: utf-8 -*-
"""C3 · « Elle m'a demandé si… » — rapporter une question.
Bloc C « Défi 2 » · couleur ambre · 75 min. Écriture.
Source : exercice `t2ind` et sa mini-leçon.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-urgence/images/')


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="« Elle m'a demandé si… »",
        chapeau="Pendant une hospitalisation, on passe son temps à répéter "
                "à quelqu'un d'autre ce qu'on vient de nous demander. Une "
                "question rapportée n'est plus une question : elle perd son "
                "inversion et son point d'interrogation.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire. C'est le point qui sépare le niveau 5 du niveau "
                  "4 : on ne se contente plus de répondre aux questions, on les rapporte. "
                  "Le dire au groupe, cela motive.")

    d.objectifs([
        "rapporter une question fermée avec « si » ;",
        "employer « ce qui » et « ce que » à la place de « qu'est-ce qui / que » ;",
        "garder où, quand, combien, pourquoi tels quels ;",
        "rétablir l'ordre sujet + verbe, sans inversion.",
    ])

    d.declencheur(
        'Situation', "Vous sortez du triage et votre frère demande : « Qu'est-ce "
                     "qu'ils t'ont demandé ? » Vous répondez comment ?",
        image=IMG + 'telephone-nuit.jpg',
        pistes=[
            "Répétez-vous la question mot pour mot ?",
            "Que devient « est-ce que » ?",
            "Où passe le sujet ?",
            "Y a-t-il encore un point d'interrogation ?",
        ],
        notes="Faire produire deux ou trois réponses spontanées et les écrire au tableau "
              "sans les corriger. On y reviendra en fin de séance.")

    d.regle("Une question rapportée n'est plus une question",
            "« Est-ce qu'elle est consciente ? » donne Il m'a demandé si elle était consciente.",
            precision="Plus d'inversion, plus de point d'interrogation, et « est-ce que » "
                      "disparaît complètement. La phrase devient un simple complément du "
                      "verbe « demander ».",
            notes="Diapositive à photographier. Insister sur la disparition de « est-ce "
                  "que » : c'est l'erreur la plus visible.")

    d.tableau('Le mot de liaison', "Ce qui change, et ce qui ne change pas",
              ['La question posée', 'Rapportée'],
              [["Est-ce qu'elle est consciente ?", "… si elle était consciente"],
               ["Qu'est-ce qui s'est passé ?", "… ce qui s'était passé"],
               ["Qu'est-ce que vous avez vu ?", "… ce que j'avais vu"],
               ["Où avez-vous mal ?", "… où elle avait mal"],
               ["Quel âge a-t-elle ?", "… quel âge elle avait"]],
              cle=1,
              note="où, quand, comment, combien et quel ne changent pas de forme.",
              notes="Faire lire la colonne de droite à voix haute : l'oreille repère "
                    "l'ordre sujet + verbe mieux que l'œil.")

    d.cartes("Trois mécanismes, et rien d'autre", "À ce niveau, la liste est complète", [
        ("Question fermée donne si",
         "Toute question à laquelle on répond par oui ou non."),
        ("Qu'est-ce qui donne ce qui",
         "Le mot est sujet : il est suivi d'un verbe."),
        ("Qu'est-ce que donne ce que",
         "Le mot est complément : il est suivi d'un sujet."),
        ("Les autres mots donne inchangés",
         "Seul l'ordre des mots redevient normal."),
    ], notes="Le raccourci qui marche : si la réponse commence par un verbe, c'est « ce "
             "qui » ; si elle commence par quelqu'un, c'est « ce que ».")

    d.pratique('Transformation', "Rapportez la question",
               "À l'oral d'abord, puis à l'écrit.", [
        ("« Est-ce qu'elle est consciente ? » donne Il m'a demandé ___ elle était consciente.", "si"),
        ("« Est-ce qu'elle prend des médicaments ? » donne … ___ elle prenait des médicaments.", "si"),
        ("« Qu'est-ce qui s'est passé ? » donne Elle m'a demandé ___ s'était passé.", "ce qui"),
        ("« Qu'est-ce que vous avez vu ? » donne … ___ j'avais vu.", "ce que"),
        ("« Où avez-vous mal ? » donne Elle lui a demandé ___ elle avait mal.", "où"),
        ("« Quand est-elle tombée ? » donne … ___ elle était tombée.", "quand"),
        ("« Combien de temps allons-nous attendre ? » donne Je ne sais pas ___ de temps…", "combien"),
        ("« Est-ce qu'elle a des allergies ? » donne Elle m'a demandé ___ ma mère avait des allergies.", "si"),
    ], corrige=True,
       notes="La septième montre que « je ne sais pas… » se construit exactement comme "
             "« il m'a demandé… ». Un seul mécanisme, deux entrées.")

    d.piege("Garder « est-ce que »",
            "Il m'a demandé est-ce qu'elle respirait.",
            "Il m'a demandé si elle respirait.",
            "« Est-ce que » n'existe que dans une vraie question, celle qui se termine par "
            "un point d'interrogation.",
            notes="Très fréquent, et très visible à l'écrit. Le corriger sans "
                  "dramatiser : la structure est simple une fois nommée.")

    d.piege("Garder l'inversion",
            "Je ne sais pas où est-elle.",
            "Je ne sais pas où elle est.",
            "Dans une question rapportée, l'ordre redevient sujet + verbe. L'inversion "
            "appartient à la question directe.",
            notes="Faire relire les phrases spontanées du déclencheur : l'erreur y est "
                  "presque toujours. C'est le moment le plus efficace de la séance.")

    d.billet(
        "Écrivez quatre questions qu'on vous a posées cette semaine, rapportées.",
        exemples=[
            "Deux avec « si », une avec « ce que » ou « ce qui », une avec où ou quand.",
            "Au travail, à l'école, chez le médecin : n'importe où.",
        ],
        notes="Ramasser. Les phrases justes ouvriront la séance C4, où l'on travaillera "
              "les questions à poser soi-même pendant l'attente.")

    return d.save(dossier)
