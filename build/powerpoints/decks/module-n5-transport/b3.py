# -*- coding: utf-8 -*-
"""B3 · Depuis quand, et pour combien de temps
Bloc B « Défi 1 · Ce qui bloque la route » · couleur ambre · 75 min.
Source : exercice `t1qd` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Depuis quand, et pour combien de temps",
        chapeau="Tout le monde pose la mauvaise question : « Combien de "
                "temps ? » Il y en a deux, et elles ne se répondent pas de la "
                "même façon. La première dit si c'est en train de finir ; la "
                "seconde, s'il faut attendre.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire du temps, ancrée dans une décision réelle. Ouvrir "
                  "par la question : « Ça fait combien de temps que ça bloque ? » et "
                  "« Ça va durer combien de temps ? » — deux questions différentes, que "
                  "le groupe confond presque toujours au départ.")

    d.objectifs([
        "employer « depuis » avec un moment de départ ou une durée ;",
        "employer « il y a » pour une durée écoulée ;",
        "employer « ça fait… que » à l'oral ;",
        "distinguer « pendant », « dans » et « jusqu'à ».",
    ], notes="Cinq expressions, six si l'on compte « jusqu'à ». C'est beaucoup pour une "
             "séance : accepter que « pendant » et « dans » soient seulement reconnus "
             "aujourd'hui et repris en D2.")

    d.regle("Deux questions, pas une",
            "Depuis quand ça dure ? Et pour combien de temps encore ?",
            precision="« Ça fait presque une heure » répond aux deux d'un coup : "
                      "ça a commencé il y a une heure, et ce n'est pas fini.",
            notes="Diapositive à photographier. C'est aussi la question que la "
                  "responsable de l'atelier pose au téléphone en D1.")

    d.tableau('Trois façons de dire le début',
              "Elles ne sont pas interchangeables",
              ['On dit', 'Ce que ça donne'],
              [["depuis six heures", "l'heure du début"],
               ["depuis une heure", "la durée écoulée"],
               ["il y a quarante minutes", "à reculons"],
               ["ça fait une heure que", "la durée, à l'oral"]],
              cle=1,
              notes="Faire remarquer que « depuis » accepte les deux : une heure de "
                    "départ ou une durée. C'est la seule de la série qui fasse les deux, "
                    "et c'est ce qui la rend commode.")

    d.tableau('Trois façons de dire la suite', "Ce qui reste à venir",
              ['On dit', 'Ce que ça donne'],
              [["pendant deux jours", "la durée complète"],
               ["dans dix minutes", "un délai"],
               ["jusqu'à neuf heures", "l'heure de la fin"]],
              cle=1,
              note="« Jusqu'à » est le mot le plus précieux du bulletin.",
              notes="Insister sur « jusqu'à » : c'est le seul qui donne une heure à "
                    "laquelle on pourra repartir. Faire noter cette heure chaque fois "
                    "qu'elle est dite.")

    d.piege("Mélanger « il y a » et « depuis »",
            "Il y a depuis une heure que c'est bloqué.",
            "C'est bloqué depuis une heure. Ou : ça a commencé il y a une heure.",
            "Ce sont deux constructions différentes. Les mettre ensemble ne forme "
            "pas une phrase française, et c'est l'erreur la plus fréquente à ce "
            "niveau.",
            notes="Écrire les deux formes correctes au tableau et les y laisser toute la "
                  "séance. L'erreur revient dès qu'on cesse de les voir.")

    d.piege("Employer « pendant » pour un accident",
            "L'accident bloque la route pendant vingt minutes.",
            "L'accident bloque la route pour au moins vingt minutes.",
            "« Pendant » s'emploie pour ce qui est prévu et dont on connaît la fin : "
            "des travaux, une fermeture annoncée. Un accident ne se planifie pas.",
            notes="Ce piège prépare la séance B4, qui porte entièrement sur la "
                  "différence entre le prévu et l'imprévu.")

    d.pratique('Grammaire', "Complétez avec l'expression juste",
               "depuis · il y a · ça fait… que · pendant · dans · jusqu'à", [
        ("La voie est bloquée ___ six heures et demie.", "depuis"),
        ("L'accident s'est produit ___ quarante minutes.", "il y a"),
        ("___ presque une heure ___ c'est arrêté.", "ça fait … que"),
        ("La bretelle sera fermée ___ toute la fin de semaine.", "pendant"),
        ("Le pont est fermé ___ neuf heures.", "jusqu'à"),
        ("Prochain bulletin ___ dix minutes.", "dans"),
    ], corrige=True,
       notes="Les six mêmes phrases sont dans l'exercice `t1qd` de l'activité "
             "interactive. Faire dire chaque phrase complète à voix haute après "
             "correction : la forme se fixe par l'oreille.")

    d.billet(
        "Écrivez deux phrases sur une attente que vous avez vécue : depuis quand, et jusqu'à quand.",
        exemples=[
            "Une attente à l'hôpital, à la banque, à l'aéroport fait aussi l'affaire.",
            "Employez « depuis » dans la première et « jusqu'à » dans la seconde.",
        ],
        notes="Ramasser les billets. Les deux expressions sont celles qui reviendront "
              "dans le message de retard de la séance E1.")

    return d.save(dossier)
