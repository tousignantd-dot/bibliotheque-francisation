# -*- coding: utf-8 -*-
"""C4 · Les étapes de l'achat.
Bloc C « Défi 2 · Demander au guichet » · couleur framboise · 60 min.
Source : exercices `t2ordre` et `t2img`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='framboise',
        titre="Les étapes de l'achat",
        chapeau="Six moments, six phrases. Un achat au comptoir dure deux "
                "minutes et suit toujours le même ordre.",
        duree='60 minutes')

    d.titre(notes="Séance de synthèse du défi 2, courte. Elle rassemble tout ce que les "
                  "trois séances précédentes ont installé et le met dans l'ordre. "
                  "Ouvrir en demandant au groupe de reconstituer l'achat de Rosario de "
                  "mémoire, sans notes.")

    d.objectifs([
        "mettre en ordre les six moments d'un achat ;",
        "dire la phrase qui va avec chaque moment ;",
        "reconnaître les gestes de l'achat : recharger, valider, payer ;",
        "enchaîner les six phrases sans s'arrêter.",
    ])

    d.tableau('Analyse', "Les six moments, dans l'ordre",
              ["Le moment", "Ce qu'on dit"],
              [["1 · on arrive", "Bonjour. Je voudrais un titre mensuel, s'il vous plaît."],
               ["2 · on donne sa carte", "Oui, la voici."],
               ["3 · on se renseigne", "Est-ce qu'elle a droit au tarif réduit ?"]],
              cle=0,
              note="Une chose à la fois, et on attend la réponse.",
              notes="Diapositive à photographier. Premier des deux tableaux : le second "
                    "suit immédiatement. Faire répéter les trois premières phrases avant "
                    "de passer à la suite.")

    d.tableau('Analyse', "Les six moments, la fin",
              ["Le moment", "Ce qu'on dit"],
              [["4 · on n'a pas compris", "Pardon, pouvez-vous répéter, s'il vous plaît ?"],
               ["5 · on paie", "Par carte, s'il vous plaît."],
               ["6 · on vérifie", "Un mensuel, zone A, cent dix dollars. C'est ça ?"]],
              cle=0,
              note="La sixième est celle qu'on oublie, et c'est la plus utile.",
              notes="Diapositive à photographier. Insister sur le moment 4 : il peut "
                    "arriver n'importe quand, plusieurs fois, et il n'a rien "
                    "d'exceptionnel.")

    d.pratique('Association', "Quelle phrase, à quel moment ?",
               "Dites la phrase qui va avec chaque situation.", [
        ("Vous arrivez devant le comptoir.", "Bonjour. Je voudrais un titre mensuel, s'il vous plaît."),
        ("On vous demande si vous avez une carte.", "Oui, la voici."),
        ("Vous pensez à votre fille de quinze ans.", "Est-ce qu'elle a droit au tarif réduit ?"),
        ("Vous n'avez pas bien entendu le prix.", "Pardon, pouvez-vous répéter, s'il vous plaît ?"),
        ("On vous demande comment vous payez.", "Par carte, s'il vous plaît."),
        ("Vous voulez être sûr avant de partir.", "Un mensuel, zone A, cent dix dollars. C'est ça ?"),
    ], corrige=True,
       notes="C'est l'exercice 4 du défi 2. Le faire d'abord de mémoire, puis vérifier "
             "avec l'activité interactive. Terminer par un enchaînement complet, "
             "chronométré : deux minutes suffisent.")

    d.cartes("Les gestes de l'achat", "Quatre verbes à ne pas confondre", [
        ("recharger sa carte",
         "Mettre un nouveau titre sur une carte qu'on possède déjà. C'est ce que fait "
         "la personne au comptoir. On ne rachète pas une carte chaque mois."),
        ("valider son titre",
         "Passer sa carte sur l'appareil en montant, pour que le voyage soit compté. "
         "Un titre non validé ne vaut rien, même s'il est payé."),
        ("payer comptant",
         "Payer avec des billets et de la monnaie, plutôt qu'avec une carte "
         "bancaire. On vous posera la question chaque fois."),
        ("faire faire sa photo",
         "Pour le tarif réduit seulement. Cela se fait au point de service, avec la "
         "personne concernée et une preuve de son âge."),
    ], notes="Les quatre verbes sont dans l'exercice 5 du défi 2, qui les fait "
             "reconnaître en images. « Valider » est celui dont l'oubli coûte une "
             "amende : le répéter.")

    d.piege('Usage',
            "monter sans valider sa carte",
            "valider sa carte en montant",
            "Un titre payé mais non validé ne compte pas. En cas de contrôle, "
            "c'est une amende — et l'argument « j'ai payé » ne sert à rien, "
            "puisque rien ne le prouve. Le geste prend une seconde.",
            notes="Erreur coûteuse et très fréquente chez les nouveaux arrivants, "
                  "surtout dans l'autobus, où le lecteur est moins visible qu'un "
                  "tourniquet. Le dire clairement, sans dramatiser.")

    d.pratique('Production', "Faites l'achat complet",
               "À deux : l'un tient le comptoir, l'autre achète. Puis on échange.", [
        ("Saluer et dire ce qu'on veut.", "Bonjour. Je voudrais…"),
        ("Donner sa carte.", "La voici."),
        ("Poser une question sur le tarif réduit.", "Est-ce que…"),
        ("Faire répéter le prix.", "Pardon, pouvez-vous…"),
        ("Dire comment on paie.", "Par carte / comptant."),
        ("Vérifier avant de partir.", "…C'est ça ?"),
    ], corrige=True,
       notes="Dernière activité du défi 2, et répétition générale du jeu de rôle de la "
             "séance E1. Passer dans les rangées sans interrompre : noter deux ou trois "
             "erreurs communes et les reprendre à la fin, sans nommer personne.")

    d.billet(
        "Écrivez les six phrases de l'achat, dans l'ordre.",
        exemples=[
            "1. Bonjour. Je voudrais ___ .",
            "6. ___ . C'est ça ?",
        ],
        notes="Devoir court. C'est la fiche que l'élève pourra emporter au comptoir. Le "
              "dire au groupe : ce billet-là sert vraiment à quelque chose.")

    return d.save(dossier)
