# -*- coding: utf-8 -*-
"""A3 · Trois dommages et une clause
Bloc A « Je découvre » · couleur acier · 75 min. Compréhension orale.
Source du module : le dialogue `prep` et l'exercice `pr1`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='acier',
        titre="Trois dommages et une clause",
        chapeau="Amira appelle l'entreprise de déménagement le soir même. "
                "Elle a trois points ; le patron a un contrat et une réponse "
                "toute prête.",
        duree='75 minutes')

    d.titre(notes="Séance d'écoute. Faire écouter l'extrait une première fois "
                  "sans consigne, diapositive masquée : au niveau 8, la "
                  "première écoute sert à situer la scène, pas à prélever.")

    d.objectifs([
        "suivre un appel de vingt-trois répliques et en tirer trois griefs ;",
        "repérer sur quoi chacun des deux s'appuie ;",
        "reconnaître le moment où Amira concède un point ;",
        "expliquer pourquoi elle concède, et ce que ça lui rapporte.",
    ], notes="Le quatrième objectif est celui du module entier. Ne pas le "
             "donner en premier : le faire découvrir par l'écoute.")

    d.declencheur(
        'Avant d\'écouter', "À qui téléphone-t-on d'abord quand un déménageur "
                            "a abîmé quelque chose ?",
        pistes=[
            "Au déménageur, à l'assurance, ou au propriétaire du logement ?",
            "Est-ce qu'on peut appeler les trois ?",
            "Qu'est-ce qu'on dit en premier, dans les dix premières secondes ?",
        ],
        notes="La deuxième question a une bonne réponse — oui, et les "
              "démarches ne se nuisent pas — mais ne pas la donner ici : "
              "elle est le sujet du défi 1.")

    d.dialogue('Écoute', "Le camion est reparti à onze heures", [
        ("AMIRA", "Il y en a trois. Je préfère vous les dire au téléphone avant de vous écrire quoi que ce soit.", False),
        ("AMIRA", "Le coin de la remorque l'a accrochée en reculant, vers neuf heures et quart.", True),
        ("DENIS", "Elle était déjà croche, cette rampe-là. C'est un triplex des années trente.", False),
        ("AMIRA", "Elle était droite hier. J'ai des photos datées de la veille.", True),
        ("AMIRA", "Ça, je vous l'accorde : personne ne surveillait le balcon, et j'aurais dû y penser.", True),
        ("DENIS", "Notre responsabilité est limitée à soixante cents par livre par article.", False),
    ], consigne="Six répliques sur vingt-trois. Les trois en couleur sont "
                "celles qui décident de la suite.",
       notes="Faire écouter l'extrait entier avant d'afficher. Les répliques "
             "en évidence sont celles où Amira pose une preuve ou concède un "
             "point — c'est là que se joue tout le reste du module.")

    d.tableau('Analyse', "Ce que chacun met sur la table",
              ['Amira apporte', 'Denis oppose'],
              [["des photos datées de la veille", "« la rampe était déjà croche »"],
               ["l'inventaire signé à huit heures", "« un meuble ancien, ça travaille »"],
               ["une concession sur les boîtes", "« ça, c'est votre affaire »"],
               ["l'annonce d'une lettre écrite", "la limite au poids : soixante cents la livre"]],
              cle=0,
              note="Chaque fois : un fait daté d'un côté, une opinion de l'autre.",
              notes="Diapositive à photographier. Faire remarquer que Denis "
                    "n'est pas de mauvaise foi : il applique un contrat, et "
                    "il a raison sur ce contrat-là. C'est ce qui rend "
                    "l'exercice réel.")

    d.regle("Concéder n'est pas perdre",
            "Amira reconnaît tout de suite que personne ne surveillait le balcon — et c'est ce qui la rend crédible sur les deux autres points.",
            precision="Celui qui conteste tout en bloc se fait lire la clause "
                      "et raccrocher. Celui qui lâche le point faible obtient "
                      "qu'on écoute les points forts.",
            notes="Diapositive à photographier. C'est la règle centrale du "
                  "module, et elle reviendra en C1, en E1 et dans la lettre "
                  "de E2. La poser ici, une fois, clairement.")

    d.pratique('Pratique', "Vrai ou faux",
               "Écoutez de nouveau, puis répondez.", [
        ("Amira téléphone avant d'envoyer quoi que ce soit par écrit.", "VRAI"),
        ("Denis reconnaît que la rampe était droite avant l'arrivée du camion.", "FAUX"),
        ("Amira reconnaît elle-même que personne ne surveillait les boîtes.", "VRAI"),
        ("Le chauffeur a signé l'inventaire sans y noter de dommage.", "VRAI"),
        ("Amira avait lu le connaissement avant de le signer.", "FAUX"),
        ("Le déménageur lui conseille de réclamer à son assurance.", "VRAI"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `pr1` du module, dans sa version projetée. "
             "Pour chaque « faux », demander la phrase exacte de l'extrait "
             "qui le prouve — c'est ce qui entraîne au niveau 8.")

    d.billet(
        "Dans un désaccord que tu as déjà eu, quel point aurais-tu pu concéder tout de suite ?",
        exemples=[
            "Deux phrases : le désaccord, puis le point.",
            "Termine par « je vous l'accorde, mais… ».",
        ],
        notes="Cinq minutes. Ne pas ramasser : lire deux ou trois réponses à "
              "voix haute avec l'accord des personnes. L'exercice touche "
              "souvent des situations réelles et récentes.")

    return d.save(dossier)
