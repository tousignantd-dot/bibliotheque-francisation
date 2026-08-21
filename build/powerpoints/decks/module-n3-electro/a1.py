# -*- coding: utf-8 -*-
"""A1 · Ma laveuse est brisée.
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-electro/images/')


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre='Ma laveuse est brisée',
        chapeau="Un appareil qui lâche, c'est une dépense de plusieurs "
                "centaines de dollars et une semaine de démarches. Avant de "
                "comparer quoi que ce soit, il faut savoir comment ça "
                "s'appelle.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Demander au groupe quel appareil a lâché "
                  "chez eux depuis leur arrivée, et comment ils l'ont remplacé. Les "
                  "réponses donnent des exemples réels pour toute la semaine.")

    d.objectifs([
        "nommer les appareils de la maison ;",
        "reconnaître ceux qui coûtent cher et durent longtemps ;",
        "comprendre une conversation entre voisines sur un achat ;",
        "dire qu'un appareil est brisé.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qui coûte le plus cher dans un logement ?",
        image=IMG + 'refrigerateurs-alignes.jpg',
        pistes=[
            "Quels appareils sont déjà là quand on loue ?",
            "Lesquels faut-il acheter soi-même ?",
            "Combien de temps dure une laveuse, à votre avis ?",
            "Qu'est-ce qu'on fait quand un appareil brise ?",
        ],
        notes="Laisser venir les mots dans n'importe quelle langue, puis les traduire "
              "ensemble au tableau. C'est la liste de vocabulaire du module qui se "
              "construit toute seule. Noter que dans beaucoup de logements d'ici, la "
              "cuisinière et le réfrigérateur sont fournis, mais pas la laveuse.")

    d.dialogue('Dialogue · 1 de 3', "Elle a quel âge, ta laveuse ?", [
        ("MARISOL", "Louise ! Ma laveuse est brisée. Elle s'est arrêtée au milieu du lavage.", True),
        ("LOUISE", "Ah non. Elle a quel âge, ta laveuse ?", True),
        ("MARISOL", "Elle était là quand je suis arrivée. Peut-être quinze ans.", True),
        ("LOUISE", "Quinze ans, c'est vieux. Le réparateur va coûter presque le prix d'une neuve.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="« Elle est brisée » est la phrase de départ du module. La faire répéter "
             "avec trois autres appareils : le réfrigérateur, la cuisinière, l'aspirateur.")

    d.dialogue('Dialogue · 2 de 3', "J'ai la circulaire sur la table", [
        ("MARISOL", "Une laveuse neuve, c'est très cher ?", True),
        ("LOUISE", "Ça dépend. Attends, j'ai la circulaire du magasin sur la table.", True),
        ("MARISOL", "La circulaire ? C'est le papier qui arrive dans la boîte aux lettres ?", True),
        ("LOUISE", "Oui, celui-là. Regarde : il y a des laveuses, des sécheuses, des réfrigérateurs.", True),
    ], notes="Le mot « circulaire » apparaît ici pour la première fois. Ne pas le définir "
             "tout de suite : Marisol le fait elle-même à la réplique suivante, et c'est "
             "le modèle de la stratégie qu'on veut enseigner.")

    d.dialogue('Dialogue · 3 de 3', "Ça, c'est quoi ?", [
        ("MARISOL", "Et ça, la petite machine noire, c'est quoi ?", True),
        ("LOUISE", "Ça, c'est un four à micro-ondes. Et à côté, c'est un aspirateur.", True),
        ("MARISOL", "D'accord. Une laveuse, une sécheuse, un réfrigérateur, un micro-ondes.", True),
        ("LOUISE", "Tu apprends vite. Regarde le gros chiffre : celle-là est en spécial cette semaine.", True),
    ], notes="« Ça, c'est quoi ? » avec le doigt : c'est la question la plus rentable du "
             "niveau. La faire dire à voix haute par tout le groupe.")

    d.tableau('Analyse', "Les appareils, par ce qu'ils font",
              ["Ce qu'on veut faire", "L'appareil"],
              [["laver et sécher le linge", "une laveuse, une sécheuse"],
               ["garder la nourriture au froid", "un réfrigérateur"],
               ["cuire et réchauffer", "une cuisinière, un micro-ondes"],
               ["nettoyer le plancher", "un aspirateur"]],
              cle=1,
              note="Chaque appareil se retient avec son article : un ou une.",
              notes="Diapo à photographier. Faire nommer chaque ligne par un élève "
                    "différent, avec l'article.")

    d.regle("Dire qu'un appareil ne marche plus",
            "« Ma laveuse est brisée. »",
            precision="C'est le mot d'ici : au Québec, un appareil est « brisé », pas "
                      "« cassé ». On peut aussi dire « elle ne marche plus » ou « elle "
                      "ne fonctionne plus ». Les trois se comprennent partout.",
            notes="Diapo à photographier. Faire répéter la phrase à voix haute par tout "
                  "le groupe, deux fois, avec trois appareils différents.")

    d.cartes("Ce qu'on achète une fois par dix ans", "Quatre familles", [
        ("Les gros appareils",
         "une laveuse, une sécheuse, un réfrigérateur, une cuisinière. Ils coûtent des "
         "centaines de dollars et se livrent en camion."),
        ("Les petits appareils",
         "un micro-ondes, un grille-pain, un aspirateur. Ils se transportent à la main "
         "et coûtent entre cinquante et deux cents dollars."),
        ("L'électronique",
         "un ordinateur portable, un téléphone, un téléviseur. On les achète aussi en "
         "ligne, sur le site du magasin."),
        ("Le reste de la maison",
         "la literie, les outils, la vaisselle, l'équipement de jardinage. Ce sont aussi "
         "des biens durables : on les garde des années."),
    ], notes="Ces quatre familles sont exactement celles du programme. Demander au groupe "
             "dans quelle famille se range chaque appareil de leur logement.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("La laveuse de Marisol s'est arrêtée pendant le lavage.", "vrai"),
        ("La laveuse est neuve : elle a deux ans.", "faux — peut-être quinze ans"),
        ("Louise pense que la réparation va coûter cher.", "vrai"),
        ("La petite machine noire est un aspirateur.", "faux — un micro-ondes"),
        ("Une laveuse de la circulaire est en spécial cette semaine.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte.")

    d.billet(
        "Écrivez cinq appareils qu'il y a chez vous.",
        exemples=[
            "Avec leur article : une laveuse, un micro-ondes…",
            "Et dites lequel est le plus vieux.",
        ],
        notes="Devoir court. Il prépare la séance A4 sur le genre des appareils et donne "
              "des exemples personnels pour le défi 1.")

    return d.save(dossier)
