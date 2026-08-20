# -*- coding: utf-8 -*-
"""B3 · jusqu'à, vers, par.
Bloc B · couleur ambre (écriture) · 75 min.
Source : mini-leçon `t1prep`, exercice `t1prep`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="jusqu'à, vers, par",
        chapeau="Un itinéraire répond à trois questions : où j'arrête, de quel "
                "côté je vais, par où je passe. Chacune a sa préposition.",
        duree='75 minutes')

    d.titre(notes="Écrire les trois questions au tableau dès le début et les y laisser. "
                  "Toute la séance s'y ramène.")

    d.objectifs([
        "employer jusqu'à pour dire où le déplacement s'arrête ;",
        "employer vers pour donner une direction sans destination ;",
        "employer par pour nommer le chemin emprunté ;",
        "fusionner correctement : jusqu'au, jusqu'aux.",
    ])

    d.tableau('Analyse', "Trois questions, trois prépositions",
              ['La question', 'La préposition', 'Exemple'],
              [["Où j'arrête ?", "jusqu'à", "jusqu'au feu"],
               ["De quel côté ?", "vers", "vers Gaétan-Boucher"],
               ["Par où je passe ?", "par", "par le corridor"]],
              cle=0,
              note="Dans le doute, c'est jusqu'à : c'est la plus fréquente dans un itinéraire.",
              notes="Diapo centrale. Faire recopier, puis cacher les deux colonnes de droite "
                    "et faire retrouver.")

    d.regle("jusqu'à — la limite",
            "Elle dit où le déplacement s'arrête.",
            precision="« Continuez jusqu'au feu » : la personne sait exactement quand "
                      "s'arrêter. Attention à la fusion : à + le donne <b>au</b>, à + les "
                      "donne <b>aux</b>. Devant un nom de lieu sans déterminant, pas de "
                      "fusion : jusqu'à Longueuil.",
            notes="La fusion est le vrai enjeu de la séance. Écrire les quatre formes au "
                  "tableau : au, aux, à la, à l'.")

    d.regle('vers — la direction',
            "Elle donne le côté, sans dire où l'on s'arrête.",
            precision="« L'autobus va vers le centre-ville » ne veut pas dire qu'il s'y "
                      "arrête : il peut tourner avant. C'est le mot des panneaux et des "
                      "autobus, justement parce qu'il n'engage à rien.",
            notes="Faire la différence avec jusqu'à sur un exemple concret : « allez vers le "
                  "feu » laisse dans le doute, « allez jusqu'au feu » tranche.")

    d.regle('par — le chemin',
            "Elle nomme par où l'on passe, pas où l'on va.",
            precision="« Passez par le corridor vitré. » · « Sortez par la porte "
                      "principale. » Sa cousine <b>à travers</b> insiste sur le fait de "
                      "traverser quelque chose : à travers le parc, à travers le boisé.",
            notes="Beaucoup de langues n'ont qu'une seule préposition pour tout cela. "
                  "Prévoir du temps sur cette diapositive.")

    d.piege('Oublier la fusion',
            "Continuez jusqu'à le feu.",
            "Continuez jusqu'au feu.",
            "à + le donne au, à + les donne aux. La fusion est obligatoire en français, "
            "sans exception. « À le » et « de le » n'existent tout simplement pas. "
            "C'est mécanique, et ça se corrige en une séance.",
            notes="Écrire les quatre fusions au tableau — au, aux, du, des — et les laisser "
                  "jusqu'à la fin du module. Elles servent partout.")

    d.pratique('Pratique · 1 de 2', "Quelle préposition ?",
               "Complétez. Posez-vous la question du tableau.", [
        ("Continuez tout droit ___ feu de circulation.", "jusqu'au"),
        ("Prenez l'autobus qui va ___ Gaétan-Boucher.", "vers"),
        ("Passez ___ le corridor vitré, à votre gauche.", "par"),
        ("Sortez ___ la porte principale et tournez à droite.", "par"),
        ("Prenez la ligne jaune ___ Longueuil.", "jusqu'à"),
        ("Le sentier passe ___ le parc.", "à travers"),
    ], corrige=True,
       notes="Faire dire la question à voix haute avant chaque réponse : « où j'arrête ? », "
             "« de quel côté ? », « par où ? ».")

    d.pratique('Pratique · 2 de 2', "Corrigez la fusion",
               "Chaque phrase contient une fusion manquée.", [
        ("Marchez jusqu'à le parc.", "jusqu'au parc"),
        ("Descendez jusqu'à les escaliers.", "jusqu'aux escaliers"),
        ("C'est en face de le dépanneur.", "en face du dépanneur"),
        ("L'escalier est au bout de le corridor.", "au bout du corridor"),
    ], corrige=True, cols=1,
       notes="Les deux dernières lignes emploient de + le : la même règle, avec l'autre "
             "préposition. Le faire remarquer.")

    d.cartes('Un itinéraire complet', "Les trois prépositions à l'œuvre", [
        ("Le départ",
         "« Sortez par la porte principale. » — par nomme le chemin de sortie."),
        ("Le milieu",
         "« Marchez jusqu'au parc, puis traversez à travers le sentier. » — jusqu'à donne "
         "la limite, à travers le passage."),
        ("La fin",
         "« Prenez l'autobus qui va vers Saint-Hubert. » — vers donne la direction "
         "générale, sans promettre l'arrivée."),
    ], notes="Faire construire un itinéraire complet au tableau avec le groupe, en imposant "
             "les trois prépositions. Dix minutes, très efficaces.")

    d.billet(
        "Écrivez quatre phrases d'itinéraire, une par préposition.",
        exemples=[
            "jusqu'à, vers, par, à travers.",
            "Vérifiez chaque fusion : au, aux, du, des.",
        ],
        notes="Corriger surtout les fusions. C'est la faute qui survit le plus longtemps.")

    return d.save(dossier)
