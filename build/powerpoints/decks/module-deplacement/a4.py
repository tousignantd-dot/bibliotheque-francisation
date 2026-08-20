# -*- coding: utf-8 -*-
"""A4 · Lire une adresse.
Bloc A « Je découvre » · couleur teal · 50 min.
Source : exercice `prNum` et son encadré de savoir.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='teal',
        titre='Lire une adresse',
        chapeau="340, rue Sainte-Hélène, app. 4. Trois informations dans un "
                "ordre précis — et deux règles que personne n'explique jamais : "
                "les numéros pairs, et le sens dans lequel ils montent.",
        duree='50 minutes')

    d.titre(notes="Séance courte et très concrète. Faire écrire à chacun sa propre adresse "
                  "au tableau dès le début : les erreurs d'ordre apparaissent tout de suite.")

    d.objectifs([
        "écrire une adresse québécoise dans le bon ordre ;",
        "savoir de quel côté de la rue se trouve un numéro ;",
        "savoir si je marche dans la bonne direction en regardant les numéros ;",
        "dicter mon adresse au téléphone sans être repris.",
    ])

    d.tableau('Analyse', "L'ordre des éléments",
              ['Élément', 'Exemple'],
              [["Le numéro civique", "340"],
               ["Le type et le nom de rue", "rue Sainte-Hélène"],
               ["L'appartement, s'il y en a un", "app. 4"],
               ["La ville et le code postal", "Longueuil, J4K 2R1"]],
              cle=0,
              note="Le numéro vient AVANT le nom de la rue. C'est l'inverse de plusieurs pays.",
              notes="Diapo centrale. Faire comparer avec l'ordre en usage dans les pays "
                    "d'origine du groupe : la discussion est courte et très efficace.")

    d.cartes('Les deux règles invisibles', "Ce qui sauve du temps", [
        ("Pair d'un côté, impair de l'autre",
         "Les numéros pairs (2, 4, 340) sont tous du même côté de la rue ; les impairs "
         "(1, 3, 341) de l'autre. Vérifier le numéro AVANT de traverser évite de "
         "traverser deux fois."),
        ("Les numéros montent vers l'extérieur",
         "Ils augmentent en s'éloignant du centre. Si vous marchez et que les numéros "
         "DESCENDENT alors que vous cherchez un grand numéro, vous allez dans la mauvaise "
         "direction."),
        ("La deuxième règle est la plus utile",
         "Elle vous prévient au bout de vingt secondes de marche, avant d'avoir perdu dix "
         "minutes. C'est exactement ce que Nour fera au bloc C, dans l'autobus."),
    ], notes="La troisième carte annonce le dialogue de C4. Le lien vaut la peine d'être "
             "fait : la même logique, appliquée à un autobus.")

    d.regle('Dire son adresse au téléphone',
            "Donnez le numéro chiffre par chiffre, puis le nom de la rue, puis épelez-le.",
            precision="« Trois, quatre, zéro — rue Sainte-Hélène. S, A, I, N, T, E, trait "
                      "d'union… » Personne ne trouve cela lent : c'est ce que font les "
                      "gens d'ici aussi, parce que les noms de rue se ressemblent.",
            notes="Faire pratiquer à deux, dos à dos, pour retirer les gestes et les "
                  "lèvres. Cinq minutes suffisent et l'exercice marque.")

    d.piege("L'ordre inversé",
            "Rue Sainte-Hélène, 340",
            "340, rue Sainte-Hélène",
            "L'ordre inversé se comprend, mais il ralentit tout le monde — au téléphone, "
            "sur un formulaire, chez le médecin. Au Québec, le numéro vient toujours en "
            "premier, suivi d'une virgule.",
            notes="Insister sur la virgule après le numéro : elle est attendue sur tous "
                  "les formulaires.")

    d.pratique('Pratique · 1 de 2', "Pair ou impair, de quel côté ?",
               "Répondez d'après les deux règles.", [
        ("Le 340 est un numéro…", "pair — du même côté que le 342"),
        ("Le 341 est…", "impair — en face du 340"),
        ("Je cherche le 500 et les numéros descendent…", "je vais dans la mauvaise direction"),
        ("Je cherche le 12 et je suis au 340…", "je dois revenir vers le centre"),
        ("Le 338 et le 340 sont…", "du même côté, l'un à côté de l'autre"),
    ], corrige=True, cols=1,
       notes="Faire dessiner une rue au tableau avec quelques numéros de chaque côté. "
             "La règle devient évidente en dix secondes.")

    d.pratique('Pratique · 2 de 2', "Remettre l'adresse en ordre",
               "Récrivez chaque adresse correctement.", [
        ("rue Chambly, 1250, appartement 3", "1250, rue Chambly, app. 3"),
        ("app. 12, boulevard Curé-Poirier, 890", "890, boulevard Curé-Poirier, app. 12"),
        ("Sainte-Hélène 340 rue", "340, rue Sainte-Hélène"),
        ("Victoria, avenue, 77", "77, avenue Victoria"),
    ], corrige=True, cols=1,
       notes="Faire venir quatre élèves au tableau. L'exercice est mécanique, mais il "
             "ancre l'ordre mieux qu'une explication.")

    d.billet(
        "Écrivez votre adresse complète, puis celle de l'école.",
        exemples=[
            "Numéro, virgule, type et nom de rue, appartement, ville.",
            "Indiquez si votre numéro est pair ou impair.",
        ],
        notes="Corriger l'ordre et la virgule. Cette information servira aussi à la "
              "production écrite de E1 — expliquer le chemin pour venir chez soi.")

    return d.save(dossier)
