# -*- coding: utf-8 -*-
"""A3 · Quand la voix insiste.
Bloc A « Je découvre » · couleur teal · 60 min.
Source : mini-leçon `prPhon`, exercice `prPhon` (cartes à écouter).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre='Quand la voix insiste',
        chapeau="« Elle portait des sandales. » et « Des sandales ! » — mêmes "
                "mots, deux messages. En français, ce n'est pas le vocabulaire "
                "qui porte la surprise, c'est la voix.",
        duree='60 minutes')

    d.titre(notes="Séance d'écoute. Prévoir le son : sans haut-parleur, cette séance ne "
                  "fonctionne pas. Faire l'essai avant l'arrivée du groupe.")

    d.objectifs([
        "reconnaître à l'oreille une phrase où la personne insiste ;",
        "comprendre qu'une exclamation n'attend pas de réponse ;",
        "savoir que les phrases d'insistance sont souvent très courtes ;",
        "laisser monter ma propre voix sur le mot qui compte.",
    ])

    d.declencheur(
        'Écoute', "Ces deux phrases disent-elles la même chose ?",
        pistes=[
            "« Elle portait des sandales à l'aéroport. »",
            "« Des sandales ! En janvier ! »",
            "Quelle est la personne surprise ? À quoi l'entendez-vous ?",
            "Est-ce que la deuxième phrase attend une réponse ?",
        ],
        notes="Faire écouter les deux extraits du module (exercice 2 de « Je découvre ») "
              "avant toute explication. Laisser le groupe décrire ce qu'il entend avec ses "
              "mots — « plus fort », « plus haut », « plus long » : les trois sont justes.")

    d.tableau('Analyse', "Ce qui change entre les deux",
              ['', 'Phrase neutre', 'Phrase qui insiste'],
              [["Ce qu'on fait", "on informe", "on réagit, on s'étonne"],
               ["La voix", "elle descend jusqu'au point", "une syllabe monte nettement"],
               ["La longueur", "phrase complète", "souvent deux ou trois mots"],
               ["Ce qu'on attend", "rien de spécial", "que l'autre confirme"]],
              cle=1,
              note="La ligne de la longueur est le repère le plus simple : une phrase très "
                   "courte, dans une conversation, est presque toujours une réaction.",
              notes="Faire relire la colonne de droite à voix haute par plusieurs élèves, "
                    "en exagérant. L'exagération est pédagogique ici.")

    d.regle('Ce que vous devez faire',
            "Reconnaître l'insistance suffit. Vous n'avez pas à la produire parfaitement.",
            precision="Le programme du cours demande de la reconnaître, pour comprendre son "
                      "interlocuteur. La produire viendra tout seul, à force d'écouter. "
                      "Ne bloquez pas là-dessus.",
            notes="Le dire clairement : plusieurs élèves se découragent sur la prononciation. "
                  "L'objectif est la compréhension.")

    d.cartes('Les exclamations du module', "Ce qu'elles veulent dire", [
        ("« Des sandales ! En janvier ! »",
         "Surprise. Chantal ne demande pas quel type de chaussures : elle trouve ça "
         "incroyable. La bonne réponse est « oui, je ne savais pas »."),
        ("« Cinq heures et quart ! »",
         "Étonnement. Chantal ne demande pas l'heure : elle trouve ça très tôt."),
        ("« Six ans dans la même équipe ! »",
         "Admiration. Mariama ne pose pas de question : elle souligne que c'est long."),
        ("« Onze voyages ! »",
         "Incrédulité. La phrase entière monte, parce que c'est le nombre qui surprend."),
    ], notes="Faire écouter chaque extrait, puis demander au groupe de répondre à voix haute "
             "comme si on leur parlait. C'est la partie utile de la séance.")

    d.piege("Confondre exclamation et question",
            "— Des sandales ! — Euh… oui, des sandales bleues.",
            "— Des sandales ! — Oui ! Personne ne m'avait dit qu'il faisait si froid.",
            "Une exclamation réagit à ce que vous venez de dire ; elle ne demande pas "
            "d'information nouvelle. Y répondre par un détail donne l'impression de ne pas "
            "avoir compris. Il suffit de confirmer, et d'ajouter une phrase.",
            notes="Faire jouer les deux versions par deux élèves. La différence de naturel "
                  "est immédiatement audible.")

    d.pratique('Pratique', "On insiste, ou pas ?",
               "Écoutez chaque phrase et dites si la personne insiste ou parle normalement.", [
        ("Des sandales ! En janvier !", "on insiste"),
        ("Elle portait des sandales à l'aéroport.", "c'est neutre"),
        ("Cinq heures et quart !", "on insiste"),
        ("Je me lève à cinq heures et quart.", "c'est neutre"),
        ("Six ans dans la même équipe !", "on insiste"),
        ("Elle joue dans cette équipe depuis six ans.", "c'est neutre"),
    ], corrige=True,
       notes="Utiliser l'exercice 2 du module pour l'écoute — les élèves peuvent le refaire "
             "seuls ensuite. Ne pas donner la réponse avant deux écoutes.")

    d.cartes('À vous', "Trois phrases à dire à voix haute", [
        ("« Félicitations ! »",
         "La voix monte sur la dernière syllabe. C'est la phrase la plus utile du bloc D."),
        ("« Tu ferais ça ? »",
         "Surprise reconnaissante : quelqu'un vous offre quelque chose et vous ne "
         "l'attendiez pas."),
        ("« Depuis l'automne seulement ! »",
         "Étonnement admiratif. À réutiliser au bloc B, dans le dialogue du tournoi."),
    ], notes="Faire dire chaque phrase par toute la classe en même temps, deux fois. "
             "L'effet de groupe lève la gêne.")

    d.billet(
        "Notez une phrase entendue cette semaine où quelqu'un insistait.",
        exemples=[
            "Au travail, dans l'autobus, à la télévision — n'importe où.",
            "Écrivez la phrase, puis soulignez le mot sur lequel la voix montait.",
        ],
        notes="Excellent point de départ pour la séance suivante : lire deux ou trois "
              "relevés à voix haute.")

    return d.save(dossier)
