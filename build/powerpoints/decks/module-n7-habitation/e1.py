# -*- coding: utf-8 -*-
"""E1 · Monter parler, puis raconter
Bloc E « Je me lance » · couleur teal · production orale · 75 min.
Source : bloc `appli` de `custom.js` — jeu de rôle « voisinage » (trois cas,
deux rôles) et la production orale en trois temps.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="Monter parler, puis raconter",
        chapeau="Deux productions orales en une séance : la conversation sur "
                "le palier, puis le compte rendu de cette conversation à "
                "quelqu'un qui n'y était pas.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Les deux tâches viennent directement des "
                  "deux intentions orales de la situation « Problèmes reliés à "
                  "l'habitation » : régler un problème de voisinage, en comprenant et "
                  "en produisant.")

    d.objectifs([
        "mener une conversation de voisinage du début à la fin ;",
        "concéder, demander au conditionnel, proposer une solution précise ;",
        "rapporter au passé ce que l'autre a répondu ;",
        "séparer ce qui a été dit de ce qu'on en conclut.",
    ], notes="Les quatre objectifs correspondent aux quatre blocs précédents. Le dire "
             "au groupe : rien de neuf aujourd'hui, tout a déjà été travaillé.")

    d.declencheur(
        'Préparation', "Qu'est-ce que tu apportes avec toi en montant ?",
        pistes=[
            "Une heure, une durée, un nombre de jours.",
            "Une concession que tu es prêt à faire.",
            "Deux solutions précises, pas une seule.",
            "Une phrase pour finir : quand est-ce qu'on se reparle ?",
        ],
        notes="Faire écrire les quatre éléments sur une fiche avant de commencer le "
              "jeu de rôle. Sans cette fiche, la conversation tourne court en deux "
              "minutes.")

    d.tableau('Jeu de rôle', "Trois situations, deux rôles",
              ['La situation', 'Ce qui la distingue'],
              [["Le tapis roulant du matin", "première conversation, quinze matins notés"],
               ["Le vélo dans l'escalier", "un seul point, facile à régler"],
               ["Deux semaines plus tard", "deux mesures sur trois, il faut remercier d'abord"]],
              note="On joue la locataire qui ne dort plus, ou le voisin qui court le "
                   "matin. Les deux rôles s'essaient : au niveau 7, il faut savoir "
                   "demander et savoir répondre.",
              cle=0,
              notes="Faire tourner les rôles au bout de sept minutes. Ceux qui jouent "
                    "le voisin comprennent mieux pourquoi un reproche ferme la porte.")

    d.cartes('Jeu de rôle', "Les huit sujets à couvrir", [
        ("1", "Saluer, se nommer, dire pourquoi on vient — avant tout détail."),
        ("2", "Décrire le bruit : une heure, une durée, un nombre de jours."),
        ("3", "Dire la conséquence : cela m'empêche de…, cela m'oblige à…"),
        ("4", "Concéder : même si votre horaire…, bien que je comprenne…"),
        ("5", "Demander au conditionnel : accepteriez-vous, pourriez-vous."),
        ("6", "Restreindre pour désamorcer : je ne me plains que du matin."),
        ("7", "Proposer une solution précise, jamais « faites quelque chose »."),
        ("8", "Faire confirmer, et fixer un moment pour se reparler."),
    ], notes="Distribuer la liste sur papier. Cocher au fur et à mesure : c'est la "
             "grille d'observation de l'enseignante autant que celle de l'élève.")

    d.piege('Jeu de rôle',
            "Vous faites du bruit tous les matins",
            "Ça commence à 5 h 45 et ça dure quarante minutes, depuis quinze jours",
            "La première phrase parle de la personne : elle se conteste, et l'autre se "
            "met à se défendre. La seconde parle du bruit : elle ne se conteste pas, "
            "et l'autre n'a rien à défendre. Toute la conversation se joue dans les "
            "dix premières secondes.",
            notes="Faire jouer les deux ouvertures par deux paires différentes, devant "
                  "le groupe. La différence de suite est saisissante.")

    d.tableau('Production orale', "Le compte rendu, en trois temps",
              ['Temps', 'Ce qu\'on dit'],
              [["1 · La situation", "les heures, la durée, depuis quand, la conséquence"],
               ["2 · Ce qu'il a dit", "il m'a dit qu'il avait…, qu'il ferait…, qu'il allait…"],
               ["3 · La suite", "le fait, la conclusion annoncée, puis une date"]],
              note="Quatre-vingt-dix secondes environ. Le temps 2 est celui qu'on "
                   "évalue : c'est là que le discours rapporté au passé se voit.",
              cle=0,
              notes="Diapositive à photographier. Les élèves s'enregistrent dans le "
                    "module et peuvent recommencer autant de fois qu'ils veulent.")

    d.pratique('Production orale', "Ce qu'on écoute dans l'enregistrement",
               "Grille de relecture, à donner avant l'enregistrement.", [
        ("Une heure, une durée et un nombre de jours dans les trois premières phrases", "temps 1"),
        ("Au moins une conséquence : cela m'empêche de, cela m'oblige à", "temps 1"),
        ("Trois formes du discours rapporté : avait, ferait, allait", "temps 2"),
        ("Les personnes décalées : je devient il, mon devient son", "temps 2"),
        ("Un fait, puis une conclusion annoncée par « j'en conclus que »", "temps 3"),
        ("Une date pour la suite, pas « bientôt »", "temps 3"),
    ], corrige=True,
       notes="Faire écouter un enregistrement volontaire devant le groupe et cocher la "
             "grille ensemble. Corriger la langue après, jamais pendant.")

    d.billet(
        "Quelle est la phrase la plus difficile à dire, pour toi, dans cette conversation ?",
        exemples=[
            "Une phrase, et dis pourquoi en cinq mots.",
            "Personne ne lira ta réponse à voix haute.",
        ],
        notes="Deux minutes. Les réponses disent où le groupe a besoin d'un dernier "
              "tour de piste avant la lettre de E2.")

    return d.save(dossier)
