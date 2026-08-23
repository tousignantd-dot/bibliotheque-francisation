# -*- coding: utf-8 -*-
"""C3 · Lire une offre d'emploi pour décider
Bloc C « Défi 2 » · couleur ambre · 75 min.
Source : exercice `t2offre` (type `texte`) et sa mini-leçon. Deuxième des
trois lectures du module, et d'un genre différent de celle de C2 : on ne
prélève plus un fait, on décide de son admissibilité.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="Exigé, atout, et les trois mots qui ouvrent une porte",
        chapeau="Une majorité de candidats renoncent devant une exigence "
                "qu'ils croient absolue. Or presque toutes les exigences "
                "portent une porte, et elle tient en trois mots.",
        duree='75 minutes')

    d.titre(notes="Séance la plus utile du module pour la vie réelle. Beaucoup "
                  "d'élèves ont déjà renoncé à une offre cette année : demander qui, "
                  "et pourquoi. La réponse ouvre la séance toute seule.")

    d.objectifs([
        "distinguer ce qui est exigé de ce qui est un atout ;",
        "repérer la formule qui ouvre une exigence ;",
        "lire les conditions aussi attentivement que les exigences ;",
        "recopier le titre du poste mot pour mot.",
    ], notes="Le deuxième objectif est celui qui change une vie de recherche "
             "d'emploi. Le poser en grand, et y revenir trois fois.")

    d.declencheur(
        'Discussion', "À quelle offre avez-vous renoncé cette année, et pourquoi ?",
        pistes=[
            "Il manquait combien d'années d'expérience ?",
            "Le mot exact de l'annonce était-il « exigé » ou « atout » ?",
            "Y avait-il « ou l'équivalent » quelque part ?",
            "Qui a décidé que vous n'étiez pas admissible : l'employeur, ou vous ?",
        ],
        notes="La dernière question est brutale et elle est juste. Ne pas l'adoucir : "
              "c'est le sujet de la séance.")

    d.regle("Exigé élimine, atout distingue",
            "Ce qui est exigé vous écarte si vous ne l'avez pas. Ce qui est "
            "un atout vous distingue si vous l'avez, et ne vous coûte rien "
            "sinon. Ne renoncez jamais à une offre faute d'un atout.",
            precision="Un dossier sans aucun des atouts mais avec toutes les exigences "
                      "passe le tri. L'inverse ne le passe pas. Les deux mots ne "
                      "pèsent pas pareil, et l'annonce ne le dit nulle part.",
            notes="Diapositive à photographier. Faire relire les annonces apportées en "
                  "devoir avec ce seul filtre : combien d'exigences, combien d'atouts.")

    d.cartes('Analyse', "Les trois mots qui ouvrent une exigence", [
        ("« ou l'équivalent »",
         "Cinq années en supervision, ou l'équivalent. L'employeur sait qu'il "
         "ne trouvera pas le profil idéal, et il l'écrit exprès."),
        ("« ou expérience jugée pertinente »",
         "Diplôme collégial, ou expérience jugée pertinente. C'est à "
         "l'employeur de juger, pas à vous de vous éliminer d'avance."),
        ("« ou toute expérience équivalente »",
         "La formule de l'offre de Boréalis, et c'est par cette porte-là que "
         "Shirin passe avec ses onze années de Téhéran."),
        ("Comment franchir la porte",
         "Pas en affirmant. Avec une taille d'équipe, un nombre d'années et "
         "un résultat : vingt-deux personnes, trois lignes, onze ans."),
    ], notes="Faire chercher la formule dans chaque annonce apportée. Quand elle n'y "
             "est pas, c'est un renseignement aussi : l'exigence est ferme.")

    d.pratique('Pratique 1 de 2', "Où est-ce écrit ?",
               "Retrouvez dans l'offre le passage qui répond.", [
        ("Quel est le titre exact du poste ?", "superviseure ou superviseur de production, quart de soir"),
        ("Quel est l'horaire précis du quart ?", "du lundi au vendredi, de quinze heures à vingt-trois heures trente"),
        ("Quelle responsabilité ne figure pas dans le titre ?", "participer au recrutement de l'équipe"),
        ("Quelle porte l'exigence d'expérience laisse-t-elle ?", "ou toute expérience jugée équivalente"),
        ("Combien de temps dure la période d'essai ?", "six mois"),
        ("Sur quoi le congé annuel est-il calculé ?", "la Loi sur les normes du travail"),
    ], corrige=True,
       notes="Exercice de repérage. Le troisième est le plus riche : une "
             "responsabilité absente du titre change complètement le poste, et c'est "
             "ce que l'appel de présélection avait déjà révélé.")

    d.tableau('Analyse', "Huit formules, et ce qu'elles cachent",
              ['Ce qui est écrit', 'Ce que cela veut dire'],
              [["« ou toute expérience jugée équivalente »",
                "la porte : à vous de démontrer l'équivalence"],
               ["« capacité démontrée à »",
                "il faudra un exemple précis, pas une affirmation"],
               ["« selon l'échelle en vigueur »",
                "le salaire n'est pas dit : question à poser"],
               ["« participer au recrutement »",
                "une responsabilité absente du titre"],
               ["« selon la Loi sur les normes du travail »",
                "le minimum légal, rien de plus"]],
              cle=0,
              notes="Diapositive à photographier. La dernière ligne mérite une "
                    "explication : deux semaines de congé après un an de service "
                    "continu, trois après trois ans, chez le même employeur.")

    d.regle("Le congé annuel selon la loi, c'est le minimum",
            "Deux semaines après un an de service continu, trois semaines "
            "après trois ans. Le service continu se compte chez un même "
            "employeur, sans interruption.",
            precision="Une expérience acquise ailleurs, même de vingt ans, ne compte "
                      "jamais dans le service continu. Un employeur peut en revanche "
                      "accorder davantage par contrat, et cela se demande — c'est "
                      "exactement ce qui n'est pas affiché.",
            notes="Diapositive à photographier. Fait vérifié auprès de la CNESST. C'est "
                  "aussi une des trois choses qui se négocient au défi 3, avec "
                  "l'échelon et la formation.")

    d.pratique('Pratique 2 de 2', "Postuler ou non ?",
               "Dites si le dossier passe le tri.", [
        ("Il manque un atout, toutes les exigences sont là.", "postuler - un atout n'élimine pas"),
        ("Trois ans d'expérience au lieu de cinq, avec « ou l'équivalent ».", "postuler - la porte est ouverte"),
        ("Trois ans au lieu de cinq, sans aucune formule d'ouverture.", "le tri sera serré, mais l'appel reste possible"),
        ("Aucune disponibilité pour le quart demandé.", "ne pas postuler - la disponibilité est une exigence réelle"),
    ], corrige=True,
       notes="Le troisième cas n'a pas de réponse tranchée, et c'est voulu. Un appel "
             "avant de postuler règle la question en trois minutes.")

    d.billet(
        "Reprenez l'offre de votre devoir et faites-en deux colonnes.",
        exemples=[
            "À gauche ce qui est exigé, à droite ce qui est un atout.",
            "Soulignez toute formule d'ouverture que vous trouvez.",
        ],
        notes="Devoir. Le tableau se relit en trois minutes au début de C4, et il "
              "montre presque toujours que la colonne de gauche est plus courte que "
              "l'élève ne le croyait.")

    return d.save(dossier)
