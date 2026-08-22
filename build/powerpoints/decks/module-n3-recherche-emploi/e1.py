# -*- coding: utf-8 -*-
"""E1 · Pousse la porte.
Bloc E « Je me lance » · couleur teal · 75 min. Production orale.
Source du module : section `appli`, jeu de rôle `embauche`, exercice `aQui`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre='Pousse la porte',
        chapeau="Tout ce qui a été appris tient en trente secondes debout "
                "devant un comptoir. On répète avec l'assistant, puis on "
                "s'enregistre, puis on y va pour de vrai.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Reprendre les billets de A3 et de B2 : le "
                  "commerce que chacun avait nommé, et la question qu'il comptait "
                  "poser. La production orale porte sur ce commerce-là.")

    d.objectifs([
        "offrir ses services de vive voix, sans papier ;",
        "poser sa question et comprendre la réponse ;",
        "donner ses disponibilités et ses coordonnées ;",
        "s'enregistrer, s'écouter, recommencer.",
    ])

    d.tableau('Le plan', "Trois temps, et rien de plus",
              ['Le temps', 'Ce qu\'on dit'],
              [["1. Saluer et demander",
                "Bonjour. J'ai vu votre affiche. Est-ce que vous engagez ?"],
               ["2. Se faire connaître",
                "Je sais faire… J'ai de l'expérience en… Je suis libre du… au…"],
               ["3. Laisser sa trace",
                "Je m'appelle… Vous pouvez me joindre au… Merci, bonne journée !"]],
              cle=0,
              note="Trente à quarante-cinq secondes en tout. Pas davantage.",
              notes="Diapo à photographier, et à laisser affichée pendant toute la "
                    "production. C'est le seul soutien autorisé.")

    d.cartes("Le jeu de rôle avec l'assistant", "Trois situations, au choix", [
        ("La boulangerie",
         "Une affiche rouge dans la vitrine : « On embauche ». Vous entrez à neuf "
         "heures et demie, quand le comptoir est calme."),
        ("Le centre communautaire",
         "Pas d'affiche : c'est une voisine qui vous l'a dit. Vous entrez à l'accueil "
         "et vous demandez d'abord à qui parler."),
        ("L'épicerie",
         "Une petite annonce punaisée au babillard. Vous l'apportez à la caisse et "
         "vous offrez vos services."),
        ("Ce que l'assistant ne fera pas",
         "Il ne donnera ni l'horaire, ni le salaire, ni les tâches si vous ne les "
         "demandez pas. C'est exprès : c'est ce que fait un vrai gérant occupé."),
    ], notes="Vingt minutes au module, chacun sur son appareil. Passer voir qui reste "
             "bloqué à la première réplique et lui souffler la phrase du plan.")

    d.regle("On demande, sinon on n'apprend rien",
            "Quel horaire ? Combien de l'heure ? Quelles tâches ?",
            precision="Le gérant répond à ce qu'on lui demande et n'explique rien "
                      "d'avance. Trois questions valent la peine d'être posées avant de "
                      "partir, et une quatrième : quand est-ce que vous rappelez ?",
            notes="Diapo à photographier. Faire lister les quatre questions au tableau "
                  "avant de lancer le jeu de rôle.")

    d.piege("Parler trop longtemps",
            "Une réponse de deux minutes à « vous savez faire quoi ? »",
            "Deux phrases, puis on se tait et on écoute.",
            "La personne en face travaille pendant qu'elle vous parle. Deux phrases "
            "nettes laissent de la place à sa question suivante, et c'est sa question "
            "suivante qui fait avancer la conversation.",
            notes="Chronométrer une prise trop longue et la faire refaire en trente "
                  "secondes : la deuxième version est presque toujours meilleure.")

    d.pratique('Écoute', "Celui qui cherche, ou celui qui engage ?",
               "Écoutez chaque phrase et dites qui la dit.", [
        ("J'ai vu votre affiche dans la vitrine.", "celle qui cherche"),
        ("Vous avez déjà travaillé en boulangerie ?", "celui qui engage"),
        ("J'ai de l'expérience en garde d'enfants.", "celle qui cherche"),
        ("Remplissez ce formulaire.", "celui qui engage"),
        ("Je suis libre du lundi au vendredi, le matin.", "celle qui cherche"),
        ("Je vous rappelle vendredi, avant cinq heures.", "celui qui engage"),
    ], corrige=True, cols=2,
       notes="Même exercice que aQui dans le module. Il sert d'échauffement avant "
             "l'enregistrement : dix minutes, pas plus.")

    d.pratique('Production orale', "Enregistrez-vous",
               "Quarante-cinq secondes. Vous pouvez recommencer autant de fois que vous voulez.", [
        ("Temps 1", "Bonjour. J'ai vu votre affiche. Est-ce que vous engagez encore ?"),
        ("Temps 2", "Je sais faire… J'ai de l'expérience en… Je suis libre…"),
        ("Temps 3", "Je m'appelle… , T-R-A-… Vous pouvez me joindre au… Merci !"),
    ], notes="Trente minutes. Rappeler la marche : je m'enregistre, je m'écoute, je "
             "corrige, j'envoie. L'assistant donne une rétroaction avant l'envoi ; "
             "cette rétroaction reste privée tant que l'élève n'envoie pas.")

    d.billet(
        "À quel commerce irez-vous cette semaine, et quel jour ?",
        exemples=[
            "Le nom, la rue, le jour et l'heure.",
            "Pas entre onze heures et deux heures.",
        ],
        notes="Deux minutes. Reprendre les billets à la prochaine session et demander "
              "qui y est allé. C'est la seule évaluation qui compte vraiment.")

    return d.save(dossier)
