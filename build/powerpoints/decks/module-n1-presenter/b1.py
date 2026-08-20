# -*- coding: utf-8 -*-
"""B1 · D'où viens-tu ?
Bloc B « Défi 1 · Se présenter » · couleur acier · 75 min.
Source : dialogues `t1` et `t1b`, exercices `t1vf` et `t1b`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n1-presenter/images/')


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="D'où viens-tu ?",
        chapeau="Entre élèves, on se tutoie. Cinq phrases suffisent pour se "
                "présenter — et les mêmes cinq servent à poser les questions.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc B. Faire remarquer d'emblée le passage du « vous » "
                  "de l'accueil au « tu » entre camarades.")

    d.objectifs([
        "dire d'où on vient ;",
        "dire où on habite ;",
        "dire quelles langues on parle ;",
        "poser les mêmes questions à quelqu'un.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qu'on voit ici ?",
        image=IMG + 'carte-monde.jpg',
        pistes=[
            "Montrez votre pays.",
            "Qui vient du même continent que vous ?",
            "Combien de pays dans la classe ?",
            "Combien de langues ?",
        ],
        notes="Faire venir chacun montrer son pays. C'est le moment le plus fort de la "
              "séance, et il ne demande presque pas de français.")

    d.dialogue('Dialogue · 1 de 2', "Le pays", [
        ("LIN", "Bonjour ! Moi, c'est Lin.", True),
        ("AMINA", "Bonjour Lin. Moi, c'est Amina.", True),
        ("LIN", "D'où viens-tu ?", True),
        ("AMINA", "Je viens d'Algérie. Et toi ?", True),
        ("LIN", "Je viens du Vietnam. J'habite à Montréal.", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="« Moi, c'est Lin » : la forme courte, entre camarades. « Et toi ? » renvoie "
             "la question sans la répéter en entier.")

    d.dialogue('Dialogue · 2 de 2', "La langue et la famille", [
        ("LIN", "Tu parles quelles langues ?", True),
        ("AMINA", "Je parle arabe et un peu français.", True),
        ("LIN", "Moi, je parle vietnamien et anglais.", True),
        ("AMINA", "Tu as des enfants ?", True),
        ("LIN", "Oui, j'ai deux enfants. Et toi ?", True),
        ("AMINA", "J'ai un fils. Il a six ans.", True),
    ], notes="« Un peu français » est une réponse honnête et très utile. La faire "
             "répéter : elle enlève beaucoup de pression.")

    d.tableau('Analyse', "Les cinq phrases",
              ['La phrase', "Ce qu'elle dit"],
              [["Je m'appelle…", "le nom"],
               ["Je viens de…", "le pays"],
               ["J'habite à…", "la ville"],
               ["Je parle…", "les langues"],
               ["J'ai…", "la famille, l'âge"]],
              cle=0,
              note="Les mêmes cinq, partout, toute la vie.",
              notes="Diapo à photographier. C'est le cœur du module. Faire écrire les cinq "
                    "phrases complètes par chaque élève.")

    d.regle("Et toi ?",
            "Deux mots pour renvoyer la question.",
            precision="Au lieu de répéter toute la question, on dit « <b>et toi ?</b> » — "
                      "ou « <b>et vous ?</b> » si l'on vouvoie. C'est court, c'est poli, "
                      "et cela fait durer la conversation.",
            notes="Diapo à photographier. C'est la formule qui transforme une réponse en "
                  "échange.")

    d.cartes("Tu ou vous ?", "Trois repères simples", [
        ("Entre élèves : tu",
         "Dans la classe, entre camarades, on se tutoie. « D'où viens-tu ? »"),
        ("Au comptoir : vous",
         "À l'accueil, au secrétariat, dans un magasin. « D'où venez-vous ? »"),
        ("Dans le doute : vous",
         "Le « vous » n'est jamais impoli. Le « tu » à la mauvaise personne peut "
         "surprendre."),
    ], notes="Diapo à photographier. Ne pas entrer dans les nuances : ces trois repères "
             "suffisent pour tout le niveau 1.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après les deux dialogues.", [
        ("Lin vient du Vietnam.", "vrai"),
        ("Amina vient du Maroc.", "faux — d'Algérie"),
        ("Les deux habitent à Montréal.", "vrai"),
        ("Lin a trois enfants.", "faux — deux"),
        ("Amina a un fils de six ans.", "vrai"),
    ], corrige=True, cols=1,
       notes="Faire justifier chaque « faux » par la réplique exacte.")

    d.billet(
        "Écrivez vos cinq phrases.",
        exemples=[
            "Je m'appelle… Je viens de… J'habite à… Je parle… J'ai…",
            "Apprenez-les par cœur pour la prochaine séance.",
        ],
        notes="Ramasser et corriger. Ces cinq phrases servent au jeu de rôle et à la "
              "production orale.")

    return d.save(dossier)
