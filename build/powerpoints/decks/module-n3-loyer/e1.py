# -*- coding: utf-8 -*-
"""E1 · Je me lance — la visite, à voix haute.
Bloc E « Je me lance » · couleur teal · 75 min. Production orale.
Source : section `appli`, jeu de rôle `visite`, dialogue `appli`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre='Je me lance — la visite, à voix haute',
        chapeau="Tout ce que les quatorze séances ont préparé tient en deux "
                "minutes de parole : saluer, demander, comprendre, vérifier.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. C'est la production orale du module, et elle "
                  "est déposable : les élèves s'enregistrent et envoient. Rassurer le "
                  "groupe — on peut recommencer autant de fois qu'on veut avant "
                  "d'envoyer, et la correction de l'assistant reste privée.")

    d.objectifs([
        "téléphoner au sujet d'une annonce, du début à la fin ;",
        "poser au moins trois questions ;",
        "faire répéter quand on n'a pas compris un chiffre ou une date ;",
        "répéter le rendez-vous avant de raccrocher.",
    ])

    d.dialogue('Dialogue · modèle', "Un deux et demie meublé", [
        ("RACHID", "Bonjour, je vous appelle pour le deux et demie de la rue Saint-Hubert.", True),
        ("CLAUDINE", "Bonjour. Il est encore libre, oui.", True),
        ("RACHID", "L'annonce dit « meublé ». Qu'est-ce qu'il y a dedans ?", True),
        ("CLAUDINE", "Un lit, une table, deux chaises et une commode. Pas de vaisselle.", True),
        ("RACHID", "Est-ce que je pourrais le voir demain après-midi ?", True),
        ("CLAUDINE", "Demain, deux heures. Je vous attends.", True),
    ], consigne="Un dernier modèle avant de se lancer.",
       notes="Ce dialogue montre une annonce que le groupe n'a pas travaillée : un deux "
             "et demie meublé. Le faire remarquer — la structure de l'appel ne change "
             "pas, seules les questions changent.")

    d.tableau('Analyse', "Les trois temps de la production orale",
              ["Le temps", "Ce qu'on dit"],
              [["1 · dire pourquoi on appelle", "Je vous appelle pour l'annonce."],
               ["2 · poser ses trois questions", "Est-ce que le chauffage est compris ?"],
               ["3 · prendre rendez-vous et répéter", "Samedi, dix heures. C'est bien ça ?"]],
              cle=0,
              note="Environ quarante-cinq secondes en tout.",
              notes="Diapositive à photographier. C'est le plan exact de la production "
                    "orale, celui qui s'affiche à l'écran de l'élève. Le faire recopier "
                    "avant de commencer.")

    d.tableau('Analyse', "Les huit sujets du jeu de rôle · 1 de 2",
              ["Le sujet", "Un exemple"],
              [["saluer et dire pourquoi on vient", "Bonjour, c'est pour l'annonce."],
               ["combien de personnes", "Nous sommes trois."],
               ["ce qui est compris", "Est-ce que le chauffage est compris ?"],
               ["le nombre de chambres", "Combien il y a de chambres fermées ?"]],
              cle=0,
              notes="Diapositive à photographier. Les quatre premiers sujets, ceux "
                    "qu'aucun élève n'oublie. C'est la même liste que dans l'activité "
                    "interactive, où elle se coche.")

    d.tableau('Analyse', "Les huit sujets du jeu de rôle · 2 de 2",
              ["Le sujet", "Un exemple"],
              [["la buanderie et le stationnement", "Est-ce qu'il y a une buanderie ?"],
               ["la date", "À quelle date est-ce libre ?"],
               ["faire répéter", "Pouvez-vous répéter, s'il vous plaît ?"],
               ["répéter avant de partir", "1 150 $, le 1er juillet. C'est ça ?"]],
              cle=0,
              note="L'assistant ne dit rien qu'on ne lui demande pas.",
              notes="Diapositive à photographier. Ce sont les quatre derniers sujets qui "
                    "font la différence entre une visite subie et une visite menée. "
                    "Insister sur le dernier.")

    d.regle("Ce qui distingue une bonne prise de parole",
            "Poser des questions, et vérifier à la fin",
            precision="Ce n'est pas la perfection grammaticale. Un élève qui "
                      "pose trois questions et redit le loyer et la date a "
                      "réussi, même avec des fautes. Un élève qui ne dit rien "
                      "et hoche la tête n'a pas réussi, même sans faute.",
            notes="Diapositive à photographier. Le dire franchement : c'est le critère "
                  "d'évaluation, et il correspond à ce que le programme demande — "
                  "demander et comprendre des renseignements sur le logement.")

    d.pratique('Préparation', "Trois logements au choix",
               "Choisissez le vôtre et préparez vos questions.", [
        ("Le 4 ½ de la rue Chabot", "1 150 $, chauffé et éclairé, libre le 1er juillet"),
        ("Le 3 ½ au sous-sol", "850 $, non chauffé, laveuse incluse, chat accepté"),
        ("Le 2 ½ meublé", "780 $, tout compris sauf internet, libre tout de suite"),
    ], corrige=True,
       notes="Laisser cinq minutes de préparation écrite avant de parler. Le deuxième "
             "logement est le plus intéressant : « non chauffé » oblige à poser la "
             "question du coût réel, vue à la séance B3.")

    d.pratique('Production', "Le jeu de rôle avec l'assistant",
               "À l'écran : choisissez le logement, le rôle et le mode.", [
        ("Vous jouez la personne qui visite.", "l'assistant fait visiter"),
        ("Vous jouez la propriétaire.", "l'assistant vient visiter"),
        ("En écrivant.", "pour préparer, sans la pression de la voix"),
        ("En parlant.", "pour de vrai, comme au téléphone"),
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
            "Je vais la répéter avant de téléphoner.",
        ],
        notes="Devoir court. Les questions signalées ici sont à reprendre en début de "
              "séance E2, avant la production écrite.")

    return d.save(dossier)
