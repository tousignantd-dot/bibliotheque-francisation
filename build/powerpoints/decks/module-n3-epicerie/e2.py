# -*- coding: utf-8 -*-
"""E2 · Je retiens des mots.
Bloc E « Je me lance » · couleur foret · 60 min.
Source : cartes mémoire, banc de vocabulaire et autoévaluation du module.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='foret',
        titre='Je retiens des mots',
        chapeau="Quinze mots, six points de langue, huit questions. Dernière "
                "séance : on rassemble, on révise, et chacun fait le point.",
        duree='60 minutes')

    d.titre(notes="Séance de bilan. Rendre tous les billets corrigés du module avant de "
                  "commencer.")

    d.objectifs([
        "rassembler le vocabulaire du module en trois familles ;",
        "réviser avec les cartes mémoire, seul ou à deux ;",
        "reformuler les points de langue en une phrase chacun ;",
        "évaluer honnêtement ce que je suis maintenant capable de faire.",
    ])

    d.vocabulaire('Famille · 1 de 3', "Dans le magasin", [
        ("une allée", "Le passage entre deux rangées. Elle porte un numéro."),
        ("une affichette", "Le panneau au-dessus de l'allée."),
        ("une tablette", "La planche où les produits sont posés."),
        ("un panier", "Le contenant qu'on porte ou qu'on pousse."),
        ("un dépanneur", "Le petit commerce ouvert tard."),
    ], notes="« Dépanneur » est un mot d'ici. En France, on dirait « supérette ».")

    d.vocabulaire('Famille · 2 de 3', "Choisir", [
        ("la circulaire", "Le journal des spéciaux de la semaine."),
        ("un spécial", "Un prix réduit pendant quelques jours."),
        ("une livre", "Environ 450 grammes — un peu moins d'un demi-kilo."),
        ("un paquet", "Ce qui contient plusieurs morceaux ensemble."),
        ("une boîte de conserve", "La boîte de métal qui garde longtemps."),
        ("une mise en garde", "Le dessin qui avertit d'un danger."),
    ], notes="« Un spécial » comme nom est propre au Québec : ailleurs on dit « une "
             "promotion ».")

    d.vocabulaire('Famille · 3 de 3', "À la caisse", [
        ("la caisse", "L'endroit où on paie, à la sortie."),
        ("la facture", "Le papier qui montre ce qu'on a payé."),
        ("un sac réutilisable", "Le sac solide qu'on rapporte chaque semaine."),
        ("la carte de points", "La carte gratuite qui donne des rabais."),
    ], notes="Ces quatre mots reviennent à chaque passage à la caisse, toutes les semaines.")

    d.tableau('Les points de langue', "Une phrase chacun",
              ['Le point', 'En une phrase'],
              [["treize ou trente", "c'est la fin du mot qui décide"],
               ["dire où c'est", "un numéro, une position, une hauteur"],
               ["demander de l'aide", "excusez-moi, puis la question"]],
              cle=0,
              note="Trois autres au tableau suivant.",
              notes="Faire reformuler chaque ligne par un élève différent avant d'afficher "
                    "la colonne de droite.")

    d.tableau('Les points de langue', "Une phrase chacun (suite)",
              ['Le point', 'En une phrase'],
              [["les mots qui mesurent", "un contenant ou un poids, puis « de »"],
               ["les dessins qui avertissent", "poison, corrosif, inflammable, explosif"],
               ["lire une facture", "sous-total, taxes, total, économies"]],
              cle=1,
              notes="La ligne du milieu est celle que les élèves rapportent le plus souvent "
                    "comme utile à la maison.")

    d.regle("Ce qu'il faut retenir du module",
            "Demander coûte une minute ; chercher en coûte vingt.",
            precision="Marisol n'a pas appris le nom de tous les produits d'une épicerie. "
                      "Elle a appris quatre phrases : attirer l'attention, demander où "
                      "c'est, faire répéter un chiffre, remercier. C'est ce qui lui permet "
                      "de faire ses courses seule, dans n'importe quel magasin.",
            notes="Diapo à photographier. C'est la phrase de clôture du module.")

    d.cartes('Réviser seul', "Trois façons de le faire", [
        ("Les cartes mémoire",
         "Dans l'activité interactive, section « Je retiens des mots ». La traduction est "
         "masquée par défaut."),
        ("Les trois exercices de vocabulaire",
         "Le mot et sa définition, le mot et l'image, le mot à écrire. Les mêmes quinze "
         "mots."),
        ("Les six mini-leçons",
         "Six panneaux « En apprendre plus », avec de l'audio. Ils restent accessibles "
         "après la fin du module."),
    ], notes="Montrer les trois à l'écran, une minute chacun.")

    d.billet(
        "Autoévaluation : pour chaque énoncé, pas encore, un peu, ou oui.",
        exemples=[
            "Je peux demander où se trouve un produit.",
            "Je fais la différence entre treize et trente, quinze et cinquante.",
            "Je peux dire une quantité : un paquet de, un kilo de.",
            "Je reconnais les dessins de mise en garde et je sais lire ma facture.",
        ],
        notes="L'autoévaluation complète est dans l'activité interactive. La faire remplir "
              "là : elle est conservée avec les traces de l'élève.")

    return d.save(dossier)
