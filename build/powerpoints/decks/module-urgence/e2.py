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

    d.vocabulaire('Vocabulaire · 1 de 3', "La blessure", [
        ("une brûlure", "Une blessure causée par la chaleur, le feu ou un liquide chaud."),
        ("une cloque", "Une petite poche de liquide sur la peau brûlée."),
        ("une plaie", "Une blessure ouverte sur la peau."),
        ("le deuxième degré", "Le niveau d'une brûlure avec des cloques."),
        ("une cicatrice", "La marque qui reste sur la peau après une blessure."),
        ("éclabousser", "Projeter un liquide en gouttes."),
    ], notes="Cacher la colonne de droite et faire donner les définitions par le groupe. "
             "Puis l'inverse.")

    d.vocabulaire('Vocabulaire · 2 de 3', "Les soins", [
        ("un pansement", "Ce qu'on pose sur une plaie pour la protéger."),
        ("désinfecter", "Nettoyer pour éliminer les microbes."),
        ("des points de suture", "Des fils pour refermer une plaie."),
        ("une radiographie", "Une image des os."),
        ("une prise de sang", "Un prélèvement pour analyser le sang."),
        ("une compresse stérile", "Un tissu propre pour couvrir une plaie."),
    ], notes="Faire produire une phrase complète avec chaque mot, au passé composé : "
             "cela révise les deux savoirs à la fois.")

    d.vocabulaire('Vocabulaire · 3 de 3', "L'hôpital et le travail", [
        ("Info-Santé", "Une ligne téléphonique, le 811, où une infirmière conseille."),
        ("l'urgence", "Le service de l'hôpital pour les cas qui ne peuvent pas attendre."),
        ("la salle d'attente", "L'endroit où les gens attendent leur tour."),
        ("un congé de maladie", "Des jours autorisés pour ne pas travailler quand on est blessé."),
        ("un accompagnateur", "La personne qui vient avec le patient."),
    ], notes="Vérifier une dernière fois que chacun a le 811 dans son téléphone. C'est le "
             "savoir le plus utile du module.")

    d.tableau('Révision · 1 de 2', "Les savoirs du module",
              ['Le savoir', 'La règle en une phrase', 'Séance'],
              [["u et ou", "les lèvres pareilles, la langue différente", "A2"],
               ["Le groupe du nom", "déterminant, nom, adjectif, accordés", "A4"],
               ["Le passé composé", "auxiliaire au présent + participe", "B2"],
               ["Les pronominaux", "toujours être, accord avec le sujet", "B3"],
               ["Les pronoms", "toujours devant le verbe conjugué", "C2"]],
              cle=0,
              notes="Faire retrouver la règle avant d'afficher la colonne du milieu. Ce "
                    "qui ne revient pas est ce qu'il faut retravailler.")

    d.tableau('Révision · 2 de 2', "Les savoirs du module, suite",
              ['Le savoir', 'La règle en une phrase', 'Séance'],
              [["L'appartenance", "le déterminant s'accorde avec l'objet", "C3"],
               ["La partie du corps", "l'article, pas le possessif", "C3"],
               ["La question polie", "le conditionnel change le rapport", "D2"],
               ["Le message", "nouvelles, souhait, offre concrète", "D2, E1"]],
              cle=0,
              note="Neuf savoirs pour un module. Chacun renvoie à une séance : c'est là "
                   "qu'il faut retourner si la règle ne revient pas.",
              notes="Insister sur la dernière colonne. Le module reste ouvert dans le "
                    "portail : chacun peut y revenir seul.")

    d.cartes('Les quatre gestes du module', "Ce qu'on sait faire maintenant", [
        ("Réagir dans les premières minutes",
         "De l'eau fraîche qui coule, quinze minutes. Retirer les bagues. Ne rien "
         "mettre d'autre sur la peau."),
        ("Appeler le bon numéro",
         "911 si la vie est en danger. 811 dans tous les cas de doute. Et l'adresse en "
         "premier, toujours."),
        ("Raconter ce qui est arrivé",
         "Ce que je faisais, ce qui est arrivé, ce que ça m'a fait, ce que j'ai fait. "
         "Au passé composé, dans l'ordre."),
        ("Demander poliment",
         "Pourriez-vous, auriez-vous, est-ce que je pourrais. À l'accueil, au "
         "téléphone, partout."),
    ], notes="Faire dire à chacun lequel des quatre lui paraît le plus solide, et lequel "
             "le moins. Personne ne doit répondre « tous ».")

    d.pratique('Bilan · 1 de 2', "Le vocabulaire, sans regarder",
               "Donnez le mot qui correspond à la définition.", [
        ("Une petite poche de liquide sur la peau brûlée.", "une cloque"),
        ("Des fils pour refermer une plaie.", "des points de suture"),
        ("Projeter un liquide en gouttes.", "éclabousser"),
        ("Nettoyer pour éliminer les microbes.", "désinfecter"),
        ("Le numéro d'Info-Santé.", "le 811"),
        ("Le numéro quand la vie est en danger.", "le 911"),
    ], corrige=True,
       notes="Exercice individuel, cahier fermé, cinq minutes. Corriger ensemble sans "
             "compter les points.")

    d.pratique('Bilan · 2 de 2', "Autoévaluation",
               "Pour chaque énoncé : je sais faire, presque, ou pas encore.", [
        ("Je sais quoi faire dans la première minute d'une brûlure.", "séances A1, C4"),
        ("Je sais choisir entre le 911 et le 811.", "séance A3"),
        ("Je peux raconter un accident au passé composé.", "séances B1, B2, B4"),
        ("Je peux dire « je me suis coupé le doigt » sans me tromper.", "séance B3"),
        ("Je peux poser une question polie à l'accueil.", "séance D2"),
        ("Je peux écrire un message à une personne blessée.", "séances D2, E1"),
    ], corrige=True,
       notes="La colonne de droite n'est pas une correction : c'est l'adresse où "
             "retourner. Le dire clairement au groupe.")

    d.billet(
        "Nommez un geste du module que vous avez déjà expliqué à quelqu'un d'autre.",
        exemples=[
            "À la maison, au travail, à un ami.",
            "S'il n'y en a aucun, nommez celui que vous expliquerez cette semaine.",
        ],
        notes="Fin du module. Un savoir de premiers soins qui se transmet vaut mieux "
              "qu'un savoir qui reste dans un cahier.")

    return d.save(dossier)
