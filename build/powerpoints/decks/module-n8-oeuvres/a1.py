# -*- coding: utf-8 -*-
"""A1 · Un cercle de lecture qui tourne à vide
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.
"""
from theme import Deck

import pathlib

# Chemin déduit du fichier, jamais écrit en dur : le dépôt est aussi construit
# depuis un worktree git, où un chemin absolu vers la copie principale
# pointerait sur des images qui n'y sont pas encore.
IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n8-oeuvres' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Un cercle de lecture qui tourne à vide",
        chapeau="Dix-huit personnes se réunissent chaque mardi. Chacune "
                "raconte, chacune dit si elle a aimé, et à neuf heures moins "
                "quart tout le monde se lève. Il manque quelque chose au "
                "milieu.",
        duree='75 minutes')

    d.titre(notes="Première séance du module, et dernier module du programme. Ouvrir "
                  "par une question au groupe : avez-vous déjà discuté d'un film avec "
                  "quelqu'un qui l'avait compris autrement ? Les histoires sortent "
                  "vite. Garder celle qui vient la première : elle servira en D1.")

    d.objectifs([
        "distinguer un fait, une interprétation et un jugement ;",
        "entendre ce qu'une voix ajoute aux mots ;",
        "redire avec ses propres mots ce que quelqu'un vient de dire ;",
        "employer les premiers mots du dossier : une lecture, l'implicite, "
        "une interprétation.",
    ], notes="Le premier objectif est le cœur du module et il ne sera pas atteint "
             "aujourd'hui. Le poser quand même : les quinze séances y reviennent.")

    d.declencheur(
        'Observation', "Qu'est-ce qui se passe dans cette image ?",
        image=IMG + 'quai-lumiere.jpg',
        pistes=[
            "Nommez trois choses que vous voyez, sans rien deviner.",
            "Maintenant, qu'est-ce que vous imaginez ?",
            "Sur quoi vous appuyez-vous pour l'imaginer ?",
            "Est-ce que la personne à côté de vous imagine la même chose ?",
        ],
        notes="Exercice fondateur, à mener lentement. Les deux premières pistes font "
              "faire au groupe, sans le nommer, le partage entre le fait et "
              "l'interprétation. Noter les réponses au tableau en deux colonnes, sans "
              "les titrer : les titres viendront en A4.")

    d.dialogue('Dialogue · 1 de 3', "Ce qui manque au cercle du mardi", [
        ("FATOUMATA", "J'anime le cercle du mardi soir. Dix-huit personnes, une œuvre par mois. Ça marche très bien, et pourtant quelque chose ne va pas.", True),
        ("JOSYANE", "Qu'est-ce qui ne va pas ?", True),
        ("FATOUMATA", "Chacun raconte ce qu'il a vu. Puis chacun dit s'il a aimé. Et à neuf heures moins quart, on se lève.", True),
        ("JOSYANE", "Autrement dit, vous résumez et vous notez.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="La réplique de Josyane est une reformulation : le premier outil du "
             "module, employé avant d'être enseigné. Le faire remarquer sans "
             "l'expliquer — A4 y revient.")

    d.dialogue('Dialogue · 2 de 3', "« Ce que l'œuvre veut dire »", [
        ("JOSYANE", "Attention. « Ce que l'œuvre veut dire », c'est une formule dangereuse.", True),
        ("JOSYANE", "Elle laisse croire qu'il y a une réponse cachée quelque part et qu'un professeur la connaît.", True),
        ("FATOUMATA", "Il n'y en a pas ?", True),
        ("JOSYANE", "Il y a mieux. Il y a des lectures, plusieurs, et elles ne se valent pas toutes.", True),
    ], notes="Point de doctrine du module, dit par un personnage. Beaucoup d'adultes "
             "ont appris le contraire à l'école : il y avait une bonne réponse et le "
             "professeur l'avait. Prendre le temps.")

    d.dialogue('Dialogue · 3 de 3', "Trois choses qu'on dit d'un souffle", [
        ("JOSYANE", "Une lecture se juge à ce qu'elle permet d'expliquer dans l'œuvre.", True),
        ("JOSYANE", "Le problème de votre cercle, ce n'est pas qu'on y juge trop.", True),
        ("JOSYANE", "C'est qu'on saute du fait au jugement sans passer par l'interprétation.", True),
        ("FATOUMATA", "Est-ce que vous viendriez le dire vous-même, un mardi ?", True),
    ], notes="La règle de tout le module tient dans la première réplique. L'écrire au "
             "tableau et l'y laisser jusqu'à E2 : une lecture se juge à ce qu'elle "
             "permet d'expliquer.")

    d.tableau('Analyse', "Trois choses, et on les dit ensemble",
              ['On dit', 'Ce que c\'est'],
              [["Elle s'assoit dans la chaloupe",
                "un fait : on peut revoir la scène et le constater"],
               ["Elle renonce à partir",
                "une interprétation : ce n'est montré nulle part"],
               ["Cette fin est ratée",
                "un jugement : bon ou mauvais, et il coûte une raison"]],
              cle=0,
              note="Les trois sont permis. Les mélanger ne l'est pas.",
              notes="Diapositive à photographier. C'est le tableau le plus important du "
                    "module ; il revient en A4, en B2 et en D2.")

    d.regle("Une lecture n'est pas une opinion",
            "Une lecture se juge à ce qu'elle permet d'expliquer dans l'œuvre.",
            precision="Deux personnes peuvent avoir deux lectures défendables du même "
                      "passage. « Défendable » n'est pas « vraie » : celle qui rend "
                      "compte du plus grand nombre de détails est la plus solide ce "
                      "jour-là, et une meilleure peut venir demain.",
            notes="Diapositive à photographier. Question fréquente : « alors tout le "
                  "monde a raison ? » Non : celui qui n'explique rien a tort, et cela "
                  "se compte.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Le cercle du mardi réunit dix-huit personnes.", "vrai"),
        ("Fatoumata trouve que les gens ne viennent plus.", "faux - ça marche très bien"),
        ("Josyane trouve la formule « ce que l'œuvre veut dire » dangereuse.", "vrai"),
        ("Pour elle, une réponse est cachée et le professeur la connaît.", "faux - le contraire"),
        ("Une lecture se juge à ce qu'elle permet d'expliquer.", "vrai"),
        ("Josyane accepte de parler la première, mardi.", "faux - elle refuse"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le dernier "
             "surprend : pourquoi l'invitée refuserait-elle de commencer ? Parce "
             "qu'elle veut dix-huit lectures, pas dix-huit fois la sienne.")

    d.billet(
        "Nommez une œuvre dont la fin ne conclut pas — un film, une série, un "
        "livre, une chanson — et dites en une phrase ce que vous en avez compris.",
        exemples=[
            "Le titre, et où vous l'avez vue ou lue.",
            "Une phrase qui commence par « j'ai compris que ».",
        ],
        notes="Devoir concret. Les réponses servent de matière première tout le "
              "module : chaque élève arrive avec une œuvre à défendre, et c'est celle "
              "qu'il présentera en E1.")

    return d.save(dossier)
