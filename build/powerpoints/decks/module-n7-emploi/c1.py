# -*- coding: utf-8 -*-
"""C1 · Ce qui se passe au poste 4
Bloc C « Défi 2 · Le poste 4 » · couleur acier · 75 min.
Source du module : dialogue `t2`, exercice `t2compr`.
"""
import pathlib

from theme import Deck

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n7-emploi' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Ce qui se passe au poste 4",
        chapeau="Deux semaines après avoir écouté, c'est Aïcha qui a quinze "
                "minutes. Elle ne va pas se plaindre du poste 4 : elle va "
                "l'exposer. Le constat, la cause, la conséquence chiffrée, le "
                "correctif, l'échéance.",
        duree='75 minutes')

    d.titre(notes="Ouverture du Défi 2. C'est le modèle que chaque élève imitera en "
                  "E1. Faire entendre l'extrait en entier une première fois, puis par "
                  "morceaux. Vingt et une répliques.")

    d.objectifs([
        "suivre une présentation faite par quelqu'un qui n'est pas le patron ;",
        "repérer les cinq parties dans un discours réel ;",
        "reconnaître ce que la présentatrice dit ne pas savoir ;",
        "comprendre pourquoi le correctif gratuit vient avant le payant.",
    ], notes="Le troisième objectif porte sur une phrase précise, et c'est la plus "
             "importante du module : « je ne voulais pas l'inventer ici ».")

    d.declencheur(
        'Observation', "Quatre-vingt-deux fois par quart de travail",
        image=IMG + 'table-elevatrice.jpg',
        pistes=[
            "Que fait cet appareil, à votre avis ?",
            "Qu'est-ce qui change pour la personne qui emballe ?",
            "Avez-vous déjà eu mal au dos à cause d'un poste de travail ?",
            "À qui l'auriez-vous dit ?",
        ],
        notes="La table élévatrice est le correctif payant du projet d'Aïcha. La "
              "montrer avant l'écoute rend la présentation beaucoup plus facile à "
              "suivre : l'élève sait de quel objet on parle.")

    d.dialogue('Dialogue · 1 de 5', "Le plan annoncé, puis le constat", [
        ("AÏCHA", "J'ai quinze minutes pour vous parler du poste 4. Je vais faire comme monsieur Cormier : le constat, la cause, ce que ça coûte, ce que je propose, et une date.", True),
        ("AÏCHA", "Le constat. Depuis mars, trois personnes du poste 4 ont consulté pour le dos. Jean-Marc a été absent onze jours ouvrables, Suzanne quatre, et Kadiatou travaille en tâches allégées depuis le 2 juin.", True),
        ("RENAUD", "Trois personnes sur combien, au poste 4 ?", False),
        ("AÏCHA", "Sur cinq. C'est ce qui m'a fait commencer à compter, justement.", False),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Première réplique : elle annonce son plan. C'est le geste que le groupe "
             "devra reproduire en E1, et il coûte quinze secondes.")

    d.dialogue('Dialogue · 2 de 5', "La cause, et ce qui use vraiment", [
        ("AÏCHA", "La cause. Les caisses vides arrivent sur une palette, posées à terre. L'emballeur se penche, prend la caisse, se relève, la remplit, puis la repose à terre.", True),
        ("AÏCHA", "J'ai compté quatre-vingt-deux caisses par quart en moyenne, sur six quarts différents. Ce qui use le dos, ce n'est pas le poids d'une caisse, c'est de se pencher quatre-vingt-deux fois.", True),
        ("THÉRÈSE", "C'est exactement ce que la manutention manuelle répétitive veut dire. C'est nommé dans notre programme de prévention, section 3.", False),
        ("AÏCHA", "Merci, Thérèse, j'y arrive.", False),
    ], notes="« Ce qui use le dos, c'est... » : première mise en relief du module. La "
             "faire répéter ; la séance C3 est faite pour elle.")

    d.dialogue('Dialogue · 3 de 5', "Ce que ça coûte, et ce qu'elle ne sait pas", [
        ("AÏCHA", "Les conséquences, en chiffres. Quinze jours ouvrables d'absence depuis mars, plus un poste en tâches allégées depuis onze semaines.", True),
        ("AÏCHA", "Chaque jour d'absence se remplace par une agence, à un taux plus élevé que le nôtre. Je n'ai pas le chiffre exact, madame Ouellet l'a et je ne voulais pas l'inventer ici.", True),
        ("RENAUD", "Vous avez bien fait. Je le demanderai. Continuez.", False),
    ], notes="Diapositive centrale du module. La réaction de monsieur Cormier est la "
             "démonstration : dire qu'on ne sait pas ne fait pas perdre de crédit, ça "
             "en donne. Le faire remarquer explicitement.")

    d.dialogue('Dialogue · 4 de 5', "Deux correctifs, le gratuit d'abord", [
        ("AÏCHA", "La première : une table élévatrice à ciseaux. La palette est dessus, et la caisse reste toujours à la même hauteur. L'emballeur ne se penche plus.", True),
        ("AÏCHA", "La deuxième : faire tourner les gens. Quatre heures d'emballage, quatre heures ailleurs. Ça ne coûte rien du tout, et on pourrait l'essayer lundi prochain.", True),
        ("THÉRÈSE", "Ce qui est intéressant, c'est que la deuxième partie ne dépend pas de la première.", False),
        ("AÏCHA", "C'est voulu. Si la table est refusée, la rotation reste possible.", False),
    ], notes="L'ordre est stratégique et la dernière réplique le dit. Faire nommer par "
             "le groupe ce qui se passerait si Aïcha n'avait proposé que la table.")

    d.dialogue('Dialogue · 5 de 5', "Ce qu'elle demande, et ce qu'elle obtient", [
        ("RENAUD", "Combien coûte la table ?", False),
        ("AÏCHA", "Je ne le sais pas encore. J'ai le nom d'un fournisseur et je voudrais leur demander une soumission écrite. C'est ce que je viens vous demander : l'autorisation d'écrire, et le nom de la personne qui doit signer.", True),
        ("RENAUD", "L'autorisation, vous l'avez. Écrivez « demande de soumission », pas « commande ». Ce n'est pas la même chose du tout, et une lettre mal formulée nous engage.", True),
        ("RENAUD", "Mettez-moi tout ça dans une note de service pour l'équipe, et la lettre part chez le fournisseur cette semaine.", True),
    ], notes="La dernière réplique lance le bloc D. Écrire au tableau les deux "
             "documents demandés : une note de service, une lettre d'affaires.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la présentation d'Aïcha.", [
        ("Elle annonce son plan avant de commencer.", "vrai"),
        ("Elle a compté les caisses sur un seul quart.", "faux - sur six quarts"),
        ("Elle dit que le poids d'une caisse use le dos.", "faux - c'est la répétition"),
        ("Elle donne le coût exact des remplacements par l'agence.", "faux - elle dit qu'elle ne l'a pas"),
        ("Elle propose d'abord la solution qui ne coûte rien.", "vrai"),
        ("Monsieur Cormier lui demande d'écrire « commande ».", "faux - « demande de soumission »"),
    ], corrige=True,
       notes="C'est l'exercice `t2compr` du module, qui en compte dix. Les quatre "
             "autres se font en autonomie.")

    d.billet(
        "Écrivez la conséquence chiffrée de votre projet.",
        exemples=[
            "Combien de jours, d'heures, de dollars ou de retards ?",
            "S'il vous manque un chiffre, écrivez qui l'a.",
        ],
        notes="Ramasser. C'est la quatrième pièce du projet de chacun. Vérifier "
              "surtout la dernière consigne : ceux qui inventent un chiffre plutôt que "
              "de nommer qui le détient n'ont pas compris la séance.")

    return d.save(dossier)
