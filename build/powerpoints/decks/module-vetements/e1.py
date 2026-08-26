# -*- coding: utf-8 -*-
"""E1 · Je me lance.
Bloc E « Je me lance » · couleur teal · 75 min.
Source : production orale et écrite du module, jeu de rôle `vetement`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre='Je me lance',
        chapeau="Tout ce qui a été appris se rassemble ici : essayer, dire ce "
                "qui ne va pas, demander un avis, lire l'étiquette, échanger. "
                "Une production orale, une production écrite.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Prévoir des écouteurs : la production orale se "
                  "fait à l'ordinateur, chacun de son côté.")

    d.objectifs([
        "tenir une conversation complète en magasin ;",
        "employer les trois défis du module dans une même production ;",
        "écrire un court texte sur un achat de vêtement ;",
        "recevoir une correction et la relire.",
    ])

    d.cartes('Les trois défis, réunis', "Ce qui doit apparaître", [
        ("Défi 1 · la taille",
         "Dire ce qui ne va pas : degré + adjectif + endroit. « Il est un peu serré aux "
         "épaules. »"),
        ("Défi 2 · l'avis et l'étiquette",
         "Demander un avis, en donner un nuancé, poser la question de l'entretien."),
        ("Défi 3 · l'échange",
         "Demander un échange, présenter la facture, expliquer le motif."),
    ], notes="Diapo à photographier. C'est la grille de la production orale.")

    d.regle("Le jeu de rôle",
            "Trois cas, deux rôles.",
            precision="Dans l'activité interactive : le <b>manteau</b> (essayer et "
                      "choisir), les <b>bottes</b> (la pointure d'un enfant), l'<b>échange</b> "
                      "(au service à la clientèle). Vous choisissez d'être le "
                      "<b>client</b> ou le <b>conseiller</b> — faites les deux, ils "
                      "n'emploient pas les mêmes phrases.",
            notes="Six combinaisons en tout. Demander au moins deux tours, dont un dans "
                  "chaque rôle.")

    d.pratique('Production orale', "Ce qui est demandé",
               "Trois minutes, à l'ordinateur.", [
        ("Ouvrir", "saluer et dire ce que vous cherchez"),
        ("Décrire", "le vêtement, sa couleur, sa matière"),
        ("Dire le problème", "degré + adjectif + endroit"),
        ("Demander", "une autre taille, un avis, ou un échange"),
        ("Fermer", "remercier et conclure"),
    ], cols=1,
       notes="La correction par l'IA arrive tout de suite. Elle n'est pas conservée : "
             "l'élève la lit, la note, et recommence s'il le veut.")

    d.piege("Réciter au lieu de parler",
            "Apprendre le dialogue par cœur et le redire.",
            "Employer les structures avec ses propres mots.",
            "Un dialogue récité s'entend, et il ne prépare à rien : le vrai vendeur ne dira "
            "pas la réplique attendue. Les structures — « je voudrais », « il est trop… "
            "aux… », « je trouve que » — se réemploient ; les phrases entières, non.",
            notes="Rassurer : hésiter, se reprendre et chercher un mot est normal et n'est "
                  "pas pénalisé.")

    d.pratique('Production écrite', "Ce qui est demandé",
               "Une centaine de mots, dans l'activité.", [
        ("Le sujet", "un achat de vêtement, vrai ou inventé"),
        ("À employer", "deux couleurs accordées, une matière avec « en »"),
        ("À employer aussi", "une phrase d'opinion et une phrase de problème"),
        ("À vérifier", "l'adjectif après le nom, l'accord au féminin"),
    ], cols=1,
       notes="Le texte s'envoie par le bouton d'envoi : il arrive dans le portail de "
             "l'enseignante. La correction de l'IA, elle, reste privée.")

    d.tableau('Analyse', "Ce qui est regardé",
              ['Le critère', 'Ce qui compte'],
              [["La tâche", "les trois moments sont là"],
               ["Le vocabulaire", "les mots du module sont employés"],
               ["La langue", "accords, adjectif après le nom"],
               ["La clarté", "on comprend du premier coup"]],
              cle=3,
              note="La clarté passe avant la perfection : une phrase simple et juste vaut "
                   "mieux qu'une phrase compliquée et fausse.",
              notes="Diapo à photographier. Le dire avant que les élèves commencent.")

    d.cartes("Si vous bloquez", "Trois secours", [
        ("Les mini-leçons",
         "Six panneaux « Ouvrir la mini-leçon » dans l'activité, avec l'audio. Ils restent "
         "ouverts pendant la production."),
        ("Les cartes mémoire",
         "Quinze mots avec définition, exemple et image. Section « Je retiens des mots »."),
        ("Le bouton d'aide",
         "Il envoie un signal à l'enseignante avec le titre de l'exercice où vous êtes. "
         "Elle vient sans que vous ayez à lever la main."),
    ], notes="Montrer les trois à l'écran avant de lancer la production.")

    d.billet(
        "Notez ce que la correction vous a signalé.",
        exemples=[
            "Deux choses réussies, deux choses à travailler.",
            "Gardez la note : elle sert à la séance E2.",
        ],
        notes="La correction de l'IA n'est pas conservée par le système. Cette note est la "
              "seule trace qu'il en restera.")

    return d.save(dossier)
