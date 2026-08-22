# -*- coding: utf-8 -*-
"""C1 · On reporte ou on annule ?
Bloc C « Défi 2 · La décision, et pourquoi » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t2a`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="On reporte ou on annule ?",
        chapeau="Marisol a compris le bulletin. Reste le plus difficile : "
                "trente personnes attendent, et ce n'est pas la météo qui "
                "décide entre reporter et annuler — c'est le calendrier.",
        duree='75 minutes')

    d.titre(notes="Première séance du Défi 2. Ouvrir en posant la question du titre au "
                  "groupe, avant toute écoute : « quelle différence entre reporter et "
                  "annuler ? ». La plupart répondront par le degré de gravité. C'est "
                  "faux, et c'est le point de départ de la séance.")

    d.objectifs([
        "distinguer maintenir, reporter et annuler, et dire ce qui les sépare ;",
        "reconnaître la question qui tranche : existe-t-il une date de rechange ?",
        "comprendre qu'un maintien s'annonce, lui aussi ;",
        "savoir qu'une décision sans raison se fait discuter toute la semaine.",
    ], notes="Le troisième objectif est celui qu'on saute toujours : sans message, la "
             "moitié du groupe reste chez elle « au cas où ». Un maintien se dit, comme "
             "les deux autres décisions.")

    d.declencheur(
        'Question', "La promenade sera-t-elle encore là dans quinze jours ?",
        pistes=[
            "Si oui, que faut-il faire de la sortie de samedi ?",
            "Et si c'était un spectacle qui ne passe qu'une fois ?",
            "Et si l'autobus était déjà payé et non remboursable ?",
            "Qu'est-ce qui décide, dans les trois cas : la météo, ou autre chose ?",
        ],
        notes="La quatrième piste est la réponse de la séance : c'est le calendrier et "
              "l'argent qui décident entre reporter et annuler, pas l'intensité de la "
              "tempête. Laisser le groupe y arriver seul.")

    d.dialogue('Dialogue · 1 de 3', "Ce n'est pas la même décision", [
        ("MARISOL", "Je ne sais pas si on reporte ou si on annule.", True),
        ("RÉJEAN", "Ce n'est pas la même décision, et ce n'est pas le même "
                   "message. Reporter, c'est déplacer la sortie à une autre "
                   "date. Annuler, c'est dire qu'elle n'aura pas lieu du "
                   "tout.", True),
        ("MARISOL", "Comme les trottoirs seront glacés toute la journée, je "
                    "ne veux pas de la sortie samedi. Ça, c'est clair.", False),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire remarquer la construction de Marisol : « Comme… , je ne veux pas… ». "
             "C'est le connecteur de C3, employé naturellement. Le noter au tableau et y "
             "revenir dans deux séances.")

    d.dialogue('Dialogue · 2 de 3', "La question qui tranche", [
        ("RÉJEAN", "La vraie question, c'est : est-ce que la promenade de la "
                   "mer sera encore là dans quinze jours ?", True),
        ("MARISOL", "Bien sûr qu'elle sera encore là.", True),
        ("RÉJEAN", "Donc on reporte. On annule seulement quand il n'y a pas "
                   "de date de rechange : un spectacle qui passe une fois, un "
                   "autobus déjà payé, un guide qui ne revient pas.", False),
    ], notes="Trois exemples d'annulation, tous concrets et tous non météorologiques. "
             "Demander au groupe d'en trouver un quatrième : les meilleurs viennent "
             "toujours de leur propre vie.")

    d.dialogue('Dialogue · 3 de 3', "Jamais une décision sans sa raison", [
        ("RÉJEAN", "N'écris jamais une décision sans sa raison. Les gens "
                   "acceptent presque tout quand ils comprennent pourquoi.", True),
        ("MARISOL", "Puisqu'un avertissement de pluie verglaçante est en "
                    "vigueur et que les trottoirs resteront glacés, la sortie "
                    "est reportée.", True),
        ("RÉJEAN", "Voilà. La raison d'abord, la décision ensuite. Ou "
                   "l'inverse, mais les deux dans la même phrase.", False),
    ], notes="« Les deux dans la même phrase » est la consigne d'écriture de tout le bloc "
             "C. L'écrire au tableau et l'y laisser jusqu'à la fin du module.")

    d.regle("Trois décisions, une seule question",
            "Est-ce que cette activité existera encore dans quinze jours ? "
            "Si oui, on reporte. Si non, on annule.",
            precision="Et si l'avis ne touche pas le créneau, on maintient — mais "
                      "on le dit, sinon la moitié du groupe reste chez elle.",
            notes="Diapositive à photographier. Cette question à une ligne règle presque "
                  "tous les cas, et elle ne demande aucune connaissance de la météo.")

    d.tableau('Trois décisions', "Ce que chacune annonce",
              ['Décision', 'Quand', "Ce qu'il faut dire en plus"],
              [["On maintient", "L'avis ne touche pas le créneau", "L'heure et le lieu, pour rassurer"],
               ["On reporte", "Une date de rechange existe", "La nouvelle date, l'heure, le lieu"],
               ["On annule", "Aucune date de rechange", "La raison, et ce qui arrive à l'argent"],
               ["On déplace", "L'heure ou le lieu suffit à régler", "Ce qui change exactement"]],
              note="La quatrième est une forme de maintien : l'activité a lieu, autrement.",
              notes="La ligne « on déplace » est celle qu'on oublie et souvent la "
                    "meilleure : marcher au centre commercial, partir à neuf heures au "
                    "lieu de quatorze. Y revenir en C2.")

    d.piege("Dire « annulé » quand on veut dire « reporté »",
            "La sortie est annulée. (Alors qu'elle est déplacée au 22.)",
            "La sortie est reportée au samedi 22, même heure, même endroit.",
            "Annulé veut dire qu'elle n'aura pas lieu, point. Vingt personnes "
            "ne se réinscriront pas, et trois seront fâchées d'apprendre qu'elle "
            "a eu lieu sans elles.",
            notes="Ce n'est pas une nuance de vocabulaire : c'est une différence de "
                  "conséquences. Le dire ainsi, avec le chiffre — vingt personnes — "
                  "plutôt qu'en termes de justesse de langue.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après l'appel de Marisol à Réjean.", [
        ("Reporter et annuler veulent dire la même chose.", "faux — l'un déplace, l'autre ferme"),
        ("Marisol appelle Réjean avant d'écrire au groupe.", "vrai"),
        ("La sortie est reportée au samedi 22.", "vrai"),
        ("On peut annoncer une décision sans donner la raison.", "faux — elle se discutera toute la semaine"),
        ("Marisol écrira à tout le monde, sans téléphoner à personne.", "faux — huit appels d'abord"),
        ("Réjean conseille de commencer par ceux qui n'ont pas de courriel.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. L'avant-dernière "
             "amène une discussion utile : à qui téléphone-t-on, et pourquoi un appel "
             "vaut trois courriels quand quelqu'un a soixante-quinze ans.")

    d.billet(
        "Reprenez la situation que vous avez notée en A1. Fallait-il maintenir, reporter ou annuler ?",
        exemples=[
            "Écrivez la décision, puis la question qui l'a tranchée.",
            "Y avait-il une date de rechange ? Dites laquelle.",
        ],
        notes="Ramasser les billets et en lire trois à voix haute, anonymement, à "
              "l'ouverture de C2. Les cas réels du groupe valent mieux que les huit cas "
              "inventés de l'exercice.")

    return d.save(dossier)
