# -*- coding: utf-8 -*-
"""A4 · J'ai mal à la tête, j'ai mal au dos.
Bloc A « Je découvre » · couleur ambre (écriture) · 75 min.
Source : exercice `prCorps`, mini-leçon `prCorps`.

Le lexique du programme nomme « les principales parties du corps » pour cette
situation. Elles ne servent à rien seules : ce qui compte, c'est la phrase
« j'ai mal à… » et le petit mot qui suit.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="J'ai mal à la tête, j'ai mal au dos",
        chapeau="Une seule phrase à retenir, et quatre petits mots à choisir : "
                "au, à la, à l', aux. C'est la première chose qu'on dit au "
                "comptoir.",
        duree='75 minutes')

    d.titre(notes="Séance d'écriture et de langue. Prévoir une silhouette du corps au "
                  "tableau : les mots se retiennent mieux montrés que traduits.")

    d.objectifs([
        "nommer les principales parties du corps ;",
        "dire où on a mal avec « j'ai mal à… » ;",
        "choisir entre au, à la, à l' et aux ;",
        "écrire six phrases justes.",
    ])

    d.declencheur(
        'Mise en situation', "Le pharmacien demande : « Où avez-vous mal ? »",
        pistes=[
            "Qu'est-ce que vous répondez, en une phrase ?",
            "Est-ce qu'on peut montrer avec la main plutôt que de le dire ?",
            "Quelles parties du corps connaissez-vous déjà en français ?",
        ],
        notes="Faire monter les mots connus au tableau avant d'ouvrir la diapositive "
              "suivante. Le groupe en connaît toujours plus qu'il ne croit.")

    d.regle("La phrase de base",
            "« J'ai mal à… »",
            precision="Le petit mot « à » est obligatoire, et il change de "
                      "forme selon le mot qui suit : au dos, à la tête, à "
                      "l'oreille, aux dents. Sans lui, la phrase ne se dit pas.",
            notes="Diapositive à photographier. Faire répéter la phrase seule, puis avec "
                  "quatre parties du corps différentes.")

    d.tableau('Analyse', "Les quatre formes, et quand les employer",
              ["La forme", "Quand", "Exemples"],
              [["au", "mot masculin", "j'ai mal au dos"],
               ["à la", "mot féminin", "j'ai mal à la tête"],
               ["à l'", "devant une voyelle", "j'ai mal à l'oreille"],
               ["aux", "pluriel", "j'ai mal aux dents"]],
              cle=0,
              note="Une seule forme au pluriel, masculin comme féminin : aux.",
              notes="Diapositive à photographier. C'est le tableau de référence de toute "
                    "la séance ; le laisser affiché pendant les exercices.")

    d.cartes("Le corps", "Les mots à connaître", [
        ("la tête, la gorge, la bouche",
         "Le haut du corps. Tous féminins : « j'ai mal à la tête ». La gorge est la "
         "partie la plus nommée à la pharmacie, avec la tête."),
        ("le dos, le ventre, le cou",
         "Le tronc. Tous masculins : « j'ai mal au dos ». Le mal de dos est le motif de "
         "consultation le plus fréquent chez les adultes qui travaillent debout."),
        ("le bras, la main, la jambe, le pied",
         "Les membres. Attention : « le bras » est masculin, « la main » et « la jambe » "
         "sont féminines. On dit au bras, à la main, à la jambe, au pied."),
        ("les dents, les yeux, les oreilles",
         "Ce qui va souvent par deux ou par plusieurs : « j'ai mal aux dents », « j'ai "
         "mal aux yeux ». Au singulier : à la dent, à l'œil, à l'oreille."),
    ], notes="Montrer chaque partie sur soi en la nommant. Faire refaire le geste par le "
             "groupe : les mots du corps s'apprennent avec le corps.")

    d.piege('Écriture',
            "« j'ai mal la tête »",
            "« j'ai mal à la tête »",
            "Oublier le « à » est la faute la plus fréquente, et elle vient souvent de "
            "la langue d'origine, où la préposition n'existe pas ici. Le « à » est le "
            "mot le plus court de la phrase et le plus obligatoire.",
            notes="Écrire les deux formes au tableau et faire barrer la fausse par un "
                  "élève. Le geste marque davantage qu'une explication.")

    d.pratique('Application', "Au, à la, à l' ou aux ?",
               "Complétez chaque phrase.", [
        ("J'ai mal ___ tête depuis ce matin.", "à la"),
        ("Mon garçon a mal ___ gorge.", "à la"),
        ("J'ai mal ___ dos quand je travaille.", "au"),
        ("Elle a mal ___ dents depuis deux jours.", "aux"),
        ("J'ai mal ___ oreille gauche.", "à l'"),
        ("Il a mal ___ ventre après les repas.", "au"),
    ], corrige=True,
       notes="Ce sont les six items de l'exercice interactif. Les faire d'abord à "
             "l'oral, puis les écrire : la faute se voit à l'écrit, pas à l'oreille.")

    d.pratique('Production', "Dites-le au pharmacien",
               "Faites une phrase complète pour chaque situation.", [
        ("Vous avez mal en avalant.", "« J'ai mal à la gorge. »"),
        ("Vous avez soulevé une boîte trop lourde.", "« Je me suis fait mal au dos. »"),
        ("Votre enfant tient sa joue depuis hier.", "« Il a mal aux dents. »"),
        ("Vous entendez mal d'un côté.", "« J'ai mal à l'oreille. »"),
    ], corrige=True,
       notes="Faire dire les phrases debout, comme au comptoir. Ajouter « depuis » "
             "quand un élève est prêt : la séance B3 le reprendra.")

    d.billet(
        "Écrivez quatre phrases : « J'ai mal… » avec les quatre formes.",
        exemples=[
            "Une phrase avec au, une avec à la, une avec à l', une avec aux.",
            "Ajoutez depuis quand, si vous le pouvez déjà.",
        ],
        notes="Devoir court. Il ferme le bloc A et ouvre le défi 1, où l'on ajoutera "
              "le malaise et la durée.")

    return d.save(dossier)
