# -*- coding: utf-8 -*-
"""C2 · Faire répéter.
Bloc C « Défi 2 » · couleur ambre · 60 min.
Source : mini-leçon `t2poli`, exercice `t2poli`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre='Faire répéter',
        chapeau="La phrase qu'on ose le moins dire est celle qui sert le "
                "plus. Trois façons de la dire, et une qui marche mieux que "
                "les autres.",
        duree='60 minutes')

    d.titre(notes="Séance courte et très pratique. Elle clôt le bloc C et prépare la "
                  "production orale.")

    d.objectifs([
        "dire qu'on n'a pas compris ;",
        "demander de parler plus lentement ;",
        "vérifier ce qu'on a compris ;",
        "employer les six phrases de politesse du module.",
    ])

    d.declencheur(
        'Écoute', "Laquelle de ces phrases marche le mieux ?",
        pistes=[
            "« Pardon ? »",
            "« Vous pouvez répéter ? »",
            "« Plus lentement, s'il vous plaît. »",
            "Pourquoi la troisième ?",
        ],
        notes="Les deux premières font redire la même phrase à la même vitesse. La "
              "troisième change quelque chose.")

    d.tableau('Analyse', "Trois façons de faire répéter",
              ['La phrase', "Ce qu'elle obtient"],
              [["Pardon ?", "la même phrase, même vitesse"],
               ["Vous pouvez répéter ?", "la même phrase, même vitesse"],
               ["Plus lentement, s'il vous plaît.", "la même phrase, plus lentement"]],
              cle=2,
              note="Ce n'est pas le volume qui manque : c'est la vitesse.",
              notes="Diapo à photographier. C'est la découverte de la séance, et elle "
                    "change vraiment les échanges du quotidien.")

    d.regle("Vérifier ce qu'on a compris",
            "Répéter ce qu'on a entendu.",
            precision="« Salle <b>douze</b> ? » « Mardi, c'est bien ça ? » En répétant "
                      "l'information, on donne à la personne l'occasion de corriger — et "
                      "on n'a plus besoin de deviner.",
            notes="Diapo à photographier. Faire pratiquer avec des chiffres : c'est là que "
                  "l'erreur coûte le plus cher.")

    d.cartes("Les six phrases du module", "À savoir par cœur", [
        ("Bonjour · Bonsoir",
         "En arrivant. Le jour, le soir."),
        ("Merci · De rien",
         "On remercie souvent, ici. « Bienvenue » veut dire « de rien »."),
        ("Pardon",
         "Pour s'excuser, et pour faire répéter."),
        ("Je ne comprends pas · Plus lentement, s'il vous plaît",
         "Les deux plus utiles de toutes. Elles ne sont pas un aveu d'échec."),
    ], notes="Diapo à photographier. C'est la liste de révision du défi 2.")

    d.piege("S'excuser trop",
            "Je suis désolé, excusez-moi, pardon, je ne parle pas bien…",
            "Pardon, plus lentement, s'il vous plaît.",
            "Un seul mot suffit. S'excuser longuement de ne pas parler la langue prend "
            "plus de temps que la question elle-même — et personne ne l'attend.",
            notes="Beaucoup d'élèves s'excusent d'exister. Le dire avec bienveillance, mais "
                  "le dire.")

    d.pratique('Pratique · 1 de 2', "Que dites-vous ?",
               "Une phrase par situation.", [
        ("Vous entrez dans un magasin, le matin.", "Bonjour."),
        ("Quelqu'un vous aide.", "Merci beaucoup."),
        ("On vous dit merci.", "De rien."),
        ("Vous n'avez pas compris.", "Pardon ? Je ne comprends pas."),
        ("On parle trop vite.", "Plus lentement, s'il vous plaît."),
    ], corrige=True, cols=1,
       notes="Utiliser l'exercice 2 du module, qui accepte plusieurs formulations.")

    d.pratique('Pratique · 2 de 2', "À deux · la conversation complète",
               "L'un parle vite, l'autre fait répéter.", [
        ("Étape 1", "l'un dit une phrase avec un chiffre, vite"),
        ("Étape 2", "l'autre dit « plus lentement, s'il vous plaît »"),
        ("Étape 3", "le premier répète lentement"),
        ("Étape 4", "l'autre vérifie : « douze ? »"),
    ], cols=1,
       notes="Vingt-cinq minutes. Exiger les quatre étapes. C'est un exercice de courage "
             "autant que de langue.")

    d.billet(
        "Écrivez les six phrases de politesse dans votre carnet.",
        exemples=[
            "En français, et dans votre langue à côté.",
            "Apprenez surtout les deux dernières.",
        ],
        notes="Fin du bloc C. Ces six phrases sont le vrai acquis du module.")

    return d.save(dossier)
