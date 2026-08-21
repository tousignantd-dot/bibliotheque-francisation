# -*- coding: utf-8 -*-
"""D1 · Entrez, je vais vous montrer.
Bloc D « Défi 3 · Poser mes questions sur place » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3vf` et `t3prep`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre='Entrez, je vais vous montrer',
        chapeau="Une visite dure quinze minutes. La propriétaire montre les "
                "pièces, mais elle ne dit que ce qu'on lui demande.",
        duree='75 minutes')

    d.titre(notes="Première séance du bloc D. Ouvrir en demandant au groupe ce qu'on "
                  "regarde en visitant un logement. Les réponses porteront sur ce qui se "
                  "voit ; la séance porte sur ce qui ne se voit pas et qui se demande.")

    d.objectifs([
        "comprendre où se trouve une pièce quand on vous l'explique ;",
        "employer au fond de, à côté de, au, derrière, en bas de ;",
        "poser une question pendant la visite, sans attendre ;",
        "comprendre une réponse dite vite.",
    ])

    d.dialogue('Dialogue · 1 de 3', "Voici la cuisine", [
        ("CLAUDINE", "Entrez, entrez. Vous avez trouvé facilement ?", True),
        ("DILNOZA", "Oui, merci. L'autobus arrête juste au coin.", True),
        ("CLAUDINE", "Alors voici la cuisine. Le balcon est derrière, par cette porte-là.", True),
        ("DILNOZA", "Il est grand. Est-ce que les fenêtres sont neuves ?", True),
        ("CLAUDINE", "Elles ont été changées l'an dernier. Le logement est chaud l'hiver.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire remarquer la quatrième réplique : Dilnoza pose sa première question "
             "après trente secondes de visite, sans attendre qu'on lui propose. C'est "
             "tout l'apprentissage du bloc D.")

    d.dialogue('Dialogue · 2 de 3', "Au fond du couloir", [
        ("DILNOZA", "Et les deux chambres, elles sont où ?", True),
        ("CLAUDINE", "Au fond du couloir, à côté de la salle de bain.", True),
        ("DILNOZA", "La deuxième est plus petite. C'est parfait pour mon garçon.", True),
        ("CLAUDINE", "L'école primaire est à cinq minutes à pied, sur la même rue.", True),
    ], notes="Deux petits mots de lieu dans une seule réponse : « au fond du » et « à "
             "côté de ». Les écrire au tableau au moment où ils passent — la séance les "
             "reprendra en tableau juste après.")

    d.dialogue('Dialogue · 3 de 3', "Je vais vous montrer, c'est en bas", [
        ("DILNOZA", "Est-ce qu'il y a un stationnement pour l'auto ?", True),
        ("CLAUDINE", "Non. Il n'y a pas de stationnement. On se gare dans la rue, avec une vignette.", True),
        ("DILNOZA", "Ce n'est pas grave, nous n'avons pas d'auto. Et la buanderie ?", True),
        ("THÉO", "Je vais vous montrer. Je suis Théo, le concierge. C'est en bas.", True),
        ("THÉO", "De sept heures du matin à dix heures du soir, tous les jours.", True),
    ], notes="Le concierge est un personnage à présenter : dans beaucoup d'immeubles "
             "québécois, c'est lui qui connaît vraiment le bâtiment. Lui poser des "
             "questions est normal et utile.")

    d.tableau('Analyse', "Dire où se trouve une pièce",
              ["On dit", "Ce que ça veut dire"],
              [["au fond du couloir", "tout au bout, la dernière porte"],
               ["à côté de la salle de bain", "les deux portes se touchent"],
               ["derrière la cuisine", "de l'autre côté"],
               ["en bas de l'escalier", "il faut descendre"]],
              cle=0,
              note="De + le donne toujours du : au fond du couloir.",
              notes="Diapositive à photographier. Faire montrer du doigt un endroit de la "
                    "classe pour chaque expression : le geste installe le sens mieux "
                    "qu'une traduction.")

    d.tableau('Analyse', "Au, pour un étage ou un niveau",
              ["On dit", "Où c'est"],
              [["au rez-de-chaussée", "au niveau de la rue"],
               ["au premier étage", "un escalier plus haut"],
               ["au deuxième étage", "deux escaliers plus haut"],
               ["au sous-sol", "en bas du rez-de-chaussée"]],
              cle=0,
              note="Au Québec, le premier étage n'est pas au niveau de la rue.",
              notes="Diapositive à photographier. La note est un vrai piège pour les "
                    "élèves venus de pays où le premier étage est au niveau du sol : ils "
                    "montent un escalier de trop, ou pas assez.")

    d.regle("Pendant une visite, on demande",
            "La propriétaire ne dit que ce qu'on lui demande",
            precision="Ce n'est pas de la mauvaise foi : elle ne sait pas ce "
                      "qui compte pour vous. Le stationnement, la buanderie, "
                      "la date, l'argent à donner aujourd'hui : quatre choses "
                      "qui ne se voient pas et qui ne se diront pas toutes "
                      "seules.",
            notes="Diapositive à photographier. C'est le message central du bloc D, et il "
                  "vaut bien au-delà du logement : dans une démarche, celui qui demande "
                  "obtient.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Les fenêtres ont été changées l'an dernier.", "vrai"),
        ("Les deux chambres sont au fond du couloir.", "vrai"),
        ("Il y a un stationnement pour l'auto.", "faux — on se gare dans la rue"),
        ("L'école primaire est à cinq minutes à pied.", "vrai"),
        ("Théo est le concierge de l'immeuble.", "vrai"),
        ("Dilnoza doit donner de l'argent le jour de la visite.", "faux"),
    ], corrige=True,
       notes="C'est l'exercice 1 du Défi 3. La dernière ligne annonce la séance D2 : ne "
             "pas expliquer pourquoi tout de suite, seulement noter la surprise du "
             "groupe.")

    d.pratique('Grammaire', "Où se trouve chaque pièce ?",
               "Complétez avec le petit mot qui manque.", [
        ("Les deux chambres sont ___ couloir.", "au fond du"),
        ("La deuxième chambre est ___ la salle de bain.", "à côté de"),
        ("La buanderie est ___ sous-sol.", "au"),
        ("Le balcon est ___ la cuisine.", "derrière"),
        ("Le logement est ___ deuxième étage.", "au"),
        ("Les laveuses sont ___ l'escalier.", "en bas de"),
    ], corrige=True, cols=2,
       notes="C'est l'exercice 2 du Défi 3. Faire décrire ensuite la classe ou l'école "
             "avec les mêmes expressions : la salle est au fond du couloir, la "
             "bibliothèque est à côté de la sortie.")

    d.billet(
        "Décrivez votre logement en trois phrases, avec au fond de, à côté de et au.",
        exemples=[
            "Ma chambre est ___ .",
            "La cuisine est ___ . Le logement est ___ étage.",
        ],
        notes="Devoir court. Les trois expressions obligatoires forcent la structure. "
              "Les descriptions produites servent d'échauffement en début de séance D2.")

    return d.save(dossier)
