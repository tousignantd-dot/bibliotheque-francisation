# -*- coding: utf-8 -*-
"""A1 · Lina appelle la clinique — mise en situation.
Bloc A « Je découvre » · couleur teal · 75 min.
Source du module : dialogue `prep`, exercice `pr2`, cartes mémoire.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A1', section='teal',
        titre='Lina appelle la clinique',
        chapeau="Lina se sent fatiguée depuis deux semaines et a souvent mal à la tête. "
                "Elle veut voir un médecin. Tout commence par un appel de deux minutes.",
        duree='75 minutes')

    d.titre(notes="Ouverture du module 3. Écrire au tableau les trois choses qu'on donne "
                  "toujours au téléphone : QUI · POURQUOI · QUAND. C'est le plan du "
                  "module entier, et celui de l'appel que chacun fera en E1.")

    d.objectifs([
        "comprendre un appel pour obtenir un rendez-vous ;",
        "dire qui on est et pourquoi on appelle ;",
        "décrire simplement comment on se sent ;",
        "savoir ce qu'il faut apporter à un rendez-vous.",
    ])

    d.declencheur(
        'Mise en situation', "Vous êtes fatigué depuis deux semaines. Qu'est-ce que vous faites ?",
        pistes=[
            "Est-ce qu'on attend que ça passe ? Combien de temps ?",
            "Qui appelle-t-on en premier, au Québec ?",
            "Faut-il un rendez-vous pour voir un médecin ?",
            "Qu'est-ce qu'on dit quand la réceptionniste répond ?",
        ],
        notes="Cinq minutes en grand groupe. Ne pas corriger tout de suite : la deuxième "
              "question est le sujet de A2, on y revient. Noter au tableau les réponses "
              "du groupe pour les comparer à la fin de A2.")

    d.cartes('La situation', "Ce qu'on sait de Lina", [
        ("Depuis quand",
         "Deux semaines de fatigue, et souvent mal à la tête. Ce n'est pas une urgence, "
         "mais ça dure."),
        ("Ce qu'elle décide",
         "Appeler la Clinique Notre-Dame, où elle est déjà allée l'année dernière."),
        ("Ce qu'on lui demande",
         "Son nom, si elle est déjà venue, et la raison de sa visite. Trois questions, "
         "toujours les mêmes."),
        ("Ce qu'on lui rappelle",
         "D'apporter sa carte d'assurance maladie. Sans elle, la visite peut être "
         "facturée."),
    ], notes="La quatrième carte est la plus utile pour un nouvel arrivant : la carte "
             "d'assurance maladie s'apporte à CHAQUE visite, pas seulement la première.")

    d.dialogue('Dialogue · 1 de 2', "Clinique Notre-Dame, bonjour", [
        ("LA RÉCEPTIONNISTE", "Clinique Notre-Dame, bonjour.", False),
        ("LINA", "Bonjour, je voudrais prendre un rendez-vous avec un médecin, s'il vous "
                 "plaît.", True),
        ("LA RÉCEPTIONNISTE", "Bien sûr. Est-ce que vous êtes déjà venue à notre "
                              "clinique ?", True),
        ("LINA", "Oui, l'année dernière. Je m'appelle Lina Ferreira.", False),
        ("LA RÉCEPTIONNISTE", "Parfait. Quelle est la raison de votre visite ?", True),
    ], consigne="Écoutez une première fois sans lire.",
       notes="Faire écouter deux fois : la première sans le texte, la deuxième avec. "
             "Les trois répliques en évidence sont les trois questions rituelles.")

    d.dialogue('Dialogue · 2 de 2', "Jeudi à onze heures", [
        ("LINA", "Je me sens fatiguée depuis deux semaines et j'ai souvent mal à la "
                 "tête.", True),
        ("LA RÉCEPTIONNISTE", "Je comprends. Le docteur Tremblay est libre jeudi à onze "
                              "heures. Est-ce que ça vous convient ?", True),
        ("LINA", "Oui, c'est parfait. Merci beaucoup !", False),
        ("LA RÉCEPTIONNISTE", "N'oubliez pas votre carte d'assurance maladie. À jeudi !",
         True),
    ], notes="Faire remarquer que Lina ne raconte pas sa vie : deux symptômes, une "
             "durée. C'est exactement ce qu'il faut, et c'est ce qu'on travaille en A4.")

    d.regle('La règle de l\'appel',
            "Qui je suis · pourquoi j'appelle · quand je peux venir.",
            precision="Trois informations, dans cet ordre. La réceptionniste n'a pas "
                      "besoin d'autre chose, et l'appel dure deux minutes.",
            notes="La diapositive à photographier. Elle revient en A4, en B5 et en E1 — "
                  "c'est la colonne vertébrale du module.")

    d.pratique('Pratique · 1 de 2', "Vrai ou faux",
               "D'après le dialogue.", [
        ("Lina appelle pour prendre un rendez-vous.", "vrai"),
        ("C'est la première fois qu'elle vient à cette clinique.",
         "faux — elle est venue l'année dernière"),
        ("Elle se sent fatiguée depuis deux semaines.", "vrai"),
        ("Elle a souvent mal au dos.", "faux — elle a mal à la tête"),
        ("Le rendez-vous est jeudi à onze heures.", "vrai"),
        ("La réceptionniste lui rappelle d'apporter sa carte d'assurance maladie.",
         "vrai"),
    ], corrige=True,
       notes="Les deux fausses se corrigent en disant la bonne information, pas "
             "seulement « faux ». C'est la consigne à donner avant de commencer.")

    d.pratique('Pratique · 2 de 2', "Qu'est-ce qu'elle répond ?",
               "Vous êtes Lina. Répondez à la réceptionniste.", [
        ("« Clinique Notre-Dame, bonjour. »",
         "Bonjour, je voudrais prendre un rendez-vous, s'il vous plaît."),
        ("« Est-ce que vous êtes déjà venue chez nous ? »",
         "Oui, l'année dernière. / Non, c'est la première fois."),
        ("« Quelle est la raison de votre visite ? »",
         "Je me sens fatiguée depuis deux semaines."),
        ("« Jeudi à onze heures, ça vous convient ? »",
         "Oui, c'est parfait, merci. / Non, est-ce que vous avez autre chose ?"),
    ], corrige=True,
       notes="À deux, debout, sans regarder le texte. Deux minutes par tour, puis on "
             "échange les rôles. La quatrième réponse compte double : savoir dire NON "
             "poliment à une heure qui ne convient pas.")

    d.billet(
        "Écrivez les deux phrases que vous diriez pour prendre un rendez-vous.",
        exemples=[
            "Qui vous êtes, et pourquoi vous appelez.",
            "Utilisez votre vrai nom et une vraie raison.",
        ],
        notes="Ramasser. Ces deux phrases servent de point de départ en A4, puis dans "
              "l'appel enregistré de E1.")

    return d.save(dossier)
