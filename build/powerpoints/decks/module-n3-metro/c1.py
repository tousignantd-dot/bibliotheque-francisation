# -*- coding: utf-8 -*-
"""C1 · Je voudrais un mensuel, s'il vous plaît.
Bloc C « Défi 2 · Demander au guichet » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t2vf`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Je voudrais un mensuel, s'il vous plaît",
        chapeau="Cette fois, c'est l'élève qui parle. Il sait ce qu'il veut, "
                "et il lui reste quatre questions à poser avant de sortir "
                "son argent.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 2, qui est la compétence de production orale du "
                  "programme. Le bloc B était de l'écoute ; ici, l'élève prend la "
                  "parole. Le dire explicitement au groupe : la difficulté change de "
                  "nature.")

    d.objectifs([
        "entrer en conversation au comptoir avec une formule polie ;",
        "demander si on a droit au tarif réduit ;",
        "comprendre ce qu'il faut apporter pour une carte avec photo ;",
        "répéter ce qu'on a compris avant de payer.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qu'on dit en arrivant devant le comptoir ?",
        pistes=[
            "Est-ce qu'on dit « je veux » ou autre chose ?",
            "Est-ce qu'on salue d'abord ?",
            "Que fait-on si on ne connaît pas le nom du titre ?",
            "Combien de questions peut-on poser sans déranger ?",
        ],
        notes="Laisser le groupe proposer des formules, même maladroites, et les écrire "
              "au tableau sans corriger. On y reviendra en fin de séance : ce qui "
              "manque presque toujours, c'est « je voudrais » et « s'il vous plaît ».")

    d.dialogue('Dialogue · 1 de 3', "Vous avez votre carte ?", [
        ("ROSARIO", "Bonjour. Je voudrais un titre mensuel, s'il vous plaît.", True),
        ("LORRAINE", "Bien sûr. Vous avez votre carte OPUS avec vous ?", True),
        ("ROSARIO", "La voici. Est-ce que je dois acheter une nouvelle carte ?", True),
        ("LORRAINE", "Non. Je recharge celle-là. Le titre s'ajoute dessus.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Quatre répliques, et déjà toute la structure : on salue, on demande "
             "poliment, on donne sa carte, on pose une question. Faire remarquer que "
             "Rosario n'attend pas qu'on lui dise quoi faire : elle demande.")

    d.dialogue('Dialogue · 2 de 3', "Ma fille a quinze ans", [
        ("ROSARIO", "Est-ce que ma fille peut avoir le tarif réduit ? Elle a quinze ans.", True),
        ("LORRAINE", "Oui, de six à dix-sept ans. Mais il lui faut une carte avec photo.", True),
        ("ROSARIO", "Où est-ce qu'on fait la photo ?", True),
        ("LORRAINE", "Ici même. Apportez une preuve de son âge et venez avec elle.", True),
        ("ROSARIO", "Et ma mère ? Elle a soixante-huit ans.", True),
        ("LORRAINE", "Soixante-cinq ans et plus, c'est aussi le tarif réduit.", True),
    ], notes="Rosario pose trois questions à la suite, une à la fois, et obtient trois "
             "renseignements que personne ne lui aurait donnés spontanément. C'est le "
             "point de la séance : au comptoir, on ne reçoit que ce qu'on demande.")

    d.dialogue('Dialogue · 3 de 3', "Je répète pour être sûre", [
        ("LORRAINE", "Cent dix dollars. Vous payez comptant ou par carte ?", True),
        ("ROSARIO", "Par carte. Est-ce que je peux répéter pour être sûre ?", True),
        ("LORRAINE", "Allez-y.", True),
        ("ROSARIO", "Un mensuel, zone A, cent dix dollars, bon jusqu'à la fin du mois. C'est ça ?", True),
        ("LORRAINE", "C'est exactement ça. N'oubliez pas de valider votre carte au tourniquet.", True),
    ], notes="La reformulation finale est ce qu'on demandera à l'oral en E1. Quatre "
             "éléments : le titre, la zone, le prix, la durée. La faire répéter par "
             "plusieurs élèves, en changeant le titre à chaque fois.")

    d.regle("La formule d'entrée",
            "« Bonjour. Je voudrais un titre mensuel, s'il vous plaît. »",
            precision="Trois choses en une phrase : on salue, on demande "
                      "poliment, on nomme ce qu'on veut. « Je veux » n'est pas "
                      "faux, mais sonne sec. « Je voudrais » demande la même "
                      "chose et ouvre bien mieux la conversation.",
            notes="Diapositive à photographier. Faire dire la phrase par tout le groupe, "
                  "puis individuellement, avec la salutation. Beaucoup d'élèves oublient "
                  "de saluer, et c'est ce qui se remarque le plus au Québec.")

    d.tableau('Analyse', "Les quatre questions de Rosario",
              ["Ce qu'elle demande", "La phrase"],
              [["sa carte", "Est-ce que je dois acheter une nouvelle carte ?"],
               ["le tarif réduit", "Est-ce que ma fille peut avoir le tarif réduit ?"],
               ["la carte avec photo", "Où est-ce qu'on fait la photo ?"],
               ["vérifier", "Est-ce que je peux répéter pour être sûre ?"]],
              cle=0,
              note="Une question à la fois, et on attend la réponse.",
              notes="Diapositive à photographier. Faire compter combien de "
                    "renseignements Rosario obtient : cinq, pour quatre questions. "
                    "Aucun ne lui aurait été donné si elle s'était tue.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Rosario doit acheter une nouvelle carte.", "faux — on recharge celle qu'elle a"),
        ("Sa fille de quinze ans a droit au tarif réduit.", "vrai — de 6 à 17 ans"),
        ("Pour le tarif réduit, il faut une carte avec photo.", "vrai"),
        ("Sa mère de soixante-huit ans paie le tarif ordinaire.", "faux — 65 ans et plus, tarif réduit"),
        ("Rosario paie comptant.", "faux — elle paie par carte"),
        ("Elle répète ce qu'elle a compris avant de partir.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le quatrième "
             "énoncé fait souvent hésiter : soixante-huit ans est bien au-dessus de "
             "soixante-cinq, donc tarif réduit.")

    d.billet(
        "Écrivez la première phrase que vous direz au comptoir.",
        exemples=[
            "Bonjour. Je voudrais ___ , s'il vous plaît.",
            "Est-ce que ___ ?",
        ],
        notes="Devoir court. Chacun écrit sa propre phrase, avec le titre qui lui "
              "convient. Elle servira telle quelle à la séance E1.")

    return d.save(dossier)
