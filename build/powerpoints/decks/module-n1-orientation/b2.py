# -*- coding: utf-8 -*-
"""B2 · C'est la cafétéria.
Bloc B « Défi 1 · Le mot sur la porte » · couleur ambre (écriture) · 60 min.
Source : exercices `t1art` et `t1cest`, mini-leçons `t1art` et `t1cest`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre="C'est la cafétéria",
        chapeau="Deux petits mots font tout le travail : celui qui se met "
                "devant le nom, et « c'est », qui sert à nommer n'importe quoi.",
        duree='60 minutes')

    d.titre(notes="Séance de langue, assise, au cahier. Elle vient après B1 parce qu'on "
                  "ne met pas un article devant un mot qu'on ne connaît pas encore.")

    d.objectifs([
        "employer le, la, les, l' devant le nom d'un lieu ;",
        "nommer un endroit avec « c'est » ;",
        "dire que non avec « ce n'est pas » ;",
        "poser la question « c'est ici ? ».",
    ])

    d.declencheur(
        'Observation', "Pourquoi pas le même petit mot ?",
        pistes=[
            "la cafétéria",
            "le vestiaire",
            "les toilettes",
            "l'accueil",
        ],
        notes="Écrire les quatre au tableau. Laisser chercher. La réponse honnête est "
              "qu'il n'y a pas de logique à trouver : le dire tout de suite plutôt que "
              "de laisser chercher dix minutes.")

    d.regle("Le petit mot fait partie du nom",
            "On l'apprend avec lui, jamais après.",
            precision="<b>la</b> cafétéria · <b>le</b> vestiaire · <b>les</b> "
                      "toilettes · <b>l'</b>accueil. Il ne se devine pas. « Cafétéria » "
                      "tout seul ne s'apprend pas ; « la cafétéria », oui.",
            notes="Diapositive à photographier. Insister : c'est une habitude à prendre "
                  "dès le premier mot, et elle épargne des années de correction.")

    d.tableau('Analyse', "Quand met-on lequel ?",
              ['Le petit mot', 'Devant quoi'],
              [["la", "un nom féminin : la sortie"],
               ["le", "un nom masculin : le vestiaire"],
               ["les", "un nom au pluriel : les toilettes"],
               ["l'", "un nom qui commence par une voyelle : l'accueil"]],
              cle=0,
              note="« Les toilettes » est toujours au pluriel, même pour une seule salle.",
              notes="Diapositive à photographier. Ne pas expliquer le genre : à ce "
                    "stade, masculin et féminin sont deux étiquettes, rien de plus.")

    d.pratique('Pratique', "Le, la, les ou l' ?",
               "Complétez avec le bon petit mot.", [
        ("___ cafétéria est au premier étage.", "la"),
        ("___ toilettes sont au bout du corridor.", "les"),
        ("___ vestiaire est à côté de l'entrée.", "le"),
        ("___ sortie est à droite.", "la"),
        ("Je vais à ___ accueil.", "l'"),
        ("___ service de garde est au rez-de-chaussée.", "le"),
    ], corrige=True, cols=2,
       notes="Vingt minutes au cahier. C'est l'exercice le plus long de la séance.")

    d.regle("C'est · Ce n'est pas · C'est ici ?",
            "Trois phrases devant une porte.",
            precision="On <b>nomme</b> : « C'est la cafétéria. » On <b>corrige</b> : "
                      "« Ce n'est pas la cafétéria. » On <b>demande</b> : « C'est "
                      "ici ? » — les mêmes mots, la voix qui monte à la fin.",
            notes="Diapositive à photographier. Faire dire les trois versions à voix "
                  "haute, en chœur, en exagérant la montée de la voix.")

    d.pratique('Pratique', "C'est, ou ce n'est pas ?",
               "Regardez le panneau, puis complétez.", [
        ("Le panneau dit CAFÉTÉRIA. ___ la cafétéria.", "c'est"),
        ("Vous cherchez les toilettes, le panneau dit ACCUEIL.", "ce n'est pas"),
        ("Le panneau dit SORTIE. ___ la sortie.", "c'est"),
        ("Vous demandez : le service de garde, ___ ici ?", "c'est"),
    ], corrige=True, cols=1,
       notes="Faire jouer la scène debout, deux par deux, après la correction.")

    d.piege("Oublier le petit mot après « c'est »",
            "« C'est cafétéria. »",
            "« C'est la cafétéria. »",
            "Le petit mot ne disparaît jamais, même après « c'est ». C'est l'erreur la "
            "plus fréquente du module, et elle vient de ce que le panneau, lui, écrit "
            "le mot tout seul : CAFÉTÉRIA. Le panneau est un titre, pas une phrase.",
            notes="Excellente remarque à faire faire par le groupe plutôt que par vous : "
                  "« pourquoi le panneau n'écrit-il pas “la” ? »")

    d.billet(
        "Écrivez trois phrases avec « c'est ».",
        exemples=[
            "Une pour la cafétéria, une pour les toilettes, une pour la sortie.",
            "N'oubliez pas le petit mot.",
        ],
        notes="Deux minutes. Ramasser et corriger : c'est le meilleur relevé du bloc B.")

    return d.save(dossier)
