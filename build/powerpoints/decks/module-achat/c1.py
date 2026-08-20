# -*- coding: utf-8 -*-
"""C1 · Ce que couvre la garantie.
Bloc C « Défi 2 · La garantie et la livraison » · couleur acier · 75 min.
Source : mini-leçon `t2garantie`, dialogue `t2`, exercices `t2vf` et `t2garantie`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre='Ce que couvre la garantie',
        chapeau="Une garantie n'est pas une assurance tous risques. Elle "
                "couvre ce qui vient de l'usine — jamais ce qu'on fait à "
                "l'appareil. Toute la différence est là.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc C. Question d'entrée : « qui a déjà fait réparer un "
                  "appareil sous garantie ? ». Les récits sortent tout seuls, et ils sont "
                  "instructifs.")

    d.objectifs([
        "distinguer un défaut de fabrication d'un accident ;",
        "comprendre « pièces et main-d'œuvre » ;",
        "savoir si le déplacement du technicien est couvert ;",
        "décider si une garantie prolongée vaut la peine.",
    ])

    d.dialogue('Dialogue · 1 de 2', "Ce qui est couvert", [
        ("YIN", "Qu'est-ce que la garantie couvre, au juste ?", True),
        ("MARTIN", "Un an, pièces et main-d'œuvre. Si l'appareil brise, on répare sans frais.", True),
        ("YIN", "Et si c'est moi qui l'abîme ?", True),
        ("MARTIN", "Ça, ce n'est pas couvert. La garantie couvre les défauts de fabrication, pas les accidents.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Les quatre répliques sont teintées : chacune contient une information "
             "essentielle. La dernière est la définition à retenir.")

    d.dialogue('Dialogue · 2 de 2', "La garantie prolongée", [
        ("YIN", "Vous parliez d'une garantie prolongée.", False),
        ("MARTIN", "Cent vingt dollars pour trois ans de plus. Elle couvre aussi le déplacement du technicien.", True),
        ("YIN", "Je vais y penser. Pour le paiement, vous prenez quoi ?", True),
        ("MARTIN", "Comptant, débit, crédit. Ou en douze versements sans intérêt, si vous préférez.", False),
    ], notes="« Je vais y penser » est une réponse parfaitement acceptable devant une "
             "offre supplémentaire. Le dire : personne n'est obligé de décider sur place.")

    d.tableau('Analyse', "Couvert, ou pas couvert",
              ['La situation', 'Le verdict'],
              [["Le moteur brise après huit mois", "couvert — défaut de fabrication"],
               ["L'appareil tombe au déménagement", "pas couvert — accident"],
               ["Trois fois trop de savon", "pas couvert — mauvaise utilisation"],
               ["Panne après quatorze mois", "pas couvert — hors période"]],
              cle=0,
              note="Trois sur quatre ne sont pas couvertes. C'est le rapport habituel.",
              notes="Diapo centrale. Faire trouver le verdict par le groupe avant "
                    "d'afficher la colonne de droite.")

    d.regle("Pièces et main-d'œuvre",
            "Ni la pièce ni le travail du technicien ne vous sont facturés.",
            precision="C'est la formule standard. Elle ne comprend pas toujours le "
                      "<b>déplacement</b> — souvent quatre-vingt-dix dollars. Certaines "
                      "garanties prolongées le couvrent ; la garantie de base rarement. "
                      "À demander avant d'acheter.",
            notes="Diapo à photographier. Le déplacement est le poste le plus souvent "
                  "oublié, et le plus contesté au comptoir de service.")

    d.regle("La garantie prolongée : quand ça vaut la peine",
            "Pour les appareils chers à réparer, pas pour les petits.",
            precision="Un réfrigérateur ou une laveuse coûtent cher à réparer : la "
                      "prolongée peut se justifier. Un petit appareil se remplace au lieu "
                      "de se réparer : elle ne vaut presque jamais la peine. Repère : "
                      "au-delà du tiers du prix de l'appareil, c'est rarement avantageux.",
            notes="Point utile et rarement dit. Les élèves subissent souvent une pression "
                  "de vente sur ce produit.")

    d.piege("Croire que la garantie couvre tout",
            "L'appareil est tombé, mais il est sous garantie.",
            "La garantie couvre les défauts de fabrication, pas les accidents.",
            "Une garantie n'est pas une assurance. Elle promet que l'appareil est conforme "
            "à sa sortie d'usine et qu'il le restera un certain temps. Ce qui lui arrive "
            "chez vous ne la concerne pas.",
            notes="C'est la source de presque tous les malentendus au service à la "
                  "clientèle. Le formuler clairement une fois suffit.")

    d.pratique('Pratique', "Couvert ou pas ?",
               "Dites si la garantie de base s'applique.", [
        ("Le moteur brise après huit mois.", "couvert"),
        ("L'appareil tombe pendant le déménagement.", "pas couvert"),
        ("Une pièce casse toute seule la première semaine.", "couvert"),
        ("L'appareil ne fonctionne plus après quatorze mois.", "pas couvert — hors période"),
        ("On a mis trois fois trop de savon.", "pas couvert — mauvaise utilisation"),
        ("Le déplacement du technicien, sans garantie prolongée.", "pas couvert"),
    ], corrige=True,
       notes="Faire justifier chaque réponse : défaut, accident, mauvaise utilisation, ou "
             "hors période ?")

    d.cartes("Garder ses preuves", "Trois réflexes", [
        ("Photographier la facture",
         "Le jour de l'achat. La date déclenche la période de garantie, et le papier "
         "s'efface avec le temps."),
        ("Garder le bon de livraison",
         "Il prouve ce qui a été promis : installation, reprise, date."),
        ("Noter le numéro de modèle",
         "Il est sur une plaque, souvent à l'arrière ou dans la porte. Le service le "
         "demandera au premier appel."),
    ], notes="Ces trois réflexes prennent cinq minutes le jour de l'achat et évitent des "
             "heures de discussion plus tard.")

    d.billet(
        "Décrivez trois situations et dites si elles seraient couvertes.",
        exemples=[
            "Une couverte, une non couverte, une dont vous n'êtes pas sûr.",
            "Pour la troisième, écrivez la question que vous poseriez au magasin.",
        ],
        notes="La troisième situation est la plus intéressante à corriger : elle révèle ce "
              "que le groupe n'a pas encore assimilé.")

    return d.save(dossier)
