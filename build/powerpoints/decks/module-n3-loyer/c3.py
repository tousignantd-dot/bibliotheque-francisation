# -*- coding: utf-8 -*-
"""C3 · Mes trois questions, préparées.
Bloc C « Défi 2 · Téléphoner pour visiter » · couleur ambre · 75 min.
Source : exercices `t2trois` et `t2ordre`, mini-leçon `t2trois`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre='Mes trois questions, préparées',
        chapeau="On n'improvise pas un appel dans une langue nouvelle. Trois "
                "questions écrites sur un bout de papier, et l'appel se tient "
                "tout seul.",
        duree='75 minutes')

    d.titre(notes="Séance de préparation. Distribuer à chacun un petit papier vierge dès "
                  "l'ouverture : il servira toute la séance et sera emporté à la maison. "
                  "C'est un objet, pas une métaphore.")

    d.objectifs([
        "poser une question sur ce qui est compris dans le loyer ;",
        "poser une question sur le nombre de chambres ;",
        "poser une question sur la date à laquelle le logement est libre ;",
        "poser les questions une à la fois, et noter les réponses.",
    ])

    d.regle("Trois questions, écrites avant de composer le numéro",
            "L'argent, la place, la date",
            precision="Une personne qui n'a rien préparé oublie la moitié de "
                      "ce qu'elle voulait demander et rappelle deux heures "
                      "plus tard. Écrivez-les vraiment : les gens qui parlent "
                      "français depuis toujours le font aussi.",
            notes="Diapositive à photographier. Faire écrire les trois questions sur le "
                  "papier distribué, en toutes lettres, avant d'aller plus loin dans la "
                  "séance.")

    d.tableau('Analyse', "Les trois questions, et pourquoi celles-là",
              ["La question", "Pourquoi"],
              [["Est-ce que c'est chauffé ?", "elle change le vrai prix"],
               ["Combien de chambres ?", "elle dit si ça convient"],
               ["À quelle date c'est libre ?", "elle dit si c'est possible"],
               ["Je pourrais le visiter ?", "c'est le but de l'appel"]],
              cle=0,
              note="Trois questions, puis la demande.",
              notes="Diapositive à photographier. Expliquer pourquoi on s'arrête à "
                    "trois : au-delà, on ne retient plus les réponses et on prend le "
                    "temps de quelqu'un qui a d'autres appels.")

    d.tableau('Analyse', "Poser une question, trois façons",
              ["La façon", "Un exemple"],
              [["la voix qui monte", "C'est chauffé ?"],
               ["avec est-ce que", "Est-ce que c'est chauffé ?"],
               ["avec un mot de question", "Combien il y a de chambres ?"],
               ["le plus sûr au téléphone", "avec est-ce que"]],
              cle=1,
              note="Est-ce que se met devant la phrase et ne change rien d'autre.",
              notes="Diapositive à photographier. Recommander « est-ce que » sans "
                    "interdire le reste : c'est la forme qui se comprend le mieux quand "
                    "la ligne est mauvaise.")

    d.tableau('Analyse', "Les mots de question",
              ["Le mot", "Ce qu'il demande"],
              [["combien", "un nombre, un prix"],
               ["quand", "un moment"],
               ["à quelle date", "un jour précis"],
               ["où", "un endroit, une adresse"]],
              cle=0,
              note="Ils se mettent devant est-ce que : combien est-ce que…",
              notes="Diapositive à photographier. « À quelle date » est plus précis que "
                    "« quand » et donne toujours une meilleure réponse : le faire "
                    "remarquer.")

    d.piege('Méthode',
            "poser les trois questions d'un coup",
            "une question, une réponse, puis la suivante",
            "« Est-ce que c'est chauffé, il y a combien de chambres et c'est "
            "libre quand ? » : la personne ne répondra qu'à la dernière, et "
            "vous n'oserez pas redemander les deux autres.",
            notes="Faire la démonstration en jouant la propriétaire : poser les trois "
                  "questions d'un trait à un élève et ne répondre qu'à la dernière. La "
                  "leçon se retient mieux qu'expliquée.")

    d.piege('Méthode',
            "ne rien noter pendant l'appel",
            "écrire le prix, la date et l'adresse en écoutant",
            "Trois logements en deux jours, et tout se mélange. Le papier des "
            "questions sert aussi à écrire les réponses : une colonne pour "
            "chaque.",
            notes="Montrer le papier avec deux colonnes : les questions à gauche, la "
                  "place des réponses à droite. C'est ce qui transforme un appel en "
                  "information utilisable.")

    d.pratique('Grammaire', "Complétez la question",
               "Un seul mot manque.", [
        ("Est-ce que le chauffage est ___ dans le loyer ?", "compris"),
        ("___ est-ce qu'il y a de chambres ?", "Combien"),
        ("À quelle ___ est-ce que le logement est libre ?", "date"),
        ("___ est-ce que je pourrais le visiter ?", "Quand"),
        ("C'est à quelle ___ , exactement ?", "adresse"),
        ("Pouvez-vous ___ , s'il vous plaît ?", "répéter"),
    ], corrige=True, cols=2,
       notes="C'est l'exercice 3 du Défi 2. Faire dire chaque question complète à voix "
             "haute après l'avoir complétée : écrite seulement, elle ne sert à rien.")

    d.pratique('Production', "Ce qu'on dit, et à quel moment",
               "Associez le moment de l'appel et la phrase.", [
        ("La personne décroche.", "Bonjour. Je vous appelle pour l'annonce."),
        ("On vous demande qui va habiter là.", "Nous sommes trois."),
        ("Vous voulez savoir ce qui est compris.", "Est-ce que le chauffage est compris ?"),
        ("Vous n'avez pas entendu la date.", "Pouvez-vous répéter, s'il vous plaît ?"),
        ("Vous voulez voir le logement.", "Est-ce que je pourrais le visiter ?"),
        ("Le rendez-vous est pris.", "Samedi, dix heures. Merci beaucoup."),
    ], corrige=True,
       notes="C'est l'exercice 5 du Défi 2, sous forme orale. Enchaîner en faisant jouer "
             "l'appel complet à deux, dos à dos : c'est la meilleure imitation du "
             "téléphone qu'on puisse faire en classe.")

    d.billet(
        "Écrivez vos trois questions et gardez le papier dans votre poche.",
        exemples=[
            "1. Est-ce que ___ ?",
            "2. Combien ___ ? 3. À quelle date ___ ?",
        ],
        notes="Devoir court, et objet réel : le papier doit revenir à la séance C4, puis "
              "servir à la production orale de E1. Le demander à chaque séance.")

    return d.save(dossier)
