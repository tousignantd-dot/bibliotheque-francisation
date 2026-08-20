# -*- coding: utf-8 -*-
"""C1 · Bonjour, merci, pardon.
Bloc C « Défi 2 · Saluer et remercier » · couleur acier · 75 min.
Source : dialogue `t2`, exercices `t2vf` et `t2quand`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n1-presenter/images/')


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre='Bonjour, merci, pardon',
        chapeau="Trois mots, et on est poli partout. Un quatrième est encore "
                "plus utile : « je ne comprends pas ».",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc C. Demander au groupe ce qu'on dit en entrant dans un "
                  "magasin dans leur pays. Les réponses varient beaucoup — c'est une "
                  "bonne entrée en matière.")

    d.objectifs([
        "saluer selon le moment de la journée ;",
        "remercier et répondre à un merci ;",
        "dire qu'on ne comprend pas ;",
        "demander de parler plus lentement.",
    ])

    d.declencheur(
        'Observation', "Que se disent ces deux personnes ?",
        image=IMG + 'poignee-main.jpg',
        pistes=[
            "Est-ce qu'elles se connaissent ?",
            "Que dit-on en se serrant la main ?",
            "Et dans votre pays, que fait-on ?",
            "Serre-t-on toujours la main ici ?",
        ],
        notes="Au Québec, la poignée de main est courante au travail et à l'accueil, moins "
              "entre amis. Personne n'est obligé : un sourire et un bonjour suffisent.")

    d.dialogue('Dialogue', "Je ne comprends pas", [
        ("AMINA", "Pardon, monsieur. Je ne comprends pas.", True),
        ("PAUL", "Pas de problème. Je répète plus lentement.", True),
        ("AMINA", "Merci beaucoup.", True),
        ("PAUL", "De rien. Vous comprenez maintenant ?", True),
        ("AMINA", "Oui, merci. Vous êtes gentil.", True),
        ("PAUL", "Ça me fait plaisir. Bonne journée !", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Personne ne se fâche, personne n'est gêné. C'est exactement ce que le groupe "
             "a besoin de voir : dire « je ne comprends pas » ne coûte rien.")

    d.tableau('Analyse', "En arrivant, en partant",
              ['En arrivant', 'En partant'],
              [["Bonjour", "Bonne journée"],
               ["Bonsoir", "Bonne soirée"],
               ["Salut (entre amis)", "Salut · À demain"]],
              cle=0,
              note="On ne dit pas « bonjour » en partant.",
              notes="Diapo à photographier. C'est une erreur très fréquente et facile à "
                    "corriger.")

    d.regle("Merci, de rien",
            "Ici, on remercie souvent.",
            precision="On dit merci pour presque tout. La réponse est « <b>de rien</b> », "
                      "« <b>bienvenue</b> » ou « <b>ça me fait plaisir</b> ». Attention : "
                      "au Québec, « bienvenue » après un merci ne veut pas dire "
                      "« entrez » — cela veut dire « de rien ».",
            notes="Diapo à photographier. Cette confusion sur « bienvenue » revient chaque "
                  "année.")

    d.regle("Je ne comprends pas",
            "C'est une phrase de la langue, comme les autres.",
            precision="Ce n'est pas un aveu d'échec. Tout le monde la dit, même les gens "
                      "nés ici quand il y a du bruit. Et la meilleure suite est : "
                      "« <b>plus lentement, s'il vous plaît</b> » — parce que le problème "
                      "est presque toujours la vitesse, pas le volume.",
            notes="Diapo à photographier. C'est la diapositive la plus importante du "
                  "module. Faire répéter la phrase par tout le groupe, deux fois.")

    d.piege("Faire oui de la tête sans comprendre",
            "Oui, oui… et on se trompe de salle, de jour, de rendez-vous.",
            "Pardon, je ne comprends pas.",
            "Un « oui » poli coûte plus cher qu'un « pardon ». La personne en face ne peut "
            "pas deviner que vous n'avez pas compris — et elle ne le prendra pas mal.",
            notes="Le dire deux fois, et le rappeler à chaque séance du module.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Amina dit qu'elle ne comprend pas.", "vrai"),
        ("L'homme se fâche.", "faux — « pas de problème »"),
        ("Il répète plus lentement.", "vrai"),
        ("Amina remercie.", "vrai"),
    ], corrige=True, cols=1,
       notes="Quatre énoncés seulement, comme partout dans ce module.")

    d.pratique('Pratique · à deux', "Quand le dit-on ?",
               "L'un donne le moment, l'autre dit la phrase.", [
        ("Vous entrez le matin", "Bonjour"),
        ("Vous entrez le soir", "Bonsoir"),
        ("Vous partez le matin", "Bonne journée"),
        ("Vous partez le soir", "Bonne soirée"),
        ("Vous revenez demain", "À demain"),
    ], corrige=True, cols=1,
       notes="Utiliser l'exercice 3 du module. Puis faire jouer les entrées et les sorties "
             "à la porte de la classe, pour de vrai.")

    d.billet(
        "Notez ce que vous dites en entrant et en sortant, cette semaine.",
        exemples=[
            "Au dépanneur, à l'autobus, au centre.",
            "Est-ce qu'on vous a répondu ? Qu'est-ce qu'on a dit ?",
        ],
        notes="Devoir d'observation. Les réponses entendues (« bienvenue », « ça me fait "
              "plaisir ») nourrissent la séance suivante.")

    return d.save(dossier)
