# -*- coding: utf-8 -*-
"""B3 · Chaque envoi sert à quelque chose.
Bloc B « Défi 1 · Demander avant de choisir » · couleur teal · 75 min.
Source : exercice `t1envois`, banc `FC_CARDS` (services).
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-poste/images/')


def build(dossier):
    d = Deck(
        code='B3', section='teal',
        titre='Chaque envoi sert à quelque chose',
        chapeau="Six façons d'envoyer, six besoins différents. On ne choisit "
                "pas le plus rapide ni le moins cher : on choisit celui qui "
                "fait ce dont on a besoin.",
        duree='75 minutes')

    d.titre(notes="Séance d'écoute et de compréhension. Elle répond à la question que "
                  "les élèves posent toujours après B1 : « Et les autres services, "
                  "c'est quoi ? »")

    d.objectifs([
        "distinguer six services de la poste ;",
        "dire à quoi chacun sert, en une phrase ;",
        "choisir le bon service pour une situation donnée ;",
        "comprendre ce qu'est le repérage.",
    ])

    d.declencheur(
        'Observation', "Pourquoi cette boîte-là est fermée avec du ruban ?",
        image=IMG + 'ruban-boite.jpg',
        pistes=[
            "Est-ce qu'on peut envoyer une boîte ouverte ?",
            "Qu'est-ce qui est écrit dessus, d'habitude ?",
            "Comment savoir si elle est bien rendue ?",
            "Est-ce qu'on peut la suivre pendant le voyage ?",
        ],
        notes="Amener le mot « repérage » par la dernière piste. C'est le service que "
              "les élèves connaissent le mieux sans savoir le nommer en français : "
              "beaucoup suivent déjà des colis sur leur téléphone.")

    d.vocabulaire('Les six envois', "À quoi sert chacun ?", [
        ("Le colis standard", "Envoyer une boîte sans être pressé, au prix le plus bas."),
        ("L'Xpresspost", "Faire arriver la boîte en un ou deux jours ouvrables."),
        ("Le courrier recommandé", "Obtenir la signature de la personne qui reçoit."),
        ("Le mandat-poste", "Envoyer de l'argent sans mettre du comptant dans l'enveloppe."),
        ("Un timbre sur une enveloppe", "Envoyer une simple lettre, sans passer au comptoir."),
        ("Le repérage", "Savoir sur Internet où est rendue la boîte."),
    ], notes="C'est l'exercice `t1envois` du module, donné ici en tableau. Faire lire "
             "chaque ligne, puis masquer la colonne de droite et interroger.")

    d.regle("Le service qui protège vos papiers importants",
            "le courrier recommandé",
            precision="La personne qui reçoit doit signer. Vous obtenez la preuve "
                      "qu'elle a bien reçu l'envoi, avec la date. C'est ce qu'on "
                      "demande pour un bail, un contrat, un avis au propriétaire, "
                      "un document du gouvernement.",
            notes="Diapo à photographier. Beaucoup d'élèves auront à envoyer un "
                  "document important cette année : c'est l'information la plus "
                  "utile de la séance, au-delà du vocabulaire.")

    d.regle("Le service qui remplace le comptant",
            "le mandat-poste",
            precision="C'est un papier acheté à la poste qui vaut de l'argent. On "
                      "l'envoie dans une enveloppe : s'il se perd, il ne peut pas "
                      "être encaissé par n'importe qui. On ne met jamais de billets "
                      "dans une enveloppe.",
            notes="Diapo à photographier. Insister sur la dernière phrase : c'est une "
                  "erreur fréquente et coûteuse chez les personnes nouvellement "
                  "arrivées, qui envoient de l'argent à leur famille.")

    d.tableau('Analyse', "Le même besoin, deux réponses possibles",
              ['Ce que vous voulez', 'Le bon service'],
              [["Que ça arrive vite", "l'Xpresspost, plus cher"],
               ["Que ça coûte le moins possible", "le colis standard"],
               ["Une preuve que c'est reçu", "le courrier recommandé"],
               ["Envoyer de l'argent", "le mandat-poste"],
               ["Savoir où c'est rendu", "le repérage, compris partout"]],
              cle=1,
              note="Le repérage est le seul de la liste qui ne se paie pas : il vient avec le colis.",
              notes="Diapo à photographier. Faire dire au groupe, pour chaque ligne, "
                    "une situation vraie de leur vie.")

    d.pratique('Compréhension', "Quel service choisir ?",
               "Lisez la situation, puis nommez le service.", [
        ("Vous envoyez un cadeau qui doit arriver dans deux semaines.", "le colis standard"),
        ("Vous devez envoyer un contrat signé à un propriétaire.", "le courrier recommandé"),
        ("Vous envoyez deux cents dollars à votre mère.", "le mandat-poste"),
        ("Votre soeur se marie samedi et le cadeau part mercredi.", "l'Xpresspost"),
        ("Vous envoyez une carte d'anniversaire.", "un timbre sur une enveloppe"),
        ("Vous voulez savoir si la boîte est arrivée à Calgary.", "le repérage, sur Internet"),
    ], corrige=True,
       notes="Faire justifier chaque réponse : c'est le raisonnement qui compte, pas le "
             "mot. Deux services peuvent convenir à la quatrième situation ; accepter "
             "les deux si l'élève explique le délai.")

    d.pratique('À l\'oral', "Demandez le service",
               "Deux par deux : employez une formule de la séance A4.", [
        ("Vous voulez envoyer un contrat avec signature.", "Je voudrais l'envoyer par courrier recommandé, s'il vous plaît."),
        ("Vous voulez acheter un mandat-poste.", "J'aimerais acheter un mandat-poste, s'il vous plaît."),
        ("Vous voulez savoir si le repérage est compris.", "Est-ce que le repérage est compris ?"),
        ("Vous voulez comparer les deux vitesses.", "Et pour l'Xpresspost, ça coûte combien ?"),
    ], corrige=True,
       notes="Cinq minutes par rôle. C'est la première fois que les élèves enchaînent "
             "une formule polie et un nom de service : c'est exactement la tâche du "
             "jeu de rôle de la séance E1.")

    d.billet(
        "Écrivez un envoi que vous devrez faire, et le service qui convient.",
        exemples=[
            "Des papiers, un cadeau, de l'argent, une lettre ?",
            "Pourquoi ce service-là plutôt qu'un autre ?",
        ],
        notes="Ramasser. Les billets servent d'exemples réels pour la séance B4, où on "
              "compare les prix.")

    return d.save(dossier)
