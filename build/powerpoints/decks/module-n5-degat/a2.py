# -*- coding: utf-8 -*-
"""A2 · Le son o : eau, au ou o.
Bloc A « Je découvre » · couleur indigo · 75 min. Graphie-phonie.
Source : exercice `prSon`, mini-leçon `prSon`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-degat/images/')


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Le son o : eau, au ou o",
        chapeau="Un seul son, trois orthographes. L'oreille ne peut pas "
                "trancher — et c'est justement ce qu'il faut expliquer avant "
                "de faire écrire quoi que ce soit.",
        duree='75 minutes')

    d.titre(notes="Séance de graphie-phonie. Commencer en écrivant au tableau « eau », "
                  "« chaud », « photo » et en demandant ce que ces trois mots ont en "
                  "commun. Personne ne le voit tout de suite : c'est le son.")

    d.objectifs([
        "entendre que eau, au et o se prononcent pareil ;",
        "savoir où chaque orthographe se place dans le mot ;",
        "connaître les lettres muettes qui suivent souvent ce son ;",
        "écrire correctement les mots du module qui le contiennent.",
    ])

    d.regle("Le son o s'écrit de trois façons",
            "eau, au et o se prononcent exactement pareil.",
            precision="Aucune règle de prononciation ne peut vous départager : il n'y a "
                      "rien à entendre. Ce qui décide, c'est la place du son dans le mot "
                      "et la famille du mot. La bonne méthode n'est donc pas d'écouter "
                      "mieux, c'est de voir le mot écrit souvent.",
            notes="Dire cette phrase telle quelle. Beaucoup d'élèves croient qu'ils "
                  "entendent mal ; les rassurer sur ce point change leur rapport à la "
                  "dictée.")

    d.tableau('Où va chaque orthographe', "La place dans le mot décide",
              ['Orthographe', 'Sa place, et un exemple du module'],
              [["eau", "à la fin des mots longs : l'eau, le bureau, le nouveau"],
               ["au", "au milieu, et devant d, t, s : chaud, une chaudière, aussi"],
               ["o", "dans les mots courts et savants : une photo, un numéro, trop"],
               ["un tuyau", "l'exception à retenir : « au » à la fin d'un mot"]],
              cle=0,
              note="Trois règles et une exception, c'est tout ce qu'il y a à retenir.",
              notes="Faire chercher au groupe d'autres mots pour chaque ligne. Les écrire "
                    "au tableau dans trois colonnes et les y laisser toute la séance.")

    d.cartes("Trois observations qui aident", "Ce qu'on peut regarder", [
        ("Devant d, t, s : presque toujours au",
         "chaud, haut, la faute, la cause, aussi. Une régularité solide."),
        ("Le son o final d'un mot long : souvent eau",
         "un chapeau, un morceau, un rideau, le bureau, le nouveau."),
        ("Les lettres muettes",
         "chaud, trop, haut, le mot : une consonne se cache à la fin."),
        ("Le féminin trahit la muette",
         "chaud donne chaude, haut donne haute. Le féminin fait entendre la lettre."),
    ], notes="La quatrième carte est la plus utile en dictée : chercher le féminin ou un "
             "mot de la même famille (chaud, chaudière) fait apparaître la lettre "
             "manquante.")

    d.pratique('Pratique · exercice prSon · 1 de 2', "Quelle orthographe entendez-vous ?",
               "Lisez la phrase à voix haute, puis dites comment le son o s'écrit "
               "dans le mot souligné.",
               [("L'eau tombait du plafond.", "eau"),
                ("Elle a mis une chaudière par terre.", "au"),
                ("J'ai pris vingt-deux photos.", "o"),
                ("Le réservoir était encore chaud.", "au"),
                ("Le bureau du propriétaire est fermé le samedi.", "eau")],
               corrige=True,
               notes="Lire chaque phrase deux fois : la première pour le sens, la seconde "
                     "en ne guettant que le mot souligné.")

    d.pratique('Pratique · exercice prSon · 2 de 2', "Quatre de plus",
               "Même consigne. Ces quatre-là sont ceux qui trompent le plus.",
               [("Voici mon numéro de dossier.", "o"),
                ("Le tuyau était fissuré depuis longtemps.", "au — à la fin du mot"),
                ("Le nouveau plancher arrive lundi.", "eau"),
                ("C'est trop de bruit pour une chambre.", "o, avec un p muet")],
               corrige=True,
               notes="« tuyau » est l'exception : la relever explicitement, elle revient "
                     "dans tout le module.")

    d.piege("Croire qu'on va finir par l'entendre",
            "Je vais mieux écouter la prochaine fois.",
            "Je vais regarder le mot écrit plus souvent.",
            "Les trois orthographes se prononcent identiquement : mieux écouter ne peut "
            "rien donner. C'est la paire son + image qui se retient. Un élève qui a vu "
            "« chaudière » écrit dix fois ne se trompe plus ; un élève qui l'a seulement "
            "entendu dix fois se trompe encore.",
            notes="Point important pour l'estime de soi du groupe : l'échec n'est pas "
                  "auditif, il est visuel.")

    d.vocabulaire('Vocabulaire · les mots en o du module', "À écrire, pas seulement à dire",
                  [("l'eau", "ce qui coule du plafond — et le mot de tout le module"),
                   ("une chaudière", "le seau de plastique posé sous la fuite"),
                   ("un tuyau", "le conduit qui amène ou évacue l'eau"),
                   ("chaud", "l'eau du chauffe-eau ; le féminin fait entendre le d"),
                   ("une photo", "la preuve datée du premier matin"),
                   ("un numéro", "celui du dossier de réclamation")],
                  notes="Dictée de six mots en fin de séance. Corriger au tableau en "
                        "entourant l'orthographe du son o dans chacun.")

    d.billet(
        "Écrivez trois mots avec le son o : un en eau, un en au, un en o.",
        exemples=[
            "« l'eau — une chaudière — une photo »",
            "Les mots peuvent venir d'ailleurs que du module.",
        ],
        notes="Deux minutes. La correction se fait au tableau en trois colonnes : elle "
              "sert de révision pour tout le groupe.")

    return d.save(dossier)
