# -*- coding: utf-8 -*-
"""B4 · Les mots qui tiennent le reportage debout
Bloc B « Défi 1 · Le reportage » · couleur ambre · 75 min.
Source : exercice `t1conn` et sa mini-leçon — les connecteurs de
topicalisation, de reformulation et de conclusion.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="Les mots qui tiennent le reportage debout",
        chapeau="Trois minutes sans se perdre, c'est possible : le "
                "journaliste pose des panneaux tout au long du parcours. "
                "Celui qui les repère sait toujours où il en est, même s'il "
                "a manqué une phrase.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du Défi 1. C'est autant une stratégie d'écoute qu'un "
                  "point de grammaire ; le dire au groupe, parce que ça change la façon "
                  "d'y travailler.")

    d.objectifs([
        "repérer les connecteurs qui annoncent un changement de sujet ;",
        "reconnaître une reformulation et s'en servir pour rattraper le fil ;",
        "distinguer un résumé d'une conséquence ;",
        "employer ces connecteurs dans ses propres phrases.",
    ], notes="Le deuxième objectif est le plus rentable à l'écoute : « autrement dit » "
             "annonce une seconde chance de comprendre.")

    d.declencheur(
        'Écoute', "Où en est-on dans le reportage ?",
        pistes=[
            "Réécoutez le début : quel mot annonce que ça commence ?",
            "Quel mot annonce qu'on change de sujet ?",
            "Quel mot annonce que c'est fini ?",
            "Sans ces mots, sauriez-vous où vous en êtes ?",
        ],
        notes="Faire l'expérience en écoutant sans regarder la transcription. Les "
              "connecteurs sont audibles même quand le reste échappe.")

    d.tableau('Analyse', "Cinq rôles, cinq familles de mots",
              ['Le rôle', 'Les mots'],
              [["Ouvrir, poser le contexte", "d'abord, premièrement, rappelons que"],
               ["Changer de sujet", "quant à, en ce qui concerne, à propos de"],
               ["Ajouter un autre aspect", "par ailleurs, d'autre part"],
               ["Redire plus simplement", "autrement dit, c'est-à-dire, en d'autres termes"],
               ["Résumer ou conclure", "en somme, donc, par conséquent"]],
              cle=0,
              note="Le mot qui suit « quant à » vous donne le thème du paragraphe entier.",
              notes="Diapositive à photographier. C'est la grille de lecture de tous les "
                    "textes longs du niveau, pas seulement de ce reportage.")

    d.regle("Autrement dit, c'est une seconde chance",
            "Quand le journaliste reformule, il vous redonne la phrase en plus simple.",
            precision="« Autrement dit » et « c'est-à-dire » arrivent après une "
                      "information technique. Celui qui a manqué la version savante "
                      "reçoit la version claire deux secondes plus tard. C'est le seul "
                      "endroit d'un reportage où la même chose est dite deux fois : il "
                      "serait dommage de décrocher juste avant.",
            notes="Diapositive à photographier. Faire chercher les deux reformulations "
                  "du reportage et vérifier qu'elles sont bien comprises.")

    d.piege("Confondre « en somme » et « par conséquent »",
            "Par conséquent, merci de votre attention.",
            "En somme : un local vide, deux emplacements, une décision en octobre.",
            "« En somme » résume : il rassemble ce qui vient d'être dit, sans rien "
            "ajouter. « Par conséquent » conclut : il tire une conséquence, donc il "
            "ajoute quelque chose de nouveau. Employer « par conséquent » là où il n'y "
            "a aucune conséquence est l'erreur la plus visible dans un texte d'élève.",
            notes="Le piège se corrige par une question unique : y a-t-il une "
                  "conséquence ? Si non, c'est « en somme ».")

    d.cartes("Deux pièges de l'oreille", "À corriger tout de suite", [
        ("« par ailleurs » n'est pas « en plus »",
         "« En plus » ajoute dans la même direction. « Par ailleurs » ouvre un autre angle, souvent contraire."),
        ("« quant à » n'a rien à voir avec « quand »",
         "« Quant à » introduit un sujet ; « quand » introduit un moment. Ils se ressemblent à l'oreille et en rien d'autre."),
        ("« rappelons que » annonce du connu",
         "Ce qui suit est du contexte, pas la nouvelle. On peut relâcher deux secondes si on le sait déjà."),
        ("« en ce qui concerne » ouvre un nouveau bloc",
         "Le reportage change de sujet. Se remettre en marche, même si on était perdu avant."),
    ], notes="Les deux premiers sont des confusions de forme, les deux derniers des "
             "stratégies d'écoute. Faire la différence explicitement.")

    d.pratique('Application', "Le bon connecteur",
               "Complétez. Chacun ne sert qu'une fois.", [
        ("____, les faits. Le local est vide depuis deux ans.", "D'abord"),
        ("____ que la consigne est de dix cents depuis novembre 2023.", "Rappelons"),
        ("____, il y a de plus en plus de contenants à rapporter.", "Autrement dit"),
        ("____ la date d'ouverture, elle n'est pas arrêtée.", "Quant à"),
        ("____, tout le monde n'accueille pas le projet de la même façon.", "Par ailleurs"),
        ("____ les heures d'ouverture, aucune information ne circule.", "En ce qui concerne"),
        ("____ : un local vide, deux emplacements, une décision en octobre.", "En somme"),
    ], corrige=True,
       notes="Les sept phrases sont celles du reportage, dans l'ordre. Le faire "
             "remarquer une fois l'exercice corrigé : le groupe vient de reconstituer "
             "le squelette d'un texte de trois minutes.")

    d.billet(
        "Racontez une nouvelle en trois phrases, avec « d'abord », « par ailleurs » et « en somme ».",
        exemples=[
            "N'importe quelle nouvelle, même personnelle.",
            "Les trois connecteurs doivent y être, dans cet ordre.",
        ],
        notes="Fin du Défi 1. Ce billet est la première production organisée du module ; "
              "il annonce le compte rendu oral de E1.")

    return d.save(dossier)
