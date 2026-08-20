# -*- coding: utf-8 -*-
"""C1 · À ton tour d'expliquer.
Bloc C « Défi 2 · Expliquer le chemin » · couleur acier · 60 min.
Source : dialogue `t2`, exercices `t2vf` et `t2ordre`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="À ton tour d'expliquer",
        chapeau="Cette fois, c'est Nour qui explique. Patrice doit se rendre au "
                "centre d'emploi demain matin. Sortir, tourner, traverser, "
                "marcher : quatre verbes suffisent, si l'ordre est bon.",
        duree='60 minutes')

    d.titre(notes="Ouverture du bloc C. Renverser les rôles est le vrai saut du module : "
                  "comprendre un itinéraire est plus facile que d'en donner un.")

    d.objectifs([
        "donner un itinéraire à pied, étape par étape ;",
        "choisir des repères visuels que l'autre reconnaîtra ;",
        "annoncer la durée du trajet ;",
        "ajouter l'avertissement utile que personne n'a demandé.",
    ])

    d.declencheur(
        'Mise en situation', "Quelqu'un vous demande le chemin. Par quoi commencez-vous ?",
        pistes=[
            "Demandez-vous d'abord d'où la personne part ?",
            "Donnez-vous tout l'itinéraire d'un coup, ou étape par étape ?",
            "Quels repères choisissez-vous : des noms de rue, des commerces, des couleurs ?",
            "Dites-vous combien de temps ça prend ?",
        ],
        notes="Cinq minutes. Insister sur la première piste : demander le point de départ "
              "est l'étape que tout le monde saute, et sans elle rien ne fonctionne.")

    d.dialogue('Dialogue · 1 de 3', "D'où pars-tu ?", [
        ("PATRICE", "Nour, tu connais le chemin pour aller au centre d'emploi ? Je dois y aller demain matin.", False),
        ("NOUR", "Oui, j'y suis allée la semaine passée. Tu pars d'ici, du centre de formation ?", True),
        ("PATRICE", "Oui, à huit heures.", False),
        ("NOUR", "Alors sors par la porte principale et tourne à droite. Marche jusqu'au parc.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="La deuxième réplique contient la question qui sauve tout : « tu pars d'ici ? ». "
             "Sans elle, l'itinéraire pourrait être entièrement faux.")

    d.dialogue('Dialogue · 2 de 3', "Le repère qu'on reconnaît", [
        ("PATRICE", "Le parc avec les jeux d'enfants ?", False),
        ("NOUR", "Celui-là, oui. Traverse le parc, il y a un sentier au milieu. Tu arrives sur la rue Victoria.", True),
        ("PATRICE", "Et là, à droite ou à gauche ?", False),
        ("NOUR", "À gauche. L'édifice est le troisième, celui qui a une grande porte vitrée.", True),
    ], notes="« Celui-là » et « celui qui » : deux pronoms démonstratifs en quatre "
             "répliques. Les signaler sans les enseigner — c'est la séance C3.")

    d.dialogue('Dialogue · 3 de 3', "Ce qu'on ajoute sans qu'on le demande", [
        ("PATRICE", "Il y a une enseigne ?", False),
        ("NOUR", "Une petite, au-dessus de la porte. Ne cherche pas une grande affiche, il n'y en a pas.", True),
        ("PATRICE", "Ça me prend combien de temps ?", False),
        ("NOUR", "Douze minutes à pied. Mais s'il pleut, ne traverse pas le parc : le sentier devient de la boue.", True),
    ], notes="La dernière réplique est ce qui distingue une bonne explication d'une "
             "explication correcte : l'avertissement que l'autre n'a pas pensé à demander.")

    d.tableau('Analyse', "Les cinq étapes du trajet de Patrice",
              ['Où il est', 'Ce qu\'il fait'],
              [["En sortant du centre", "sortir par la porte principale, tourner à droite"],
               ["Sur le trottoir", "marcher jusqu'au parc"],
               ["Dans le parc", "traverser par le sentier du milieu"],
               ["Sur la rue Victoria", "tourner à gauche"],
               ["À l'arrivée", "chercher le troisième édifice, celui à la porte vitrée"]],
              cle=2,
              notes="Cacher la colonne de droite et faire reconstituer de mémoire, à deux. "
                    "L'ordre est ce qui compte.")

    d.regle("Ce qu'il faut retenir",
            "Demandez toujours d'où la personne part. C'est l'étape qu'on saute.",
            precision="Un itinéraire est relatif à un point de départ. Sans lui, la "
                      "meilleure explication du monde envoie la personne dans la mauvaise "
                      "direction. Nour pose la question dès sa deuxième réplique.",
            notes="Diapo à photographier. La faire répéter par deux élèves.")

    d.piege('Tout donner d\'un coup',
            "Sors, tourne à droite, marche jusqu'au parc, traverse, tourne à gauche, c'est le troisième.",
            "Sors par la porte principale et tourne à droite. Marche jusqu'au parc. — Le parc avec les jeux ? — Celui-là, oui.",
            "Personne ne retient six étapes d'affilée. Donnez-en une ou deux, attendez que "
            "l'autre confirme, puis continuez. C'est ce que fait Nour, et c'est pour ça que "
            "Patrice suit.",
            notes="Faire l'expérience : un élève débite six étapes, un autre essaie de les "
                  "répéter. L'échec est immédiat et convaincant.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Nour n'est jamais allée à cet endroit.", "faux — elle y est allée la semaine passée"),
        ("Il faut sortir par la porte principale et tourner à droite.", "vrai"),
        ("Après le parc, il faut tourner à droite sur Victoria.", "faux — à gauche"),
        ("Il y a une grande affiche sur l'édifice.", "faux — une petite enseigne"),
        ("Le trajet prend douze minutes à pied.", "vrai"),
        ("S'il pleut, Nour conseille de traverser le parc quand même.", "faux — le sentier devient de la boue"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte.")

    d.billet(
        "Écrivez l'itinéraire de l'arrêt d'autobus jusqu'à la porte de votre logement.",
        exemples=[
            "Cinq étapes maximum, dans l'ordre.",
            "Au moins deux repères visuels et la durée.",
        ],
        notes="Ce billet est le brouillon direct de la production écrite de E1. Le corriger "
              "et le rendre avant cette séance.")

    return d.save(dossier)
