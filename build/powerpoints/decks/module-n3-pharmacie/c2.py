# -*- coding: utf-8 -*-
"""C2 · Est-ce que je peux, je dois, il faut.
Bloc C « Défi 2 · Renouveler l'ordonnance » · couleur teal · 75 min.
Source : exercice `t2modal`, mini-leçon `t2modal`.

Savoirs du niveau : les auxiliaires de modalité. Ils sont neuf points dans le
programme ; le module en retient trois, ceux qui servent au comptoir.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='teal',
        titre='Est-ce que je peux, je dois, il faut',
        chapeau="Trois verbes suffisent pour presque tout ce qui se dit au "
                "comptoir : un pour demander, un pour dire son obligation, un "
                "pour la règle de tout le monde.",
        duree='75 minutes')

    d.titre(notes="Séance de langue. Le point le plus rentable du module : ces trois "
                  "verbes servent partout, à la banque comme à l'école. Le dire au "
                  "groupe en ouvrant.")

    d.objectifs([
        "demander poliment avec « est-ce que je peux » ;",
        "demander un service avec « est-ce que vous pouvez » ;",
        "dire une obligation avec « je dois » et « il faut » ;",
        "mettre le second verbe à l'infinitif.",
    ])

    d.declencheur(
        'Mise en situation', "Comment demandez-vous un renouvellement ?",
        pistes=[
            "« Je veux mon médicament » — comment cela sonne-t-il ?",
            "Quelle formule est plus polie ?",
            "Qu'est-ce qui change entre « je peux » et « je dois » ?",
        ],
        notes="Faire entendre les deux versions à voix haute : « je veux » et « est-ce "
              "que je peux ». La différence de ton se perçoit avant l'explication.")

    d.tableau('Analyse', "Trois verbes, trois usages",
              ["La forme", "Ce qu'elle fait"],
              [["est-ce que je peux…", "demander pour soi"],
               ["est-ce que vous pouvez…", "demander un service"],
               ["je dois…", "dire son obligation"],
               ["vous devez…", "l'obligation, dite poliment"],
               ["il faut…", "la règle, pour tout le monde"]],
              cle=0,
              note="Derrière chacun, le second verbe ne se conjugue jamais.",
              notes="Diapositive à photographier. C'est le tableau de référence de la "
                    "séance ; le laisser affiché pendant les exercices.")

    d.regle("La règle qui ne change jamais",
            "« Il faut apporter sa carte. »",
            precision="« Il faut » garde toujours la même forme, pour tout le "
                      "monde. On ne dit jamais « il faut je ». On dit « je "
                      "dois » ou « il faut », jamais les deux ensemble.",
            notes="Diapositive à photographier. La faute « il faut je prends » est très "
                  "fréquente et se corrige vite si elle est nommée tôt.")

    d.cartes("Quatre demandes utiles", "À apprendre par cœur", [
        ("Est-ce que je peux faire renouveler mon ordonnance ?",
         "La demande de base du défi 2. Elle contient la politesse, la demande et le "
         "mot exact. À dire telle quelle."),
        ("Est-ce que vous pouvez regarder mon dossier ?",
         "Quand c'est l'autre personne qui doit agir. Ajoutez « s'il vous plaît » à la "
         "fin : la demande devient plus polie encore."),
        ("Est-ce que vous pouvez répéter, s'il vous plaît ?",
         "La phrase qui sauve toutes les conversations. Personne ne s'en offusque, et "
         "elle vaut mieux que de repartir sans avoir compris."),
        ("Est-ce que je dois attendre ici ?",
         "Pour savoir ce qu'on attend de vous. Utile quand le pharmacien dit « ça va "
         "prendre vingt minutes » sans préciser où s'asseoir."),
    ], notes="Faire répéter les quatre phrases entières, à voix haute, deux fois. Ce "
             "sont des blocs : on ne les fabrique pas mot à mot au comptoir.")

    d.piege('Construction',
            "« je dois je prends un comprimé »",
            "« je dois prendre un comprimé »",
            "Après pouvoir, devoir et falloir, le verbe qui suit ne se conjugue pas. On "
            "dit « je dois prendre », « il faut apporter », « est-ce que je peux "
            "attendre ». Un seul verbe conjugué par phrase.",
            notes="Écrire les deux formes au tableau, faire barrer la fausse. Puis faire "
                  "produire trois phrases justes avec trois verbes différents.")

    d.pratique('Application', "Peux, pouvez, dois, devez ou faut ?",
               "Complétez chaque phrase.", [
        ("Est-ce que je ___ faire renouveler mon ordonnance ?", "peux"),
        ("Est-ce que vous ___ regarder mon dossier, s'il vous plaît ?", "pouvez"),
        ("Je ___ prendre un comprimé le matin et un le soir.", "dois"),
        ("Vous ___ finir les sept jours, même si ça va mieux.", "devez"),
        ("Il ___ apporter sa carte d'assurance maladie chaque fois.", "faut"),
    ], corrige=True,
       notes="Les items de l'exercice interactif. Faire justifier chaque réponse : qui "
             "parle, et de qui parle-t-on ?")

    d.pratique('Production', "Demandez-le au comptoir",
               "Faites une phrase complète pour chaque situation.", [
        ("Vous voulez un renouvellement.", "« Est-ce que je peux faire renouveler mon ordonnance ? »"),
        ("Vous n'avez pas compris ce qu'on vient de dire.", "« Est-ce que vous pouvez répéter, s'il vous plaît ? »"),
        ("Vous voulez savoir si vous devez rester sur place.", "« Est-ce que je dois attendre ici ? »"),
        ("Vous voulez connaître l'obligation générale.", "« Est-ce qu'il faut apporter la carte chaque fois ? »"),
    ], corrige=True,
       notes="Faire dire les phrases debout, à voix haute. Corriger le second verbe : "
             "c'est la seule chose à surveiller aujourd'hui.")

    d.billet(
        "Écrivez quatre questions que vous poseriez à un pharmacien.",
        exemples=[
            "Deux avec « est-ce que je peux », deux avec « est-ce que vous pouvez ».",
            "Employez « il faut » dans une cinquième phrase.",
        ],
        notes="Devoir court. Les questions produites servent au jeu de rôle de la "
              "séance E1, où l'assistant ne répond qu'à ce qu'on lui demande.")

    return d.save(dossier)
