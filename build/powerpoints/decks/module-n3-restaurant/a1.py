# -*- coding: utf-8 -*-
"""A1 · Chez Marcel, on commande au comptoir.
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-restaurant/images/')


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre='Chez Marcel, on commande au comptoir',
        chapeau="Dans un casse-croûte, personne ne vient à la table. On fait "
                "la file, on commande, on paie, et on attend son numéro. "
                "Quatre gestes, et une heure de dîner qui suffit.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Demander au groupe où ils dînent le midi, "
                  "et qui a déjà commandé au comptoir en français. Les réponses donnent "
                  "des exemples réels pour toute la semaine.")

    d.objectifs([
        "reconnaître un casse-croûte et son comptoir ;",
        "savoir où est le menu et comment il est fait ;",
        "comprendre une conversation entre deux camarades de classe ;",
        "nommer les quatre gestes d'une commande au comptoir.",
    ])

    d.declencheur(
        'Observation', "Où est le menu, dans cet endroit-là ?",
        image=IMG + 'file-comptoir.jpg',
        pistes=[
            "Qu'est-ce que ces personnes attendent ?",
            "Est-ce qu'un serveur va venir à leur table ?",
            "Où faut-il regarder pour voir ce qu'il y a à manger ?",
            "Qu'est-ce qu'on fait après avoir commandé ?",
        ],
        notes="Laisser venir les mots dans n'importe quelle langue, puis les traduire "
              "ensemble au tableau. Beaucoup d'élèves connaissent le service aux tables "
              "de leur pays d'origine, mais pas la file au comptoir : c'est là que se "
              "joue toute la différence du module.")

    d.dialogue('Dialogue · 1 de 3', "On commande au comptoir", [
        ("YOLETTE", "Fatou, on mange où ce midi ? J'ai seulement une heure.", True),
        ("FATOU", "Chez Marcel, le casse-croûte au coin. On commande au comptoir, c'est vite.", True),
        ("YOLETTE", "Il n'y a pas de serveur ?", True),
        ("FATOU", "Non. Tu fais la file, tu commandes, tu paies, et on t'appelle quand c'est prêt.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="La quatrième réplique donne les quatre gestes du module dans l'ordre. La "
             "faire répéter, puis la faire redire par un élève sans regarder l'écran.")

    d.dialogue('Dialogue · 2 de 3', "Regarde en haut", [
        ("YOLETTE", "Et le menu ? Je ne vois pas de papier sur les tables.", True),
        ("FATOU", "Regarde en haut, au-dessus de la caisse. Le grand tableau, c'est le menu.", True),
        ("YOLETTE", "Ah oui. Il y a des photos et des colonnes de chiffres.", True),
        ("FATOU", "À gauche, ce que tu manges. À droite, le prix. En bas, les breuvages.", True),
    ], notes="C'est la découverte centrale de la séance : le menu n'est pas un papier "
             "qu'on tient, c'est un panneau qu'on lit de loin. Demander qui a déjà eu "
             "de la difficulté à le lire assez vite dans la file.")

    d.dialogue('Dialogue · 3 de 3', "Trois formats", [
        ("YOLETTE", "Et les trois chiffres à côté de la soupe ?", True),
        ("FATOU", "Ce sont les trois formats : petit, moyen, grand.", True),
        ("YOLETTE", "Trois prix pour la même soupe. D'accord.", True),
        ("FATOU", "Prends ton plateau au bout du comptoir. Les serviettes sont là aussi.", True),
    ], notes="Le mot « format » apparaît ici pour la première fois. Ne pas l'expliquer "
             "davantage : la séance A4 lui est consacrée entièrement.")

    d.tableau('Analyse', "Les quatre gestes de la commande",
              ["Dans l'ordre", "Ce qu'on fait"],
              [["1. La file", "on prend un plateau et on attend son tour"],
               ["2. La commande", "on dit ce qu'on veut, on choisit un format"],
               ["3. La caisse", "on paie et on reçoit un numéro"],
               ["4. Le ramassage", "on attend son numéro, puis on prend son repas"]],
              cle=1,
              note="Les quatre gestes sont toujours dans cet ordre, partout.",
              notes="Diapo à photographier. Faire nommer chaque ligne par un élève "
                    "différent. C'est le plan du module entier.")

    d.regle("L'endroit et son nom",
            "« un casse-croûte »",
            precision="C'est le mot d'ici pour un petit restaurant rapide, sans "
                      "service aux tables. On dit aussi « une cantine » dans une "
                      "école ou un hôpital. Ce qui les réunit : on commande au "
                      "comptoir et on porte son plateau soi-même.",
            notes="Diapo à photographier. Faire répéter le mot à voix haute par tout le "
                  "groupe : le trait d'union et l'accent circonflexe se voient à l'écrit, "
                  "mais le mot se dit d'un seul souffle.")

    d.cartes("Les mots de l'endroit", "Quatre mots", [
        ("le comptoir",
         "Le long meuble haut où on commande et où on paie. On y appuie les coudes, on "
         "y pose son plateau, et on y attend son tour."),
        ("le tableau du menu",
         "Le grand panneau accroché au-dessus de la caisse. Il ne se prend pas dans les "
         "mains : il se lit de loin, avant d'arriver devant le préposé."),
        ("un plateau",
         "Le carré de plastique qui porte tout le repas d'une seule main. Il se prend au "
         "début du comptoir, jamais à la fin."),
        ("la caisse",
         "L'endroit du comptoir où on paie. Beaucoup de casse-croûte prennent le comptant "
         "et le débit, mais pas la carte de crédit."),
    ], notes="Faire dire chaque mot avec son article. Les quatre reviennent dans toutes "
             "les séances du module.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Chez Marcel, un serveur vient prendre la commande à la table.", "faux — on commande au comptoir"),
        ("On paie après avoir commandé.", "vrai"),
        ("Le menu est un papier posé sur les tables.", "faux — un tableau au-dessus de la caisse"),
        ("Les prix sont écrits à droite du tableau.", "vrai"),
        ("Les trois chiffres à côté de la soupe sont trois formats.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte du dialogue.")

    d.billet(
        "Écrivez où vous dînez le midi, et comment ça se passe.",
        exemples=[
            "Est-ce qu'il y a un comptoir ou un service aux tables ?",
            "Où est le menu : sur la table, ou au mur ?",
        ],
        notes="Devoir court. Il prépare la séance A3 sur le vocabulaire de l'endroit et "
              "donne des exemples personnels pour le défi 1.")

    return d.save(dossier)
