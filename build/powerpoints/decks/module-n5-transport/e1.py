# -*- coding: utf-8 -*-
"""E1 · Expliquer, et appeler
Bloc E « Je me lance » · couleur teal · 75 min. Production orale.
Source : bloc « Je me lance » de l'activité interactive — jeu de rôle
`circulation` et production orale (message de retard).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="Expliquer, et appeler",
        chapeau="C'est à vous. Vous expliquez à votre collègue ce que la "
                "radio vient d'annoncer et vous proposez un autre chemin ; "
                "puis vous laissez un message sur la boîte vocale de votre "
                "responsable pour annoncer votre retard.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Elle se fait presque entièrement debout et à "
                  "deux. Prévoir des postes avec écouteurs pour le jeu de rôle avec "
                  "l'assistant, et un coin calme pour l'enregistrement. L'enseignante "
                  "circule et écoute, elle ne corrige pas pendant.")

    d.objectifs([
        "expliquer une entrave sans que l'autre ait à poser de questions ;",
        "proposer un autre chemin, dans l'ordre et jusqu'au bout ;",
        "laisser un message de retard de trente à quarante-cinq secondes ;",
        "tenir le tutoiement avec le collègue, le vouvoiement avec la responsable.",
    ], notes="Le premier objectif est le critère d'évaluation principal : si le collègue "
             "doit demander « où ? », l'explication n'était pas complète. C'est ce que "
             "l'assistant fait dans le jeu de rôle, et il le fait exprès.")

    d.regle("Six informations, dans l'ordre",
            "Ce qui bloque · où · dans quel sens · depuis quand · par où "
            "passer · à quelle heure on arrive.",
            precision="« Ça bloque » n'est pas une information. Sans nom de route, "
                      "sans repère et sans durée, personne ne peut décider.",
            notes="Diapositive à photographier et à laisser projetée pendant tout "
                  "l'atelier. C'est la grille du jeu de rôle et celle de la correction.")

    d.tableau('Trois situations', "Choisissez la vôtre",
              ['La situation', 'Ce qui est en jeu'],
              [["Le pont fermé", "Trouver un autre pont"],
               ["Le carambolage", "Entrer sur l'autoroute ou non"],
               ["La bretelle en travaux", "Expliquer un chemin pour samedi"]],
              cle=1,
              notes="Les trois cas sont ceux de l'activité interactive. Faire choisir "
                    "chacun selon son trajet réel : celui qui prend un pont tous les "
                    "matins prendra le premier.")

    d.cartes("Ce que fait l'assistant", "Il ne devine rien à votre place", [
        ("Il n'a pas écouté la radio",
         "Il ne sait rien : tout doit venir de vous."),
        ("Il redemande une fois",
         "Si vous dites « ça bloque », il demande où."),
        ("Il ne propose pas le détour",
         "C'est à vous de le trouver et de le dire."),
        ("Il veut une heure",
         "« Bientôt » ne lui suffit jamais."),
    ], notes="Prévenir le groupe : l'assistant est exigeant exprès. Ce n'est pas une "
             "panne ni de la mauvaise volonté — c'est ainsi qu'il fait travailler le "
             "discours suivi demandé au niveau 5.")

    d.tableau('Le message de retard', "Cinq morceaux, dans l\'ordre",
              ['Le morceau', 'Ce qu\'on y met'],
              [["1", "Qui parle, et à qui"],
               ["2", "Ce qui bloque, et où"],
               ["3", "Depuis quand, ce qu'on fait"],
               ["4", "L'heure, et ce qu'on propose"],
               ["5", "Comment vous joindre"]],
              cle=1,
              notes="Faire écrire les cinq lignes avant d'enregistrer. Un message "
                    "improvisé dure quatre-vingt-dix secondes et oublie le nom ; un "
                    "message écrit d'abord en dure quarante et n'oublie rien.")

    d.piege("Enregistrer sans avoir écrit",
            "Je vais improviser, c'est plus naturel.",
            "J'écris mes cinq lignes, je les lis une fois, puis j'enregistre.",
            "Un message improvisé oublie presque toujours deux choses : le nom de "
            "celui qui appelle, et une heure en chiffres. Ce sont justement les deux "
            "qui rendent le message utile.",
            notes="Insister : lire ses notes n'a rien d'artificiel au téléphone. Tout le "
                  "monde le fait, y compris les gens dont c'est la langue maternelle.")

    d.pratique('Autoévaluation', "Réécoutez-vous comme si vous étiez la responsable",
               "Répondez honnêtement avant d'envoyer.", [
        ("Savez-vous qui parle ?", "sinon, le message ne sert à personne"),
        ("Pouvez-vous noter une heure d'arrivée ?", "sinon, rien ne s'organise"),
        ("Savez-vous quoi faire en attendant ?", "sinon, il faudra rappeler"),
        ("Le message dure-t-il moins de 45 secondes ?", "sinon, coupez les excuses"),
        ("Le vouvoiement est-il tenu du début à la fin ?", "sinon, reprenez le début"),
    ], corrige=True,
       notes="Faire faire cette autoévaluation avant l'envoi à l'enseignante, pas après. "
             "Les élèves recommencent d'eux-mêmes une fois sur deux, et c'est le but.")

    d.billet(
        "Après votre enregistrement : notez la chose que vous referiez autrement.",
        exemples=[
            "Une seule chose, la plus importante.",
            "Notez aussi ce qui a bien marché : ça se garde pour la prochaine fois.",
        ],
        notes="Ramasser les billets et les rendre en E2 avec la production écrite. La "
              "comparaison entre ce que l'élève a repéré lui-même et ce que la "
              "rétroaction dit vaut mieux qu'une note.")

    return d.save(dossier)
