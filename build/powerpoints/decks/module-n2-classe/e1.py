# -*- coding: utf-8 -*-
"""E1 · Je me lance.
Bloc E « Je me lance » · couleur teal · 60 min. Dernière séance du module.
Source : dialogue `appli`, jeu de rôle `classe`, productions orale et écrite.

Séance de production. Tout ce que le module a montré revient ici, et rien de
neuf n'y est introduit — sauf un renversement : l'élève, qui a passé quatre
séances à comprendre ce qu'on lui dit, doit maintenant l'expliquer à
quelqu'un d'autre.

C'est l'intention de production orale du programme, mot pour mot : donner des
renseignements sur le fonctionnement de la classe et de l'établissement de
formation.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-classe/images/')


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="Je me lance",
        chapeau="Expliquer sa classe à une personne qui arrive, puis écrire "
                "un mot à son enseignante.",
        duree='60 minutes')

    d.titre(notes="Dernière séance. Prévoir que la moitié du temps se passe en production "
                  "réelle : jeu de rôle, enregistrement, écriture. Les diapositives ne "
                  "sont qu'un cadre.")

    d.objectifs([
        "expliquer l'horaire et la pause à un nouvel élève ;",
        "dire ce qu'il faut apporter ;",
        "dire une chose permise et une chose interdite ;",
        "écrire un mot d'absence de trois à cinq phrases.",
    ])

    d.declencheur(
        'Observation', "Une personne arrive dans le groupe. Que faut-il lui dire ?",
        image=IMG + 'pupitre-eleve.jpg',
        pistes=[
            "Qu'est-ce qu'elle ne sait pas encore ?",
            "Qu'est-ce que vous auriez voulu savoir, le premier jour ?",
            "Qu'est-ce qui est permis dans notre classe ?",
            "Qu'est-ce qui est interdit ?",
        ],
        notes="La deuxième piste ouvre toujours la séance : chacun se souvient de son "
              "premier matin. Noter au tableau ce que le groupe dit — c'est le plan de "
              "la production orale.")

    d.dialogue('Dialogue', "Bienvenue dans la classe", [
        ("MYRIAM", "Le cours commence à quelle heure ?", True),
        ("TARIQ", "À huit heures et demie. La pause est à dix heures.", True),
        ("MYRIAM", "Et on apporte quoi ?", True),
        ("TARIQ", "Un cahier, un crayon et une gomme à effacer.", True),
        ("MYRIAM", "Le téléphone, c'est permis ?", True),
        ("TARIQ", "Non, c'est interdit en classe. L'eau, c'est permis.", True),
    ], consigne="Écoutez, puis comptez ce que Tariq a réussi à expliquer.",
       notes="Quatre choses en trois répliques : l'heure, la pause, le matériel, les "
             "règles. Faire compter par le groupe : c'est le plan de leur propre "
             "enregistrement.")

    d.tableau('Analyse', "Ce qui revient de tout le module",
              ["Ce qu'on dit", "Vu en"],
              [["un cahier, un crayon, une gomme", "A1 — les objets de la classe"],
               ["une feuille blanche", "B2 — la couleur après l'objet"],
               ["Est-ce que je peux… ?", "C1 — demander la permission"],
               ["c'est permis, c'est interdit", "C2 — l'avis affiché"]],
              cle=2,
              note="Rien de neuf dans cette colonne : le module entier tient dans ces "
                   "quatre lignes.",
              notes="Diapositive à photographier. Elle sert de révision de tout le module "
                    "en une seule page.")

    d.regle("Expliquer, c'est dire une chose à la fois",
            "Quatre phrases courtes valent mieux qu'une longue.",
            precision="« Le cours commence à huit heures et demie. La pause est à dix "
                      "heures. Apportez un cahier et un crayon. Le téléphone est "
                      "<b>interdit</b> en classe. » Quatre phrases, quatre "
                      "renseignements, et la personne a tout ce qu'il lui faut.",
            notes="Diapositive à photographier. Rappeler le vouvoiement : c'est ce que la "
                  "correction en ligne regarde en premier.")

    d.cartes("Trois situations pour le jeu de rôle", "Choisissez la vôtre", [
        ("Je n'ai pas compris",
         "L'enseignante vient de donner une consigne. Vous ne l'avez pas comprise."),
        ("Est-ce que je peux ?",
         "Vous n'avez pas de crayon, et vous voulez sortir deux minutes."),
        ("Demain, je suis absent",
         "Vous avez un rendez-vous demain matin. Vous prévenez avant de partir."),
    ], cols=3, notes="Ce sont les trois situations du jeu de rôle en ligne. L'élève y joue "
                     "avec l'assistant, qui parle lentement, ne dit jamais plus de deux "
                     "ou trois phrases à la fois, et répète sans s'impatienter.")

    d.pratique('Production orale', "Expliquez votre classe à une personne qui arrive",
               "Trois temps. Enregistrez-vous, écoutez-vous, recommencez.", [
        ("TEMPS 1", "Le cours commence à huit heures et demie. La pause est à dix heures."),
        ("TEMPS 2", "Apportez un cahier, un crayon et une gomme à effacer."),
        ("TEMPS 3", "L'eau est permise. Le téléphone est interdit en classe."),
    ], cols=1,
       notes="Vingt minutes. Le vouvoiement doit tenir du début à la fin. Laisser "
             "recommencer autant de fois qu'il le faut : c'est le but du panneau "
             "d'enregistrement.")

    d.pratique('Production écrite', "Écrivez un mot à votre enseignante",
               "De trois à cinq phrases, pour une absence ou un retard.", [
        ("À écrire", "Le nom de votre enseignante, au début."),
        ("À écrire", "Le jour : demain, jeudi, lundi…"),
        ("À écrire", "« Je suis absent », « je suis absente » ou « je suis en retard »."),
        ("À écrire", "La raison, en trois ou quatre mots."),
        ("À écrire", "Votre prénom, sur la dernière ligne."),
    ], cols=1,
       notes="Vingt minutes. Le cadre est exactement celui écrit en C2 : ceux qui l'ont "
             "fait n'ont qu'à le reprendre et l'améliorer.")

    d.billet(
        "Cette semaine, posez une vraie question à votre enseignante en français.",
        exemples=[
            "Excusez-moi, je n'ai pas compris.",
            "Est-ce que je peux prendre une feuille ?",
            "Est-ce qu'il y a un congé cette semaine ?",
        ],
        notes="Dernier devoir du module. Demander au cours suivant qui l'a fait, et ce "
              "qu'on lui a répondu : c'est souvent la première phrase que l'élève dit à "
              "quelqu'un sans l'avoir préparée.")

    return d.save(dossier)
