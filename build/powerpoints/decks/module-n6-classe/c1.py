# -*- coding: utf-8 -*-
"""C1 · Un jeudi à la bibliothèque
Bloc C « Défi 2 » · couleur acier · 75 min. Compréhension orale.
Source du module : dialogue `t2` et exercice `t2vf`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Un jeudi à la bibliothèque",
        chapeau="Trois documents sur le même sujet, et pas un qui dise la "
                "même chose que l'autre. Aucun ne ment : ils ne font pas le "
                "même travail.",
        duree='75 minutes')

    d.titre(notes="Première séance du défi 2. Le dialogue fait vingt et une "
                  "répliques et il est construit comme une leçon dans la "
                  "leçon : la bibliothécaire pose deux questions à chaque "
                  "document, toujours les mêmes.")

    d.objectifs([
        "poser à un document les deux questions qui comptent ;",
        "distinguer une source de faits d'une source d'opinions ;",
        "noter le titre, l'auteur et la date pendant qu'on lit ;",
        "savoir ce qu'on peut recopier, et comment.",
    ], notes="La deuxième question — « qu'est-ce que cette personne veut ? » — "
             "est celle qui manque le plus souvent, et c'est elle qui rend "
             "un travail honnête.")

    d.declencheur(
        'Avant d\'écouter', "Trois documents disent trois choses différentes. Lequel croire ?",
        pistes=[
            "Le plus récent ? Le plus officiel ?",
            "Faut-il vraiment en choisir un ?",
            "Que feriez-vous des deux autres ?",
        ],
        notes="La bonne réponse — n'en choisir aucun et écrire pourquoi ils "
              "diffèrent — n'apparaît presque jamais spontanément. La "
              "laisser venir du dialogue.")

    d.dialogue('Écoute 1', "Deux questions par document", [
        ("DANIÈLE", "Alors, l'équipe du bac brun. Vous avez apporté ce que vous avez trouvé ?", False),
        ("MARISOL", "Trois documents. Mais plus on les lit, moins on comprend.", False),
        ("DANIÈLE", "C'est bon signe. Étalez-les. On va les regarder un par un, et je vais vous poser à chaque fois les deux mêmes questions : qui parle, et qu'est-ce que cette personne veut ?", True),
        ("YOUSSEF", "Le premier vient du site de la ville. C'est une page qui explique la collecte : ce qu'on met dans le bac, ce qu'on n'y met pas, et pourquoi.", False),
    ], consigne="Première écoute : quelles sont les deux questions ?",
       notes="Faire noter les deux questions au tableau et les y laisser "
             "toute la séance. Tout le reste s'y rapporte.")

    d.dialogue('Écoute 2', "La page de la ville, et le bulletin", [
        ("DANIÈLE", "Elle veut que la collecte fonctionne. Ce n'est pas un défaut, c'est un fait à savoir : cette page vous donnera très bien la liste des matières acceptées, et elle ne vous dira jamais ce qui a mal marché la première année.", True),
        ("MARISOL", "Le deuxième, c'est un article du bulletin municipal. Il raconte l'histoire de la collecte. C'est écrit d'une drôle de façon : « le conseil adopta le règlement ».", False),
        ("DANIÈLE", "Le passé simple. On ne le parle jamais et on l'écrit encore souvent, dans les historiques surtout. Traduisez-le en passé composé dans votre tête et continuez.", True),
        ("MARISOL", "J'ai buté sur une phrase. « La ville avait distribué les bacs en avril, mais la collecte ne commença qu'en juin. »", False),
    ], consigne="Deuxième écoute : quels temps de verbe sont nommés ?",
       notes="Les deux temps du défi 2 apparaissent ici : le passé simple et "
             "le plus-que-parfait. Ils seront travaillés en C5 ; ici, il "
             "s'agit de les entendre nommer.")

    d.dialogue('Écoute 3', "La lettre, et ce qu'on en fait", [
        ("YOUSSEF", "Le troisième, c'est une lettre. Une dame écrit au bulletin pour dire que le compostage ne sert à rien.", False),
        ("DANIÈLE", "Elle veut convaincre. Ce n'est pas une source de faits, c'est une source d'opinions — et vous en avez besoin, à condition de la présenter pour ce qu'elle est.", True),
        ("MARISOL", "Mais alors, laquelle des trois a raison ?", False),
        ("DANIÈLE", "Aucune ne ment. Vous les mettez côte à côte, vous notez à quel endroit elles se contredisent, et vous l'écrivez. C'est ça, votre travail — pas de choisir un gagnant.", True),
    ], consigne="Troisième écoute : que faut-il faire des contradictions ?",
       notes="C'est la réplique la plus importante du module. La faire "
             "reformuler par deux élèves avant de passer à la suite.")

    d.tableau('Analyse', "Trois documents, trois travaux",
              ['Le document', 'Ce qu\'il fait'],
              [["la page de la ville", "explique une règle et veut qu'elle soit suivie"],
               ["l'article du bulletin", "raconte ce qui est arrivé, avec des dates"],
               ["la lettre au journal", "donne un avis et veut convaincre"]],
              cle=0,
              note="Aucun ne ment. Les présenter pour ce qu'ils sont vaut huit points sur vingt.",
              notes="Diapositive à photographier. Relier explicitement à la "
                    "ligne « contenu » de la grille, vue en B3.")

    d.regle("Une opinion s'annonce comme une opinion",
            "« Selon une lectrice du bulletin, la collecte ne fonctionne pas » — jamais « il est prouvé que ».",
            precision="C'est exactement ce que la grille appelle "
                      "« distinguer ce qu'un document affirme de ce que "
                      "l'équipe en pense ».",
            notes="Diapositive à photographier. Faire transformer deux "
                  "phrases d'opinion mal présentées, à l'oral.")

    d.pratique('Pratique', "Vrai ou faux",
               "Réécoutez au besoin, puis répondez.", [
        ("Il faut se demander qui parle et ce que cette personne veut.", "vrai"),
        ("Le bulletin est écrit au passé simple parce que c'est un historique.", "vrai"),
        ("Les bacs sont arrivés en même temps que la collecte a commencé.", "faux : deux mois avant"),
        ("La lettre de la lectrice est une source de faits.", "faux : d'opinions"),
        ("L'équipe doit choisir laquelle des trois a raison.", "faux : elle écrit pourquoi elles diffèrent"),
        ("On note le titre, l'auteur et la date pendant qu'on lit.", "vrai"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `t2vf` du module. La troisième affirmation "
             "prépare le plus-que-parfait de la séance C5.")

    d.billet(
        "Nomme une de tes sources et dis ce qu'elle veut.",
        exemples=[
            "Qui parle ? Qu'est-ce que cette personne ou cet organisme veut ?",
            "Deux phrases.",
        ],
        notes="Trois minutes. Les équipes qui n'ont pas encore de source le "
              "disent ici, et il reste assez de temps pour les aider.")

    return d.save(dossier)
