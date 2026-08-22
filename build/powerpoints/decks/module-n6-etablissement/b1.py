# -*- coding: utf-8 -*-
"""B1 · Une heure avec le conseiller d'orientation
Bloc B « Défi 1 » · couleur acier · 75 min. Compréhension orale.
Source : dialogue `t1`, exercice `t1vf` et son bandeau de savoir.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Une heure avec le conseiller d'orientation",
        chapeau="Un entretien d'orientation n'est pas une série de questions "
                "et de réponses : c'est un fil. Perdre le fil ici ne coûte "
                "pas un mot, ça coûte une année.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc B. Reprendre au tableau la phrase de A1 — « ce "
                  "qui se dit au comptoir ne compte pas » — et annoncer que "
                  "l'entretien d'aujourd'hui, lui, produira des dates.")

    d.objectifs([
        "suivre un entretien de vingt et une répliques sans en perdre le fil ;",
        "nommer les trois voies d'entrée d'un programme professionnel ;",
        "distinguer ce qui remplace un préalable de ce qui n'en remplace aucun ;",
        "employer les cinq mots de la démarche avec leur article.",
    ], notes="Le troisième objectif est le plus important et le plus douloureux : "
             "les années de travail à l'étranger ne remplacent aucun préalable. Le "
             "dire clairement, puis dire tout de suite à quoi elles servent.")

    d.declencheur(
        'Observation', "Qu'est-ce que vous faisiez avant d'arriver ici ?",
        pistes=[
            "Est-ce que vous faites le même travail aujourd'hui ?",
            "Avez-vous déjà demandé si vos années comptaient ?",
            "Qu'est-ce qu'on vous a répondu ?",
        ],
        notes="Question délicate et essentielle. Laisser parler sans commenter. "
              "Beaucoup d'élèves ont reçu des réponses contradictoires : la séance "
              "va en donner une seule, précise et vérifiable.")

    d.dialogue('Dialogue · 1 de 3', "Je ne sais pas quoi faire de mes années", [
        ("PASCAL", "Entrez, assoyez-vous. J'ai lu votre demande : vous cherchez à savoir quels préalables il vous manque. C'est déjà plus clair que la moitié de ce que je reçois.", True),
        ("BINTOU", "Merci. Je me demande surtout par où commencer. J'ai travaillé six ans dans une pharmacie à Bamako.", True),
        ("PASCAL", "Et vous aimeriez le refaire.", True),
        ("BINTOU", "J'y pense tous les soirs. Mais je ne sais pas quoi faire de mes années là-bas. Personne ne me dit si ça compte ou si ça ne compte pas.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Faire remarquer « j'y pense tous les soirs » : le « y » renvoie à la "
             "phrase d'avant. C'est le sujet entier de B3, annoncé ici sans le "
             "nommer.")

    d.dialogue('Dialogue · 2 de 3', "Trois chemins", [
        ("PASCAL", "Trois chemins. Le premier : un diplôme d'études secondaires, ou son équivalent reconnu.", True),
        ("PASCAL", "Le deuxième : avoir seize ans au trente septembre et les unités de quatrième secondaire en langue d'enseignement, en langue seconde et en mathématiques.", True),
        ("PASCAL", "Le troisième, celui qui vous concerne : avoir dix-huit ans et réussir le test de développement général, plus les préalables particuliers du programme.", True),
        ("BINTOU", "Ça fait beaucoup de mots. Le test, il remplace le diplôme ?", True),
    ], notes="Trois répliques de suite pour le même locuteur : c'est volontaire, un "
             "conseiller énumère. Arrêter après chacune et faire compter sur les "
             "doigts. Ces trois voies sont vérifiées et exactes.")

    d.dialogue('Dialogue · 3 de 3', "On vous l'a mal dit", [
        ("PASCAL", "Non, et c'est la confusion la plus fréquente. Le test de développement général ouvre la porte d'un programme professionnel, rien d'autre.", True),
        ("BINTOU", "J'ai aussi un papier du ministère de l'Immigration. On m'a dit que c'était une équivalence.", True),
        ("PASCAL", "On vous l'a mal dit, et ça arrive chaque semaine. Ce document est un avis d'expert : il dit à quel niveau d'ici vos études de là-bas se comparent.", True),
        ("PASCAL", "Ce n'est pas une équivalence de diplôme, ça ne remplace pas un permis, et ça ne garantit l'admission à aucun programme. Gardez-le, mais ne bâtissez pas votre année dessus.", True),
    ], notes="Le point le plus important du module. Le redire soi-même après "
             "l'écoute, lentement. Plusieurs élèves du groupe auront ce document et "
             "croiront le contraire depuis des mois.")

    d.tableau('Analyse', "Trois voies vers un programme professionnel",
              ['La voie', 'Ce qu\'elle demande'],
              [["Par le diplôme", "un diplôme d'études secondaires ou son équivalent reconnu"],
               ["Par les unités", "seize ans au 30 septembre et les unités de 4e secondaire"],
               ["Par le test", "dix-huit ans, le test de développement général, les préalables du programme"]],
              cle=0,
              note="Ces trois voies sont celles du programme réel. La troisième est celle de la plupart des adultes en francisation.",
              notes="Diapositive à photographier. Faire situer chaque élève dans une "
                    "des trois voies : c'est le moment le plus utile de la séance.")

    d.piege('Vocabulaire',
            "le test de développement général donne une équivalence de secondaire",
            "il ouvre la porte d'un programme professionnel, et rien d'autre",
            "Deux tests existent et se confondent chaque semaine. Le test de "
            "développement général ouvre un programme professionnel quand les "
            "préalables particuliers sont réussis. C'est l'autre — le test "
            "d'équivalence de niveau de scolarité, sept épreuves dont deux en "
            "français — qui mène à une attestation valant une cinquième "
            "secondaire.",
            notes="Écrire les deux noms au tableau, l'un sous l'autre, et les y "
                  "laisser jusqu'à la fin du bloc. C'est une confusion qui coûte des "
                  "mois d'inscription au mauvais endroit.")

    d.vocabulaire('Vocabulaire', "Les cinq mots de la démarche", [
        ("un programme d'études", "L'ensemble organisé des cours qui mènent à un diplôme précis."),
        ("un préalable", "Le cours ou le niveau qu'il faut avoir réussi avant d'être admis."),
        ("la formation professionnelle", "L'enseignement qui prépare à un métier et se termine par un diplôme d'État."),
        ("une évaluation comparative", "L'avis d'expert qui dit à quel niveau d'ici se comparent des études faites ailleurs."),
        ("la reconnaissance des acquis", "La démarche qui fait reconnaître ce qu'une personne sait déjà faire."),
    ], notes="Insister sur l'article de « la formation professionnelle » et de « la "
             "reconnaissance des acquis » : le défini, parce qu'il n'y en a qu'une.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après l'entretien de Bintou et de Pascal.", [
        ("Bintou a travaillé six ans dans une pharmacie à Bamako.", "vrai"),
        ("Le test de développement général donne une équivalence de secondaire.", "faux - il ouvre un programme professionnel"),
        ("Les six années de pharmacie remplacent un préalable.", "faux - elles servent ailleurs"),
        ("L'évaluation comparative garantit l'admission à un programme.", "faux - elle ne garantit rien"),
        ("Pascal conseille de terminer la francisation avant tout le reste.", "vrai"),
        ("Un échec au test ferme définitivement la porte.", "faux - on le reprend"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Terminer sur le "
             "dernier item, qui est le seul consolant, et le laisser affiché.")

    d.billet(
        "Dans quelle voie es-tu, et qu'est-ce qu'il te manque ?",
        exemples=[
            "Une ou deux phrases suffisent.",
            "Si tu ne le sais pas encore, écris la question que tu poserais.",
        ],
        notes="Cinq minutes. Ramasser : les réponses disent qui a besoin d'un vrai "
              "rendez-vous d'orientation, et il y en a toujours plus qu'on ne croit.")

    return d.save(dossier)
