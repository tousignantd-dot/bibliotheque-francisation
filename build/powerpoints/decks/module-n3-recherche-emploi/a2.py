# -*- coding: utf-8 -*-
"""A2 · Le é de métier, le è de salaire.
Bloc A « Je découvre » · couleur indigo · 60 min. Graphie-phonie.
Source du module : exercice `prPhon` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre='Le é de métier, le è de salaire',
        chapeau="Deux sons voisins, et deux mots du travail pour les tenir. "
                "Ce n'est pas un détail de prononciation : c'est ce qui "
                "sépare « j'ai travaillé » de « je travaillais ».",
        duree='60 minutes')

    d.titre(notes="Séance de graphie-phonie. Prévoir un miroir de poche ou demander à "
                  "chacun de poser une main sous le menton : le mouvement de la "
                  "mâchoire est ce qui rend la différence visible.")

    d.objectifs([
        "entendre la différence entre le é fermé et le è ouvert ;",
        "reconnaître les écritures de chaque son ;",
        "prononcer les mots du travail sans hésiter ;",
        "ne plus dire le r final des verbes en -er.",
    ])

    d.declencheur(
        'Écoute', "Métier, salaire. Est-ce le même son ?",
        pistes=[
            "Dites les deux mots à voix haute, l'un après l'autre.",
            "Où est votre mâchoire pour le premier ? Pour le second ?",
            "Lequel des deux fait sourire ?",
            "Est-ce que votre langue a ces deux sons ?",
        ],
        notes="Faire dire les deux mots dix fois en alternance, sans explication. "
              "L'oreille précède la règle : la règle vient à la diapo suivante.")

    d.tableau('Analyse', "Deux sons, deux bouches, plusieurs écritures",
              ['Le son', 'La bouche', "On l'écrit"],
              [["é fermé, comme dans métier", "presque fermée, lèvres étirées", "é, er, ez"],
               ["è ouvert, comme dans salaire", "ouverte, mâchoire basse", "ai, è, ê, ei"],
               ["é : un employé, un congé", "on sourit presque", "embaucher, vous engagez"],
               ["è : un horaire, la semaine", "un doigt entre les dents", "un formulaire, une aide"]],
              cle=0,
              note="Deux mots repères : métier pour le fermé, salaire pour l'ouvert.",
              notes="Diapo à photographier. Ne pas allonger la liste des écritures : "
                    "celles-ci couvrent tous les mots du module.")

    d.regle("Le r final d'un verbe en -er ne se prononce jamais",
            "Embaucher se dit « embauché ».",
            precision="Travailler, chercher, engager, demander : la fin s'entend « é » "
                      "et rien d'autre. C'est vrai de tous les verbes du premier groupe, "
                      "et c'est la moitié des verbes du module.",
            notes="Diapo à photographier. Faire dire la liste en chaîne, un verbe par "
                  "élève, sans reprendre : c'est la vitesse qui installe le réflexe.")

    d.cartes("Les deux sons dans les mots du module", "À écouter et à répéter", [
        ("Le son é — bouche presque fermée",
         "un métier, un employé, un congé, embaucher, vous engagez. Les lèvres "
         "s'étirent comme au début d'un sourire ; la mâchoire ne bouge presque pas."),
        ("Le son è — bouche ouverte",
         "un salaire, un horaire, un formulaire, la semaine, une aide. La mâchoire "
         "descend d'un cran : on peut glisser un doigt entre les dents."),
        ("Le mot qui contient les deux",
         "« Un employé reçoit un salaire. » Garder cette phrase comme repère : elle "
         "redonne les deux sons chaque fois qu'on la dit."),
        ("Ce qui trompe l'œil",
         "les lettres ai s'entendent è, jamais é. Salaire, horaire, formulaire, aide : "
         "les quatre mots les plus fréquents d'une offre d'emploi."),
    ], notes="Faire répéter chaque carte par le groupe entier avant de passer à la "
             "suivante. Corriger la mâchoire, pas la lettre.")

    d.piege("Fermer le è de salaire",
            "Le salére est de seize dollars.",
            "Le salaire est de seize dollars.",
            "Les lettres ai ouvrent le son. Fermé, le mot ne ressemble plus à rien et "
            "l'interlocuteur cherche ce qu'on a voulu dire au lieu d'écouter la suite. "
            "Même chose pour horaire, formulaire et aide.",
            notes="Faire entendre les deux versions au groupe et demander laquelle "
                  "ressemble à ce qu'ils entendent au commerce.")

    d.pratique('Écoute', "Le son de métier, ou le son de salaire ?",
               "L'enseignante dit le mot ; vous dites quel son vous entendez.", [
        ("un métier", "le son de métier"),
        ("un salaire", "le son de salaire"),
        ("embaucher", "le son de métier"),
        ("un horaire", "le son de salaire"),
        ("un employé", "le son de métier"),
        ("un formulaire", "le son de salaire"),
        ("un congé", "le son de métier"),
        ("la semaine", "le son de salaire"),
    ], corrige=True, cols=2,
       notes="Même liste que l'exercice prPhon du module. Dire les mots deux fois, "
             "puis les faire redire par le groupe avant de donner la réponse.")

    d.pratique('Lecture', "Six phrases à lire à voix haute",
               "Chacun lit une phrase. Le groupe dit quels sons il a entendus.", [
        ("C'est un métier que j'aimerais apprendre.", "é deux fois"),
        ("Le salaire est de seize dollars de l'heure.", "è trois fois"),
        ("La boulangerie va embaucher quelqu'un.", "é à la fin du verbe"),
        ("Mon horaire va de neuf heures à une heure.", "è au début"),
        ("Vous engagez encore ? J'ai vu votre affiche.", "é, puis é"),
        ("Je remplis le formulaire cette semaine.", "è deux fois"),
    ], corrige=True,
       notes="Ne pas corriger la grammaire pendant cette diapo : seulement les deux "
             "sons. Les phrases reviennent telles quelles dans les défis.")

    d.billet(
        "Écrivez deux mots avec le son é et deux mots avec le son è.",
        exemples=[
            "Prenez-les dans les mots du module, pas ailleurs.",
            "Soulignez la lettre ou les lettres qui font le son.",
        ],
        notes="Deux minutes. Ramasser : les erreurs d'écriture révèlent qui confond "
              "encore les deux sons, avant que le défi 2 n'arrive avec ses salaires.")

    return d.save(dossier)
