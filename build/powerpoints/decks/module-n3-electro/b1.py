# -*- coding: utf-8 -*-
"""B1 · Le spécial finit dimanche.
Bloc B « Défi 1 · Lire la circulaire » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t1vf`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-electro/images/')


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre='Le spécial finit dimanche',
        chapeau="La circulaire dit tout : le prix, le prix des autres "
                "semaines, le modèle et les dates. Encore faut-il savoir où "
                "regarder — et le programme en fait la seule intention de "
                "cette situation.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 1. Si des élèves ont rapporté une circulaire "
                  "(devoir de A2), la distribuer maintenant : la séance se fait bien "
                  "mieux avec du vrai papier dans les mains.")

    d.objectifs([
        "trouver le prix d'aujourd'hui dans un encadré de circulaire ;",
        "distinguer le prix régulier du prix en spécial ;",
        "relever le modèle et la marque d'un appareil ;",
        "comprendre les dates de début et de fin d'un spécial.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qui est écrit le plus gros ?",
        image=IMG + 'circulaire-table.jpg',
        pistes=[
            "Combien de chiffres voyez-vous autour d'un appareil ?",
            "Lequel est le prix ? Comment le savez-vous ?",
            "À quoi sert le chiffre barré ?",
            "Qu'est-ce qui est écrit tout en bas, en petit ?",
        ],
        notes="Faire chercher sans expliquer d'abord. La taille des caractères est un "
              "indice que tout le monde sait lire, même sans connaître les mots : c'est "
              "la stratégie de lecture qu'on veut installer.")

    d.dialogue('Dialogue · 1 de 3', "Le gros chiffre et le petit", [
        ("MARISOL", "Il y a beaucoup de chiffres. Je ne sais pas lequel est le prix.", True),
        ("LOUISE", "Le gros chiffre en bas de la photo, c'est le prix d'aujourd'hui. Huit cent quarante-neuf dollars.", True),
        ("MARISOL", "Et le petit chiffre barré au-dessus ?", True),
        ("LOUISE", "C'est le prix régulier. Mille quarante-neuf dollars. Le magasin enlève deux cents dollars.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Deux chiffres, deux fonctions. Faire redire par un élève, avec ses mots, "
             "avant de passer à la suite.")

    d.dialogue('Dialogue · 2 de 3', "Du mardi au dimanche", [
        ("MARISOL", "Alors c'est un spécial.", True),
        ("LOUISE", "Oui. Et regarde en bas de la page : du mardi 4 au dimanche 9 novembre.", True),
        ("MARISOL", "Ça veut dire que lundi, c'est fini ?", True),
        ("LOUISE", "Lundi, c'est fini. Le prix remonte à mille quarante-neuf.", True),
    ], notes="Marisol vérifie sa compréhension en reformulant : « Ça veut dire que… » "
             "C'est la stratégie à souligner, plus encore que la réponse.")

    d.dialogue('Dialogue · 3 de 3', "Note le modèle", [
        ("LOUISE", "Il faut y aller cette semaine. Et note le modèle : LT 4200.", True),
        ("MARISOL", "LT 4200. Marque Norlac. Je l'écris sur mon papier.", True),
        ("LOUISE", "Parfait. Avec le modèle et la circulaire, le vendeur trouve tout de suite.", True),
    ], notes="Le geste à retenir : écrire le modèle sur un papier avant de partir. Il "
             "évite dix minutes d'explications au magasin.")

    d.tableau('Analyse', "Les quatre chiffres d'un encadré",
              ['Ce qu\'on voit', 'Ce que ça veut dire'],
              [["le gros chiffre", "le prix de cette semaine"],
               ["le petit chiffre barré", "le prix régulier, celui des autres semaines"],
               ["des lettres et des chiffres", "le modèle de l'appareil"],
               ["deux dates, en bas", "le début et la fin du spécial"]],
              cle=1,
              note="Un encadré de circulaire ne se lit pas en entier : on y cherche "
                   "une chose à la fois.",
              notes="Diapo à photographier. C'est le tableau central du défi 1 : y "
                    "revenir en B3 et en B4.")

    d.regle("Vérifier qu'on a compris, en reformulant",
            "« Ça veut dire que lundi, c'est fini ? »",
            precision="Redire avec ses mots ce qu'on croit avoir compris, et "
                      "attendre le oui ou le non. Ça prend cinq secondes et ça "
                      "évite de se déplacer pour rien.",
            notes="Diapo à photographier. Faire pratiquer avec trois phrases dites par "
                  "l'enseignante : les élèves reformulent chaque fois.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Le gros chiffre est le prix d'aujourd'hui.", "vrai"),
        ("Le petit chiffre barré est le prix régulier.", "vrai"),
        ("Le spécial finit le mardi 4 novembre.", "faux — le dimanche 9"),
        ("Lundi, le prix va baisser encore.", "faux — il remonte à 1 049 $"),
        ("LT 4200 est le modèle de la laveuse.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Les deux « faux » "
             "portent sur les dates : c'est la matière de B4.")

    d.billet(
        "Apportez une circulaire et entourez un spécial.",
        exemples=[
            "Écrivez le prix d'aujourd'hui et le prix régulier.",
            "Écrivez la date de fin.",
        ],
        notes="Devoir concret. Les circulaires rapportées serviront en B3 et en B4 : "
              "demander à ceux qui n'en reçoivent pas d'en prendre une à l'entrée d'un "
              "magasin.")

    return d.save(dossier)
