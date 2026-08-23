# -*- coding: utf-8 -*-
"""D1 · Trois questions, trois portes
Bloc D « Défi 3 · Quand ce n'est pas écrit publicité » · acier · 75 min.
Source : dialogue `t3`, exercices `t3vf`, `t3fiche` et `t3ou`.
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n7-publicite' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Trois questions, trois portes",
        chapeau="Les publicités les plus efficaces ne ressemblent pas à des "
                "publicités. Chacune des trois situations de cette séance est "
                "encadrée par une règle, et chacune a sa porte.",
        duree='75 minutes')

    d.titre(notes="Première séance du Défi 3, et la plus dense en faits. Prévoir de "
                  "donner les trois règles lentement : ce sont des chiffres et des "
                  "dates, et les élèves les noteront.")

    d.objectifs([
        "reconnaître une publicité qui ne se présente pas comme telle ;",
        "savoir ce qu'exige un témoignage employé en publicité ;",
        "connaître l'interdiction qui vise les moins de treize ans ;",
        "nommer les trois organismes et ce que chacun reçoit.",
    ], notes="Le quatrième objectif est celui qui rend le module utile hors de la "
             "classe : se tromper de porte fait perdre des semaines.")

    d.declencheur(
        'Observation', "Est-ce une publicité ?",
        image=IMG + 'televiseur-salon.jpg',
        pistes=[
            "Une personne montre un objet qu'on lui a envoyé, et donne un code.",
            "Rien n'indique nulle part qu'il s'agit d'une annonce.",
            "Est-ce que ça change quelque chose que ce soit gratuit ?",
            "Et si l'enfant qui regarde a onze ans ?",
        ],
        notes="Les deux dernières questions sont les deux règles de la séance. "
              "Laisser le groupe hésiter : c'est exactement l'hésitation que les "
              "règles servent à trancher.")

    d.dialogue('Dialogue · 1 de 3', "Ils me l'ont envoyée", [
        ("VALERIA", "Maman, la trottinette est bleue, elle monte les côtes, et elle est presque gratuite.", True),
        ("YAMILÉ", "Presque gratuite ? Tu as vu ça où ?", True),
        ("VALERIA", "Dans une vidéo. Il dit qu'on peut avoir la même avec son code. Il dit qu'ils la lui ont envoyée.", True),
        ("YAMILÉ", "Ils. Qui, ils ?", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="La dernière réplique est le point de départ de la séance D2. La noter "
             "au tableau et l'y laisser.")

    d.dialogue('Dialogue · 2 de 3', "Une annonce doit se dire annonce", [
        ("MAXIME", "Si la personne a reçu quelque chose en échange, oui, c'est de la publicité, quelle que soit la forme.", True),
        ("MAXIME", "Et une publicité doit se présenter comme telle. Une annonce qui se déguise en opinion personnelle, ça ne se fait pas.", True),
        ("YAMILÉ", "Il n'y a rien d'écrit dans la vidéo. Nulle part.", True),
        ("MAXIME", "Alors la commandite n'est pas divulguée, et c'est signalable.", True),
    ], notes="Fait vérifié, à donner tel quel : le Code canadien des normes de la "
             "publicité interdit à son article deux qu'une annonce cache qu'elle en "
             "est une.")

    d.dialogue('Dialogue · 3 de 3', "Moins de treize ans", [
        ("MAXIME", "Au Québec, la publicité commerciale destinée aux personnes de moins de treize ans est interdite.", True),
        ("YAMILÉ", "Mais la vidéo ne dit pas qu'elle est pour les enfants.", True),
        ("MAXIME", "Elle n'a pas besoin de le dire. La loi regarde le but, la façon de présenter, et le moment et l'endroit.", True),
        ("MAXIME", "Une trottinette de couleur vive, essayée en riant, diffusée après l'école — vous voyez le raisonnement.", True),
    ], notes="Fait vérifié : l'interdiction est unique en Amérique du Nord, et ce "
             "n'est pas une ligne directrice. Les trois critères sont ceux de la loi, "
             "et l'intention déclarée de l'annonceur n'en fait pas partie.")

    d.regle("La loi ne demande pas ce qu'on voulait viser",
            "Trois éléments décident si une publicité est destinée aux "
            "enfants : le but, la façon de la présenter, le moment et "
            "l'endroit où elle paraît.",
            precision="L'intention déclarée par l'annonceur n'entre pas dans cet "
                      "examen. C'est ce qui rend la règle applicable : personne n'a "
                      "jamais déclaré viser les enfants.",
            notes="Diapositive à photographier. La précision est la partie utile : "
                  "sans elle, la règle paraîtrait facile à contourner.")

    d.tableau('Analyse', "Trois portes, et ce qui passe par chacune",
              ['La situation', 'À qui s\'adresser'],
              [["Prix annoncé, frais cachés", "Office de la protection du consommateur"],
               ["Publicité aux moins de 13 ans", "Office de la protection du consommateur"],
               ["Annonce déguisée, témoignage", "Normes de la publicité"],
               ["Comparaison sans fondement", "Normes de la publicité"],
               ["Langue d'une enseigne", "Office québécois de la langue française"]],
              cle=0,
              notes="Diapositive à photographier. Trois organismes seulement, et ils "
                    "ne se marchent pas sur les pieds. Rien n'empêche de s'adresser "
                    "à deux d'entre eux.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après l'appel.", [
        ("Une vidéo payée doit annoncer qu'elle est payée.", "vrai"),
        ("Recevoir un produit gratuitement n'est pas une contrepartie.", "faux - c'en est une"),
        ("La publicité aux moins de treize ans est interdite au Québec.", "vrai"),
        ("La loi demande à l'annonceur quel public il visait.", "faux - elle regarde trois éléments"),
        ("Un témoignage peut refléter une opinion que la personne n'a plus.", "faux - opinion actuelle"),
        ("Une seule organisation reçoit les trois plaintes.", "faux - trois portes"),
    ], corrige=True,
       notes="Exercice `t3vf` du module. Le deuxième item est celui qui surprend : "
             "un produit reçu est une contrepartie au même titre qu'un paiement.")

    d.billet(
        "Trouvez une vidéo ou une publication qui présente un produit, et cherchez la mention de commandite.",
        exemples=[
            "Y a-t-il un mot qui dit que c'est une publicité ?",
            "Où est-il placé : au début, à la fin, dans les commentaires ?",
        ],
        notes="Devoir d'observation. La position de la mention est instructive : "
              "au début, elle informe ; à la fin, beaucoup moins.")

    return d.save(dossier)
