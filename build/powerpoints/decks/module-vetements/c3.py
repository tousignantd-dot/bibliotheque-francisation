# -*- coding: utf-8 -*-
"""C3 · L'étiquette d'entretien.
Bloc C « Défi 2 » · couleur ambre · 60 min.
Source : mini-leçon `t2entretien`, exercices `t2entretien` et `t2symboles`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-vetements/images/')


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="L'étiquette d'entretien",
        chapeau="Cinq dessins cousus dans le col, les mêmes partout dans le "
                "monde. Ils disent comment laver, sécher et repasser — et "
                "comment ne pas ruiner un vêtement en une seule brassée.",
        duree='60 minutes')

    d.titre(notes="Apporter deux ou trois vêtements avec des étiquettes différentes. Les "
                  "faire circuler pendant le déclencheur.")

    d.objectifs([
        "reconnaître les cinq symboles d'entretien ;",
        "lire une température de lavage ;",
        "comprendre ce qu'un X veut dire ;",
        "employer le vocabulaire du lavage.",
    ])

    d.declencheur(
        'Observation', "Que veulent dire ces dessins ?",
        image=IMG + 'etiquette-col.jpg',
        pistes=[
            "Combien de dessins voyez-vous ?",
            "Lequel ressemble à une machine à laver ?",
            "Que veut dire une croix par-dessus ?",
            "Avez-vous déjà rétréci un vêtement ?",
        ],
        notes="La dernière question fait parler tout le monde. Le lainage rétréci est une "
              "expérience universelle.")

    d.tableau('Analyse', "Les cinq symboles",
              ['Le dessin', "Ce qu'il dit"],
              [["Un bac d'eau", "le lavage — souvent avec une température"],
               ["Un triangle", "l'eau de Javel"],
               ["Un carré", "le séchage"],
               ["Un fer", "le repassage"],
               ["Un cercle", "le nettoyage à sec"]],
              cle=0,
              note="Toujours dans cet ordre, de gauche à droite.",
              notes="Diapo à photographier. L'ordre est une norme internationale : une fois "
                    "su, il rend l'étiquette lisible partout.")

    d.regle("La croix veut dire non",
            "Un X sur un symbole : c'est interdit.",
            precision="Un carré barré : ne pas mettre à la sécheuse. Un triangle barré : "
                      "pas d'eau de Javel. Un fer barré : ne pas repasser. C'est la "
                      "convention la plus utile de toute l'étiquette, et elle s'apprend en "
                      "dix secondes.",
            notes="Diapo à photographier. Faire chercher un symbole barré sur les vêtements "
                  "apportés.")

    d.cartes("Les points et les chiffres", "Deux façons de dire la chaleur", [
        ("Les chiffres dans le bac",
         "30, 40, 60 : la température de l'eau en degrés. 30, c'est l'eau froide ; 60, "
         "c'est très chaud et réservé au coton blanc."),
        ("Les points",
         "Un point = doux ou froid. Deux points = moyen. Trois points = chaud. On les "
         "trouve dans le fer et dans le carré du séchage."),
        ("La main dans le bac",
         "Lavage à la main seulement. La machine, même au cycle délicat, abîmera le "
         "vêtement."),
    ], notes="Les points servent surtout au fer et à la sécheuse. Les élèves les confondent "
             "souvent avec des degrés.")

    d.tableau('Analyse', "Les mots du lavage",
              ['Le mot', 'Ce que ça veut dire'],
              [["laver à froid", "à trente degrés ou moins"],
               ["sécher à plat", "étendu, jamais suspendu"],
               ["ne pas mettre à la sécheuse", "il rétrécirait"],
               ["nettoyage à sec", "au nettoyeur, pas à la maison"]],
              cle=1,
              note="« Sécher à plat » évite qu'un lainage s'étire et s'allonge.",
              notes="Ces quatre expressions sont dans le banc de vocabulaire.")

    d.piege("La laine à la sécheuse",
            "Je l'ai mis à la sécheuse avec le reste.",
            "Lavage à froid, séchage à plat.",
            "La chaleur et le mouvement font feutrer la laine : les fibres s'accrochent "
            "entre elles et le vêtement rétrécit de plusieurs tailles, définitivement. "
            "Aucun traitement ne le répare.",
            notes="Erreur classique et coûteuse. Le manteau de duvet, lui, va à la "
                  "sécheuse — avec des balles de tennis, à basse température.")

    d.pratique('Pratique · 1 de 2', "Que dit l'étiquette ?",
               "Traduisez le symbole en phrase.", [
        ("Un bac avec 30", "laver à trente degrés — à froid"),
        ("Un carré barré", "ne pas mettre à la sécheuse"),
        ("Un triangle barré", "pas d'eau de Javel"),
        ("Un fer à un point", "repasser à basse température"),
        ("Un cercle", "nettoyage à sec"),
        ("Une main dans le bac", "laver à la main"),
    ], corrige=True,
       notes="Utiliser l'exercice de symboles du module, qui montre les dessins.")

    d.pratique('Pratique · 2 de 2', "Que faire de ce vêtement ?",
               "Choisissez.", [
        ("Un chandail de laine", "laver à froid, sécher à plat"),
        ("Un manteau de duvet", "machine à froid, sécheuse basse, balles de tennis"),
        ("Une chemise de coton blanc", "machine à chaud, repassage possible"),
        ("Un manteau de laine habillé", "nettoyage à sec"),
    ], corrige=True, cols=1,
       notes="Faire justifier. Le duvet surprend : il va bien à la sécheuse.")

    d.billet(
        "Lisez l'étiquette d'un vêtement que vous portez souvent.",
        exemples=[
            "Notez les cinq symboles et ce qu'ils disent.",
            "Est-ce que vous le laviez comme il faut ?",
        ],
        notes="Devoir concret. Plusieurs découvriront qu'ils lavent trop chaud.")

    return d.save(dossier)
