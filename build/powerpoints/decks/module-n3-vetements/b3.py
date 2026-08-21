# -*- coding: utf-8 -*-
"""B3 · Taille, pointure et essayage.
Bloc B « Défi 1 · Demander ce qu'on cherche » · couleur teal · 60 min.
Source : exercice `t1taille`, mini-leçon `t1taille`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='teal',
        titre='Taille, pointure et essayage',
        chapeau="Le vêtement a une taille, le pied a une pointure. Deux mots "
                "différents pour la même idée — et l'un des deux ne sert "
                "qu'aux chaussures.",
        duree='60 minutes')

    d.titre(notes="Séance d'écoute et de production orale. Prévoir le son : les quatre "
                  "questions du magasin doivent être entendues avant d'être dites.")

    d.objectifs([
        "distinguer la taille et la pointure ;",
        "poser une question avec « quel » et « quelle » ;",
        "dire ce qui ne va pas avec un adjectif et un endroit ;",
        "demander une autre taille ou un autre modèle.",
    ])

    d.declencheur(
        'Écoute', "Quelle question vous pose-t-on ?",
        pistes=[
            "« Vous portez quelle taille ? »",
            "« Quelle pointure faites-vous ? »",
            "Laquelle est pour un manteau ?",
            "Laquelle est pour des bottes ?",
        ],
        notes="Faire écouter les deux questions du module. Le groupe repère vite que les "
              "deux mots ne s'emploient pas au même endroit.")

    d.tableau('Analyse', "Deux mots, deux usages",
              ['On demande', 'Pour quoi'],
              [["Vous portez quelle taille ?", "un manteau, un chandail, un pantalon"],
               ["Quelle pointure faites-vous ?", "des bottes, des souliers"],
               ["P · M · G · TG", "les lettres de l'étiquette de taille"],
               ["6 · 7 · 8 · 9", "les chiffres de la pointure, ici"]],
              cle=0,
              note="Un 38 européen fait environ un 7 ici : les chiffres ne se traduisent pas.",
              notes="Diapo à photographier. Le dernier point est celui qui surprend le "
                    "plus les nouveaux arrivants.")

    d.regle("La question avec « quel »",
            "<b>Quelle</b> taille ? <b>Quelle</b> couleur ? <b>Quel</b> modèle ?",
            precision="Le mot s'accorde avec ce qui suit. Taille, couleur et pointure sont "
                      "féminins : <b>quelle</b>. Modèle et prix sont masculins : "
                      "<b>quel</b>. À l'oral, les deux formes se prononcent pareil — c'est "
                      "à l'écrit que la différence compte.",
            notes="Diapo à photographier. Rassurer : à l'oral, aucune erreur possible.")

    d.cartes("Dire ce qui ne va pas", "Un adjectif et un endroit", [
        ("Trop petit",
         "« C'est trop <b>serré</b> aux épaules. » Serré veut dire que le vêtement presse "
         "le corps."),
        ("Trop grand",
         "« C'est un peu <b>large</b>. » Ou « c'est trop grand », qui se dit aussi."),
        ("Trop long ou trop court",
         "« Les <b>manches</b> sont trop longues. » Sur un pantalon, ce sont les jambes."),
        ("Ce qu'on demande ensuite",
         "« Vous l'avez en grand ? » « Vous avez un autre modèle ? » « Vous l'avez dans "
         "une autre couleur ? »"),
    ], notes="Faire jouer la scène à deux : un élève dit le problème, l'autre propose la "
             "suite. Deux minutes suffisent.")

    d.piege("Traduire son chiffre",
            "Je fais du 42.",
            "Je ne connais pas ma taille ici, je vais essayer.",
            "Les systèmes de tailles ne se correspondent pas d'un pays à l'autre, et deux "
            "magasins d'ici ne taillent même pas pareil. Essayer est la seule méthode "
            "sûre, et personne ne trouve étrange qu'on le fasse.",
            notes="Insister : dire qu'on ne sait pas est une phrase d'adulte, pas un aveu "
                  "d'ignorance.")

    d.pratique('Pratique · 1 de 2', "Complétez",
               "D'après le dialogue et l'encadré.", [
        ("Sur l'étiquette, M veut dire ___ .", "moyen"),
        ("Farida pense qu'elle est ___ .", "moyenne"),
        ("Le manteau moyen est trop ___ aux épaules.", "serré"),
        ("Pour les bottes, on dit la ___ .", "pointure"),
        ("Pour essayer, on va dans la ___ d'essayage.", "cabine"),
    ], corrige=True,
       notes="Utiliser l'exercice 3 du défi 1.")

    d.pratique('Pratique · 2 de 2', "Que dites-vous ?",
               "Une phrase courte et polie pour chaque situation.", [
        ("Vous cherchez un manteau noir.", "Je cherche un manteau noir."),
        ("On vous demande votre taille.", "Je porte du moyen."),
        ("Vous voulez mettre le manteau pour voir.", "Je peux l'essayer ?"),
        ("Vous cherchez la cabine.", "Où est la cabine d'essayage ?"),
        ("Le manteau presse aux épaules.", "C'est trop serré aux épaules."),
        ("Vous voulez la taille au-dessus.", "Vous l'avez en grand ?"),
    ], corrige=True, cols=1,
       notes="Utiliser l'exercice 4 du défi 1. Faire dire à voix haute avant d'écrire : "
             "c'est de la production orale déguisée.")

    d.billet(
        "Écrivez le dialogue complet d'un essayage, en six répliques.",
        exemples=[
            "Vous entrez, vous demandez, on vous demande votre taille.",
            "Vous essayez, quelque chose ne va pas, vous demandez autre chose.",
        ],
        notes="Devoir de production écrite. Il sert de brouillon au jeu de rôle de E1 : "
              "garder les copies.")

    return d.save(dossier)
