# -*- coding: utf-8 -*-
"""C2 · L'éditorial, pièce par pièce
Bloc C « Défi 2 · L'éditorial et sa thèse » · couleur teal · 75 min.
Source : exercice `t2edito` (type `texte`, l'éditorial de Wilfrid Chamberland
dans Le Courant de la Rive) et sa mini-leçon `t2edito`.
Intention du programme : comprendre un article d'opinion, une chronique, un
éditorial ou un blogue.
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n8-actualite' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='C2', section='teal',
        titre="Un éditorial n'est pas une suite d'idées, c'est un bâtiment",
        chapeau="Sept pièces, toujours les mêmes : accroche, thèse, "
                "arguments, concession, réfutation, objection anticipée, "
                "conclusion et appel. Qui les connaît lit trois fois plus "
                "vite et répond beaucoup mieux.",
        duree='75 minutes')

    d.titre(notes="Distribuer l'éditorial sur papier : le texte se travaille au "
                  "crayon, pas à l'écran. Chaque élève découpe son exemplaire en "
                  "pièces au fil de la séance ; l'exercice interactif reprendra le "
                  "même geste en cliquant dans le texte.")

    d.objectifs([
        "reconnaître les sept pièces d'un texte d'opinion ;",
        "trouver la thèse et vérifier qu'on peut en être en désaccord ;",
        "repérer la concession et la réfutation qui la suit ;",
        "lire l'appel en premier, pour savoir ce que l'auteur veut obtenir.",
    ], notes="Le quatrième est une méthode de lecture, pas une notion : le faire "
             "essayer tout de suite, avant même la première lecture complète.")

    d.declencheur(
        'Observation', "Par quoi commence-t-on la lecture d'un texte d'opinion ?",
        image=IMG + 'hotel-de-ville.jpg',
        pistes=[
            "Par le début, comme un roman ? Par le titre ? Par la fin ?",
            "Que demande la dernière phrase de cet éditorial, et à qui ?",
            "Maintenant, cherchez la thèse. Est-elle plus facile à trouver ?",
            "Qu'est-ce que l'auteur voulait obtenir en écrivant ce texte ?",
        ],
        notes="Faire lire l'appel d'abord, la thèse ensuite. L'ordre est délibéré : "
              "l'appel révèle le but du texte, et donc comment lire tout le reste. "
              "Ici, l'appel demande d'aller à l'assemblée plutôt que de signer.")

    d.regle("La thèse est une phrase avec laquelle on peut être en désaccord",
            "Le conseil a eu raison d'autoriser la cession du boisé, et il "
            "fallait le faire maintenant.",
            precision="C'est le test, et il est imparable : une phrase que personne "
                      "ne pourrait contester n'est pas une thèse, c'est un constat. "
                      "Notez aussi ce que la thèse contient en plus de l'idée — ici, "
                      "le mot « maintenant » ajoute l'urgence, qui devra être "
                      "défendue séparément.",
            notes="Diapositive à photographier. La thèse se trouve presque toujours à "
                  "la fin du premier paragraphe ou au début du deuxième. Faire "
                  "vérifier sur l'éditorial distribué.")

    d.cartes('Analyse', "Quatre pièces à reconnaître dans ce texte", [
        ("L'accroche",
         "« Trois logements libres sur mille. » Un chiffre brutal qui donne "
         "envie de lire, et qui ne démontre rien. On peut la retirer sans "
         "rien perdre au raisonnement : c'est à cela qu'on la reconnaît."),
        ("La concession",
         "« Il est vrai que le conseil a voté quatre jours après avoir reçu "
         "l'évaluation. » L'auteur donne raison à l'autre camp sur un point "
         "réel. Elle désarme l'objection avant qu'on la pose."),
        ("La réfutation",
         "« Mais aucune de ces deux maladresses ne rend le projet moins "
         "nécessaire. » Elle suit toujours la concession. Une concession "
         "sans réfutation est un abandon ; une réfutation sans concession "
         "est un cri."),
        ("L'objection anticipée",
         "« On nous dira que le terrain derrière l'aréna ferait aussi bien "
         "l'affaire. » L'auteur formule lui-même l'argument adverse — celui "
         "qu'il a choisi. C'est efficace et un peu déloyal."),
    ], notes="Faire surligner les quatre passages dans l'exemplaire papier, par "
             "groupes de deux, en dix minutes. Les couleurs importent peu ; ce qui "
             "compte est de pouvoir nommer la fonction de chaque passage.")

    d.tableau('Analyse', "Les sept pièces, dans l'ordre habituel",
              ['La pièce', 'Ce qu\'elle fait'],
              [["l'accroche", "donne envie de lire, sans rien démontrer"],
               ["la thèse", "l'idée à faire accepter, en une phrase discutable"],
               ["les arguments", "ce qui la soutient, idéalement des faits vérifiables"],
               ["la concession", "donne raison à l'autre camp sur un point"],
               ["la réfutation", "répond à la concession sans la nier"],
               ["l'objection anticipée", "formule l'argument adverse pour y répondre d'avance"],
               ["la conclusion et l'appel", "résume, puis demande une action à quelqu'un de précis"]],
              cle=0,
              notes="Diapositive à photographier. C'est aussi le plan que l'élève "
                    "suivra pour écrire sa lettre au bloc E : on apprend d'abord à "
                    "démonter. Ne pas le dire tout de suite, mais y revenir en E1.")

    d.pratique('Pratique 1 de 2', "Quel passage remplit cette fonction ?",
               "Retrouvez dans l'éditorial le passage qui répond.", [
        ("Quel passage sert d'accroche, sans rien démontrer ?", "trois logements libres sur mille"),
        ("Quel passage énonce la thèse ?", "le conseil a eu raison, et il fallait le faire maintenant"),
        ("Quel argument repose sur un chiffre du marché du logement ?", "le taux de zéro virgule trois pour cent"),
        ("Quel argument répond d'avance à qui doute du promoteur ?", "la pénalité de deux millions au règlement"),
        ("Quel passage est la concession ?", "il est vrai que le conseil a voté quatre jours après"),
        ("Quel passage est la réfutation qui la suit ?", "mais cela ne rend pas le projet moins nécessaire"),
        ("Quel passage est l'appel, adressé à quelqu'un de précis ?", "aux personnes qui hésitent : allez à l'assemblée"),
    ], corrige=True,
       notes="Exercice de repérage : la réponse est le passage du texte, pas une "
             "reformulation. C'est exactement ce que fait l'exercice interactif "
             "`t2edito`, où l'élève arme une question puis clique le passage.")

    d.pratique('Pratique 2 de 2', "Argument solide ou argument faible ?",
               "Dites sur quoi chaque phrase s'appuie.", [
        ("Le taux d'inoccupation est le plus bas jamais mesuré ici.", "solide - un chiffre vérifiable"),
        ("Tout le monde sait qu'il faut construire.", "faible - une évidence supposée"),
        ("Les logements sont inscrits au règlement avec une pénalité.", "solide - un document"),
        ("Le comité est composé de propriétaires aisés.", "faible - on vise la personne"),
        ("Le terrain coûtait onze mille dollars par année.", "solide - un montant"),
        ("C'est ce projet-là ou rien.", "faible - une fausse alternative"),
    ], corrige=True,
       notes="Les trois faiblesses sont celles de la mini-leçon : l'argument "
             "d'évidence, l'attaque de la personne et la fausse alternative. Insister "
             "sur la dernière : cherchez toujours la troisième voie, elle existe "
             "presque toujours et souvent elle a été écartée sans étude.")

    d.piege('Piège', "Attaquer tout le texte à la fois",
            "Viser la pièce faible",
            "Un texte d'opinion se conteste par un seul endroit, et le "
            "meilleur est l'objection anticipée : montrez que l'objection "
            "réelle n'était pas celle à laquelle l'auteur a répondu. "
            "Contester les sept pièces en même temps donne une réponse "
            "confuse, que personne ne lit jusqu'au bout.",
            notes="C'est le geste que la lettre du bloc E demandera. Le nommer ici "
                  "pour que l'élève lise déjà en cherchant l'endroit où il "
                  "répondrait.")

    d.billet(
        "Trouvez un texte d'opinion et découpez-le en pièces au crayon.",
        exemples=[
            "Marquez au moins la thèse, la concession et l'appel.",
            "Si vous ne trouvez pas la thèse, écrivez-le : c'est un renseignement aussi.",
        ],
        notes="Devoir. Un texte sans thèse repérable existe vraiment, et le "
              "constater vaut l'exercice : c'est souvent un texte qui n'a rien à "
              "demander.")

    return d.save(dossier)
