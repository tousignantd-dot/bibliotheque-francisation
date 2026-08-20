# -*- coding: utf-8 -*-
"""B2 · Dire ce qui ne va pas.
Bloc B « Défi 1 » · couleur ambre · 60 min.
Source : mini-leçon `t1taille`, exercice `t1taille`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre='Dire ce qui ne va pas',
        chapeau="« Trop », « un peu », « pas assez » : trois mots qui "
                "changent tout. Avec un endroit, ils disent exactement ce "
                "qu'il faut changer.",
        duree='60 minutes')

    d.titre(notes="Séance de langue. Elle donne la formule que le jeu de rôle de E1 "
                  "réutilisera telle quelle.")

    d.objectifs([
        "employer trop, un peu, pas assez devant un adjectif ;",
        "situer le problème avec à, aux, dans ;",
        "demander une autre taille poliment ;",
        "distinguer taille et pointure.",
    ])

    d.declencheur(
        'Écoute', "Ces trois phrases disent-elles la même chose ?",
        pistes=[
            "« Il est serré. »",
            "« Il est un peu serré. »",
            "« Il est trop serré. »",
            "Laquelle veut dire : je le prends quand même ?",
        ],
        notes="La deuxième. « Un peu » atténue : le vêtement reste acceptable. « Trop » "
              "signifie que ça ne va pas. La nuance est décisive en magasin.")

    d.tableau('Analyse', "Les trois degrés",
              ['Le mot', 'Ce que ça veut dire'],
              [["un peu serré", "ça peut aller, mais je le remarque"],
               ["serré", "ça ne va pas très bien"],
               ["trop serré", "ça ne va pas — je change"],
               ["pas assez chaud", "il en manque"]],
              cle=2,
              note="« Trop » ferme la porte. « Un peu » la laisse ouverte.",
              notes="Diapo à photographier. Beaucoup d'élèves emploient « trop » pour tout, "
                    "et se font apporter une autre taille sans le vouloir.")

    d.regle("La formule complète",
            "degré + adjectif + endroit",
            precision="« Il est <b>un peu</b> <b>serré</b> <b>aux épaules</b>. » Les trois "
                      "morceaux ensemble donnent à la personne tout ce qu'il lui faut. "
                      "Sans l'endroit, elle apportera une autre taille ; avec l'endroit, "
                      "elle peut proposer une autre coupe.",
            notes="Diapo à photographier. Faire produire la formule complète par six élèves, "
                  "à voix haute.")

    d.cartes("Les endroits", "Trois petits mots", [
        ("aux — pour une partie double",
         "aux épaules, aux bras, aux jambes, aux hanches. C'est le cas le plus fréquent."),
        ("à la, au — pour une partie unique",
         "à la taille, à la poitrine, au cou, au dos."),
        ("dans — pour ce qui contient",
         "« Je flotte dans ce manteau. » « J'ai mal dans les bottes. » Moins fréquent, "
         "mais très naturel."),
    ], notes="Ne pas faire un cours sur les contractions : donner les formes toutes faites, "
             "elles s'apprennent en bloc.")

    d.tableau('Analyse', "Taille ou pointure ?",
              ['On dit', 'Pour'],
              [["la taille", "manteaux, chandails, pantalons, robes"],
               ["la pointure", "souliers, bottes, sandales"],
               ["« Je fais du 9 »", "la pointure, en chiffres"],
               ["« Je fais un moyen »", "la taille, en lettres"]],
              cle=1,
              note="Un pied a une pointure ; tout le reste a une taille.",
              notes="Erreur très fréquente et facile à corriger définitivement.")

    d.piege("Dire seulement « ça ne va pas »",
            "Non, ça ne va pas.",
            "Il est trop serré aux épaules.",
            "« Ça ne va pas » oblige la personne à deviner : elle apportera une autre "
            "taille, puis une autre, puis une autre. Dire où et comment fait gagner dix "
            "minutes et trois allers-retours.",
            notes="C'est le cœur de la séance. Le formuler comme un service qu'on rend, pas "
                  "comme une politesse.")

    d.pratique('Pratique · 1 de 2', "Complétez la phrase",
               "Employez un degré, un adjectif et un endroit.", [
        ("Le pantalon me serre à la ceinture.", "Il est trop serré à la taille."),
        ("Je ne peux pas lever les bras.", "Il est trop serré aux épaules."),
        ("Les manches dépassent mes mains.", "Les manches sont trop longues."),
        ("Le manteau flotte partout.", "Il est trop grand pour moi."),
        ("J'ai encore froid avec ce manteau.", "Il n'est pas assez chaud."),
    ], corrige=True, cols=1,
       notes="Accepter toute réponse contenant les trois morceaux.")

    d.pratique('Pratique · 2 de 2', "Demander une autre taille",
               "Trouvez une formule polie.", [
        ("Vous avez besoin d'un plus grand.", "Auriez-vous la taille au-dessus ?"),
        ("Vous avez besoin d'un plus petit.", "Est-ce que vous l'avez en plus petit ?"),
        ("Vous voulez une autre couleur.", "Vous l'avez dans une autre couleur ?"),
        ("Vous voulez essayer.", "Est-ce que je peux l'essayer ?"),
    ], corrige=True, cols=1,
       notes="Ces quatre formules sont à mémoriser. Les faire répéter deux fois.")

    d.billet(
        "Écrivez cinq phrases de la forme : degré + adjectif + endroit.",
        exemples=[
            "Une avec « un peu », deux avec « trop », une avec « pas assez ».",
            "Chacune avec un endroit différent.",
        ],
        notes="Ramasser et corriger. Ces phrases servent au jeu de rôle.")

    return d.save(dossier)
