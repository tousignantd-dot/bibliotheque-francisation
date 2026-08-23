# -*- coding: utf-8 -*-
"""D2 · Une critique qu'on discute sans avoir vu la pièce
Bloc D « Défi 3 · Défendre une lecture » · couleur ambre · 75 min.
Source : exercices `t3crit` (type `texte`), `t3rel`, `t3cit` et `t3resu`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="Une critique qu'on discute sans avoir vu la pièce",
        chapeau="Personne au cercle n'a vu « Le troisième rang ». Personne ne "
                "peut donc dire si le critique a raison. Tout le monde peut "
                "dire si son texte tient.",
        duree='75 minutes')

    d.titre(notes="Dernière séance avant les productions. C'est aussi la plus "
                  "transférable du module : on lit des critiques toute sa vie, et "
                  "presque jamais en ayant vu l'œuvre.")

    d.objectifs([
        "distinguer dans une critique ce qui décrit, ce qui juge, ce qui devine ;",
        "citer un passage avec « dont », « auquel », « sur lequel » ;",
        "distinguer citer, résumer et déformer ;",
        "choisir un verbe introducteur neutre quand on veut être cru.",
    ], notes="Le premier objectif est le cœur ; les trois autres sont les outils de "
             "langue qui permettent d'y répondre par écrit en E2.")

    d.declencheur(
        'Préparation', "Peut-on discuter d'une critique sans avoir vu l'œuvre ?",
        pistes=[
            "Qu'est-ce qu'on ne peut pas faire ? Dire s'il a raison.",
            "Qu'est-ce qu'on peut faire ? Regarder ses appuis.",
            "Combien de faits vérifiables une critique contient-elle, à votre avis ?",
            "Que reste-t-il, si on les enlève ?",
        ],
        notes="Compter les faits d'une vraie critique surprend toujours : quatre ou "
              "cinq sur trente lignes. Le reste est jugement et supposition, ce qui "
              "n'est pas un défaut mais qui se sait.")

    d.tableau('Analyse', "Trois choses qu'une critique fait",
              ['L\'opération', 'Comment la reconnaître'],
              [["Elle décrit", "un fait daté, chiffré, vérifiable"],
               ["Elle juge", "bon ou mauvais, avec ou sans appui"],
               ["Elle devine", "on devine, il semble, sans doute, visiblement"]],
              cle=0,
              note="Un jugement vaut ce que vaut le fait auquel il est accroché.",
              notes="Diapositive à photographier. Faire relever les verbes de la "
                    "troisième ligne dans le texte : ils sont le signal honnête d'une "
                    "supposition, et leur absence est le vrai défaut.")

    d.cartes('Analyse', "La phrase, et son statut", [
        ("« Quatre comédiens, une heure quarante. »", "fait vérifiable"),
        ("« Le spectacle le plus juste de la saison. »", "jugement sans appui"),
        ("« La comédienne ne quitte pas la scène. »", "fait vérifiable"),
        ("« Elle porte le spectacle d'un bout à l'autre. »", "jugement, accroché au fait"),
        ("« On devine que l'auteur a grandi là. »", "supposition, et il le marque"),
        ("« Je n'ai pas pu le vérifier. »", "aveu, et il vaut de l'or"),
    ], notes="Les deux dernières cases sont celles à défendre : un critique qui marque "
             "sa supposition et avoue n'avoir pas vérifié est plus fiable, pas moins. "
             "Le groupe pense d'abord le contraire.")

    d.regle("On ne conteste pas le fait, on conteste l'accrochage",
            "Vous n'étiez pas dans la salle. Le seul terrain où vous êtes son "
            "égal est le texte.",
            precision="La question à poser est toujours la même : ce jugement-là "
                      "repose-t-il sur ce fait-là ? « Le spectacle le plus juste de la "
                      "saison » ne repose sur rien pour l'instant — et c'est une "
                      "question légitime, publiable, à laquelle le critique doit "
                      "répondre.",
            notes="Diapositive à photographier. C'est la consigne exacte de la lettre "
                  "d'E2 : jamais la personne, toujours l'appui.")

    d.tableau('Analyse', "Le verbe décide du pronom",
              ['Le verbe', 'Le pronom'],
              [["parler de, se souvenir de", "dont, ce dont"],
               ["penser à, faire allusion à", "auquel, ce à quoi"],
               ["répondre à (une question)", "à laquelle"],
               ["s'appuyer sur, compter sur", "sur lequel, ce sur quoi"],
               ["parler à (une personne)", "à qui"]],
              cle=0,
              note="Faites la phrase à l'endroit pour trouver la préposition.",
              notes="Diapositive à photographier. Ce n'est jamais le nom repris qui "
                    "décide, c'est le verbe de la relative : le répéter deux fois.")

    d.pratique('Pratique', "Le pronom relatif",
               "Complétez.", [
        ("Le détail ___ il parle est à la troisième strophe.", "dont"),
        ("La question ___ personne n'a répondu, c'est la corde.", "à laquelle"),
        ("Le passage ___ vous faites allusion tient en une parenthèse.", "auquel"),
        ("___ je pense, c'est la nappe pliée en quatre.", "Ce à quoi"),
        ("Le fait ___ votre jugement s'appuie n'est pas dans le texte.", "sur lequel"),
        ("La voisine ___ elle tend la carte se met à lire.", "à qui"),
    ], corrige=True,
       notes="Exercice `t3rel` du module. Interdire « le passage que vous parlez » "
             "explicitement : c'est la faute qui vient de l'oral rapide, et elle se "
             "corrige en cherchant la préposition.")

    d.tableau('Analyse', "Citer, résumer, déformer",
              ['L\'opération', 'La règle'],
              [["Citer", "deux-points, guillemets, mots exacts"],
               ["Résumer", "d'autres mots, et la personne pourrait approuver"],
               ["Déformer", "un absolu ajouté, une condition retirée"]],
              cle=0,
              note="Le test : la personne citée approuve-t-elle d'un signe de tête ?",
              notes="Diapositive à photographier. Les trois marques de la déformation : "
                    "généraliser un cas, supprimer une condition, durcir un verbe "
                    "d'opinion en verbe de certitude.")

    d.pratique('Pratique', "Exact, fidèle, ou déformé ?",
               "Dites ce que fait chaque phrase rapportée.", [
        ("Josyane a dit : « Une lecture se juge à ce qu'elle explique. »", "citation exacte"),
        ("Selon Josyane, une lecture vaut par ce qu'elle explique.", "résumé fidèle"),
        ("Josyane prétend qu'aucune lecture n'est meilleure.", "déformation"),
        ("Léandre trouve la finale bâclée faute de temps.", "résumé fidèle"),
        ("Léandre soutient que toute la série est ratée.", "déformation"),
        ("Le critique affirme que l'auteur a grandi là.", "déformation - il devine"),
    ], corrige=True,
       notes="Exercice `t3cit` du module. Le dernier est le plus fin : aucun fait "
             "n'est faux, on a seulement retiré une précaution. C'est ainsi qu'on "
             "déforme sans mentir.")

    d.piege('Piège', "« il prétend que »",
            "« il écrit que »",
            "Le verbe introducteur juge celui qu'on rapporte avant même que le "
            "lecteur ait lu la citation. « Prétend » signale que vous ne le "
            "croyez pas ; « avoue » suppose qu'il y avait quelque chose à "
            "cacher. Employés sans le savoir dans une lettre au journal, ils "
            "décrédibilisent votre propre texte : le lecteur voit d'abord "
            "l'attaque, et il ne lit pas votre argument.",
            notes="Faire relever les verbes neutres : dit, écrit, explique, précise, "
                  "soutient. Ce sont ceux de la lettre d'E2.")

    d.billet(
        "Choisissez un jugement de la critique et écrivez la question que vous "
        "poseriez au critique. Un verbe introducteur neutre, aucune attaque.",
        exemples=[
            "« Vous écrivez que c'est le spectacle le plus juste de la saison ; sur quelle scène ce jugement repose-t-il ? »",
            "Deux phrases au maximum.",
        ],
        notes="Ce billet est le deuxième paragraphe de la lettre d'E2, en germe. Le "
              "rendre annoté au début du bloc E.")

    return d.save(dossier)
