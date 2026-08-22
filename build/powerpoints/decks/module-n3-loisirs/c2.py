# -*- coding: utf-8 -*-
"""C2 · Dix-neuf heures trente, ou sept heures et demie ?
Bloc C « Défi 2 · Le ciné-club du vendredi » · ambre · 75 min.
Source du module : exercice `t2heure`, mini-leçon `t2heure`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Dix-neuf heures trente, ou sept heures et demie ?",
        chapeau="Le feuillet écrit 19 h 30. La préposée dit « sept heures et "
                "demie ». Ce n'est pas une contradiction : l'un est l'heure "
                "des papiers, l'autre celle qu'on parle. Il faut savoir "
                "passer de l'une à l'autre, dans les deux sens.",
        duree='75 minutes')

    d.titre(notes="Séance qui compte parmi les plus utiles du module, et parmi les plus "
                  "réclamées par les élèves. Prévoir de la craie : le calcul « moins "
                  "douze » se fait au tableau, plusieurs fois.")

    d.objectifs([
        "lire l'heure officielle, de 0 h à 24 h ;",
        "la dire dans l'heure de tous les jours, de 1 à 12 ;",
        "employer « et demie », « et quart » et « moins quart » ;",
        "dire le début et la fin d'une activité avec « de… à… ».",
    ])

    d.tableau('Analyse', "Les deux systèmes, côte à côte",
              ["Sur le papier", "En parlant", "Le calcul"],
              [["10 h", "dix heures du matin", "avant midi : rien à changer"],
               ["13 h 15", "une heure et quart", "13 moins 12 = 1"],
               ["19 h", "sept heures du soir", "19 moins 12 = 7"],
               ["19 h 30", "sept heures et demie", "19 moins 12 = 7, et 30 = demie"],
               ["20 h 45", "neuf heures moins quart", "on compte sur l'heure suivante"]],
              cle=1,
              note="Après midi, on enlève 12. Avant midi, les deux se disent pareil.",
              notes="Diapo à photographier. Faire faire le calcul à voix haute pour "
                    "chaque ligne. La dernière est celle qui coince : y revenir avec "
                    "le piège plus loin.")

    d.regle("Les trois expressions à retenir",
            "et demie · et quart · moins quart",
            precision="30 minutes se dit « et demie ». 15 minutes, « et quart ». "
                      "45 minutes, « moins quart », en comptant sur l'heure suivante. "
                      "Avec ces trois-là, on dit les trois quarts des heures qu'on "
                      "rencontre dans un horaire.",
            notes="Diapo à photographier. Faire écrire les trois dans le cahier, avec un "
                  "exemple chacune tiré du feuillet du centre.")

    d.piege('Le piège', "huit heures moins quart pour 20 h 45",
            "neuf heures moins quart",
            "« Moins quart » veut dire : il manque quinze minutes avant l'heure "
            "suivante. À 20 h 45, l'heure suivante est 21 h, c'est-à-dire neuf heures. "
            "On dit donc « neuf heures moins quart », jamais huit.",
            notes="C'est la faute la plus fréquente de la séance, et elle est logique : "
                  "on lit le 20 et on l'annonce. Faire dessiner une horloge au tableau "
                  "et montrer l'aiguille qui monte vers le 9.")

    d.cartes("Deux précisions à ne pas oublier", "Elles évitent les malentendus", [
        ("du matin · du soir",
         "« On se voit à sept heures » est ambigu : matin ou soir ? Douze heures "
         "d'écart. On ajoute « du matin » ou « du soir » dès qu'il y a le moindre "
         "doute. Personne ne trouve ça lourd."),
        ("de… à…",
         "Une activité a un début et une fin : « de dix-neuf heures à vingt et une "
         "heures ». Sans les deux petits mots, la phrase ne tient pas. C'est ce qui "
         "distingue un horaire d'un rendez-vous."),
    ], cols=1,
       notes="Faire dire les heures du feuillet du centre avec « de… à… » : le "
             "badminton, la danse en ligne, l'heure des familles, la cuisine "
             "collective. Quatre phrases, et la forme est installée.")

    d.pratique('Écriture · 1 de 2', "De l'heure officielle à l'heure parlée",
               "Écrivez l'heure de tous les jours qui correspond.", [
        ("Le ciné-club commence à 19 h, c'est-à-dire à ___ heures du soir.", "sept"),
        ("La séance du 17 octobre est à 19 h 30, c'est-à-dire à sept heures ___ .", "et demie"),
        ("Le badminton finit à 21 h, c'est-à-dire à ___ heures du soir.", "neuf"),
        ("L'heure des familles est à 10 h, c'est-à-dire à ___ heures du matin.", "dix"),
        ("La cuisine collective commence à 13 h 15, c'est-à-dire à une heure ___ .", "et quart"),
        ("Le centre ferme à 20 h 45, c'est-à-dire à neuf heures ___ .", "moins quart"),
    ], corrige=True,
       notes="C'est l'exercice t2heure du module. Faire dire la réponse avant de "
             "l'écrire : l'oral va plus vite que le calcul écrit, et c'est l'oral "
             "qu'on veut.")

    d.pratique('Écriture · 2 de 2', "Écrivez la ligne complète",
               "Pour chaque activité, écrivez une phrase avec « de… à… ».", [
        ("badminton, mardi, 19 h à 21 h",
         "Le mardi soir, de dix-neuf heures à vingt et une heures."),
        ("danse en ligne, jeudi, 19 h à 20 h 30",
         "Le jeudi soir, de dix-neuf heures à vingt heures trente."),
        ("heure des familles, samedi, 10 h à 11 h",
         "Le samedi matin, de dix heures à onze heures."),
        ("cuisine collective, mercredi, 13 h à 16 h",
         "Le mercredi après-midi, de treize heures à seize heures."),
        ("ciné-club, vendredi, 19 h 30",
         "Le vendredi soir, à dix-neuf heures trente. (pas de fin annoncée)"),
    ], corrige=True,
       notes="La dernière ligne n'a pas de fin : un film n'annonce pas son heure de "
             "sortie, il annonce sa durée. Le faire remarquer — c'est le lien avec C1.")

    d.billet(
        "Écrivez trois heures de votre semaine, des deux façons.",
        exemples=[
            "L'heure officielle d'abord, l'heure parlée ensuite.",
            "Exemple : 18 h 30 — six heures et demie du soir.",
        ],
        notes="Devoir court. Ramasser : les erreurs de « moins quart » se voient tout de "
              "suite, et deux minutes en début de séance C3 suffisent à les reprendre.")

    return d.save(dossier)
