# -*- coding: utf-8 -*-
"""C1 · Est-ce que je peux échanger mon jeudi ?
Bloc C « Défi 2 · Est-ce que je peux vous demander ? » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t2vf`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-horaire/images/')


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Est-ce que je peux échanger mon jeudi ?",
        chapeau="Deux phrases changent tout au travail : « est-ce que je "
                "peux… ? » demande une permission, « est-ce que vous pouvez "
                "m'aider ? » demande un service. Fabiola a besoin des deux "
                "dans la même semaine.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 2. Faire remarquer d'entrée que Fabiola ne demande "
                  "pas une faveur : elle demande un échange prévu par les règles de la "
                  "place. La différence compte pour la confiance en soi.")

    d.objectifs([
        "comprendre une demande d'échange de quart ;",
        "relever la règle de la place : aviser trois jours avant ;",
        "distinguer une demande de permission d'une demande d'aide ;",
        "entendre une réponse conditionnelle : « vous pouvez, mais… ».",
    ])

    d.declencheur(
        'Observation', "Comment demander à changer une journée de travail ?",
        image=IMG + 'note-papier.jpg',
        pistes=[
            "À qui faut-il demander, à votre travail ?",
            "Combien de temps à l'avance ?",
            "Est-ce qu'il faut trouver quelqu'un soi-même ?",
            "Est-ce qu'on doit dire pourquoi ?",
        ],
        notes="La troisième question est la vraie : dans la plupart des milieux, c'est à "
              "l'employé de trouver son remplaçant. Beaucoup d'élèves l'ignorent et "
              "croient qu'un refus est un refus personnel.")

    d.dialogue('Dialogue · 1 de 3', "Est-ce que je peux vous parler ?", [
        ("FABIOLA", "Monsieur Roy, est-ce que je peux vous parler deux minutes ?", True),
        ("GAÉTAN", "Bien sûr. Qu'est-ce qui se passe ?", True),
        ("FABIOLA", "Jeudi prochain, mon garçon a un rendez-vous à la clinique.", True),
        ("GAÉTAN", "À quelle heure, le rendez-vous ?", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="La première réplique est une demande avant la demande : on demande d'abord "
             "du temps, ensuite la chose. C'est ce qui évite d'arriver au mauvais moment "
             "au milieu d'un service.")

    d.dialogue('Dialogue · 2 de 3', "Il faut m'aviser trois jours avant", [
        ("GAÉTAN", "Est-ce que quelqu'un peut prendre votre quart de jeudi ?", True),
        ("FABIOLA", "Miguel dit qu'il peut. Est-ce que je pourrais échanger avec lui ?", True),
        ("GAÉTAN", "Vous pouvez, oui. Mais il faut m'aviser trois jours avant.", True),
        ("FABIOLA", "Trois jours. Aujourd'hui, c'est lundi : est-ce que ça va ?", True),
    ], notes="Trois choses à relever : Fabiola a trouvé son remplaçant avant de demander, "
             "elle emploie la forme polie « je pourrais », et elle vérifie la règle en "
             "comptant les jours à voix haute. Trois réflexes d'employé d'expérience.")

    d.dialogue('Dialogue · 3 de 3', "Est-ce que vous pouvez m'aider ?", [
        ("MIGUEL", "Monsieur Roy, est-ce que vous pouvez m'aider une seconde ?", True),
        ("GAÉTAN", "Oui, Miguel. Qu'est-ce qu'il y a ?", False),
        ("MIGUEL", "Le lave-vaisselle affiche un chiffre rouge. Je ne comprends pas.", True),
        ("FABIOLA", "Est-ce que je peux regarder ? Je ne l'ai jamais fait.", True),
    ], notes="Les deux demandes sont côte à côte : Miguel demande de l'aide — quelqu'un "
             "doit faire quelque chose —, Fabiola demande une permission — elle veut "
             "faire quelque chose. C'est tout le défi, en quatre répliques.")

    d.tableau('Analyse', "Deux demandes qui ne se ressemblent pas",
              ["La phrase", "Ce qu'elle demande"],
              [["Est-ce que je peux… ?", "une permission : l'autre dit oui ou non"],
               ["Est-ce que vous pouvez m'aider ?", "un service : l'autre fait quelque chose"],
               ["Est-ce que je pourrais… ?", "la même permission, en plus poli"],
               ["Il faut aviser trois jours avant.", "la règle de la place, pour tout le monde"]],
              cle=1,
              note="La quatrième n'est pas une demande : c'est la réponse "
                   "qui encadre toutes les autres.",
              notes="Diapo à photographier. C'est le tableau de référence du défi, et il "
                    "sert directement à l'exercice de C3.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Fabiola demande à parler à monsieur Roy deux minutes.", "vrai"),
        ("Son garçon a un rendez-vous à la clinique jeudi.", "vrai"),
        ("Personne ne peut prendre son quart de jeudi.", "faux — Miguel peut"),
        ("Il faut aviser le chef d'équipe trois jours avant.", "vrai"),
        ("Miguel comprend tout de suite le lave-vaisselle.", "faux — il demande de l'aide"),
        ("Fabiola demande la permission de regarder.", "vrai"),
    ], corrige=True,
       notes="C'est l'exercice `t2vf` du module interactif, mot pour mot. La dernière "
             "ligne mérite un arrêt : Fabiola demande à apprendre quelque chose qui n'est "
             "pas sa tâche. C'est ce qui la rend précieuse pour l'équipe.")

    d.billet(
        "Écrivez une demande que vous auriez à faire au travail.",
        exemples=[
            "Une permission, ou de l'aide — dites laquelle.",
            "« Est-ce que je peux partir à midi vendredi ? »",
        ],
        notes="Devoir court. Ramasser : ces demandes réelles serviront en C3 et en E1. "
              "Chacun travaillera la sienne plutôt qu'un exemple inventé.")

    return d.save(dossier)
