# -*- coding: utf-8 -*-
"""D2 · CD ou CI ?
Bloc D · couleur ambre (écriture) · 75 min.
Source : exercices `t3cdci` et `t3cdci2` et leur mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre='CD ou CI ?',
        chapeau="« Ginette montre le sous-sol aux locataires. » Deux compléments dans une "
                "phrase, et un seul mot les distingue : la préposition.",
        duree='75 minutes')

    d.titre(notes="Écrire la phrase du chapeau au tableau et demander ce que Ginette "
                  "montre, et à qui. Les deux questions donnent les deux compléments.")

    d.objectifs([
        "trouver le complément direct avec « qui ? » ou « quoi ? » ;",
        "trouver le complément indirect avec « à qui ? » ou « à quoi ? » ;",
        "reconnaître les deux compléments dans une même phrase ;",
        "savoir pourquoi cette distinction sert.",
    ])

    d.regle('La règle',
            "Le complément direct suit le verbe sans préposition. L'indirect en a une.",
            precision="« Ibrahim visite un logement » — rien entre le verbe et le "
                      "complément : c'est direct. « Leyla téléphone à son frère » — la "
                      "préposition « à » : c'est indirect.",
            notes="Écrire la règle au tableau. Le repère est visuel : y a-t-il un petit "
                  "mot entre le verbe et le complément ?")

    d.tableau('Analyse', "Deux questions, deux compléments",
              ['Le complément', 'La question', 'Un exemple'],
              [["direct (CD)", "qui ? quoi ?", "Ibrahim visite quoi ? un logement"],
               ["indirect (CI)", "à qui ? à quoi ?", "Leyla téléphone à qui ? à son frère"]],
              cle=0, props=[0.24, 0.24, 0.52],
              note="La question se pose au verbe : « visite quoi ? », « téléphone à "
                   "qui ? ». La réponse est le complément.",
              notes="Faire poser la question à voix haute avant chaque réponse. C'est la "
                    "méthode, et elle ne se trompe pas.")

    d.cartes('Ouvrir la mini-leçon', "Quatre choses à savoir en plus", [
        ("Pourquoi cette distinction sert",
         "Le pronom n'est pas le même : « je le vois » (direct) et « je lui parle » "
         "(indirect). C'est la règle du module 6, et elle repose sur celle-ci."),
        ("Le CI n'a pas toujours « à »",
         "« Je parle de mon logement », « je compte sur elle », « je pense à toi ». "
         "Toute préposition rend le complément indirect."),
        ("Une phrase peut avoir les deux",
         "« Ginette montre le sous-sol aux locataires. » Le sous-sol est direct, les "
         "locataires sont indirects."),
        ("Certains verbes exigent une préposition",
         "On téléphone à quelqu'un, on parle à quelqu'un, on répond à quelqu'un. La "
         "préposition fait partie du verbe : elle s'apprend avec lui."),
    ], notes="La première carte donne la raison d'être de la séance. La donner en "
             "premier si le groupe demande à quoi cela sert.")

    d.pratique('Pratique · 1 de 4', "Trouvez le complément",
               "Posez la question au verbe.", [
        ("Ibrahim visite un logement lumineux.", "CD : un logement lumineux"),
        ("Leyla téléphone à son frère.", "CI : à son frère"),
        ("La propriétaire fournit la peinture.", "CD : la peinture"),
        ("Ibrahim pense à son déménagement.", "CI : à son déménagement"),
        ("Le boulanger reçoit une livraison de farine.", "CD : une livraison de farine"),
    ], corrige=True,
       notes="Faire poser la question à voix haute : « visite quoi ? », « téléphone à "
             "qui ? ». Sans elle, l'exercice devient une intuition.")

    d.pratique('Pratique · 2 de 4', "Les deux compléments",
               "Trouvez le CD, puis le CI.", [
        ("Ginette montre le sous-sol aux nouveaux locataires.",
         "CD : le sous-sol · CI : aux nouveaux locataires"),
        ("Ibrahim explique son horaire de soir à la propriétaire.",
         "CD : son horaire de soir · CI : à la propriétaire"),
        ("Leyla offre un ventilateur à son frère.",
         "CD : un ventilateur · CI : à son frère"),
        ("Le concierge remet les clés au nouveau locataire.",
         "CD : les clés · CI : au nouveau locataire"),
    ], corrige=True,
       notes="Faire remarquer l'ordre : le CD vient presque toujours avant le CI en "
             "français. C'est un repère utile.")

    d.piege("Le piège de la préposition contractée",
            "« aux locataires » n'a pas de préposition.",
            "« aux » est la contraction de « à les ».",
            "« Au », « aux », « du », « des » sont des prépositions contractées avec un "
            "déterminant. « Aux locataires » veut dire « à les locataires » : il y a "
            "bien une préposition, donc c'est un complément indirect.",
            notes="Point technique important. Faire décomposer les quatre formes au "
                  "tableau : au, aux, du, des.")

    d.piege("Le piège de la question mal posée",
            "Ibrahim visite qui ? — personne.",
            "Ibrahim visite quoi ? — un logement.",
            "Il faut poser les deux questions : « qui ? » pour une personne, « quoi ? » "
            "pour une chose. Si aucune des deux ne donne de réponse, il n'y a pas de "
            "complément direct — et il faut essayer « à qui ? » ou « à quoi ? ».",
            notes="Faire essayer les quatre questions systématiquement au début. Avec la "
                  "pratique, on voit tout de suite laquelle poser.")

    d.pratique('Pratique · 3 de 4', "CD, CI, ou les deux ?",
               "Combien de compléments dans la phrase ?", [
        ("Ibrahim signe le bail.", "un CD"),
        ("Ibrahim pense à son déménagement.", "un CI"),
        ("Ginette remet les clés à Ibrahim.", "un CD et un CI"),
        ("Leyla répond à sa mère.", "un CI"),
        ("Le propriétaire fournit la peinture aux locataires.", "un CD et un CI"),
    ], corrige=True,
       notes="Faire compter les compléments avant de les nommer. Le compte oriente la "
             "recherche.")

    d.pratique('Pratique · 4 de 4', "Remplacez par un pronom",
               "Le CD devient le, la, les. Le CI devient lui, leur.", [
        ("Ibrahim signe le bail.", "Ibrahim le signe."),
        ("Leyla téléphone à son frère.", "Leyla lui téléphone."),
        ("Ginette fournit la peinture.", "Ginette la fournit."),
        ("Le propriétaire répond aux locataires.", "Le propriétaire leur répond."),
        ("Ibrahim explique son horaire à la propriétaire.", "Ibrahim lui explique son horaire."),
    ], corrige=True,
       notes="C'est le lien avec le module 6. Faire remarquer que la distinction CD et CI "
             "sert exactement à cela : choisir le bon pronom.")

    d.billet(
        "Écrivez trois phrases sur un logement.",
        exemples=[
            "Une avec un CD, une avec un CI, une avec les deux.",
            "Soulignez le CD une fois et le CI deux fois.",
        ],
        notes="Corriger l'identification avant tout. Rendre avant E1 : ces compléments "
              "reviennent dans la lettre de motivation.")

    return d.save(dossier)
