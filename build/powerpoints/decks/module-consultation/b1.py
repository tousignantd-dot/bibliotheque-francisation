# -*- coding: utf-8 -*-
"""B1 · Yannick au triage.
Bloc B · couleur acier (compréhension orale) · 75 min.
Source : dialogue `t1` et exercice `t1vf`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre='Yannick au triage',
        chapeau="Avant de voir la docteure, il faut passer par l'infirmière du triage. "
                "Sept questions, trois minutes, et c'est là que se décide le temps "
                "d'attente de toute la journée.",
        duree='75 minutes')

    d.titre(notes="Première séance du défi 1. Rappeler les trois mots écrits au tableau "
                  "en A1 : ENDROIT · DEPUIS QUAND · QUEL GESTE. Ils vont servir ici.")

    d.objectifs([
        "comprendre les questions que pose une infirmière au triage ;",
        "y répondre avec une information utile, pas seulement par oui ou non ;",
        "évaluer sa douleur sur une échelle de un à dix ;",
        "dire ce qu'on faisait quand la douleur est apparue.",
    ])

    d.cartes('Avant le dialogue', "À quoi sert le triage", [
        ("Ce n'est pas une consultation",
         "L'infirmière ne soigne pas et ne pose pas de diagnostic. Elle évalue la "
         "gravité pour décider qui passe en premier."),
        ("Elle décide de l'ordre",
         "Deux personnes arrivées en même temps ne passeront pas en même temps. Ce qui "
         "compte, c'est le risque, pas l'heure d'arrivée."),
        ("Elle est très rapide",
         "Trois minutes environ. C'est pour ça qu'une réponse précise vaut de l'or : "
         "il n'y a pas de temps pour dix questions de plus."),
        ("Elle prend des notes",
         "Ce que vous dites est écrit et lu par la docteure ensuite. Une information "
         "oubliée ici ne sera peut-être jamais demandée."),
    ], notes="La quatrième carte étonne toujours : les élèves croient qu'il faudra tout "
             "répéter au médecin. Non — ce qui est dit au triage est transmis.")

    d.dialogue('Dialogue · 1 de 2', "Qu'est-ce qui vous amène ce matin ?", [
        ("L'INFIRMIÈRE", "Bonjour, asseyez-vous. Qu'est-ce qui vous amène ce matin ?",
         False),
        ("YANNICK", "J'ai le genou droit enflé depuis cette nuit. Je travaille dans un "
                    "entrepôt et je soulève des boîtes toute la soirée.", True),
        ("L'INFIRMIÈRE", "Est-ce que vous vous êtes cogné ou tordu la jambe ?", False),
        ("YANNICK", "Je ne me souviens pas d'un coup précis. La douleur est arrivée peu "
                    "à peu.", True),
    ], consigne="Écoutez d'abord l'enregistrement, diapo masquée. Lisez ensuite.",
       notes="Passer l'audio du défi 1 avant d'afficher le texte. Faire compter combien "
             "d'informations Yannick donne dans sa première réponse : quatre (côté, "
             "état, moment, métier).")

    d.dialogue('Dialogue · 2 de 2', "Sur une échelle de un à dix", [
        ("L'INFIRMIÈRE", "Sur une échelle de un à dix, où se situe votre douleur ?",
         False),
        ("YANNICK", "Environ six quand je marche, deux quand je reste assis.", True),
        ("L'INFIRMIÈRE", "Très bien. Prenez ce numéro, la docteure Beaulieu va vous "
                         "appeler.", False),
    ], notes="La réponse de Yannick donne DEUX chiffres, selon la position. C'est ce qui "
             "fait la qualité de la réponse : la douleur n'est pas la même selon ce qu'on "
             "fait. Insister.")

    d.tableau('Analyse', "Les quatre questions du triage",
              ['La question', 'Ce qu\'elle cherche'],
              [["Qu'est-ce qui vous amène ?", "le problème, en une phrase"],
               ["Vous êtes-vous cogné ?", "un choc, ou une usure lente"],
               ["Depuis quand ?", "l'urgence de la situation"],
               ["De un à dix ?", "l'intensité, comparable d'un patient à l'autre"]],
              cle=0,
              note="Ces quatre questions reviennent partout : urgence, clinique, 811. "
                   "Les préparer une fois sert toute la vie.",
              notes="Faire écrire les quatre questions dans le cahier. Elles seront "
                    "réutilisées telles quelles en E1.")

    d.regle("L'échelle de la douleur",
            "Zéro, c'est aucune douleur. Dix, c'est la pire douleur imaginable.",
            precision="Il n'y a pas de bonne réponse : c'est votre douleur à vous. Mais "
                      "donnez un chiffre, même approximatif — « ça fait très mal » ne "
                      "peut pas être comparé, « sept sur dix » oui.",
            notes="Faire donner un chiffre par chaque élève pour une douleur qu'il a "
                  "déjà eue. Personne ne doit dire « je ne sais pas ».")

    d.cartes('Analyse', "Comment répondre mieux qu'un chiffre seul", [
        ("Donnez deux chiffres",
         "Un pour le repos, un pour le mouvement. « Six quand je marche, deux quand je "
         "reste assis. » L'écart entre les deux est une information."),
        ("Dites ce qui aggrave",
         "« Ça élance dès que je plie la jambe. » Le geste qui déclenche oriente le "
         "diagnostic mieux que l'intensité."),
        ("Dites ce qui soulage",
         "« C'est mieux quand je mets de la glace. » Si quelque chose soulage, le "
         "soignant veut le savoir."),
        ("Ne minimisez pas",
         "Beaucoup de gens disent « trois » par politesse. L'infirmière classe selon ce "
         "chiffre : minimiser, c'est attendre plus longtemps."),
    ], notes="La quatrième carte est culturelle et vaut la discussion. Dans plusieurs "
             "pays, se plaindre est mal vu ; ici, le chiffre sert à trier, pas à juger.")

    d.pratique('Pratique · 1 de 3', 'Vrai ou faux — au triage',
               "Répondez sans relire le dialogue.", [
        ("C'est le genou gauche de Yannick qui est enflé.", "FAUX — le droit"),
        ("Yannick soulève des boîtes dans un entrepôt.", "VRAI"),
        ("Il se souvient précisément du coup qu'il a reçu.", "FAUX — aucun coup précis"),
        ("La douleur est arrivée peu à peu.", "VRAI"),
        ("L'infirmière demande d'évaluer la douleur de un à dix.", "VRAI"),
        ("La douleur est plus forte quand il est assis.", "FAUX — quand il marche"),
        ("L'infirmière lui remet un numéro.", "VRAI"),
        ("C'est le docteur Nadeau qui va le recevoir.", "FAUX — la docteure Beaulieu"),
    ], corrige=True,
       notes="La sixième est celle qui trompe : les deux chiffres sont donnés dans la "
             "même phrase, et l'ordre inverse l'attention.")

    d.pratique('Pratique · 2 de 3', 'Répondez à la question du triage',
               "Une phrase complète, avec au moins deux informations.", [
        ("Qu'est-ce qui vous amène ?",
         "J'ai la cheville droite enflée depuis hier soir."),
        ("Est-ce que vous vous êtes cogné ?",
         "Non, je me suis tordu le pied dans l'escalier."),
        ("Depuis quand avez-vous mal ?",
         "Depuis hier soir, après le travail."),
        ("Sur une échelle de un à dix ?",
         "Sept quand je marche, trois quand je suis assis."),
    ], corrige=True,
       notes="Les réponses proposées sont des modèles, pas des corrigés : accepter toute "
             "réponse contenant deux informations. Faire jouer la scène à deux.")

    d.pratique('Pratique · 3 de 3', "Trouvez l'information manquante",
               "Chaque réponse est incomplète. Qu'est-ce qui manque ?", [
        ("« J'ai mal. »", "l'endroit, le côté, depuis quand"),
        ("« J'ai mal au genou. »", "le côté et depuis quand"),
        ("« J'ai mal au genou droit. »", "depuis quand"),
        ("« Ça fait très mal. »", "un chiffre de un à dix"),
        ("« J'ai mal depuis longtemps. »", "l'endroit, et une durée précise"),
    ], corrige=True,
       notes="Exercice en escalier : chaque réponse est un peu meilleure que la "
             "précédente. Faire remarquer qu'on n'arrive à une réponse complète qu'à "
             "la fin.")

    d.piege('Le piège de la politesse',
            "Ça va, ce n'est pas si grave.",
            "Six sur dix quand je marche.",
            "Répondre modestement au triage n'est pas de la politesse : c'est une "
            "information fausse. L'infirmière classe les patients avec ce chiffre. "
            "Dire moins que la vérité, c'est passer après quelqu'un qui souffre moins.",
            notes="Point culturel important. Le dire clairement : ici, décrire sa douleur "
                  "précisément n'est pas se plaindre, c'est aider le personnel à "
                  "travailler.")

    d.billet(
        "Écrivez la réponse que vous donneriez à « Qu'est-ce qui vous amène ? »",
        exemples=[
            "Trois informations minimum : l'endroit avec le côté, depuis quand, ce qui "
            "aggrave.",
            "Ajoutez votre chiffre sur dix, au repos et en mouvement.",
        ],
        notes="Ramasser. Ces billets seront relus en E1, où chacun devra dire la même "
              "chose à voix haute, au téléphone.")

    return d.save(dossier)
