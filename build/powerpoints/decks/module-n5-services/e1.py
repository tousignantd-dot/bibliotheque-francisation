# -*- coding: utf-8 -*-
"""E1 · L'appel, et le message dans la boîte vocale.
Bloc E « Je me lance » · couleur teal · 75 min. Production orale.
Source : bloc `appli` — jeu de rôle `services` et production orale.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-services/images/')


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="L'appel, et le message dans la boîte vocale",
        chapeau="Cette fois personne ne répond. Une minute pour laisser un "
                "message complet, et pas de deuxième chance : on ne "
                "rappelle pas quelqu'un pour lui faire répéter son numéro.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Ramasser le devoir D1 et lire cinq premières "
                  "phrases de guichet à voix haute, sans nommer les auteurs. Le groupe "
                  "dit laquelle il trouve la plus efficace, et pourquoi.")

    d.objectifs([
        "mener un appel complet du menu jusqu'à la clôture ;",
        "laisser un message de boîte vocale en quatre temps ;",
        "donner un numéro de rappel de façon audible du premier coup ;",
        "s'écouter et se corriger avant d'envoyer.",
    ])

    d.declencheur(
        'Écoute', "Un message sur un répondeur. Pourriez-vous rappeler cette personne ?",
        image=IMG + 'appel-telephone.jpg',
        pistes=[
            "« Oui bonjour c'est moi j'avais appelé pour le bac rappelez-moi merci »",
            "Qui est-ce ?",
            "À quel numéro la rappeler ?",
            "De quoi s'agissait-il exactement ?",
        ],
        notes="Dire le message très vite, sans pause, comme un vrai. Les trois questions "
              "restent sans réponse et le groupe le voit tout de suite. C'est le meilleur "
              "déclencheur du module.")

    d.regle("Un message vaut ce qu'on peut en faire",
            "Un nom, un numéro de dossier, une demande, un numéro de rappel.",
            precision="La personne qui écoute votre message ne vous connaît pas et a "
                      "quarante messages avant le vôtre. Si l'un des quatre éléments "
                      "manque, elle ne peut rien faire — et votre demande s'arrête là.",
            notes="Diapositive à photographier. C'est la règle centrale de la production "
                  "orale ; y revenir à chaque écoute.")

    d.tableau('Les quatre temps du message', "Une minute, pas plus",
              ['Temps', 'Ce qu\'on dit'],
              [["1. Se nommer", "« Ici Leïla Haddad, au sujet de la requête 24-118-7690. »"],
               ["2. Rappeler la situation", "deux phrases : ce qui s'est passé, ce qui avait été annoncé"],
               ["3. Dire ce qu'on attend", "« Je voudrais savoir si la requête est toujours ouverte. »"],
               ["4. Laisser un rappel", "un numéro, un moment — et on répète le numéro"]],
              cle=0,
              note="Le numéro se dit deux fois, en début et en fin de message. Toujours.",
              notes="Diapositive à photographier. La note du bas est le geste que personne "
                    "ne fait spontanément et qui change tout.")

    d.cartes("Le jeu de rôle avec l'assistant", "Avant de vous enregistrer", [
        ("Trois situations",
         "Le bac qui n'est plus ramassé · le vieux réfrigérateur · la demande bloquée."),
        ("Deux rôles",
         "Vous appelez, ou vous êtes le préposé. Faites les deux : le niveau 5 demande les deux."),
        ("La règle du jeu",
         "L'assistant ne donne jamais un renseignement avant qu'on le lui demande."),
        ("Ce que ça vous apprend",
         "Ce que vous n'aurez pas demandé, vous ne le saurez pas. Comme au vrai téléphone."),
    ], notes="Insister sur la troisième carte : c'est ce qui rend l'exercice utile et "
             "parfois frustrant. Prévenir, sinon les élèves croient que l'outil fonctionne mal.")

    d.pratique('Préparation', "Écrivez vos quatre temps",
               "Une ligne par temps, avant de vous enregistrer.", [
        ("Temps 1 — se nommer et donner le numéro",
         "« Bonjour, ici … , au sujet de la requête … »"),
        ("Temps 2 — la situation, en deux phrases",
         "« J'ai appelé … parce que … On m'avait annoncé un délai de … »"),
        ("Temps 3 — ce que vous attendez",
         "« Je voudrais savoir si … et quand … »"),
        ("Temps 4 — le rappel",
         "« Vous pouvez me rappeler au … , de préférence … Je répète : … »"),
    ], corrige=False,
       notes="Dix minutes d'écriture individuelle. Circuler et vérifier surtout le temps "
             "4 : c'est celui qu'on bâcle, et c'est celui qui décide du rappel.")

    d.piege("Parler trop vite en donnant son numéro",
            "cinqcentquatorzecinqcinqcinqzéroundeux",
            "Cinq… un… quatre… cinq… cinq… cinq… zéro… un… huit… deux.",
            "Un numéro se dit chiffre par chiffre, lentement, et deux fois. La personne "
            "qui écoute le note à la main, souvent sans pouvoir réécouter. C'est le "
            "moment du message où il faut ralentir le plus.",
            notes="Faire l'expérience : dictez un numéro vite, puis lentement, et "
                  "demandez au groupe de l'écrire les deux fois. La démonstration est nette.")

    d.pratique('Jeu de rôle', "Deux par deux, dos à dos",
               "L'un appelle, l'autre est le préposé. Puis on inverse.", [
        ("Le bac qui n'est plus ramassé", "le préposé ne dit rien qu'on ne lui demande pas"),
        ("Le vieux réfrigérateur", "gratuit pour les résidents, preuve de résidence exigée"),
        ("La demande bloquée en ligne", "il faut se déplacer : deux pièces d'identité"),
    ], corrige=False,
       notes="Vingt minutes. Circuler avec la grille des sept choses à faire et cocher "
             "sans interrompre. Bilan collectif à la fin : quelles questions ont été "
             "oubliées le plus souvent ?")

    d.billet(
        "Enregistrez votre message dans le module et écoutez-vous.",
        exemples=[
            "Écoutez-vous comme si vous étiez le préposé : pourriez-vous rappeler cette personne ?",
            "Recommencez autant de fois qu'il faut, puis envoyez.",
        ],
        notes="La consigne d'écoute est la partie qui apprend. Insister : un élève qui "
              "s'écoute une fois corrige plus d'erreurs qu'avec dix minutes de correction.")

    return d.save(dossier)
