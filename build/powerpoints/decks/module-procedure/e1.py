# -*- coding: utf-8 -*-
"""E1 · À toi : expliquer et rédiger une procédure.
Bloc E · couleur teal (je me lance) · 90 min.
Source : section `appli` — expliquer une procédure à l'oral, puis par écrit.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre='À toi : expliquer et rédiger',
        chapeau="Tout le module en une séance. Expliquer une procédure à un collègue à "
                "voix haute, puis la rédiger pour quelqu'un qui ne sera pas là pour "
                "poser des questions.",
        duree='90 minutes')

    d.titre(notes="Séance d'application. Aucun contenu nouveau. Un tiers d'oral, un "
                  "tiers d'écrit, un tiers de relecture croisée.")

    d.objectifs([
        "expliquer une procédure en cinq étapes, à voix haute ;",
        "répondre aux questions d'un collègue ;",
        "rédiger une procédure à l'impératif ;",
        "relire une procédure écrite par quelqu'un d'autre et la tester.",
    ])

    d.regle("À l'oral · la règle",
            "Une étape par phrase, un mot d'ordre au début, et on vérifie à la fin.",
            precision="D'abord, ensuite, puis, après ça, enfin. Et à la fin : « Est-ce "
                      "que c'est clair, ou tu veux que je reprenne une étape ? » Cette "
                      "dernière question fait toute la différence.",
            notes="Écrire les mots d'ordre et la question finale au tableau. C'est le "
                  "modèle de l'exercice oral.")

    d.pratique('Pratique · 1 de 4', "Jeu de rôle · expliquer à un collègue",
               "À deux. L'un explique, l'autre pose des questions. Puis on échange.", [
        ("Le collègue demande", "Comment je fais pour me faire rembourser ?"),
        ("Vous expliquez", "cinq étapes, un mot d'ordre par étape"),
        ("Le collègue demande", "Est-ce que la photo est obligatoire ?"),
        ("Le collègue demande", "Ça prend combien de temps ?"),
        ("Vous vérifiez", "Est-ce que c'est clair, ou tu veux que je reprenne ?"),
    ], corrige=False,
       notes="Vingt minutes. Circuler et vérifier deux choses : les mots d'ordre, et la "
             "question finale. Ne pas corriger la langue pendant l'échange.")

    # ── l'écrit ────────────────────────────────────────────────────
    d.regle("À l'écrit · la règle",
            "L'impératif, une étape par ligne, numérotées.",
            precision="À l'écrit, personne ne peut poser de question. Chaque étape doit "
                      "donc être complète et sans ambiguïté : « Prenez une photo "
                      "claire du reçu, directement avec l'application. »",
            notes="Comparer avec l'oral : à l'oral on peut dire « tu prends une photo » "
                  "et préciser après. À l'écrit, la précision doit être là du premier "
                  "coup.")

    d.tableau('Analyse', "Une procédure écrite, en cinq lignes",
              ['Rang', 'La ligne'],
              [["1", "Ouvrez l'application Ressources+."],
               ["2", "Appuyez sur Nouvelle demande."],
               ["3", "Prenez une photo claire du reçu, avec l'application."],
               ["4", "Inscrivez le montant exact et choisissez la catégorie."],
               ["5", "Appuyez sur Envoyer et attendez l'approbation."]],
              cle=0, props=[0.1, 0.9],
              note="Cinq lignes numérotées, cinq verbes à l'impératif. Aucun mot "
                   "d'ordre : la numérotation les remplace.",
              notes="Faire remarquer que les mots d'ordre disparaissent à l'écrit. Les "
                    "numéros font le même travail, plus efficacement.")

    d.cartes('Écrire', "Quatre choses à ajouter à une procédure écrite", [
        ("Ce qui est obligatoire",
         "« La photo est obligatoire, sinon la demande est refusée. » Une ligne "
         "séparée, en fin de procédure."),
        ("Le délai",
         "« Comptez environ dix jours ouvrables après l'approbation. » Le lecteur "
         "n'aura personne à qui le demander."),
        ("Quoi faire si ça bloque",
         "« En cas de problème, communiquez avec les finances, au poste 6. » C'est le "
         "troisième bloc de toute directive, vu en D1."),
        ("Ce qu'il faut garder",
         "« Conservez votre reçu original jusqu'au versement. » Le conseil qui évite "
         "le plus de refus."),
    ], notes="Ces quatre ajouts transforment une liste d'étapes en vraie directive. Les "
             "faire cocher un par un pendant la rédaction.")

    d.pratique('Pratique · 2 de 4', "Rédigez la procédure",
               "Cinq étapes numérotées à l'impératif, plus les quatre ajouts.", [
        ("La procédure", "la demande de remboursement, du début au versement"),
        ("Pour qui", "un nouveau collègue qui commence lundi"),
        ("À ne pas oublier", "obligation, délai, quoi faire si ça bloque, ce qu'il faut garder"),
    ], corrige=False,
       notes="Vingt-cinq minutes d'écriture individuelle. Circuler et aider sur la forme "
             "de l'impératif, pas sur le contenu.")

    d.pratique('Pratique · 3 de 4', "Testez la procédure d'un autre",
               "Échangez les feuilles. Suivez la procédure ligne par ligne.", [
        ("Est-ce que chaque ligne dit une seule action ?", "sinon, la couper en deux"),
        ("Est-ce que chaque verbe est à l'impératif ?", "Ouvrez, prenez, inscrivez"),
        ("Est-ce qu'il manque une précision ?", "claire, exact, bonne catégorie"),
        ("Est-ce que le délai est écrit ?", "et à partir de quand il court"),
        ("Est-ce qu'on sait quoi faire si ça bloque ?", "un nom, un poste, un courriel"),
    ], corrige=True,
       notes="C'est l'exercice le plus formateur de la séance : on découvre ce qui manque "
             "en lisant la procédure de quelqu'un d'autre.")

    d.piege("Le piège de l'étape évidente",
            "Prenez une photo du reçu.",
            "Prenez une photo claire du reçu, directement avec l'application.",
            "Ce qui est évident pour celui qui écrit ne l'est pas pour celui qui lit. "
            "« Claire » et « directement avec l'application » paraissent superflus — ce "
            "sont pourtant les deux précisions qui font la différence entre une demande "
            "acceptée et une demande refusée.",
            notes="Faire relever, dans les procédures échangées, toutes les précisions "
                  "manquantes. Il y en aura beaucoup.")

    d.pratique('Pratique · 4 de 4', "Corrigez votre procédure",
               "D'après les remarques de votre voisin.", [
        ("Ce qui manquait", "notez-le avant de corriger"),
        ("Ce que vous ajoutez", "les précisions, le délai, le recours"),
        ("Ce que vous coupez", "les lignes qui contiennent deux actions"),
        ("La relecture finale", "chaque ligne commence par un verbe à l'impératif"),
    ], corrige=False,
       notes="Dix minutes. Ramasser les versions corrigées : ce sont elles qu'on évalue, "
             "pas les premières.")

    d.billet(
        "En une phrase : qu'est-ce qui manquait le plus souvent dans les procédures de la classe ?",
        exemples=[
            "Une seule chose, précise.",
            "Exemple : « le délai n'était presque jamais écrit ».",
        ],
        notes="Relever les réponses et en faire une liste au tableau. C'est le meilleur "
              "bilan possible de la compétence du module.")

    return d.save(dossier)
