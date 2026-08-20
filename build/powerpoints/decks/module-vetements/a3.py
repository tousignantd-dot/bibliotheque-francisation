# -*- coding: utf-8 -*-
"""A3 · Choisir un manteau d'hiver.
Bloc A « Je découvre » · couleur teal · 60 min.
Source : exercices `prChoisir` et `prTaille`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-vetements/images/')


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre="Choisir un manteau d'hiver",
        chapeau="Cinq choses à regarder, et une seule est écrite en gros : le "
                "prix. Les quatre autres décident si vous aurez froid tout "
                "l'hiver.",
        duree='60 minutes')

    d.titre(notes="Si possible, apporter un vrai manteau d'hiver et faire chercher "
                  "l'étiquette de la cote de température. Elle est minuscule, et personne "
                  "ne la trouve du premier coup.")

    d.objectifs([
        "trouver la cote de température sur une étiquette ;",
        "distinguer le duvet de la fibre synthétique ;",
        "savoir quelle longueur choisir, et pourquoi ;",
        "comprendre l'utilité du capuchon bordé.",
    ])

    d.declencheur(
        'Observation', "Pourquoi une fourrure autour du capuchon ?",
        image=IMG + 'capuchon-fourrure.jpg',
        pistes=[
            "Est-ce décoratif, ou utile ?",
            "Qu'est-ce qui gèle en premier, l'hiver ?",
            "Avez-vous déjà eu le visage brûlé par le vent ?",
            "Que font les gens d'ici quand il vente à moins vingt ?",
        ],
        notes="La bordure crée une zone d'air calme devant le visage. Ce n'est pas "
              "décoratif : c'est ce qui empêche les gelures aux joues.")

    d.tableau('Analyse', "Les cinq choses à regarder",
              ['Ce qu\'on regarde', 'Ce qu\'il faut'],
              [["La cote de température", "moins trente pour l'hiver d'ici"],
               ["Le remplissage", "duvet ou fibre, selon l'usage"],
               ["La longueur", "aux genoux pour attendre dehors"],
               ["Le capuchon", "avec une bordure coupe-vent"],
               ["La taille", "une de plus, pour un chandail dessous"]],
              cle=0,
              note="Une seule est écrite en gros dans le magasin : le prix.",
              notes="Diapo à photographier. Faire recopier : c'est la liste à emporter au "
                    "magasin.")

    d.regle("La cote de température",
            "Elle est écrite en petit, sur une étiquette cousue.",
            precision="« Moins vingt », « moins trente », « moins quarante ». C'est la "
                      "température jusqu'à laquelle le manteau protège une personne qui "
                      "marche. Debout à un arrêt d'autobus, comptez dix degrés de moins.",
            notes="Cette dernière précision est importante et rarement dite : la cote "
                  "suppose qu'on bouge.")

    d.cartes('Duvet ou fibre ?', "Chacun ses forces", [
        ("Le duvet",
         "Plus chaud et beaucoup plus léger, à volume égal. Mais il perd presque tout son "
         "pouvoir isolant s'il est mouillé, et il sèche lentement."),
        ("La fibre synthétique",
         "Moins chaude à volume égal, plus lourde — mais elle isole même humide et sèche "
         "vite. Elle coûte moins cher."),
        ("Comment choisir",
         "Grand froid sec : duvet. Pluie verglaçante, neige mouillée, travail dehors : "
         "fibre. Beaucoup de manteaux mélangent les deux."),
    ], notes="Pas de bonne réponse universelle. Le critère est l'usage, pas le prix.")

    d.regle("La longueur",
            "Aux genoux pour attendre dehors.",
            precision="Un manteau court laisse les cuisses au froid, et c'est là qu'on "
                      "perd le plus de chaleur en restant immobile. Pour marcher vite, un "
                      "manteau plus court suffit ; pour attendre l'autobus quinze minutes, "
                      "non.",
            notes="Le lien avec le transport en commun est concret : beaucoup d'élèves "
                  "attendent dehors chaque jour.")

    d.piege("Choisir d'après l'apparence seulement",
            "Il est beau et il n'est pas cher.",
            "Il est coté moins dix. En janvier, tu auras froid.",
            "Un manteau qui plaît mais qui ne protège pas finit au fond du placard dès le "
            "premier grand froid — et il faut en racheter un. La cote de température coûte "
            "quelques dollars de plus et se paie en un hiver.",
            notes="Ne pas opposer beauté et chaleur : les deux existent. Il s'agit de "
                  "vérifier la cote avant de tomber amoureux du modèle.")

    d.pratique('Pratique · 1 de 2', "Quel manteau pour qui ?",
               "Choisissez la caractéristique qui compte le plus.", [
        ("Attendre l'autobus vingt minutes chaque matin", "aux genoux, coté moins trente"),
        ("Marcher dix minutes jusqu'au métro", "plus court, coté moins vingt suffit"),
        ("Travailler dehors sous la neige mouillée", "fibre synthétique, imperméable"),
        ("Voyager souvent, peu de place dans la valise", "duvet, plus léger et compressible"),
    ], corrige=True, cols=1,
       notes="Faire justifier chaque réponse. L'usage décide, pas le prix.")

    d.pratique('Pratique · 2 de 2', "Le mot juste pour chaque chose",
               "Quelle mesure emploie-t-on ?", [
        ("Un manteau, un chandail", "la taille : petit, moyen, grand"),
        ("Des bottes, des souliers", "la pointure : un chiffre"),
        ("Des gants", "petit, moyen, grand — parfois taille unique"),
        ("Un manteau d'hiver, en plus", "la cote de température"),
    ], corrige=True, cols=1,
       notes="La distinction taille / pointure revient. C'est une des erreurs les plus "
             "fréquentes et les plus faciles à corriger.")

    d.billet(
        "Trouvez la cote de température d'un manteau, chez vous ou en magasin.",
        exemples=[
            "Cherchez l'étiquette cousue, souvent dans une couture de côté.",
            "Notez aussi le remplissage : duvet ou fibre ?",
        ],
        notes="Devoir concret. Plusieurs découvrent que leur manteau n'est pas assez chaud "
              "— et c'est une information utile.")

    return d.save(dossier)
