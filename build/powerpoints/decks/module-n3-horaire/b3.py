# -*- coding: utf-8 -*-
"""B3 · L'heure écrite, l'heure dite, et la question qui manque.
Bloc B « Défi 1 · Mon quart commence à quelle heure ? » · couleur ambre · 60 min.
Source : exercices `t1heures` et `t1quest`, mini-leçon `t1quest`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="L'heure écrite, l'heure dite, la question qui manque",
        chapeau="On écrit « 14 h » et on dit « deux heures ». Deux systèmes "
                "pour la même heure — et cinq mots courts pour demander ce "
                "qu'on n'a pas compris.",
        duree='60 minutes')

    d.titre(notes="Séance d'écriture. Sortir les questions ramassées au billet de B1 : "
                  "elles serviront à la deuxième moitié de la séance, et les élèves "
                  "verront que leur propre question devient la matière du cours.")

    d.objectifs([
        "passer de l'heure écrite à l'heure parlée ;",
        "dire et demi, et quart, moins dix ;",
        "poser une question avec à quelle heure, quand, combien de temps ;",
        "employer « est-ce que » pour adoucir la question.",
    ])

    d.regle("On écrit 14 h, on dit deux heures",
            "14 h se dit : deux heures de l'après-midi",
            precision="L'horaire de travail s'écrit toujours sur "
                      "vingt-quatre heures, pour qu'aucune confusion ne "
                      "soit possible. Mais personne ne dit « quatorze "
                      "heures » à un collègue : on dit « deux heures », et "
                      "on ajoute « de l'après-midi » s'il y a un doute.",
            notes="Diapo à photographier. Faire la conversion à voix haute pour toutes "
                  "les heures de l'après-midi : 13, 14, 15… moins douze. C'est un calcul, "
                  "et il se fait vite avec l'habitude.")

    d.pratique('Lecture', "L'heure de l'horaire et l'heure qu'on dit",
               "Comment dit-on chaque heure écrite ?", [
        ("6 h", "six heures du matin"),
        ("11 h 30", "onze heures et demie, juste avant la pause"),
        ("13 h", "une heure de l'après-midi"),
        ("14 h", "deux heures de l'après-midi"),
        ("18 h 15", "six heures et quart, le soir"),
        ("22 h", "dix heures du soir"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `t1heures` du module interactif. Faire ajouter le moment "
             "de la journée à chaque réponse : c'est ce qui lève l'ambiguïté quand on "
             "parle, et c'est justement ce que l'écriture en vingt-quatre heures évite.")

    d.tableau('Analyse', "Les minutes qu'on dit tous les jours",
              ["Écrit", "Dit"],
              [["7 h 15", "sept heures et quart"],
               ["7 h 30", "sept heures et demie"],
               ["7 h 45", "huit heures moins quart"],
               ["7 h 50", "huit heures moins dix"]],
              cle=1,
              note="À partir de la demie, on annonce l'heure suivante et on "
                   "enlève : « huit heures moins dix », jamais « sept heures "
                   "cinquante ».",
              notes="Diapo à photographier. C'est la difficulté réelle de la séance : "
                    "compter à rebours dans une langue étrangère demande un temps que le "
                    "chef d'équipe ne laisse pas toujours. Faire pratiquer lentement.")

    d.regle("Cinq mots pour poser une question",
            "à quelle heure · quand · combien de temps · qui · où",
            precision="L'heure précise, le jour, la durée, la personne, "
                      "l'endroit. Ces cinq mots règlent presque tout ce "
                      "qu'un employé a besoin de demander.",
            notes="Diapo à photographier. Faire classer les questions ramassées au billet "
                  "de B1 dans ces cinq catégories : presque toutes y entrent, et l'élève "
                  "voit que sa question a une forme connue.")

    d.pratique('Écriture', "La question qui manque",
               "Complétez avec à quelle heure, quand, combien de temps, qui ou où.", [
        ("___ est-ce que mon quart commence ? — À six heures.", "À quelle heure"),
        ("___ est-ce que je travaille cette semaine ? — Du lundi au vendredi.", "Quand"),
        ("___ est-ce que la pause dure ? — Trente minutes.", "Combien de temps"),
        ("___ est-ce qui me remplace jeudi ? — Miguel.", "Qui"),
        ("___ est-ce que je poinçonne ? — À côté de la porte grise.", "Où"),
    ], corrige=True,
       notes="C'est l'exercice `t1quest` du module interactif, mot pour mot. La réponse "
             "donne le mot : faire lire la réponse en premier, puis chercher la question. "
             "C'est plus facile et c'est le bon raisonnement.")

    d.regle("Est-ce que adoucit la question",
            "À quelle heure est-ce que je finis ?",
            precision="« Je finis quand ? » est correct, mais sec — surtout "
                      "adressé à un chef d'équipe. « Est-ce que » prend deux "
                      "secondes de plus et change complètement le ton de la "
                      "demande.",
            notes="Diapo à photographier. Faire dire les deux versions de la même "
                  "question, l'une après l'autre. La différence s'entend sans qu'on ait "
                  "besoin de l'expliquer.")

    d.billet(
        "Écrivez trois questions à poser à votre chef d'équipe.",
        exemples=[
            "Avec « est-ce que », et un des cinq mots.",
            "« À quelle heure est-ce que je finis vendredi ? »",
        ],
        notes="Devoir court. Ce sont les questions que l'élève posera vraiment, et "
              "plusieurs les poseront pour de bon dans la semaine. Le demander au retour, "
              "en B4 : la réponse obtenue vaut mieux que n'importe quel exercice.")

    return d.save(dossier)
