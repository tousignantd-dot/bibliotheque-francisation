# -*- coding: utf-8 -*-
"""A2 · Le son CH et le son S.
Bloc A « Je découvre » · couleur indigo · 75 min. Graphie-phonie.
Source : exercice `prPhon` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre='Le son CH et le son S',
        chapeau="Chambre, chauffage, chercher — salon, sous-sol, salle. Deux "
                "sons voisins, et presque tout le vocabulaire du logement "
                "passe par l'un ou par l'autre.",
        duree='75 minutes')

    d.titre(notes="Séance de prononciation, placée tout de suite après la découverte "
                  "pour que les mots nouveaux soient dits correctement dès la première "
                  "fois. Ouvrir en écrivant au tableau « chambre » et « salon » et en "
                  "demandant au groupe de les répéter.")

    d.objectifs([
        "entendre la différence entre le son CH et le son S ;",
        "prononcer chambre, chauffage, chercher avec les lèvres avancées ;",
        "prononcer salon, sous-sol, salle avec la langue en avant ;",
        "savoir qu'un seul s entre deux voyelles se dit comme un z.",
    ])

    d.regle("Ce qui change, c'est la bouche",
            "Les lèvres pour CH, la langue pour S",
            precision="Pour CH, les lèvres s'avancent, comme pour souffler sur "
                      "une cuillère. Pour S, les lèvres ne bougent pas et la "
                      "langue reste derrière les dents du haut. Mettez la main "
                      "devant la bouche : l'air ne sort pas au même endroit.",
            notes="Diapositive à photographier. Faire le geste devant le groupe, très "
                  "exagérément, puis faire imiter. C'est une séance où l'on regarde "
                  "beaucoup la bouche de l'enseignante.")

    d.tableau('Analyse', "Le son CH — les lèvres en avant",
              ["On écrit", "On entend"],
              [["une chambre", "le son CH au début"],
               ["le chauffage", "le son CH au début"],
               ["chercher", "le son CH deux fois"],
               ["un chèque", "le son CH au début"]],
              cle=0,
              note="Presque toujours écrit avec les deux lettres c et h.",
              notes="Diapositive à photographier. Les quatre mots reviennent dans tout "
                    "le module. « Chercher » est le plus difficile : deux fois le même "
                    "son dans un mot court.")

    d.tableau('Analyse', "Le son S — la langue en avant",
              ["On écrit", "On entend"],
              [["le salon", "le son S au début"],
               ["le sous-sol", "le son S deux fois"],
               ["la salle de bain", "le son S au début"],
               ["samedi", "le son S au début"]],
              cle=0,
              note="Écrit s au début, ss entre deux voyelles, parfois c devant e ou i.",
              notes="Diapositive à photographier. « Sous-sol » est le mot du module : il "
                    "porte le son deux fois et il reviendra à chaque séance du bloc D.")

    d.tableau('Analyse', "Le piège : un seul s se dit comme un z",
              ["On écrit", "On entend"],
              [["la cuisine", "le son Z au milieu"],
               ["la maison", "le son Z au milieu"],
               ["une chaise", "le son Z à la fin"],
               ["une adresse", "le son S, parce qu'il y a deux s"]],
              cle=0,
              note="Un seul s entre deux voyelles se dit Z. Deux s gardent le son S.",
              notes="Diapositive à photographier. C'est la règle qui explique pourquoi "
                    "« cuisine » ne se prononce pas comme on l'écrit. Elle vaut pour "
                    "toute la langue, pas seulement pour ce module.")

    d.piege('Prononciation',
            "« le logement est sauffé »",
            "« le logement est chauffé »",
            "C'est le mot le plus important d'une annonce : il dit qui paie le "
            "chauffage. Avancez bien les lèvres avant de commencer le mot, et "
            "faites-le durer un peu.",
            notes="Faire répéter la phrase complète, pas le mot seul : « Le logement est "
                  "chauffé et éclairé. » C'est ainsi qu'elle se dira au téléphone.")

    d.piege('Prononciation',
            "« la cuiSSine »",
            "« la cuiZine »",
            "Un seul s entre deux voyelles se dit toujours comme un z. Pour "
            "garder le son S, il faut deux s : une adresse, une poussière.",
            notes="Faire chercher au groupe d'autres mots du logement avec un s entre "
                  "deux voyelles : maison, chaise, voisin, saison. Tous se disent avec "
                  "un z.")

    d.pratique('Discrimination', "CH ou S ?",
               "Écoutez chaque mot et dites quel son vous entendez.", [
        ("une chambre", "CH"),
        ("le salon", "S"),
        ("le chauffage", "CH"),
        ("le sous-sol", "S"),
        ("la cuisine", "S, puis Z au milieu"),
        ("chercher un logement", "CH deux fois"),
    ], corrige=True, cols=2,
       notes="C'est l'exercice 2 de « Je découvre », où chaque mot s'écoute en touchant "
             "la carte. Faire d'abord l'exercice à voix haute, puis ouvrir l'activité "
             "sur les postes.")

    d.pratique('Répétition', "Six phrases de la visite",
               "Écoutez, puis répétez lentement.", [
        ("Le logement est chauffé et éclairé.", "CH deux fois"),
        ("Le salon est à côté de la cuisine.", "S trois fois"),
        ("Je cherche une chambre de plus.", "CH deux fois"),
        ("La buanderie est au sous-sol.", "S trois fois"),
        ("Les chaises restent dans la cuisine.", "CH, puis Z"),
        ("La salle de bain est au fond du couloir.", "S deux fois"),
    ], corrige=True,
       notes="Répétition en chœur, puis individuellement. Faire ralentir : à vitesse "
             "normale, les deux sons se confondent et l'exercice ne sert plus à rien.")

    d.billet(
        "Écrivez deux mots du logement avec le son CH et deux mots avec le son S.",
        exemples=[
            "Avec le son CH : ___ et ___ .",
            "Avec le son S : ___ et ___ .",
        ],
        notes="Devoir court. Relever les mots qui reviennent le plus : ils seront repris "
              "en début de séance A3, au moment du vocabulaire.")

    return d.save(dossier)
