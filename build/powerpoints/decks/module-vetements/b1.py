# -*- coding: utf-8 -*-
"""B1 · Dans la cabine d'essayage.
Bloc B « Défi 1 · Trouver sa taille » · couleur acier · 75 min.
Source : dialogue `t1`, exercices `t1vf` et `t1verifier`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Dans la cabine d'essayage",
        chapeau="Serré aux épaules, manches trop longues, longueur aux "
                "genoux. Dire ce qui ne va pas demande quelques mots précis — "
                "et un manteau d'hiver se choisit plus grand qu'on ne croit.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc B. Demander au groupe ce qu'il vérifie en essayant un "
                  "vêtement. Les réponses sont souvent vagues : c'est le point de départ.")

    d.objectifs([
        "dire ce qui ne va pas avec un adjectif et un endroit ;",
        "vérifier les épaules, les manches et la longueur ;",
        "comprendre pourquoi un manteau doit être ample ;",
        "demander une autre taille.",
    ])

    d.declencheur(
        'Mise en situation', "Vous essayez un manteau. Que vérifiez-vous, et comment ?",
        pistes=[
            "Qu'est-ce que vous regardez en premier ?",
            "Comment savoir si les manches sont à la bonne longueur ?",
            "Levez-vous les bras dans la cabine ?",
            "Est-ce qu'un manteau doit être ajusté ou ample ?",
        ],
        notes="La troisième piste est la plus utile : lever les bras est le test le plus "
              "simple, et presque personne ne le fait.")

    d.dialogue('Dialogue · 1 de 3', "Trop petit", [
        ("VALÉRIE", "Alors, le moyen ?", False),
        ("KOFI", "Il est un peu serré aux épaules. Je ne peux pas lever les bras.", True),
        ("VALÉRIE", "Alors c'est trop petit. Un manteau d'hiver doit laisser de la place pour un chandail.", True),
        ("KOFI", "Ah, je n'avais pas pensé à ça.", False),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="« Serré aux épaules » : un adjectif et un endroit. C'est la formule complète, "
             "et elle donne à la conseillère tout ce qu'il lui faut.")

    d.dialogue('Dialogue · 2 de 3', "La bonne taille", [
        ("VALÉRIE", "Essayez le grand. Il va vous sembler trop large, mais c'est normal.", True),
        ("KOFI", "Celui-là est mieux. Les manches sont un peu longues, par exemple.", True),
        ("VALÉRIE", "Elles doivent couvrir le poignet quand vous levez le bras. Montrez-moi… Non, c'est parfait.", True),
        ("KOFI", "Et la longueur ?", False),
    ], notes="Le test des manches est concret : lever le bras et regarder le poignet. Le "
             "faire faire au groupe.")

    d.dialogue('Dialogue · 3 de 3', "Longueur et poids", [
        ("VALÉRIE", "Aux genoux, c'est bien pour attendre l'autobus. Plus court, vous aurez froid aux jambes.", True),
        ("KOFI", "Il est lourd, non ?", True),
        ("VALÉRIE", "C'est du duvet, il est plus léger qu'il n'en a l'air. Essayez de bouger un peu.", True),
        ("KOFI", "D'accord. Il est chaud, ça c'est sûr.", False),
    ], notes="« Essayez de bouger un peu » : un bon conseil. Un manteau s'essaie en "
             "mouvement, pas debout devant un miroir.")

    d.tableau('Analyse', "Ce qu'on vérifie, et comment",
              ['La partie', 'Le test'],
              [["Les épaules", "lever les bras — sans être serré"],
               ["Les manches", "elles couvrent le poignet, bras levé"],
               ["La longueur", "elle descend aux genoux"],
               ["La place dessous", "il reste de l'espace pour un chandail"]],
              cle=0,
              note="Quatre tests, trente secondes. C'est tout ce qu'il faut faire en cabine.",
              notes="Diapo à photographier. Faire faire les quatre tests au groupe, avec ce "
                    "qu'ils portent.")

    d.regle("Un adjectif et un endroit",
            "« Il est un peu serré aux épaules. »",
            precision="Dire « ça ne va pas » oblige la personne à deviner. Dire l'adjectif "
                      "et l'endroit lui permet de proposer une autre <b>coupe</b>, pas "
                      "seulement une autre taille. C'est la différence entre trois essais "
                      "et dix.",
            notes="Diapo à photographier. Faire produire cinq phrases sur ce modèle par "
                  "cinq élèves.")

    d.piege("Choisir un manteau ajusté",
            "Il me va parfaitement, il est bien ajusté.",
            "Trop ajusté : il n'y a plus de place pour un chandail.",
            "C'est l'air emprisonné entre les couches qui tient chaud. Un manteau collé au "
            "corps est un manteau froid — et par-dessus un chandail, il devient serré aux "
            "épaules et aux bras.",
            notes="Contre-intuitif et important. Le dire deux fois.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Le manteau moyen est serré aux épaules.", "vrai"),
        ("Un manteau d'hiver doit être ajusté.", "faux — il doit laisser de la place"),
        ("Le grand lui semble d'abord trop large.", "vrai"),
        ("Les manches doivent couvrir le poignet bras levé.", "vrai"),
        ("La bonne longueur est aux chevilles.", "faux — aux genoux"),
        ("Le duvet est plus lourd qu'il n'en a l'air.", "faux — plus léger"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte.")

    d.billet(
        "Décrivez ce qui ne va pas sur un vêtement que vous possédez.",
        exemples=[
            "Un adjectif et un endroit : « serré aux épaules », « trop court ».",
            "Trois vêtements, trois phrases.",
        ],
        notes="Ramasser. Ces phrases servent au jeu de rôle de E1.")

    return d.save(dossier)
