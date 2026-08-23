# -*- coding: utf-8 -*-
"""C3 · Le prix est exact, et l'annonce reste discutable
Bloc C « Défi 2 » · couleur ambre · 75 min.
Source : exercice `t2conc`, mini-leçon `t2conc`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="Le prix est exact, et l'annonce reste discutable",
        chapeau="Reconnaître que l'autre a raison sur un point, et maintenir "
                "quand même sa demande. C'est la tournure des lettres de "
                "réclamation qui aboutissent.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire au service de la lettre de E2. L'annoncer : "
                  "ce qu'on apprend aujourd'hui sera exigé dans la production écrite.")

    d.objectifs([
        "exprimer une concession avec le mode qui convient ;",
        "distinguer « bien que » et « même si » ;",
        "employer « malgré » avec un nom ;",
        "comprendre pourquoi concéder rend une demande plus forte.",
    ], notes="Le quatrième objectif est celui qui persuade les élèves d'employer la "
             "tournure. Sans lui, ils la trouvent compliquée pour rien.")

    d.declencheur(
        'Observation', "Laquelle des deux lettres obtient une réponse ?",
        pistes=[
            "« Votre annonce est mensongère et je veux être remboursé. »",
            "« Bien que le prix hebdomadaire soit exact, l'annonce ne mentionnait pas les frais. »",
            "Laquelle montre qu'on a lu le dépliant ?",
            "Laquelle se répond en une ligne ?",
        ],
        notes="La première se répond en une ligne : « tout était dans les "
              "conditions ». La seconde oblige à répondre sur le fond. La différence "
              "est une tournure de grammaire, et c'est la leçon.")

    d.regle("Accorder d'abord, maintenir ensuite",
            "Bien que le prix hebdomadaire soit exact, l'annonce donne une "
            "fausse impression.",
            precision="La concession fait deux choses en même temps : elle reconnaît "
                      "que l'autre a raison sur un point précis, et elle maintient la "
                      "demande. C'est plus fort qu'une opposition, parce que c'est "
                      "plus juste — et ça se remarque dans une lettre.",
            notes="Diapositive à photographier. Faire remarquer que la concession "
                  "coûte peu : on donne raison sur un détail, on garde l'essentiel.")

    d.tableau('Analyse', "Trois marqueurs, trois régimes",
              ['Le marqueur', 'Ce qui suit'],
              [["bien que, quoique", "le subjonctif : soit, ait, paraisse"],
               ["malgré que", "le subjonctif aussi, mais moins soutenu"],
               ["même si", "l'indicatif : est, avez, finit"],
               ["malgré", "un nom, sans verbe du tout"]],
              cle=0,
              note="« Même si ce soit » n'existe pas. C'est l'erreur la plus fréquente.",
              notes="Diapositive à photographier. Si le groupe hésite sur le mode, la "
                    "quatrième ligne est l'échappatoire : « malgré » + un nom évite "
                    "la question.")

    d.cartes('Analyse', "La même idée, trois façons", [
        ("Avec bien que", "Bien que j'aie signé, je demande l'annulation."),
        ("Avec même si", "Même si j'ai signé, je demande l'annulation."),
        ("Avec malgré", "Malgré ma signature, je demande l'annulation."),
        ("Ce qui change", "le ton, jamais le sens"),
    ], cols=1,
       notes="Les trois phrases disent la même chose. Le choix se fait sur le registre : "
             "« bien que » dans une lettre, « même si » à l'oral.")

    d.pratique('Pratique', "Complétez la concession",
               "Attention au mode du verbe qui suit.", [
        ("___ le prix soit exact, l'annonce donne une fausse impression.", "Bien que"),
        ("___ j'aie signé le contrat, je demande l'annulation.", "Bien que"),
        ("___ vous avez lu les conditions, vous pouvez contester.", "Même si"),
        ("___ l'astérisque, le total n'apparaît nulle part.", "Malgré"),
        ("Bien que l'offre ___ (paraître) avantageuse, elle coûte plus cher.", "paraisse"),
        ("Bien que le centre ___ (avoir) raison sur le tarif, il a omis les frais.", "ait"),
        ("Même si la vente ___ (finir) jeudi, je prends le temps de comparer.", "finit"),
    ], corrige=True,
       notes="Exercice `t2conc` du module. Les trois derniers items sont ceux qui "
             "trient : c'est le mode, pas le marqueur, qui pose problème.")

    d.piege('Écrit',
            "« Le prix est bas, mais l'engagement est long. »",
            "« Bien que le prix soit bas, l'engagement est long. »",
            "La première met deux faits côte à côte : c'est une opposition. "
            "La seconde commence par donner raison, puis maintient : c'est "
            "une concession. Dans une lettre de réclamation, la seconde est "
            "plus forte, parce qu'elle montre qu'on a lu et compris avant de "
            "contester.",
            notes="Ce n'est pas une faute de grammaire, c'est un choix de ton. Le dire "
                  "clairement : les deux phrases sont correctes.")

    d.billet(
        "Écrivez deux phrases de concession sur votre annonce, une avec chaque marqueur.",
        exemples=[
            "Bien que… soit… / Même si… est…",
            "Les deux phrases doivent porter sur la même annonce.",
        ],
        notes="Devoir de production. Ces deux phrases entrent telles quelles dans la "
              "lettre de E2 : le dire, ça motive et ça évite de récrire.")

    return d.save(dossier)
