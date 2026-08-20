# -*- coding: utf-8 -*-
"""A4 · Où ça se trouve.
Bloc A « Je découvre » · couleur teal · 50 min.
Source : exercices `prImg` et `prAllee`, cartes mémoire.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-alimentation/images/')


def build(dossier):
    d = Deck(
        code='A4', section='teal',
        titre='Où ça se trouve',
        chapeau="Huit endroits d'une épicerie. Savoir lequel sert à quoi, "
                "c'est la moitié du temps gagné — et c'est ce qui permet de "
                "poser une question précise quand on ne trouve pas.",
        duree='50 minutes')

    d.titre(notes="Séance visuelle et courte. Elle clôt le bloc A : à la fin, chacun doit "
                  "pouvoir dire où se trouve n'importe quel produit de sa liste.")

    d.objectifs([
        "nommer huit endroits d'une épicerie ;",
        "savoir ce qui se vend au comptoir et ce qui se prend soi-même ;",
        "employer l'article juste : une allée, le comptoir, la balance ;",
        "poser une question précise quand je ne trouve pas.",
    ])

    d.declencheur(
        'Observation', "Que peut-on acheter ici, et comment ?",
        image=IMG + 'comptoir-boucherie.jpg',
        pistes=[
            "Se sert-on soi-même, ou faut-il demander ?",
            "Comment dit-on la quantité qu'on veut ?",
            "À quoi sert la balance ?",
            "Est-ce plus cher qu'un plateau déjà emballé ?",
        ],
        notes="La dernière piste ouvre une vraie discussion : au comptoir, on obtient la "
              "quantité exacte et souvent une meilleure coupe, pour le même prix au poids.")

    d.cartes('Ce qu\'on prend soi-même', "Quatre rayons en libre-service", [
        ("les allées",
         "Conserves, pâtes, riz, produits secs. On se sert et on met dans le panier."),
        ("les fruits et légumes",
         "On choisit à la pièce ou au poids. La balance du rayon donne le prix."),
        ("les produits d'entretien",
         "Savons, nettoyants, papier. Souvent la dernière allée du magasin."),
        ("les surgelés",
         "Au fond, dans les congélateurs. À prendre en dernier pour qu'ils restent froids."),
    ], notes="La dernière carte donne un conseil pratique que peu de gens connaissent : "
             "l'ordre de la tournée compte.")

    d.cartes("Ce qu'on demande à quelqu'un", "Quatre comptoirs", [
        ("la boucherie",
         "Viandes et volailles, vendues au poids. On dit ce qu'on veut et combien."),
        ("la poissonnerie",
         "Poisson frais sur la glace. On peut demander de le vider ou de l'écailler."),
        ("la charcuterie",
         "Jambons, fromages, tranchés devant vous. On précise mince ou épais."),
        ("la boulangerie",
         "Pains et pâtisseries. Souvent en libre-service, mais avec un comptoir pour les "
         "commandes."),
    ], notes="Faire nommer les quatre comptoirs de l'épicerie la plus proche de l'école. "
             "Plusieurs élèves n'en ont jamais utilisé un seul.")

    d.tableau('Analyse', "Où chercher quoi",
              ['Le produit', 'Où le trouver'],
              [["De la pâte de tomate", "avec les sauces, pas avec les légumes"],
               ["Du poulet frais", "au comptoir de la boucherie"],
               ["Du savon à vaisselle", "avec les produits d'entretien"],
               ["Du riz en grand format", "en bas des étagères, allée des produits secs"]],
              cle=0,
              note="La première ligne est le piège classique : la logique du magasin n'est "
                   "pas celle du cuisinier.",
              notes="Faire trouver d'autres exemples de rangement contre-intuitif : le lait "
                    "de coco, les épices, les nouilles asiatiques.")

    d.regle('La question précise',
            "Nommez le produit exactement, pas la catégorie.",
            precision="« Où sont les sauces ? » obtient une allée. « Je cherche de la pâte "
                      "de tomate » obtient l'endroit exact, et souvent une comparaison de "
                      "marques en prime. Nommer le produit, c'est obtenir une réponse "
                      "utilisable.",
            notes="Diapo à photographier. Faire produire trois questions précises par trois "
                  "élèves.")

    d.piege('Chercher dans la mauvaise logique',
            "La pâte de tomate, c'est de la tomate : ce doit être avec les légumes en conserve.",
            "La pâte de tomate sert à faire des sauces : elle est avec les sauces.",
            "Un magasin range par usage, pas par ingrédient. Le lait de coco est avec les "
            "produits asiatiques, pas avec le lait. Les olives sont avec les marinades, pas "
            "avec les légumes. Quand la logique échoue, on demande.",
            notes="Exactement la faute de Farida dans le dialogue de A1. Le rappeler.")

    d.pratique('Pratique', "Le mot juste",
               "Complétez avec le mot du vocabulaire.", [
        ("La pâte de tomate est dans l'___ cinq.", "allée"),
        ("Au ___ de la boucherie, on commande au poids.", "comptoir"),
        ("Les ___ se gardent des mois dans l'armoire.", "conserves"),
        ("La ___ donne le poids et le prix.", "balance"),
        ("La ___ est écrite sous le code-barres.", "provenance"),
        ("Le tableau de la valeur ___ est au dos.", "nutritive"),
    ], corrige=True,
       notes="Ces six mots sont dans le banc de vocabulaire du module.")

    d.billet(
        "Écrivez votre liste d'épicerie de la semaine, en indiquant où chaque produit se trouve.",
        exemples=[
            "Allée, comptoir, rayon des fruits et légumes, surgelés.",
            "Mettez un point d'interrogation là où vous ne savez pas : on en parlera.",
        ],
        notes="Bilan du bloc A. Les points d'interrogation font une excellente ouverture de "
              "la séance suivante.")

    return d.save(dossier)
