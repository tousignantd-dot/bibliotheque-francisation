# -*- coding: utf-8 -*-
"""C1 · Le formulaire ne se remplit pas tout seul.
Bloc C « Défi 2 · La demande » · couleur acier · 75 min.
Source : dialogue `t2`, exercices `t2vf` et `t2taches`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n6-recherche/images/')


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Le formulaire ne se remplit pas tout seul",
        chapeau="Les deux premières pages sont faciles. C'est la troisième "
                "qui décide : « Décrivez vos fonctions dans votre dernier "
                "emploi. » Là, une phrase vraie peut être totalement inutile.",
        duree='75 minutes')

    d.titre(notes="Première séance du Défi 2. Projeter un formulaire réel de demande "
                  "d'emploi si possible ; sinon, celui de Boisverte suffit.")

    d.objectifs([
        "nommer les rubriques d'une demande d'emploi détaillée ;",
        "distinguer une description vide d'une description utile ;",
        "employer des verbes d'action et des chiffres ;",
        "remplir les rubriques de renseignements sans erreur.",
    ])

    d.declencheur(
        'Observation', "« J'ai travaillé dans un entrepôt. »",
        image=IMG + 'formulaire-papier.jpg',
        pistes=[
            "Cette phrase est-elle vraie ?",
            "Qu'est-ce que l'employeur en apprend ?",
            "Que faisiez-vous, exactement ?",
            "Combien, combien de temps, avec combien de personnes ?",
        ],
        notes="Laisser le groupe compléter la phrase à l'oral. Il produit spontanément "
              "des verbes d'action : c'est sur cette production que la séance s'appuie.")

    d.dialogue('Dialogue · 1 de 2', "Vraie et inutile", [
        ("MARISOL", "Oui, ça, c'est fait. C'est la page trois qui me bloque. « Décrivez vos fonctions dans votre dernier emploi. »", True),
        ("DJAMILA", "Et vous avez écrit quoi ?", True),
        ("MARISOL", "« J'ai travaillé dans un entrepôt. » C'est vrai, mais c'est court.", True),
        ("DJAMILA", "C'est vrai et c'est inutile. Ils ne peuvent rien en faire. Il faut des verbes d'action et des chiffres.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="« C'est vrai et c'est inutile » : la formule est dure et c'est voulu. "
             "Elle résume la séance.")

    d.dialogue('Dialogue · 2 de 2', "Des chiffres", [
        ("MARISOL", "Des chiffres ?", True),
        ("DJAMILA", "Combien de personnes, combien de produits, à quelle fréquence. « J'ai tenu l'inventaire de huit cents références » — ça, un employeur le comprend tout de suite.", True),
        ("MARISOL", "Après avoir fait l'inventaire, je préparais aussi les bons de livraison. Je peux l'écrire comme ça ?", True),
        ("DJAMILA", "Exactement comme ça. C'est précis et c'est du bon français.", True),
    ], notes="La phrase de Marisol contient déjà l'infinitif passé. Ne pas l'expliquer "
             "ici : la séance C2 lui est consacrée. Se contenter de la faire remarquer.")

    d.tableau('Rubriques', "Ce que demande une demande détaillée",
              ['La rubrique', 'Ce qu\'on y écrit'],
              [["Renseignements", "Nom, adresse, téléphone, courriel — en lettres détachées."],
               ["Formation", "Diplôme, établissement, année. Un diplôme étranger porte le nom du pays."],
               ["Expérience", "Employeur, titre du poste, dates, puis la description des tâches."],
               ["Disponibilités et références", "Jours et heures ; deux personnes qui parleront de votre travail."]],
              cle=0,
              note="La rubrique « Expérience » est celle qui décide. Les autres ne font qu'identifier.",
              notes="Diapositive à photographier. Insister sur le courriel en lettres "
                    "détachées : une lettre mal lue, et la réponse n'arrive jamais.")

    d.pratique('Comparaison', "La phrase vide, et celle qui compte",
               "Que faudrait-il ajouter à la phrase de gauche ?", [
        ("« J'ai travaillé dans un entrepôt. »",
         "« J'ai tenu l'inventaire de 800 références dans un entrepôt de 40 employés. »"),
        ("« Je m'occupais des commandes. »",
         "« Je préparais une trentaine de commandes par jour. »"),
        ("« J'avais des responsabilités. »",
         "« Je supervisais trois personnes et j'organisais leur horaire. »"),
        ("« Je connais l'informatique. »",
         "« J'ai utilisé un logiciel d'inventaire pendant six ans, tous les jours. »"),
    ], corrige=True,
       notes="Faire nommer ce qui a été ajouté chaque fois : un verbe précis, un "
             "chiffre, un contexte. Trois ingrédients, toujours les mêmes.")

    d.regle("Trois ingrédients",
            "Un verbe d'action, un chiffre, un contexte.",
            precision="« Je tenais » plutôt que « je travaillais ». « 800 références » "
                      "plutôt que « beaucoup ». « Dans un entrepôt de 40 employés » "
                      "plutôt que rien. Les trois tiennent en une phrase, et cette "
                      "phrase-là se lit en quatre secondes par quelqu'un qui en lit "
                      "quarante.",
            notes="Diapositive à photographier. C'est la règle du bloc C entier, et "
                  "elle sert aussi à l'oral, en entrevue.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Le formulaire de Boisverte fait quatre pages.", "vrai"),
        ("« J'ai travaillé dans un entrepôt » est une bonne description.", "faux — vraie mais inutile"),
        ("Djamila conseille d'ajouter des chiffres.", "vrai"),
        ("La lettre de motivation devrait faire une page pleine.", "faux — trois paragraphes"),
        ("On relit à voix haute avant d'envoyer.", "vrai"),
    ], corrige=True,
       notes="Le quatrième item annonce la séance C4.")

    d.billet(
        "Réécrivez en une phrase ce que vous faisiez dans votre dernier emploi.",
        exemples=[
            "Un verbe d'action, un chiffre, un contexte.",
            "Comparez avec ce que vous auriez écrit avant la séance.",
        ],
        notes="Ramasser ces phrases : elles serviront de matière aux séances C2 et C3, "
              "et à la production écrite de E1.")

    return d.save(dossier)
