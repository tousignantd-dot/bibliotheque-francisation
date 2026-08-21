# -*- coding: utf-8 -*-
"""A3 · Dans le magasin des appareils.
Bloc A « Je découvre » · couleur teal · 60 min.
Source : exercice `prImg`, banc `FC_CARDS`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-electro/images/')


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre='Dans le magasin des appareils',
        chapeau="Un magasin d'électroménagers est grand comme un aréna. "
                "Reconnaître les objets et les endroits avant d'y entrer, "
                "c'est la moitié du travail.",
        duree='60 minutes')

    d.titre(notes="Séance de vocabulaire. Prévoir de projeter les huit images de "
                  "l'exercice 3 du module interactif : elles servent de support à toute "
                  "la séance.")

    d.objectifs([
        "reconnaître les endroits d'un magasin d'appareils ;",
        "nommer les objets qui portent l'information : circulaire, affichette ;",
        "associer une image et une phrase qui la décrit ;",
        "dire ce qu'on cherche en une phrase courte.",
    ])

    d.declencheur(
        'Observation', "Où est-ce qu'on regarde en premier ?",
        image=IMG + 'affiche-rayon.jpg',
        pistes=[
            "Qu'est-ce qui est écrit en gros dans un magasin ?",
            "Comment trouve-t-on un rayon sans demander ?",
            "Qu'est-ce qui est écrit sur le petit carton devant l'appareil ?",
            "À qui demande-t-on quand on ne trouve pas ?",
        ],
        notes="Faire remarquer que tout est écrit : l'affiche du rayon, l'affichette de "
              "l'appareil, la circulaire. C'est exactement l'intention du programme pour "
              "cette situation — lire avant de parler.")

    d.tableau('Analyse', "Trois papiers, trois usages",
              ['Le papier', 'Où il est', 'Ce qu\'il donne'],
              [["la circulaire", "dans la boîte aux lettres", "les spéciaux de la semaine"],
               ["l'affiche du rayon", "suspendue au plafond", "où sont les appareils"],
               ["l'affichette", "devant l'appareil", "le prix et le format"],
               ["le bon de livraison", "au comptoir, après la caisse", "le jour du camion"]],
              cle=0,
              note="Aucun de ces papiers ne se lit en entier : on y cherche une chose.",
              notes="Diapo à photographier. C'est la carte de route du module : quatre "
                    "papiers, quatre moments de l'achat.")

    d.cartes("Les mots des lieux", "Quatre mots à retenir", [
        ("le rayon",
         "L'endroit du magasin où on met ensemble les mêmes sortes d'articles. On dit "
         "aussi « l'allée » pour un couloir entre deux tablettes."),
        ("l'affichette",
         "Le petit carton posé devant l'appareil, avec le prix, le modèle et le format. "
         "Il reste au magasin ; il ne part pas avec l'appareil."),
        ("la caisse",
         "Le comptoir où on paie. Le terminal de paiement est posé dessus."),
        ("le comptoir de la livraison",
         "L'endroit, près de la sortie, où on donne son adresse pour le camion. Ce n'est "
         "pas la caisse : on y va après avoir payé."),
    ], notes="Faire répéter chaque mot avec son article. Demander à qui on parle à chaque "
             "endroit : au vendeur dans le rayon, à la caissière à la caisse.")

    d.pratique('Vocabulaire', "Quelle image ?",
               "Dites de quelle image il s'agit.", [
        ("Une rangée de laveuses blanches, côte à côte.", "le rayon des laveuses"),
        ("Le papier du magasin ouvert sur une table de cuisine.", "la circulaire"),
        ("Le petit carton posé devant l'appareil.", "l'affichette"),
        ("La grande affiche suspendue au plafond.", "l'affiche du rayon"),
        ("Le ruban déroulé entre un mur et une porte.", "le ruban à mesurer"),
        ("Le camion arrêté devant un immeuble.", "la livraison"),
    ], corrige=True,
       notes="Projeter les images une à une et faire répondre à voix haute. Les phrases "
             "sont celles de l'exercice 3 du module interactif : les élèves les "
             "retrouveront telles quelles.")

    d.regle("Dire ce qu'on cherche, en une phrase",
            "« Bonjour. Je cherche une laveuse. »",
            precision="Trois mots après « bonjour », et le vendeur sait où vous "
                      "emmener. Ajouter la marque ou le modèle ne sert à rien "
                      "tant qu'on n'est pas devant l'appareil.",
            notes="Diapo à photographier. Faire dire la phrase par chaque élève, avec "
                  "l'appareil de son choix.")

    d.piege("Chercher tout seul pendant vingt minutes",
            "tourner dans les allées sans demander",
            "Bonjour, où est le rayon des laveuses ?",
            "Dans un magasin de cette taille, personne ne trouve seul, pas même les gens "
            "d'ici. Demander est la façon normale de faire, et c'est aussi la seule "
            "occasion de parler français de la journée.",
            notes="Insister : la gêne de demander coûte du temps et une occasion de "
                  "pratiquer. La question exacte s'apprend en C1.")

    d.billet(
        "Mesurez la place que vous avez chez vous pour un appareil.",
        exemples=[
            "Entre deux murs, ou entre le mur et la porte.",
            "Écrivez le chiffre en pouces : on s'en servira au défi 2.",
        ],
        notes="Devoir concret. Beaucoup d'élèves n'ont jamais mesuré en pouces : montrer "
              "un ruban à mesurer en classe et faire lire trois mesures.")

    return d.save(dossier)
