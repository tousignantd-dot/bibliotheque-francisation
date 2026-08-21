# -*- coding: utf-8 -*-
"""A1 · La circulaire du mardi.
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.

Troisième module court du projet. L'élève de niveau 2 tient une phrase à la
fois : les diapositives portent peu de mots, et chaque phrase projetée est
une phrase qu'il pourra dire lui-même en sortant.

Ce module part d'un papier, pas d'une conversation : la situation du
programme est en compréhension écrite. La première séance sert donc à
reconnaître l'objet avant de savoir le lire.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-panier/images/')


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="La circulaire du mardi",
        chapeau="Reconnaître le papier des prix, et savoir ce qu'on y "
                "cherche : une photo, un chiffre, un mot rouge.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Apporter une vraie circulaire, si possible "
                  "plusieurs, et en donner une à chaque élève. Toute la séance se fait "
                  "avec le papier dans les mains.")

    d.objectifs([
        "reconnaître une circulaire ;",
        "y repérer une photo, un prix, un mot rouge ;",
        "nommer les objets du magasin ;",
        "dire ce qu'on achète chaque semaine.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce que ce papier ?",
        image=IMG + 'circulaire-table.jpg',
        pistes=[
            "Où avez-vous déjà vu ce papier ?",
            "Qui l'a mis dans votre boîte aux lettres ?",
            "Qu'est-ce qu'il y a dessus ?",
            "Est-ce qu'il faut le lire en entier ?",
        ],
        notes="Laisser répondre dans la langue qu'on peut. La bonne réponse à la dernière "
              "question est « non » : une circulaire se regarde, elle ne se lit pas.")

    d.dialogue('Dialogue · 1 de 2', "Un gros papier dans la boîte aux lettres", [
        ("AMINATA", "Rose, il y a un gros papier dans ma boîte aux lettres.", True),
        ("ROSE", "C'est la circulaire. Elle arrive le mardi.", True),
        ("AMINATA", "C'est un journal ?", True),
        ("ROSE", "Non. Ce sont les prix de la semaine à l'épicerie.", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Faire écouter deux fois, diapositive masquée. Puis afficher et faire "
             "répéter réplique par réplique, en chœur. Aminata est une élève comme eux ; "
             "Rose est sa voisine.")

    d.dialogue('Dialogue · 2 de 2', "Des photos et des chiffres", [
        ("AMINATA", "Il y a des photos et des chiffres.", True),
        ("ROSE", "Oui. La photo, c'est le produit. Le chiffre, c'est le prix.", True),
        ("AMINATA", "Et ce mot rouge, là ?", True),
        ("ROSE", "« Spécial ». Cette semaine, ce produit coûte moins cher.", True),
    ], notes="Faire chercher un mot rouge dans la vraie circulaire distribuée au début. "
             "Presque toutes en ont un.")

    d.tableau('Analyse', "Trois choses sur une page",
              ['Ce qu\'on voit', 'Ce que ça dit'],
              [["une photo", "le produit"],
               ["un chiffre", "le prix"],
               ["un mot rouge", "moins cher cette semaine"]],
              cle=2,
              note="On ne lit pas le reste. Trois repères suffisent pour se servir "
                   "d'une circulaire.",
              notes="Diapositive à photographier. Faire pointer les trois choses sur le "
                    "papier réel, chacun sur le sien.")

    d.vocabulaire('Vocabulaire', "Les mots du magasin", [
        ("une circulaire", "Le grand papier qui montre les prix de la semaine."),
        ("un panier", "Ce qu'on porte pour mettre ses achats dedans."),
        ("une allée", "Le chemin entre deux rangées de tablettes."),
        ("une tablette", "La planche où les produits sont posés."),
    ], notes="Diapositive à photographier. Faire répéter chaque mot avec son article : "
             "l'article s'apprend avec le mot, jamais après.")

    d.regle("Un spécial",
            "Un prix plus bas, seulement pendant quelques jours.",
            precision="Au Québec, on dit « un <b>spécial</b> » plutôt qu'« une promotion ». "
                      "« Le poulet est <b>en spécial</b> cette semaine. » Le spécial a "
                      "toujours une date : quand la semaine finit, il finit aussi.",
            notes="Diapositive à photographier. Chercher ensemble la date écrite en haut "
                  "de la circulaire : c'est elle qui dit jusqu'à quand.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("La circulaire arrive le mardi.", "vrai"),
        ("La circulaire est un journal.", "faux — ce sont les prix de la semaine"),
        ("Les chiffres de la circulaire sont les prix.", "vrai"),
        ("« Spécial » veut dire plus cher.", "faux — moins cher"),
    ], corrige=True, cols=1,
       notes="Quatre énoncés seulement. Les faire d'abord à l'oral, en groupe, avant de "
             "les faire écrire.")

    d.pratique('Pratique · à deux', "Trois produits en spécial",
               "Deux par deux, avec la circulaire distribuée au début.", [
        ("Étape 1", "Trouvez trois produits avec un mot rouge."),
        ("Étape 2", "Montrez la photo à votre voisin et nommez le produit."),
        ("Étape 3", "Montrez le chiffre du prix, sans le dire encore."),
        ("Étape 4", "Dites lequel des trois vous achèteriez."),
    ], cols=1,
       notes="Vingt minutes. On ne dit pas encore les prix à voix haute : c'est la séance "
             "B1 qui apprend à les dire. Ici, on repère seulement.")

    d.billet(
        "Écrivez trois produits que vous achetez chaque semaine.",
        exemples=[
            "J'achète du lait.",
            "J'achète du riz.",
            "J'achète des pommes.",
        ],
        notes="Devoir court. Demander des produits qu'ils achètent vraiment : ce sont eux "
              "qui reviendront dans tout le module.")

    return d.save(dossier)
