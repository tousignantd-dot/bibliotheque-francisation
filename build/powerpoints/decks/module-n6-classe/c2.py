# -*- coding: utf-8 -*-
"""C2 · Ce que dit la page de la ville
Bloc C « Défi 2 » · couleur teal · 75 min. Compréhension écrite d'un texte suivi.
Source du module : exercice `t2src` (type `texte`) et la mini-leçon `t2src`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='teal',
        titre="Ce que dit la page de la ville",
        chapeau="Cinq paragraphes, une règle, une interdiction, une raison et "
                "un objectif. Trente secondes de repérage rendent la lecture "
                "deux fois plus rapide.",
        duree='75 minutes')

    d.titre(notes="C'est la séance qui porte l'unique intention de la "
                  "situation : comprendre de l'information liée à un sujet de "
                  "recherche. La ville, le bulletin et la lectrice sont "
                  "inventés — le dire, pour qu'aucun élève ne cite ce "
                  "document dans un vrai travail.")

    d.objectifs([
        "regarder un document avant de le lire ;",
        "retrouver dans un texte le passage qui répond à une question ;",
        "distinguer la règle, la raison et l'objectif ;",
        "noter ce qu'il faudra citer, avec sa date.",
    ], notes="Le module fait cliquer dans le texte ; en classe, on surligne "
             "sur la feuille distribuée. Prévoir des surligneurs de deux "
             "couleurs.")

    d.declencheur(
        'Pour commencer', "Qu'est-ce qu'on regarde avant de lire une page d'information ?",
        pistes=[
            "Qui l'a publiée ?",
            "De quand elle date ?",
            "Est-ce qu'il y a des intertitres ?",
        ],
        notes="Faire l'exercice en direct sur la feuille distribuée, montre "
              "en main : trente secondes, pas plus, puis demander ce qu'on "
              "sait déjà.")

    d.tableau('Analyse', "Ce que chaque paragraphe apporte",
              ['Le paragraphe', 'Ce qu\'il donne'],
              [["le premier", "la liste des matières acceptées et la fréquence"],
               ["le deuxième", "l'interdiction : aucun sac de plastique"],
               ["le troisième", "la raison : le méthane produit par l'enfouissement"],
               ["le quatrième", "les deux traitements : compostage, biométhanisation"],
               ["le cinquième", "l'objectif du gouvernement, et depuis quand"]],
              cle=0,
              note="Une idée par paragraphe : c'est ce que la grille demande à votre propre texte.",
              notes="Diapositive à photographier. Faire remarquer que le "
                    "document lu obéit à la même règle que le texte à écrire "
                    "— c'est le meilleur argument pour la ligne "
                    "« organisation ».")

    d.regle("Trois questions, avant de lire",
            "Qui parle ? Qu'est-ce que cette personne veut ? De quand ça date ?",
            precision="Une page de 2019 sur une collecte modifiée depuis dit "
                      "des choses fausses sans mentir. La date décide de ce "
                      "que vaut le reste.",
            notes="Diapositive à photographier. Ce sont les questions de la "
                  "bibliothécaire, vues en C1 : les mêmes, dans le même "
                  "ordre.")

    d.pratique('Pratique', "Trouvez le passage qui répond",
               "Pour chaque question, surlignez dans la page le passage qui y répond.", [
        ("Qu'est-ce qui a le droit d'aller dans le bac ?", "« les restes de table, les résidus de jardin, le papier souillé »"),
        ("À quelle fréquence est-il ramassé ?", "« chaque semaine du printemps à l'automne, une semaine sur deux l'hiver »"),
        ("Qu'est-ce qui n'est jamais accepté ?", "« aucun sac de plastique, même vendu comme biodégradable »"),
        ("Pourquoi retire-t-on les matières organiques ?", "« elles se décomposent sans air et produisent du méthane »"),
        ("Que fait-on de ce qui est ramassé ?", "« deux traitements : le compostage et la biométhanisation »"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `t2src` du module, du type `texte` : à "
             "l'écran, l'élève arme une question puis clique le passage, et "
             "le lien se voit des deux côtés.")

    d.tableau('Analyse', "Ce qui tient un texte suivi",
              ['Le fil', 'Ce qu\'il faut voir'],
              [["les pronoms", "le, en, y : ils renvoient à ce qui vient d'être dit"],
               ["les reprises", "cette distribution, ce ramassage"],
               ["les connecteurs", "par exemple, c'est-à-dire, notamment"],
               ["les temps", "un plus-que-parfait recule d'un cran"]],
              cle=0,
              note="Ce sont les quatre savoirs de grammaire du texte du niveau 6, et les quatre séances qui suivent.",
              notes="Diapositive à photographier. Elle annonce C3, C4 et C5 : "
                    "le dire, la suite du défi a alors un plan visible.")

    d.piege('Recherche',
            "citer une page sans noter sa date",
            "tout noter pendant la lecture",
            "Retrouver trois jours plus tard la page d'où venait une phrase "
            "prend plus de temps que de l'avoir écrite sur le coup. Et la "
            "grille est formelle : une source citée sans date ne compte pas, "
            "donc ce sont quatre points qui partent avec elle.",
            notes="Faire ouvrir un carnet ou un fichier « sources » séance "
                  "tenante, avec trois lignes par source : titre, qui "
                  "publie, date.")

    d.billet(
        "Recopie une phrase de la page de la ville que ton équipe va citer.",
        exemples=[
            "Entre guillemets, avec la source et la date en dessous.",
            "Une phrase, pas un paragraphe.",
        ],
        notes="Trois minutes. Vérifier surtout les guillemets : c'est le "
              "geste, plus que la phrase choisie, qui doit être acquis.")

    return d.save(dossier)
