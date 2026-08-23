# -*- coding: utf-8 -*-
"""B2 · Lire l'avis, ligne par ligne
Bloc B « Défi 1 · L'avis du propriétaire » · couleur ambre · compréhension
écrite · 75 min.
Source : exercice `t1avis` (type `texte`, onze passages cliquables) et sa
mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre="Lire l'avis, ligne par ligne",
        chapeau="Un avis ne cherche pas à convaincre : il informe et il "
                "déclenche un compte à rebours. On ne le lit pas pour le "
                "ton, on le lit pour trois choses.",
        duree='75 minutes')

    d.titre(notes="Séance de compréhension écrite. Distribuer l'avis et la fiche sur "
                  "papier avant d'ouvrir le module : l'exercice `t1avis` se fait ensuite "
                  "à l'écran, et la lecture sur papier prépare le repérage.")

    d.objectifs([
        "trouver dans un avis la date, le montant et le délai ;",
        "repérer le paragraphe « autre condition », que tout le monde saute ;",
        "dire ce qui arrive après un refus, et dans quel délai ;",
        "expliquer pourquoi la date de réception est la seule qui compte.",
    ], notes="Les quatre objectifs sont des repérages, pas des compréhensions fines. "
             "C'est voulu : au niveau 7, l'enjeu est de tenir le fil d'un document long.")

    d.declencheur(
        'Observation', "Trois choses à trouver, et dans cet ordre",
        pistes=[
            "La date où vous avez reçu le papier : où la note-t-on ?",
            "Le montant proposé : de combien est la hausse en pourcentage ?",
            "Le délai : combien de temps, à partir de quand ?",
            "Qu'est-ce qui reste, une fois ces trois choses relevées ?",
        ],
        notes="La dernière question est rhétorique : il reste du décor administratif. "
              "Le dire soulage le groupe, qui croit devoir tout comprendre.")

    d.tableau('Analyse', "Les deux documents du défi",
              ['Le document', 'Ce quon y cherche'],
              [["L'avis de modification", "la date, le montant, l'autre condition, le délai"],
               ["Le paragraphe 3 de l'avis", "la phrase qui dit que le silence vaut acceptation"],
               ["La fiche de renseignements", "quand l'avis doit être donné : de trois à six mois"],
               ["La section « si le locataire refuse »", "le mois dont dispose le locateur pour aller au Tribunal"],
               ["L'encadré « à retenir »", "ce que l'auteur juge le plus souvent oublié"]],
              cle=0,
              notes="Diapositive à photographier. C'est le plan de lecture de "
                    "l'exercice `t1avis` : les onze questions suivent cet ordre-là.")

    d.regle("La date de réception, et rien d'autre",
            "Le délai court à partir du jour où l'avis vous parvient.",
            precision="Pas du jour où il a été écrit, pas du jour où vous l'avez lu "
                      "attentivement : du jour où il est arrivé chez vous. C'est la "
                      "seule date que vous pourrez prouver plus tard, et elle ne "
                      "s'écrit nulle part toute seule. Une photo de l'enveloppe le soir "
                      "même coûte cinq secondes.",
            notes="Diapositive à photographier. Faire calculer la date limite de "
                  "l'exemple au tableau, à voix haute : reçu le 12 février, réponse au "
                  "plus tard le 12 mars.")

    d.pratique('Compréhension écrite', "Où est la réponse dans le document ?",
               "Pour chaque question, retrouvez le passage exact.", [
        ("Quel jour l'avis a-t-il été remis ?", "« Remis en main propre le 12 février »"),
        ("Quelle autre condition que le loyer change ?", "le stationnement, 25 $ de plus"),
        ("Que se passe-t-il si la locataire ne répond pas ?", "« réputé avoir accepté »"),
        ("Quand un tel avis doit-il être donné ?", "de trois à six mois avant la fin du bail"),
        ("Après un refus, que doit faire le locateur ?", "s'adresser au Tribunal dans le mois"),
        ("Et s'il ne fait rien ?", "le bail est reconduit aux mêmes conditions"),
    ], corrige=True,
       notes="Six des onze questions de `t1avis`. À l'écran, l'élève clique dans le "
             "texte ; ici, on demande la phrase à voix haute. Les deux gestes sont le "
             "même travail.")

    d.piege('Compréhension écrite',
            "Je n'ai pas répondu, donc je n'ai rien accepté.",
            "Je n'ai pas répondu, donc j'ai accepté.",
            "C'est la particularité de cet avis, et elle prend tout le monde. Dans la "
            "plupart des démarches administratives, ne rien faire veut dire refuser. "
            "Ici, un mois passe et la hausse est acceptée. Un refus, à l'inverse, ne "
            "met fin à rien et ne met personne dehors.",
            notes="Demander qui, dans le groupe, a déjà laissé passer un délai sans le "
                  "savoir. Presque toutes les mains se lèvent. Dédramatiser, puis "
                  "revenir à la date limite écrite au tableau.")

    d.billet(
        "Écris la phrase de refus que tu enverrais, en une seule ligne.",
        exemples=[
            "« Je refuse la modification proposée dans votre avis du 12 février. »",
            "Rien d'autre n'est obligatoire.",
        ],
        notes="Deux minutes. Faire remarquer qu'un refus tient en une ligne : c'est "
              "l'écrit le plus court et le plus utile du module.")

    return d.save(dossier)
