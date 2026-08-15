# -*- coding: utf-8 -*-
"""D1 · À l'accueil de l'hôpital.
Bloc D · couleur teal (écoute et réponds) · 60 min.
Source : dialogue `t3`, exercices `t3vf` et `t3plan`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D1', section='teal',
        titre="À l'accueil de l'hôpital",
        chapeau="Aminata vient chercher sa sœur. Elle ne connaît ni les règles de "
                "visite, ni le chemin, ni le tarif du stationnement. Quatre questions "
                "suffisent à tout savoir.",
        duree='60 minutes')

    d.titre(notes="Ouverture du défi 3. Demander au groupe : que fait-on quand on arrive "
                  "dans un hôpital qu'on ne connaît pas ? La réponse — on demande à "
                  "l'accueil — n'est pas évidente pour tout le monde.")

    d.objectifs([
        "comprendre les règles d'accompagnement d'un hôpital ;",
        "demander son chemin et comprendre la réponse ;",
        "nommer les services d'un hôpital et dire ce qu'on y fait ;",
        "comprendre une information sur le stationnement.",
    ])

    d.dialogue('Dialogue · 1 de 3', "Je viens chercher ma sœur", [
        ("AMINATA", "Bonjour, je viens chercher ma sœur. Elle est à l'urgence depuis ce "
                    "matin.", True),
        ("LA RÉCEPTIONNISTE", "Pourriez-vous me donner son nom, s'il vous plaît ?", True),
        ("AMINATA", "Fatou Diarra. Est-ce que je pourrais monter la rejoindre ?", True),
        ("LA RÉCEPTIONNISTE", "Un accompagnateur à la fois, et seulement quand le "
                              "personnel vous appelle.", True),
    ], consigne="Écoutez d'abord l'enregistrement, diapo masquée. Lisez ensuite.",
       notes="Passer l'audio du défi 3. Faire remarquer les formes de politesse : "
             "« pourriez-vous », « est-ce que je pourrais ». C'est le sujet de D2.")

    d.dialogue('Dialogue · 2 de 3', "Auriez-vous un endroit où attendre ?", [
        ("AMINATA", "Auriez-vous un endroit où attendre ?", True),
        ("LA RÉCEPTIONNISTE", "La salle d'attente est au fond du corridor, à droite, "
                              "après l'ascenseur.", True),
    ], notes="Faire répéter l'indication de chemin par trois élèves, de mémoire. Trois "
             "repères : au fond, à droite, après l'ascenseur.")

    d.dialogue('Dialogue · 3 de 3', "Et pour le stationnement ?", [
        ("AMINATA", "Et pour le stationnement, est-ce que c'est payant ?", True),
        ("LA RÉCEPTIONNISTE", "Oui, mais gardez votre billet : à l'urgence, les quatre "
                              "premières heures sont gratuites.", True),
    ], notes="Information très concrète et très utile. Beaucoup de gens paient sans "
             "savoir que la gratuité existe. Le dire explicitement.")

    d.tableau('Analyse', "Les quatre questions d'Aminata",
              ['La question', 'Ce qu\'elle obtient'],
              [["Je viens chercher ma sœur.", "on lui demande le nom"],
               ["Est-ce que je pourrais monter ?", "les règles d'accompagnement"],
               ["Auriez-vous un endroit où attendre ?", "le chemin de la salle d'attente"],
               ["Est-ce que c'est payant ?", "les quatre heures gratuites"]],
              cle=0,
              note="Quatre questions posées à la même personne, en deux minutes. C'est "
                   "le rôle de l'accueil : répondre à tout ce qui n'est pas médical.",
              notes="Faire remarquer que la quatrième question — le stationnement — n'a "
                    "rien à voir avec la santé, et pourtant elle a une vraie valeur.")

    d.tableau('Analyse', "Les services d'un hôpital",
              ['Le service', 'On y va pour'],
              [["l'accueil", "s'inscrire et demander son chemin"],
               ["l'urgence", "un problème grave ou soudain"],
               ["la radiologie", "passer une radiographie"],
               ["le laboratoire", "faire une prise de sang"],
               ["la pharmacie", "obtenir les médicaments prescrits"]],
              cle=0,
              note="Ces cinq mots sont écrits sur les panneaux de tous les hôpitaux du "
                   "Québec.",
              notes="Faire lire les mots à voix haute : ils doivent être reconnus vite, "
                    "sur un panneau, en marchant.")

    d.cartes('Analyse', "Comprendre une indication de chemin", [
        ("Les repères de direction",
         "À droite, à gauche, tout droit. Toujours donnés du point de vue de celui qui "
         "marche, pas de celui qui parle."),
        ("Les repères de distance",
         "Au fond, au bout, après, avant. « Au fond du corridor » veut dire jusqu'à "
         "l'extrémité, sans tourner avant."),
        ("Les repères visibles",
         "Après l'ascenseur, en face de la pharmacie, à côté de l'escalier. Ce sont les "
         "plus fiables : on les voit."),
        ("La bonne réaction",
         "Répétez l'indication à voix haute avant de partir : « Au fond, à droite, "
         "après l'ascenseur ? » On vous corrigera tout de suite si vous avez mal "
         "compris."),
    ], notes="La quatrième carte est le geste à installer. Le faire pratiquer : "
             "quelqu'un donne une indication, l'autre la répète.")

    d.pratique('Pratique · 1 de 3', "Vrai ou faux — à l'accueil",
               "Répondez sans relire le dialogue.", [
        ("Aminata vient chercher sa sœur.", "VRAI"),
        ("La réceptionniste demande le nom de la patiente.", "VRAI"),
        ("Deux accompagnateurs peuvent monter en même temps.", "FAUX — un seul à la fois"),
        ("La salle d'attente est au fond du corridor, à droite.", "VRAI"),
        ("Le stationnement est entièrement gratuit.", "FAUX — payant, sauf quatre heures"),
        ("À l'urgence, les quatre premières heures de stationnement sont gratuites.", "VRAI"),
    ], corrige=True,
       notes="Les deux dernières se contredisent en apparence. C'est voulu : il faut "
             "entendre la restriction « à l'urgence » et « les quatre premières ».")

    d.pratique('Pratique · 2 de 3', "Le service et ce qu'on y fait",
               "Reliez chaque service à son usage.", [
        ("l'urgence", "un problème grave ou soudain"),
        ("l'accueil", "s'inscrire et demander son chemin"),
        ("la radiologie", "passer une radiographie"),
        ("le laboratoire", "faire une prise de sang"),
        ("la pharmacie", "obtenir les médicaments prescrits"),
    ], corrige=True, cols=2,
       notes="Exercice rapide. Enchaîner sur le jeu de rôle, qui est le vrai contenu de "
             "la séance.")

    d.piege("Le piège du hochement de tête",
            "Vous hochez la tête sans avoir compris le chemin.",
            "Vous répétez : « Au fond, à droite, après l'ascenseur ? »",
            "Hocher la tête met fin à la conversation, et on se retrouve à errer dans "
            "un corridor. Répéter l'indication prend cinq secondes et permet à la "
            "personne de corriger tout de suite. C'est le geste le plus rentable de "
            "toute la séance.",
            notes="Faire pratiquer trois fois : l'un donne une indication compliquée, "
                  "l'autre la répète. Personne n'a le droit de hocher la tête.")

    d.pratique('Pratique · 3 de 3', "Jeu de rôle · à l'accueil",
               "À deux. L'un est à l'accueil, l'autre cherche quelqu'un. Puis on échange.", [
        ("Vous cherchez", "un membre de votre famille arrivé ce matin à l'urgence"),
        ("Vous demandez", "si vous pouvez monter le rejoindre"),
        ("Vous demandez", "où se trouve la salle d'attente"),
        ("Vous répétez", "l'indication de chemin, pour vérifier"),
    ], corrige=False,
       notes="Quinze minutes. Circuler et vérifier que la quatrième étape est bien "
             "faite : c'est celle que tout le monde saute.")

    d.billet(
        "Écrivez les quatre questions que vous poseriez à l'accueil d'un hôpital.",
        exemples=[
            "Une pour trouver la personne, une sur les règles, une sur le chemin, une "
            "sur le stationnement.",
            "Écrivez-les comme vous les diriez vraiment.",
        ],
        notes="Ces billets préparent D2 : on y reprendra ces mêmes questions pour les "
              "rendre polies.")

    return d.save(dossier)
