# -*- coding: utf-8 -*-
"""A1 · Qui travaille ici ?
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercices `prVocab` et `pr1`.

Dixième et dernier module du niveau 2, format court. L'élève de ce niveau
tient une phrase à la fois : les diapositives portent peu de mots, et chaque
phrase projetée est une phrase qu'il dira vraiment dans son centre.

La situation du programme est « Communication avec le personnel de
l'établissement de formation ». Avant de parler à quelqu'un, il faut savoir à
qui : la séance commence donc par les quatre personnes du centre — la
secrétaire, l'enseignante, le concierge, la direction — et par une élève qui
prend le concierge pour son enseignant.
"""
import pathlib
from theme import Deck

IMG = (pathlib.Path(__file__).resolve().parents[4]
       / 'assets' / 'interactive' / 'module-n2-secretaire' / 'images')


def img(nom):
    """La photo si elle existe, sinon rien.

    Les vingt images du module sont produites par
    `build/contenu/module-n2-secretaire/gen_images.py`, qui demande une clé
    d'API. Tant qu'elles manquent, la séance se construit sans elles plutôt
    que de s'arrêter ; il faut reconstruire les huit `.pptx` une fois les
    photos sur le disque.
    """
    chemin = IMG / (nom + '.jpg')
    return str(chemin) if chemin.exists() else None


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Qui travaille ici ?",
        chapeau="Nommer les personnes du centre et dire où elles se trouvent.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Commencer sans diapositive : demander à "
                  "chacun de nommer une personne du centre à qui il a déjà parlé. Le "
                  "groupe en nomme deux ou trois, jamais quatre — et c'est le sujet de "
                  "la séance.")

    d.objectifs([
        "nommer quatre personnes qui travaillent au centre ;",
        "dire ce que chacune fait, en une phrase ;",
        "dire où est le secrétariat ;",
        "demander poliment où se trouve un local.",
    ])

    d.declencheur(
        'Observation', "Qui sont ces personnes, et que font-elles ?",
        image=img('lieu-secretariat'),
        pistes=[
            "Qui répond quand on arrive au centre le matin ?",
            "Qui ouvre les portes avant huit heures ?",
            "Qui donne le cours de français ?",
            "À qui parlez-vous quand vous ne comprenez pas un papier ?",
        ],
        notes="Laisser chercher les mots avant de les donner. « Secrétaire » sort "
              "toujours ; « concierge » et « direction » presque jamais. Ce sont ces "
              "deux-là qu'il faut travailler.")

    d.dialogue('Dialogue · 1 de 2', "Amel cherche le local 214", [
        ("AMEL", "Excusez-moi, monsieur. Je cherche le local 214.", True),
        ("MARC", "Bonjour ! Le 214, c'est au deuxième étage.", True),
        ("AMEL", "Au deuxième étage… Merci. Et le secrétariat ?", True),
        ("MARC", "Le secrétariat est ici, au rez-de-chaussée.", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Faire écouter deux fois, diapositive masquée. Faire remarquer qu'Amel "
             "répète « au deuxième étage » avant de continuer : c'est la stratégie de "
             "tout le module.")

    d.dialogue('Dialogue · 2 de 2', "Vous êtes l'enseignant ?", [
        ("AMEL", "À côté de la porte d'entrée ?", True),
        ("MARC", "Oui, à côté de l'entrée. Le comptoir est là.", True),
        ("AMEL", "Merci beaucoup. Vous êtes l'enseignant ?", True),
        ("MARC", "Non, je suis le concierge. Moi, j'ouvre les portes.", True),
    ], notes="La méprise est le cœur de la séance : on ne devine pas le rôle de "
             "quelqu'un à son apparence. Demander au groupe comment Amel aurait pu "
             "savoir. La réponse est simple : en demandant.")

    d.tableau('Analyse', "Quatre personnes, quatre rôles",
              ["La personne", "Ce qu'elle fait"],
              [["une enseignante", "elle donne le cours de français"],
               ["une secrétaire", "elle répond au comptoir et écrit les papiers"],
               ["un concierge", "il ouvre les portes et garde le centre propre"],
               ["la direction", "elle dirige le centre et signe les avis"]],
              cle=1,
              note="On dit « madame » et le nom de famille : madame Dufresne, madame Chartrand.",
              notes="Diapositive à photographier. Faire écrire dans le cahier le vrai "
                    "nom de l'enseignante et celui de la secrétaire du centre. Un nom "
                    "appris ici sert dès le lendemain.")

    d.vocabulaire('Vocabulaire', "Les six mots de « Je découvre »", [
        ("le secrétariat", "Le bureau du centre où on demande les papiers."),
        ("une secrétaire", "La personne qui répond au comptoir."),
        ("un concierge", "La personne qui ouvre les portes."),
        ("le couloir", "Le long passage entre les portes des classes."),
        ("le rez-de-chaussée", "L'étage d'en bas, celui de la porte d'entrée."),
        ("une enseignante", "La personne qui donne le cours de français."),
    ], notes="Diapositive à photographier. Faire répéter chaque mot avec son article : "
             "l'article s'apprend avec le mot, jamais après.")

    d.regle("« Excusez-moi, monsieur. »",
            "On commence toujours par ces deux mots.",
            precision="Au centre comme dans la rue, on ouvre par <b>excusez-moi</b>, "
                      "puis <b>monsieur</b> ou <b>madame</b>. Ensuite seulement vient "
                      "la question. Sans ces deux mots, la question paraît sèche même "
                      "quand elle est juste.",
            notes="Diapositive à photographier. Faire dire la phrase debout, à voix "
                  "haute, par chacun. C'est court, et c'est la porte d'entrée de tout "
                  "le module.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Amel cherche le local 214.", "vrai"),
        ("Le local 214 est au rez-de-chaussée.", "faux - il est au deuxième étage"),
        ("Le secrétariat est à côté de la porte d'entrée.", "vrai"),
        ("L'homme est l'enseignant du cours.", "faux - il est le concierge"),
    ], corrige=True, cols=1,
       notes="Quatre énoncés seulement. Les faire d'abord à l'oral, en groupe, avant de "
             "les faire écrire.")

    d.pratique('Pratique · debout, à deux', "Qui fait quoi dans notre centre ?",
               "Vingt minutes. Un élève demande, l'autre répond.", [
        ("Étape 1", "A dit : « Excusez-moi, madame. Qui donne le cours de français ? »"),
        ("Étape 2", "B répond avec le vrai nom de l'enseignante du groupe."),
        ("Étape 3", "A demande : « Et le secrétariat, il est où ? »"),
        ("Étape 4", "B répond, A répète la réponse, puis on échange les rôles."),
    ], cols=1,
       notes="Faire le tour du vrai centre en fin de séance, dix minutes, en nommant "
             "chaque endroit à voix haute. La séance se retient trois fois mieux "
             "debout.")

    d.billet(
        "Écrivez le nom de trois personnes qui travaillent dans votre centre.",
        exemples=[
            "Mon enseignante s'appelle madame…",
            "La secrétaire s'appelle madame…",
            "Le concierge s'appelle monsieur…",
        ],
        notes="Devoir court. Ceux qui ne connaissent pas les noms doivent aller les "
              "demander : c'est le vrai devoir, et il se fait en trente secondes au "
              "comptoir.")

    return d.save(dossier)
