# -*- coding: utf-8 -*-
"""C3 · Lire le feuillet du ciné-club.
Bloc C « Défi 2 · Le ciné-club du vendredi » · teal · 75 min.
Source du module : exercices `t2genre` et `t2choix`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='teal',
        titre="Lire le feuillet du ciné-club",
        chapeau="Quatre films, quatre descriptions, une seule page. Il ne "
                "s'agit pas de tout comprendre : il s'agit de trouver, en "
                "vingt secondes, celui qu'on veut aller voir.",
        duree='75 minutes')

    d.titre(notes="Séance de compréhension écrite, la plus proche de l'intention du "
                  "programme : « lire une brève description de film dans un "
                  "téléhoraire ». Projeter le feuillet et laisser le groupe chercher "
                  "avant d'expliquer quoi que ce soit.")

    d.objectifs([
        "trouver une information précise dans un feuillet de quatre entrées ;",
        "comparer les durées et les heures de quatre séances ;",
        "reconnaître le genre d'un film à sa description ;",
        "choisir une séance selon qui m'accompagne.",
    ])

    d.tableau('Le feuillet · 1 de 2', "Ciné-club d'automne · salle 2",
              ["Quand", "La description"],
              [["Vendredi 3 octobre, 19 h",
                "Une famille quitte son village et recommence sa vie en ville. "
                "Drame. 1 h 52."],
               ["Vendredi 10 octobre, 19 h",
                "Deux voisins se disputent un stationnement pendant tout un "
                "hiver. Comédie. 1 h 34."]],
              note="Le jour, l'heure, l'histoire, le genre, la durée. Toujours dans cet ordre.",
              notes="Diapo à photographier. La laisser à l'écran pendant les exercices "
                    "qui suivent : chercher dans un texte qu'on a sous les yeux, c'est "
                    "ce que fait un lecteur réel.")

    d.tableau('Le feuillet · 2 de 2', "Ciné-club d'automne · salle 2",
              ["Quand", "La description"],
              [["Vendredi 17 octobre, 19 h 30",
                "Les rivières du Québec, du printemps à l'automne. "
                "Documentaire. 1 h 10. En français, sous-titré."],
               ["Vendredi 24 octobre, 14 h",
                "Un chien perdu traverse la ville pour retrouver sa rue. Film "
                "d'animation. 1 h 05. Pour les familles."]],
              note="Ces deux-là portent une précision de plus : sous-titré, pour les familles.",
              notes="Diapo à photographier. Les deux mentions supplémentaires sont "
                    "exactement celles qui font choisir : elles disent à qui la séance "
                    "s'adresse. Le faire remarquer avant les exercices.")

    d.pratique('Lecture · 1 de 2', "De quel film s'agit-il ?",
               "Lisez les quatre descriptions, puis répondez : 3, 10, 17 ou 24 octobre ?", [
        ("C'est le film le plus court des quatre.", "le 24 octobre — 1 h 05"),
        ("C'est le seul film qui n'est pas présenté le soir.", "le 24 octobre — à 14 h"),
        ("C'est celui qui commence à sept heures et demie.", "le 17 octobre — 19 h 30"),
        ("C'est le film qui devrait faire rire.", "le 10 octobre — une comédie"),
        ("C'est le film le plus long, presque deux heures.", "le 3 octobre — 1 h 52"),
        ("C'est celui qui montre des choses vraies, sans acteurs.", "le 17 octobre — un documentaire"),
        ("C'est le film à choisir pour venir avec un enfant de huit ans.", "le 24 octobre — pour les familles"),
        ("C'est celui où on entend le français et où on peut le lire en même temps.",
         "le 17 octobre — en français, sous-titré"),
    ], corrige=True,
       notes="C'est l'exercice t2choix du module. Chronométrer : vingt secondes par "
             "question, feuillet sous les yeux. La vitesse fait partie de la "
             "compétence — un feuillet se lit debout, dans une entrée.")

    d.pratique('Lecture · 2 de 2', "Le genre et ce qu'il annonce",
               "Reliez chaque genre à ce qu'il promet.", [
        ("un drame", "une histoire sérieuse, souvent triste"),
        ("une comédie", "une histoire drôle, qui fait rire"),
        ("un documentaire", "des choses vraies et des gens vrais, sans acteurs"),
        ("un film d'animation", "des personnages dessinés, souvent pour les familles"),
        ("un film policier", "un crime, une enquête et quelqu'un qui cherche"),
        ("un court métrage", "un film très court, de quelques minutes seulement"),
    ], corrige=True,
       notes="C'est l'exercice t2genre du module. Les deux derniers genres ne sont pas "
             "au feuillet : ils élargissent la liste vers ce qu'on trouve ailleurs.")

    d.regle("Ce que « sous-titré » veut dire",
            "On entend le film et on lit en même temps ce qui est dit.",
            precision="Pour quelqu'un qui apprend le français, une séance sous-titrée en "
                      "français vaut deux séances ordinaires : l'oreille et l'œil "
                      "travaillent ensemble, et le mot qu'on n'attrape pas au vol se "
                      "lit au bas de l'écran.",
            notes="Diapo à photographier. Beaucoup d'élèves ignorent que les sous-titres "
                  "français existent sur les plateformes qu'ils ont déjà chez eux. Le "
                  "dire : c'est une heure d'exposition gratuite par soir.")

    d.piege('Le piège', "un documentaire, c'est un film avec de vrais acteurs",
            "un documentaire montre des gens vrais, qui ne jouent pas",
            "Personne ne joue un rôle dans un documentaire : on filme des personnes "
            "réelles dans leur vie réelle. Le mot existe dans beaucoup de langues avec "
            "un sens plus large — d'où la confusion, qui n'a rien d'une étourderie.",
            notes="La question vient de Marisol dans le dialogue de C1. Y renvoyer : "
                  "l'élève qui l'a posée voit que sa question était la bonne.")

    d.billet(
        "Choisissez une des quatre séances et dites pourquoi.",
        exemples=[
            "Écrivez le jour, l'heure, le genre et la durée.",
            "Ajoutez une phrase : avec qui iriez-vous, et pourquoi celle-là ?",
        ],
        notes="Devoir court. Il prépare le message d'invitation du bloc E, où la même "
              "information devra être écrite à quelqu'un d'autre.")

    return d.save(dossier)
