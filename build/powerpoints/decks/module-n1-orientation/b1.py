# -*- coding: utf-8 -*-
"""B1 · Le mot sur la porte.
Bloc B « Défi 1 · Le mot sur la porte » · couleur acier · 75 min.
Source : dialogues `t1` et `t1b`, exercices `t1vf` et `t1lieu`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre='Le mot sur la porte',
        chapeau="Six mots à reconnaître d'un coup d'œil. Ce sont ceux qui "
                "sont écrits sur les portes de tous les centres du Québec.",
        duree='75 minutes')

    d.titre(notes="Première séance du Défi 1. Faire relire le billet de A3 avant de "
                  "commencer : les quatre premiers mots y sont déjà.")

    d.objectifs([
        "lire six noms de lieux écrits sur une porte ;",
        "dire ce qu'on fait à chacun de ces endroits ;",
        "comprendre une réponse « oui, c'est ici » ou « non, ce n'est pas ici » ;",
        "décoder un mot long syllabe par syllabe.",
    ])

    d.declencheur(
        'Observation', "Ca-fé-té-ria",
        pistes=[
            "Combien de morceaux entendez-vous dans ce mot ?",
            "Et dans « toilettes » ?",
            "Et dans « service de garde » ?",
            "Lequel est le plus long à lire ?",
        ],
        notes="Frapper les syllabes dans les mains en les disant. Le geste aide plus "
              "que l'explication à ce stade.")

    d.dialogue('Dialogue · 1 de 2', "C'est écrit sur la porte", [
        ("ROSA", "Kofi, c'est quoi, ici ?", True),
        ("KOFI", "Lis le mot. C-A-F-É…", True),
        ("ROSA", "Ca-fé-té-ria. La cafétéria !", True),
        ("KOFI", "Oui. On mange ici, à midi.", True),
        ("ROSA", "Et là ? Il y a un dessin d'enfant.", True),
        ("KOFI", "C'est le service de garde. Pour les petits.", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Le point à faire entendre : Rosa ne lit pas le mot d'un coup, elle le "
             "coupe en morceaux. C'est la bonne méthode, pas un échec.")

    d.dialogue('Dialogue · 2 de 2', "Ce n'est pas ici", [
        ("ROSA", "Madame ! C'est le service de garde, ici ?", True),
        ("MADAME PARÉ", "Non, ce n'est pas ici. Ici, c'est l'accueil.", True),
        ("ROSA", "Ah. Pardon.", True),
        ("MADAME PARÉ", "Regardez le dessin sur la porte, là-bas.", True),
    ], notes="Rosa se trompe et personne n'en fait un drame. Le dire : se tromper de "
             "porte est la chose la plus normale du monde dans un bâtiment neuf.")

    d.regle("Un mot long se lit en morceaux",
            "Une syllabe à la fois.",
            precision="<b>ca — fé — té — ria</b>. On lit chaque morceau, puis on les "
                      "remet ensemble. Personne ne lit un mot long d'un seul coup au "
                      "début, et beaucoup de gens nés ici font pareil devant un mot "
                      "qu'ils ne connaissent pas.",
            notes="Diapositive à photographier. Faire découper trois mots au tableau, "
                  "avec des traits, par des élèves différents.")

    d.vocabulaire('Vocabulaire', "Six lieux du centre",
                  [("les toilettes", "on se lave les mains"),
                   ("la cafétéria", "on mange, le midi"),
                   ("l'accueil", "on pose une question"),
                   ("le service de garde", "on laisse son enfant"),
                   ("le vestiaire", "on laisse son manteau"),
                   ("la sortie", "on part du bâtiment")],
                  notes="Faire répéter avec le petit mot. Puis faire dire à chacun "
                        "l'endroit qu'il a déjà trouvé tout seul dans le centre.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le premier dialogue.", [
        ("Rosa lit le mot « cafétéria ».", "vrai"),
        ("On mange à la cafétéria, le midi.", "vrai"),
        ("Le dessin du service de garde montre une auto.", "faux — un enfant"),
        ("La fille de Rosa a quatre ans.", "vrai"),
    ], corrige=True, cols=1,
       notes="Quatre énoncés. Faire relire le dialogue avant de corriger.")

    d.pratique('Pratique', "Le mot et l'endroit",
               "Associez chaque mot du panneau à ce qu'on y fait.", [
        ("TOILETTES", "on se lave les mains"),
        ("CAFÉTÉRIA", "on mange, le midi"),
        ("ACCUEIL", "on pose une question"),
        ("SERVICE DE GARDE", "on laisse son enfant"),
        ("VESTIAIRE", "on laisse son manteau"),
        ("SORTIE", "on part du bâtiment"),
    ], corrige=True, cols=2,
       notes="Même exercice que dans l'activité interactive. Le faire d'abord à l'oral, "
             "au tableau, avant qu'ils l'ouvrent à l'écran.")

    d.billet(
        "Écrivez le nom de deux endroits du centre, et ce qu'on y fait.",
        exemples=[
            "Exemple : la cafétéria — on mange.",
            "N'oubliez pas le petit mot devant : le, la, les.",
        ],
        notes="Deux minutes. Ce billet nourrit directement la production écrite de E1.")

    return d.save(dossier)
