# -*- coding: utf-8 -*-
"""A4 · Les valeurs morales dans les publicités.
Bloc A · couleur foret (vocabulaire) · 60 min.
Source : exercice `prValeurs` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='foret',
        titre='Les valeurs des publicités',
        chapeau="Une publicité ne vend pas seulement un service : elle propose une façon "
                "de voir les choses. Réparer plutôt que jeter, c'est un geste — et "
                "c'est aussi une valeur.",
        duree='60 minutes')

    d.titre(notes="Séance de vocabulaire et d'analyse. Le mot « valeur » est abstrait : "
                  "partir d'exemples concrets et remonter au mot, jamais l'inverse.")

    d.objectifs([
        "nommer une valeur morale mise en avant par une publicité ;",
        "connaître une quinzaine de valeurs courantes ;",
        "distinguer ce qui est dit de ce qui est suggéré ;",
        "choisir la valeur qui convient à son propre message.",
    ])

    d.regle('La définition',
            "Une valeur morale, c'est ce qu'une personne ou une société considère comme important et bien.",
            precision="L'entraide, l'autonomie, l'écologie, la famille, la sécurité. Ce "
                      "ne sont pas des objets ni des services : ce sont des raisons de "
                      "faire quelque chose.",
            notes="Écrire la définition au tableau. Demander deux ou trois exemples au "
                  "groupe avant d'afficher la liste.")

    d.tableau('Analyse', "Quinze valeurs courantes",
              ['Autour de soi', 'Autour des autres', 'Autour du monde'],
              [["l'autonomie", "l'entraide", "l'écologie"],
               ["le courage", "la coopération", "la justice"],
               ["la liberté", "la famille", "la sécurité"],
               ["le plaisir", "l'ouverture à l'autre", "la simplicité"],
               ["la découverte", "le partage", "le travail"]],
              cle=0,
              notes="Le classement en trois colonnes est une aide, pas une règle. "
                    "Certaines valeurs pourraient aller dans deux colonnes.")

    d.cartes('Analyse', "Comment trouver la valeur d'une publicité", [
        ("Regardez ce qu'on montre",
         "Trois voisins qui réparent ensemble un vélo : ce n'est pas le vélo qui "
         "compte, c'est le « ensemble ». La valeur est la coopération."),
        ("Regardez ce qu'on évite",
         "Un service qui remet en état plutôt que de remplacer met en avant "
         "l'écologie — sans forcément prononcer le mot."),
        ("Regardez à qui on parle",
         "Une invitation aux personnes nouvellement arrivées met en avant l'ouverture "
         "à l'autre. Le récepteur choisi porte la valeur."),
        ("Regardez ce qu'on promet",
         "« Apprenez à faire vos réparations vous-même » promet l'autonomie. Ce qu'on "
         "gagne est souvent la valeur."),
    ], notes="Quatre méthodes, toutes valables. Faire essayer les quatre sur une même "
             "publicité : elles donnent parfois des valeurs différentes.")

    d.pratique('Pratique · 1 de 4', "Quelle valeur ?",
               "Une valeur par publicité.", [
        ("Trois voisins réparent ensemble une bicyclette.", "la coopération"),
        ("Un service remet en état les appareils au lieu de les remplacer.", "l'écologie"),
        ("Les personnes nouvellement arrivées sont invitées à prendre un café.",
         "l'ouverture à l'autre"),
        ("Un cours du soir apprend à faire ses réparations soi-même.", "l'autonomie"),
        ("Une grand-mère enseigne la couture à des adolescents.", "le partage"),
    ], corrige=True,
       notes="Plusieurs réponses se défendent pour chaque item. Accepter toute valeur "
             "justifiée : c'est la justification qu'on évalue.")

    d.pratique('Pratique · 2 de 4', "Deux valeurs par publicité",
               "Les publicités en portent souvent plus d'une.", [
        ("L'atelier de réparation du quartier.", "l'écologie et l'entraide"),
        ("Le salon des métiers manuels.", "l'autonomie et la découverte"),
        ("La bibliothèque d'outils.", "le partage et la simplicité"),
        ("La clinique de vélo bénévole.", "la coopération et l'autonomie"),
    ], corrige=True,
       notes="Faire chercher les deux valeurs séparément : celle du geste, et celle de "
             "la manière dont il se fait.")

    d.piege("Le piège de la valeur inventée",
            "Cette publicité met en avant le bonheur.",
            "Cherchez ce qui est montré, pas ce qui est agréable.",
            "Presque toutes les publicités promettent d'être heureux : ce n'est donc pas "
            "une valeur qui les distingue. Cherchez ce qui est propre à celle-ci : "
            "qu'est-ce qu'on montre, et qu'est-ce qu'on évite ?",
            notes="Nommer les valeurs vagues à éviter : le bonheur, le bien-être, la "
                  "qualité. Elles ne disent rien.")

    d.piege("Le piège de la valeur non dite",
            "Le mot « écologie » n'est pas dans le texte, donc ce n'est pas la valeur.",
            "Une valeur est presque toujours suggérée, pas nommée.",
            "Une publicité qui dirait « nous mettons en avant l'écologie » serait "
            "maladroite. Elle montre plutôt un objet réparé, un bénévole, un geste. La "
            "valeur se lit entre les lignes — et c'est ce qui la rend efficace.",
            notes="Point d'analyse important. Faire chercher, dans les vraies publicités, "
                  "si la valeur est nommée. Presque jamais.")

    d.pratique('Pratique · 3 de 4', "Dit ou suggéré ?",
               "La valeur est-elle écrite dans le texte ?", [
        ("« Rien ne se jette, tout se répare. »", "suggéré — l'écologie, sans le mot"),
        ("« Nos mécaniciens bénévoles vous montreront à régler vos freins. »",
         "suggéré — l'autonomie et l'entraide"),
        ("« Un lieu ouvert à tous, sans exception. »", "dit — l'ouverture à l'autre"),
        ("« Vos mains savent plus que vous croyez. »", "suggéré — l'autonomie"),
    ], corrige=True,
       notes="Le troisième item est le seul où la valeur est presque nommée. Faire "
             "remarquer que c'est aussi le moins convaincant.")

    d.pratique('Pratique · 4 de 4', "Choisissez votre valeur",
               "Pour l'événement de votre billet de A1.", [
        ("La valeur principale", "une seule, choisie dans la liste"),
        ("Comment la montrer", "un geste, une image, une phrase — sans nommer la valeur"),
        ("Le récepteur", "à qui cette valeur parle-t-elle ?"),
        ("Le slogan possible", "une phrase courte qui la porte"),
    ], corrige=False,
       notes="Dix minutes. C'est la préparation directe de E1 : garder les feuilles.")

    d.billet(
        "Nommez la valeur d'une publicité que vous aimez, et celle d'une publicité que vous n'aimez pas.",
        exemples=[
            "Une valeur par publicité, avec ce qui vous l'a fait deviner.",
            "N'importe quelle publicité : télévision, autobus, téléphone.",
        ],
        notes="Le contraste entre les deux est instructif. Lire quelques billets : les "
              "raisons de ne pas aimer sont souvent les plus fines.")

    return d.save(dossier)
