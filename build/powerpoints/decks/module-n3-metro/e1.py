# -*- coding: utf-8 -*-
"""E1 · Je me lance — au comptoir, à voix haute.
Bloc E « Je me lance » · couleur teal · 75 min. Production orale.
Source : section `appli`, jeu de rôle `titre`, dialogue `appli`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre='Je me lance — au comptoir, à voix haute',
        chapeau="Tout ce que les quatorze séances ont préparé tient en deux "
                "minutes de parole : saluer, demander, comprendre, vérifier.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. C'est la production orale du module, et elle "
                  "est déposable : les élèves s'enregistrent et envoient. Rassurer le "
                  "groupe — on peut recommencer autant de fois qu'on veut avant "
                  "d'envoyer.")

    d.objectifs([
        "acheter un titre de transport à voix haute, du début à la fin ;",
        "poser au moins trois questions au comptoir ;",
        "faire répéter quand on n'a pas compris ;",
        "vérifier le titre et le prix avant de payer.",
    ])

    d.dialogue('Dialogue · modèle', "Un titre pour la fin de semaine", [
        ("MAXIME", "Bonjour. Ma sœur arrive samedi et elle reste trois jours.", True),
        ("LORRAINE", "Elle va se déplacer beaucoup ?", True),
        ("MAXIME", "Oui, elle veut visiter la ville. Le métro, l'autobus, partout.", True),
        ("LORRAINE", "Alors le Week-end illimité. Dix-sept dollars, du vendredi seize heures au lundi cinq heures.", True),
        ("MAXIME", "Elle n'a pas de carte OPUS. Est-ce que c'est un problème ?", True),
        ("LORRAINE", "Non. Je peux le mettre sur une carte à puce occasionnelle.", True),
    ], consigne="Un dernier modèle avant de se lancer.",
       notes="Ce dialogue montre une situation que les élèves n'ont pas encore "
             "travaillée : acheter pour quelqu'un d'autre. Le faire remarquer — la "
             "structure ne change pas, seul le titre change.")

    d.tableau('Analyse', "Les trois temps de la prise de parole",
              ["Le temps", "Ce qu'on dit"],
              [["1 · dire ce qu'on vient chercher", "Bonjour. Je voudrais un titre de transport, s'il vous plaît."],
               ["2 · demander le prix et le tarif réduit", "Combien coûte le mensuel ? Est-ce que ma fille paie moins cher ?"],
               ["3 · répéter avant de payer", "Un mensuel, zone A, cent dix dollars. C'est ça ?"]],
              cle=0,
              note="Environ quarante-cinq secondes en tout.",
              notes="Diapositive à photographier. C'est le plan exact de la production "
                    "orale du module, celui qui s'affiche à l'écran de l'élève. Le faire "
                    "recopier avant de commencer.")

    d.tableau('Analyse', "Les sept sujets du jeu de rôle · 1 de 2",
              ["Le sujet", "Un exemple"],
              [["saluer et dire ce qu'on cherche", "Bonjour. Je voudrais…"],
               ["combien de fois par semaine", "Je me déplace dix fois."],
               ["dans quelle zone on reste", "Tout est à Montréal."],
               ["le prix du titre", "Combien coûte le mensuel ?"]],
              cle=0,
              notes="Diapositive à photographier. Les quatre premiers sujets, ceux "
                    "qu'aucun élève n'oublie. C'est la même liste que dans l'activité "
                    "interactive, où elle se coche.")

    d.tableau('Analyse', "Les sept sujets du jeu de rôle · 2 de 2",
              ["Le sujet", "Un exemple"],
              [["le tarif réduit", "Est-ce qu'elle paie moins cher ?"],
               ["ce qu'il faut apporter", "Qu'est-ce que je dois apporter ?"],
               ["faire répéter un chiffre", "Pardon, pouvez-vous répéter ?"],
               ["répéter le titre et le prix", "Un mensuel, 110 $. C'est ça ?"]],
              cle=0,
              note="L'assistant ne dit rien qu'on ne lui demande pas.",
              notes="Diapositive à photographier. Ce sont les trois derniers sujets qui "
                    "font la différence entre une conversation subie et une "
                    "conversation menée. Insister sur le dernier.")

    d.regle("Ce qui distingue une bonne prise de parole",
            "Poser des questions, et vérifier à la fin",
            precision="Ce n'est pas la perfection grammaticale. Un élève qui "
                      "pose trois questions et redit le prix avant de payer a "
                      "réussi, même avec des fautes. Un élève qui ne dit rien "
                      "et hoche la tête n'a pas réussi, même sans faute.",
            notes="Diapositive à photographier. Le dire franchement : c'est le critère "
                  "d'évaluation, et il correspond à ce que le programme demande — "
                  "demander et comprendre l'information pour acheter un titre.")

    d.pratique('Préparation', "Trois situations au choix",
               "Choisissez la vôtre et préparez vos questions.", [
        ("Le titre du mois", "vous vous déplacez cinq jours par semaine, zone A"),
        ("Le tarif réduit de la famille", "une fille de 15 ans, une mère de 68 ans"),
        ("La visiteuse de trois jours", "elle arrive samedi, repart lundi, aucune carte"),
    ], corrige=True,
       notes="Laisser cinq minutes de préparation écrite avant de parler. Les élèves "
             "les plus timides choisissent presque toujours la première : c'est bien, "
             "elle est la plus proche de leur vie.")

    d.pratique('Production', "Le jeu de rôle avec l'assistant",
               "À l'écran : choisissez la situation, le rôle et le mode.", [
        ("Vous jouez le client.", "l'assistant tient le comptoir"),
        ("Vous jouez la personne au comptoir.", "l'assistant vient acheter"),
        ("En écrivant.", "pour préparer, sans la pression de la voix"),
        ("En parlant.", "pour de vrai, comme au guichet"),
    ], corrige=True,
       notes="Faire commencer en mode écrit, puis refaire la même situation en mode "
             "parlé. Le deuxième passage est toujours meilleur, et le dire aux élèves "
             "les décomplexe.")

    d.pratique('Production', "L'enregistrement à déposer",
               "Trois temps, environ quarante-cinq secondes.", [
        ("Je m'enregistre.", "on peut recommencer autant de fois qu'on veut"),
        ("Je m'écoute et je corrige.", "l'assistant donne une rétroaction"),
        ("J'envoie à mon enseignant.", "seulement quand on est prêt"),
    ], corrige=True,
       notes="Insister sur le troisième temps : la correction de l'assistant reste "
             "privée, rien ne part sans un geste de l'élève. C'est une règle du projet "
             "et elle rassure beaucoup.")

    d.billet(
        "Écrivez la question que vous avez trouvée la plus difficile à poser.",
        exemples=[
            "La question la plus difficile pour moi, c'est ___ .",
            "Je vais la répéter avant d'aller au comptoir.",
        ],
        notes="Devoir court. Les questions signalées ici sont à reprendre en début de "
              "séance E2, avant la production écrite.")

    return d.save(dossier)
