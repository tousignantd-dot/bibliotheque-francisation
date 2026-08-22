# -*- coding: utf-8 -*-
"""C1 · Au comptoir, avec Nadia
Bloc C « Défi 2 · Lire une bande dessinée » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t2a`.
"""
import pathlib

from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-oeuvres/images/')


def photo(nom):
    """La photo si elle est sur le disque, None sinon — voir a1.py."""
    p = pathlib.Path(IMG + nom)
    return str(p) if p.exists() else None


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Au comptoir, avec Nadia",
        chapeau="Mai n'a jamais lu de bande dessinée. Elle ne sait pas "
                "comment ça se lit, ni comment on appelle ce qu'elle voit. "
                "Nadia Ferland tient le comptoir depuis douze ans et "
                "explique ces mots-là tous les jours : une case, une bulle, "
                "une planche, un album.",
        duree='75 minutes')

    d.titre(notes="Première séance du défi 2. Apporter deux ou trois albums de la "
                  "bibliothèque et les faire circuler avant de commencer. Beaucoup "
                  "d'élèves n'en ont jamais tenu ; d'autres en ont lu toute leur enfance "
                  "dans leur langue. Les seconds expliqueront aux premiers mieux que "
                  "l'enseignante.")

    d.objectifs([
        "nommer une case, une bulle, une planche, une onomatopée, un album ;",
        "savoir dans quel ordre se lit une planche ;",
        "reconnaître une bulle de parole et une bulle de pensée ;",
        "demander un conseil au comptoir en disant ce qu'on aime.",
    ], notes="Le quatrième objectif est le vrai travail de conversation du défi. Un "
             "bibliothécaire ne conseille rien avant d'avoir compris ce que la personne "
             "aime : c'est à l'élève de le dire d'abord, et il faut lui apprendre.")

    d.declencheur(
        'Observation', "Une page découpée en petits carrés. Vous la lisez "
                       "dans quel ordre ?",
        image=photo('planche-ouverte.jpg'),
        pistes=[
            "Par où commencez-vous : en haut à gauche, au milieu, au plus gros carré ?",
            "Dans un carré, quel texte lisez-vous en premier ?",
            "Et le gros mot en travers, qui n'est dans aucune bulle ?",
            "Comment savez-vous qui parle ?",
        ],
        notes="Faire répondre plusieurs élèves : les habitudes diffèrent, surtout chez "
              "ceux dont la première langue s'écrit de droite à gauche. La règle "
              "française — de gauche à droite, puis la rangée en dessous — n'a rien "
              "d'évident et mérite d'être dite.")

    d.dialogue('Dialogue · 1 de 3', "La case et la planche", [
        ("MAI", "Nadia, je voudrais essayer une bande dessinée. Je n'en ai "
                "jamais lu.", True),
        ("NADIA", "Jamais ? Alors on commence par les mots. Voyez ce carré, ici.", True),
        ("MAI", "Le petit cadre avec le dessin dedans ?", True),
        ("NADIA", "Ça s'appelle une case. La page complète, c'est une planche.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Écrire les deux mots au tableau tout de suite et les faire montrer du doigt "
             "sur un album réel. Le geste fixe le mot bien mieux que la répétition — "
             "c'est le principe de toute la séance.")

    d.dialogue('Dialogue · 2 de 3', "La bulle, et sa pointe", [
        ("MAI", "Et ce rond blanc avec le texte ?", True),
        ("NADIA", "Une bulle. Celle qui a une pointe vers un personnage, "
                  "c'est lui qui parle.", True),
        ("MAI", "Et quand la pointe est en petits ronds ?", True),
        ("NADIA", "Alors le personnage ne parle pas : il pense. C'est différent.", True),
    ], notes="La bulle de pensée est l'information la plus utile de la séance : sans elle, "
             "on croit que le personnage a dit tout haut ce qu'il gardait pour lui, et "
             "l'histoire ne se tient plus. Faire chercher un exemple dans les albums.")

    d.dialogue('Dialogue · 3 de 3', "L'album, le tome, la série", [
        ("MAI", "Ce livre-là est épais. Il y a une suite ?", True),
        ("NADIA", "C'est un album. Celui que vous tenez est le premier tome "
                  "d'une série.", True),
        ("MAI", "Donc l'album, la bande dessinée, l'histoire… c'est la même chose ?", True),
        ("NADIA", "Presque. L'album, c'est l'objet ; l'histoire, c'est ce qu'il "
                  "y a dedans.", False),
    ], notes="La dernière réplique reprend la distinction de la séance A3 — l'objet et son "
             "contenu — et annonce la séance C4, où elle devient un outil : c'est ce qui "
             "permet de changer de mot sans changer de sujet.")

    d.regle("Du plus petit au plus grand",
            "Une bulle tient dans une case, une case tient dans une planche, "
            "une planche tient dans un album.",
            precision="Retenez l'ordre et vous ne vous tromperez plus jamais : bulle, "
                      "case, planche, album. Le tome est le numéro de l'album dans une "
                      "suite, et la série est l'ensemble. Six mots, et vous parlez la "
                      "langue du comptoir.",
            notes="Diapositive à photographier. Faire redire l'ordre à voix haute par tout "
                  "le groupe, deux fois. C'est le genre de liste qui s'installe en trente "
                  "secondes et qui tient des années.")

    d.tableau('Comment on lit une planche', "Une seule règle, et trois conséquences",
              ['Ce qu\'on se demande', 'La réponse'],
              [["Par où je commence ?", "En haut à gauche, comme un texte ordinaire."],
               ["Et ensuite ?", "Vers la droite, puis la rangée en dessous."],
               ["Dans une case, quelle bulle d'abord ?", "La plus haute et la plus à gauche."],
               ["Qui parle ?", "Suivez la pointe de la bulle : elle mène à une bouche."],
               ["Et le bruit en grosses lettres ?", "Il n'est dit par personne : c'est la scène."]],
              cle=1,
              notes="Faire appliquer les cinq lignes sur une planche réelle, album ouvert "
                    "sur le bureau, un élève qui montre du doigt pendant que les autres "
                    "disent l'ordre. Cinq minutes, et la lecture est acquise.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Le petit cadre avec un dessin s'appelle une case.", "vrai"),
        ("La page complète s'appelle une bulle.", "faux — une planche"),
        ("La pointe de la bulle montre qui parle.", "vrai"),
        ("Une pointe en petits ronds veut dire que le personnage crie.", "faux — il pense"),
        ("On lit de gauche à droite, puis la rangée en dessous.", "vrai"),
        ("Une onomatopée se place à l'intérieur d'une bulle.", "faux — en dehors"),
        ("L'album que Mai emprunte est le premier tome d'une série.", "vrai"),
        ("On garde une bande dessinée pendant trois semaines.", "vrai"),
    ], corrige=True,
       notes="C'est l'exercice `t2a` du module interactif. La dernière ligne est une "
             "information pratique qui vaut la peine d'être vérifiée avec la bibliothèque "
             "du quartier : la durée du prêt varie d'un réseau à l'autre.")

    d.billet(
        "Écrivez les cinq mots de la bande dessinée, du plus petit au plus grand.",
        exemples=[
            "Ajoutez à côté de chacun ce qu'il désigne, en trois ou quatre mots.",
            "Nommez un mot que vous employez dans votre première langue pour la même chose.",
        ],
        notes="La deuxième consigne fait remonter des comparaisons intéressantes et donne "
              "une place à ceux qui lisaient de la bande dessinée avant d'arriver ici. "
              "Lire deux ou trois billets au début de C2.")

    return d.save(dossier)
