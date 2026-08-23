# -*- coding: utf-8 -*-
"""A4 · Le fait, l'interprétation, le jugement — et redire autrement
Bloc A « Je découvre » · couleur ambre · 75 min.
Source : exercices `prFait`, `prImpl` et `prRefor`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="Trois opérations, et comment redire celle des autres",
        chapeau="« Elle s'assoit, elle renonce, et franchement c'est raté. » "
                "Une phrase, trois opérations complètement différentes — et "
                "personne ne les entend passer.",
        duree='75 minutes')

    d.titre(notes="Séance charnière du bloc A. Tout le module en dépend : un cercle qui "
                  "confond les trois opérations discute d'un jugement sans s'être "
                  "entendu sur les faits.")

    d.objectifs([
        "trancher entre fait, interprétation et jugement en deux secondes ;",
        "reconnaître une interprétation déguisée en fait ;",
        "nommer ce qu'une phrase laisse entendre sans le dire ;",
        "reformuler avec « autrement dit », « c'est-à-dire », « si je vous suis bien ».",
    ], notes="Le deuxième objectif est le plus difficile, et le plus utile hors du "
             "cours : « elle a l'air fâchée » se dit comme un fait et n'en est pas un.")

    d.declencheur(
        'Observation', "Combien de choses différentes y a-t-il dans cette phrase ?",
        pistes=[
            "« Elle s'assoit dans la chaloupe, elle renonce à partir, et cette fin est ratée. »",
            "Laquelle peut-on vérifier en revoyant la scène ?",
            "Laquelle ajoute quelque chose que l'œuvre ne montre pas ?",
            "Laquelle dit si c'est bon ou mauvais ?",
        ],
        notes="Écrire la phrase au tableau et la découper à la craie sous les yeux du "
              "groupe. Le découpage physique fait plus que l'explication.")

    d.tableau('Analyse', "Trois questions, dans cet ordre",
              ['La question', 'Si oui'],
              [["Puis-je le vérifier en revoyant ?", "c'est un fait"],
               ["Est-ce que j'ajoute quelque chose ?", "c'est une interprétation"],
               ["Est-ce que je dis bon ou mauvais ?", "c'est un jugement"]],
              cle=1,
              note="Les poser dans cet ordre : la première élimine la moitié des cas.",
              notes="Diapositive à photographier. C'est l'outil que l'élève emportera ; "
                    "tout le reste de la séance sert à l'exercer.")

    d.piege('Piège', "« Elle est triste »",
            "« Elle ne lève pas les yeux »",
            "Une émotion n'est jamais un fait. On voit un visage, on déduit un "
            "sentiment, et la déduction se fait si vite qu'on croit avoir vu la "
            "tristesse. Presque toutes les phrases d'un cercle de lecture sont "
            "des interprétations déguisées en descriptions, et c'est ce qui rend "
            "les discussions confuses : deux personnes croient parler du même "
            "fait et parlent déjà de deux lectures.",
            notes="Faire chercher au groupe trois autres exemples du même moule : "
                  "« il hésite », « elle ment », « il s'en fiche ». Chacun est une "
                  "déduction présentée comme une observation.")

    d.piege('Piège', "« Évidemment, elle renonce »",
            "« Elle laisse sonner le téléphone : je comprends qu'elle renonce »",
            "« Évidemment », « clairement », « manifestement » font passer une "
            "interprétation pour un fait sans rien prouver. Ce sont des mots de "
            "pression, pas des mots de preuve. Quand vous en entendez un, "
            "cherchez le détail qui suit : s'il n'y en a pas, il n'y a rien.",
            notes="Le dire sans sévérité : tout le monde emploie ces adverbes, "
                  "l'enseignante comprise. Ce qui compte est de les entendre.")

    d.cartes('Analyse', "Ce qui est dit, ce qui est entendu", [
        ("« On avait commencé sans elle. »", "sa présence n'était pas nécessaire"),
        ("« Il l'appela deux fois Ginette. »", "trente et un ans n'ont pas suffi"),
        ("« On ne le corrigea pas. »", "personne d'autre ne savait son nom"),
        ("« Elle avait oublié ses lunettes. »", "elle refuse de lire, et le cache"),
        ("« La banquette de droite est chaude pour rien. »", "quelqu'un s'y asseyait"),
        ("« Vous passez la corde sous silence. »", "vous évitez ce qui vous gêne"),
    ], notes="Exercice `prImpl` du module. Les six colonnes de droite ne sont écrites "
             "nulle part dans les textes : c'est le lecteur qui les apporte. Le faire "
             "remarquer une fois, à la fin.")

    d.regle("Reformuler prouve qu'on a compris",
            "Répéter les mots de l'autre prouve qu'on a entendu ; les remplacer "
            "prouve qu'on a compris.",
            precision="Le test est simple : la personne citée doit pouvoir approuver "
                      "votre phrase d'un signe de tête, sans rien corriger. Si elle "
                      "doit corriger, vous avez ajouté quelque chose — et ce n'est "
                      "plus une reformulation.",
            notes="Diapositive à photographier. C'est aussi une attente de fin de "
                  "cours du niveau 8 : l'adulte résume les propos de son "
                  "interlocuteur pour vérifier l'information reçue.")

    d.tableau('Analyse', "Quatre connecteurs, quatre usages",
              ['Le connecteur', 'Ce qu\'il fait'],
              [["Autrement dit", "redit la même chose avec d'autres mots"],
               ["C'est-à-dire", "précise : ce qui suit est plus étroit"],
               ["En somme", "rassemble plusieurs éléments en un seul"],
               ["Si je vous suis bien", "fait confirmer, et finit sur une question"]],
              cle=0,
              note="Le dernier est le plus utile : il rend la parole à l'autre.",
              notes="Diapositive à photographier. Faire produire une phrase de chaque "
                    "sorte, en dyades, à partir d'une réplique du dialogue `prep`.")

    d.pratique('Pratique', "Quel connecteur ?",
               "Complétez.", [
        ("Chacun raconte, puis chacun note. ___, on ne lit jamais.", "Autrement dit"),
        ("Elle prend le fond, ___ la table des stagiaires.", "c'est-à-dire"),
        ("Deux lectures, trois indices : ___, une bonne soirée.", "en somme"),
        ("___, vous y voyez un piège plutôt qu'un choix ?", "Si je vous suis bien"),
        ("Il n'a rien vérifié ; ___ termes, il l'écrit sans le savoir.", "en d'autres"),
        ("Elle a refusé, ___ elle a demandé à quelqu'un d'autre.", "c'est-à-dire"),
    ], corrige=True,
       notes="Exercice `prRefor` du module. Le piège habituel est de mettre « en "
             "somme » devant une précision : le contrôle est la longueur, ce qui suit "
             "« en somme » doit être plus court que ce qui précède.")

    d.billet(
        "Écoutez la personne à côté de vous pendant deux minutes, puis "
        "reformulez ce qu'elle a dit en une phrase commençant par « si je vous "
        "suis bien ». Elle approuve ou elle corrige.",
        exemples=[
            "Sujet libre : une œuvre, une semaine, un souvenir.",
            "Une seule règle : rien de neuf ne doit entrer dans votre phrase.",
        ],
        notes="Exercice à faire en classe, debout, pas à la maison. Les corrections "
              "sont immédiates et le groupe rit — c'est le meilleur moment du bloc A.")

    return d.save(dossier)
