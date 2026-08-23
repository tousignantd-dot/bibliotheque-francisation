# -*- coding: utf-8 -*-
"""C2 · Ce que dit le portrait, ligne par ligne
Bloc C « Défi 2 » · couleur ambre · 75 min.
Source : exercice `t2portrait` (type texte), mini-leçon `t2portrait`.
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n7-recherche' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Ce que dit le portrait, ligne par ligne",
        chapeau="Un portrait socioéconomique n'est pas un texte : c'est un "
                "tableau qu'on a mis en phrases. Aujourd'hui, on cherche "
                "dans le texte la ligne qui répond, et rien d'autre.",
        duree='75 minutes')

    d.titre(notes="Séance de lecture guidée. Distribuer le portrait imprimé — c'est "
                  "le même texte que l'exercice `t2portrait` du module interactif — "
                  "et travailler dessus, surligneur en main.")

    d.objectifs([
        "retrouver dans un texte suivi le passage qui répond à une question ;",
        "lire un pourcentage comme une part, jamais comme un nombre de postes ;",
        "repérer le mot « contre », qui annonce la comparaison utile ;",
        "vérifier la date de chaque chiffre avant de s'en servir.",
    ], notes="Le deuxième objectif est celui qui coûte le plus. Prévoir un calcul au "
             "tableau : 11,2 % de 137 100, c'est environ quinze mille postes.")

    d.declencheur(
        'Observation', "Que voit-on d'abord dans un document comme celui-ci ?",
        image=IMG + 'laboratoire-controle.jpg',
        pistes=[
            "Des chiffres, des pourcentages, des graphiques.",
            "Combien de pourcentages avez-vous comptés dans la première page ?",
            "Lesquels sont suivis d'un deuxième chiffre ?",
            "Pourquoi ce deuxième chiffre est-il là ?",
        ],
        notes="Faire compter réellement. Le portrait en contient une dizaine, et la "
              "moitié sont suivis d'un « contre ». C'est visible avant même de lire.")

    d.regle("Un pourcentage de l'emploi n'est pas un nombre de postes",
            "« La fabrication occupe 11,2 % de l'emploi » ne veut pas dire "
            "onze mille deux cents postes.",
            precision="Pour convertir, il faut l'emploi total — 137 100 dans notre "
                      "portrait — et il est donné au début du document, jamais à côté "
                      "du pourcentage. Notez-le avant de lire la suite : sans lui, "
                      "toutes les parts sont des informations vides.",
            notes="Diapositive à photographier. Faire le calcul ensemble au tableau, "
                  "une fois : 11,2 % de 137 100, environ 15 400 postes.")

    d.tableau('Analyse', "Ce que le portrait dit du territoire",
              ['La ligne du texte', 'Le chiffre'],
              [["Population", "286 395 habitants, 11e rang sur 17"],
               ["Produit intérieur brut, 2023", "15,5 G$, en hausse de 4,7 %"],
               ["Emploi total, 2025", "137 100 postes"],
               ["Ventes manufacturières", "11,1 milliards de dollars"]],
              cle=0,
              note="Chaque chiffre porte sa date. Deux dates différentes dans le même document.",
              notes="Diapositive à photographier. Faire surligner ces quatre lignes "
                    "dans le portrait imprimé avant de passer au tableau suivant.")

    d.tableau('Analyse', "Ce que le portrait dit des secteurs",
              ['Secteur', 'Part de l\'emploi'],
              [["Primaire", "4,2 %, soit le double de la moyenne de 2,0 %"],
               ["Fabrication", "11,2 %, tournée vers la transformation"],
               ["Construction", "8,9 %, contre 7,0 % au Québec"],
               ["Services", "75,6 % de l'ensemble de l'emploi"]],
              cle=0,
              note="Trois lignes sur quatre portent un « contre » ou une comparaison. C'est là qu'est l'information.",
              notes="Diapositive à photographier. La fabrication est la seule sans "
                    "comparaison : faire remarquer le manque, et se demander pourquoi.")

    d.piege('Lecture',
            "« la région est une région d'usines »",
            "« plus du tiers de son économie repose sur la production de biens »",
            "Les services y occupent tout de même 75,6 % de l'emploi, comme "
            "presque partout. Ce qui distingue la région, ce n'est pas "
            "l'absence de services : c'est la part inhabituelle de la "
            "production de biens. Le raccourci se retourne dans un exposé.",
            notes="Point de rigueur. Un élève qui dit « là-bas, tout le monde est en "
                  "usine » se fera contredire par le premier auditeur venu.")

    d.pratique('Lecture', "Retrouvez la ligne qui répond",
               "Écrivez le passage exact du portrait.", [
        ("Combien d'habitants la région compte-t-elle ?", "286 395 habitants"),
        ("Quel rang occupe-t-elle parmi les régions ?", "le onzième rang sur dix-sept"),
        ("À combien s'élève le PIB, et pour quelle année ?", "15,5 G$ en 2023"),
        ("Combien d'emplois en 2025 ?", "137 100 postes"),
        ("Quelle est la part du secteur primaire ?", "4,2 %, le double de la moyenne"),
        ("Sur quoi la fabrication se concentre-t-elle ?", "la transformation des ressources naturelles"),
        ("Combien valent les ventes manufacturières ?", "11,1 milliards de dollars"),
        ("Quelle part de l'emploi les services représentent-ils ?", "75,6 %"),
    ], corrige=True,
       notes="Exercice `t2portrait` du module interactif, où l'élève clique dans le "
             "texte. Sur papier, faire surligner : le geste est le même, et il compte "
             "autant que la réponse.")

    d.billet(
        "Deuxième ligne de votre feuille : que dit le portrait de votre région sur votre secteur ?",
        exemples=[
            "Une part de l'emploi, et sa comparaison s'il y en a une.",
            "Si le portrait ne dit rien de votre secteur, écrivez-le : c'est une information.",
        ],
        notes="La feuille de comparaison se remplit ligne par ligne depuis C1. La "
              "troisième ligne vient en C4.")

    return d.save(dossier)
