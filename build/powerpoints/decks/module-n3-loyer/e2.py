# -*- coding: utf-8 -*-
"""E2 · Je retiens des mots — et j'écris à ma famille.
Bloc E « Je me lance » · couleur framboise · 60 min. Production écrite et bilan.
Source : section `appli` (production écrite), section `retiens`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="Je retiens des mots — et j'écris à ma famille",
        chapeau="Dernière séance. On écrit à quelqu'un qui n'était pas là "
                "pour décrire un logement qu'on vient de visiter — et c'est "
                "le meilleur test de ce qu'on a vraiment retenu.",
        duree='60 minutes')

    d.titre(notes="Séance de clôture. Commencer en reprenant les questions difficiles "
                  "signalées aux billets de la séance E1. Rappeler au groupe où il en "
                  "était à la séance A1 : c'est ce trajet-là qu'on mesure aujourd'hui.")

    d.objectifs([
        "écrire un court message qui décrit un logement visité ;",
        "écrire un loyer correctement, avec le signe après le nombre ;",
        "dire où se trouve une pièce et ce qui manque ;",
        "faire le point sur ce qu'on est capable de faire.",
    ])

    d.tableau('Analyse', "Ce que le message doit contenir",
              ["À écrire", "Exemple"],
              [["le nombre de pièces", "J'ai visité un 4 ½."],
               ["le loyer, en chiffres", "Le loyer est de 1 150 $."],
               ["ce qui est compris", "C'est chauffé et éclairé."]],
              cle=0,
              note="De cinq à huit phrases, pas plus.",
              notes="Diapositive à photographier. Premier des deux tableaux. Ce sont les "
                    "six exigences affichées dans l'activité interactive, coupées en "
                    "deux pour rester lisibles à la projection.")

    d.tableau('Analyse', "Ce que le message doit contenir — la suite",
              ["À écrire", "Exemple"],
              [["où se trouve une pièce", "Les chambres sont au fond du couloir."],
               ["une chose qui manque", "Il n'y a pas de stationnement."],
               ["ce que vous allez faire", "Je vais rappeler demain."]],
              cle=0,
              note="Attention : une cuisine chauffée, il n'y a pas de, il n'y a pas d'.",
              notes="Diapositive à photographier. La note reprend les trois points de "
                    "grammaire du module : l'accord de l'adjectif, la négation, le futur "
                    "proche. C'est sur eux que portera la correction.")

    d.regle("À qui on écrit",
            "À quelqu'un qui n'a pas vu le logement",
            precision="Une personne de votre famille vous demande comment "
                      "c'était. Elle n'a rien vu : chaque chose que vous ne "
                      "dites pas, elle ne l'aura pas. Écrivez-lui ce que vous "
                      "auriez voulu qu'on vous dise.",
            notes="Diapositive à photographier. Cette consigne fait toujours écrire "
                  "davantage que « rédigez un message » : elle donne un destinataire "
                  "réel et une raison d'écrire.")

    d.pratique('Écriture', "Vérifiez avant d'envoyer",
               "Relisez votre message et cochez.", [
        ("Le signe de dollar est après le nombre.", "1 150 $ et non $1150"),
        ("Chaque pièce a son article.", "une cuisine, un balcon"),
        ("Les adjectifs sont accordés.", "la cuisine est chauffée"),
        ("J'ai dit où se trouve une pièce.", "au fond du, à côté de, au"),
        ("J'ai employé « il n'y a pas de ».", "et « d' » devant une voyelle"),
        ("Mon message fait de cinq à huit phrases.", "le compteur l'indique"),
    ], corrige=True, cols=2,
       notes="Faire cocher avant de demander la vérification à l'assistant : l'élève "
             "corrige d'abord ce qu'il peut corriger seul. C'est ce qui fait progresser, "
             "pas la rétroaction automatique.")

    d.vocabulaire('Bilan · 1 de 2', "Les mots à emporter", [
        ("un loyer", "l'argent qu'on donne chaque mois au propriétaire"),
        ("chauffé", "le chauffage est déjà payé dans le loyer"),
        ("l'électricité comprise", "le compte d'électricité est dans le loyer"),
        ("le bail", "le papier qu'on signe, douze mois d'habitude"),
    ], notes="Révision rapide. Faire donner la définition par les élèves plutôt que la "
             "lire : c'est un bilan, pas un enseignement.")

    d.vocabulaire('Bilan · 2 de 2', "Les phrases à ne pas oublier", [
        ("Je vous appelle pour l'annonce.", "la première phrase de tout appel"),
        ("Est-ce que le chauffage est compris ?", "la question du vrai prix"),
        ("Est-ce que je pourrais le visiter ?", "le but de l'appel"),
        ("Je vais y penser et je vous rappelle.", "ne jamais signer sur place"),
    ], notes="Les quatre phrases qui servent vraiment. La dernière est une phrase de "
             "protection : la répéter une dernière fois, tout le groupe ensemble.")

    d.tableau('Analyse', "Trois choses à ne pas oublier au Québec",
              ["La règle", "Ce que ça veut dire"],
              [["le bail dure douze mois", "du 1er juillet au 30 juin"],
               ["il se renouvelle tout seul", "personne ne vous met dehors"],
               ["le dépôt de garantie est interdit", "seulement le premier mois"]],
              cle=0,
              note="On peut toujours dire : je vais y penser et je vous rappelle.",
              notes="Diapositive à photographier. Dernier rappel des droits, vus à la "
                    "séance D2. Ce sont les trois choses qui restent utiles longtemps "
                    "après le module.")

    d.pratique('Autoévaluation', "Qu'est-ce que je suis capable de faire ?",
               "Pour chaque énoncé : pas encore, un peu, ou oui.", [
        ("Je comprends une petite annonce en abrégé.", "4 ½, ch. et écl., s.-sol"),
        ("Je sais ce que veut dire chauffé et éclairé.", "compris dans le loyer"),
        ("Je peux téléphoner et dire pourquoi j'appelle.", "je vous appelle pour l'annonce"),
        ("Je peux poser mes trois questions.", "l'argent, la place, la date"),
        ("Je peux dire où se trouve une pièce.", "au fond du couloir"),
        ("Je sais qu'un dépôt de garantie est interdit.", "seulement le premier mois"),
    ], corrige=True, cols=2,
       notes="L'autoévaluation complète est dans l'activité interactive, avec onze "
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
