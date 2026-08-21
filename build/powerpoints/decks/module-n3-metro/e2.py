# -*- coding: utf-8 -*-
"""E2 · Je retiens des mots — et j'écris à quelqu'un qui arrive.
Bloc E « Je me lance » · couleur framboise · 60 min. Production écrite et bilan.
Source : section `appli` (production écrite), section `retiens`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="Je retiens des mots — et j'écris à quelqu'un qui arrive",
        chapeau="Dernière séance. On écrit à une personne qui débarque et ne "
                "connaît rien au transport collectif — c'est-à-dire à "
                "soi-même, il y a seize séances.",
        duree='60 minutes')

    d.titre(notes="Séance de clôture. Commencer en reprenant les questions difficiles "
                  "signalées aux billets de la séance E1. Rappeler au groupe où il en "
                  "était à la séance A1 : c'est ce trajet-là qu'on mesure aujourd'hui.")

    d.objectifs([
        "écrire un court message qui conseille un titre de transport ;",
        "écrire un prix correctement, avec la virgule et le signe après ;",
        "dire jusqu'à quand un titre est bon ;",
        "faire le point sur ce qu'on est capable de faire.",
    ])

    d.tableau('Analyse', "Ce que le message doit contenir",
              ["À écrire", "Exemple"],
              [["le titre conseillé, et pourquoi", "Prends un mensuel, parce que…"],
               ["son prix, en chiffres", "Ça coûte 110,00 $."],
               ["où l'acheter", "au point de service ou à la borne"]],
              cle=0,
              note="De cinq à huit phrases, pas plus.",
              notes="Diapositive à photographier. Premier des deux tableaux. Ce sont les "
                    "cinq exigences affichées dans l'activité interactive, coupées en "
                    "deux pour rester lisibles à la projection.")

    d.tableau('Analyse', "Ce que le message doit contenir — la suite",
              ["À écrire", "Exemple"],
              [["jusqu'à quand il est bon", "Il est bon jusqu'à la fin du mois."],
               ["une chose à ne pas oublier", "N'oublie pas de valider ta carte."]],
              cle=0,
              note="Attention aux petits mots : ce titre-là, du lundi au dimanche, moins cher que.",
              notes="Diapositive à photographier. La note reprend les trois points de "
                    "grammaire du module : le démonstratif, les prépositions de temps, "
                    "la comparaison. C'est sur eux que portera la correction.")

    d.regle("À qui on écrit",
            "À la personne que vous étiez il y a seize séances",
            precision="Quelqu'un arrive à Montréal la semaine prochaine et ne "
                      "connaît rien au transport collectif. Écrivez-lui ce que "
                      "vous auriez voulu qu'on vous dise. C'est le meilleur "
                      "test de ce que vous savez vraiment.",
            notes="Diapositive à photographier. Cette consigne fait toujours écrire "
                  "davantage que « rédigez un message » : elle donne un destinataire "
                  "réel et une raison d'écrire.")

    d.pratique('Écriture', "Vérifiez avant d'envoyer",
               "Relisez votre message et cochez.", [
        ("Le prix est écrit avec une virgule.", "3,75 $ et non 3.75 $"),
        ("Le signe de dollar est après le nombre.", "110 $ et non $110"),
        ("J'ai dit jusqu'à quand le titre est bon.", "jusqu'à, du… au…, pendant"),
        ("J'ai écrit « ces » et non « ses ».", "ces prix-là, sur la grille"),
        ("Après « il faut », le verbe est à sa forme de base.", "il faut valider"),
        ("Mon message fait de cinq à huit phrases.", "le compteur l'indique"),
    ], corrige=True, cols=2,
       notes="Faire cocher avant de demander la vérification à l'assistant : l'élève "
             "corrige d'abord ce qu'il peut corriger seul. C'est ce qui fait progresser, "
             "pas la rétroaction automatique.")

    d.vocabulaire('Bilan · 1 de 2', "Les mots à emporter", [
        ("une carte OPUS", "la carte de plastique, gardée des années, qu'on recharge"),
        ("un titre de transport", "ce qu'on achète et qu'on met dessus"),
        ("le point de service", "le comptoir de la station, où on vend et on explique"),
        ("le tarif réduit", "le prix plus bas — avec une carte avec photo"),
    ], notes="Révision rapide. Faire donner la définition par les élèves plutôt que la "
             "lire : c'est un bilan, pas un enseignement.")

    d.vocabulaire('Bilan · 2 de 2', "Les gestes à ne pas oublier", [
        ("recharger sa carte", "avant la fin du mois, au comptoir ou à la borne"),
        ("valider son titre", "en montant, chaque fois — sinon, amende"),
        ("une correspondance", "cent vingt minutes pour finir son trajet"),
        ("une place réservée", "en avant : on se lève sans qu'on demande"),
    ], notes="Les quatre gestes qui servent tous les jours. « Valider » est celui dont "
             "l'oubli coûte le plus cher : le répéter une dernière fois.")

    d.pratique('Autoévaluation', "Qu'est-ce que je suis capable de faire ?",
               "Pour chaque énoncé : pas encore, un peu, ou oui.", [
        ("Je comprends les quatre titres principaux.", "passage, dix passages, hebdo, mensuel"),
        ("Je peux dire et écrire un prix.", "trois dollars soixante-quinze, 3,75 $"),
        ("Je peux demander le prix d'un titre au comptoir.", "combien coûte…"),
        ("Je peux demander si j'ai droit au tarif réduit.", "est-ce que…"),
        ("J'ose faire répéter un chiffre.", "pardon, pouvez-vous répéter"),
        ("Je peux lire la grille : la ligne, la colonne, le prix.", "en croix"),
    ], corrige=True, cols=2,
       notes="L'autoévaluation complète est dans l'activité interactive, avec dix "
             "énoncés. Celle-ci en projette six pour la discussion de groupe. Ne pas "
             "commenter les réponses de qui que ce soit à voix haute.")

    d.billet(
        "Écrivez une chose que vous savez faire aujourd'hui et que vous ne saviez pas faire il y a un mois.",
        exemples=[
            "Avant, je ___ .",
            "Maintenant, je peux ___ .",
        ],
        notes="Dernier billet du module. Le lire soi-même avant de le rendre : c'est là "
              "qu'on voit ce que les seize séances ont réellement produit, et ce qu'il "
              "faudra reprendre au module suivant.")

    return d.save(dossier)
