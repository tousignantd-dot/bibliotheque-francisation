# -*- coding: utf-8 -*-
"""C2 · Ce carton-ci, cette boîte-là.
Bloc C « Défi 2 · La nouvelle adresse » · couleur ambre · 75 min.
Source : exercice `t2demo` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Ce carton-ci, cette boîte-là",
        chapeau="Un jour de déménagement, tout est en tas et rien n'a de nom. "
                "Il faut désigner.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire. Elle peut se faire debout, avec de vraies boîtes "
                  "ou de vrais objets : les démonstratifs s'apprennent en pointant.")

    d.objectifs([
        "choisir entre ce, cet, cette et ces ;",
        "savoir pourquoi « cet » existe ;",
        "employer -ci et -là pour opposer deux choses ;",
        "remplacer le nom par celui, celle, ceux, celles.",
    ])

    d.tableau('Les quatre formes', "Le genre et le nombre décident",
              ['La forme', 'Quand', 'Exemple'],
              [["ce", "masculin, devant une consonne", "ce carton · ce camion"],
               ["cet", "masculin, devant une voyelle ou un h muet", "cet escalier · cet immeuble"],
               ["cette", "féminin", "cette boîte · cette chambre"],
               ["ces", "pluriel, les deux genres", "ces cartons · ces boîtes"]],
              cle=0,
              note="« Cettes » n'existe pas. Le pluriel des deux genres est « ces ».",
              notes="Diapositive à photographier. La deuxième ligne est celle qu'on "
                    "explique, les trois autres se retiennent seules.")

    d.regle("« Cet » existe pour l'oreille, pas pour la grammaire",
            "« ce escalier » est impossible à dire : deux voyelles se cognent.",
            precision="Le t de « cet » fait la liaison : cet appartement, cet immeuble, "
                      "cet homme, cet été. À l'oreille, « cet » et « cette » se "
                      "prononcent pareil — c'est seulement à l'écrit qu'il faut choisir.",
            notes="Faire dire « ce escalier » à voix haute. Le groupe entend tout de suite "
                  "pourquoi la forme n'existe pas.")

    d.regle("-ci et -là servent à opposer",
            "Cette boîte-ci va dans la cuisine, cette boîte-là dans la chambre.",
            precision="S'il n'y a qu'une seule chose, on n'ajoute rien : « posez cette "
                      "boîte ici ». Le trait d'union, lui, est obligatoire.",
            notes="Erreur fréquente : mettre -ci partout pour insister. Le dire clairement, "
                  "sinon les productions écrites en seront couvertes.")

    d.cartes("Quand le nom disparaît", "celui · celle · ceux · celles", [
        ("— Quelle chambre ?", "— Celle qui donne sur la ruelle."),
        ("— Quelles boîtes ?", "— Celles-là, avec le point rouge."),
        ("Presque toujours suivi", "de -ci, de -là, de « qui » ou de « de »."),
        ("À l'oral", "« Celui-ci » tout seul ne se dit presque jamais sans un geste. "
                     "On pointe."),
    ], notes="Faire l'exercice en pointant de vrais objets du local : « celui-là », « celle "
             "qui est près de la fenêtre ». Deux minutes suffisent.")

    d.piege("Écrire « cette » pour un nom masculin",
            "cette escalier · cette immeuble",
            "cet escalier · cet immeuble",
            "À l'oreille, rien ne distingue « cet » de « cette ». C'est le genre du nom "
            "qui tranche, et il faut donc le connaître. Escalier, appartement, immeuble, "
            "été : tous masculins.",
            notes="Faire chercher cinq noms masculins commençant par une voyelle, puis "
                  "cinq féminins. La liste des masculins est plus longue qu'on croit.")

    d.pratique('Choix', "Ce, cet, cette ou ces ?",
               "L'enseignante lit la phrase sans le déterminant ; le groupe le donne.", [
        ("___ carton-ci contient la vaisselle.", "Ce"),
        ("___ escalier tourne serré.", "Cet"),
        ("___ boîtes-là vont dans la chambre du fond.", "Ces"),
        ("___ chambre donne sur la ruelle.", "Cette"),
        ("Je vais ouvrir mon compte ___ après-midi.", "cet"),
        ("___ immeuble a six logements.", "Cet"),
        ("Gardez ___ papiers-ci : c'est l'état des lieux.", "ces"),
        ("— Quelle boîte ? — ___ -là, avec le point rouge.", "Celle"),
    ], corrige=True,
       notes="Ce sont les items de l'exercice t2demo. La dernière ligne change de "
             "catégorie : c'est un pronom, pas un déterminant. Le faire remarquer.")

    d.pratique('Production', "Dites où va chaque chose",
               "Par deux, avec des objets du local : l'un désigne, l'autre exécute.", [
        ("Deux boîtes, deux endroits", "Cette boîte-ci dans la cuisine, cette boîte-là dans la chambre."),
        ("Un objet masculin à voyelle", "Cet objet-là, sur la table."),
        ("Plusieurs choses semblables", "Ces papiers-ci, gardez-les."),
        ("Une chose sans opposition", "Posez cette boîte ici, s'il vous plaît."),
        ("En remplaçant le nom", "— Quelle chaise ? — Celle qui est près de la porte."),
        ("Avec un impératif du bloc B", "Ne la mettez pas là : celle-là va dans le salon."),
    ], corrige=True,
       notes="La dernière ligne réunit l'impératif de B4 et le démonstratif d'aujourd'hui. "
             "C'est exactement ce que fait le dialogue t1b.")

    d.billet(
        "Décrivez trois objets de la pièce où vous êtes, sans dire leur nom.",
        exemples=[
            "« Celui qui est près de la fenêtre », « celle-là, sur la table ».",
            "Votre voisin doit deviner de quoi vous parlez.",
        ],
        notes="Le jeu force l'emploi du pronom démonstratif, qui est la partie la plus "
              "difficile de la séance.")

    return d.save(dossier)
