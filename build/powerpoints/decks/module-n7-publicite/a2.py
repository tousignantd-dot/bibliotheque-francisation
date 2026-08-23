# -*- coding: utf-8 -*-
"""A2 · Le « e » que la vitesse avale
Bloc A « Je découvre » · couleur indigo · graphie-phonie · 75 min.
Source : exercice `prDebit`, mini-leçon `prDebit`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Le « e » que la vitesse avale",
        chapeau="La fin d'une annonce de radio est dite deux fois plus vite "
                "que le reste. C'est le petit « e » du milieu des mots qui en "
                "fait les frais — et c'est là que se trouvent les chiffres.",
        duree='75 minutes')

    d.titre(notes="Séance de prononciation, mais son enjeu est l'écoute. Le dire dès "
                  "le début : on travaille ici pour comprendre une mention légale, "
                  "pas pour bien parler.")

    d.objectifs([
        "entendre le petit « e » du milieu des mots, ou son absence ;",
        "savoir dans quels cas il se maintient, et dans quels cas il tombe ;",
        "reconnaître un mot connu sous sa forme raccourcie ;",
        "cesser de croire qu'on manque de vocabulaire quand on manque un « e ».",
    ], notes="Le quatrième objectif est celui qui change quelque chose. Beaucoup "
             "d'adultes qui lisent très bien croient mal entendre, alors qu'ils "
             "entendent parfaitement une forme qu'ils n'ont jamais apprise.")

    d.declencheur(
        'Écoute', "Trois mots, dits deux fois",
        pistes=[
            "Écoutez « seulement », puis « seul'ment ». Entendez-vous les deux ?",
            "Lequel des deux avez-vous déjà entendu à la radio ?",
            "Lequel des deux dites-vous, vous ?",
            "Est-ce qu'un des deux est une faute ?",
        ],
        notes="Répondre à la dernière question seulement à la fin : aucun des deux "
              "n'est une faute. C'est la place du « e » dans le mot qui décide, pas "
              "le niveau de langue ni le soin qu'on met à parler.")

    d.regle("Un son qui n'est pas obligatoire",
            "Le petit « e » de « semaine », de « rapidement », de « depuis » "
            "se dit parfois, et parfois pas du tout.",
            precision="Ce ne sont pas deux façons de parler, l'une soignée et "
                      "l'autre relâchée. Ce sont deux prononciations également "
                      "correctes, et c'est la place du « e » dans le mot qui décide.",
            notes="Diapositive à photographier. Le nom savant — « e caduc » — peut "
                  "être donné, mais il n'est pas à retenir.")

    d.tableau('Analyse', "Trois cas où le « e » tient",
              ['Le cas', 'Les mots'],
              [["Début, après p b t d k g", "depuis · devant · tenir · debout"],
               ["Deux consonnes devant", "autrement · le premier · vendredi"],
               ["Devant « ri » ou « li »", "un atelier · un ouvrier"]],
              cle=0,
              note="Dans ces trois cas, le mot devient impossible à dire sans lui.",
              notes="Faire prononcer « atlier » et « autrment » à voix haute : la "
                    "langue butte, et la règle se comprend d'elle-même.")

    d.tableau('Analyse', "Le cas où il tombe",
              ['On écrit', 'On entend'],
              [["seulement", "seul'ment"],
               ["gratuitement", "gratuit'ment"],
               ["rapidement", "rapid'ment"],
               ["la semaine", "la s'maine"],
               ["samedi", "sam'di"],
               ["finalement", "final'ment"]],
              cle=0,
              notes="Une seule consonne devant le « e », au milieu du mot : il tombe. "
                    "Faire répéter la colonne de droite, pas celle de gauche.")

    d.piege('Prononciation',
            "prononcer chaque « e » écrit, en quatre morceaux",
            "laisser tomber ceux du milieu",
            "Dire « ra-pi-de-ment » se comprend très bien, mais sonne "
            "appliqué et ralentit tout. Personne ne parle comme ça, et "
            "surtout pas dans une annonce de trente secondes. Le vrai coût "
            "n'est pas à la production : c'est à l'écoute, où l'on cherche un "
            "mot en quatre morceaux qui n'en fait que trois.",
            notes="Rassurer : garder un « e » qui aurait pu tomber ne provoque aucun "
                  "malentendu. C'est l'oreille qu'on entraîne ici.")

    d.pratique('Pratique', "On l'entend, ou il est avalé ?",
               "Écoutez chaque mot et classez-le.", [
        ("depuis", "on l'entend - d au début"),
        ("seulement", "il est avalé"),
        ("devant", "on l'entend - d au début"),
        ("gratuitement", "il est avalé"),
        ("autrement", "on l'entend - deux consonnes"),
        ("rapidement", "il est avalé"),
        ("tenir", "on l'entend - t au début"),
        ("la semaine", "il est avalé"),
    ], corrige=True,
       notes="Exercice `prDebit` du module. Faire dire les huit mots à voix haute "
             "après correction, dans les deux formes quand les deux existent.")

    d.cartes('Application', "Écouter une fin d'annonce", [
        ("Ce qu'on écrit", "Offre valable sur adhésion de douze mois."),
        ("Ce qu'on entend", "Offre valable sur adhésion de douze mois, dit deux fois plus vite."),
        ("Ce qui saute", "les « e » du milieu, et les syllabes faibles"),
        ("Ce qui reste", "les chiffres, toujours — douze, soixante, quatre"),
    ], cols=1,
       notes="Point de méthode : dans une mention légale, les chiffres résistent "
             "mieux que les mots. Entraîner l'oreille à les attraper d'abord, quitte "
             "à reconstruire la phrase ensuite.")

    d.billet(
        "Écoutez une annonce à la radio et notez un seul chiffre entendu à la fin.",
        exemples=[
            "Un montant, une durée, un pourcentage.",
            "Écrivez aussi ce que vous n'avez pas compris.",
        ],
        notes="Devoir d'écoute. Ce qu'ils n'ont pas compris est aussi intéressant que "
              "ce qu'ils ont attrapé : c'est la matière du bloc B.")

    return d.save(dossier)
