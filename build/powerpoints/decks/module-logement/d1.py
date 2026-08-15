# -*- coding: utf-8 -*-
"""D1 · Quatre personnes, quatre besoins.
Bloc D · couleur teal (lire et répondre) · 60 min.
Source : exercices `t3img` et `t3besoins`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/assets/'
       'interactive/module-logement/images/')


def build(dossier):
    d = Deck(
        code='D1', section='teal',
        titre='Quatre personnes, quatre besoins',
        chapeau="Une étudiante sans auto, une famille avec des jumeaux, un travailleur de "
                "nuit, deux colocataires qui cuisinent. Quatre vies, et aucun logement "
                "ne convient aux quatre.",
        duree='60 minutes')

    d.titre(notes="Ouverture du défi 3. C'est la synthèse du module : ce qui compte "
                  "dépend de qui cherche. Le dire d'entrée.")

    d.objectifs([
        "déduire les besoins d'une personne de sa situation ;",
        "associer un logement à une personne ;",
        "justifier une recommandation ;",
        "distinguer un besoin d'une préférence.",
    ])

    d.declencheur(
        'Mise en situation', "À qui ce logement conviendrait-il ?",
        image=IMG + 'studio-etudiante.jpg',
        pistes=[
            "Combien de personnes peuvent y vivre ?",
            "Qu'est-ce qui manque, et pour qui est-ce un problème ?",
            "Quel serait l'avantage principal ?",
            "À qui le déconseilleriez-vous ?",
        ],
        notes="Trois minutes. La dernière question est la plus formatrice : nommer à qui "
              "cela ne convient pas précise à qui cela convient.")

    d.tableau('Analyse', "Quatre logements, quatre profils",
              ['Le logement', 'À qui il convient'],
              [["un studio meublé avec cuisinette", "une étudiante seule, petit budget"],
               ["une entrée de plain-pied, sans marche", "une famille avec une poussette"],
               ["une chambre tranquille, chien accepté", "un travailleur de nuit"],
               ["une grande cuisine avec longue table", "deux colocataires qui reçoivent"]],
              cle=0, props=[0.44, 0.56],
              notes="Faire deviner la colonne de droite avant de l'afficher. Le groupe y "
                    "arrivera presque toujours.")

    d.regle('La règle du défi 3',
            "Un besoin n'est pas une préférence.",
            precision="La famille avec une poussette a BESOIN d'une entrée sans marches : "
                      "sans cela, elle ne peut pas entrer. Les colocataires PRÉFÈRENT "
                      "une grande cuisine : ils peuvent vivre sans. Le besoin passe "
                      "avant.",
            notes="Diapo centrale du défi. Faire classer trois exigences du groupe en "
                  "besoins et préférences : la discussion est utile.")

    d.pratique('Pratique · 1 de 4', "À qui convient ce logement ?",
               "Associez le logement et la personne.", [
        ("Un petit studio meublé, avec une cuisinette dans la même pièce.",
         "une étudiante seule qui cherche un petit loyer"),
        ("Une entrée de plain-pied, sans aucune marche.",
         "une famille avec une poussette"),
        ("Une chambre tranquille avec de gros rideaux, et un chien accepté.",
         "un travailleur de nuit qui a un chien"),
        ("Une grande cuisine avec une longue table.",
         "deux colocataires qui cuisinent et reçoivent"),
    ], corrige=True,
       notes="Faire l'exercice avec les images du module. Cette diapo sert de correction "
             "et de trace écrite.")

    d.pratique('Pratique · 2 de 4', "Quels sont leurs besoins ?",
               "Déduisez de la situation.", [
        ("« Je suis étudiante au cégep et je n'ai pas d'auto. Je veux quelque chose de "
         "petit et de pas cher, près de l'autobus. »",
         "un 2 ½ ou 3 ½ abordable, près d'un arrêt et du cégep"),
        ("« Nous venons d'avoir des jumeaux et ma mère habite avec nous. Monter un "
         "escalier avec la poussette, c'est impossible. »",
         "un grand logement au rez-de-chaussée, près d'une garderie"),
        ("« Je travaille de nuit à l'usine et je dors le jour. J'ai un vieux chien "
         "tranquille. »",
         "un logement calme et bien insonorisé, où les chiens sont acceptés"),
        ("« Nous sommes deux colocataires. On cuisine beaucoup et on reçoit des amis "
         "presque chaque fin de semaine. »",
         "un 4 ½ avec deux chambres fermées et une grande cuisine"),
    ], corrige=True,
       notes="Faire relever, dans chaque citation, les mots qui donnent le besoin : "
             "« pas d'auto », « impossible », « je dors le jour », « deux ».")

    d.cartes('Analyse', "Quatre besoins que l'annonce ne nomme jamais", [
        ("L'accessibilité",
         "Une entrée sans marches, un ascenseur, une porte assez large. Les annonces "
         "disent « rez-de-chaussée », rarement « accessible »."),
        ("Le calme réel",
         "Une annonce dit « quartier tranquille », jamais « le camion passe à cinq "
         "heures ». Il faut le demander."),
        ("La proximité utile",
         "Près de quoi, exactement ? D'un arrêt d'autobus, d'une garderie, d'une "
         "épicerie ? « Bien situé » ne veut rien dire."),
        ("La possibilité de recevoir",
         "Une grande cuisine, une table, des voisins tolérants. Cela ne s'écrit jamais, "
         "et cela se voit pendant la visite."),
    ], notes="Ces quatre besoins expliquent pourquoi la visite compte autant que "
             "l'annonce. Le dire.")

    d.piege("Le piège du besoin confondu avec la préférence",
            "J'ai besoin d'une grande cuisine.",
            "Je préfère une grande cuisine, mais j'ai besoin d'un logement au rez-de-chaussée.",
            "Quand tout devient un besoin, on ne trouve rien. Séparez ce sans quoi vous "
            "ne pouvez pas vivre de ce qui vous ferait plaisir. Deux ou trois vrais "
            "besoins suffisent à orienter une recherche.",
            notes="Faire écrire à chacun ses deux vrais besoins. La plupart en écriront "
                  "cinq d'abord, puis couperont.")

    d.pratique('Pratique · 3 de 4', "Besoin ou préférence ?",
               "Peut-on vivre sans ?", [
        ("Une entrée sans marches, avec une poussette et une mère âgée.", "un besoin"),
        ("Une grande cuisine pour recevoir des amis.", "une préférence"),
        ("Un logement près de l'autobus, sans auto.", "un besoin"),
        ("Des murs d'une autre couleur.", "une préférence"),
        ("Un logement où les chiens sont acceptés, avec un chien.", "un besoin"),
    ], corrige=True,
       notes="Le cinquième item se discute : on peut donner son chien. Laisser le groupe "
             "argumenter — c'est justement la limite entre besoin et préférence.")

    d.pratique('Pratique · 4 de 4', "Recommandez un logement",
               "Une des trois annonces de la séance A4, avec la raison.", [
        ("Pour l'étudiante sans auto", "le 3 ½ à 780 $ — le moins cher, chauffé"),
        ("Pour la famille avec des jumeaux",
         "le 5 ½ — trois chambres, école et parc à cinq minutes"),
        ("Pour le travailleur de nuit", "le 4 ½ — la chambre donne sur la cour"),
        ("Pour les deux colocataires", "le 4 ½ — deux chambres fermées"),
    ], corrige=True,
       notes="Le 4 ½ convient à deux profils, pour des raisons différentes. Le faire "
             "remarquer : un logement peut convenir à plusieurs vies.")

    d.billet(
        "Écrivez vos deux vrais besoins et vos deux préférences.",
        exemples=[
            "Deux de chaque, pas plus.",
            "Un besoin, c'est ce sans quoi vous ne pouvez pas vivre dans ce logement.",
        ],
        notes="Ramasser. Ces quatre lignes serviront en E1, où chacun choisira une "
              "annonce selon ses propres critères.")

    return d.save(dossier)
