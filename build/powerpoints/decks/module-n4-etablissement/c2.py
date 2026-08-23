# -*- coding: utf-8 -*-
"""C2 · Parce que, à cause de, grâce à
Bloc C « Défi 2 · Les messages qu'on me laisse » · couleur ambre · 75 min.
Source du module : exercice `t2cause` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Parce que, à cause de, grâce à",
        chapeau="Donner une raison est le cœur du module : justifier, c'est "
                "exactement cela. Trois outils, et ils ne se choisissent pas "
                "au hasard — l'un sous-entend un ennui, l'autre une aide.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire, et la plus utile du module hors de la classe. "
                  "Commencer par écrire les trois au tableau et demander lequel est "
                  "positif. Personne ne le sait, et c'est justement le contenu de la "
                  "séance.")

    d.objectifs([
        "employer « parce que » devant une phrase complète ;",
        "employer « à cause de » devant un nom, pour un ennui ;",
        "employer « grâce à » devant un nom, pour une aide ;",
        "faire la contraction : à cause du, grâce au.",
    ], notes="Le troisième objectif est celui qui change quelque chose : « grâce à » "
             "est une phrase que le personnel d'un centre entend rarement, et qui fait "
             "toujours plaisir.")

    d.regle("Ce qui suit décide",
            "Parce que + une phrase. À cause de + un nom. Grâce à + un nom.",
            precision="« À cause de mon fils est malade » n'existe pas : il "
                      "faut « parce que ».",
            notes="Diapositive à photographier. La règle tient dans le mot qui suit, "
                  "pas dans le sens : faire chercher au groupe ce qui suit dans chaque "
                  "exemple avant d'expliquer quoi que ce soit.")

    d.tableau('Trois outils', "Ce qui suit, et ce que ça veut dire",
              ['L\'outil', 'Ce qui suit, et le sens'],
              [["parce que", "Une phrase complète. Aucun jugement : ça convient partout."],
               ["à cause de", "Un nom. La chose a causé un ennui."],
               ["grâce à", "Un nom. La chose a aidé."]],
              note="Même construction pour les deux derniers, sens opposé.",
              notes="Insister sur la deuxième ligne : « à cause de vous, j'ai réussi » "
                    "se comprend mais sonne comme un reproche. C'est le seul point de "
                    "la séance qui ne s'apprend pas par la forme.")

    d.cartes("Parce que", "Une phrase complète derrière", [
        ("La forme entière",
         "Je serai absente parce que mon fils est malade."),
        ("Devant une voyelle",
         "Je vous rappelle parce qu'il manque un papier. Le e tombe."),
        ("Au milieu, jamais au début",
         "Dans une note, « parce que » vient toujours après la première partie."),
        ("Ce qui ne se dit pas",
         "« parce que la tempête » — il manque le sujet et le verbe."),
    ], notes="Faire produire trois phrases avec « parce que » à partir de motifs réels "
             "du groupe. Vérifier chaque fois qu'un sujet et un verbe suivent.")

    d.tableau('Les contractions', "de + le, à + le",
              ['La forme', 'L\'exemple'],
              [["à cause de la", "à cause de la neige, à cause de la tempête"],
               ["à cause de l'", "à cause de l'autobus, à cause de l'heure"],
               ["à cause du", "à cause du bruit, à cause du verglas"],
               ["à cause des", "à cause des travaux, à cause des enfants"],
               ["grâce au", "grâce au rattrapage, grâce au message"],
               ["grâce aux", "grâce aux feuilles gardées"]],
              cle=1,
              notes="La contraction est obligatoire, comme dans « je parle du cours ». "
                    "Ce n'est pas une règle nouvelle : c'est la même que celle des "
                    "déterminants contractés, déjà vue au niveau 3.")

    d.pratique('Complétez', "Parce que, à cause de, grâce à",
               "Attention aux contractions.", [
        ("Je serai absente ce matin ___ mon fils a une otite.", "parce que"),
        ("Elle est arrivée en retard ___ la tempête de neige.", "à cause de"),
        ("Le cours a été annulé ___ bruit des travaux.", "à cause du"),
        ("___ son message, elle a appris l'affaire à temps.", "Grâce à"),
        ("Je vous rappelle ___ il manque un papier à mon dossier.", "parce qu'"),
        ("Elle a rattrapé la matière ___ rattrapage du midi.", "grâce au"),
    ], corrige=True,
       notes="Les deux dernières sont les plus manquées : l'élision de « parce qu' » et "
             "la contraction « grâce au ». Les faire écrire au tableau plutôt que dire.")

    d.pratique('Le bon sens', "Ennui ou aide ?",
               "À cause de, ou grâce à ?", [
        ("___ la neige, je serai en retard.", "à cause de — c'est un ennui"),
        ("___ Wilner, j'avais le bon numéro.", "grâce à — c'est une aide"),
        ("___ des travaux, le local a changé.", "à cause — c'est un ennui"),
        ("___ au rattrapage, je n'ai rien manqué.", "grâce — c'est une aide"),
        ("___ de l'autobus, j'ai manqué la première heure.", "à cause — un ennui"),
        ("___ à votre message, j'ai compris à temps.", "grâce — une aide"),
    ], corrige=True,
       notes="Faire dire à voix haute pourquoi c'est un ennui ou une aide, avant de "
             "choisir. Le sens vient d'abord, la forme suit : c'est l'inverse du reste "
             "du module.")

    d.piege("Mettre une phrase après « à cause de »",
            "Je serai absente à cause de mon fils est malade.",
            "Je serai absente parce que mon fils est malade.",
            "Après « à cause de », il faut un nom seul : « à cause de mon "
            "fils ». Si vous voulez la phrase entière, employez « parce que ». "
            "C'est la faute la plus fréquente du module.",
            notes="Donner la sortie de secours : dans le doute, « parce que » convient "
                  "toujours. Un élève qui n'emploie que « parce que » ne fait jamais de "
                  "faute de construction.")

    d.regle("La cause s'entend même sans mot",
            "Je ne viens pas ce matin ; mon fils est malade.",
            precision="Deux phrases collées, et tout le monde comprend. Mais "
                      "à l'écrit, dans une note, mettez le « parce que ».",
            notes="Ce n'est pas une permission de tout laisser tomber : c'est une "
                  "reconnaissance de ce que le groupe fait déjà à l'oral, et qui n'est "
                  "pas fautif. La note écrite, elle, demande le connecteur.")

    d.billet(
        "Écrivez trois phrases : une avec « parce que », une avec « à cause "
        "de », une avec « grâce à ».",
        exemples=[
            "Des choses vraies, de votre semaine.",
            "Vérifiez la contraction : du, des, au, aux.",
        ],
        notes="Ramasser. Les phrases avec « grâce à » sont souvent les plus belles du "
              "module : en lire deux ou trois à voix haute au début de C3.")

    return d.save(dossier)
