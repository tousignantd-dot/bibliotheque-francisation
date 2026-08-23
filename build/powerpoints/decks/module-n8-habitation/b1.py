# -*- coding: utf-8 -*-
"""B1 · Quatre pages, ligne par ligne
Bloc B « Défi 1 · Le rapport qu'on discute » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t11`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Trois sortes de phrases, trois poids",
        chapeau="Un refus tient en une ligne, mais il s'appuie sur un "
                "document de quatre pages que presque personne ne demande. "
                "Ce défi apprend à le lire.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc B. Rappeler où on en est : la lettre est arrivée, "
                  "le rapport a été demandé, et Teodora consulte un expert qu'elle "
                  "paie elle-même. C'est un geste que peu de gens connaissent.")

    d.objectifs([
        "distinguer ce qu'un expert a vu, ce qu'on lui a dit, et ce qu'il en déduit ;",
        "reconnaître les verbes de constat, de rapport et de déduction ;",
        "savoir ce qu'est un expert en sinistre public, et qu'on peut en engager un ;",
        "comparer deux documents du même assureur.",
    ], notes="Le premier objectif est le cœur du bloc. Tout le reste en découle, y "
             "compris la lettre du bloc E.")

    d.declencheur(
        'Discussion', "Avez-vous déjà lu un rapport écrit sur vous ?",
        pistes=[
            "Un rapport médical, scolaire, de travail, d'inspection ?",
            "Était-il facile à comprendre ?",
            "Y avait-il des phrases dont vous n'étiez pas sûr du sens ?",
            "À qui ce rapport était-il adressé, à votre avis ?",
        ],
        notes="La dernière question est celle qui ouvre la séance : un rapport "
              "d'expertise n'est jamais écrit pour vous. On le lit par-dessus "
              "l'épaule de quelqu'un.")

    d.dialogue('Dialogue 1 de 3', "Ce qu'il faut savoir avant de lire", [
        ("NORMAND", "Avant de le lire, une chose : un rapport contient trois sortes de phrases, et elles n'ont pas la même valeur.", True),
        ("TEODORA", "Lesquelles ?", True),
        ("NORMAND", "Ce que l'expert a vu de ses yeux, ce qu'on lui a dit, et ce qu'il en déduit. Le premier bloc est presque impossible à contester. Le troisième se discute toujours.", True),
        ("TEODORA", "Comment je les distingue ?", True),
        ("NORMAND", "Par les verbes. « J'ai constaté », « j'ai mesuré » : c'est vu. « Selon l'assurée » : c'est dit. « Il appert que » : c'est déduit.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire noter les trois familles de verbes au tableau, en trois colonnes. "
             "Elles y resteront tout le bloc B.")

    d.dialogue('Dialogue 2 de 3', "Le passif cache celui qu'on accuse", [
        ("TEODORA", "Il y a cette phrase, page deux : « Le drain n'aurait pas été entretenu depuis plusieurs années. »", True),
        ("NORMAND", "Celle-là est intéressante. Vous voyez ce qui manque ?", True),
        ("TEODORA", "Le nom. On ne dit pas qui n'a pas entretenu.", True),
        ("NORMAND", "Exactement. C'est le passif, et dans ce métier il travaille tout le temps. La phrase ne met personne en cause à voix haute, mais l'exclusion, elle, s'applique à vous.", True),
    ], notes="La réponse de Teodora est celle qu'on attend du groupe. Poser la question "
             "à haute voix avant de dévoiler la réplique : « qu'est-ce qui manque à "
             "cette phrase ? »")

    d.dialogue('Dialogue 3 de 3', "Deux documents, deux tuyaux", [
        ("NORMAND", "Leur rapport parle d'une obstruction du drain de fondation, pas du drain de plancher.", True),
        ("TEODORA", "Ce n'est pas la même chose ?", True),
        ("NORMAND", "Pas du tout. Le drain de fondation est dehors, au pied des murs. Le drain de plancher est dedans. La lettre de refus parle du drain de plancher, le rapport parle du drain de fondation.", True),
        ("TEODORA", "Je n'avais pas fait attention.", True),
        ("NORMAND", "C'est là qu'est votre dossier, madame Vlaicu. Deux documents du même assureur qui ne parlent pas du même tuyau.", True),
    ], notes="Le point de bascule du module. Reprendre le dessin en coupe de A3 si "
             "besoin. Faire remarquer que Teodora avait lu les deux documents sans "
             "le voir : ce n'est pas une question d'attention, c'est une méthode.")

    d.regle("Une déduction se reconnaît à ses précautions",
            "« Il appert que », « laisse supposer », « pourrait résulter de », "
            "« selon toute vraisemblance » : un rapport qui accumule ces "
            "formules ne raconte pas ce qu'on a vu. Il propose une "
            "explication.",
            precision="Et une explication se discute avec une autre explication — ou "
                      "mieux, avec un constat. Une caméra passée dans le tuyau vaut "
                      "dix « il appert que ».",
            notes="Diapositive à photographier. Faire chercher ces formules dans le "
                  "rapport du module : il y en a trois, et elles sont toutes dans le "
                  "bloc « Analyse ».")

    d.tableau('Analyse', "Trois familles de verbes",
              ['Famille', 'Formules'],
              [["Vu", "j'ai constaté · j'ai mesuré · j'ai photographié · j'ai relevé"],
               ["Dit", "selon l'assurée · il m'a été rapporté · le service rapporte"],
               ["Déduit", "il appert que · tout indique que · la cause probable est"]],
              cle=0,
              note="Seule la première famille engage la signature de l'expert.",
              notes="Diapositive à photographier. Insister : on ne conteste pas un "
                    "constat, on remarque ce qu'il ne couvre pas. Une ligne de "
                    "mouillure mesurée ne dit rien de la cause.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la rencontre avec l'expert.", [
        ("Ce que l'expert a vu de ses yeux est le plus difficile à contester.", "vrai"),
        ("« Il appert que » annonce un constat.", "faux - une déduction"),
        ("La phrase « le drain n'aurait pas été entretenu » nomme la personne en cause.", "faux - le passif l'efface"),
        ("La lettre et le rapport parlent tous les deux du drain de plancher.", "faux - la lettre seulement"),
        ("Le drain de fondation se trouve à l'extérieur, au pied des murs.", "vrai"),
        ("Monsieur Lauzière s'engage à écrire un rapport favorable à Teodora.", "faux - il écrit ce qu'il voit"),
    ], corrige=True,
       notes="Le dernier est le plus important pour la suite : un expert qu'on paie "
             "n'est pas un expert qui nous approuve, et c'est ce qui donne de la "
             "valeur à son rapport.")

    d.billet(
        "Cherchez dans le rapport du module une phrase de chaque famille.",
        exemples=[
            "Une qui commence par « j'ai ».",
            "Une qui commence par « selon ».",
            "Une qui contient « il appert » ou « laisse supposer ».",
        ],
        notes="Le rapport est dans le module, exercice 2 du défi 1. Les trois phrases "
              "trouvées serviront directement à la séance B2.")

    return d.save(dossier)
