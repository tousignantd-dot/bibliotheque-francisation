# -*- coding: utf-8 -*-
"""C1 · Quatre films, quatre petits textes.
Bloc C « Défi 2 · Le ciné-club du vendredi » · acier · 75 min.
Source du module : dialogue `t2`, exercice `t2vf`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Quatre films, quatre petits textes",
        chapeau="Le feuillet du ciné-club tient sur une page. Quatre films, "
                "quatre textes de trois lignes, et toujours le même ordre : "
                "le jour, l'heure, l'histoire en une phrase, le genre, la "
                "durée. C'est cet ordre qui rend la page lisible.",
        duree='75 minutes')

    d.titre(notes="Première séance du défi 2, et premier vrai travail de lecture du "
                  "module. Apporter si possible un vrai téléhoraire ou une page de "
                  "cinéma de quartier : la forme est la même partout.")

    d.objectifs([
        "reconnaître l'ordre des informations dans une description de film ;",
        "comprendre les mots de genre : drame, comédie, documentaire ;",
        "lire une durée écrite « 1 h 52 » ;",
        "choisir une séance à partir de trois lignes de texte.",
    ])

    d.dialogue('Dialogue · 1 de 3', "Trois lignes chacune", [
        ("THIERRY", "Marisol, tu as pris le feuillet du ciné-club ?", True),
        ("MARISOL", "Oui, mais je ne comprends pas tout. Il y a quatre films et quatre petits textes.", True),
        ("THIERRY", "Ce sont les descriptions. Trois lignes chacune, pas plus. Lis-moi la première.", True),
        ("MARISOL", "« Vendredi 3 octobre, 19 h. Une famille quitte son village et recommence sa vie en ville. Drame. 1 h 52. »", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Faire relire la quatrième réplique à voix haute par trois élèves "
             "différents. C'est le texte modèle de tout le défi : on y reviendra à "
             "chaque séance du bloc.")

    d.dialogue('Dialogue · 2 de 3', "Toujours dans le même ordre", [
        ("THIERRY", "Alors : le jour, l'heure, l'histoire en une phrase, le genre et la durée. Toujours dans cet ordre.", True),
        ("MARISOL", "« Drame », ça veut dire quoi ?", True),
        ("THIERRY", "Une histoire sérieuse, souvent triste. Une comédie, c'est le contraire : c'est drôle.", True),
        ("MARISOL", "Et « 1 h 52 » ?", True),
    ], notes="L'ordre annoncé dans la première réplique est la clé de la lecture. "
             "L'écrire au tableau en cinq mots et l'y laisser tout le bloc C.")

    d.dialogue('Dialogue · 3 de 3', "Un documentaire", [
        ("THIERRY", "La durée : une heure cinquante-deux. Presque deux heures.", True),
        ("MARISOL", "Le troisième dit « documentaire ». C'est un film avec des acteurs ?", True),
        ("THIERRY", "Non, justement. Un documentaire montre des choses vraies, des gens vrais.", True),
        ("MARISOL", "Celui-là parle des rivières du Québec. Camila aimerait ça.", False),
    ], notes="La question de Marisol sur le documentaire est celle que posent la moitié "
             "des élèves. Ne pas la traiter comme une évidence : le mot existe dans "
             "beaucoup de langues avec un sens plus large.")

    d.tableau('Analyse', "Les cinq informations, dans l'ordre",
              ["Le rang", "L'information", "Dans l'exemple"],
              [["1", "le jour et la date", "Vendredi 3 octobre"],
               ["2", "l'heure", "19 h"],
               ["3", "l'histoire, en une phrase", "Une famille quitte son village…"],
               ["4", "le genre", "Drame"],
               ["5", "la durée", "1 h 52"]],
              cle=1,
              note="Le même ordre pour les quatre films : la page se lit en diagonale.",
              notes="Diapo à photographier. Faire couvrir la troisième colonne et faire "
                    "redire l'ordre de mémoire. Puis distribuer le feuillet et faire "
                    "vérifier sur les trois autres films.")

    d.vocabulaire('Vocabulaire', "Les genres de films", [
        ("un drame",
         "Une histoire sérieuse, souvent triste. C'est le genre le plus fréquent des "
         "ciné-clubs de quartier."),
        ("une comédie",
         "Une histoire drôle, qui fait rire. Le contraire du drame."),
        ("un documentaire",
         "Un film qui montre des choses vraies et des gens vrais, sans acteurs qui "
         "jouent un rôle."),
        ("un film d'animation",
         "Des personnages dessinés. Souvent choisi pour les séances de familles."),
        ("un court métrage",
         "Un film très court, de quelques minutes. On en présente parfois deux ou trois "
         "à la suite."),
    ], notes="Demander à chacun quel genre il regarderait ce vendredi. C'est une "
             "question de goût, donc facile à répondre même avec peu de mots.")

    d.regle("Lire une durée",
            "« 1 h 52 » se dit « une heure cinquante-deux ».",
            precision="Le petit h veut dire « heure ». Les chiffres après lui sont des "
                      "minutes, jamais des centièmes. « 1 h 52 », c'est donc presque "
                      "deux heures — et « 1 h 05 », à peine plus d'une heure.",
            notes="Diapo à photographier. Faire lire cinq durées au hasard écrites au "
                  "tableau. Le point revient en C2, appliqué aux heures de séance.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Chaque description de film tient en trois lignes.", "vrai"),
        ("L'ordre est toujours : le jour, l'heure, l'histoire, le genre, la durée.", "vrai"),
        ("Un drame est une histoire drôle.", "faux — c'est une histoire sérieuse, souvent triste"),
        ("« 1 h 52 » veut dire une heure cinquante-deux minutes.", "vrai"),
        ("Un documentaire est joué par des acteurs.", "faux — il montre des choses vraies"),
        ("Le film du 17 octobre est sous-titré.", "vrai"),
    ], corrige=True,
       notes="C'est l'exercice t2vf du module. La dernière affirmation prépare C3, où "
             "le feuillet entier sera lu.")

    d.billet(
        "Écrivez la description d'un film que vous aimez, en trois lignes.",
        exemples=[
            "Respectez l'ordre : le jour, l'heure, l'histoire, le genre, la durée.",
            "Inventez le jour et l'heure : c'est la forme qu'on travaille, pas la vérité.",
        ],
        notes="Devoir court. Les descriptions écrites ce soir servent d'exercice de "
              "lecture en C3 : on les échange entre élèves plutôt que d'en relire une "
              "de plus dans le feuillet.")

    return d.save(dossier)
