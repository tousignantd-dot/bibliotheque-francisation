# -*- coding: utf-8 -*-
"""C2 · Plus cher, moins cher, aussi cher.
Bloc C « Défi 2 · Comparer deux prix » · couleur ambre (écriture) · 60 min.
Source : exercice `t2comparer`, mini-leçon `t2comparer`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre='Plus cher, moins cher, aussi cher',
        chapeau="Trois mots, un adjectif, et le petit mot « que ». Une fois "
                "ce moule appris, il sert pour le prix, la chaleur, la "
                "longueur — tout ce qui se compare.",
        duree='60 minutes')

    d.titre(notes="Séance d'écriture. Reprendre les chiffres relevés au billet de C1 : la "
                  "comparaison se fait sur des prix réels, pas inventés.")

    d.objectifs([
        "employer plus … que, moins … que, aussi … que ;",
        "ne pas oublier le mot « que » ;",
        "accorder l'adjectif dans une comparaison ;",
        "employer « meilleur » au lieu de « plus bon ».",
    ])

    d.declencheur(
        'Question', "Comment dites-vous que 65 $ est moins que 99 $ ?",
        pistes=[
            "En une phrase complète.",
            "Avec le mot « bottes » dedans.",
            "Et si les deux coûtaient 99 $ ?",
            "Et pour la chaleur, pas le prix ?",
        ],
        notes="Laisser produire des phrases fautives, les noter au tableau, et corriger "
              "après le tableau d'analyse. C'est plus efficace que l'inverse.")

    d.tableau('Analyse', "Le moule de la comparaison",
              ['On dit', 'Ça veut dire'],
              [["plus cher que", "il coûte davantage"],
               ["moins cher que", "il coûte moins"],
               ["aussi cher que", "les deux coûtent pareil"],
               ["meilleur que", "irrégulier — jamais « plus bon »"]],
              cle=0,
              note="L'adjectif se glisse au milieu, et « que » ferme toujours la phrase.",
              notes="Diapo centrale, à photographier. Faire lire les quatre lignes, puis "
                    "faire produire une phrase complète pour chacune.")

    d.regle("Le « que » ne se saute pas",
            "« Les bottes sont moins chères <b>que le manteau</b>. »",
            precision="Sans « que », la phrase reste en l'air : moins chères que quoi ? "
                      "Quand le deuxième article vient d'être nommé, on peut dire « que "
                      "l'autre » — mais on dit quelque chose. C'est l'erreur la plus "
                      "fréquente, et la plus facile à corriger.",
            notes="Diapo à photographier. Faire relire les phrases fautives du déclencheur "
                  "en ajoutant le « que » manquant.")

    d.cartes("Trois choses qui se comparent, au magasin", "Et les mots qui vont avec", [
        ("Le prix",
         "plus cher, moins cher, aussi cher. C'est la comparaison la plus utile — et celle "
         "qui décide l'achat."),
        ("La chaleur et la matière",
         "plus chaud, moins chaud. « La laine est plus chaude que l'acrylique » : une "
         "phrase qu'on entend vraiment dans un magasin d'ici."),
        ("La taille et la longueur",
         "plus grand, plus long, plus court. « Celui-ci est plus long que celui-là » sert "
         "à choisir entre deux manteaux."),
    ], notes="Faire produire une phrase de chaque type, à partir de vêtements réels du "
             "groupe.")

    d.regle("Deux formes irrégulières",
            "bon donne <b>meilleur</b> · bien donne <b>mieux</b>",
            precision="« Plus bon » n'existe pas. On dit « la laine est <b>meilleure</b> "
                      "que l'acrylique ». Et « meilleur » s'accorde comme un adjectif "
                      "ordinaire : meilleur, meilleure, meilleurs, meilleures. Ce sont les "
                      "deux seules irrégularités de ce niveau.",
            notes="Diapo à photographier. Deux formes, pas davantage : ne pas alourdir.")

    d.piege("Oublier d'accorder",
            "Ces bottes sont plus cher.",
            "Ces bottes sont plus chères.",
            "Comparer ne dispense pas d'accorder : l'adjectif suit toujours le vêtement. "
            "Des bottes, c'est féminin pluriel — donc « chères », avec un e et un s, comme "
            "au défi 1.",
            notes="Rappeler la règle de B2 : c'est le même accord, dans une autre phrase.")

    d.pratique('Pratique', "Plus, moins ou aussi ?",
               "Complétez chaque phrase.", [
        ("65 $ et 99 $ : les bottes en liquidation sont ___ chères.", "moins"),
        ("La laine est ___ chaude que l'acrylique.", "plus"),
        ("120 $ et 120 $ : les deux manteaux sont ___ chers.", "aussi"),
        ("Le chandail à 28 $ est ___ cher que celui à 40 $.", "moins"),
        ("Une tuque de laine est ___ chaude qu'une casquette.", "plus"),
        ("Cette tuque à 22 $ est ___ chère que celle à 14 $.", "plus"),
    ], corrige=True,
       notes="Utiliser l'exercice 2 du défi 2. Faire relire la phrase complète après "
             "correction, avec l'accord de l'adjectif.")

    d.billet(
        "Comparez deux vêtements que vous possédez, en quatre phrases.",
        exemples=[
            "Le prix, la chaleur, la longueur, la matière.",
            "N'oubliez pas le mot « que ».",
        ],
        notes="Ramasser. Vérifier surtout la présence du « que » et l'accord de "
              "l'adjectif : ce sont les deux points de la séance.")

    return d.save(dossier)
