# -*- coding: utf-8 -*-
"""A2 · Ce que la voix ajoute aux mots
Bloc A « Je découvre » · couleur indigo · phonétique · 75 min.
Source : exercice `prInto` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Ce que la voix ajoute aux mots",
        chapeau="Le niveau 8 ne demande plus qu'une chose à l'oreille : "
                "l'intonation expressive. Pas un son nouveau — une mélodie. "
                "Une même phrase de six mots peut dire trois choses.",
        duree='75 minutes')

    d.titre(notes="Séance de phonétique, et la seule du module : le programme du "
                  "niveau 8 ne porte qu'un savoir de phonétique, l'intonation "
                  "expressive. Aucun symbole au tableau — ce savoir s'entend et se "
                  "répète, il ne se lit pas.")

    d.objectifs([
        "reconnaître quatre intentions à la seule mélodie ;",
        "produire l'admiration, la déception et l'incompréhension ;",
        "entendre chez l'autre le signal qu'une réponse ne lui a pas plu ;",
        "cesser de monter la voix à la fin de chaque phrase.",
    ], notes="Le quatrième objectif est le vrai. C'est le défaut le plus répandu chez "
             "les adultes qui apprennent, et il vient de la prudence, pas de "
             "l'ignorance.")

    d.declencheur(
        'Écoute', "Trois fois la même phrase. Qu'est-ce qui change ?",
        pistes=[
            "« Six épisodes pour arriver à ça. »",
            "Dite lentement, la voix qui tombe dès le début.",
            "Dite vite, la voix qui monte à la fin.",
            "Dite en s'appuyant longuement sur « ça ».",
        ],
        notes="Dire les trois vous-même, sans annoncer laquelle est laquelle. Le groupe "
              "entend la différence avant de savoir la nommer, et c'est l'ordre "
              "correct.")

    d.tableau('Analyse', "Quatre mélodies, quatre intentions",
              ['La mélodie', 'Ce qu\'elle dit'],
              [["Elle s'élargit et appuie", "l'admiration"],
               ["Elle tombe dès la première syllabe", "la déception"],
               ["Elle freine, un silence, puis le mot", "l'incompréhension"],
               ["Elle monte d'un coup à la fin", "la surprise"]],
              cle=1,
              note="Aucun symbole. On les nomme par ce que fait la voix.",
              notes="Diapositive à photographier. Faire répéter chaque ligne deux fois, "
                    "en exagérant : l'exagération est ce qui fait entrer une mélodie "
                    "dans l'oreille.")

    d.cartes('Écoute', "Huit répliques, quatre intentions", [
        ("Quatorze secondes sur des bottes !", "admiration"),
        ("C'est la plus belle dernière page de l'année.", "admiration"),
        ("Ah bon. Moi qui attendais ça depuis six semaines.", "déception"),
        ("Bon. Je pensais qu'on parlerait du texte.", "déception"),
        ("Le mot « défendable », vous l'entendez comment ?", "incompréhension"),
        ("Là, j'ai perdu le fil de votre lecture.", "incompréhension"),
        ("Comment ça, elle ne détache pas la corde ?", "surprise"),
        ("Trois lectures de la même scène ?", "surprise"),
    ], notes="Les faire dire par les élèves, deux fois chacune, avant de donner "
             "l'intention. Corriger la mélodie, jamais les mots.")

    d.regle("L'admiration ralentit, elle ne monte pas",
            "Une admiration dite vite passe pour de la politesse. C'est la "
            "lenteur qui la rend crédible.",
            precision="La voix s'élargit et s'appuie longuement sur le mot qui porte "
                      "l'éloge. C'est le contraire de la surprise, qui grimpe "
                      "brusquement sur les deux dernières syllabes.",
            notes="Diapositive à photographier. Faire dire « c'est magnifique » deux "
                  "fois : une fois vite, une fois en tenant la deuxième syllabe. La "
                  "différence est entendue par tout le groupe.")

    d.piege('Piège', "monter la voix à chaque phrase",
            "descendre quand on affirme",
            "Une mélodie qui monte partout transforme chaque affirmation en "
            "question, et chaque lecture en demande d'autorisation. C'est le "
            "défaut le plus fréquent chez les adultes qui apprennent, et il ne "
            "vient pas de la langue : il vient de la prudence. On n'ose pas "
            "conclure, alors on laisse la phrase ouverte.",
            notes="Le montrer sur une phrase du module : « je crois qu'elle choisit "
                  "de rester ». Dite en montant, elle demande la permission. Dite en "
                  "descendant, elle ouvre la discussion.")

    d.pratique('Pratique', "Quelle intention entendez-vous ?",
               "Écoutez, puis nommez l'intention.", [
        ("Elle réussit tout ça sans une seule réplique.", "admiration"),
        ("Je pensais que c'était décidé.", "déception"),
        ("Vous avez bien dit quatorze secondes ?", "incompréhension"),
        ("Comment ça, l'auteure ne le dit jamais ?", "surprise"),
        ("Ah. Bon.", "déception"),
        ("C'est magnifique.", "admiration"),
    ], corrige=True,
       notes="Exercice `prInto` du module. Le faire à l'oral d'abord, puis à l'écran. "
             "Les élèves qui hésitent entre déception et incompréhension écoutent le "
             "début de la phrase : la déception tombe dès la première syllabe.")

    d.pratique('Production', "Dites la même phrase trois fois",
               "Une phrase, trois intentions. Le groupe devine.", [
        ("Elle ne détache pas la corde.", "constat, admiration, incompréhension"),
        ("Trois strophes seulement.", "surprise, déception, admiration"),
        ("Personne n'a rien dit.", "constat, déception, incompréhension"),
        ("Il ne l'a pas vérifié.", "constat, surprise, déception"),
    ], corrige=False,
       notes="En dyades, cinq minutes. Celui qui écoute nomme l'intention ; celui qui "
             "parle confirme. C'est le seul exercice du module où l'on se trompe "
             "utilement, parce que l'erreur s'entend tout de suite.")

    d.billet(
        "Écoutez quelqu'un cette semaine — à la radio, au travail, à la "
        "maison — et notez une phrase dont la mélodie disait plus que les mots.",
        exemples=[
            "La phrase, telle que vous l'avez entendue.",
            "Ce que la voix ajoutait : surprise, admiration, déception ?",
        ],
        notes="Devoir d'écoute, pas d'écriture. Les rapports servent d'entrée en "
              "matière à A3.")

    return d.save(dossier)
