# -*- coding: utf-8 -*-
"""B2 · Ce qui se passait, ce qui est arrivé.
Bloc B « Défi 1 · Le constat » · couleur ambre · 75 min. Grammaire.
Source : exercices `t1temps` et `t1tri`, mini-leçon `t1temps`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre="Ce qui se passait, ce qui est arrivé",
        chapeau="L'imparfait plante le décor, le passé composé fait avancer "
                "l'histoire. Ce n'est pas une question de durée : c'est une "
                "question de rôle dans le récit.",
        duree='75 minutes')

    d.titre(notes="Le point de grammaire le plus lourd du module, et celui qui sert le "
                  "plus loin — un récit d'accident, une déclaration à la police, une "
                  "anecdote au souper se racontent tous ainsi.")

    d.objectifs([
        "distinguer le décor de l'événement dans un récit ;",
        "former l'imparfait et le passé composé sans hésiter ;",
        "employer quand + passé composé et pendant que + imparfait ;",
        "accorder le participe passé avec être.",
    ])

    d.regle("Deux temps, deux rôles",
            "L'imparfait décrit ce qui durait ; le passé composé raconte ce qui "
            "est arrivé.",
            precision="Ce n'est pas la durée réelle qui décide. « Il a plu pendant trois "
                      "jours » est un passé composé, et trois jours, c'est long. Ce qui "
                      "compte est le rôle : est-ce que la phrase pose le décor, ou "
                      "est-ce qu'elle fait avancer l'histoire d'un cran ?",
            notes="Cette précision règle à elle seule la moitié des erreurs. La dire "
                  "avant toute conjugaison.")

    d.tableau('Deux tests qui ne trompent pas', "À se dire dans sa tête",
              ['Le test', 'Ce qu\'il donne'],
              [["« pendant tout ce temps-là »",
                "si on peut l'ajouter sans que ce soit bizarre : imparfait"],
               ["« et puis »",
                "si on peut le mettre devant : passé composé"],
               ["quand + passé composé",
                "l'événement qui coupe : quand je me suis réveillée"],
               ["pendant que + imparfait",
                "le décor qui dure : pendant que je travaillais"]],
              cle=0,
              note="Les deux derniers forment une paire : elle règle l'autre moitié des "
                   "hésitations.",
              notes="Faire appliquer les deux tests à voix haute sur trois phrases du "
                    "dialogue B1 avant de passer à la conjugaison.")

    d.cartes("Comment ils se forment", "Deux règles, un irrégulier", [
        ("L'imparfait",
         "Le radical de « nous » + -ais, -ais, -ait, -ions, -iez, -aient."),
        ("Le seul irrégulier",
         "être donne j'étais. Tous les autres suivent la règle du « nous »."),
        ("Le passé composé avec avoir",
         "j'ai mis, j'ai appelé, il a lâché. Pas d'accord avec le sujet."),
        ("Le passé composé avec être",
         "je me suis levée, elle est montée. Le participe s'accorde."),
    ], notes="Insister sur la dernière : les verbes pronominaux — se lever, se réveiller, "
             "s'inquiéter — prennent tous être, et c'est là que l'accord se perd.")

    d.pratique('Pratique · exercice t1tri', "Trois temps dans la même histoire",
               "Chaque phrase va dans un des trois blocs : ce qui se passait, ce qui "
               "est arrivé, ce qui reste.",
               [("Le chauffe-eau avait quinze ans.", "ce qui se passait"),
                ("Le réservoir a lâché vers trois heures du matin.", "ce qui est arrivé"),
                ("Il y a aujourd'hui un cerne d'un mètre au plafond.", "ce qui reste"),
                ("Il faisait encore noir et tout le monde dormait.", "ce qui se passait"),
                ("Le plombier est venu le jour même.", "ce qui est arrivé"),
                ("Je ne peux toujours pas coucher dans ma chambre.", "ce qui reste")],
               corrige=True, cols=1,
               notes="Le troisième bloc n'est pas un temps du passé : c'est le présent. "
                     "Le faire remarquer — un récit de sinistre finit toujours au "
                     "présent, sur l'état actuel.")

    d.pratique('Pratique · exercice t1temps', "Imparfait ou passé composé ?",
               "Mettez le verbe entre parenthèses au temps qui convient.",
               [("Quand je (se lever) ___ , il était six heures.", "je me suis levée"),
                ("L'eau (tomber) ___ du plafond depuis un bon moment.", "tombait"),
                ("J' (mettre) ___ une chaudière sous la fuite.", "ai mis"),
                ("Le chauffe-eau (avoir) ___ quinze ans.", "avait"),
                ("Le plombier (remplacer) ___ le réservoir le jour même.",
                 "a remplacé"),
                ("Je ne (savoir) ___ pas encore d'où venait l'eau.", "savais")],
               corrige=True, cols=1,
               notes="Faire justifier chaque réponse par l'un des deux tests. Une réponse "
                     "juste sans justification ne tiendra pas la semaine prochaine.")

    d.regle("L'accord avec être",
            "Avec être, le participe s'accorde avec le sujet ; avec avoir, non.",
            precision="Elle est montée. Elle s'est levée. Ils sont partis. Mais : elle a "
                      "mis, ils ont appelé, elle a remplacé. C'est la règle qui distingue "
                      "un écrit soigné d'un écrit approximatif, et elle se voit "
                      "immédiatement dans une lettre à un propriétaire.",
            notes="Faire relever les participes avec être dans le dialogue B1 : il y en a "
                  "trois. Les écrire avec leur accord.")

    d.piege("Mettre tout le récit au passé composé",
            "Il a fait noir, l'eau a tombé, je n'ai pas su quoi faire.",
            "Il faisait noir, l'eau tombait, je ne savais pas quoi faire.",
            "Le récit devient une liste et on ne distingue plus le décor des événements. "
            "En plus, « l'eau a tombé » n'existe pas : tomber se conjugue avec être, "
            "donc « l'eau est tombée ». Deux erreurs dans la même phrase, et elles "
            "viennent de la même cause.",
            notes="Écrire les deux versions au tableau et faire lire les deux à voix "
                  "haute par le même élève. La différence de rythme s'entend.")

    d.billet(
        "Racontez en deux phrases un incident chez vous : une au décor, une à l'événement.",
        exemples=[
            "« Il pleuvait depuis deux jours. »",
            "« L'eau est entrée par la fenêtre du sous-sol. »",
        ],
        notes="Trois minutes. Ramasser : c'est le premier essai de récit du module, et il "
              "dit exactement où en est chacun.")

    return d.save(dossier)
