# -*- coding: utf-8 -*-
"""B2 · La couleur après le vêtement.
Bloc B « Défi 1 · Demander ce qu'on cherche » · couleur ambre (écriture) · 60 min.
Source : exercice `t1adj`, mini-leçon `t1adj`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre='La couleur après le vêtement',
        chapeau="« Un manteau noir », jamais « un noir manteau ». C'est "
                "l'inverse de plusieurs langues, et c'est la première chose "
                "qu'on remarque à l'oreille.",
        duree='60 minutes')

    d.titre(notes="Séance d'écriture. Commencer en écrivant au tableau « un noir manteau » "
                  "et demander au groupe ce qui cloche. Plusieurs le sentiront sans savoir "
                  "le dire.")

    d.objectifs([
        "placer l'adjectif de couleur après le nom ;",
        "accorder la couleur au féminin et au pluriel ;",
        "connaître les couleurs qui ne changent jamais ;",
        "savoir que « pâle » et « foncé » bloquent l'accord.",
    ])

    d.declencheur(
        'Question', "Laquelle de ces deux phrases est juste ?",
        pistes=[
            "« Je cherche un noir manteau. »",
            "« Je cherche un manteau noir. »",
            "Comment dit-on dans votre langue ?",
            "Et si la couleur était « rouge » ?",
        ],
        notes="La comparaison avec la langue d'origine est utile ici : en anglais, en "
              "arabe et en espagnol, l'ordre n'est pas le même. Le nommer aide à retenir.")

    d.tableau('Analyse', "La couleur suit le vêtement, et elle s'accorde",
              ['Le vêtement', 'La couleur'],
              [["un manteau", "noir"],
               ["une tuque", "noire — un e de plus"],
               ["des gants", "gris — le s y est déjà"],
               ["des bottes", "noires — un e et un s"]],
              cle=0,
              note="Le e s'entend souvent ; le s ne s'entend jamais, mais il s'écrit.",
              notes="Diapo centrale, à photographier. Faire lire les quatre lignes à voix "
                    "haute : la différence entre « noir » et « noire » s'entend.")

    d.regle("Quatre couleurs ne changent jamais",
            "rouge · jaune · rose · beige",
            precision="Elles finissent déjà par un e : au féminin, on n'ajoute rien. « Une "
                      "tuque <b>rouge</b> », « des mitaines <b>rouges</b> » — seul le s du "
                      "pluriel s'ajoute. Deux autres ne bougent pas du tout, parce qu'elles "
                      "viennent d'un nom de chose : <b>marine</b> (la mer) et <b>marron</b> "
                      "(le fruit).",
            notes="Diapo à photographier. « Marine » et « marron » sont fréquents sur les "
                  "étiquettes de manteaux : la remarque n'est pas théorique.")

    d.cartes("Trois cas, trois formes", "Ce qui décide", [
        ("Le vêtement est masculin",
         "Rien ne s'ajoute : <b>un manteau noir</b>, <b>un chandail vert</b>. La couleur "
         "reste comme dans le dictionnaire."),
        ("Le vêtement est féminin",
         "On ajoute un e : <b>une tuque noire</b>, <b>une jupe verte</b>. Et souvent, la "
         "consonne d'avant se met à sonner : « gri » devient « grize »."),
        ("Le vêtement est au pluriel",
         "On ajoute un s : <b>des bottes noires</b>, <b>des gants gris</b>. Il ne s'entend "
         "pas — mais une liste, une étiquette et un courriel s'écrivent."),
    ], notes="Faire produire un exemple de chaque cas par un élève différent, avec un "
             "vêtement de sa propre garde-robe.")

    d.regle("Pâle et foncé bloquent tout",
            "des mitaines <b>bleu pâle</b>, un manteau <b>gris foncé</b>",
            precision="Dès qu'une nuance s'ajoute, l'ensemble ne s'accorde plus : ni la "
                      "couleur, ni la nuance. On écrit « des mitaines bleu pâle », et non "
                      "« des mitaines bleues pâles ». C'est une règle vraie et souvent "
                      "ignorée, même par des gens d'ici.",
            notes="Diapo à photographier. Ne pas en faire un drame : personne ne bloquera "
                  "pour cela, mais l'écrire juste vaut mieux.")

    d.piege("Accorder une couleur en e",
            "une tuque rougee",
            "une tuque rouge",
            "Rouge, jaune, rose et beige finissent déjà par un e. Au féminin, on n'ajoute "
            "rien du tout ; au pluriel, on n'ajoute que le s. L'erreur vient de "
            "l'application mécanique de la règle du e.",
            notes="Faire relire les quatre couleurs à voix haute avant l'exercice.")

    d.pratique('Pratique', "Complétez avec la bonne forme",
               "L'adjectif est entre parenthèses.", [
        ("Je cherche un manteau ___ . (noir)", "noir"),
        ("Elle porte une tuque ___ . (gris)", "grise"),
        ("Il achète des bottes ___ . (brun)", "brunes"),
        ("Voici un chandail ___ . (vert)", "vert"),
        ("Je veux une jupe ___ . (rouge)", "rouge"),
        ("Ce sont des mitaines ___ . (bleu)", "bleues"),
    ], corrige=True,
       notes="Utiliser l'exercice 2 du défi 1. Faire justifier chaque réponse par le genre "
             "et le nombre du vêtement, pas par l'oreille.")

    d.billet(
        "Écrivez six vêtements de votre garde-robe, avec leur couleur.",
        exemples=[
            "Trois masculins, trois féminins.",
            "Au moins un au pluriel, et au moins une couleur en e.",
        ],
        notes="Ramasser. Les erreurs d'accord se corrigent une fois ici et ne reviennent "
              "presque plus dans la production écrite de E1.")

    return d.save(dossier)
