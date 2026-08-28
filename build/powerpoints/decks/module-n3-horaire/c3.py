# -*- coding: utf-8 -*-
"""C3 · Ce que la phrase demande, et comment on répond.
Bloc C « Défi 2 · Est-ce que je peux vous demander ? » · couleur ambre · 60 min.
Source : exercices `t2poli` et `t2repondre`, mini-leçon `t2repondre`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="Ce que la phrase demande, et comment on répond",
        chapeau="Jusqu'ici on demandait. Cette fois, c'est un collègue qui "
                "demande — et il faut répondre en trois mots, sans laisser "
                "l'autre en plan.",
        duree='60 minutes')

    d.titre(notes="Séance d'écriture. Le renversement de rôle est le cœur de la séance : "
                  "un employé qu'on n'ose pas déranger devient vite un employé qu'on "
                  "n'aide pas non plus.")

    d.objectifs([
        "reconnaître ce qu'une phrase demande vraiment ;",
        "répondre oui en trois mots ;",
        "refuser en donnant une raison ;",
        "faire attendre sans laisser l'autre sans réponse.",
    ])

    d.pratique('Compréhension', "Qu'est-ce que cette phrase demande ?",
               "Une permission, de l'aide, un service, ou autre chose ?", [
        ("« Est-ce que je peux partir à midi ? »", "une permission : le responsable dit oui ou non"),
        ("« Est-ce que vous pouvez m'aider ? »", "de l'aide : quelqu'un fait la chose avec toi"),
        ("« Passe-moi ton crayon, s'il te plaît. »", "un petit service, tout de suite, entre collègues"),
        ("« Qu'est-ce qui se passe ? »", "une explication : tu ne comprends pas la situation"),
        ("« Est-ce que je pourrais échanger mon jeudi ? »", "une permission, demandée très poliment"),
        ("« Vous pouvez répéter, s'il vous plaît ? »", "redire la phrase : tu n'as pas bien entendu"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `t2poli` du module interactif. La troisième ligne est la "
             "seule qui n'a pas de « est-ce que » : entre collègues, l'impératif suffit — "
             "avec « s'il te plaît ».")

    d.tableau('Analyse', "Trois façons de répondre",
              ["La réponse", "Quand l'employer"],
              [["Oui, bien sûr. Pas de problème.", "vous êtes libre : la réponse la plus courte est la meilleure"],
               ["Je regrette, je suis occupée.", "vous refusez : jamais « non » tout seul"],
               ["Une minute, j'arrive.", "vous n'êtes pas libre tout de suite"]],
              cle=1,
              note="La troisième est une vraie réponse : elle dit que vous "
                   "avez entendu. Le silence, lui, n'en est pas une.",
              notes="Diapo à photographier. Insister sur la dernière note : dans le bruit "
                    "d'une cuisine, ne rien répondre passe pour un refus ou pour du "
                    "mépris, alors que c'est souvent de la timidité.")

    d.regle("Un refus se donne avec sa raison",
            "Je regrette, je dois éteindre le four.",
            precision="On ne dit pas « non » tout seul au travail : on dit "
                      "qu'on regrette, et on dit pourquoi. La raison peut "
                      "être très courte — elle montre qu'on a considéré la "
                      "demande.",
            notes="Diapo à photographier. Faire produire trois refus polis à partir de "
                  "situations réelles du groupe. Le mot « désolée » convient aussi bien "
                  "que « je regrette ».")

    d.pratique('Écriture', "Répondez à chaque demande",
               "Une réponse courte et polie.", [
        ("Un collègue : « Est-ce que tu peux m'aider deux minutes ? » Vous êtes libre.",
         "Oui, bien sûr. — ou : Pas de problème."),
        ("Un collègue : « Passe-moi ton crayon. » Vous le lui donnez.",
         "Tiens, le voilà."),
        ("Un collègue demande de l'aide, mais vous devez éteindre le four.",
         "Je regrette, je dois éteindre le four."),
        ("Votre chef dit : « Le four à onze heures. » Vous vérifiez.",
         "Le four à onze heures, c'est bien ça ?"),
        ("Il accepte votre échange de quart. Vous répondez.",
         "Merci beaucoup, monsieur Roy."),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `t2repondre` du module interactif. La quatrième ligne n'est "
             "pas une réponse mais une vérification : c'est le geste du défi 3, et il "
             "arrive ici pour la deuxième fois.")

    d.cartes("Ce qui entoure une demande", "Trois phrases à savoir par cœur", [
        ("Avant : demander le temps",
         "« Est-ce que je peux vous parler deux minutes ? » Elle évite d'arriver au "
         "mauvais moment, en plein service."),
        ("Pendant : donner la raison",
         "« Je dois aller à la clinique avec mon garçon. » Une phrase, jamais deux. Une "
         "demande sans raison inquiète."),
        ("Après : redire l'entente",
         "« Alors jeudi, c'est Miguel à six heures ? » Trois secondes qui écartent la "
         "moitié des malentendus."),
        ("À la fin : remercier",
         "« Merci beaucoup. » Même si la réponse est non. C'est ce qui rend la prochaine "
         "demande possible."),
    ], notes="Diapo à photographier. Faire copier les quatre phrases dans le cahier, dans "
             "l'ordre : c'est le squelette de la production orale de E1.")

    d.billet(
        "Écrivez trois réponses : un oui, un non, un « attendez ».",
        exemples=[
            "Chacune avec sa raison quand il en faut une.",
            "« Une minute, je finis les plateaux et j'arrive. »",
        ],
        notes="Devoir court. Ramasser : les refus sont ceux qui demandent le plus de "
              "travail, et ce sont ceux que les élèves écrivent le moins volontiers.")

    return d.save(dossier)
