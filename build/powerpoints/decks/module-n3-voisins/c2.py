# -*- coding: utf-8 -*-
"""C2 · Les trois renseignements de toute invitation.
Bloc C « Défi 2 · Venez prendre un café » · couleur ambre (écriture) · 60 min.
Source : exercice `t2inv`, mini-leçon `t2inv`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Les trois renseignements de toute invitation",
        chapeau="Quand, à quelle heure, où. Trois questions courtes, et "
                "trois réponses obligatoires : sans elles, l'invité ne "
                "sait pas où frapper.",
        duree='60 minutes')

    d.titre(notes="Séance d'écriture. Commencer par les billets de C1 : lire trois "
                  "invitations à voix haute et faire chercher au groupe ce qui manque. "
                  "C'est plus efficace que la règle donnée d'avance.")

    d.objectifs([
        "poser les questions « quand », « à quelle heure » et « où » ;",
        "donner les trois renseignements sans qu'on les demande ;",
        "dire qui est invité ;",
        "répondre poliment à « est-ce que j'apporte quelque chose ? ».",
    ])

    d.regle("Sans jour, ce n'est pas une invitation",
            "Venez prendre un café samedi, à deux heures, chez nous.",
            precision="« Un de ces jours », « bientôt », « quand vous "
                      "voulez » : ce sont des intentions polies, pas des "
                      "invitations. Personne ne vient jamais.",
            notes="Diapo à photographier. Beaucoup d'élèves auront écrit « bientôt » "
                  "dans leur billet de C1 — sans mauvaise volonté, c'est la formule "
                  "prudente. Nommer le problème sans le reprocher.")

    d.tableau('Analyse', "Les questions et leurs réponses",
              ["La question", "La réponse de Rachid"],
              [["C'est quand ?", "Samedi."],
               ["C'est à quelle heure ?", "À deux heures."],
               ["C'est où ?", "Chez nous, au 3A."],
               ["Qui est-ce qui vient ?", "Les voisins de l'immeuble."]],
              cle=1,
              note="On donne les trois premières sans attendre qu'on les "
                   "demande. La quatrième se donne si on la connaît.",
              notes="Diapo à photographier. Faire remarquer la forme de la troisième "
                    "réponse : « chez nous » ne suffit pas dans un immeuble, il faut le "
                    "numéro de porte.")

    d.pratique('Écriture', "Complétez la question ou la réponse",
               "Employez « quand », « à quelle heure », « où », « qui » ou « quelque chose ».", [
        ("— C'est ___ ? — Samedi.", "quand"),
        ("— Et c'est ___ ? — À deux heures.", "à quelle heure"),
        ("— C'est ___ ? — Chez nous, au 3A.", "où"),
        ("— ___ est-ce qui vient ? — Les voisins de l'immeuble.", "Qui"),
        ("— Est-ce que j'apporte ___ ? — Rien du tout, merci.", "quelque chose"),
        ("— On se voit ___, alors ? — Samedi, à deux heures.", "quand"),
    ], corrige=True,
       notes="C'est l'exercice `t2inv` du module interactif, mot pour mot. Insister sur "
             "l'accent grave de « où » : sans lui, c'est le « ou » du choix.")

    d.cartes("Deux façons de répondre à « j'apporte quelque chose ? »", "Et ce que chacune dit", [
        ("« Apportez seulement votre bonne humeur »",
         "La réponse de celui qui reçoit et qui ne veut rien demander. Elle est chaleureuse "
         "et elle ferme la question."),
        ("« Un dessert, si vous voulez »",
         "Quand on accepte vraiment de l'aide. On nomme une chose précise, jamais « ce que "
         "vous voulez » — c'est plus difficile pour l'invité."),
        ("Ce que l'invité fait quand même",
         "Il apporte souvent quelque chose. Manon insiste avec ses biscuits, et c'est "
         "normal : on accepte en remerciant."),
        ("Ce qu'on ne demande pas",
         "De l'argent, ou une chose chère. Entre voisins, l'invitation reste petite — "
         "c'est ce qui la rend possible."),
    ], notes="La quatrième carte évite un vrai malentendu : dans plusieurs pays, arriver "
             "les mains vides est impoli, et l'invité se met en dépense. Le dire.")

    d.piege("Inviter sans dire où",
            "Venez prendre un café samedi à deux heures !",
            "Venez prendre un café samedi à deux heures, chez nous, au 3A.",
            "Dans un immeuble, « chez nous » ne suffit pas : six portes se "
            "ressemblent. Le numéro de logement fait partie de l'adresse, "
            "au même titre que le numéro de la rue.",
            notes="Faire dire à chacun son propre numéro de porte à voix haute. "
                  "Plusieurs ne l'ont jamais prononcé en français.")

    d.pratique('Écriture', "Écrivez l'invitation complète",
               "Une phrase, avec les trois renseignements dans l'ordre.", [
        ("Un café, chez vous, dimanche après-midi.", "Venez prendre un café dimanche, à deux heures, chez moi au 402."),
        ("Un souper, samedi soir, chez le voisin du premier.", "Venez souper samedi, à six heures, chez moi au 1B."),
        ("Un thé, mercredi, dans la cour de l'immeuble.", "Venez prendre un thé mercredi, à trois heures, dans la cour."),
        ("Une fête pour l'anniversaire de votre fils.", "Venez fêter les cinq ans de mon fils samedi, à une heure, au 3A."),
    ], corrige=True, cols=1,
       notes="Corriger seulement la présence des trois renseignements et leur ordre. La "
             "forme du verbe se travaille en C3.")

    d.billet(
        "Réécrivez votre invitation de C1, complète.",
        exemples=[
            "Le jour, l'heure, l'endroit avec le numéro de porte.",
            "Ajoutez pourquoi vous invitez : une seule phrase.",
        ],
        notes="Devoir court. C'est la deuxième version de la même invitation. Elle "
              "servira de brouillon au carton écrit de E1 — le dire, ça change le soin "
              "qu'on y met.")

    return d.save(dossier)
