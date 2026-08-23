# -*- coding: utf-8 -*-
"""E1 · Négocier, puis décider à voix haute
Bloc E « Je me lance » · couleur teal · production orale · 75 min.
Source : bloc `appli` de `custom.js` — jeu de rôle « louerouacheter » (trois
cas, deux rôles) et production orale en trois temps.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="Négocier, puis décider à voix haute",
        chapeau="Deux prises de parole : une négociation avec l'assistant, "
                "puis un exposé de quatre-vingt-dix secondes qui pèse les "
                "deux options et qui tranche.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Redistribuer les billets de B4 — la phrase "
                  "de négociation complète — et ceux de D2 — la phrase en « d'autant "
                  "plus… que ». Chacun entre en scène avec ses propres mots.")

    d.objectifs([
        "tenir une négociation en vouvoyant, sans céder ni se fâcher ;",
        "offrir une contrepartie et demander un écrit ;",
        "exposer deux avantages et deux inconvénients par option, chiffrés ;",
        "trancher, et dire à quelle condition on changerait d'avis.",
    ], notes="C'est l'attente de fin de cours du niveau 7, mot pour mot : exposer les "
             "avantages et les inconvénients de deux situations pour prendre une "
             "décision durant une négociation.")

    d.cartes('Jeu de rôle', "Trois moments, deux rôles", [
        ("L'avis, à discuter", "Le loyer passerait de 940 $ à 1 024 $, et le stationnement coûterait 25 $ de plus. Un mois pour répondre par écrit."),
        ("La fenêtre de la chambre", "Elle ne ferme plus depuis février, signalée au téléphone seulement. Les travaux d'entretien sont à la charge du propriétaire."),
        ("Le projet qui change tout", "Vous vous informez pour acheter. Rien n'est décidé, et vous ne voulez ni promettre de rester ni annoncer un départ."),
        ("Vous jouez qui ?", "La locataire qui a lu son avis, ou le propriétaire aux six logements. Faire les deux : on négocie mieux quand on a été de l'autre côté."),
    ], notes="Vingt minutes de jeu de rôle, en autonomie, dans le module. Passer dans "
             "les rangées et noter deux phrases réussies par élève : elles serviront de "
             "modèles au moment de l'exposé.")

    d.tableau('Analyse', "Les huit sujets à couvrir",
              ['Ce quon dit', 'Comment'],
              [["de quoi il s'agit", "avant tout détail, en une phrase"],
               ["le délai d'un mois", "rappelé, jamais brandi comme une menace"],
               ["la demande", "au conditionnel : pourriez-vous, accepteriez-vous"],
               ["ce qui compte", "mis en avant : ce qui me dérange, c'est…"],
               ["la contrepartie et l'écrit", "un montant précis, puis deux lignes datées"]],
              cle=0,
              notes="Diapositive à photographier, et à laisser affichée pendant tout le "
                    "jeu de rôle : c'est la grille que l'élève coche lui-même.")

    d.regle("Une décision se termine par une date",
            "« Je ne sais pas encore » n'est pas une conclusion ; « cette année, je reste » en est une.",
            precision="Comparer sans trancher ne répond pas à la question posée. Et "
                      "trancher ne veut pas dire s'enfermer : une décision datée — "
                      "« cette année je reste, et je reviendrai voir quand j'aurai "
                      "trente mille dollars de côté » — est à la fois ferme et ouverte. "
                      "C'est la forme qu'on attend de vous.",
            notes="Diapositive à photographier. C'est le critère principal de la "
                  "correction de la production orale ; le dire avant, pas après.")

    d.cartes('Production orale', "Les trois temps de votre exposé", [
        ("Temps 1 · Les deux options", "« J'ai deux possibilités : rester locataire à 995 $ par mois si mon entente tient, ou acheter un condo de 275 000 $. »"),
        ("Temps 2 · Deux avantages, deux inconvénients", "Pour chacune, avec un chiffre à l'appui : la mise de fonds de 13 750 $, les 600 $ de plus par mois, l'avis de hausse chaque année."),
        ("Temps 3 · La comparaison, puis la décision", "« C'est d'autant plus difficile que les deux se défendent. Cette année, je reste ; je reviendrai voir si j'atteins 30 000 $. »"),
        ("Ce qui se corrige", "Le plan en trois temps, les chiffres, une comparaison correcte, une décision datée. Pas l'accent, pas l'hésitation."),
    ], notes="Quatre-vingt-dix secondes, enregistrées dans le module. Rappeler qu'on "
             "peut recommencer autant de fois qu'on veut avant d'envoyer, et que la "
             "correction de l'assistant n'est jamais transmise telle quelle.")

    d.pratique('Production orale', "Les deux colonnes, à préparer avant de parler",
               "Écrivez-les au brouillon : deux minutes, pas plus.", [
        ("Rester locataire · avantage", "aucun autre frais ; je peux partir avec un avis"),
        ("Rester locataire · inconvénient", "une hausse possible chaque année ; rien ne m'appartient"),
        ("Acheter · avantage", "une partie du paiement me revient ; le montant est prévisible"),
        ("Acheter · inconvénient", "13 750 $ de mise de fonds ; 600 $ de plus par mois"),
        ("La phrase de comparaison", "« C'est d'autant plus difficile que… »"),
    ], corrige=True,
       notes="Ne pas laisser parler quelqu'un qui n'a pas les deux colonnes écrites. "
             "L'exposé improvisé tombe toujours dans une seule colonne, et le groupe "
             "l'entend.")

    d.billet(
        "Écris ta décision en une phrase, avec sa date.",
        exemples=[
            "« Cette année, je reste locataire, et je reviendrai voir en mars. »",
            "Une seule phrase.",
        ],
        notes="Deux minutes. Ces phrases ouvriront la production écrite de E2 : la "
                  "lettre au propriétaire découle de la décision, pas l'inverse.")

    return d.save(dossier)
