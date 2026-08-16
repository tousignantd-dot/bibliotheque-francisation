# -*- coding: utf-8 -*-
"""B1 · Lina apporte son ordonnance.
Bloc B « Défi 1 · À la pharmacie » · couleur acier (compréhension orale) · 75 min.
Source du module : dialogue `t1`, exercice `co1`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre='Lina apporte son ordonnance',
        chapeau="Le médecin a prescrit des antibiotiques. Au comptoir, le pharmacien "
                "explique comment les prendre — et il pose une question que beaucoup "
                "n'attendent pas.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 1. Rappeler où on en est : Lina a eu son rendez-vous "
                  "jeudi (bloc A), elle sort de chez le médecin avec un papier.")

    d.objectifs([
        "comprendre un échange au comptoir de la pharmacie ;",
        "repérer les quatre consignes d'un traitement ;",
        "répondre à « avez-vous déjà pris ce médicament ? » ;",
        "savoir qu'on peut poser des questions au pharmacien.",
    ])

    d.declencheur(
        'Mise en situation', "Le pharmacien vous demande si vous avez déjà pris ce médicament. Pourquoi ?",
        pistes=[
            "Qu'est-ce qu'il cherche à savoir, exactement ?",
            "Que se passe-t-il si on répond « je ne sais pas » ?",
            "Est-ce qu'il faut parler de ses allergies ?",
            "Et des autres médicaments qu'on prend déjà ?",
        ],
        notes="Cinq minutes. La bonne réponse : il vérifie les allergies et les "
              "interactions. Dire qu'on ne sait pas est une réponse acceptable — le "
              "pharmacien a le dossier.")

    d.dialogue('Dialogue · 1 de 2', "Est-ce que je peux vous aider ?", [
        ("LE PHARMACIEN", "Bonjour, est-ce que je peux vous aider ?", False),
        ("LINA", "Oui, j'ai une ordonnance du médecin pour des antibiotiques.", True),
        ("LE PHARMACIEN", "D'accord. Est-ce que vous avez déjà pris ce médicament "
                          "avant ?", True),
        ("LINA", "Non, c'est la première fois. Comment est-ce que je dois le prendre ?",
         True),
    ], consigne="Écoutez une première fois sans lire.",
       notes="La question de Lina, à la fin, est celle qu'il faut oser poser. Le faire "
             "remarquer : c'est gratuit, et c'est le travail du pharmacien.")

    d.dialogue('Dialogue · 2 de 2', "Un comprimé, deux fois par jour", [
        ("LE PHARMACIEN", "Prenez un comprimé deux fois par jour, matin et soir, pendant "
                          "sept jours.", True),
        ("LINA", "Est-ce que je peux le prendre avec de la nourriture ?", True),
        ("LE PHARMACIEN", "Oui, c'est même recommandé. Ne buvez pas d'alcool pendant le "
                          "traitement.", True),
        ("LINA", "Merci beaucoup pour vos conseils !", False),
    ], notes="Quatre consignes dans deux répliques : combien, quand, combien de temps, "
             "et une interdiction. Les faire compter avant de les nommer.")

    d.regle('La règle de la posologie',
            "Combien · quand · pendant combien de temps.",
            precision="Trois informations sur chaque étiquette, dans cet ordre. S'il en "
                      "manque une, on la demande avant de sortir de la pharmacie.",
            notes="La diapositive à photographier. Elle structure toute la séance B3.")

    d.pratique('Pratique · 1 de 3', "Vrai ou faux",
               "D'après le dialogue.", [
        ("Lina a une ordonnance du médecin.", "vrai"),
        ("Lina a déjà pris ce médicament avant.", "faux — c'est la première fois"),
        ("Elle doit prendre un comprimé deux fois par jour.", "vrai"),
        ("Elle doit prendre le médicament pendant sept jours.", "vrai"),
        ("Elle peut boire de l'alcool pendant le traitement.", "faux — pas d'alcool"),
        ("Elle peut prendre le médicament avec de la nourriture.",
         "vrai — c'est même recommandé"),
    ], corrige=True,
       notes="C'est l'exercice 1 du défi 1. Faire corriger les fausses en citant la "
             "réplique du pharmacien.")

    d.pratique('Pratique · 2 de 3', "Les quatre consignes",
               "Relevez-les dans le dialogue.", [
        ("Combien à la fois ?", "un comprimé"),
        ("Combien de fois par jour ?", "deux fois — matin et soir"),
        ("Pendant combien de temps ?", "sept jours"),
        ("Qu'est-ce qui est interdit ?", "l'alcool, pendant tout le traitement"),
    ], corrige=True,
       notes="Écrire les quatre réponses au tableau et les laisser : elles servent de "
             "modèle à la pratique 3.")

    d.pratique('Pratique · 3 de 3', "Vous êtes Lina",
               "À deux. L'un est le pharmacien, l'autre le client.", [
        ("Le pharmacien demande", "« Est-ce que je peux vous aider ? »"),
        ("Vous présentez votre papier", "« J'ai une ordonnance pour… »"),
        ("Il vérifie", "« Est-ce que vous avez déjà pris ce médicament ? »"),
        ("Vous posez votre question", "« Comment est-ce que je dois le prendre ? »"),
        ("Vous vérifiez la nourriture", "« Est-ce que je peux le prendre en mangeant ? »"),
    ], corrige=False,
       notes="Quinze minutes, puis on échange. Circuler et vérifier une chose : est-ce "
             "que le client POSE une question ? C'est le critère de la séance.")

    d.billet(
        "Écrivez la question que vous poseriez au pharmacien, pour un vrai médicament.",
        exemples=[
            "Une question sur la façon de le prendre, ou sur ce qu'il ne faut pas faire.",
            "Ce peut être un médicament que vous prenez déjà.",
        ],
        notes="Ramasser. Les questions du groupe alimentent B4, où on apprend à faire "
              "répéter quand la réponse n'a pas été comprise.")

    return d.save(dossier)
