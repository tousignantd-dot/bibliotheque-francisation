# -*- coding: utf-8 -*-
"""B2 · La démarche, dans son ordre
Bloc B « Défi 1 » · couleur teal · 75 min. Écoute et réponds.
Source : exercices `t1etapes` et `t1chiffres`, deuxième écoute du dialogue `t1`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='teal',
        titre="La démarche, dans son ordre",
        chapeau="Six étapes, et l'ordre compte autant que les étapes. "
                "Commencer par la troisième fait perdre une session entière.",
        duree='75 minutes')

    d.titre(notes="Deuxième écoute du même entretien. Les élèves ont déjà compris "
                  "l'essentiel en B1 ; aujourd'hui on écoute pour les détails, ce "
                  "qui est une écoute tout à fait différente et qu'il faut annoncer.")

    d.objectifs([
        "remettre en ordre les six étapes d'une démarche administrative ;",
        "repérer les chiffres exacts d'un discours entendu deux fois ;",
        "reconnaître l'ordre des étapes sans mot de liaison explicite ;",
        "redire la démarche à voix haute, dans l'ordre, sans notes.",
    ], notes="Le troisième objectif vient du programme : « comprendre l'ordre des "
             "étapes d'une consigne à partir d'indices autres que les connecteurs de "
             "temps ». C'est plus difficile qu'il n'y paraît.")

    d.declencheur(
        'Observation', "Qu'est-ce qui vient en premier, selon vous ?",
        pistes=[
            "Finir son cours de français, ou s'inscrire au test ?",
            "Demander la description du programme, ou attendre la réponse ?",
            "Y a-t-il des choses qu'on peut faire en même temps ?",
        ],
        notes="Laisser le groupe se tromper. L'erreur la plus fréquente est de "
              "vouloir tout faire en même temps ; la deuxième est d'attendre une "
              "réponse avant de commencer autre chose.")

    d.tableau('Analyse', "Six étapes, dans leur ordre",
              ['Quand', 'Ce qu\'il faut faire'],
              [["1 · avant tout", "terminer la francisation : le français commande tous les autres préalables"],
               ["2 · en même temps", "s'inscrire au comptoir à la séance du test"],
               ["3 · en même temps", "demander la description officielle du programme"],
               ["4 · au résultat", "déposer la preuve de réussite au secrétariat"],
               ["5 · avant la date", "vérifier que la preuve est au dossier, pas seulement postée"],
               ["6 · en janvier", "revoir le conseiller avec des papiers, pas des suppositions"]],
              cle=0,
              notes="Diapositive à photographier. Faire remarquer que deux étapes "
                    "portent « en même temps » : une démarche n'est pas toujours une "
                    "file, et attendre pour rien coûte des semaines.")

    d.regle("L'ordre se lit sans « ensuite »",
            "Un conseiller ne dit presque jamais « premièrement, deuxièmement ». Il dit « commencez par », « une fois que », « d'ici là ».",
            precision="Écoutez les repères de temps plutôt que les numéros : « avant "
                      "tout », « pendant ce temps », « dès que », « d'ici janvier ». "
                      "Ce sont eux qui rangent les étapes, et ils ne se comptent pas.",
            notes="Diapositive à photographier. Faire relever dans le dialogue les "
                  "expressions qui ordonnent : il y en a cinq, aucune n'est un "
                  "numéro.")

    d.pratique('Pratique', "Remettez la démarche en ordre",
               "Numérotez de 1 à 6, d'après ce que Pascal a dit.", [
        ("Revoir le conseiller avec des papiers plutôt qu'avec des suppositions.", "6"),
        ("Terminer la francisation.", "1"),
        ("Déposer la preuve de réussite au secrétariat.", "4"),
        ("S'inscrire au comptoir à la séance du test.", "2"),
        ("Vérifier que la preuve est bien au dossier.", "5"),
        ("Demander la description officielle du programme.", "3"),
    ], corrige=True,
       notes="Faire travailler à deux, cinq minutes, avant de corriger. Demander à "
             "chaque équipe de justifier une seule étape : la justification vaut plus "
             "que la réponse.")

    d.pratique('Pratique', "Deuxième écoute : les chiffres exacts",
               "Réécoutez l'entretien et complétez.", [
        ("Bintou a travaillé ... ans dans une pharmacie à Bamako.", "six"),
        ("Elle est commis de soir depuis ... ans.", "deux"),
        ("La deuxième voie demande d'avoir seize ans au ... septembre.", "trente"),
        ("Les unités demandées sont celles de ... secondaire.", "quatrième"),
        ("La séance du test a lieu le ... novembre.", "vingt-huit"),
        ("Le test d'équivalence compte ... épreuves.", "sept"),
    ], corrige=True, cols=2,
       notes="Arrêter l'extrait après chaque chiffre la première fois, puis le "
             "repasser en entier sans arrêt. C'est la deuxième écoute qui compte : "
             "elle montre au groupe qu'il a progressé en une heure.")

    d.piege('Écoute',
            "noter un chiffre entendu sans le vérifier",
            "le redire à voix haute pour se le faire confirmer",
            "« Le vingt-huit, c'est bien ça ? » Deux secondes, et l'erreur ne "
            "part pas avec vous. Un chiffre mal noté dans un bureau ne se "
            "corrige plus : il devient une absence, une place perdue ou un "
            "rendez-vous manqué.",
            notes="Faire pratiquer la formule tout de suite : donner une date au "
                  "hasard à chaque élève, qui doit la redire pour vérification. Cinq "
                  "minutes, et le réflexe est pris.")

    d.cartes('Analyse', "Deux façons de sortir d'un rendez-vous", [
        ("Sans rien", "« Il m'a expliqué. C'était intéressant. Je pense qu'il faut faire un test. »"),
        ("Avec quelque chose", "« Test le 28 novembre, inscription au comptoir. Preuve à déposer avant le 6 février. Prochain rendez-vous en janvier. »"),
    ], cols=2,
       notes="Faire trouver la différence : des dates, des lieux, des verbes "
             "d'action. C'est le modèle de la production orale de E1.")

    d.billet(
        "Redis la démarche à voix haute, à ton voisin, sans regarder tes notes.",
        exemples=[
            "Six étapes, dans l'ordre.",
            "Ton voisin coche celles que tu as dites ; vous changez ensuite de rôle.",
        ],
        notes="Dix minutes en tout. Circuler et noter les étapes le plus souvent "
              "oubliées : ce sont la cinquième — vérifier — et la sixième — revoir "
              "le conseiller. Les redire au groupe avant de terminer.")

    return d.save(dossier)
