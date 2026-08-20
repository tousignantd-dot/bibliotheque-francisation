# -*- coding: utf-8 -*-
"""A3 · Les mots de la rue.
Bloc A « Je découvre » · couleur teal · 60 min.
Source : exercices `prVocab`, `prImg`, `prLieu` ; banc de vocabulaire.

Séance de vocabulaire. Les huit mots du banc se voient tous depuis un
trottoir : c'est le critère qui les a choisis. Un élève de niveau 2 les
associe à une image, pas à une définition.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-autobus/images/')


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre="Les mots de la rue",
        chapeau="Huit mots qui se voient depuis un trottoir. Les connaître, "
                "c'est pouvoir comprendre une réponse et en donner une.",
        duree='60 minutes')

    d.titre(notes="Séance de vocabulaire. Si le temps et le quartier le permettent, la "
                  "faire dehors : vingt minutes sur le trottoir devant le centre valent "
                  "une heure de diapositives.")

    d.objectifs([
        "nommer ce qu'on voit dans une rue ;",
        "nommer les lieux du quartier ;",
        "associer un mot à une image ;",
        "employer les mots dans une phrase.",
    ])

    d.declencheur(
        'Observation', "Nommez tout ce que vous voyez.",
        image=IMG + 'arret-autobus.jpg',
        pistes=[
            "Qu'est-ce que c'est ?",
            "À quoi ça sert ?",
            "Qu'est-ce qu'il y a autour ?",
            "Y en a-t-il un près de chez vous ?",
        ],
        notes="Laisser nommer dans la langue qu'on peut, puis donner le mot français. "
              "Écrire au tableau au fur et à mesure.")

    d.vocabulaire('Vocabulaire', "Ce qu'on voit dans la rue", [
        ("un arrêt", "L'endroit où l'autobus s'arrête pour prendre les passagers."),
        ("un coin", "L'endroit où deux rues se rencontrent."),
        ("un feu", "Le feu de circulation : rouge, jaune, vert."),
        ("un trottoir", "Le côté de la rue où on marche."),
    ], notes="Diapositive à photographier. Faire répéter chaque mot avec son article : "
             "l'article s'apprend avec le mot, jamais après.")

    d.vocabulaire('Vocabulaire', "Ce qu'on lit dans la rue", [
        ("un plan", "Le dessin d'une ville ou d'un quartier, vu d'en haut."),
        ("un horaire", "Le papier ou l'écran qui dit les heures de passage."),
        ("un avis", "Le petit papier affiché qui annonce quelque chose."),
        ("une correspondance", "Le papier qui permet de prendre un deuxième autobus "
                               "sans payer."),
    ], notes="Diapositive à photographier. « Correspondance » est le mot le plus long et "
             "le plus utile : il revient dans tout le bloc C.")

    d.tableau('Analyse', "Les lieux du quartier",
              ['Le lieu', 'On dit'],
              [["la bibliothèque", "je vais à la bibliothèque"],
               ["le parc", "je vais au parc"],
               ["l'école", "je vais à l'école"],
               ["l'hôpital", "je vais à l'hôpital"]],
              cle=2,
              note="Le genre s'apprend avec le mot. Ne pas essayer de le deviner : il n'y "
                   "a pas de règle sûre.",
              notes="Rappel de la mini-leçon de A1. Trois minutes suffisent : c'est un "
                    "rappel, pas une reprise.")

    d.pratique('Association', "Quel mot pour quelle image ?",
               "Dites le mot qui va avec chaque photo.", [
        ("On attend l'autobus ici.", "un arrêt"),
        ("Rouge, jaune, vert.", "un feu"),
        ("Le quartier vu d'en haut.", "un plan"),
        ("Ici, deux rues se rencontrent.", "un coin"),
    ], corrige=True, cols=1,
       notes="Le même exercice existe dans le module en ligne, en glisser-déposer. Le "
             "faire ici à l'oral d'abord : il ira plus vite ensuite à l'écran.")

    d.pratique('Pratique · à deux', "Mon quartier",
               "Deux par deux, avec le plan du quartier si vous en avez un.", [
        ("Étape 1", "Nommez trois lieux près de chez vous."),
        ("Étape 2", "Dites où ils sont : au coin, près du parc, sur la rue…"),
        ("Étape 3", "Votre voisin répète ce que vous avez dit."),
        ("Étape 4", "Échangez les rôles."),
    ], cols=1,
       notes="Vingt minutes. Un plan papier du quartier, imprimé, change tout : les élèves "
             "montrent du doigt et parlent davantage.")

    d.billet(
        "Écrivez quatre mots de la rue, avec leur article.",
        exemples=[
            "un arrêt · le trottoir · un feu · le coin",
            "Puis faites une phrase avec deux d'entre eux.",
        ],
        notes="Devoir court. L'article compte autant que le mot : le corriger sans "
              "commenter.")

    return d.save(dossier)
