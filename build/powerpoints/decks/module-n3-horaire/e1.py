# -*- coding: utf-8 -*-
"""E1 · Je me lance.
Bloc E « Je me lance » · couleur teal · 75 min.
Source : jeu de rôle, production orale et production écrite du module.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre='Je me lance',
        chapeau="Les trois défis se rassemblent en une seule visite au chef "
                "d'équipe : dire l'heure dont on parle, demander, expliquer, "
                "redire l'entente, remercier. Une production orale, un mot à "
                "écrire.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Prévoir des écouteurs : la production orale se "
                  "fait à l'ordinateur, chacun de son côté. C'est ce qui permet de se "
                  "reprendre dix fois sans témoin — et pour ce module, c'est décisif.")

    d.objectifs([
        "tenir une conversation complète avec un chef d'équipe ;",
        "employer les trois défis dans une même production ;",
        "écrire le mot qu'on laisse sur son bureau ;",
        "recevoir une correction et la relire.",
    ])

    d.cartes('Les trois défis, réunis', "Ce qui doit apparaître", [
        ("Défi 1 · l'heure",
         "Dire quel jour et quelle heure posent problème, avec « de… à… ». Redire l'heure "
         "entendue pour la vérifier."),
        ("Défi 2 · la demande",
         "Demander une permission ou de l'aide — « est-ce que je peux… ? » — puis donner "
         "sa raison en une phrase avec « je dois »."),
        ("Défi 3 · la tâche",
         "Dire où on en est : c'est fait, je suis en train de, je vais le faire. Et noter "
         "ce qu'on vous répond."),
    ], notes="Diapo à photographier. C'est la grille de la production orale, et c'est "
             "aussi celle avec laquelle l'enseignante écoute.")

    d.regle("Le jeu de rôle vient en premier",
            "Trois situations, autant de reprises qu'on veut.",
            precision="Dans l'activité : <b>échanger un quart</b> (le "
                      "rendez-vous de jeudi), <b>je n'ai pas compris</b> "
                      "(une consigne donnée trop vite), <b>c'est fait, et "
                      "après ?</b> (la tâche finie avant l'heure). "
                      "L'assistant joue le chef d'équipe.",
            notes="Le chef joué par l'assistant ne devine rien : il faut lui dire le jour, "
                  "l'heure et la raison. Un élève qui attend qu'on lui demande n'obtient "
                  "rien — c'est exactement la leçon du module.")

    d.pratique('Production orale', "Ce qui est demandé",
               "Environ 45 secondes, à l'ordinateur.", [
        ("Temps 1 · s'annoncer", "« Est-ce que je peux vous parler deux minutes ? »"),
        ("Temps 2 · dire l'heure", "le jour et le quart : « jeudi, je travaille de 6 h à 14 h »"),
        ("Temps 3 · demander et expliquer", "la demande, puis la raison avec « je dois »"),
        ("Temps 4 · redire et remercier", "« Alors jeudi, c'est Miguel à six heures. Merci beaucoup. »"),
    ], cols=1,
       notes="On s'enregistre, on s'écoute, on recommence autant de fois qu'on veut. Rien "
             "ne part avant que l'élève appuie sur envoyer : le rappeler avant de "
             "commencer enlève la moitié de la peur.")

    d.piege("Demander sans donner la raison",
            "Est-ce que je peux échanger mon jeudi ?",
            "Est-ce que je peux échanger mon jeudi ? Mon garçon a un rendez-vous.",
            "Une demande sans raison oblige le chef à la demander lui-même, "
            "ou à refuser par prudence. Une phrase suffit — jamais deux, et "
            "jamais de détails intimes.",
            notes="La deuxième partie de la remarque compte : plusieurs élèves expliquent "
                  "trop, par crainte de ne pas être crus. Une phrase courte est plus "
                  "crédible qu'un récit.")

    d.pratique('Production écrite', "Ce qui est demandé",
               "Le mot laissé sur le bureau du chef, de 5 à 8 phrases.", [
        ("Une tâche terminée", "« c'est fait », ou « je viens de finir »"),
        ("Une tâche non terminée", "avec ce qui reste à faire"),
        ("Une heure", "avec « de… à… », « jusqu'à » ou « à partir de »"),
        ("Une demande polie", "« est-ce que je peux… ? »"),
        ("Pour et De", "à qui vous écrivez, et de la part de qui"),
    ], cols=1,
       notes="Les billets de B2, C2 et D2 contiennent déjà presque tout : le faire "
             "remarquer avant de commencer. L'élève assemble plutôt qu'il n'invente, et "
             "c'est ce qui rend l'exercice tenable en une séance.")

    d.regle("Les petits mots de l'heure, à l'écrit",
            "de six heures à quatorze heures · jusqu'à midi · à partir de lundi",
            precision="C'est ce que la correction signale le plus souvent "
                      "sur ce travail : un « à » à la place d'un « de », ou "
                      "une heure donnée sans son petit mot.",
            notes="Diapo à photographier. Le dire avant, plutôt que de le corriger vingt "
                  "fois après.")

    d.tableau('Analyse', "Ce qui est regardé",
              ['Le critère', 'Ce qui compte'],
              [["La tâche", "les quatre temps sont là"],
               ["Le vocabulaire", "les mots du travail sont employés"],
               ["La langue", "les heures, la demande polie, où on en est"],
               ["La clarté", "on comprend du premier coup"]],
              cle=3,
              note="La clarté passe avant la perfection : une phrase simple "
                   "et juste vaut mieux qu'une phrase compliquée et fausse.",
              notes="Diapo à photographier. Le dire avant que les élèves commencent, pas "
                    "au moment de rendre les corrections.")

    d.billet(
        "Notez ce que la correction vous a signalé.",
        exemples=[
            "Deux choses réussies, deux choses à travailler.",
            "Gardez la note : elle sert à la séance E2.",
        ],
        notes="La correction n'est pas conservée par le système : elle s'affiche et elle "
              "disparaît. Cette note est la seule trace qu'il en restera — le dire "
              "clairement pour que les élèves la prennent.")

    return d.save(dossier)
