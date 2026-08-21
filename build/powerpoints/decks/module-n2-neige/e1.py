# -*- coding: utf-8 -*-
"""E1 · Je me lance.
Bloc E « Je me lance » · couleur teal · 60 min. Dernière séance du module.
Source : dialogue `appli`, exercices `aQui` et `aMoi`, jeu de rôle `meteo`,
productions orale et écrite.

Séance de production. Rien de neuf : tout ce que le module a montré revient,
et l'élève passe du côté de celui qui sait — c'est Zina qui explique « moins
vingt » à son fils, après l'avoir appris elle-même trois séances plus tôt.

L'unique intention du programme pour cette situation est en compréhension
écrite. La prise orale est donc là pour la démarche, qui se fait debout et de
vive voix ; l'écrit reste ce qu'un débutant écrit vraiment — un message de
trois à cinq phrases à quelqu'un qui ne connaît pas l'hiver.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-neige/images/')


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="Je me lance",
        chapeau="Parler du temps qu'il fait de vive voix, puis l'écrire à "
                "quelqu'un.",
        duree='60 minutes')

    d.titre(notes="Dernière séance. La moitié du temps se passe en production réelle : "
                  "jeu de rôle, enregistrement, écriture. Les diapositives ne sont "
                  "qu'un cadre — ne pas les commenter longtemps.")

    d.objectifs([
        "dire le temps qu'il fait en deux ou trois phrases ;",
        "donner la température avec son signe ;",
        "dire ce qu'on met pour sortir ;",
        "écrire de trois à cinq phrases sur le temps qu'il fait.",
    ])

    d.declencheur(
        'Observation', "Quelqu'un n'a jamais vu la neige. Qu'est-ce que vous lui dites ?",
        image=IMG + 'temps-froid.jpg',
        pistes=[
            "Qu'est-ce que vous voyez sur la photo ?",
            "Qu'est-ce qui vous a le plus étonné, votre premier hiver ?",
            "Qu'est-ce que personne ne vous avait dit ?",
            "Qu'est-ce que vous diriez à quelqu'un qui arrive en novembre ?",
        ],
        notes="La quatrième piste ouvre la séance : noter au tableau ce que le groupe "
              "dit. C'est le plan de la production écrite, et il vient d'eux.")

    d.dialogue('Dialogue', "Cette fois, c'est Zina qui explique", [
        ("YOUSSEF", "Maman, c'est quoi, « moins vingt » ?", True),
        ("ZINA", "C'est très froid. Zéro, c'est déjà froid. Moins vingt, c'est pire.", True),
        ("YOUSSEF", "Et « plus vingt » ?", True),
        ("ZINA", "Plus vingt, c'est chaud. C'est l'été.", True),
        ("YOUSSEF", "Alors aujourd'hui, il fait moins ou plus ?", True),
        ("ZINA", "Moins. Moins huit. Regarde le thermomètre.", True),
    ], consigne="Écoutez, puis dites comment Zina explique le mot.",
       notes="Elle n'explique pas avec des mots savants : elle compare avec zéro, puis "
             "elle montre. C'est exactement ce que le groupe peut faire.")

    d.tableau('Analyse', "Ce qui revient de tout le module",
              ["Ce qu'on dit", "Vu en"],
              [["Il neige. Il vente.", "A3 - le « il » de la météo"],
               ["Il fait moins huit degrés.", "B2 - lire une température"],
               ["Il faut mettre une tuque.", "C1 - il faut, je mets, mets"],
               ["Quel temps fait-il demain ?", "C2 - poser la question"]],
              cle=1,
              note="Rien de neuf dans cette colonne : le module entier tient en quatre lignes.",
              notes="Diapositive à photographier. Elle sert de révision de tout le "
                    "module en une seule page.")

    d.regle("Trois choses, et on a tout dit",
            "Le temps, la température, ce qu'on met.",
            precision="« Il neige. Il fait moins douze. Je mets ma tuque et mes "
                      "mitaines. » Trois phrases très courtes valent mieux qu'une "
                      "longue : c'est le niveau de langue de la rue, pas une "
                      "simplification pour la classe.",
            notes="Diapositive à photographier. C'est le plan de la production orale. "
                  "Le faire répéter par trois élèves avant d'ouvrir les postes.")

    d.cartes("Trois situations pour le jeu de rôle", "Choisissez la vôtre", [
        ("Dans l'entrée de l'immeuble",
         "Tu pars au cours. Ton voisin rentre de dehors, le manteau couvert de neige."),
        ("Je n'ai pas tout compris à la radio",
         "Tu as entendu le bulletin de sept heures, mais trop vite. Ton voisin l'a écouté au complet."),
        ("Est-ce qu'il y a de l'école ?",
         "Il tombe trente centimètres de neige. Tu veux savoir si ton cours a lieu."),
    ], cols=3, notes="Ce sont les trois situations du jeu de rôle en ligne. L'assistant "
                     "tient Roland, le voisin retraité : il ne donne qu'un "
                     "renseignement par phrase et répète sans s'impatienter.")

    d.pratique('Production orale', "Parlez du temps qu'il fait",
               "Trois temps. Enregistrez-vous, écoutez-vous, recommencez.", [
        ("TEMPS 1", "Bonjour ! Aujourd'hui, il neige et il vente."),
        ("TEMPS 2", "Il fait moins douze degrés. C'est froid !"),
        ("TEMPS 3", "Je mets mon manteau, ma tuque et mes mitaines."),
    ], cols=1,
       notes="Vingt minutes. Environ trente secondes par prise. Laisser recommencer "
             "autant de fois qu'il le faut : c'est le but du panneau "
             "d'enregistrement.")

    d.pratique('Production écrite', "Écrivez la météo à quelqu'un de votre famille",
               "De trois à cinq phrases, à quelqu'un qui vit dans un pays chaud.", [
        ("À écrire", "« Bonjour », au début."),
        ("À écrire", "Le temps qu'il fait : il neige, il pleut, il vente, il fait beau."),
        ("À écrire", "La température, avec « moins » ou « plus » devant."),
        ("À écrire", "Deux vêtements que vous mettez pour sortir."),
        ("À écrire", "La saison, et « à bientôt » à la fin."),
    ], cols=1,
       notes="Vingt minutes. Rappeler les deux points que la correction en ligne "
             "regarde en premier : « en hiver » mais « au printemps », et le « il » "
             "de la météo — jamais « la neige neige ».")

    d.billet(
        "Cette semaine, parlez de la météo en français à une personne, pour de vrai.",
        exemples=[
            "Il fait froid aujourd'hui !",
            "Est-ce qu'il neige demain ?",
            "Il fait combien de degrés ?",
        ],
        notes="Dernier devoir du module. Demander au cours suivant qui l'a fait et ce "
              "qu'on lui a répondu : la météo est le sujet dont tout le monde parle "
              "au Québec, et c'est la porte d'entrée la plus facile.")

    return d.save(dossier)
