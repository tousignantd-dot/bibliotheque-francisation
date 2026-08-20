# -*- coding: utf-8 -*-
"""B3 · Ça se garde, ça se cuisine.
Bloc B · couleur ambre (écriture) · 60 min.
Source : mini-leçon `t1garde`, exercice `t1garde`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre='Ça se garde, ça se cuisine',
        chapeau="« Le poisson se garde deux jours. » Qui le garde ? Personne "
                "en particulier. C'est une façon de donner une information "
                "générale, et elle est partout dans l'alimentation.",
        duree='60 minutes')

    d.titre(notes="Écrire au tableau « Le poisson se garde deux jours » et demander : qui "
                  "le garde ? Le flottement du groupe est le point de départ.")

    d.objectifs([
        "transformer une phrase avec « on » en phrase avec « se » ;",
        "accorder le verbe avec la chose, au singulier comme au pluriel ;",
        "employer cette forme pour parler de conservation et de préparation ;",
        "la distinguer du verbe pronominal ordinaire.",
    ])

    d.tableau('Analyse', "Deux façons de dire la même chose",
              ['Avec « on »', 'Avec « se »'],
              [["On garde le poisson deux jours.", "Le poisson se garde deux jours."],
               ["On mange ce fruit cru.", "Ce fruit se mange cru."],
               ["On ne dit pas ça ici.", "Ça ne se dit pas ici."]],
              cle=0,
              note="La chose devient le sujet. Personne n'est nommé, ni avant ni après.",
              notes="Diapo centrale. Faire recopier. Les deux colonnes sont correctes ; "
                    "celle de droite est plus courante à l'oral.")

    d.regle("L'accord se fait avec la chose",
            "C'est elle le sujet, pas la personne.",
            precision="« Le poisson se garde » au singulier. « Les conserves se "
                      "conservent » au pluriel. C'est la seule difficulté de la leçon, et "
                      "elle se règle en regardant le sujet.",
            notes="Écrire les deux formes au tableau. Faire produire trois phrases au "
                  "pluriel par trois élèves.")

    d.cartes("Les verbes de l'alimentation", "Toute une famille", [
        ("Pour la conservation",
         "ça se garde · ça se conserve · ça se congèle · ça se réchauffe"),
        ("Pour la préparation",
         "ça se mange · ça se cuisine · ça se coupe · ça se sert"),
        ("La question la plus posée d'une épicerie",
         "« Ça se garde combien de temps ? » — quatre mots qui évitent de jeter."),
    ], notes="La troisième carte mérite d'être répétée par le groupe. C'est une phrase "
             "qu'ils emploieront la semaine même.")

    d.regle('Ailleurs aussi',
            "Cette construction déborde largement l'alimentation.",
            precision="« Ça se dit beaucoup ici. » · « Ça ne se fait pas. » · « Ce mot "
                      "s'écrit avec deux l. » · « Ça se comprend. » Toutes ces phrases "
                      "parlent d'un usage général, sans nommer personne.",
            notes="« Ça ne se fait pas » est très utile culturellement : elle dit qu'une "
                  "chose n'est pas interdite, mais qu'on ne la fait pas ici.")

    d.piege('Confondre les deux emplois de « se »',
            "Il se lave. / Ce chandail se lave à l'eau froide.",
            "Sujet personne › il fait l'action sur lui. Sujet chose › la phrase est générale.",
            "Le même petit mot sert à deux choses. Le test tient en une question : le sujet "
            "est-il une personne ou une chose ? Une personne fait l'action sur elle-même ; "
            "une chose ne fait rien du tout.",
            notes="Faire produire une paire par le groupe : « elle se coupe » et « ça se "
                  "coupe en tranches ». La différence saute aux yeux.")

    d.pratique('Pratique · 1 de 2', "Transformez avec « se »",
               "Récrivez la phrase.", [
        ("On garde le poisson frais deux jours.", "Le poisson frais se garde deux jours."),
        ("On congèle ce poisson trois mois.", "Ce poisson se congèle trois mois."),
        ("On mange ce fruit cru.", "Ce fruit se mange cru."),
        ("On conserve les conserves des mois.", "Les conserves se conservent des mois."),
        ("On ne dit pas ça ici.", "Ça ne se dit pas ici."),
    ], corrige=True, cols=1,
       notes="La quatrième ligne est au pluriel : c'est celle qui départage. Faire venir un "
             "élève au tableau.")

    d.pratique('Pratique · 2 de 2', "Personne ou chose ?",
               "Dites si le sujet est une personne ou une chose.", [
        ("Il se lave les mains.", "personne — il fait l'action sur lui"),
        ("Ce chandail se lave à l'eau froide.", "chose — phrase générale"),
        ("Elle se coupe les cheveux.", "personne"),
        ("Ça se coupe en tranches minces.", "chose"),
        ("Le poisson se garde deux jours.", "chose"),
    ], corrige=True, cols=1,
       notes="Cet exercice vérifie la compréhension du mécanisme, pas la production.")

    d.billet(
        "Écrivez cinq phrases avec « se » sur des aliments que vous connaissez.",
        exemples=[
            "Trois sur la conservation, deux sur la préparation.",
            "Au moins une au pluriel.",
        ],
        notes="Corriger surtout l'accord au pluriel. Rendre à la séance suivante.")

    return d.save(dossier)
