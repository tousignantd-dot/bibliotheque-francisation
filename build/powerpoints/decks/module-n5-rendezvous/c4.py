# -*- coding: utf-8 -*-
"""C4 · Poser ses questions avant de sortir.
Bloc C « Défi 2 » · couleur acier · 75 min.
Source : exercices `t2quest` et `t2mots`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-rendezvous/images/')


def build(dossier):
    d = Deck(
        code='C4', section='acier',
        titre="Poser ses questions avant de sortir",
        chapeau="Un rendez-vous se termine quand vous avez fini, pas quand "
                "le médecin a fini. La moitié de ce qu'on vient chercher "
                "s'obtient dans les deux dernières minutes.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du défi 2. Demander au groupe : à votre dernier "
                  "rendez-vous, avez-vous posé une question ? Le silence qui suit est le "
                  "meilleur départ possible.")

    d.objectifs([
        "poser les quatre questions qui valent pour tout problème ;",
        "faire redire autrement un mot qu'on n'a pas compris ;",
        "reformuler une consigne pour la faire vérifier ;",
        "reconnaître huit mots courants d'un bureau de médecin.",
    ])

    d.declencheur(
        'Observation', "Vous sortez du bureau. Quand aurez-vous vos résultats, et "
                       "comment ?",
        image=IMG + 'ordonnance-papier.jpg',
        pistes=[
            "Est-ce qu'on vous appellera ?",
            "Faut-il reprendre un rendez-vous ?",
            "Qui doit le fixer, vous ou la clinique ?",
            "Qu'est-ce que vous faites si ça empire d'ici là ?",
        ],
        notes="Ces quatre questions restent sans réponse dans une consultation sur deux — "
              "non parce que le médecin refuse, mais parce que personne ne les pose.")

    d.regle("Un rendez-vous finit quand vous avez fini",
            "« J'ai deux questions avant de partir. »",
            precision="Annoncées d'avance, les questions trouvent leur place : le médecin "
                      "garde le temps qu'il faut. Gardées pour la fin, elles arrivent "
                      "quand il est déjà debout et qu'il n'y a plus de place pour elles.",
            notes="Diapositive à photographier. Faire répéter la phrase à voix haute, "
                  "toute la classe : c'est une phrase qu'on n'ose pas dire, et la répéter "
                  "en groupe la désamorce.")

    d.cartes("Les quatre questions à poser toujours", "Quel que soit le problème", [
        ("1 · Qu'est-ce que j'ai, en mots simples ?",
         "« Est-ce que vous pouvez m'expliquer ce que ça veut dire ? »"),
        ("2 · Qu'est-ce que je peux continuer de faire ?",
         "« Est-ce que je dois arrêter de travailler ? Et le sport ? »"),
        ("3 · Quand et comment j'aurai les résultats ?",
         "« On m'appelle ? Il faut reprendre un rendez-vous ? »"),
        ("4 · Qu'est-ce que je fais si ça empire ?",
         "« D'ici là, à partir de quoi je dois m'inquiéter ? »"),
    ], notes="Les faire écrire sur la même feuille que la fiche de rendez-vous de B4. "
             "Une seule feuille, deux listes, un seul geste.")

    d.tableau('Faire redire, et vérifier', "Trois phrases qui n'offensent personne",
              ['Ce qu\'on veut', 'Ce qu\'on dit'],
              [["Un autre mot", "« Vous pouvez me le redire autrement ? »"],
               ["Une explication", "« Qu'est-ce que ça veut dire pour moi ? »"],
               ["Vérifier ce qu'on a compris", "« Donc, si je comprends bien… »"],
               ["Du temps", "« Un instant, je le note. »"]],
              cle=0,
              note="« Redire autrement » vaut mieux que « répéter » : répéter donne les mêmes mots.",
              notes="Cette nuance surprend toujours et sert toute la vie. Y insister.")

    d.vocabulaire('Vocabulaire', "Huit mots du bureau", [
        ("un symptôme", "Ce que le corps montre quand quelque chose ne va pas."),
        ("un étourdissement", "La tête qui tourne, sans tomber ni perdre connaissance."),
        ("la tension artérielle", "La force du sang : deux nombres, le grand puis le petit."),
        ("une ordonnance", "Le papier signé qui autorise un examen ou un médicament."),
        ("une prise de sang", "Le prélèvement qu'on fait au bras, souvent tôt le matin."),
        ("à jeun", "Rien à manger depuis plusieurs heures ; de l'eau seulement."),
        ("un bilan sanguin", "L'ensemble des analyses demandées d'un coup."),
        ("un rendez-vous de suivi", "Le rendez-vous d'après, pour regarder les résultats."),
    ], notes="Ne pas exiger la production : il suffit de les reconnaître. Le dire aux "
             "élèves, ça enlève une inquiétude inutile.")

    d.piege("Dire oui sans avoir compris",
            "« Oui, oui, d'accord. »",
            "« Je m'excuse, je n'ai pas compris ce mot-là. »",
            "Personne ne s'en aperçoit dans le bureau — le prix se paie ensuite, quand une "
            "consigne est appliquée de travers pendant des semaines. Un « à jeun » mal "
            "compris fait refaire un prélèvement un autre matin.",
            notes="Nommer la gêne : on dit oui pour ne pas déranger. Dire clairement "
                  "qu'aucun professionnel ne s'en offusque.")

    d.pratique('Compréhension', "Que rapporte cette question ?",
               "Associez chaque question à ce qu'elle vous apprend.", [
        ("« Vous pouvez m'expliquer ce que ça veut dire ? »", "un mot ou un résultat, autrement"),
        ("« Est-ce que je dois arrêter de travailler ? »", "ce qu'on peut continuer de faire"),
        ("« Quand est-ce que j'aurai les résultats ? »", "le délai et le moyen"),
        ("« Qu'est-ce que je fais si ça empire ? »", "une consigne pour le pire cas"),
        ("« Est-ce qu'il faut que je sois à jeun ? »", "comment se préparer"),
        ("« Est-ce que je dois reprendre un rendez-vous ? »", "si un suivi est prévu, et qui le fixe"),
    ], corrige=True,
       notes="Faire dire chaque question à voix haute avant de donner la réponse. "
             "L'intonation compte autant que les mots.")

    # `capture` n'existe que dans theme.Deck : les présentations la portent, les
    # fiches imprimées non (build/powerpoints/fiche.py n'a pas la méthode). Une
    # fiche noir et blanc n'a de toute façon rien à faire d'une capture d'écran.
    if hasattr(d, 'capture'):
        d.capture('t2quest', "Vos questions, et ce qu'elles vous rapportent",
                  consigne="Choisissez une question, puis ce qu'elle sert à obtenir.",
                  notes="Projeter après l'exercice à l'oral : le groupe voit alors ce qu'il "
                        "vient de faire, et chacun continue à l'écran.")

    d.billet(
        "Écrivez les deux questions que vous poserez à votre prochain rendez-vous.",
        exemples=[
            "Des questions à vous, pas celles du dialogue.",
            "Commencez par : « J'ai deux questions avant de partir. »",
        ],
        notes="Ramasser et relire : les questions écrites par les élèves sont souvent "
              "meilleures que celles du module, et valent d'être lues au groupe en E1.")

    return d.save(dossier)
