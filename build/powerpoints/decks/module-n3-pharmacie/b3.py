# -*- coding: utf-8 -*-
"""B3 · Depuis quand est-ce que ça dure ?
Bloc B « Défi 1 · Dire ce qui ne va pas » · couleur ambre (écriture) · 75 min.
Source : exercice `t1depuis`, mini-leçon `t1depuis`.

Le programme nomme ces mots pour cette situation : dans, depuis, ça fait,
il y a, voilà, pendant. Ils ne veulent pas dire la même chose.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre='Depuis quand est-ce que ça dure ?',
        chapeau="Une toux de deux jours n'est pas une toux de deux semaines : "
                "la réponse change le conseil. Cinq petits mots pour la donner, "
                "et ils ne sont pas interchangeables.",
        duree='75 minutes')

    d.titre(notes="Séance de langue et d'écriture. Les cinq mots servent bien au-delà "
                  "de la pharmacie : au travail, à l'école, chez le médecin. Le dire au "
                  "groupe, ça motive.")

    d.objectifs([
        "répondre à « depuis quand ? » ;",
        "distinguer depuis, ça fait… que, il y a, pendant et dans ;",
        "écrire six phrases justes ;",
        "poser soi-même la question à un camarade.",
    ])

    d.declencheur(
        'Mise en situation', "« Je tousse depuis quatre jours » ou « il y a quatre jours » ?",
        pistes=[
            "Dans quel cas est-ce que ça continue encore aujourd'hui ?",
            "Dans quel cas est-ce que c'est fini ?",
            "Comment dit-on la durée dans votre langue ?",
        ],
        notes="Faire voter à main levée sur les deux phrases avant d'expliquer. La "
              "confusion est presque générale, et c'est normal.")

    d.tableau('Analyse', "Les cinq mots, et ce qu'ils disent",
              ["Le mot", "Ce qu'il dit"],
              [["depuis quatre jours", "ça continue aujourd'hui"],
               ["ça fait quatre jours que…", "la même chose, dite autrement"],
               ["il y a deux jours", "un moment fini, dans le passé"],
               ["pendant sept jours", "toute la durée, du début à la fin"],
               ["dans six semaines", "le temps qu'il reste à attendre"]],
              cle=0,
              note="Trois servent au comptoir, deux sur l'étiquette et au calendrier.",
              notes="Diapositive à photographier. C'est le tableau de référence de la "
                    "séance ; le laisser affiché pendant tous les exercices.")

    d.regle("Ce qui dure encore",
            "« Je tousse depuis quatre jours. »",
            precision="Après « depuis », on met soit une durée — quatre jours, "
                      "deux semaines —, soit un moment de départ : depuis "
                      "samedi, depuis hier soir. Dans les deux cas, ça continue "
                      "au moment où l'on parle.",
            notes="Diapositive à photographier. Faire produire les deux formes par le "
                  "groupe : « depuis quatre jours », « depuis samedi ».")

    d.regle("La même chose, autrement",
            "« Ça fait quatre jours que je tousse. »",
            precision="Deux morceaux : « ça fait » au début, « que » au milieu. "
                      "Au Québec, on l'entend au moins autant que « depuis ». "
                      "Oublier le « que » est la faute la plus fréquente.",
            notes="Diapositive à photographier. Faire transformer trois phrases avec "
                  "« depuis » en phrases avec « ça fait… que ».")

    d.piege('Choix du mot',
            "« je tousse il y a quatre jours »",
            "« je tousse depuis quatre jours »",
            "« Il y a » ferme le moment : l'action est arrivée une fois et c'est fini. "
            "« Depuis » l'ouvre jusqu'à aujourd'hui. Si vous toussez encore en parlant, "
            "c'est forcément « depuis ».",
            notes="Le test à donner aux élèves : « est-ce que ça continue en ce moment ? "
                  "oui → depuis ; non → il y a ». Ça règle presque tous les cas.")

    d.pratique('Application', "Depuis, ça fait, il y a, pendant ou dans ?",
               "Complétez chaque phrase.", [
        ("Je tousse ___ quatre jours.", "depuis"),
        ("___ deux jours que j'ai mal à la gorge.", "Ça fait"),
        ("Je me suis coupé le doigt ___ trois jours.", "il y a"),
        ("Prenez un comprimé ___ sept jours.", "pendant"),
        ("Mon rendez-vous chez le médecin est ___ six semaines.", "dans"),
        ("Il a de la fièvre ___ hier soir.", "depuis"),
    ], corrige=True,
       notes="Les six items de l'exercice interactif. Les faire à l'écrit, puis "
             "corriger à l'oral en demandant chaque fois « ça continue ou c'est fini ? ».")

    d.pratique('Production', "Posez la question, répondez",
               "En paires : l'un joue le pharmacien, l'autre le client.", [
        ("« Depuis quand est-ce que ça dure ? »", "« Depuis trois jours. »"),
        ("« Depuis quand avez-vous mal à la gorge ? »", "« Ça fait deux jours que j'ai mal. »"),
        ("« Quand est-ce que vous vous êtes coupé ? »", "« Il y a une semaine. »"),
        ("« Quand est votre rendez-vous ? »", "« Dans six semaines. »"),
    ], corrige=False,
       notes="Circuler et noter au tableau les deux ou trois erreurs les plus "
             "fréquentes, sans nommer personne. Les corriger en groupe à la fin.")

    d.billet(
        "Écrivez trois phrases sur vous : une avec depuis, une avec il y a, une avec dans.",
        exemples=[
            "Depuis quand êtes-vous au Québec ?",
            "Quand avez-vous commencé votre cours de français ?",
            "Quand est votre prochain rendez-vous ?",
        ],
        notes="Devoir court. Les phrases personnelles fixent la différence mieux que "
              "les phrases de pharmacie : le sens y est vécu.")

    return d.save(dossier)
