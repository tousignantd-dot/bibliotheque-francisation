# -*- coding: utf-8 -*-
"""A3 · Mesurer avant d'acheter.
Bloc A « Je découvre » · couleur teal · 60 min.
Source : exercices `prMesure` et `prChiffres`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-achat/images/')


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre="Mesurer avant d'acheter",
        chapeau="Un appareil qui n'entre pas repart avec le camion — et la "
                "livraison reste à payer. Cinq mesures suffisent à ne jamais "
                "vivre ça.",
        duree='60 minutes')

    d.titre(notes="Apporter un ruban à mesurer. La séance vaut surtout si les élèves "
                  "mesurent quelque chose pour de vrai pendant le cours.")

    d.objectifs([
        "prendre les trois dimensions d'un espace ;",
        "penser au dégagement et au passage, pas seulement au local ;",
        "lire les chiffres d'une fiche technique : décibels, kilowattheures, litres ;",
        "demander ce qu'un chiffre veut dire.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qu'on mesure ici, et pourquoi ?",
        image=IMG + 'ruban-mesurer.jpg',
        pistes=[
            "Quelles dimensions faut-il prendre ?",
            "Qu'est-ce qu'on oublie presque toujours ?",
            "Le local suffit-il, ou faut-il mesurer autre chose ?",
            "Que se passe-t-il si l'appareil n'entre pas ?",
        ],
        notes="La deuxième piste amène le dégagement de la porte, la troisième le passage. "
              "Les deux sont les causes habituelles d'un achat raté.")

    d.tableau('Analyse', "Les cinq mesures à prendre",
              ['Ce qu\'on mesure', 'Pourquoi'],
              [["La hauteur du local", "l'appareil doit y tenir debout"],
               ["La largeur du local", "la mesure la plus évidente"],
               ["La profondeur", "souvent oubliée, avec les tuyaux derrière"],
               ["Le dégagement devant", "pour ouvrir la porte de l'appareil"],
               ["Le passage jusqu'au local", "portes, corridor, escalier"]],
              cle=4,
              note="La dernière est celle qui fait repartir le camion.",
              notes="Diapo à photographier. Faire mesurer la porte de la classe : presque "
                    "personne n'en connaît la largeur.")

    d.regle("Toujours la porte ouverte",
            "La largeur d'une laveuse frontale se mesure porte ouverte.",
            precision="Soixante-huit centimètres fermée, quatre-vingt-dix ouverte : sans "
                      "le dégagement, la porte bute contre le mur et l'appareil est "
                      "inutilisable. La fiche technique donne les deux chiffres.",
            notes="C'est exactement le premier modèle éliminé dans le dialogue de A1.")

    d.cartes('Lire les chiffres', "Quatre unités et leur repère", [
        ("Le centimètre",
         "Hauteur × largeur × profondeur, toujours dans cet ordre : 145 × 55 × 60 cm."),
        ("Le décibel",
         "Le bruit. Une conversation normale fait 60 dB ; 52 dB est nettement plus "
         "silencieux."),
        ("Le kilowattheure par année",
         "L'électricité. Plus le chiffre est bas, moins l'appareil coûte à faire "
         "fonctionner."),
        ("Le litre par brassée",
         "L'eau. Trente litres d'écart par brassée, sur cinq ans, compensent souvent une "
         "différence de prix."),
    ], notes="La dernière carte est le raisonnement du dialogue t1. Le faire calculer : "
             "30 L × 3 brassées × 52 semaines × 5 ans.")

    d.piege('Mesurer seulement le local',
            "Le local fait un mètre, l'appareil soixante-huit centimètres. C'est bon.",
            "Et la porte du sous-sol ? Et l'escalier ?",
            "L'appareil doit d'abord se rendre jusqu'au local. Une porte de soixante-dix "
            "centimètres, un escalier étroit, un tournant serré : chacun peut arrêter la "
            "livraison. Le livreur repartira avec l'appareil, et la livraison restera à "
            "payer.",
            notes="C'est exactement l'avertissement du livreur dans le dialogue t2b. "
                  "L'annoncer.")

    d.pratique('Pratique · 1 de 2', "Le chiffre et ce qu'il mesure",
               "Dites ce que chaque chiffre indique.", [
        ("68 centimètres", "la largeur de l'appareil"),
        ("4,5 kilos", "la capacité : le linge qui entre dedans"),
        ("52 décibels", "le bruit à l'essorage"),
        ("30 litres par brassée", "la consommation d'eau"),
        ("300 kilowattheures par année", "la consommation d'électricité"),
        ("12 mois", "la durée de la garantie"),
    ], corrige=True,
       notes="Faire répondre à voix haute avant d'afficher. Ces six chiffres couvrent "
             "toutes les fiches techniques.")

    d.pratique('Pratique · 2 de 2', "Ça entre, ou pas ?",
               "Le local fait 100 cm de large et la porte 70 cm.", [
        ("Appareil de 68 cm, porte fermée", "il entre dans le local"),
        ("Le même, 90 cm porte ouverte", "il faut 90 cm de dégagement devant"),
        ("Appareil de 76 cm", "il n'entre pas par la porte de 70 cm"),
        ("Appareil de 60 cm, profondeur 65 cm", "vérifier aussi la profondeur du local"),
    ], corrige=True, cols=1,
       notes="Faire dessiner le local au tableau. Le raisonnement devient évident dès "
             "qu'il est vu.")

    d.billet(
        "Mesurez un espace chez vous et écrivez les cinq mesures.",
        exemples=[
            "Hauteur, largeur, profondeur, dégagement, passage.",
            "Notez laquelle vous auriez oubliée sans cette séance.",
        ],
        notes="Ce billet servira au jeu de rôle de E1 : l'assistant demande l'espace "
              "disponible dès la première réplique.")

    return d.save(dossier)
