# -*- coding: utf-8 -*-
"""E1 · Je me lance.
Bloc E « Je me lance » · couleur teal · 75 min.
Source : production orale et écrite du module, jeu de rôle `allees`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre='Je me lance',
        chapeau="Tout ce qui a été appris se rassemble : demander où c'est, "
                "faire répéter, dire une quantité, comprendre un prix. Une "
                "production orale, une production écrite.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Prévoir des écouteurs : la production orale se "
                  "fait à l'ordinateur, chacun de son côté.")

    d.objectifs([
        "tenir une conversation complète dans une épicerie ;",
        "employer les trois défis dans une même production ;",
        "écrire une liste d'épicerie avec les quantités ;",
        "recevoir une correction et la relire.",
    ])

    d.cartes('Les trois défis, réunis', "Ce qui doit apparaître", [
        ("Défi 1 · trouver",
         "Attirer l'attention, demander où c'est, faire répéter le numéro en donnant les "
         "deux possibilités."),
        ("Défi 2 · choisir",
         "Demander le format ou le prix, employer un mot de quantité suivi de « de »."),
        ("Défi 3 · payer",
         "Répondre aux trois questions de la caisse, comprendre le montant."),
    ], notes="Diapo à photographier. C'est la grille de la production orale.")

    d.regle("Le jeu de rôle",
            "Trois situations, deux rôles.",
            precision="Dans l'activité interactive : la <b>farine de maïs</b> (un produit "
                      "qui n'est pas là où on croit), le <b>spécial</b> (vérifier un prix "
                      "de circulaire), le <b>produit d'entretien</b> (comprendre une mise "
                      "en garde). Vous choisissez d'être le <b>client</b> ou le "
                      "<b>commis</b> — faites les deux, ils n'emploient pas les mêmes "
                      "phrases.",
            notes="Six combinaisons en tout. Demander au moins deux tours, dont un dans "
                  "chaque rôle.")

    d.pratique('Production orale', "Ce qui est demandé",
               "Trois minutes, à l'ordinateur.", [
        ("Ouvrir", "attirer l'attention et dire ce que vous cherchez"),
        ("Comprendre", "écouter la réponse, faire répéter le chiffre"),
        ("Préciser", "demander le format, la quantité ou le prix"),
        ("Vérifier", "répéter ce que vous avez compris"),
        ("Fermer", "remercier"),
    ], cols=1,
       notes="La correction par l'IA arrive tout de suite. Elle n'est pas conservée : "
             "l'élève la lit, la note, et recommence s'il le veut.")

    d.piege("Réciter au lieu de parler",
            "Apprendre le dialogue par cœur et le redire.",
            "Employer les structures avec ses propres mots.",
            "Un dialogue récité s'entend, et il ne prépare à rien : le vrai commis ne dira "
            "pas la réplique attendue. Les structures — « je cherche… », « cinq ou quinze ? "
            "», « un sac de… » — se réemploient ; les phrases entières, non.",
            notes="Rassurer : hésiter, se reprendre et chercher un mot est normal et n'est "
                  "pas pénalisé.")

    d.pratique('Production écrite', "Ce qui est demandé",
               "Une liste d'épicerie, de 5 à 8 phrases.", [
        ("Le sujet", "ce que vous devez acheter cette semaine"),
        ("À employer", "six produits au moins, une quantité pour chacun"),
        ("À employer aussi", "un produit en spécial, un produit d'entretien"),
        ("À vérifier", "le mot de quantité suivi de « de » ou « d' »"),
    ], cols=1,
       notes="La liste des billets de B4 et C2 sert de matière première : les élèves "
             "l'ont déjà écrite en partie.")

    d.tableau('Analyse', "Ce qui est regardé",
              ['Le critère', 'Ce qui compte'],
              [["La tâche", "les trois moments sont là"],
               ["Le vocabulaire", "les mots du module sont employés"],
               ["La langue", "« de » après la quantité, les mots de lieu"],
               ["La clarté", "on comprend du premier coup"]],
              cle=3,
              note="La clarté passe avant la perfection : une phrase simple et juste vaut "
                   "mieux qu'une phrase compliquée et fausse.",
              notes="Diapo à photographier. Le dire avant que les élèves commencent.")

    d.cartes("Si vous bloquez", "Trois secours", [
        ("Les mini-leçons",
         "Six panneaux « En apprendre plus » dans l'activité, avec l'audio. Ils restent "
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
