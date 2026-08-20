# -*- coding: utf-8 -*-
"""B1 · Tout droit, à droite, à gauche.
Bloc B « Défi 1 · Demander son chemin » · couleur acier · 75 min.
Source : dialogue `t1`, exercices `t1vf`, `t1direction`, mini-leçon `t1direction`.

Six mots portent presque toute l'information d'une réponse. La séance ne
cherche pas à faire comprendre la phrase entière : elle apprend à attraper
ces six mots-là au vol.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-autobus/images/')


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Tout droit, à droite, à gauche",
        chapeau="On ne comprendra pas toute la phrase, et ce n'est pas grave. "
                "Six mots suffisent à trouver son chemin.",
        duree='75 minutes')

    d.titre(notes="Ouvrir la séance debout, sans un mot de français : montrer la direction "
                  "avec la main et faire nommer par le groupe. Beaucoup connaissent déjà "
                  "les gestes.")

    d.objectifs([
        "comprendre les six mots de la direction ;",
        "suivre une direction en trois étapes ;",
        "donner une direction simple ;",
        "employer « jusqu'au », « jusqu'à la ».",
    ])

    d.declencheur(
        'Observation', "Que dit ce feu ?",
        image=IMG + 'feu-circulation.jpg',
        pistes=[
            "Qu'est-ce qu'on voit ?",
            "Que fait-on quand il est rouge ?",
            "Pourquoi le feu sert-il à expliquer un chemin ?",
            "Quels autres repères se voient de loin ?",
        ],
        notes="Amener l'idée du repère : un feu, une pharmacie, une école se voient de "
              "loin, un nom de rue non. C'est l'idée centrale de la séance.")

    d.dialogue('Dialogue', "Je répète pour être sûr", [
        ("MARIE-JOSÉE", "Vous continuez tout droit jusqu'au feu.", True),
        ("HASSAN", "Jusqu'au feu.", True),
        ("MARIE-JOSÉE", "Au feu, vous tournez à droite.", True),
        ("HASSAN", "À droite au feu.", True),
        ("MARIE-JOSÉE", "Et la bibliothèque est au coin, à gauche.", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Faire écouter deux fois, diapositive masquée. Demander ensuite : « Combien "
             "d'étapes ? » Réponse : trois. C'est presque toujours trois.")

    d.tableau('Analyse', "Les six mots",
              ['Le mot', 'Ce qu\'il dit'],
              [["tout droit", "ne tournez pas"],
               ["à droite / à gauche", "tournez de ce côté"],
               ["jusqu'à", "allez jusque-là, puis arrêtez"],
               ["au coin", "là où deux rues se rencontrent"],
               ["après", "d'abord ceci, ensuite cela"]],
              cle=2,
              note="Ces mots-là portent l'information. Le reste de la phrase, on peut le "
                   "perdre sans conséquence.",
              notes="Diapositive à photographier. C'est la diapositive la plus importante "
                    "du bloc B : y consacrer dix minutes.")

    d.regle("Jusqu'au, jusqu'à la",
            "« Jusqu'à » se colle à l'article, comme « à ».",
            precision="jusqu'<b>au</b> feu (masculin) · jusqu'<b>à la</b> pharmacie "
                      "(féminin) · jusqu'<b>à l'</b>école (voyelle).",
            notes="Diapositive à photographier. Faire le lien explicite avec la mini-leçon "
                  "de A1 : c'est la même règle, appliquée à un autre mot.")

    d.piege('Piège', "à droite", "tout droit",
            "Deux expressions très proches, deux sens opposés. <b>Tout droit</b> : on ne "
            "tourne pas. <b>À droite</b> : on tourne. Dans le doute, montrer la direction "
            "avec la main et demander « comme ça ? ».",
            notes="Faire l'exercice debout : l'enseignant dit, le groupe montre du bras. "
                  "L'erreur se voit tout de suite et se corrige sans un mot.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Il faut continuer tout droit jusqu'au feu.", "vrai"),
        ("Au feu, on tourne à gauche.", "faux — à droite"),
        ("La bibliothèque est au coin.", "vrai"),
        ("Hassan répète ce qu'il a compris.", "vrai"),
    ], corrige=True, cols=1,
       notes="La dernière ligne annonce la séance B2. Ne pas la développer ici.")

    d.pratique('Pratique · à deux', "Expliquez un chemin",
               "Deux par deux, avec un plan du quartier.", [
        ("Étape 1", "Choisissez un lieu, sans le dire à votre voisin."),
        ("Étape 2", "Expliquez le chemin en trois étapes."),
        ("Étape 3", "Votre voisin suit sur le plan et devine le lieu."),
        ("Étape 4", "Échangez les rôles."),
    ], cols=1,
       notes="Vingt-cinq minutes. Imposer les trois étapes : ni deux, ni six. C'est la "
             "contrainte qui fait apprendre.")

    d.billet(
        "Écrivez le chemin du centre jusqu'à chez vous, en trois étapes.",
        exemples=[
            "Je sors et je vais tout droit.",
            "Au feu, je tourne à gauche.",
            "Ma maison est au coin.",
        ],
        notes="Devoir court. Trois phrases, pas plus. Certains dessineront un plan : "
              "l'accepter, c'est un bon signe.")

    return d.save(dossier)
