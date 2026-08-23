# -*- coding: utf-8 -*-
"""C3 · Concéder avant d'avancer
Bloc C « Défi 2 · L'éditorial et sa thèse » · couleur ambre · 75 min.
Source : exercice `t2conc` et sa mini-leçon. Savoir du niveau 8 : les
connecteurs de concession et d'opposition — certes... mais, bien que et
quoique plus le subjonctif, même si plus l'indicatif, or, il n'en reste pas
moins que.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="Certes, bien que, même si, or",
        chapeau="Dans un débat, celui qui n'accorde jamais rien perd "
                "l'auditoire en trois minutes. Concéder n'est ni de la "
                "faiblesse ni de la politesse : c'est une technique, et le "
                "français a une demi-douzaine de tournures faites pour ça.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire, mais qui se joue à l'oral. Faire dire chaque "
                  "exemple à voix haute : le rapport logique s'entend dans la "
                  "mélodie autant qu'il se lit dans le mot.")

    d.objectifs([
        "concéder pour de vrai, en nommant le point exact accordé ;",
        "employer « bien que » et « quoique » avec le subjonctif ;",
        "employer « même si » avec l'indicatif, sans les confondre ;",
        "placer un « or » là où il renverse un raisonnement.",
    ], notes="Le deuxième objectif est le plus rentable de tout le bloc, et le "
             "troisième est le piège qui l'accompagne. Les enseigner ensemble, "
             "jamais l'un sans l'autre.")

    d.declencheur(
        'Observation', "Laquelle de ces deux phrases concède vraiment ?",
        pistes=[
            "« Je comprends votre point de vue, mais le projet est nécessaire. »",
            "« Le vote a été pris trop vite : là-dessus, le comité a raison. »",
            "Qu'est-ce que la première accorde exactement ? Et la seconde ?",
            "Laquelle des deux vous donnerait envie d'écouter la suite ?",
        ],
        notes="La première ne concède rien : c'est une formule de politesse, et elle "
              "s'entend à trois kilomètres. La seconde nomme le point précis. Laisser "
              "le groupe trouver la différence avant de la nommer.")

    d.regle("Concéder, c'est nommer le point exact où l'autre a raison",
            "Certes le terrain a une valeur, mais il n'a jamais rapporté un "
            "dollar à la Ville.",
            precision="Deux temps, et jamais l'inverse : la concession d'abord, "
                      "courte ; votre point ensuite, qui porte le poids de la phrase. "
                      "Le lecteur retient la seconde moitié. « Il n'a jamais rien "
                      "rapporté, certes il a une valeur » laisse l'auditeur sur "
                      "l'argument adverse.",
            notes="Diapositive à photographier. Faire répéter la règle de l'ordre par "
                  "deux élèves : c'est elle qu'on oublie en parlant vite.")

    d.cartes('Analyse', "Quatre mouvements, quatre familles", [
        ("Concéder puis avancer",
         "certes... mais · il est vrai que... mais · bien que et quoique "
         "plus le subjonctif · même si plus l'indicatif. On donne raison, "
         "puis on avance. C'est la forme reine d'un débat public."),
        ("Opposer sans concéder",
         "en revanche · par contre · alors que · tandis que. Deux faits "
         "vrais mis côte à côte, du même poids : le comité compte trois cent "
         "quarante-deux arbres alors que le promoteur en compte quatre-vingt-dix."),
        ("Renverser",
         "or. « La Ville affirme avoir tout étudié. Or, aucune étude "
         "n'existe sur le terrain de l'aréna. » Il introduit le fait qui "
         "fait tomber ce qui précède, et un seul suffit par texte."),
        ("Refermer la concession",
         "il n'en reste pas moins que · il n'en demeure pas moins que. "
         "« Le projet répond à un besoin réel ; il n'en reste pas moins que "
         "la population n'a pas été consultée. » On ferme sans nier."),
    ], notes="Faire produire une phrase par famille sur le dossier du boisé, à l'oral, "
             "en cercle. Deux minutes par famille suffisent.")

    d.piege('Piège', "Bien que le projet c'est nécessaire",
            "Bien que le projet soit nécessaire",
            "« Bien que » et « quoique » demandent le subjonctif, sans "
            "exception. C'est la faute la plus fréquente du niveau 8, et "
            "celle qui se remarque le plus, à l'écrit comme à l'oral. Un "
            "moyen de ne plus la faire : « même si » contient « si », et "
            "« si » ne prend jamais le subjonctif ; « bien que » ne contient "
            "pas « si », donc subjonctif.",
            notes="Écrire les deux versions au tableau, la juste à droite, et les "
                  "laisser toute la séance. Y revenir à chaque item de la pratique 1 "
                  "qui contient « bien que ».")

    d.tableau('Analyse', "Le connecteur et le mode qu'il commande",
              ['Connecteur', 'Ce qui suit'],
              [["bien que · quoique", "SUBJONCTIF : bien que le projet soit nécessaire"],
               ["même si", "INDICATIF : même si le vote a été serré"],
               ["certes... mais", "indicatif des deux côtés, deux propositions"],
               ["or", "une phrase complète, après une virgule"],
               ["en revanche · par contre", "une phrase complète, sans concéder"],
               ["il n'en reste pas moins que", "INDICATIF : que personne n'a été consulté"]],
              cle=0,
              notes="Diapositive à photographier. Six lignes : ne pas la commenter "
                    "ligne à ligne, la laisser afficher pendant la pratique 1 et "
                    "laisser les élèves y revenir seuls.")

    d.pratique('Pratique 1 de 2', "Le bon connecteur",
               "Un seul convient : le sens de la phrase le désigne.", [
        ("___ le projet soit nécessaire, la façon de l'adopter reste critiquable.", "Bien que - subjonctif"),
        ("___ le vote a été serré, il est parfaitement valide.", "Même si - indicatif"),
        ("Le premier article ouvre sur les logements ; ___, le second ouvre sur l'heure du vote.", "en revanche"),
        ("La Ville affirme avoir tout étudié. ___, aucune étude n'existe sur le terrain de l'aréna.", "Or"),
        ("___ le comité a raison sur la rapidité du vote, mais il se trompe sur les délais.", "Certes"),
        ("Le projet répond à un besoin réel ; ___ que la population n'a pas été consultée.", "il n'en reste pas moins"),
        ("Le comité compte trois cent quarante-deux arbres ___ le promoteur en compte quatre-vingt-dix.", "alors que"),
    ], corrige=True,
       notes="Faire justifier chaque choix par le rapport logique, pas par l'oreille. "
             "Les deux premiers sont le couple à ne jamais confondre : demander à "
             "chaque fois quel mode suit, et pourquoi.")

    d.pratique('Pratique 2 de 2', "Concession vraie ou fausse concession ?",
               "Dites si la phrase accorde réellement quelque chose.", [
        ("Je comprends votre point de vue, mais le projet est nécessaire.", "fausse - rien n'est accordé"),
        ("Le vote a été pris trop vite : là-dessus, le comité a raison.", "vraie - le point est nommé"),
        ("Certes il y a des érables, mais il faut loger les gens.", "vraie - courte, mais précise"),
        ("Avec tout le respect que je vous dois, vous vous trompez.", "fausse - une formule de politesse"),
        ("Il est vrai que l'évaluation n'a pas été publiée.", "vraie - un fait accordé"),
        ("On peut en discuter, mais la décision est prise.", "fausse - on ferme la discussion"),
    ], corrige=True,
       notes="Le test à donner au groupe : qu'est-ce que la phrase accorde, "
             "exactement ? Si on ne peut pas le dire en trois mots, la concession est "
             "fausse. Trois concessions dans un même texte font un texte sans "
             "position ; une seule, sur le point central, fait un texte qu'on ne peut "
             "pas balayer.")

    d.billet(
        "Écrivez deux phrases sur le dossier du boisé, avec deux connecteurs différents.",
        exemples=[
            "Une avec « bien que » et le subjonctif : soit, ait, puisse, fasse.",
            "Une avec « or », qui renverse ce que la phrase précédente affirmait.",
        ],
        notes="Devoir. Les phrases se reprennent telles quelles à la tribune du "
              "bloc D et dans la lettre du bloc E : le dire, pour que le travail ne "
              "paraisse pas gratuit.")

    return d.save(dossier)
