# -*- coding: utf-8 -*-
"""E2 · Je retiens des mots.
Bloc E · couleur framboise (vocabulaire et bilan) · 60 min.
Source : les cartes mémoire du module, révision des savoirs, autoévaluation.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre='Je retiens des mots',
        chapeau="Dernière séance du module. On rassemble le vocabulaire, on revoit les "
                "savoirs, et chacun fait le point sur ce qu'il est maintenant capable "
                "de faire.",
        duree='60 minutes')

    d.titre(notes="Séance de bilan. Ton différent des autres : on ne présente rien de "
                  "nouveau. Laisser beaucoup de place aux questions restées en suspens.")

    d.objectifs([
        "revoir les mots essentiels du module ;",
        "retrouver les savoirs travaillés et savoir où chacun sert ;",
        "évaluer honnêtement ce que je suis capable de faire ;",
        "savoir où retourner chercher ce qui n'est pas encore acquis.",
    ])

    d.vocabulaire('Vocabulaire · 1 de 3', "Les quatre éléments", [
        ("l'émetteur", "La personne ou l'organisme qui envoie le message publicitaire."),
        ("le récepteur", "Les gens à qui le message publicitaire est destiné."),
        ("le canal", "Le moyen choisi pour diffuser le message."),
        ("le message", "Ce qu'on annonce : un événement, un produit ou un service."),
        ("un slogan", "Une phrase courte et facile à retenir, placée à la fin."),
    ], notes="Cacher la colonne de droite et faire donner les définitions. Ces cinq mots "
             "sont l'outil d'analyse de tout le module.")

    d.vocabulaire('Vocabulaire · 2 de 3', "Les supports", [
        ("une capsule", "Une très courte annonce diffusée à la radio."),
        ("une affiche", "Une feuille avec un message, placée pour être vue de tous."),
        ("une infolettre", "Un courriel envoyé régulièrement aux personnes inscrites."),
        ("un babillard", "Le panneau où l'on affiche les annonces d'un quartier."),
        ("une valeur morale", "Ce qu'une personne ou une société considère comme important."),
    ], notes="Faire nommer, pour chaque support, sa longueur habituelle. C'est le lien "
             "avec la séance A3.")

    d.vocabulaire('Vocabulaire · 3 de 3', "Les mots de la formation", [
        ("un préfixe", "Un élément placé devant un mot pour en changer le sens."),
        ("un suffixe", "Un élément placé à la fin d'un mot pour former un nouveau mot."),
        ("un bénévole", "Une personne qui donne son temps sans être payée."),
        ("réutiliser", "Utiliser une deuxième fois."),
        ("irréparable", "Qu'on ne peut pas réparer."),
    ], notes="Faire fabriquer trois mots de plus avec les préfixes et suffixes vus en B4 "
             "et B5. C'est la révision la plus efficace.")

    d.tableau('Révision · 1 de 2', "Les savoirs du module",
              ['Le savoir', 'La règle en une phrase', 'Séance'],
              [["L'accent d'insistance", "un seul mot, allongé, ton qui monte", "A2"],
               ["Les quatre éléments", "qui, à qui, quoi, par quel moyen", "A3"],
               ["Les valeurs", "elles sont suggérées, jamais nommées", "A4"],
               ["La comparaison", "plus ou moins, le mot, puis que", "B2"],
               ["Le slogan", "court, rythmé, il porte une idée", "B3"]],
              cle=0,
              notes="Faire retrouver la règle avant d'afficher la colonne du milieu. Ce "
                    "qui ne revient pas est ce qu'il faut retravailler.")

    d.tableau('Révision · 2 de 2', "Les savoirs du module, suite",
              ['Le savoir', 'La règle en une phrase', 'Séance'],
              [["Les préfixes", "devant le mot, ils changent le sens", "B4"],
               ["Les suffixes", "à la fin, ils changent la nature", "B5"],
               ["Général ou précis", "ce qui suit le nom décide", "C2"],
               ["La négation au passé", "ne et pas encadrent l'auxiliaire", "C3"]],
              cle=0, props=[0.28, 0.57, 0.15],
              note="Neuf savoirs pour un module. Chacun renvoie à une séance : c'est là "
                   "qu'il faut retourner.",
              notes="Insister sur la dernière colonne. Le module reste ouvert dans le "
                    "portail : chacun peut y revenir seul.")

    d.cartes('Les quatre gestes du module', "Ce qu'on sait faire maintenant", [
        ("Choisir son récepteur",
         "À qui je parle, exactement. C'est le premier geste, et il commande tous les "
         "autres."),
        ("Analyser une publicité",
         "Les quatre éléments, la valeur, le slogan. Et les trois niveaux : les faits, "
         "la promesse, la valeur."),
        ("Écrire court",
         "Trente secondes à la radio, quarante mots sur une affiche. Couper, jamais "
         "accélérer."),
        ("Dire à voix haute",
         "Un seul mot mis en avant, une pause avant le slogan, une fin nette."),
    ], notes="Faire dire à chacun lequel des quatre lui paraît le plus solide, et lequel "
             "le moins. Personne ne doit répondre « tous ».")

    d.pratique('Bilan · 1 de 2', "Le vocabulaire, sans regarder",
               "Donnez le mot qui correspond à la définition.", [
        ("Les gens à qui le message est destiné.", "le récepteur"),
        ("Le moyen choisi pour diffuser le message.", "le canal"),
        ("Une phrase courte, facile à retenir, à la fin.", "un slogan"),
        ("Un élément placé devant un mot.", "un préfixe"),
        ("Une très courte annonce à la radio.", "une capsule"),
        ("Une personne qui donne son temps sans être payée.", "un bénévole"),
    ], corrige=True,
       notes="Exercice individuel, cahier fermé, cinq minutes. Corriger ensemble sans "
             "compter les points.")

    d.pratique('Bilan · 2 de 2', "Autoévaluation",
               "Pour chaque énoncé : je sais faire, presque, ou pas encore.", [
        ("Je peux dire à qui une publicité s'adresse.", "séances A1, A3"),
        ("Je peux nommer la valeur d'une publicité.", "séance A4"),
        ("Je peux comparer deux publicités.", "séance B2"),
        ("Je peux écrire un slogan.", "séance B3"),
        ("Je peux fabriquer un mot avec un préfixe ou un suffixe.", "séances B4, B5"),
        ("Je peux écrire et dire une capsule de trente secondes.", "séance E1"),
    ], corrige=True,
       notes="La colonne de droite n'est pas une correction : c'est l'adresse où "
             "retourner. Le dire clairement au groupe.")

    d.billet(
        "Nommez une publicité que vous ne regardiez pas de la même façon avant ce module.",
        exemples=[
            "À la radio, dans l'autobus, sur un babillard, à la télévision.",
            "Une phrase pour dire ce que vous y voyez maintenant.",
        ],
        notes="Fin du module. Ces billets disent ce qui est vraiment passé de la classe "
              "à la vie — c'est le seul bilan qui compte.")

    return d.save(dossier)
