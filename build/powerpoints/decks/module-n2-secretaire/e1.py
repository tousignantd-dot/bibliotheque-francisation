# -*- coding: utf-8 -*-
"""E1 · Je me lance.
Bloc E « Je me lance » · couleur teal · 60 min. Dernière séance du module.
Source : dialogue `appli`, exercices `aQui` et `aMoi`, jeu de rôle
`secretaire`, productions orale et écrite.

Séance de production, et dernière séance du niveau 2 au complet. Rien de
neuf : tout ce que le module a montré revient, et l'élève passe du côté de
celui qui sait — c'est Amel qui explique le centre à Sami, arrivé le matin
même, après avoir posé les mêmes questions trois séances plus tôt.

Les deux intentions orales du programme se jouent ici pour de vrai : le jeu
de rôle avec l'assistant sert de répétition, la prise orale se fait debout et
de vive voix, et l'écrit reste ce qu'un débutant écrit vraiment — un message
de trois à cinq phrases pour prévenir d'une absence.
"""
import pathlib
from theme import Deck

IMG = (pathlib.Path(__file__).resolve().parents[4]
       / 'assets' / 'interactive' / 'module-n2-secretaire' / 'images')


def img(nom):
    """La photo si elle existe, sinon rien — voir a1.py."""
    chemin = IMG / (nom + '.jpg')
    return str(chemin) if chemin.exists() else None


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="Je me lance",
        chapeau="Demander au comptoir de vive voix, puis écrire un message.",
        duree='60 minutes')

    d.titre(notes="Dernière séance du module — et du niveau 2. La moitié du temps se "
                  "passe en production réelle : jeu de rôle, enregistrement, écriture. "
                  "Les diapositives ne sont qu'un cadre, ne pas les commenter "
                  "longtemps.")

    d.objectifs([
        "saluer, se nommer et demander une chose au comptoir ;",
        "demander le jour et l'heure, puis répéter la réponse ;",
        "expliquer le centre à quelqu'un qui arrive ;",
        "écrire de trois à cinq phrases pour prévenir d'une absence.",
    ])

    d.declencheur(
        'Observation', "Quelqu'un arrive aujourd'hui pour son premier jour.",
        image=img('lieu-entree'),
        pistes=[
            "Qu'est-ce qu'il ne sait pas encore ?",
            "Quelle est la première chose à lui dire ?",
            "Où est-ce qu'il doit aller s'il a une question ?",
            "Qu'est-ce que personne ne vous avait dit, à vous ?",
        ],
        notes="La quatrième piste ouvre la séance : noter au tableau ce que le groupe "
              "dit. C'est le plan de la production orale, et il vient d'eux.")

    d.dialogue('Dialogue', "Cette fois, c'est Amel qui explique", [
        ("SAMI", "Excusez-moi, c'est mon premier jour. Où est le secrétariat ?", True),
        ("AMEL", "Au rez-de-chaussée, à côté de l'entrée.", True),
        ("SAMI", "Merci ! Et il ouvre à quelle heure ?", True),
        ("AMEL", "À huit heures. Mais le midi, c'est fermé.", True),
        ("SAMI", "Et si je suis absent ?", True),
        ("AMEL", "Vous allez au comptoir et vous prévenez la secrétaire.", True),
    ], consigne="Écoutez, puis dites les trois choses qu'Amel explique.",
       notes="Trois renseignements, six répliques : l'endroit, l'heure, la démarche. "
             "C'est exactement ce que le groupe sait faire maintenant.")

    d.tableau('Analyse', "Ce qui revient de tout le module",
              ["Ce qu'on dit", "Vu en"],
              [["C'est au rez-de-chaussée.", "A3 - au, dans, à côté de"],
               ["Je voudrais une attestation.", "B1 - poser sa question"],
               ["Ouvert à 8 h, fermé le midi.", "B2 - lire un horaire"],
               ["Demain, je ne viens pas.", "C1 - ne … pas"],
               ["Soyez à l'heure.", "C2 - les consignes"]],
              cle=1,
              notes="Diapositive à photographier. Elle sert de révision de tout le "
                    "module en une seule page.")

    d.regle("Trois choses, et l'échange est fini.",
            "Je salue. Je demande une chose. Je répète la réponse.",
            precision="« Bonjour, madame. Je voudrais une attestation, s'il vous plaît. "
                      "… Jeudi, après neuf heures ? Merci beaucoup ! » Trois phrases "
                      "très courtes valent mieux qu'une longue : c'est le niveau de "
                      "langue du vrai comptoir, pas une simplification pour la classe.",
            notes="Diapositive à photographier. C'est le plan de la production orale. "
                  "Le faire répéter par trois élèves avant d'ouvrir les postes.")

    d.cartes("Trois situations pour le jeu de rôle", "Choisissez la vôtre", [
        ("Je viens chercher un papier",
         "Ton propriétaire demande une preuve que tu suis le cours."),
        ("Demain, je ne viens pas",
         "Tu as un rendez-vous à la clinique demain matin."),
        ("C'est ouvert à quelle heure ?",
         "Tu veux revenir un autre jour et tu ne connais pas les heures."),
    ], cols=3, notes="Ce sont les trois situations du jeu de rôle en ligne. L'assistant "
                     "tient Line Chartrand, la secrétaire : elle donne un seul "
                     "renseignement par phrase et ne demande jamais de justifier une "
                     "absence.")

    d.pratique('Production orale', "Demandez votre papier au comptoir",
               "Trois temps. Enregistrez-vous, écoutez-vous, recommencez.", [
        ("TEMPS 1", "Bonjour, madame. Je m'appelle…"),
        ("TEMPS 2", "Je voudrais une attestation, s'il vous plaît."),
        ("TEMPS 3", "C'est prêt quand ? … Jeudi. Merci beaucoup !"),
    ], cols=1,
       notes="Vingt minutes. Environ trente secondes par prise. Laisser recommencer "
             "autant de fois qu'il le faut : c'est le but du panneau "
             "d'enregistrement.")

    d.pratique('Production écrite', "Écrivez un message au secrétariat",
               "De trois à cinq phrases, pour dire que vous serez absent.", [
        ("À écrire", "« Bonjour », au début."),
        ("À écrire", "Votre nom et votre groupe, ou votre local."),
        ("À écrire", "Une phrase négative : je ne viens pas."),
        ("À écrire", "Le jour de votre absence."),
        ("À écrire", "« Merci » et votre nom à la fin."),
    ], cols=1,
       notes="Vingt minutes. Rappeler le point que la correction en ligne regarde en "
             "premier : le « ne » de la négation, qui tombe à l'oral et se garde à "
             "l'écrit.")

    d.billet(
        "Cette semaine, allez demander une chose au secrétariat, pour de vrai.",
        exemples=[
            "Bonjour, madame. Je m'appelle…",
            "Je voudrais…, s'il vous plaît.",
            "C'est prêt quand ?",
        ],
        notes="Dernier devoir du module, et du niveau. Demander au cours suivant qui "
              "l'a fait et ce qu'on lui a répondu : c'est la seule évaluation qui "
              "compte pour cette situation-là.")

    return d.save(dossier)
