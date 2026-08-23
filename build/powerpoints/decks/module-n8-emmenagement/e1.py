# -*- coding: utf-8 -*-
"""E1 · L'appel de révision
Bloc E « Je me lance » · couleur framboise · 75 min.
Production orale. Source du module : le jeu de rôle `sinistre` et la
production orale de « Je me lance ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='framboise',
        titre="L'appel de révision",
        chapeau="Tout ce que le module a enseigné tient dans un appel de dix "
                "minutes : découper, concéder, exiger la clause, retourner, "
                "proposer.",
        duree='75 minutes')

    d.titre(notes="Séance de production orale. Deux temps : le jeu de rôle "
                  "avec l'assistant dans le module, puis l'enregistrement "
                  "individuel. Prévoir les écouteurs — trente appels "
                  "simultanés dans une classe, c'est ingérable sans.")

    d.objectifs([
        "mener un appel de révision en cinq étapes, dans l'ordre ;",
        "obtenir la clause exacte d'un refus ;",
        "proposer un montant justifié avec une contrepartie ;",
        "porter la même réclamation de vive voix au transporteur.",
    ], notes="Le quatrième objectif est la production orale déposable : elle "
             "s'adresse au déménageur et non à l'assureur, donc le ton n'est "
             "pas le même.")

    d.declencheur(
        'Pour commencer', "Vous avez dix minutes au téléphone. Par quoi "
                          "commencez-vous ?",
        pistes=[
            "Le grief le plus grave, ou le point que vous acceptez ?",
            "Pourquoi commencer par ce qu'on accepte ?",
            "Combien de points contestez-vous dans un même appel ?",
        ],
        notes="Les trois réponses sont dans le module : on commence par ce "
              "qu'on accepte, parce que ça rend crédible, et on ne conteste "
              "qu'un point à la fois.")

    d.tableau('Analyse', "Les cinq étapes, une dernière fois",
              ['L\'étape', 'La phrase qui l\'ouvre'],
              [["1. Découper", "Reprenons les trois points l'un après l'autre."],
               ["2. Concéder", "Celle-là, je l'accepte : la clause est claire."],
               ["3. Exiger la clause", "Sur quelle clause vous appuyez-vous, exactement ?"],
               ["4. Retourner", "Certes… Or le meuble a été fendu dans l'escalier."],
               ["5. Proposer", "Ce que je propose, c'est huit cent cinquante dollars, contre…"]],
              cle=0,
              note="Les étapes ne s'inversent pas. Concéder après avoir contesté ne compte pas.",
              notes="Diapositive à photographier, si ce n'est pas déjà fait "
                    "en C1. Laisser affichée pendant le jeu de rôle.")

    d.cartes('Jeu de rôle', "L'assistant joue l'experte en sinistre", [
        ("Ce qu'elle est", "ni votre adversaire ni votre alliée : elle applique un contrat."),
        ("Ce qu'elle ne fera pas", "citer une clause d'elle-même. Il faut la lui demander, deux fois."),
        ("Ce qui la fait raccrocher", "un refus en bloc, ou un ton indigné."),
        ("Ce qui la fait écouter", "un point accepté d'entrée, et une pièce datée derrière chaque phrase."),
    ], cols=2,
       notes="Trois situations sont offertes dans le module : le vaisselier "
             "refusé, la lecture de la clause, le compromis chiffré. Faire "
             "commencer tout le monde par la première.")

    d.regle("Une contestation sans proposition reste sur un bureau",
            "Un compromis chiffré, appuyé sur une estimation extérieure, donne à la personne d'en face quelque chose à soumettre à son réviseur.",
            precision="Vous ne demandez pas une faveur : vous fournissez une "
                      "justification toute faite pour dire oui. Et offrez une "
                      "contrepartie — elle ne coûte rien si vous n'avez plus "
                      "rien à réclamer.",
            notes="Diapositive à photographier. C'est le point le plus "
                  "souvent oublié dans les enregistrements : on argumente "
                  "très bien, puis on ne demande rien de précis.")

    d.piege('Attention',
            "« Je compte sur votre compréhension. »",
            "« Je propose huit cent cinquante dollars, contre ma renonciation. »",
            "Une conversation qui ne demande rien de précis n'obtient rien de "
            "précis. La formule de politesse ne remplace pas la demande, et "
            "l'autre n'a rien à porter à son supérieur. Terminez toujours par "
            "un chiffre, sa justification et une date.",
            notes="Faire écouter deux enregistrements d'élèves si le temps le "
                  "permet — l'un qui demande, l'autre qui espère. La "
                  "différence est frappante.")

    d.pratique('Pratique', "Production orale — deux minutes au déménageur",
               "Cette fois, ce n'est plus l'assureur : c'est l'entreprise qui "
               "a causé le dommage.", [
        ("TEMPS 1", "l'objet de l'appel en une phrase, et combien de points vous avez"),
        ("TEMPS 2", "les faits, avec une heure et un montant — et le point que vous concédez"),
        ("TEMPS 3", "ce que vous demandez, mis en relief, et ce que vous ferez ensuite"),
        ("Le ton", "posé du début à la fin. C'est la moitié de l'exercice."),
    ], cols=1,
       notes="Les élèves s'enregistrent dans le module, s'écoutent, corrigent "
             "et déposent. Rappeler qu'ils peuvent recommencer autant de fois "
             "qu'ils veulent — c'est le point de l'enregistrement.")

    d.billet(
        "Avant d'enregistrer : écris ta phrase du TEMPS 3, celle qui demande.",
        exemples=[
            "Un chiffre, sa justification, une contrepartie.",
            "Relis-la à voix haute avec la mélodie descendante de la séance A2.",
        ],
        notes="Cinq minutes avant l'enregistrement. Ceux qui n'ont pas de "
              "chiffre dans leur phrase enregistreront un appel qui ne "
              "demande rien : les reprendre maintenant, pas après.")

    return d.save(dossier)
