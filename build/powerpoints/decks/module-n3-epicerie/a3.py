# -*- coding: utf-8 -*-
"""A3 · Comment une épicerie est rangée.
Bloc A « Je découvre » · couleur teal · 60 min.
Source : exercice `prTrouver` et son savoir, exercice `prImg`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-epicerie/images/')


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre='Comment une épicerie est rangée',
        chapeau="Ce n'est pas un hasard : le frais sur les murs, les boîtes "
                "au milieu, le lourd en bas. Comprendre le plan, c'est "
                "trouver sans chercher.",
        duree='60 minutes')

    d.titre(notes="Si possible, projeter le plan d'une épicerie du quartier — plusieurs "
                  "chaînes en publient un. Sinon, faire dessiner le plan au tableau par le "
                  "groupe.")

    d.objectifs([
        "lire une affichette d'allée ;",
        "savoir où se trouve le frais ;",
        "savoir où se trouvent les grands formats ;",
        "nommer huit endroits et objets de l'épicerie.",
    ])

    d.declencheur(
        'Observation', "Que dit ce panneau ?",
        image=IMG + 'affichette-rayon.jpg',
        pistes=[
            "Où est-il placé ?",
            "Qu'est-ce qu'il annonce ?",
            "Le lit-on avant ou après être entré dans l'allée ?",
            "Combien de temps ça prend, de le lire ?",
        ],
        notes="L'affichette se lit du bout de l'allée, avant d'y entrer. Trois secondes "
              "évitent de parcourir la rangée entière.")

    d.tableau('Analyse', "Le plan d'une épicerie",
              ['Où', 'Ce qu\'on y trouve'],
              [["Sur les murs", "les fruits, la viande, le lait, le pain"],
               ["Au milieu", "les boîtes, les sacs, les conserves"],
               ["Une allée à part", "les produits du monde"],
               ["À la sortie", "les caisses, et le service à la clientèle"]],
              cle=0,
              note="Le frais a besoin de réfrigérateurs, et les réfrigérateurs sont contre les murs.",
              notes="Diapo à photographier. La note explique le « pourquoi », qui rend le "
                    "plan facile à retenir.")

    d.regle("Les grands formats sont en bas",
            "Le lourd se range à hauteur des genoux.",
            precision="Le format le plus vendu est placé à hauteur des yeux ; les grands "
                      "sacs et les grosses bouteilles sont sur la tablette du bas, parce "
                      "qu'ils sont lourds. Si vous ne voyez pas ce que vous cherchez, "
                      "<b>baissez les yeux</b> avant de conclure qu'il n'y en a plus.",
            notes="Diapo à photographier. Beaucoup de gens repartent en croyant qu'un "
                  "produit est épuisé alors qu'il est à leurs pieds.")

    d.cartes("Trois mots à ne pas confondre", "Allée, rayon, tablette", [
        ("Une allée",
         "Le passage entre deux rangées. Elle porte un numéro, suspendu au bout."),
        ("Un rayon",
         "La famille de produits : le rayon des fruits, le rayon de la viande. Ce n'est pas "
         "un lieu numéroté."),
        ("Une tablette",
         "La planche où les produits sont posés. Il y en a du bas jusqu'en haut dans chaque "
         "allée."),
    ], notes="Les trois s'emploient tous les jours et se confondent facilement. Faire "
             "produire une phrase avec chacun.")

    d.piege("Croire qu'il n'y en a plus",
            "Il n'y a pas de riz, la tablette est vide.",
            "Regarder en bas, et demander.",
            "Le grand format est en bas, le petit à hauteur des yeux, et parfois une "
            "deuxième place existe ailleurs dans le magasin — le riz peut être avec les "
            "pâtes et aussi dans les produits du monde.",
            notes="Lien avec A1 : un produit peut avoir deux emplacements.")

    d.pratique('Pratique · 1 de 2', "Où est-ce ?",
               "Sur les murs, au milieu, ou dans une allée à part ?", [
        ("Le lait", "sur les murs — au réfrigérateur"),
        ("Les pâtes", "au milieu"),
        ("Les pommes", "sur les murs, souvent près de l'entrée"),
        ("La farine de maïs", "l'allée des produits du monde"),
        ("Les conserves de tomates", "au milieu"),
        ("Le pain frais", "sur les murs, près de la boulangerie"),
    ], corrige=True,
       notes="Faire justifier : le frais a besoin de froid, donc de murs.")

    d.pratique('Pratique · 2 de 2', "Le mot juste",
               "Allée, rayon ou tablette ?", [
        ("« C'est dans l'___ douze. »", "allée"),
        ("« Le ___ des fruits est à l'entrée. »", "rayon"),
        ("« Les grands sacs sont sur la ___ du bas. »", "tablette"),
        ("« Cette ___ est vide, il n'y en a plus. »", "tablette"),
    ], corrige=True, cols=1,
       notes="Exercice court. Dix minutes suffisent.")

    d.billet(
        "Dessinez le plan de votre épicerie, de mémoire.",
        exemples=[
            "Où sont les fruits, la viande, le lait, le pain ?",
            "Combien d'allées ? Où sont les caisses ?",
        ],
        notes="Devoir agréable et révélateur : la plupart des élèves connaissent le plan "
              "sans jamais y avoir pensé.")

    return d.save(dossier)
