# -*- coding: utf-8 -*-
"""C2 · La barre rouge.
Bloc C « Défi 2 · Le panneau qui dit quoi faire » · couleur ambre · 60 min.
Source : exercices `t2neg` et `t2secours`, mini-leçon `t2neg`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre='La barre rouge',
        chapeau="Un rond rouge barré, et c'est non — dans le monde entier. "
                "Les deux mots écrits à côté ne font que le répéter.",
        duree='60 minutes')

    d.titre(notes="Dernière séance avant « Je me lance ». Elle porte sur des panneaux "
                  "que le groupe comprend déjà : la difficulté est dans les mots, pas "
                  "dans le sens.")

    d.objectifs([
        "dire si un panneau permet ou interdit quelque chose ;",
        "reconnaître « défense de » et « ne… pas » ;",
        "comprendre SORTIE DE SECOURS et SILENCE ;",
        "savoir où l'on peut fumer, et où l'on ne peut pas.",
    ])

    d.declencheur(
        'Observation', "Permis, ou interdit ?",
        pistes=[
            "Une cigarette dans un rond rouge barré.",
            "Un chien dans un rond rouge barré.",
            "Une fontaine d'eau, sans barre.",
            "Comment le savez-vous ?",
        ],
        notes="Ils répondront tous juste, et vite. Le souligner : ils savent déjà lire "
              "ces panneaux-là. C'est encourageant, et c'est vrai.")

    d.regle("La barre rouge veut dire non",
            "Sans barre, c'est permis.",
            precision="Un dessin <b>seul</b> montre ce qu'on peut faire. Un dessin "
                      "<b>barré de rouge</b> montre ce qu'on ne fait pas. Ce signe se "
                      "comprend partout dans le monde, sans un seul mot.",
            notes="Diapositive à photographier. C'est la règle de la séance et elle "
                  "tient en une image.")

    d.tableau('Analyse', "Les deux façons d'écrire non",
              ['Sur le panneau', 'Ce que ça veut dire'],
              [["DÉFENSE DE FUMER", "on ne fume pas ici"],
               ["NE PAS ENTRER", "on n'entre pas"],
               ["SILENCE", "on ne parle pas fort"]],
              cle=1,
              note="« défense de » et « ne… pas » : dès qu'on les voit, c'est non.",
              notes="Diapositive à photographier. Faire souligner les deux petits "
                    "groupes de mots au cahier, en rouge.")

    d.pratique('Pratique', "Permis ou interdit ?",
               "Lisez le panneau, puis répondez.", [
        ("Une cigarette avec une barre rouge.", "interdit"),
        ("ENTREZ", "permis"),
        ("DÉFENSE DE FUMER", "interdit"),
        ("NE PAS ENTRER", "interdit"),
        ("Un verre d'eau, sans barre.", "permis"),
        ("Un chien avec une barre rouge.", "interdit"),
    ], corrige=True, cols=2,
       notes="Rapide, à main levée avant d'écrire. Même exercice que sur l'écran.")

    d.vocabulaire('Vocabulaire', "Quatre panneaux à connaître",
                  [("la sortie de secours", "la porte verte, pour partir vite"),
                   ("défense de fumer", "on ne fume pas ici"),
                   ("poussez", "la porte s'ouvre de l'autre côté"),
                   ("tirez", "la porte s'ouvre vers moi")],
                  notes="Faire répéter, puis faire montrer chacun des quatre dans le "
                        "corridor. Ils existent tous dans le bâtiment.")

    d.piege("Ouvrir la sortie de secours pour aller plus vite",
            "La porte verte est plus près.",
            "On prend la sortie ordinaire.",
            "La porte verte ne s'ouvre qu'en cas de danger. Le reste du temps, une "
            "alarme part et tout le bâtiment sort dehors. Ce n'est pas une amende, "
            "c'est un dérangement pour deux cents personnes.",
            notes="Le dire sans dramatiser. Plusieurs élèves ne savent pas du tout à "
                  "quoi sert cette porte, et personne ne leur a jamais expliqué.")

    d.regle("Où peut-on fumer ?",
            "Pas dans le bâtiment, pas devant la porte.",
            precision="Au Québec, il est interdit de fumer dans tous les bâtiments "
                      "publics, et à moins de <b>neuf mètres</b> d'une porte. C'est la "
                      "loi, pas une règle du centre.",
            notes="Information pratique, souvent inconnue et souvent source de "
                  "reproches. Montrer où l'on peut fumer, dehors, au sortir de la "
                  "séance.")

    d.billet(
        "Dessinez un panneau qui interdit quelque chose.",
        exemples=[
            "Le dessin, avec la barre rouge.",
            "Écrivez en dessous : c'est interdit.",
        ],
        notes="Deux minutes. Sert d'entrée à la production écrite de E1, qui demande "
              "au moins un panneau d'interdiction.")

    return d.save(dossier)
