# -*- coding: utf-8 -*-
"""E1 · Je me lance.
Bloc E « Je me lance » · couleur teal · 60 min. Dernière séance du module.
Source : jeu de rôle `fiche`, production orale et écrite, autoévaluation.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre='Je me lance',
        chapeau="Tout le module tient dans une minute : mon nom, je l'épelle, "
                "ma date de naissance, mon adresse, mon téléphone.",
        duree='60 minutes')

    d.titre(notes="Dernière séance. Prévoir des écouteurs : la production orale se fait à "
                  "l'ordinateur, chacun de son côté. Rendre les billets de C2 corrigés "
                  "avant de commencer — ce sont les brouillons de la fiche écrite.")

    d.objectifs([
        "répondre aux questions d'une fiche à voix haute ;",
        "remplir sa propre fiche ;",
        "réviser les mots du module ;",
        "évaluer ce que je suis maintenant capable de faire.",
    ])

    d.cartes('Les deux défis, réunis', "Ce qui doit apparaître", [
        ("Défi 1 · le nom et la date",
         "Le nom de famille épelé, le prénom, le sexe, la date de naissance dans l'ordre "
         "jour / mois / année."),
        ("Défi 2 · l'adresse et le téléphone",
         "Le numéro et la rue, l'appartement, la ville et QC, le code postal, les dix "
         "chiffres du téléphone, le courriel."),
    ], notes="Diapo à photographier. C'est la grille de la production orale et de la "
             "production écrite.")

    d.regle("Le jeu de rôle",
            "Trois situations, deux rôles.",
            precision="Dans l'activité : <b>à la table</b> (on vous demande les cases du "
                      "haut), <b>l'adresse</b> (où vous habitez), <b>les chiffres</b> "
                      "(téléphone, code postal, courriel). Vous choisissez d'être "
                      "<b>l'élève</b> ou <b>la personne au comptoir</b>.",
            notes="L'assistant parle lentement et pose une question à la fois. Demander au "
                  "moins deux tours, dont un dans chaque rôle.")

    d.pratique('Production orale', "Ce qui est demandé",
               "Environ quarante secondes, à l'ordinateur.", [
        ("Temps 1", "Mon nom de famille est… D - A - O - …"),
        ("Temps 2", "Je suis né le … (jour) … (mois) … (année)"),
        ("Temps 3", "J'habite au … , … , appartement …"),
        ("Temps 4", "Mon numéro est le … , un chiffre à la fois."),
    ], cols=1,
       notes="Quarante secondes suffisent au niveau 1. La correction par l'IA arrive tout "
             "de suite ; elle n'est pas conservée.")

    d.pratique('Production écrite', "Ce qui est demandé",
               "Votre fiche, de 4 à 6 lignes, une case par ligne.", [
        ("À écrire", "NOM DE FAMILLE, en majuscules"),
        ("À écrire", "PRÉNOM"),
        ("À écrire", "DATE DE NAISSANCE : __ / __ / ____"),
        ("À écrire", "ADRESSE, avec app., av. ou boul."),
        ("À écrire", "TÉL. : dix chiffres"),
    ], cols=1,
       notes="Les billets de B2 et de C2 servent de brouillon : la date et les trois "
             "coordonnées sont déjà écrites et corrigées.")

    d.piege("Recopier la fiche de Yusuf",
            "Écrire « Daoud, 12 mars 1992, avenue Papineau ».",
            "Écrire ses vrais renseignements.",
            "Vous ne vous appelez pas Yusuf et vous n'habitez pas avenue Papineau. Ce sont "
            "les <b>cases</b> et leur ordre qui se réemploient, jamais le contenu. Une "
            "fiche est utile seulement si elle est vraie.",
            notes="Le dire avant que les élèves commencent : la tentation est réelle quand "
                  "le modèle est au tableau depuis huit séances.")

    d.tableau('Analyse', "Ce qui est regardé",
              ['Le critère', 'Ce qui compte'],
              [["La tâche", "les cinq cases sont remplies"],
               ["L'ordre", "le jour avant le mois, le numéro avant la rue"],
               ["La clarté", "on peut vous joindre avec ce qui est écrit"]],
              cle=2,
              note="La clarté passe avant la perfection.",
              notes="Diapo à photographier. Le dire avant que les élèves commencent.")

    d.billet(
        "Autoévaluation : pour chaque énoncé, pas encore, un peu, ou oui.",
        exemples=[
            "Je peux dire mon nom de famille et l'épeler.",
            "Je peux dire ma date de naissance dans l'ordre.",
            "Je peux dire mon adresse et mon numéro de téléphone.",
            "Je peux écrire mes renseignements dans les cases d'une fiche.",
        ],
        notes="L'autoévaluation complète est dans l'activité interactive. La faire remplir "
              "là : elle est conservée avec les traces de l'élève. C'est la fin du module.")

    return d.save(dossier)
