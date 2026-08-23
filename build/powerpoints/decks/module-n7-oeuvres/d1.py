# -*- coding: utf-8 -*-
"""D1 · Le comité, jeudi, dix-sept heures
Bloc D « Défi 3 » · couleur acier · compréhension orale · 75 min.
Source : dialogue `t3`, exercices `t3vf` et `t3plan`.
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n7-oeuvres' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Le comité, jeudi, dix-sept heures",
        chapeau="Marilou a tout écouté. Reste le plus difficile : le dire "
                "devant huit personnes, dont une qui n'est d'accord avec rien.",
        duree='75 minutes')

    d.titre(notes="Première séance du Défi 3, et la plus attendue : c'est la scène "
                  "que le module prépare depuis A1. Faire écouter en entier, "
                  "diapositive masquée, avant tout commentaire.")

    d.objectifs([
        "suivre une discussion à trois où personne n'est d'accord ;",
        "reconnaître les quatre morceaux d'un commentaire ;",
        "repérer une concession et voir ce qu'elle produit chez l'autre ;",
        "admettre à voix haute qu'un adversaire a soulevé un bon argument.",
    ], notes="Le quatrième objectif n'est pas de langue et il est pourtant le plus "
             "difficile. Marilou le fait deux fois dans le dialogue : le faire "
             "remarquer.")

    d.declencheur(
        'Observation', "Qu'est-ce qui fait qu'on écoute quelqu'un jusqu'au bout ?",
        image=IMG + 'hall-de-cinema.jpg',
        pistes=[
            "Le ton ? Le fait qu'il ait raison ? Le fait qu'il soit bref ?",
            "Avez-vous déjà cessé d'écouter quelqu'un dès sa première phrase ?",
            "Pourquoi ? Qu'est-ce qu'il avait dit ?",
            "Et vous, comment commencez-vous quand vous n'êtes pas d'accord ?",
        ],
        notes="Les réponses convergent presque toujours vers la même chose : on cesse "
              "d'écouter quelqu'un qui commence par nous contredire. C'est la "
              "démonstration de la concession, faite par la classe.")

    d.dialogue('Dialogue · 1 de 3', "L'objection arrive tout de suite", [
        ("MARILOU", "J'ai vu les trois. Je propose le film, « Onze heures moins quart ».", True),
        ("GAÉTAN", "Le film ? Deux heures dans le noir pour une sortie de fin d'année ? On peut faire ça chez nous.", True),
        ("MARILOU", "C'est vrai qu'on peut regarder un film chez soi, et ton objection est bonne.", True),
        ("MARILOU", "Mais laisse-moi dire d'abord ce que le film raconte, et ensuite ce que j'en pense.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Trois répliques et tout le module y est : l'objection, la concession, "
             "l'ordre annoncé. Faire relever par la classe ce que Marilou n'a pas "
             "fait : elle n'a pas défendu son choix tout de suite.")

    d.dialogue('Dialogue · 2 de 3', "Le résumé, puis le moment précis", [
        ("MARILOU", "Une boulangerie de nuit, à Gatineau. Un boulanger de cinquante-huit ans, une étudiante de dix-neuf ans, huit nuits de travail.", True),
        ("GAÉTAN", "Puis ?", True),
        ("MARILOU", "Puis c'est fini. Je ne dirai pas la dernière scène.", True),
        ("MARILOU", "À la quatrième nuit, il lui laisse pétrir seule et il sort fumer. On comprend en dix secondes qu'il lui fait confiance, et personne n'a eu besoin de le dire.", True),
    ], notes="Le résumé tient en deux phrases et ne donne pas la fin. Le moment "
             "précis tient en une. C'est le format exact demandé en E1.")

    d.dialogue('Dialogue · 3 de 3', "Un bon argument, et le budget", [
        ("GAÉTAN", "Je réponds que le monde rit quand le monde autour rit. C'est vrai dans une salle.", True),
        ("MARILOU", "Ça, c'est un bon argument, et je ne l'avais pas. Si tu as raison, mon objection tombe en partie.", True),
        ("GHYSLAINE", "En ce qui concerne l'argent, le film est à quinze dollars, l'humour à trente-quatre. Autrement dit, avec l'humour, il ne reste rien pour le transport.", True),
        ("MARILOU", "Si le budget était de deux mille dollars, je proposerais l'humour et l'autobus. Ce n'est pas le cas.", True),
    ], notes="Trois choses en quatre répliques : reconnaître un bon argument, les "
             "connecteurs de Ghyslaine (D2), et l'hypothèse avec « si » (D2). Ne pas "
             "les expliquer aujourd'hui, seulement les faire entendre.")

    d.tableau('Analyse', "Quatre morceaux, dans l'ordre",
              ['Le morceau', 'Ce qu\'il fait'],
              [["Le résumé", "deux ou trois phrases, au présent, sans la fin"],
               ["L'avis annoncé", "je propose, j'ai trouvé, il m'a semblé"],
               ["Le moment précis", "un seul, court, que les autres peuvent retrouver"],
               ["La concession", "avant sa position, et sur un point réellement vrai"]],
              cle=0,
              note="Une minute trente en tout, et personne ne peut répondre « ah bon ».",
              notes="Diapositive à photographier, et la plus importante du module. "
                    "C'est le plan de la production orale de E1.")

    d.regle("On accorde sur un point vrai, jamais sur un faux",
            "Une concession sur un point faux s'entend tout de suite et "
            "retourne la table contre vous.",
            precision="« C'est vrai qu'on peut regarder un film chez soi » est vrai, "
                      "et Gaétan écoute la suite. « C'est vrai que c'est un mauvais "
                      "film, mais... » aurait fait perdre à Marilou sa propre "
                      "position en une phrase.",
            notes="Diapositive à photographier. C'est la seule règle du module qui "
                  "porte sur l'honnêteté plutôt que sur la langue, et c'est la plus "
                  "opérante.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la réunion.", [
        ("Marilou commence par dire ce qu'elle pense.", "faux - elle résume d'abord"),
        ("Le film se passe dans une boulangerie de nuit.", "vrai"),
        ("Elle accorde à Gaétan qu'on peut regarder un film chez soi.", "vrai"),
        ("Marilou trouve le spectacle d'humour mauvais.", "faux - elle le trouve bon"),
        ("Gaétan soulève un argument qu'elle n'avait pas prévu.", "vrai"),
        ("Le compte rendu ne gardera que l'avis gagnant.", "faux - les trois avis"),
    ], corrige=True,
       notes="Exercice `t3vf` du module. Le cinquième est le plus riche : faire dire "
             "au groupe ce que Marilou aurait perdu en ne le reconnaissant pas.")

    d.billet(
        "Relisez votre argument de C4 : quel point pourriez-vous accorder à "
        "quelqu'un qui n'est pas d'accord ?",
        exemples=[
            "Une seule phrase, qui commence par « c'est vrai que ».",
            "Le point doit être réellement vrai.",
        ],
        notes="Préparation directe de D2, où la concession se dira « bien que » et "
              "« malgré ». La version parlée d'abord, la version écrite ensuite.")

    return d.save(dossier)
