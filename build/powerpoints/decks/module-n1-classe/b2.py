# -*- coding: utf-8 -*-
"""B2 · Sur, dans, sous.
Bloc B « Défi 1 · La consigne » · couleur ambre · 75 min.
Source du module : dialogue `t1b`, exercices `t1ou` et `t1b`, mini-leçon `t1ou`.

Une consigne dit souvent où est la chose : « le livre est sur la table »,
« prenez le stylo dans le sac ». Trois petits mots suffisent, et deux d'entre
eux se ressemblent à l'oreille — c'est la difficulté réelle de la séance.
"""
import os

from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n1-classe/images/')


def photo(nom):
    """Le chemin de l'image, ou rien si elle n'est pas encore produite."""
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre='Sur, dans, sous',
        chapeau="Trois petits mots pour dire où est la chose. Deux se "
                "ressemblent beaucoup : la main le dit mieux que l'oreille.",
        duree='75 minutes')

    d.titre(notes="Commencer par un objet et une chaise : poser le stylo dessus, dedans, "
                  "dessous, en nommant chaque fois. Trois mots, trois gestes, avant "
                  "toute explication.")

    d.objectifs([
        "dire où est un objet ;",
        "employer sur, dans et sous ;",
        "entendre la différence entre sur et sous ;",
        "comprendre une consigne qui dit où prendre la chose.",
    ])

    d.dialogue('Dialogue', "Où est mon stylo ?", [
        ("BOPHA", "Ivan, où est mon stylo ?", True),
        ("IVAN", "Ton stylo ? Il est sur la table.", True),
        ("BOPHA", "Non. Il n'est pas sur la table.", True),
        ("IVAN", "Regarde sous la chaise.", True),
        ("BOPHA", "Ah oui ! Il est sous la chaise.", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Entre élèves, on se tutoie : c'est la seule fois du module où le "
             "vouvoiement tombe. Le dire en passant, sans en faire une leçon.")

    d.regle("Le petit mot passe devant",
            "sur la table, dans le sac, sous la chaise.",
            precision="En français, le petit mot vient toujours <b>avant</b> le nom. On "
                      "ne dit jamais « la table sur ». L'ordre ne change pas.",
            notes="Diapositive à photographier. C'est la seule règle de la séance, et "
                  "elle est absolue.")

    d.tableau('Analyse', "Trois places",
              ['Le mot', 'Où est la chose'],
              [["sur", "dessus, on la voit"],
               ["dans", "à l'intérieur, cachée"],
               ["sous", "en dessous, plus bas"]],
              cle=2,
              note="Si vous devez ouvrir quelque chose pour la prendre, c'est « dans ».",
              notes="Diapositive à photographier. Faire le geste de la main en même temps "
                    "que le mot : en haut, à l'intérieur, en bas.")

    d.declencheur(
        'Observation', "Où est le sac ?",
        image=photo('sac-sous-chaise.jpg'),
        pistes=[
            "Le sac est sur la chaise ?",
            "Le sac est sous la chaise ?",
            "Montrez avec votre main.",
            "Et votre sac à vous, où est-il ?",
        ],
        notes="La photo tranche à elle seule : c'est pour cela qu'elle vient après le "
              "tableau et non avant.")

    d.piege("Confondre sur et sous",
            "« Le sac est sur la chaise » — alors qu'il est dessous.",
            "La main en haut pour sur, en bas pour sous.",
            "Ces deux mots ne diffèrent que par une voyelle, et l'erreur ne se voit pas "
            "à l'écrit. Le geste de la main, fait en parlant, la corrige tout seul.",
            notes="Faire adopter le geste au groupe : il restera longtemps après la "
                  "séance, et il sert aussi à comprendre.")

    d.pratique('Pratique', "Sur, dans ou sous ?",
               "Complétez la phrase.", [
        ("Le livre est ___ la table.", "sur"),
        ("Mon stylo est ___ mon sac.", "dans"),
        ("Le sac de Bopha est ___ la chaise.", "sous"),
        ("L'horloge est ___ le mur.", "sur"),
        ("Les feuilles sont ___ le livre.", "dans"),
    ], corrige=True, cols=1,
       notes="Le quatrième surprend : pour ce qui est accroché, on dit « sur le mur ».")

    d.pratique('Pratique · à deux', "Cache et cherche",
               "Deux par deux, avec un stylo.", [
        ("Étape 1", "A cache le stylo pendant que B ferme les yeux."),
        ("Étape 2", "B cherche. A dit : « Il est sous la chaise. »"),
        ("Étape 3", "On change de rôle. Cinq fois chacun."),
        ("Étape 4", "Puis A donne une consigne : « Prenez le stylo dans le sac. »"),
    ], cols=1,
       notes="Vingt minutes. L'étape 4 rejoint le défi : la consigne dit où prendre la "
             "chose, et il faut les deux pour la suivre.")

    d.billet(
        "Écrivez trois phrases sur vos affaires.",
        exemples=[
            "Mon livre est dans mon sac.",
            "Mon sac est sous ma chaise.",
            "Mon stylo est sur la table.",
        ],
        notes="Trois phrases, trois mots différents. C'est la fin du défi 1 : la séance "
              "suivante ouvre l'heure et l'horaire.")

    return d.save(dossier)
