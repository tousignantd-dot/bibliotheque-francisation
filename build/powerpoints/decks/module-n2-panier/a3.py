# -*- coding: utf-8 -*-
"""A3 · Où est ce produit ?
Bloc A « Je découvre » · couleur teal · 75 min. Dernière séance du bloc A.
Source : exercices `prVocab`, `prImg`, `prRayon`.

La séance de vocabulaire et de repérage dans l'espace du magasin. Elle ferme
le bloc de découverte : après elle, l'élève sait nommer ce qu'il voit et dire
approximativement où il faut aller. Lire les prix vient au bloc B.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-panier/images/')


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre="Où est ce produit ?",
        chapeau="Nommer ce qu'on voit dans un magasin, et savoir dans quel "
                "rayon chercher.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire. Beaucoup de mots, peu de grammaire. Si le centre "
                  "a une épicerie à moins de dix minutes, la dernière demi-heure se fait "
                  "mieux sur place que dans la classe.")

    d.objectifs([
        "nommer les objets du magasin ;",
        "nommer les papiers des prix ;",
        "dire dans quel rayon se trouve un produit ;",
        "employer « c'est dans l'allée… »."
    ])

    d.declencheur(
        'Observation', "Que voit-on dans cette allée ?",
        image=IMG + 'allee-epicerie.jpg',
        pistes=[
            "Comment s'appelle ce chemin entre les tablettes ?",
            "Qu'est-ce qui est posé sur les tablettes ?",
            "Comment savez-vous où aller dans un magasin que vous ne connaissez pas ?",
            "À qui demandez-vous ?",
        ],
        notes="Amener les mots « allée » et « tablette » sans les forcer. Le numéro "
              "d'allée, écrit en hauteur, est le repère que tout le monde peut utiliser "
              "sans lire.")

    d.vocabulaire('Vocabulaire · 1 de 2', "Ce qu'on voit dans le magasin", [
        ("un panier", "Ce qu'on porte pour mettre ses achats dedans."),
        ("une allée", "Le chemin entre deux rangées de tablettes."),
        ("une tablette", "La planche où les produits sont posés."),
        ("une caisse", "L'endroit où on paie, avant de sortir."),
    ], notes="Diapositive à photographier. Faire répéter chaque mot avec son article.")

    d.vocabulaire('Vocabulaire · 2 de 2', "Les trois papiers des prix", [
        ("une circulaire", "Le grand papier qui montre les prix de la semaine."),
        ("une affichette", "Le petit carton posé sur la tablette, sous le produit."),
        ("une étiquette", "Le petit papier collé sur le produit lui-même."),
        ("un spécial", "Un prix plus bas, seulement pendant quelques jours."),
    ], notes="Diapositive à photographier. Ces trois papiers sont le cœur du module : "
             "la circulaire à la maison, l'affichette sur la tablette, l'étiquette sur "
             "le produit. Les faire distinguer dès maintenant.")

    d.tableau('Analyse', "Chaque produit a son rayon",
              ['Le produit', 'Le rayon'],
              [["le lait", "les produits laitiers, au fond"],
               ["les pommes", "les fruits et légumes, près de l'entrée"],
               ["le savon à vaisselle", "les produits d'entretien, allée 7"],
               ["le pain", "la boulangerie, près des caisses"]],
              cle=2,
              note="Dans presque toutes les épiceries, le lait est au fond et les fruits "
                   "sont à l'entrée. Ce n'est pas un hasard.",
              notes="Diapositive à photographier. Demander au groupe de dire où sont ces "
                    "quatre choses dans l'épicerie qu'ils fréquentent : c'est presque "
                    "toujours pareil.")

    d.regle("C'est dans l'allée…",
            "Le numéro d'allée est le repère le plus simple du magasin.",
            precision="« Le savon est dans <b>l'allée 7</b>. » On peut le trouver sans "
                      "savoir lire les panneaux : les numéros sont écrits gros, en "
                      "hauteur. Pour demander : « <b>C'est dans quelle allée ?</b> »",
            notes="Diapositive à photographier. C'est la première fois que la question "
                  "courte apparaît ; elle sera reprise en entier au bloc C.")

    d.pratique('Vocabulaire', "Le mot et sa définition",
               "Reliez chaque mot à ce qu'il veut dire.", [
        ("une circulaire", "le grand papier des prix de la semaine"),
        ("une allée", "le chemin entre deux rangées de tablettes"),
        ("une affichette", "le petit carton sous le produit, sur la tablette"),
        ("une étiquette", "le petit papier collé sur le produit"),
        ("un panier", "ce qu'on porte pour mettre ses achats"),
        ("un spécial", "un prix plus bas pendant quelques jours"),
    ], corrige=True, cols=1,
       notes="Six mots seulement. Les faire d'abord à l'oral avant de les faire écrire.")

    d.pratique('Pratique · à deux', "Dans quel rayon ?",
               "Deux par deux. L'un demande, l'autre répond.", [
        ("Étape 1", "Choisissez cinq produits de votre liste de la semaine."),
        ("Étape 2", "Demandez : « Le lait, c'est où ? »"),
        ("Étape 3", "Répondez : « Au fond, avec les produits laitiers. »"),
        ("Étape 4", "Changez de rôle."),
    ], cols=1,
       notes="Vingt minutes. Accepter les réponses approximatives : « au fond », « à "
             "droite », « allée 7 ». Le but est de se faire comprendre, pas d'être exact.")

    d.billet(
        "Écrivez quatre produits et le rayon où vous les trouvez.",
        exemples=[
            "Le riz est dans l'allée 3.",
            "Les pommes sont à l'entrée.",
            "Le savon est avec les produits d'entretien.",
        ],
        notes="Devoir court. Ils peuvent aller vérifier dans leur épicerie : c'est même "
              "la meilleure façon de faire ce devoir.")

    return d.save(dossier)
