# -*- coding: utf-8 -*-
"""B1 · L'extrait : entendre ce qu'il ne pense pas
Bloc B « Défi 1 » · couleur acier · compréhension orale · 75 min.
Source : dialogue `t1`, exercice `t1vf`.
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n7-oeuvres' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="« J'adore ça, attendre »",
        chapeau="Un humoriste dit qu'il adore attendre, et personne ne le "
                "croit. Comprendre un sketch, ce n'est pas comprendre les "
                "mots : c'est entendre l'écart entre le mot et la pensée.",
        duree='75 minutes')

    d.titre(notes="Première séance du Défi 1. Faire écouter l'extrait en entier avant "
                  "toute explication, diapositive masquée. La classe rira ou ne rira "
                  "pas, et c'est déjà l'objet de la séance.")

    d.objectifs([
        "comprendre un sketch humoristique entendu ;",
        "reconnaître l'ironie à l'écart entre ce qui est dit et ce qui est vrai ;",
        "nommer ce qui fait rire au lieu de dire « c'était drôle » ;",
        "dire à quel moment on a ri, et pourquoi à ce moment-là.",
    ], notes="Le quatrième objectif est celui qui prépare D1 : Marilou et Gaétan "
             "n'ont pas ri en même temps, et c'est devenu l'argument du comité.")

    d.declencheur(
        'Observation', "Est-ce qu'on rit des mêmes choses partout ?",
        image=IMG + 'scene-de-bar.jpg',
        pistes=[
            "Qu'est-ce qui fait rire dans votre langue première ?",
            "Avez-vous déjà ri en retard, parce qu'il fallait traduire ?",
            "Avez-vous déjà été le seul à ne pas rire dans une salle ?",
            "Est-ce qu'on peut trouver un spectacle bon sans en rire ?",
        ],
        notes="La troisième piste touche presque tout le monde et elle est "
              "inconfortable : la nommer d'entrée enlève la honte. La quatrième "
              "ouvre le module : oui, on peut, et c'est ce que Marilou fera.")

    d.dialogue('Extrait · 1 de 3', "Trente ans au comptoir", [
        ("RÉJEAN", "Moi, j'ai fait trente ans au comptoir des pièces. Trente ans.", True),
        ("RÉJEAN", "Et savez-vous ce que j'aime le plus dans la vie ? Attendre. J'adore ça, attendre.", True),
        ("RÉJEAN", "Le monde arrive, ils prennent un petit numéro, ils s'assoient, puis ils me regardent. Moi je les regarde. On se regarde.", True),
        ("RÉJEAN", "C'est beau, hein ? On appelle ça le service à la clientèle.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Après l'écoute, une seule question : est-ce qu'il aime attendre ? "
             "Laisser le désaccord s'installer dans la classe avant de trancher.")

    d.dialogue('Extrait · 2 de 3', "La madame et la réponse", [
        ("RÉJEAN", "Il y a une madame, l'autre jour, elle attendait depuis quarante minutes.", True),
        ("RÉJEAN", "Elle se lève, elle vient me voir, puis elle me dit : « Monsieur, ça fait quarante minutes. »", True),
        ("RÉJEAN", "Je lui réponds : « Madame, moi ça fait trente ans. »", True),
    ], notes="C'est la première chute, et le seul moment où Marilou et Gaétan rient "
             "ensemble. Le faire remarquer : elle est courte, elle ne s'explique pas, "
             "et rien ne vient après.")

    d.dialogue('Extrait · 3 de 3', "C'est dans le système", [
        ("RÉJEAN", "Là, mon gérant arrive. Un jeune homme très bien, très propre, une chemise bleue.", True),
        ("RÉJEAN", "Il regarde son écran, puis il dit la plus belle phrase de la langue française : « C'est dans le système. »", True),
        ("RÉJEAN", "La pièce n'est pas là, mais elle est dans le système. Elle est heureuse, dans le système.", True),
        ("RÉJEAN", "Trente ans, j'ai cherché le système. Je ne l'ai jamais trouvé.", True),
    ], notes="Trois procédés en quatre répliques : caricature du gérant, "
             "personnification de la pièce, absurde de la recherche. Ne pas les "
             "nommer aujourd'hui : c'est le travail de B2.")

    d.tableau('Analyse', "Ce qui est dit, ce qui est pensé",
              ['Ce qu\'il dit', 'Ce qu\'il pense'],
              [["J'adore ça, attendre",
                "trente ans d'attente lui ont coûté quelque chose"],
               ["On appelle ça le service",
                "ce n'est pas un service, c'est une salle d'attente"],
               ["Elle est heureuse, dans le système",
                "la pièce n'existe que sur un écran, et le client repart sans rien"]],
              cle=0,
              note="Aucun de ces écarts n'est signalé : c'est au public de rétablir.",
              notes="Diapositive à photographier. Le tableau est le cœur de la "
                    "séance : deux colonnes, et le rire vit entre les deux.")

    d.regle("L'ironie n'est pas un mensonge",
            "Elle dit le contraire de ce qu'elle pense, et elle compte sur vous "
            "pour rétablir.",
            precision="Le ton, la lenteur et la situation disent tous les trois que "
                      "c'est faux. Personne n'est trompé, et c'est ce qui distingue "
                      "l'ironie d'un mensonge : le locuteur veut être compris à "
                      "l'envers.",
            notes="Diapositive à photographier. Prévenir : le français écrit ne "
                  "marque l'ironie par aucun signe. Ni ponctuation, ni mot.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après l'extrait et la conversation.", [
        ("Réjean dit qu'il adore attendre, et il le pense vraiment.", "faux - c'est de l'ironie"),
        ("La madame attendait depuis quarante minutes.", "vrai"),
        ("Réjean imite le gérant avec une voix pointue.", "faux - il le rapporte"),
        ("Gaétan et Marilou ont ri au même moment une seule fois.", "vrai"),
        ("Marilou trouve que le spectacle est mauvais.", "faux - elle le trouve bon"),
        ("Le risque du spectacle vient du groupe de trente-huit personnes.", "vrai"),
    ], corrige=True,
       notes="Exercice `t1vf` du module. Le cinquième est le plus important : Marilou "
             "aime le spectacle et ne le propose pas. Un avis n'est pas un vote.")

    d.billet(
        "À quel moment de l'extrait avez-vous ri, et pourquoi à ce moment-là ?",
        exemples=[
            "Si vous n'avez pas ri, dites-le : c'est une réponse aussi.",
            "Nommez la phrase exacte.",
        ],
        notes="Ramasser et compter : combien de moments différents dans la classe ? "
              "Le chiffre servira en D1, quand Marilou dira qu'ils n'ont pas ri "
              "ensemble.")

    return d.save(dossier)
