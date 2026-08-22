# -*- coding: utf-8 -*-
"""B4 · Du lundi au vendredi, de 9 h à 13 h.
Bloc B « Défi 1 » · couleur acier · 60 min. Compréhension orale.
Source du module : exercices `t1dispo` et `t1qui`, mini-leçon `t1dispo`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='acier',
        titre='Du lundi au vendredi, de 9 h à 13 h',
        chapeau="Dire quand on est libre, c'est donner deux choses : des "
                "jours et des heures. Le français les encadre par deux "
                "paires de petits mots qui ne se séparent jamais.",
        duree='60 minutes')

    d.titre(notes="Dernière séance du défi 1. À la fin, chacun doit pouvoir dire ses "
                  "vraies disponibilités sans hésiter et sans papier.")

    d.objectifs([
        "dire une suite de jours avec « du... au... » ;",
        "dire une tranche d'heures avec « de... à... » ;",
        "enlever un jour avec « sauf » ;",
        "reconnaître qui parle dans un échange d'embauche.",
    ])

    d.tableau('Analyse', "Deux paires, et rien d'autre à retenir",
              ['Ce qu\'on dit', 'La paire', "L'exemple"],
              [["Une suite de jours", "du... au...", "Du lundi au vendredi."],
               ["Une tranche d'heures", "de... à...", "De 9 h à 13 h."],
               ["Un moment qui revient", "le, la", "Le matin. La fin de semaine."],
               ["Un jour qu'on enlève", "sauf", "Du mardi au samedi, sauf le mercredi."]],
              cle=1,
              note="Les deux mots d'une paire vont ensemble : jamais l'un sans l'autre.",
              notes="Diapo à photographier. Faire remarquer que les paires ne se "
                    "mélangent pas : « de lundi à vendredi » est l'erreur du jour.")

    d.regle("13 h, c'est une heure de l'après-midi",
            "L'horaire officiel va jusqu'à 24 h.",
            precision="Une offre d'emploi écrit « de 9 h à 13 h » : cela fait quatre "
                      "heures, du matin au début de l'après-midi. On écrit 8 h avec une "
                      "espace avant le h, et rien après.",
            notes="Diapo à photographier. Faire convertir cinq horaires à l'oral : "
                  "17 h, 14 h 30, 20 h, 11 h, 22 h.")

    d.cartes("Ce qui se dit et ce qui ne se dit pas", "Quatre façons de répondre", [
        ("Précis, donc utile",
         "« Je suis libre du lundi au vendredi, le matin, de 8 h à 13 h. » Le patron "
         "peut écrire cela directement dans son horaire."),
        ("Vague, donc inutile",
         "« Je suis disponible n'importe quand. » Cela sonne bien et ne remplit aucune "
         "case. Le patron devra redemander, ou passer au suivant."),
        ("Dire aussi ce qui bloque",
         "« Je suis à l'école l'après-midi. » Le dire tout de suite vaut mieux que de "
         "le dire après que l'horaire est fait."),
        ("Le mot du Québec",
         "La fin de semaine, c'est samedi et dimanche. « Week-end » se comprend "
         "partout, mais dans un commerce de quartier, on dit la fin de semaine."),
    ], notes="Faire dire à chacun ses disponibilités réelles, debout, en une seule "
             "phrase. Corriger la forme, jamais le contenu.")

    d.piege("Mélanger les deux paires",
            "De lundi à vendredi, du 9 h au 13 h.",
            "Du lundi au vendredi, de 9 h à 13 h.",
            "Pour les jours, c'est « du... au... » ; pour les heures, « de... à... ». "
            "Les deux paires se ressemblent assez pour qu'on les échange, et l'échange "
            "s'entend tout de suite. Une seule phrase modèle à retenir, et elle contient "
            "les deux.",
            notes="Faire écrire la phrase modèle au tableau et la laisser affichée "
                  "jusqu'à la fin du module.")

    d.pratique('Écriture', "Complétez avec le bon petit mot",
               "Complétez avec : du, au, de, à, le, sauf.", [
        ("Je suis libre ___ lundi ___ vendredi.", "du... au"),
        ("Je peux travailler ___ neuf heures ___ une heure.", "de... à"),
        ("Je suis à l'école ___ après-midi.", "l'"),
        ("Je travaille du mardi au samedi, ___ le jeudi.", "sauf"),
        ("Je suis disponible ___ matin seulement.", "le"),
        ("Du lundi ___ vendredi, ça me convient.", "au"),
    ], corrige=True,
       notes="Même exercice que t1dispo dans le module. Faire relire chaque phrase "
             "complète : c'est l'oreille qui retient les paires, pas la règle.")

    d.pratique('Écoute', "Fanta ou Gilles ?",
               "Qui dit cette phrase : celle qui cherche, ou celui qui engage ?", [
        ("J'ai vu votre affiche dans la vitrine.", "Fanta"),
        ("Oui, on cherche quelqu'un.", "Gilles"),
        ("Vous êtes disponible quels jours ?", "Gilles"),
        ("Du lundi au vendredi, le matin.", "Fanta"),
        ("Écrivez-le ici, sur le carnet.", "Gilles"),
        ("Je peux vous l'écrire ?", "Fanta"),
    ], corrige=True, cols=2,
       notes="Même exercice que t1qui dans le module. Demander à chaque fois ce qui "
             "permet de trancher : le verbe, le vouvoiement, l'impératif.")

    d.pratique('Oral', "Vos vraies disponibilités",
               "Chacun dit les siennes, en une phrase, avec des jours et des heures.", [
        ("La phrase attendue", "Je suis libre du... au..., de... à..."),
        ("Ce qui bloque", "Je suis à l'école... / Je garde mes enfants..."),
        ("La fin de semaine", "Je suis libre la fin de semaine, le... "),
    ], notes="Faire le tour du groupe, debout. Personne ne se rassoit avant d'avoir "
             "dit une phrase complète et juste. C'est le contrôle du défi 1.")

    d.billet(
        "Écrivez vos disponibilités, en une phrase, avec des jours et des heures.",
        exemples=[
            "Du... au..., de... à...",
            "Ajoutez ce qui bloque : école, enfants, autre travail.",
        ],
        notes="Deux minutes. Cette phrase entre dans le formulaire du défi 3 et dans "
              "la petite annonce de E2 : elle sera relue deux fois.")

    return d.save(dossier)
