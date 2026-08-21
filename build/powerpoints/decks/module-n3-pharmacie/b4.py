# -*- coding: utf-8 -*-
"""B4 · Le pharmacien ou le client ?
Bloc B « Défi 1 · Dire ce qui ne va pas » · couleur indigo · 60 min.
Source : exercice `t1qui` (cartes à écouter), révision du bloc B.

Séance d'écoute : reconnaître qui parle avant de comprendre chaque mot est
une compétence en soi, et le programme la nomme en compréhension orale.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='indigo',
        titre='Le pharmacien ou le client ?',
        chapeau="Au comptoir, les deux voix ne disent pas les mêmes choses. "
                "L'un pose des questions, l'autre raconte. Reconnaître laquelle "
                "parle, c'est déjà comprendre la moitié.",
        duree='60 minutes')

    d.titre(notes="Séance d'écoute et de bilan du défi 1. Prévoir les haut-parleurs et, "
                  "si possible, un casque par élève pour la deuxième moitié.")

    d.objectifs([
        "reconnaître qui parle, du pharmacien ou du client ;",
        "repérer les marques de la question et de la réponse ;",
        "réemployer les acquis du bloc B ;",
        "tenir un échange de quatre répliques en paires.",
    ])

    d.declencheur(
        'Écoute', "Qui dit cette phrase ?",
        pistes=[
            "« Depuis quand est-ce que ça dure ? »",
            "« Je tousse beaucoup et je ne dors pas. »",
            "« Est-ce que vous prenez d'autres médicaments ? »",
            "Qu'est-ce qui vous a permis de deviner ?",
        ],
        notes="Dire les phrases sans les écrire. Faire nommer l'indice : le vouvoiement, "
              "la forme interrogative, le « je » qui raconte.")

    d.tableau('Analyse', "Deux voix, deux façons de parler",
              ["Le pharmacien", "Le client"],
              [["« est-ce que vous… »", "« je tousse »"],
               ["il pose des questions", "il répond, et il en pose"],
               ["« allez voir un médecin »", "« qu'est-ce que je fais ? »"],
               ["« persiste », « administrer »", "« j'ai mal », « depuis »"]],
              cle=0,
              note="Le vouvoiement va dans les deux sens : personne ne se tutoie.",
              notes="Diapositive à photographier. Faire remarquer que le client aussi "
                    "vouvoie : ce n'est pas une marque d'autorité, c'est la distance "
                    "normale d'un commerce.")

    d.pratique('Discrimination', "Qui parle ?",
               "Écoutez chaque phrase, puis dites qui la dit.", [
        ("Depuis quand est-ce que ça dure ?", "le pharmacien"),
        ("Je tousse beaucoup et je ne dors pas.", "le client"),
        ("Est-ce que vous prenez d'autres médicaments ?", "le pharmacien"),
        ("J'ai mal à la gorge le matin.", "le client"),
        ("Je vais vous donner un sirop.", "le pharmacien"),
        ("Est-ce que je peux acheter ça sans ordonnance ?", "le client"),
        ("Si ça persiste, allez voir un médecin.", "le pharmacien"),
        ("Merci beaucoup. Bonne journée.", "le client"),
    ], corrige=True,
       notes="Les huit items de l'exercice interactif. Les dire deux fois, la seconde à "
             "vitesse normale. Faire justifier chaque réponse par un indice.")

    d.regle("La question polie du client",
            "« Est-ce que je peux… ? »",
            precision="Le client aussi pose des questions, et il en a le droit : "
                      "le prix, la durée, ce qu'il y a dans le médicament, ce "
                      "qu'il faut faire si ça ne va pas mieux. Un pharmacien "
                      "s'attend à être questionné.",
            notes="Diapositive à photographier. Beaucoup d'élèves n'osent pas demander. "
                  "Dire clairement que la question fait partie du travail du pharmacien.")

    d.pratique('Réemploi', "Tout le bloc B en quatre répliques",
               "En paires : jouez l'échange, puis changez de rôle.", [
        ("Le pharmacien salue et demande ce qu'il peut faire.", "« Bonjour. Qu'est-ce que je peux faire pour vous ? »"),
        ("Le client nomme son malaise.", "« Je tousse et j'ai mal à la gorge. »"),
        ("Le pharmacien demande depuis quand.", "« Depuis quand est-ce que ça dure ? »"),
        ("Le client répond et pose une question.", "« Depuis quatre jours. Est-ce que je peux prendre un sirop ? »"),
    ], corrige=False,
       notes="Circuler pendant les paires. Corriger seulement deux choses : le "
             "vouvoiement et la préposition « depuis ». Le reste attend.")

    d.billet(
        "Écrivez l'échange que vous venez de jouer, en quatre répliques.",
        exemples=[
            "Deux répliques pour le pharmacien, deux pour vous.",
            "Employez « depuis » au moins une fois.",
        ],
        notes="Devoir de fin de bloc. Ramasser : ces quatre répliques deviendront le "
              "brouillon de la production orale de la séance E1.")

    return d.save(dossier)
