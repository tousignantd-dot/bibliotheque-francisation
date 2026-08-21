# -*- coding: utf-8 -*-
"""A4 · Écrire l'état des lieux.
Bloc A « Je découvre » · couleur ambre · écriture · 75 min.
Source : exercice `prEtat` et sa mini-leçon.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-emmenagement/images/')


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="Écrire l'état des lieux",
        chapeau="Nommer, situer, mesurer. Un état des lieux se lit en une "
                "minute, ou il ne se lit pas.",
        duree='75 minutes')

    d.titre(notes="Première séance d'écriture du module. Elle produit un vrai document, "
                  "que les élèves peuvent réutiliser tels quels chez eux.")

    d.objectifs([
        "nommer un défaut avec le mot juste ;",
        "situer un défaut dans une pièce ;",
        "écrire une ligne d'état des lieux complète ;",
        "savoir ce qui rend le papier valable : deux signatures et une date.",
    ])

    d.declencheur(
        'Observation', "Comment écririez-vous ça sur une feuille ?",
        image=IMG + 'logement-vide.jpg',
        pistes=[
            "Quel mot pour la marque du plancher ?",
            "Comment dire où elle se trouve ?",
            "Faut-il donner une grandeur ?",
            "Qui signe la feuille ?",
        ],
        notes="Recueillir trois ou quatre formulations spontanées et les écrire au "
              "tableau. On les comparera à la règle des trois temps, à la diapositive "
              "suivante.")

    d.regle("Nommer, situer, mesurer",
            "Une ligne d'état des lieux fait toujours ces trois choses, dans cet ordre.",
            precision="Salon : égratignure de 40 cm sur le plancher, près de la fenêtre. "
                      "Nommer, c'est le mot juste. Situer, c'est la pièce et l'endroit. "
                      "Mesurer, c'est la grandeur ou la hauteur.",
            notes="Diapositive à photographier. Comparer avec les formulations recueillies "
                  "au tableau : il manque presque toujours l'endroit.")

    d.vocabulaire('Vocabulaire', "Les six mots des défauts", [
        ("une égratignure", "Une marque longue et mince sur une surface dure."),
        ("une fissure", "Une fente dans un mur ou dans un plafond."),
        ("une tache", "Une marque de couleur, souvent d'humidité."),
        ("une brûlure", "Une marque de chaleur sur un comptoir ou un plancher."),
        ("un trou", "Une ouverture dans un mur, souvent une vis enlevée."),
        ("une moustiquaire déchirée", "Le grillage de fenêtre percé ou fendu."),
    ], notes="Six mots couvrent presque tous les défauts d'un logement ordinaire. Les "
             "faire employer chacun dans une phrase avec un endroit.")

    d.cartes("Les mots pour situer", "Sans endroit, un défaut ne se retrouve pas", [
        ("près de", "près de la fenêtre · près de la porte · près de la plinthe"),
        ("au-dessus de", "au-dessus de la douche · au-dessus du poêle"),
        ("dans le coin", "dans le coin gauche · dans le coin de la pièce"),
        ("à droite en entrant", "la formule qui remplace un plan quand il n'y en a pas"),
    ], notes="Faire décrire l'emplacement d'un objet du local avec chacune des quatre "
             "formules. Deux minutes, et elles sont acquises.")

    d.tableau('Ce qui fonctionne mal', "Ça se note aussi, et ça devient une demande",
              ['Ce que vous voyez', 'Ce que vous écrivez'],
              [["La porte d'armoire résiste", "Cuisine : la porte de l'armoire ferme mal."],
               ["Le rond du poêle reste froid", "Cuisine : le rond arrière droit ne chauffe pas."],
               ["Le robinet goutte", "Salle de bain : le robinet coule."],
               ["La fenêtre ne se ferme pas", "Chambre : la fenêtre ferme mal."]],
              cle=1,
              note="Ces lignes-là servent tout de suite : ce sont les réparations dues.",
              notes="Distinguer les deux usages de l'état des lieux : se protéger pour "
                    "plus tard, et obtenir des réparations maintenant.")

    d.piege("Raconter au lieu de nommer",
            "Le plancher est un peu magané par endroits.",
            "Salon : égratignure de 40 cm près de la fenêtre.",
            "« Un peu magané » ne veut plus rien dire trois ans plus tard, et ne prouve "
            "rien. Le mot juste, l'endroit et la grandeur, eux, restent lisibles par "
            "n'importe qui.",
            notes="C'est l'erreur la plus fréquente, et elle vient d'une bonne intention : "
                  "on veut être poli avec le propriétaire. Dire que la précision n'est "
                  "pas de l'impolitesse.")

    d.pratique('Écriture', "Écrivez la ligne",
               "L'enseignante décrit ce qu'elle voit ; chacun écrit la ligne complète.", [
        ("Une marque longue sur le plancher du salon",
         "Salon : égratignure de 40 cm sur le plancher, près de la fenêtre."),
        ("Une marque jaune au plafond de la salle de bain",
         "Salle de bain : tache jaune au plafond, au-dessus de la douche."),
        ("La porte d'armoire qui ne ferme pas bien",
         "Cuisine : la porte de l'armoire du haut ferme mal."),
        ("Un trou de vis dans le mur de la chambre",
         "Chambre : trou de vis dans le mur, à 1 m du plancher."),
        ("La moustiquaire de la fenêtre, percée",
         "Chambre du fond : moustiquaire de la fenêtre déchirée."),
        ("Le rond du poêle qui reste froid",
         "Cuisine : le rond arrière droit du poêle ne chauffe pas."),
    ], corrige=True,
       notes="C'est le laboratoire de la mini-leçon prEtat. Faire écrire d'abord, corriger "
             "ensuite, en vérifiant les trois temps un par un.")

    d.regle("Deux signatures et une date",
            "Sans elles, c'est une note personnelle. Avec elles, c'est une pièce.",
            precision="Chacun en garde une copie. Trois ans plus tard, en partant, on "
                      "ressort la liste : ce qui y était déjà n'est pas de votre faute.",
            notes="Terminer la séance là-dessus. C'est la raison d'être de tout ce qu'on "
                  "vient de faire.")

    d.billet(
        "Écrivez trois lignes d'état des lieux pour la pièce où vous êtes en ce moment.",
        exemples=[
            "Nommez, situez, mesurez — même pour une petite marque.",
            "Comparez avec votre voisin : avez-vous vu les mêmes choses ?",
        ],
        notes="Le local de classe fait un excellent terrain : il est toujours plus abîmé "
              "qu'il n'en a l'air.")

    return d.save(dossier)
