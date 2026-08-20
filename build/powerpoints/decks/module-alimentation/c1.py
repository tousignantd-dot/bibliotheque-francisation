# -*- coding: utf-8 -*-
"""C1 · Au comptoir de la boucherie.
Bloc C « Défi 2 · Commander à un comptoir » · couleur acier · 60 min.
Source : dialogue `t2`, exercices `t2vf` et `t2cmd`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-alimentation/images/')


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre='Au comptoir de la boucherie',
        chapeau="Au comptoir, on ne se sert pas soi-même. Il faut dire ce "
                "qu'on veut, et combien. Quatre poitrines, une livre, deux "
                "cents grammes — et quelqu'un attend derrière.",
        duree='60 minutes')

    d.titre(notes="Ouverture du bloc C. Question d'entrée : « qui n'a jamais commandé à un "
                  "comptoir ici ? ». Souvent la moitié du groupe. Nommer la raison : on ne "
                  "sait pas quoi dire, et il y a du monde derrière.")

    d.objectifs([
        "commander un produit en quatre temps ;",
        "donner une quantité avec une unité juste ;",
        "faire une demande particulière : emballer à part, trancher mince ;",
        "vérifier le prix avant de repartir.",
    ])

    d.declencheur(
        'Observation', "Vous êtes le prochain. Que dites-vous ?",
        image=IMG + 'comptoir-boucherie.jpg',
        pistes=[
            "Par quoi commencez-vous ?",
            "Comment dites-vous la quantité que vous voulez ?",
            "Que faites-vous si vous ne connaissez pas le nom de la coupe ?",
            "Qu'est-ce qui vous gêne le plus, ici ?",
        ],
        notes="Cinq minutes. La troisième piste est la vraie difficulté : on peut toujours "
              "montrer du doigt et dire « celui-là », et personne ne s'en formalise.")

    d.dialogue('Dialogue · 1 de 3', "Dire ce qu'on veut, et combien", [
        ("JOHANNE", "Bonjour ! Qu'est-ce que je vous sers ?", False),
        ("FARIDA", "Bonjour. Je voudrais du poulet, s'il vous plaît. Des poitrines.", True),
        ("JOHANNE", "Combien vous en voulez ?", True),
        ("FARIDA", "Quatre. Ça fait combien de poids, à peu près ?", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Deux temps distincts : le produit, puis la quantité. La personne au comptoir "
             "les demande l'un après l'autre — c'est toujours comme ça.")

    d.dialogue('Dialogue · 2 de 3', "La demande particulière", [
        ("JOHANNE", "Quatre poitrines, ça fait environ une livre et demie. Autour de huit dollars.", False),
        ("FARIDA", "C'est parfait. Est-ce que je peux en avoir deux emballées séparément ?", True),
        ("JOHANNE", "Bien sûr. Deux et deux. Autre chose ?", True),
        ("FARIDA", "Oui, du bœuf haché. Il vous en reste du maigre ?", True),
    ], notes="« Est-ce que je peux en avoir deux emballées séparément ? » : une demande "
             "parfaitement ordinaire que beaucoup n'osent pas faire. La faire répéter.")

    d.dialogue('Dialogue · 3 de 3', "Vérifier avant de partir", [
        ("JOHANNE", "Il m'en reste, oui. Une livre, ça va ?", True),
        ("FARIDA", "Une livre, parfait. Et ça se garde combien de temps ?", True),
        ("JOHANNE", "Le haché, deux jours au frigo. C'est ce qui se garde le moins longtemps.", False),
        ("FARIDA", "Alors je vais le cuisiner demain. Merci !", False),
    ], notes="Le petit mot « en » apparaît quatre fois dans ces trois dialogues. Les faire "
             "compter : la séance C2 s'en charge.")

    d.tableau('Analyse', "Commander en quatre temps",
              ['Temps', 'Ce que je dis'],
              [["1. Le produit", "Je voudrais du poulet, s'il vous plaît."],
               ["2. La sorte ou la coupe", "Des poitrines. · Du maigre. · Tranché mince."],
               ["3. La quantité", "Quatre. · Une livre. · Deux cents grammes."],
               ["4. La vérification", "Ça fait combien ? · Ça se garde combien de temps ?"]],
              cle=0,
              note="La personne au comptoir demande les temps 2 et 3 si vous ne les donnez pas.",
              notes="Diapo centrale. Faire recopier : c'est le script complet d'une "
                    "commande.")

    d.cartes('Les demandes particulières', "Toutes parfaitement ordinaires", [
        ("Emballer séparément",
         "« Est-ce que je peux en avoir deux emballées à part ? » Utile pour congeler par "
         "portions."),
        ("Trancher mince ou épais",
         "À la charcuterie, la question est posée d'office. Répondre « mince, s'il vous "
         "plaît » suffit."),
        ("Un peu plus, un peu moins",
         "« Un peu moins, s'il vous plaît » quand la balance dépasse. Personne ne s'en "
         "formalise."),
        ("Montrer du doigt",
         "« Celui-là, s'il vous plaît. » Quand on ne connaît pas le nom de la coupe, c'est "
         "la solution la plus simple et la plus employée."),
    ], notes="La quatrième carte débloque beaucoup d'élèves. Le dire clairement : montrer "
             "du doigt n'est ni impoli ni un aveu d'ignorance.")

    d.regle("Vérifier le prix avant de partir",
            "« Ça fait combien ? » — quatre mots.",
            precision="Le poids exact est presque jamais celui qu'on a demandé : la "
                      "personne coupe un peu plus ou un peu moins. Le prix final n'est donc "
                      "jamais celui qu'on avait calculé. Le demander évite la surprise à la "
                      "caisse.",
            notes="Diapo à photographier. C'est le quatrième temps de la commande.")

    d.piege('Repartir sans avoir demandé la conservation',
            "Je le cuisinerai en fin de semaine.",
            "Ça se garde combien de temps ?",
            "Le bœuf haché tient deux jours. Acheter le mardi pour cuisiner le samedi veut "
            "dire jeter — ou congeler tout de suite, ce qui n'est possible que si on le "
            "sait au comptoir.",
            notes="Le lien avec B1 est direct. La question est la même : elle sert deux "
                  "fois.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Farida commande six poitrines.", "faux — quatre"),
        ("Quatre poitrines font environ une livre et demie.", "vrai"),
        ("Elle demande de tout emballer ensemble.", "faux — deux et deux"),
        ("Il ne reste plus de bœuf haché maigre.", "faux — il en reste"),
        ("Le bœuf haché se garde une semaine au frigo.", "faux — deux jours"),
        ("Elle décide de le cuisiner le lendemain.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte.")

    d.billet(
        "Écrivez une commande complète en quatre temps, pour un produit que vous achetez.",
        exemples=[
            "Le produit, la sorte, la quantité, la vérification.",
            "Ajoutez une demande particulière.",
        ],
        notes="Ramasser. Ces commandes servent directement au jeu de rôle de E1.")

    return d.save(dossier)
