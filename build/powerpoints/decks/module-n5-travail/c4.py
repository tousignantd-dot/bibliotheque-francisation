# -*- coding: utf-8 -*-
"""C4 · « Appuyez », ou « appuyer » ?
Bloc C « Défi 2 » · couleur ambre · 75 min. Impératif ou infinitif de consigne,
et où s'arrête ce qu'on répare soi-même.
Source : exercices `t2cons` et `t2pb`, mini-leçons du même nom.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-travail/images/')


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre="« Appuyez », ou « appuyer » ?",
        chapeau="Les deux demandent la même chose. La première s'adresse à "
                "quelqu'un ; la seconde ne s'adresse à personne. C'est toute "
                "la différence, et elle décide de laquelle vous emploierez.",
        duree='75 minutes')

    d.titre(notes="Séance qui ferme le défi 2. Projeter côte à côte une page du livret de "
                  "l'appareil et la demi-page que Dorine et Kevin veulent coller au mur. "
                  "Demander pourquoi elles ne sonnent pas pareil. La réponse est la "
                  "séance entière.")

    d.objectifs([
        "choisir entre l'impératif et l'infinitif selon ce qu'on écrit ;",
        "nier correctement dans les deux formes ;",
        "tenir la même forme du début à la fin d'une note ;",
        "savoir ce qu'on règle soi-même et ce qu'on appelle.",
    ])

    d.tableau('Deux formes', "Le même geste, deux tons",
              ['Impératif', 'Infinitif'],
              [["Appuyez sur le bouton vert.", "Appuyer sur le bouton vert."],
               ["Insérez votre carte.", "Insérer sa carte."],
               ["N'ouvrez pas la porte du bas.", "Ne pas ouvrir la porte du bas."],
               ["Refermez bien.", "Refermer bien."]],
              cle=0,
              note="À l'impératif, la négation entoure le verbe. À l'infinitif, les "
                   "deux mots restent collés devant.",
              notes="La troisième rangée est le vrai point de la séance : « ne ouvrir "
                    "pas » est la faute typique de quelqu'un qui passe d'une forme à "
                    "l'autre sans y penser.")

    d.cartes("Laquelle choisir", "Une question suffit", [
        ("Est-ce que j'écris à quelqu'un ?",
         "Oui : l'impératif. Une note aux collègues, un courriel, une consigne dite."),
        ("Est-ce que j'écris une affiche ?",
         "Oui : l'infinitif. Un livret d'appareil, une affiche, une recette, un formulaire."),
        ("À l'infinitif, « votre » devient « son »",
         "Insérez votre carte devient Insérer sa carte : la phrase ne parle à personne."),
        ("Ce qu'on n'écrit jamais",
         "« Vous devez appuyer sur le bouton vert » : plus long, et ça n'ajoute rien."),
    ], notes="La demi-page de Dorine et Kevin sera à l'impératif : ils écrivent à des "
             "gens qu'ils croisent tous les jours dans le corridor. Le faire dire par le "
             "groupe plutôt que de l'annoncer.")

    d.piege("Mélanger les deux formes",
            "Levez le couvercle. Puis placer la feuille.",
            "Levez le couvercle. Puis placez la feuille.",
            "Choisissez au début et tenez-vous-y. Le mélange donne l'impression que "
            "deux personnes ont écrit la note, et le lecteur se demande à qui elle "
            "s'adresse.",
            notes="Faire relire les billets de C3 : beaucoup mélangent sans s'en "
                  "apercevoir. Se corriger soi-même vaut mieux que de corriger un "
                  "exemple inventé.")

    d.pratique('Transformation', "Changez de forme",
               "Récrivez chaque directive dans la forme demandée.", [
        ("Appuyer sur Numériser. (impératif)", "Appuyez sur Numériser."),
        ("Insérez votre carte. (infinitif)", "Insérer sa carte."),
        ("Ne pas forcer sur la feuille. (impératif)", "Ne forcez pas sur la feuille."),
        ("N'ouvrez pas la porte du bas. (infinitif)", "Ne pas ouvrir la porte du bas."),
        ("Confirmer l'adresse. (impératif)", "Confirmez l'adresse."),
        ("Refermez bien la porte. (infinitif)", "Refermer bien la porte."),
        ("Verrouiller l'écran. (impératif)", "Verrouillez l'écran."),
        ("Ne laissez pas votre original. (infinitif)", "Ne pas laisser son original."),
    ], cols=2, corrige=True,
       notes="Les huit énoncés sont ceux de l'exercice interactif. La dernière rangée "
             "comporte deux changements dans la même phrase : la négation et le "
             "déterminant. La signaler.")

    d.declencheur(
        'Observation', "Une feuille froissée coincée entre deux rouleaux. "
                       "Vous y touchez, ou vous appelez ?",
        image=IMG + 'photocopieur-corridor.jpg',
        pistes=[
            "Qu'est-ce qui s'ouvre par une porte prévue pour ça ?",
            "Qu'est-ce qui demande de forcer, de dévisser ou de deviner ?",
            "Que se passe-t-il quand on relance la copie trois fois de suite ?",
            "Qu'est-ce qu'on dit au téléphone pour que la bonne pièce arrive ?",
        ],
        notes="La troisième piste mérite qu'on s'y arrête : chaque relance ajoute une "
              "feuille dans l'appareil. Un bourrage simple devient alors un empilement "
              "que personne ne démêle sans outil.")

    d.regle("Ce qui s'ouvre sans outil est à vous",
            "Ce qui demande de forcer, de dévisser ou de deviner ne l'est pas.",
            precision="Et ne le faites surtout pas deux fois : un appareil qu'on force "
                      "deux fois passe d'une réparation de dix minutes à une réparation "
                      "de trois jours.",
            notes="Cette règle vaut pour tout le matériel d'un lieu de travail, pas "
                  "seulement pour le photocopieur : la déchiqueteuse, le lave-vaisselle, "
                  "la machine à café.")

    d.pratique('Décision', "Je règle, ou j'appelle le poste dix-neuf ?",
               "Pour chaque situation, choisissez.", [
        ("Une feuille est coincée derrière la porte de côté.", "je règle"),
        ("Le bac à papier est vide.", "je règle"),
        ("Une odeur de brûlé sort de l'arrière de l'appareil.", "j'appelle"),
        ("L'écran demande de confirmer l'adresse courriel.", "je règle"),
        ("L'écran reste rouge après avoir été redémarré.", "j'appelle"),
        ("La feuille s'est déchirée, un morceau est resté dedans.", "j'appelle"),
        ("Les copies sortent à l'envers : le document était mal placé.", "je règle"),
        ("Il y a un liquide sombre sous l'appareil.", "j'appelle"),
    ], cols=2, corrige=True,
       notes="Après la correction, faire formuler ce qu'on dit au téléphone : le message "
             "exact de l'écran, mot pour mot, l'appareil et l'endroit, et ce qu'on a déjà "
             "essayé. « Ça ne marche pas » fait déplacer quelqu'un pour rien.")

    d.billet(
        "Écrivez la demi-page de Dorine et Kevin : les quatre opérations du "
        "photocopieur.",
        exemples=[
            "Copier · numériser · remplir le bac · débloquer une feuille.",
            "Une seule forme du début à la fin, et des marqueurs de temps.",
        ],
        notes="C'est la production écrite du défi 2, et elle prépare directement le "
              "courriel de la séance E2 : même exigence de forme tenue, même souci du "
              "lecteur. Ramasser et corriger.")

    return d.save(dossier)
