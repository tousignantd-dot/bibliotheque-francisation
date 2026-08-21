# -*- coding: utf-8 -*-
"""E1 · Je me lance.
Bloc E « Je me lance » · couleur teal · 60 min. Dernière séance du module.
Source : dialogue `appli`, jeu de rôle `couloirs`, productions orale et
écrite.

Séance de production. Rien de neuf n'y est introduit : tout ce que le module
a montré revient, et l'élève passe du côté de celui qui sait.

C'est l'intention de production orale du programme, mot pour mot : donner des
renseignements sur la localisation.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-couloirs/images/')


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="Je me lance",
        chapeau="Faire visiter le centre à une personne qui arrive, puis lui "
                "écrire où est son local.",
        duree='60 minutes')

    d.titre(notes="Dernière séance. Prévoir que la moitié du temps se passe en production "
                  "réelle : jeu de rôle, enregistrement, écriture. Les diapositives ne "
                  "sont qu'un cadre.")

    d.objectifs([
        "dire à quel étage est un local ;",
        "indiquer le chemin en deux phrases ;",
        "nommer deux repères utiles du centre ;",
        "écrire de trois à cinq phrases pour dire où est un local.",
    ])

    d.declencheur(
        'Observation', "Une personne arrive au centre. Qu'est-ce qu'elle ne sait pas ?",
        image=IMG + 'comptoir-accueil.jpg',
        pistes=[
            "Qu'est-ce que vous ne saviez pas, votre premier matin ?",
            "Qu'est-ce que vous auriez voulu qu'on vous dise ?",
            "Combien de temps avez-vous cherché ?",
            "Qui vous a aidé ?",
        ],
        notes="La deuxième piste ouvre toujours la séance : chacun se souvient de son "
              "premier matin. Noter au tableau ce que le groupe dit - c'est le plan de "
              "la production orale.")

    d.dialogue('Dialogue', "Bienvenue au centre", [
        ("AMINA", "Bonjour. C'est ma première journée ici.", True),
        ("SORAYA", "Bienvenue ! Vous cherchez quel local ?", True),
        ("AMINA", "Le 212.", True),
        ("SORAYA", "Au deuxième étage. Comme moi.", True),
        ("AMINA", "Il y a un ascenseur ?", True),
        ("SORAYA", "Oui, au milieu du corridor, à côté de l'escalier.", True),
    ], consigne="Écoutez, puis comptez ce que Soraya a réussi à expliquer.",
       notes="Trois choses en trois répliques : l'étage, l'ascenseur, sa position. "
             "Faire compter par le groupe : c'est le plan de leur propre "
             "enregistrement.")

    d.tableau('Analyse', "Ce qui revient de tout le module",
              ["Ce qu'on dit", "Vu en"],
              [["Excusez-moi, où est… ?", "A3 - la question qui ouvre les portes"],
               ["Le 214, c'est au deuxième étage.", "B2 - le premier chiffre dit l'étage"],
               ["en face de l'ascenseur", "C1 - dire où c'est, exactement"],
               ["Prenez l'escalier, puis à droite.", "C2 - indiquer le chemin"]],
              cle=1,
              note="Rien de neuf dans cette colonne : le module entier tient en quatre "
                   "lignes.",
              notes="Diapositive à photographier. Elle sert de révision de tout le "
                    "module en une seule page.")

    d.regle("Expliquer, c'est dire une chose à la fois",
            "Quatre phrases courtes valent mieux qu'une longue.",
            precision="« Votre local, c'est le 214. C'est au deuxième étage. Prenez "
                      "l'escalier, au milieu du corridor. Les toilettes sont en face de "
                      "l'ascenseur. » Quatre phrases, quatre renseignements, et la "
                      "personne a tout ce qu'il lui faut.",
            notes="Diapositive à photographier. Rappeler le vouvoiement : c'est ce que la "
                  "correction en ligne regarde en premier.")

    d.cartes("Trois situations pour le jeu de rôle", "Choisissez la vôtre", [
        ("Je cherche le local 214",
         "C'est votre première journée. Sur votre feuille, un numéro : 214."),
        ("Les casiers et les toilettes",
         "C'est la pause. Vous cherchez la salle des casiers, et les toilettes."),
        ("C'est moi qui explique",
         "Une personne arrive et cherche le secrétariat. Cette fois, vous savez."),
    ], cols=3, notes="Ce sont les trois situations du jeu de rôle en ligne. L'élève y joue "
                     "avec l'assistant, qui tient Gilles le concierge : une indication à "
                     "la fois, l'étage puis le côté, et il répète sans s'impatienter.")

    d.pratique('Production orale', "Faites visiter le centre à une personne qui arrive",
               "Trois temps. Enregistrez-vous, écoutez-vous, recommencez.", [
        ("TEMPS 1", "Votre local, c'est le 214. C'est au deuxième étage."),
        ("TEMPS 2", "Prenez l'escalier, au milieu du corridor. Puis à droite."),
        ("TEMPS 3", "Les toilettes sont en face de l'ascenseur. La cafétéria est en bas."),
    ], cols=1,
       notes="Vingt minutes. Le vouvoiement doit tenir du début à la fin. Laisser "
             "recommencer autant de fois qu'il le faut : c'est le but du panneau "
             "d'enregistrement.")

    d.pratique('Production écrite', "Écrivez où est votre local",
               "De trois à cinq phrases, pour une personne qui arrive demain.", [
        ("À écrire", "Le prénom de la personne, au début."),
        ("À écrire", "Le numéro du local, en chiffres."),
        ("À écrire", "L'étage : au rez-de-chaussée, au premier, au deuxième."),
        ("À écrire", "Un repère : à côté de, en face de, au bout du corridor."),
        ("À écrire", "Votre prénom, sur la dernière ligne."),
    ], cols=1,
       notes="Vingt minutes. Le cadre est exactement celui du billet de sortie de C2 : "
             "ceux qui l'ont fait n'ont qu'à le reprendre et l'améliorer.")

    d.billet(
        "Cette semaine, indiquez un chemin à quelqu'un, en français, dans le vrai centre.",
        exemples=[
            "C'est au deuxième étage.",
            "Prenez l'escalier, puis à droite.",
            "Les toilettes sont en face de l'ascenseur.",
        ],
        notes="Dernier devoir du module. Demander au cours suivant qui l'a fait, et si "
              "la personne a trouvé : c'est la seule évaluation qui compte vraiment "
              "pour cette situation du programme.")

    return d.save(dossier)
