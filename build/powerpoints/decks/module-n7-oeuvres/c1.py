# -*- coding: utf-8 -*-
"""C1 · L'entrevue : ce que la chanson ne dit pas
Bloc C « Défi 2 » · couleur acier · compréhension orale · 75 min.
Source : dialogue `t2`, exercice `t2vf`.
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n7-oeuvres' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="« Elle parle d'un escalier »",
        chapeau="Une chanson dit deux choses en même temps : celle qu'on voit, "
                "et celle qu'elle ne nomme jamais. L'auteure refuse de nommer "
                "la seconde, et elle explique pourquoi.",
        duree='75 minutes')

    d.titre(notes="Première séance du Défi 2. Faire entendre la chanson avant "
                  "l'entrevue si l'on dispose du module ; sinon, lire les paroles à "
                  "voix haute, lentement, sans commentaire.")

    d.objectifs([
        "comprendre une entrevue de radio sur une œuvre ;",
        "distinguer ce qu'une chanson montre de ce qu'elle veut dire ;",
        "reconnaître une image : une chose nommée pour une autre ;",
        "comprendre pourquoi une auteure choisit de ne pas nommer.",
    ], notes="Le quatrième objectif est le plus difficile et le plus intéressant. "
             "Beaucoup d'élèves cherchent la bonne réponse ; ici, il n'y en a pas, "
             "et c'est voulu par l'auteure.")

    d.declencheur(
        'Observation', "Qu'est-ce que cette photo raconte ?",
        image=IMG + 'escalier-en-colimacon.jpg',
        pistes=[
            "Que voyez-vous exactement, sans interpréter ?",
            "Maintenant : qu'est-ce que ça vous fait penser ?",
            "Est-ce que vos deux réponses sont la même ?",
            "Est-ce qu'on peut se tromper sur la deuxième ?",
        ],
        notes="L'exercice de la séance en petit : d'abord ce qui se voit, ensuite ce "
              "qu'on met dessous. La quatrième piste est la vraie question du bloc, "
              "et la réponse honnête est « pas vraiment ».")

    d.dialogue('Entrevue · 1 de 3', "De quoi ça parle", [
        ("LUDOVIC", "On vient de faire entendre « Le troisième étage ». De quoi est-ce qu'elle parle, au juste ?", True),
        ("NADIA", "Elle parle d'un escalier.", True),
        ("NADIA", "D'un escalier extérieur en colimaçon, et d'une femme qui monte trois étages avec ses sacs d'épicerie. C'est tout ce qui se passe.", True),
        ("LUDOVIC", "Pourtant, quand on l'écoute, on n'a pas l'impression que ça parle d'épicerie.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire remarquer la réponse en quatre mots. C'est une réponse complète "
             "et honnête : la chanson parle bien d'un escalier.")

    d.dialogue('Entrevue · 2 de 3', "La deuxième chose", [
        ("NADIA", "Une chanson dit deux choses en même temps. La première, on la voit : les sacs, la neige sur la marche, la fenêtre allumée en haut.", True),
        ("NADIA", "La deuxième, on ne la nomme jamais.", True),
        ("LUDOVIC", "Et la deuxième, c'est quoi ?", True),
        ("NADIA", "Si je vous la dis, elle cesse d'être la deuxième.", True),
    ], notes="La réplique clé du bloc. La laisser au tableau : elle explique pourquoi "
             "aucun exercice du module ne demande « que veut dire la chanson ».")

    d.dialogue('Entrevue · 3 de 3', "Ils, et le refrain trop haut", [
        ("LUDOVIC", "Il y a ce passage : « ils ont refait la rampe, ils n'ont rien refait d'autre ». Ils, c'est qui ?", True),
        ("NADIA", "Ceux qui décident et qu'on ne rencontre pas. Si j'avais écrit « le propriétaire », la chanson serait devenue une plainte.", True),
        ("LUDOVIC", "Le refrain monte très haut à la fin. Trop haut, m'ont dit deux personnes.", True),
        ("NADIA", "Il monte tellement haut que je le manque une fois sur trois. Mais une femme qui monte trois étages avec ses sacs est essoufflée.", True),
    ], notes="Deux points pour la suite : le « ils » sans référent, travaillé en C3, "
             "et le défaut assumé, qui servira d'exemple de nuance en D2.")

    d.tableau('Analyse', "Ce qui se voit, ce qui ne se voit pas",
              ['Dans la chanson', 'De quel côté'],
              [["Les sacs, la glace, la fenêtre",
                "ça se filme : c'est le premier degré"],
               ["Le troisième étage a des idées",
                "ça ne se filme pas : un escalier ne pense pas"],
               ["La boîte de carton depuis neuf ans",
                "ça se filme, et ça porte pourtant la seconde chose"]],
              cle=0,
              note="La troisième ligne est la plus intéressante : un objet réel qui dit autre chose.",
              notes="Diapositive à photographier. Faire chercher au groupe d'autres "
                    "objets de la chanson qui basculent dans la troisième catégorie.")

    d.regle("Ce qu'on ne nomme pas reste ouvert",
            "Nommer le propriétaire aurait fait de la chanson une plainte, et "
            "une plainte se règle.",
            precision="C'est un choix d'écriture, pas une cachotterie. Une image "
                      "ouverte laisse chacun mettre dessous ce qu'il connaît, et "
                      "c'est pour cela qu'une même chanson touche des gens dont les "
                      "vies n'ont rien en commun.",
            notes="Diapositive à photographier. La phrase répond d'avance à la "
                  "question « mais quelle est la bonne réponse ? ».")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après l'entrevue.", [
        ("Nadia Ferron dit que sa chanson parle d'un escalier.", "vrai"),
        ("Elle explique en ondes ce que la chanson veut dire en profondeur.", "faux - elle refuse"),
        ("Elle a vécu neuf ans au troisième étage sans ascenseur.", "vrai"),
        ("La chanson dit clairement qui a refait la rampe.", "faux - jamais"),
        ("Elle reconnaît manquer la note haute une fois sur trois.", "vrai"),
        ("Le sous-sol de l'église compte cent vingt places.", "vrai"),
    ], corrige=True,
       notes="Exercice `t2vf` du module. Le deuxième déçoit toujours quelqu'un : "
             "profiter du moment pour dire qu'une œuvre n'a pas de corrigé.")

    d.billet(
        "Nommez une chanson qui parle d'autre chose que de ce qu'elle raconte.",
        exemples=[
            "Dans n'importe quelle langue.",
            "Dites ce qu'elle raconte, puis ce qu'elle veut dire selon vous.",
        ],
        notes="Devoir qui marche très bien : chaque élève en a une, et les réponses "
              "font entendre à la classe des répertoires qu'elle ne connaît pas.")

    return d.save(dossier)
