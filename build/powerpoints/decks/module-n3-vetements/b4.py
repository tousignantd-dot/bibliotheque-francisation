# -*- coding: utf-8 -*-
"""B4 · Ce qu'on entend dans le magasin.
Bloc B « Défi 1 · Demander ce qu'on cherche » · couleur acier · 60 min.
Source : exercices `t1demander` et `t1essayage`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-vetements/images/')


def build(dossier):
    d = Deck(
        code='B4', section='acier',
        titre="Ce qu'on entend dans le magasin",
        chapeau="La conseillère parle vite, parce qu'elle dit les mêmes "
                "phrases cent fois par jour. Les reconnaître d'avance, c'est "
                "n'avoir plus qu'à répondre.",
        duree='60 minutes')

    d.titre(notes="Séance de compréhension orale. Prévoir le son. Fin du défi 1 : la "
                  "séance rassemble tout ce qui a été vu depuis B1.")

    d.objectifs([
        "reconnaître six phrases courantes d'une conseillère ;",
        "comprendre ce qu'elles demandent réellement ;",
        "répondre en une phrase courte ;",
        "saluer et remercier au bon moment.",
    ])

    d.declencheur(
        'Observation', "Vous entrez. Que se passe-t-il en premier ?",
        image=IMG + 'cabine-essayage.jpg',
        pistes=[
            "Quelqu'un vous regarde et vous dit quelque chose.",
            "Que dit-on, d'habitude ?",
            "Faut-il répondre tout de suite ?",
            "Et si vous voulez seulement regarder ?",
        ],
        notes="« Je regarde seulement, merci » est une réponse parfaitement acceptable et "
              "très employée. Beaucoup d'élèves ne savent pas qu'elle existe.")

    d.tableau('Analyse', "Ce qu'elles demandent vraiment",
              ['La conseillère dit', 'Elle demande'],
              [["Vous portez quelle taille ?", "petit, moyen ou grand"],
               ["Je vous le décroche.", "rien — elle vous aide"],
               ["La cabine est au fond.", "rien — elle vous indique"],
               ["On ne l'a plus en moyen.", "d'essayer une autre taille"],
               ["Vous le prenez ?", "si vous achetez"]],
              cle=0,
              note="Deux de ces phrases ne demandent rien : il suffit de remercier.",
              notes="Diapo à photographier. La remarque du bas soulage : on n'a pas à "
                    "répondre à tout. Ajouter « il vous fait bien », qui est un avis.")

    d.regle("Trois moments, trois phrases",
            "Bonjour · Je cherche… · Merci",
            precision="On salue en entrant, on dit ce qu'on cherche, on remercie en "
                      "partant. Entre les deux, il n'y a que des réponses courtes à donner. "
                      "Ces trois phrases-là ne changent jamais, quel que soit le magasin.",
            notes="Diapo à photographier. Faire répéter les trois par tout le groupe.")

    d.cartes("Quatre réponses courtes qui suffisent", "À dire sans hésiter", [
        ("Quand on vous accueille",
         "« Bonjour. Je cherche un manteau. » Ou, si vous voulez regarder : « Bonjour, je "
         "regarde seulement, merci. »"),
        ("Quand on vous demande la taille",
         "« Du moyen. » Ou : « Je ne connais pas ma taille ici. »"),
        ("Quand on vous propose un vêtement",
         "« Je peux l'essayer ? » — la phrase la plus utile du défi."),
        ("Quand vous décidez",
         "« Je le prends. » Ou : « Je vais y penser, merci. » Les deux se disent, et la "
         "seconde ne vexe personne."),
    ], notes="La dernière carte est importante : beaucoup d'élèves achètent parce qu'ils "
             "ne savent pas comment dire non.")

    d.piege("Croire qu'il faut tout comprendre",
            "Elle a dit quelque chose, je n'ai pas compris… je pars.",
            "Pardon, vous pouvez répéter ?",
            "Une phrase manquée n'oblige à rien : on demande de répéter, et on repart avec "
            "ce qu'on était venu chercher. Partir sans rien dire est la seule issue qui "
            "coûte quelque chose.",
            notes="Faire répéter « Pardon, vous pouvez répéter ? » — c'est la phrase de "
                  "secours de tout le module.")

    d.pratique('Pratique · 1 de 2', "Que dites-vous ?",
               "Une phrase pour chaque situation.", [
        ("Vous entrez et une conseillère vous regarde.", "Bonjour."),
        ("Vous cherchez un manteau noir.", "Je cherche un manteau noir."),
        ("On vous demande votre taille.", "Je porte du moyen."),
        ("Vous voulez essayer.", "Je peux l'essayer ?"),
        ("Vous cherchez la cabine.", "Où est la cabine d'essayage ?"),
        ("On vient de vous aider.", "Merci beaucoup."),
    ], corrige=True,
       notes="Utiliser l'exercice 4 du défi 1. Faire jouer les échanges à deux.")

    d.pratique('Pratique · 2 de 2', "Qu'est-ce que ça veut dire ?",
               "Associez la phrase à son sens.", [
        ("« Je vous le décroche du cintre. »", "elle enlève le vêtement de son crochet"),
        ("« Il vous fait bien. »", "le vêtement est à votre grandeur"),
        ("« On ne l'a plus en moyen. »", "cette taille est vendue"),
        ("« Vous le prenez ? »", "décidez-vous de l'acheter ?"),
    ], corrige=True, cols=1,
       notes="Utiliser l'exercice 5 du défi 1. Insister sur « il vous fait bien » : c'est "
             "un avis, pas une obligation d'acheter.")

    d.billet(
        "Allez dans un magasin cette semaine et écoutez.",
        exemples=[
            "Notez deux phrases que vous avez entendues.",
            "Vous n'êtes pas obligé d'acheter quoi que ce soit.",
        ],
        notes="Fin du défi 1. Le devoir est une observation, pas un achat : le dire "
              "clairement au groupe.")

    return d.save(dossier)
