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
                "savoirs travaillés, et chacun fait le point sur ce qu'il est maintenant "
                "capable de faire.",
        duree='60 minutes')

    d.titre(notes="Séance de bilan. Ton différent des autres : on ne présente rien de "
                  "nouveau. Laisser beaucoup de place aux questions restées en suspens.")

    d.objectifs([
        "revoir les mots essentiels du module ;",
        "retrouver les savoirs travaillés et savoir où chacun sert ;",
        "évaluer honnêtement ce que je suis capable de faire ;",
        "savoir où retourner chercher ce qui n'est pas encore acquis.",
    ])

    d.vocabulaire('Vocabulaire · 1 de 3', "Le corps et la douleur", [
        ("enflé", "Qui a augmenté de volume à cause d'une blessure."),
        ("élancer", "Faire une douleur vive et répétée, par à-coups."),
        ("une inflammation", "Une réaction du corps qui cause douleur et enflure."),
        ("un tendon", "La partie qui attache un muscle à un os."),
        ("une articulation", "L'endroit où deux os se rejoignent et se plient."),
        ("un ligament", "Ce qui tient deux os ensemble à une articulation."),
    ], notes="Cacher la colonne de droite et faire donner les définitions par le groupe. "
             "Puis l'inverse : cacher la gauche et faire retrouver les mots.")

    d.vocabulaire('Vocabulaire · 2 de 3', "Le réseau de la santé", [
        ("une clinique sans rendez-vous", "Une clinique où on consulte sans avoir réservé."),
        ("le triage", "L'étape où une infirmière évalue la gravité des cas."),
        ("une carte d'assurance maladie", "La carte qui donne accès aux soins gratuits."),
        ("référer", "Envoyer un patient vers un autre professionnel."),
        ("la physiothérapie", "Des soins avec des exercices pour retrouver ses mouvements."),
    ], notes="Vérifier que chacun sait ce qu'est le 811 et l'a noté dans son téléphone. "
             "C'est le savoir le plus utile du module.")

    d.vocabulaire('Vocabulaire · 3 de 3', "Les médicaments et les papiers", [
        ("une ordonnance", "Le papier du médecin pour obtenir un médicament."),
        ("un billet de repos", "Un papier du médecin qui autorise à ne pas travailler."),
        ("un comprimé", "Un médicament solide, en petit disque, à avaler."),
        ("un traitement", "L'ensemble des doses à prendre, du début à la fin."),
        ("un effet secondaire", "Un effet non désiré causé par un médicament."),
    ], notes="Faire produire une phrase complète avec chaque mot, en lien avec une "
             "situation réelle de l'élève.")

    d.tableau('Révision · 1 de 2', "Les savoirs du module",
              ['Le savoir', 'La règle en une phrase', 'Séance'],
              [["Les sons nasaux", "trois sons, trois positions de bouche", "A2"],
               ["La cause", "ce qui suit décide du mot", "B2"],
               ["La question", "est-ce que, ou un mot au début", "B3"],
               ["Le présent", "on regarde le sujet, pas le son", "C2"],
               ["La négation", "deux morceaux autour du verbe", "C3"]],
              cle=0,
              notes="Faire retrouver la règle avant d'afficher la colonne du milieu. "
                    "Ce qui ne revient pas est ce qu'il faut retravailler.")

    d.tableau('Révision · 2 de 2', "Les savoirs du module, suite",
              ['Le savoir', 'La règle en une phrase', 'Séance'],
              [["Le pluriel", "s partout, sauf -al et -eau", "D2"],
               ["L'obligation", "devoir désigne, il faut ne désigne pas", "D2"],
               ["Le formulaire", "des groupes de mots, pas des phrases", "D1"],
               ["Le courriel", "objet, nom, numéro, depuis quand", "E1"]],
              cle=0,
              note="Huit savoirs pour un module. Chacun renvoie à une séance : c'est là "
                   "qu'il faut retourner si la règle ne revient pas.",
              notes="Insister sur la dernière colonne. Le module reste ouvert dans le "
                    "portail : chacun peut y revenir seul.")

    d.cartes('Les quatre gestes du module', "Ce qu'on sait faire maintenant", [
        ("Choisir la bonne porte",
         "Urgence, clinique sans rendez-vous, médecin de famille, ou 811. La question "
         "n'est pas « est-ce que ça fait mal » mais « est-ce que ça peut s'aggraver »."),
        ("Décrire une douleur",
         "L'endroit avec le côté, depuis quand, ce qui aggrave, le chiffre sur dix. "
         "Quatre informations, trente secondes."),
        ("Comprendre les consignes",
         "Le diagnostic, l'arrêt de travail, la référence, les soins à la maison. Et "
         "les chiffres : vingt minutes, trois fois, quatre jours."),
        ("Demander par écrit",
         "Un courriel avec un objet clair, votre nom, votre numéro, et depuis quand ça "
         "dure."),
    ], notes="Faire dire à chacun lequel des quatre gestes lui paraît le plus solide, et "
             "lequel le moins. Personne ne doit répondre « tous ».")

    d.pratique('Bilan · 1 de 2', "Le vocabulaire, sans regarder",
               "Donnez le mot qui correspond à la définition.", [
        ("L'étape où une infirmière évalue la gravité des cas.", "le triage"),
        ("Un papier du médecin pour obtenir un médicament.", "une ordonnance"),
        ("Faire une douleur vive et répétée.", "élancer"),
        ("Envoyer un patient vers un autre professionnel.", "référer"),
        ("La partie qui attache un muscle à un os.", "un tendon"),
        ("Le numéro à composer quand on ne sait pas quoi faire.", "le 811"),
    ], corrige=True,
       notes="Exercice individuel, cahier fermé, cinq minutes. Corriger ensemble sans "
             "compter les points.")

    d.pratique('Bilan · 2 de 2', "Autoévaluation",
               "Pour chaque énoncé : je sais faire, presque, ou pas encore.", [
        ("Je peux dire où j'ai mal, de quel côté et depuis quand.", "séances A1, A3, B4"),
        ("Je peux choisir entre l'urgence et la clinique.", "séance A4"),
        ("Je peux expliquer pourquoi je consulte, avec « parce que ».", "séance B2"),
        ("Je peux poser une question au médecin.", "séance B3"),
        ("Je peux lire une étiquette de médicament.", "séance C4"),
        ("Je peux écrire un courriel pour un rendez-vous.", "séance E1"),
    ], corrige=True,
       notes="La colonne de droite n'est pas une correction : c'est l'adresse où "
             "retourner. Le dire clairement au groupe.")

    d.billet(
        "Nommez un mot du module que vous avez déjà employé en dehors de la classe.",
        exemples=[
            "À la pharmacie, chez le médecin, au téléphone, avec un collègue.",
            "S'il n'y en a aucun, nommez celui que vous emploierez cette semaine.",
        ],
        notes="Fin du module. Ces billets valent mieux qu'un examen : ils disent ce qui "
              "est vraiment passé de la classe à la vie.")

    return d.save(dossier)
