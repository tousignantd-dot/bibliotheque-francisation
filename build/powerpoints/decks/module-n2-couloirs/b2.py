# -*- coding: utf-8 -*-
"""B2 · Le premier chiffre dit l'étage.
Bloc B « Défi 1 · Le plan et les numéros » · couleur ambre · 75 min.
Source : exercices `t1etage` et `t1ou`, mini-leçons `t1etage` et `t1ou`.

Deux points de langue, tous deux tirés des savoirs du niveau 2 : les
adjectifs ordinaux (premier, deuxième) et les prépositions contractées
devant un nom de lieu (au, à la, à l', aux).

Ils tiennent ensemble parce qu'ils servent la même phrase : « c'est au
deuxième étage ». C'est la réponse que l'élève entendra le plus souvent, et
celle qu'il devra donner à son tour au bloc E.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-couloirs/images/')


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre="Le premier chiffre dit l'étage",
        chapeau="Trouver l'étage à partir du numéro, et dire où on va avec "
                "au, à la, à l' ou aux.",
        duree='75 minutes')

    d.titre(notes="Séance de langue, après la séance de lecture. Garder le plan de B1 "
                  "affiché au mur pendant toute l'heure.")

    d.objectifs([
        "trouver l'étage d'un local à partir de son numéro ;",
        "dire premier étage, deuxième étage, rez-de-chaussée ;",
        "choisir entre au, à la, à l' et aux ;",
        "dire une phrase entière : c'est au deuxième étage.",
    ])

    d.declencheur(
        'Devinette', "Le 118, c'est à quel étage ?",
        image=IMG + 'escalier-centre.jpg',
        pistes=[
            "Qu'est-ce que vous regardez en premier, dans ce numéro ?",
            "Et le 012 ?",
            "Et le 214 ?",
            "Comment vous faites pour le savoir ?",
        ],
        notes="Poser la devinette avant toute explication. La moitié du groupe aura "
              "trouvé la règle seule au bout de trois numéros : la faire dire par eux.")

    d.tableau('Analyse', "Le premier chiffre, et rien d'autre",
              ["Le numéro commence par", "C'est"],
              [["0 - 005, 012, 015", "le rez-de-chaussée"],
               ["1 - 108, 110, 118", "le premier étage"],
               ["2 - 210, 212, 214", "le deuxième étage"],
               ["les deux autres chiffres", "seulement quelle porte du corridor"]],
              cle=1,
              note="La règle vaut au Centre Bellevue. Ailleurs, c'est le plan qui le dit.",
              notes="Diapositive à photographier. Faire lire dix numéros au hasard et "
                    "répondre en chœur, très vite : la règle doit devenir un réflexe.")

    d.regle("Le rez-de-chaussée n'est pas un étage",
            "En français, l'étage du bas porte un nom à lui.",
            precision="On dit le <b>rez-de-chaussée</b>, jamais « l'étage zéro ». Le "
                      "<b>premier étage</b> est déjà un escalier plus haut. C'est une "
                      "source d'erreur constante pour qui vient d'un pays où le rez-de-"
                      "chaussée s'appelle le premier étage.",
            notes="Diapositive à photographier. Demander comment ça se dit dans les "
                  "langues du groupe : la différence se voit tout de suite, et elle "
                  "explique bien des malentendus.")

    d.tableau('Analyse', "Au, à la, à l', aux",
              ["On dit", "Quand"],
              [["au secrétariat, au deuxième étage", "le mot est masculin"],
               ["à la cafétéria, à la bibliothèque", "le mot est féminin"],
               ["à l'accueil, à l'ascenseur", "le mot commence par une voyelle"],
               ["aux toilettes, aux casiers", "il y en a plusieurs"]],
              cle=1,
              note="On ne dit jamais « à le » ni « à les » : ces deux formes n'existent pas.",
              notes="Diapositive à photographier. Ne pas expliquer la contraction : "
                    "donner les quatre cas et faire répéter avec des endroits réels.")

    d.piege('Le piège du jour',
            "« Je vais à le secrétariat »",
            "Je vais au secrétariat",
            "« À » et « le » se collent toujours en <b>au</b> ; « à » et « les » se "
            "collent en <b>aux</b>. Ce n'est pas une règle de style : les formes "
            "séparées n'existent pas en français, et personne ne les dit.",
            notes="Faire entendre les deux versions, la fausse d'abord. Puis faire "
                  "corriger cinq phrases à l'oral, très vite.")

    d.pratique('Pratique', "À quel étage ?",
               "Répondez par une phrase entière.", [
        ("Le local 214", "Il est au deuxième étage."),
        ("Le local 108", "Il est au premier étage."),
        ("Le local 012", "Il est au rez-de-chaussée."),
        ("Le local 210", "Il est au deuxième étage."),
        ("Le local 118", "Il est au premier étage."),
        ("Le local 005", "Il est au rez-de-chaussée."),
    ], corrige=True, cols=2,
       notes="Six items. Exiger la phrase entière : c'est là que « au » s'installe, "
             "pas dans un mot isolé.")

    d.pratique('Pratique · à deux', "Où est-ce que tu vas ?",
               "A pose la question, B répond avec au, à la, à l' ou aux.", [
        ("Étape 1", "A nomme un endroit du centre : la cafétéria, l'accueil, les toilettes."),
        ("Étape 2", "B répond : je vais à la cafétéria, je vais à l'accueil."),
        ("Étape 3", "On échange les rôles au bout de cinq endroits."),
        ("Étape 4", "On refait la série avec les vrais endroits de notre centre."),
    ], cols=1,
       notes="Quinze minutes. Circuler et écouter les « à le » : ils sortent tout "
             "seuls, et se corrigent sur-le-champ, sans commentaire.")

    d.billet(
        "Écrivez trois phrases avec au, à la et aux.",
        exemples=[
            "Mon cours est au deuxième étage.",
            "Je mange à la cafétéria.",
            "Mon manteau est aux casiers.",
        ],
        notes="Devoir court. Une phrase par forme : c'est le contrôle le plus rapide "
              "de la séance.")

    return d.save(dossier)
