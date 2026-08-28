# -*- coding: utf-8 -*-
"""C4 · Répondre, complimenter, lire le carton.
Bloc C « Défi 2 · Venez prendre un café » · couleur acier · 60 min.
Source : exercices `t2rep`, `t2compl`, `t2carton`, mini-leçon `t2compl`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='acier',
        titre="Répondre, complimenter, lire le carton",
        chapeau="Jusqu'ici, on invitait. Cette fois on est invité : accepter, "
                "refuser sans blesser, dire une phrase gentille une fois "
                "sur place, et comprendre le carton trouvé sous sa porte.",
        duree='60 minutes')

    d.titre(notes="Dernière séance du défi 2. Elle renverse les rôles : jusqu'ici l'élève "
                  "était celui qui invite, il devient celui qu'on invite. C'est la moitié "
                  "du défi qu'on oublie le plus souvent.")

    d.objectifs([
        "accepter une invitation en une phrase ;",
        "refuser en donnant une raison, ou en proposant autre chose ;",
        "faire un compliment sur ce que la personne a fait ;",
        "lire un carton et y trouver ce qui est demandé.",
    ])

    d.pratique('Compréhension', "Accepter, ou refuser sans blesser",
               "Qu'est-ce que la personne fait vraiment ?", [
        ("« Avec plaisir ! À samedi. »", "elle accepte tout de suite"),
        ("« C'est gentil, mais je garde ma petite-fille ce jour-là. »", "elle refuse et elle dit pourquoi"),
        ("« Samedi, je ne peux pas. Est-ce que dimanche irait ? »", "elle refuse et propose un autre moment"),
        ("« Je vais voir, je vous le dis demain. »", "elle ne répond pas encore"),
        ("« Merci d'avoir pensé à moi. »", "elle remercie de l'invitation"),
        ("« Est-ce que je peux venir avec ma fille ? »", "elle accepte et demande une permission"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `t2rep` du module interactif. Faire remarquer que la "
             "quatrième n'est ni un oui ni un non, et que c'est parfaitement poli : on a "
             "le droit de ne pas savoir tout de suite, à condition de donner une date "
             "pour la réponse.")

    d.regle("Un refus se donne avec sa raison",
            "C'est gentil, mais je garde ma petite-fille ce jour-là.",
            precision="Trois morceaux : on remercie, on refuse, on dit "
                      "pourquoi. La raison n'a pas besoin d'être longue ni "
                      "vraie dans le détail — elle montre qu'on a considéré "
                      "l'invitation.",
            notes="Diapo à photographier. Un « non » seul, sans raison, blesse presque "
                  "toujours dans un immeuble : l'autre se demande ce qu'il a fait. Le "
                  "dire explicitement.")

    d.tableau('Analyse', "Complimenter : sur quoi porte la phrase",
              ["Ce qu'on dit", "Ce que ça complimente"],
              [["Que c'est bon !", "ce qu'on mange"],
               ["Vous cuisinez bien !", "ce que la personne a fait"],
               ["Ça vous va bien !", "ce que la personne porte"],
               ["Quelle belle porte !", "une chose de la maison"]],
              cle=1,
              note="Le compliment porte sur ce que la personne a fait ou "
                   "choisi, jamais sur ce qu'elle est.",
              notes="Diapo à photographier. La note du bas est la règle culturelle la "
                    "plus utile de la séance : un compliment sur le corps ou l'âge, ici, "
                    "met mal à l'aise. Le dire sans en faire un interdit solennel.")

    d.pratique('Écriture', "Que, comme, quel, quelle ou ça",
               "Complétez la phrase gentille.", [
        ("___ c'est bon, ces biscuits-là !", "Que — ou : Comme"),
        ("___ belle porte ! C'est vous qui l'avez peinte ?", "Quelle"),
        ("___ beau salon vous avez !", "Quel"),
        ("Votre manteau est neuf ? ___ vous va bien !", "Ça"),
        ("___ c'est gentil d'avoir pensé à moi !", "Comme — ou : Que"),
        ("___ bonne idée, ce café entre voisins !", "Quelle"),
    ], corrige=True,
       notes="C'est l'exercice `t2compl` du module interactif. « Quel » et « quelle » "
             "s'accordent avec le nom qui suit ; « que » et « comme » ne changent jamais. "
             "C'est tout ce qu'il faut retenir.")

    d.regle("On remercie, on ne se défend pas",
            "— Vous cuisinez bien ! — Merci, c'est gentil.",
            precision="Répondre « non, ce n'est pas vrai » ou « ce n'était "
                      "rien » est une politesse dans beaucoup de pays. Ici, "
                      "elle met l'autre mal à l'aise : il a dit quelque "
                      "chose de vrai, et on le contredit.",
            notes="Diapo à photographier. Faire pratiquer le tour complet, deux par "
                  "deux : compliment, merci, et rien de plus. C'est court, et c'est "
                  "exactement ce qui manque le plus souvent.")

    d.pratique('Compréhension', "Le carton glissé sous les portes",
               "« Petit café entre voisins — Nous venons d'arriver au 3A et nous "
               "aimerions vous connaître. La rencontre aura lieu le samedi 14, à 14 h, "
               "chez nous, au 3A. Il y aura du café, du thé et des gâteaux. N'apportez "
               "rien : votre bonne humeur suffit. Confirmez SVP en glissant un mot sous "
               "notre porte. — Rachid, Amina et Sami Belkacem »", [
        ("L'invitation dit le jour et l'heure.", "vrai — samedi 14, à 14 h"),
        ("Il faut apporter un dessert.", "faux — « n'apportez rien »"),
        ("La rencontre a lieu chez la voisine du deuxième.", "faux — au 3A"),
        ("On demande aux voisins de répondre.", "vrai — « confirmez SVP »"),
        ("On répond en glissant un mot sous la porte du 3A.", "vrai"),
        ("Trois personnes signent l'invitation.", "vrai — Rachid, Amina et Sami"),
    ], corrige=True,
       notes="C'est l'exercice `t2carton` du module interactif. Projeter le carton et "
             "faire souligner les six renseignements avant de répondre : c'est le modèle "
             "que l'élève copiera en E1.")

    d.billet(
        "Répondez au carton de Rachid, en deux phrases.",
        exemples=[
            "Vous acceptez, ou vous refusez avec une raison.",
            "« Merci d'avoir pensé à moi. Je serai là samedi à 14 h. »",
        ],
        notes="Devoir court. Ramasser : c'est le seul écrit du module où l'élève répond "
              "au lieu d'initier. Corriger la politesse d'abord, la grammaire ensuite.")

    return d.save(dossier)
