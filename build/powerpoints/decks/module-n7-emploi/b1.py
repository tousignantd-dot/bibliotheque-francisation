# -*- coding: utf-8 -*-
"""B1 · Douze minutes pour un projet
Bloc B « Défi 1 · La réunion de production » · couleur acier · 75 min.
Source du module : dialogue `t1`, exercice `t1compr`.
"""
import pathlib

from theme import Deck

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n7-emploi' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Douze minutes pour un projet",
        chapeau="Le chef de production présente son projet de quai. Personne "
                "ne le répétera et il n'y a pas de document. Comprendre une "
                "présentation, ce n'est pas retenir chaque mot : c'est "
                "reconnaître dans quelle partie on est rendu.",
        duree='75 minutes')

    d.titre(notes="Ouverture du Défi 1. C'est le plus long extrait audio du module "
                  "avec celui du Défi 2 : vingt-deux répliques, dont plusieurs de "
                  "quatre phrases. Prévoir trois écoutes - une pour le sujet, une pour "
                  "les chiffres, une pour le détail - et le dire au groupe d'avance.")

    d.objectifs([
        "suivre une présentation longue sans se décourager ;",
        "repérer l'objectif, les étapes, l'échéancier, le budget, les risques ;",
        "distinguer un chiffre estimé d'un chiffre confirmé ;",
        "poser une question précise à la fin d'une présentation.",
    ], notes="Le troisième objectif porte sur une phrase précise du dialogue : « je "
             "précise estimée, je n'ai pas encore de soumission ». La faire remarquer.")

    d.declencheur(
        'Écoute', "Une réunion de production, un lundi matin",
        image=IMG + 'salle-reunion.jpg',
        pistes=[
            "Avez-vous déjà assisté à une réunion en français ?",
            "Qu'est-ce qui est le plus difficile : les mots, la vitesse, l'accent ?",
            "Que faites-vous quand vous perdez le fil ?",
            "Osez-vous demander qu'on répète ?",
        ],
        notes="La dernière question est la plus utile. Beaucoup d'élèves n'osent pas, "
              "et une réunion est justement un endroit où demander de répéter est "
              "normal - Thérèse le fait dans le dialogue, dès la quatrième réplique.")

    d.dialogue('Dialogue · 1 de 5', "L'objectif", [
        ("RENAUD", "Il est huit heures cinq, tout le monde est là, on commence. Premier point : le réaménagement du quai d'expédition. J'en ai pour une douzaine de minutes.", True),
        ("RENAUD", "Depuis janvier, on charge en moyenne dix-neuf camions par jour, contre quatorze l'an dernier. Le quai, lui, n'a pas changé depuis 2009.", True),
        ("RENAUD", "L'objectif du projet tient en une phrase : ramener le temps d'attente moyen sous les vingt minutes, sans agrandir le bâtiment.", True),
        ("THÉRÈSE", "Vingt minutes, c'est la moyenne ou c'est le maximum ?", False),
    ], consigne="Première écoute : de quoi parle-t-il ? Rien d'autre.",
       notes="Faire écouter diapositive masquée. Ne demander que le sujet. Résister à "
             "l'envie de tout traiter dès la première écoute : c'est ce qui décourage.")

    d.dialogue('Dialogue · 2 de 5', "Les quatre étapes", [
        ("RENAUD", "Ensuite, les étapes. Il y en a quatre. D'abord, on mesure : deux semaines de relevés, chaque camion chronométré.", True),
        ("RENAUD", "Ensuite, on trace : un plan à l'échelle. Puis on essaie : un mois à l'essai, sans rien acheter, juste avec du ruban jaune au sol. Enfin, on installe pour de bon.", True),
        ("AÏCHA", "Pourquoi mesurer d'abord ? On sait déjà que ça bloque.", False),
        ("RENAUD", "On sait que ça bloque, mais on ne sait pas où. Une fois qu'on aura deux semaines de relevés, on ne discutera plus d'impressions.", True),
    ], notes="Faire compter les connecteurs : d'abord, ensuite, puis, enfin. Ce sont "
             "eux qui rendent les quatre étapes repérables, et c'est tout le sujet de "
             "la séance B3.")

    d.dialogue('Dialogue · 3 de 5', "L'échéancier", [
        ("RENAUD", "Les relevés commencent le 8 septembre et se terminent le 19. Le plan sera prêt pour la réunion du 6 octobre. L'essai courra du 13 octobre au 14 novembre.", True),
        ("RENAUD", "Et quand l'essai sera terminé, on décidera - pas avant.", True),
        ("THÉRÈSE", "Donc rien n'est acheté avant la mi-novembre.", False),
        ("RENAUD", "Rien du tout. C'est voulu. Le jour où j'irai demander de l'argent, je veux pouvoir dire que la solution a déjà fonctionné dans notre cour.", True),
    ], notes="« Quand l'essai sera terminé » : premier futur antérieur du module. Le "
             "souligner sans l'expliquer - la séance B4 est faite pour ça.")

    d.dialogue('Dialogue · 4 de 5', "Le budget, et ce qu'il n'est pas", [
        ("RENAUD", "L'essai coûte quatre cents dollars : du ruban, des cônes, deux panneaux.", False),
        ("RENAUD", "L'installation définitive est estimée entre onze et treize mille dollars. Je précise « estimée » : je n'ai pas encore de soumission, seulement un prix approximatif donné au téléphone.", True),
        ("AÏCHA", "Et si l'essai ne marche pas ?", False),
        ("RENAUD", "Alors on aura dépensé quatre cents dollars et on saura pourquoi. Ce n'est pas un échec, c'est un résultat.", True),
    ], notes="Deuxième réplique : le mot « estimée » et le conditionnel de "
             "l'incertitude. C'est ce que le module demandera à l'élève de faire en "
             "C2, quand il dira ce qu'il ne sait pas.")

    d.dialogue('Dialogue · 5 de 5', "Les trois risques, et la suite", [
        ("RENAUD", "Les risques, pour finir. Il y en a trois, et je préfère les nommer moi-même. Le premier : la circulation dans la cour change pendant l'essai.", True),
        ("THÉRÈSE", "Le premier risque, je veux qu'il soit noté au procès-verbal.", False),
        ("RENAUD", "En somme : on mesure, on trace, on essaie, on installe. Deux mois et demi, quatre cents dollars pour savoir, et une décision en novembre.", True),
        ("RENAUD", "Madame Traoré, vous avez quinze minutes le 15 septembre si vous les voulez. Dites-moi d'ici vendredi.", True),
    ], notes="La dernière réplique lance tout le bloc C. Le dire : Aïcha a maintenant "
             "une date, et c'est ce qu'elle était venue chercher sans le demander.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la présentation.", [
        ("L'objectif est de ramener l'attente moyenne sous vingt minutes.", "vrai"),
        ("Le projet prévoit d'agrandir le bâtiment.", "faux - « sans agrandir le bâtiment »"),
        ("Le prix de onze à treize mille dollars vient d'une soumission.", "faux - d'un appel téléphonique"),
        ("Monsieur Cormier annonce lui-même les trois risques.", "vrai"),
        ("La décision d'installer se prend avant l'essai.", "faux - « pas avant »"),
        ("Aïcha obtient quinze minutes le 15 septembre.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. C'est l'exercice "
             "`t1compr` du module, qui en compte dix : les quatre autres se font en "
             "autonomie.")

    d.billet(
        "Notez les cinq parties de la présentation, dans l'ordre, avec un mot chacune.",
        exemples=[
            "Objectif : ...",
            "Étapes : ...",
            "Échéancier : ...",
        ],
        notes="Devoir de prise de notes. C'est exactement ce que Thérèse a demandé à "
              "Aïcha de faire, et c'est la préparation de la séance B2.")

    return d.save(dossier)
