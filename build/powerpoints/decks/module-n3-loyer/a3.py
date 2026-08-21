# -*- coding: utf-8 -*-
"""A3 · Les seize mots du logement.
Bloc A « Je découvre » · couleur framboise · 75 min. Vocabulaire.
Source : exercices `prVocab` et `prPieces`, banc FC_CARDS.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='framboise',
        titre='Les seize mots du logement',
        chapeau="Quatre familles : les pièces, l'annonce, les gens, "
                "l'immeuble. Seize mots qui reviennent dans les seize "
                "séances.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire, placée après la phonétique pour que les mots "
                  "nouveaux soient dits correctement dès la première fois. Ouvrir en "
                  "demandant quels mots du logement chacun connaît déjà, et les écrire "
                  "au tableau sans corriger.")

    d.objectifs([
        "nommer les pièces : le salon, la cuisine, la chambre, la salle de bain, le balcon ;",
        "nommer ce que dit une annonce : meublé, chauffé, l'électricité comprise ;",
        "nommer les personnes : le propriétaire, le locataire, le concierge ;",
        "nommer l'immeuble : le sous-sol, la buanderie, le stationnement.",
    ])

    d.vocabulaire('Vocabulaire · 1 de 4', "Les pièces", [
        ("un logement", "l'endroit où on habite : un appartement, une maison"),
        ("une chambre à coucher", "la pièce fermée, avec une porte, où on dort"),
        ("un balcon", "la petite place ouverte, dehors, devant ou derrière"),
        ("un quatre et demie", "deux chambres fermées, un salon, une cuisine"),
    ], notes="Faire dire chaque mot avec son article. « Un quatre et demie » se dit au "
             "féminin même si on n'entend pas pourquoi : on sous-entend « pièce ».")

    d.vocabulaire('Vocabulaire · 2 de 4', "Ce que dit l'annonce", [
        ("une petite annonce", "le court texte qui dit qu'un logement est à louer"),
        ("meublé", "les meubles sont déjà là quand on arrive"),
        ("chauffé", "le chauffage est déjà payé dans le loyer"),
        ("l'électricité comprise", "le compte d'électricité est déjà dans le loyer"),
    ], notes="Ces quatre mots sont ceux du bloc B. Les poser ici sans les développer : "
             "ils seront repris devant une annonce réelle à la séance B1.")

    d.vocabulaire('Vocabulaire · 3 de 4', "L'argent et les personnes", [
        ("un loyer", "l'argent qu'on donne chaque mois"),
        ("louer", "payer chaque mois pour habiter un logement qui n'est pas à soi"),
        ("un propriétaire", "la personne à qui le logement appartient"),
        ("le bail", "le papier qu'on signe, pour douze mois d'habitude"),
    ], notes="« Le bail » se prononce comme « le travail ». Ne pas développer la "
             "question du bail ici : elle a sa séance, en D2.")

    d.vocabulaire('Vocabulaire · 4 de 4', "L'immeuble", [
        ("le sous-sol", "la partie de l'immeuble sous le rez-de-chaussée"),
        ("le chauffage", "ce qui réchauffe le logement quand il fait froid"),
        ("le stationnement", "l'endroit réservé où on laisse son auto"),
        ("prendre rendez-vous", "s'entendre sur un jour et une heure pour se voir"),
    ], notes="Les trois premiers reviennent à chaque visite. « Prendre rendez-vous » est "
             "le seul verbe de la liste : il annonce le bloc C.")

    d.tableau('Analyse', "Quatre verbes du programme",
              ["Le verbe", "Ce qu'il veut dire"],
              [["louer", "payer chaque mois pour habiter"],
               ["se renseigner", "aller chercher l'information, demander"],
               ["chauffer", "réchauffer le logement"],
               ["éclairer", "donner l'électricité et la lumière"]],
              cle=0,
              note="Chauffé et éclairé viennent de ces deux verbes-là.",
              notes="Diapositive à photographier. Ce sont les verbes que le programme "
                    "rattache à cette situation. Faire remarquer que « chauffé » et "
                    "« éclairé » sont les participes de « chauffer » et « éclairer » : "
                    "les annonces les emploient tels quels.")

    d.pratique('Vocabulaire', "Le mot et sa définition",
               "Dites de quel mot il s'agit.", [
        ("L'argent qu'on donne chaque mois.", "un loyer"),
        ("La pièce fermée où on dort.", "une chambre à coucher"),
        ("Le papier qu'on signe pour douze mois.", "le bail"),
        ("Un logement où les meubles sont déjà là.", "meublé"),
        ("La personne à qui le logement appartient.", "un propriétaire"),
        ("La partie de l'immeuble sous le rez-de-chaussée.", "le sous-sol"),
    ], corrige=True,
       notes="C'est l'exercice de vocabulaire du module, sous forme orale. Enchaîner "
             "avec l'activité interactive, où les seize mots se travaillent six à la "
             "fois par glisser-déposer.")

    d.pratique('Observation', "Les pièces du logement",
               "Nommez chaque pièce et dites ce qu'on y fait.", [
        ("La cuisine.", "le comptoir, l'évier, la fenêtre"),
        ("Le salon.", "la grande pièce, sans porte"),
        ("La chambre à coucher.", "fermée, avec une porte"),
        ("La salle de bain.", "le bain, le lavabo, la toilette"),
        ("Le balcon arrière.", "dehors, derrière la cuisine"),
    ], corrige=True,
       notes="Prépare l'exercice 3 de l'activité, qui reprend ces mêmes pièces par "
             "glisser-déposer. Faire décrire aussi la classe : où est la porte, où est "
             "la fenêtre, ce qu'il y a au fond.")

    d.billet(
        "Écrivez les quatre mots du logement qui vous manquaient avant aujourd'hui.",
        exemples=[
            "Je ne connaissais pas le mot ___ .",
            "Maintenant je sais que ___ veut dire ___ .",
        ],
        notes="Devoir court. Les mots qui reviennent le plus souvent dans les billets "
              "sont à reprendre en début de séance A4.")

    return d.save(dossier)
