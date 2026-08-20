# -*- coding: utf-8 -*-
"""C4 · Avant d'acheter.
Bloc C « Défi 2 » · couleur acier · 50 min. Bilan du défi 2.
Source : dialogue `t2b`, exercice `t2symboles`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='acier',
        titre="Avant d'acheter",
        chapeau="L'étiquette du prix dit combien. L'étiquette du col dit "
                "combien ça coûtera vraiment : un manteau à nettoyer à sec "
                "quatre fois par hiver n'est pas une aubaine.",
        duree='50 minutes')

    d.titre(notes="Bilan du défi 2. La séance relie l'avis et l'étiquette : les deux "
                  "servent à décider.")

    d.objectifs([
        "lire l'étiquette avant de payer ;",
        "estimer le coût d'entretien d'un vêtement ;",
        "demander une information à une conseillère ;",
        "réviser le vocabulaire du défi 2.",
    ])

    d.declencheur(
        'Mise en situation', "Deux manteaux au même prix. Lequel coûte le plus cher ?",
        pistes=[
            "L'un se lave à la machine, l'autre va au nettoyeur.",
            "Combien coûte un nettoyage à sec ?",
            "Combien de fois par hiver ?",
            "Alors, lequel est le moins cher ?",
        ],
        notes="Un nettoyage à sec coûte entre vingt et trente dollars. Quatre par hiver, "
              "et le manteau « au même prix » coûte cent dollars de plus par année.")

    d.dialogue('Dialogue · 1 de 2', "La question à poser", [
        ("KOFI", "Excusez-moi, est-ce que celui-ci se lave à la machine ?", True),
        ("VALÉRIE", "Attendez, je regarde l'étiquette… Oui, à froid, et séchage à basse température.", True),
        ("KOFI", "Et l'autre, le gris ?", False),
        ("VALÉRIE", "Celui-là, c'est nettoyage à sec seulement.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="« Est-ce que ça se lave à la machine ? » : une question à mémoriser. Elle "
             "s'emploie partout.")

    d.dialogue('Dialogue · 2 de 2', "La décision", [
        ("KOFI", "Ça coûte combien, un nettoyage à sec ?", True),
        ("VALÉRIE", "Une vingtaine de dollars, pour un manteau. Trois ou quatre fois par hiver.", True),
        ("KOFI", "Alors je prends le noir. Il se lave chez moi.", True),
        ("VALÉRIE", "C'est un bon calcul.", False),
    ], notes="Kofi décide pour une raison, et il la dit. C'est exactement ce qu'on demande "
             "aux élèves de savoir faire.")

    d.tableau('Analyse', "Ce qui coûte, après le prix",
              ["Ce qu'on lit", 'Ce que ça coûte'],
              [["lavage à la machine", "presque rien"],
               ["lavage à la main", "du temps"],
               ["séchage à plat", "de la place et du temps"],
               ["nettoyage à sec", "20 à 30 $ chaque fois"]],
              cle=3,
              note="C'est la seule ligne qui coûte de l'argent tous les mois.",
              notes="Diapo à photographier. Ce raisonnement s'applique aussi aux "
                    "chaussures et aux rideaux.")

    d.regle("Deux questions avant de payer",
            "Comment ça se lave ? Est-ce que ça peut s'échanger ?",
            precision="La première évite un vêtement ruiné ou coûteux ; la seconde évite un "
                      "achat définitif dont on ne veut plus. Les deux se posent en dix "
                      "secondes, à la caisse, et personne ne les trouve étranges.",
            notes="Diapo à photographier. C'est le résumé du bloc C et l'annonce du bloc D.")

    d.cartes("Les mots du défi 2", "À revoir", [
        ("Donner un avis",
         "je trouve que, il me semble, à mon avis, je suis moins sûr de, il te va bien."),
        ("Nuancer",
         "un peu, plutôt, vraiment, c'est vrai, mais…"),
        ("L'entretien",
         "laver à froid, à la main, sécher à plat, la sécheuse, le nettoyage à sec, "
         "repasser, rétrécir."),
        ("L'étiquette",
         "le col, le symbole, le bac, le triangle, le carré, le fer, barré."),
    ], notes="Diapo à photographier. Liste de révision du défi 2.")

    d.piege("Payer sans avoir lu le col",
            "Je regarde l'étiquette en arrivant à la maison.",
            "Dix secondes dans le magasin.",
            "À la maison, il est trop tard pour changer d'avis sans revenir. Et si vous avez "
            "déjà coupé l'étiquette du prix, l'échange devient impossible. L'étiquette du "
            "col se lit debout, dans l'allée.",
            notes="Faire le geste : ouvrir le col, lire, remettre. Cinq secondes.")

    d.pratique('Pratique', "À deux · avant d'acheter",
               "Un client, une conseillère. Deux vêtements.", [
        ("Le client", "demande comment ça se lave, et si ça s'échange"),
        ("La conseillère", "lit l'étiquette à voix haute et répond"),
        ("Le client", "dit lequel il prend, et pourquoi"),
        ("On change de rôle", "après deux vêtements"),
    ], cols=1,
       notes="Vingt minutes. Exiger la raison du choix : c'est ce qui fait la production "
             "orale.")

    d.billet(
        "Comptez ce que vous avez à la maison qui va au nettoyeur.",
        exemples=[
            "Combien de vêtements ? Combien de fois par année ?",
            "Combien ça fait, en dollars ?",
        ],
        notes="Fin du bloc C. Le calcul surprend souvent.")

    return d.save(dossier)
