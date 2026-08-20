# -*- coding: utf-8 -*-
"""D2 · Lire un horaire et un plan.
Bloc D · couleur ambre (écriture) · 90 min.
Source : mini-leçon `t3horaire`, exercices `t3horaire`, `t3plan` et `t3b`,
dialogue `t3b`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre='Lire un horaire et un plan',
        chapeau="Deux colonnes de chiffres, des petites lettres, des cercles "
                "blancs et noirs. Tout est écrit, rien n'est expliqué. Quatre "
                "conventions suffisent à tout lire.",
        duree='90 minutes')

    d.titre(notes="Séance longue et très concrète. Apporter un horaire papier et un plan de "
                  "réseau si possible — les sociétés de transport en distribuent.")

    d.objectifs([
        "distinguer la colonne de la semaine de celle de la fin de semaine ;",
        "comprendre ce qu'annonce une petite lettre à côté d'une heure ;",
        "lire un plan : couleurs, cercles blancs, cercles noirs ;",
        "trouver la direction d'une ligne en une seule opération.",
    ])

    d.dialogue('Dialogue', 'Deux colonnes de chiffres', [
        ("PATRICE", "Je n'arrive pas à lire cet horaire. Il y a deux colonnes de chiffres.", False),
        ("NOUR", "La première colonne, c'est la semaine. La deuxième, c'est la fin de semaine.", True),
        ("PATRICE", "Et les lettres à côté des heures ?", False),
        ("NOUR", "Un petit « a », ça veut dire que l'autobus ne va pas jusqu'au terminus. Il s'arrête avant.", True),
    ], consigne="Écoutez, puis repérez les deux conventions expliquées.",
       notes="Ce dialogue contient l'essentiel de la séance. Le faire écouter avant "
             "d'expliquer quoi que ce soit.")

    d.tableau('Analyse · 1 de 2', "L'horaire",
              ['Ce qu\'on voit', 'Ce que ça veut dire'],
              [["Première colonne", "du lundi au vendredi"],
               ["Deuxième colonne", "samedi et dimanche"],
               ["Une petite lettre", "une exception — voir la légende"],
               ["« Aux quinze minutes »", "un intervalle, pas une heure"]],
              cle=2,
              note="La légende des lettres est en bas de la page, en très petits caractères.",
              notes="Diapo centrale. Faire recopier. La troisième ligne est celle qui coûte "
                    "le plus cher quand on l'ignore.")

    d.tableau('Analyse · 2 de 2', "Le plan de réseau",
              ['Le symbole', 'Ce que ça veut dire'],
              [["Une couleur", "une ligne complète"],
               ["Un cercle blanc", "un arrêt ordinaire"],
               ["Un cercle noir", "une correspondance"],
               ["Un nom en gras au bout", "un terminus"]],
              cle=2,
              note="On ne change de ligne qu'aux cercles noirs.",
              notes="Projeter un plan réel en parallèle. Les élèves retrouvent leur propre "
                    "trajet en quelques minutes.")

    d.regle("La règle d'or, encore",
            "Le nom du terminus donne la direction. Sur un plan comme sur un quai.",
            precision="C'est la troisième fois du module qu'on le dit, et c'est voulu. Sur "
                      "un horaire, sur un plan, sur un panneau, sur un autobus : cherchez "
                      "le nom du terminus avant tout le reste. Le numéro de la ligne ne "
                      "distingue pas les deux sens.",
            notes="Diapo à photographier. Si les élèves ne retiennent qu'une chose du "
                  "module, c'est celle-là.")

    d.piege('Lire la mauvaise colonne',
            "Un samedi, je lis la première colonne.",
            "Un samedi, je lis la deuxième colonne.",
            "L'erreur ne se voit pas : on attend simplement un autobus qui ne viendra "
            "jamais. Le service de fin de semaine est toujours plus rare, et parfois "
            "inexistant sur certaines lignes.",
            notes="Faire vérifier sur un horaire réel : l'écart entre les deux colonnes "
                  "surprend souvent.")

    d.pratique('Pratique · 1 de 2', "Lire l'horaire",
               "Répondez d'après ce que Nour explique.", [
        ("La première colonne est celle de la…", "semaine"),
        ("La deuxième colonne est celle de la…", "fin de semaine"),
        ("Un petit « a » veut dire que l'autobus ne va pas jusqu'au…", "terminus"),
        ("Patrice doit donc prendre celui de 7 h…", "51"),
        ("« Aux vingt minutes » est une…", "fréquence, pas une heure de départ"),
    ], corrige=True, cols=1,
       notes="La dernière ligne reprend B4. La répétition entre les blocs est voulue.")

    d.pratique('Pratique · 2 de 2', "Lire le plan",
               "Dites ce que chaque symbole indique.", [
        ("Un cercle blanc", "un arrêt ordinaire — on descend, mais on ne change pas de ligne"),
        ("Un cercle noir", "une correspondance — on peut changer de ligne"),
        ("Une couleur", "une ligne complète, d'un terminus à l'autre"),
        ("Un nom en gras au bout d'une ligne", "un terminus — il donne la direction"),
        ("Un trait pointillé", "un service temporaire ou partiel"),
    ], corrige=True, cols=1,
       notes="Faire tracer un trajet complet sur le plan projeté, avec une correspondance. "
             "Dix minutes, très efficaces.")

    d.cartes('Trois erreurs coûteuses', "Et comment les éviter", [
        ("Changer de ligne à un cercle blanc",
         "On sort de la station pour rien. Vérifier la couleur du cercle avant de descendre."),
        ("Ignorer la petite lettre",
         "L'autobus s'arrête à mi-chemin et on descend là où on ne connaît personne. "
         "La légende est en bas de la page."),
        ("Se fier au numéro de la ligne",
         "Le même numéro circule dans les deux sens. Seul le nom du terminus les distingue."),
    ], notes="Ces trois erreurs sont celles que les élèves rapportent le plus souvent. "
             "Leur demander s'ils en ont vécu une.")

    d.billet(
        "Trouvez l'horaire de la ligne la plus proche de chez vous et répondez.",
        exemples=[
            "À quelle heure passe le premier autobus, en semaine ? Et le samedi ?",
            "Quel est le nom du terminus dans chaque direction ?",
            "Y a-t-il des petites lettres ? Que disent-elles ?",
        ],
        notes="Devoir à faire à la maison, sur un horaire réel. C'est le travail le plus "
              "utile du module : il se refait toute la vie.")

    return d.save(dossier)
