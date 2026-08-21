# -*- coding: utf-8 -*-
"""B1 · « Le samedi 7 juin, de midi à quatre heures »
Bloc B « Défi 1 · L'invitation » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t1a`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="« Le samedi 7 juin, de midi à quatre heures »",
        chapeau="Marisol a réfléchi. Avant de répondre, elle pose cinq "
                "questions : quand, où, à quelle heure, quoi apporter, et "
                "ce qui arrive s'il pleut. Ce sont les cinq questions qui "
                "manquent presque toujours.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 1. Demander d'abord au groupe : quand on vous invite "
                  "quelque part, qu'est-ce que vous voulez savoir avant de dire oui ? "
                  "Noter les réponses au tableau. Les cinq questions de la séance en "
                  "sortent presque toujours, sauf la dernière — celle de la pluie.")

    d.objectifs([
        "comprendre une invitation donnée oralement, avec ses détails ;",
        "poser les cinq questions qui manquent avant de répondre ;",
        "repérer une date, une heure et un lieu dans un échange rapide ;",
        "comprendre pourquoi on demande ce qu'il faut apporter.",
    ], notes="Le troisième objectif est une compétence d'écoute pure : on entend « le "
             "samedi 7 juin, de midi à quatre heures » une seule fois. Faire écouter deux "
             "fois, pas plus, pour que l'exercice reste réaliste.")

    d.dialogue('Dialogue · 1 de 3', "Quand, où, et s'il pleut", [
        ("MARISOL", "Monsieur Deslauriers ! J'ai réfléchi à votre fête. "
                    "D'abord, je voudrais savoir quand c'est exactement.", True),
        ("RÉJEAN", "Le samedi 7 juin, de midi à quatre heures. Dans la "
                   "ruelle, derrière le hangar.", True),
        ("MARISOL", "Et s'il pleut ?", True),
        ("RÉJEAN", "On reporte au dimanche. Je glisse un papier sous chaque "
                   "porte le matin même.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire noter au tableau la date, l'heure et le lieu au fur et à mesure de "
             "l'écoute : c'est exactement le geste que l'élève devra faire au défi 2 avec "
             "le répondeur. La question « et s'il pleut ? » surprend souvent : elle est "
             "pourtant si banale qu'elle ne dérange personne.")

    d.dialogue('Dialogue · 2 de 3', "Un plat pour combien de personnes ?", [
        ("MARISOL", "Est-ce qu'il faut apporter quelque chose ?", True),
        ("RÉJEAN", "Un plat à partager, et votre chaise. Les tables, on les a.", True),
        ("MARISOL", "Un plat pour combien de personnes ?", True),
        ("RÉJEAN", "Faites-en pour six ou sept. On était vingt-deux l'année "
                   "passée.", True),
    ], notes="La deuxième question de Marisol est celle que personne ne pense à poser. Un "
             "plat pour six ne se prépare pas comme un plat pour vingt : la question est "
             "pratique, pas polie.")

    d.dialogue('Dialogue · 3 de 3', "Un oui, et une raison vraie", [
        ("MARISOL", "Alors c'est oui. J'accepte avec plaisir, parce que ça "
                    "fait trois ans que je monte cet escalier sans connaître "
                    "personne.", True),
        ("RÉJEAN", "Ça me fait plaisir de vous entendre dire ça.", True),
        ("MARISOL", "Je vais faire des empanadas. Ma mère m'a montré, et je "
                    "n'en ai jamais fait pour vingt personnes.", False),
    ], notes="Faire relever la structure de l'acceptation : le oui, le plaisir, la raison, "
             "puis ce qu'elle apportera. C'est le modèle travaillé en B2. Faire remarquer "
             "aussi que la raison est vraie et un peu fragile : c'est ce qui la rend "
             "touchante, et Réjean y répond.")

    d.regle("Cinq questions avant de répondre",
            "Quand, à quelle heure, où, quoi apporter, et ce qui arrive "
            "s'il pleut.",
            precision="Personne ne trouve ces questions impolies. Celui qui invite "
                      "a rarement pensé à tout dire, et il est content qu'on lui "
                      "demande : ça veut dire qu'on viendra.",
            notes="Diapositive à photographier. Les cinq questions se retrouvent dans le "
                  "jeu de rôle de la séance E1 : l'assistant ne donne aucune de ces "
                  "informations tant qu'on ne les demande pas.")

    d.tableau("Ce qu'on retient", "Les cinq renseignements de la fête",
              ['La question', 'La réponse de Réjean'],
              [["Quel jour ?", "Le samedi 7 juin"],
               ["À quelle heure ?", "De midi à quatre heures"],
               ["Où ?", "Dans la ruelle, derrière le hangar"],
               ["Quoi apporter ?", "Un plat à partager et sa chaise"],
               ["Et s'il pleut ?", "Reporté au dimanche, un papier sous la porte"]],
              cle=1,
              notes="Faire remplir la colonne de droite de mémoire, sans réécouter. Ceux "
                    "qui ont noté pendant l'écoute réussissent ; les autres comprennent "
                    "pourquoi on note.")

    d.cartes("Poser la question", "Quatre formules, de la plus simple à la plus soignée", [
        ("La plus courte",
         "C'est quel jour ? Il faut apporter quelque chose ?"),
        ("Avec « est-ce que »",
         "Est-ce qu'il faut apporter quelque chose ?"),
        ("En annonçant la question",
         "Je voudrais savoir quand c'est exactement."),
        ("La question qui rassure",
         "Et s'il pleut, qu'est-ce qui arrive ?"),
    ], notes="Les quatre sont correctes. La troisième est celle du niveau 5 : poser une "
             "question à l'intérieur d'une phrase demande de renoncer à l'inversion — "
             "« quand c'est », et non « quand est-ce ».")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("La fête a lieu le samedi 7 juin.", "vrai"),
        ("Elle dure de midi à quatre heures.", "vrai"),
        ("S'il pleut, la fête est annulée.", "faux — elle est reportée au dimanche"),
        ("Il faut apporter un plat et sa chaise.", "vrai"),
        ("Les tables sont fournies.", "vrai"),
        ("Marisol doit faire un plat pour vingt personnes.", "faux — pour six ou sept"),
        ("Madame Faye refuse parce qu'elle travaille.", "vrai"),
    ], corrige=True,
       notes="Exercice t1a de l'activité. La sixième est celle qui piège : on entend "
             "« vingt-deux » dans le dialogue, mais c'est le nombre d'invités, pas la "
             "taille du plat. Bel exemple d'écoute qui demande de comprendre, pas "
             "seulement d'entendre.")

    d.billet(
        "Vous êtes invité à une fête chez un voisin. Écrivez vos trois questions.",
        exemples=[
            "Trois questions différentes, chacune sur une ligne.",
            "Relisez-les : est-ce qu'on peut y répondre par oui ou par non ?",
        ],
        notes="Ramasser. Les questions serviront de matière au jeu de rôle de E1 : les "
              "meilleures peuvent être affichées avant de commencer.")

    return d.save(dossier)
