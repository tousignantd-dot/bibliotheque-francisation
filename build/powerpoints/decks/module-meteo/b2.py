# -*- coding: utf-8 -*-
"""B2 · Les chiffres et les unités du bulletin.
Bloc B · couleur framboise (vocabulaire) · 60 min.
Source : le bulletin `t1` — degrés, kilomètres à l'heure, centimètres, heures.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='framboise',
        titre='Les chiffres du bulletin',
        chapeau="« Moins six », « soixante kilomètres à l'heure », « deux à quatre "
                "centimètres ». Un bulletin est fait de chiffres — et un chiffre mal "
                "entendu change une décision.",
        duree='60 minutes')

    d.titre(notes="Dicter cinq chiffres du bulletin sans prévenir, à vitesse normale. Le "
                  "groupe verra tout de suite où est la difficulté.")

    d.objectifs([
        "entendre et écrire les nombres d'un bulletin météo ;",
        "associer chaque chiffre à son unité ;",
        "dire une température négative correctement ;",
        "lire l'heure comme le fait un bulletin.",
    ])

    d.tableau('Analyse', "Quatre unités, quatre façons de les dire",
              ["L'unité", 'On dit', 'On écrit'],
              [["la température", "moins six degrés", "-6 °C"],
               ["le vent", "soixante kilomètres à l'heure", "60 km/h"],
               ["la neige", "deux à quatre centimètres", "2 à 4 cm"],
               ["la visibilité", "moins de deux cents mètres", "moins de 200 m"]],
              cle=1, props=[0.26, 0.45, 0.29],
              notes="Faire lire la colonne du milieu à voix haute. C'est la forme "
                    "entendue ; la colonne de droite est celle qu'on écrit.")

    d.regle('La règle des températures',
            "On dit « moins six », jamais « négatif six ».",
            precision="Moins un, moins dix, moins vingt-cinq. Et pour zéro : « autour de "
                      "zéro », « le point de congélation ». Le mot « moins » se place "
                      "toujours devant le nombre.",
            notes="Erreur fréquente chez les anglophones et les hispanophones. La "
                  "corriger une fois, clairement.")

    d.cartes('En apprendre plus', "Quatre pièges des chiffres à l'oral", [
        ("Soixante et soixante-dix",
         "Au Québec comme en France, on dit « soixante-dix », pas « septante ». Mais "
         "« soixante » et « soixante-dix » se ressemblent : écoutez la fin."),
        ("Deux et douze",
         "« Deux degrés » et « douze degrés » se confondent vite à la radio. Le "
         "contexte aide : en janvier, douze est peu probable."),
        ("Les fourchettes",
         "« Deux à quatre centimètres » donne une fourchette, pas un chiffre. Notez les "
         "deux : c'est l'écart qui compte."),
        ("« Une trentaine », « une dizaine »",
         "Ce sont des approximations : environ trente, environ dix. On les entend "
         "souvent dans les bulletins."),
    ], notes="La deuxième carte donne une stratégie : le contexte corrige l'oreille. "
             "L'appliquer à trois exemples.")

    d.pratique('Pratique · 1 de 4', "Écrivez le chiffre et son unité",
               "Vous entendez la forme parlée.", [
        ("« moins six degrés »", "-6 °C"),
        ("« soixante kilomètres à l'heure »", "60 km/h"),
        ("« deux à quatre centimètres »", "2 à 4 cm"),
        ("« moins de deux cents mètres »", "moins de 200 m"),
        ("« quarante kilomètres à l'heure »", "40 km/h"),
        ("« autour de zéro degré »", "environ 0 °C"),
    ], corrige=True,
       notes="Dicter chaque forme deux fois, à vitesse normale. C'est un exercice "
             "d'écoute, pas de lecture.")

    d.pratique('Pratique · 2 de 4', "Dites le chiffre",
               "Vous lisez la forme écrite. Comment la dit-on ?", [
        ("-15 °C", "moins quinze degrés"),
        ("45 km/h", "quarante-cinq kilomètres à l'heure"),
        ("5 à 10 cm", "cinq à dix centimètres"),
        ("9 h", "neuf heures"),
        ("-27 ressenti", "moins vingt-sept ressenti, avec le facteur éolien"),
    ], corrige=True,
       notes="Faire dire chaque forme par un élève différent, à voix haute. C'est "
             "l'exercice inverse du précédent.")

    d.piege("Le piège du chiffre sans unité",
            "Vous notez « 60 » et vous ne savez plus de quoi il s'agit.",
            "Notez toujours l'unité avec le chiffre : 60 km/h.",
            "Soixante degrés, soixante kilomètres à l'heure et soixante centimètres "
            "n'ont rien à voir. Un chiffre noté seul est inutilisable une heure plus "
            "tard, et c'est l'erreur de prise de notes la plus fréquente.",
            notes="Faire relire les notes prises en B1. Beaucoup contiendront des "
                  "chiffres sans unité.")

    d.piege("Le piège de « moins » entendu comme un mot ordinaire",
            "« Le mercure descendra à moins six » — vous notez « 6 ».",
            "« Moins six » veut dire -6, sous zéro.",
            "En hiver, le mot « moins » change tout : six degrés et moins six degrés "
            "sont douze degrés d'écart. C'est la différence entre de la pluie et du "
            "verglas — donc entre travailler et rester à l'atelier.",
            notes="Point décisif du module. Faire répéter cinq températures négatives à "
                  "voix haute, avec le mot « moins ».")

    d.pratique('Pratique · 3 de 4', "Que décide ce chiffre ?",
               "Chaque chiffre a une conséquence pratique.", [
        ("Rafales à 60 km/h", "on ne monte pas — la règle est à 40"),
        ("Mercure à 0 degré", "la pluie gèle en touchant les surfaces"),
        ("Mercure à moins six", "la pluie devient de la neige"),
        ("Visibilité à 200 mètres", "on ne conduit pas, ou très lentement"),
        ("Ressenti à moins 27", "on limite l'exposition à trente minutes"),
    ], corrige=True,
       notes="C'est le lien entre le chiffre et la décision. Le faire formuler par le "
             "groupe avant d'afficher les réponses.")

    d.pratique('Pratique · 4 de 4', "Dictée de bulletin",
               "Écrivez le bulletin entendu. Chiffres et unités.", [
        ("Phrase 1", "Le mercure descendra à moins huit degrés cette nuit."),
        ("Phrase 2", "Des rafales de cinquante kilomètres à l'heure sont attendues."),
        ("Phrase 3", "Cinq à dix centimètres de neige tomberont d'ici demain matin."),
        ("Phrase 4", "La visibilité pourrait tomber sous les cinq cents mètres."),
    ], corrige=True,
       notes="Dicter chaque phrase deux fois, à vitesse normale. Corriger uniquement les "
             "chiffres et les unités.")

    d.billet(
        "Notez cinq chiffres du bulletin de demain, avec leur unité.",
        exemples=[
            "La température, le vent, les précipitations, une heure, la visibilité.",
            "Écrivez la forme parlée à côté de la forme écrite.",
        ],
        notes="Ce billet se corrige en trente secondes et il révèle exactement qui entend "
              "les chiffres et qui ne les entend pas encore.")

    return d.save(dossier)
