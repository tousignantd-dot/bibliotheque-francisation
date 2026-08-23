# -*- coding: utf-8 -*-
"""B2 · Deuxième écoute : les chiffres exacts
Bloc B « Défi 1 » · couleur acier · 75 min.
Source : reportage `t1`, exercices `t1chiffres` et `t1qui`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='acier',
        titre="Deuxième écoute : les chiffres exacts",
        chapeau="On peut maintenant arrêter l'extrait et revenir en arrière. "
                "Un économiste ne donne jamais un chiffre tout seul : il le "
                "compare — et c'est la comparaison qui porte l'information.",
        duree='75 minutes')

    d.titre(notes="Deuxième séance du Défi 1. Rappeler la méthode de B1 avant de "
                  "relancer l'extrait, et redire qu'on a le droit d'arrêter la bande "
                  "autant de fois qu'on veut.")

    d.objectifs([
        "relever des pourcentages et des grands nombres à l'oral ;",
        "comprendre qu'un chiffre seul ne dit rien ;",
        "rattacher chaque parole à la personne qui l'a dite ;",
        "distinguer une part de l'emploi d'un nombre de postes.",
    ], notes="Le dernier objectif prépare tout le bloc C : « onze virgule deux pour "
             "cent » n'est pas « onze mille emplois ».")

    d.declencheur(
        'Écoute', "Comment dit-on ces nombres à la radio ?",
        pistes=[
            "4,2 % — « quatre virgule deux pour cent ».",
            "15,5 G$ — « quinze virgule cinq milliards de dollars ».",
            "137 100 — « cent trente-sept mille cent ».",
            "286 395 — « deux cent quatre-vingt-six mille trois cent quatre-vingt-quinze ».",
        ],
        notes="Faire dire les quatre à voix haute avant l'écoute. La virgule décimale "
              "se dit « virgule » et non « point » : c'est la source d'erreur la plus "
              "fréquente chez les élèves venus d'un pays anglophone.")

    d.regle("Un chiffre seul ne dit rien",
            "Quatre virgule deux pour cent : est-ce beaucoup ? On n'en sait "
            "rien. Quatre virgule deux, contre deux pour cent au Québec : "
            "maintenant on sait, et on sait l'essentiel.",
            precision="Le mot qui annonce la comparaison est presque toujours "
                      "« contre ». À la radio comme dans un document écrit, c'est le "
                      "signal à attendre. Le deuxième chiffre est celui qui compte.",
            notes="Diapositive à photographier. C'est aussi la règle de l'exposé oral "
                  "du bloc E : un pourcentage sans point de comparaison ne convainc "
                  "personne.")

    d.dialogue('Reportage · les chiffres', "Ce que le territoire produit", [
        ("ODILE", "La région compte un peu plus de deux cent quatre-vingt-six mille habitants, onzième sur dix-sept.", True),
        ("ODILE", "Son produit intérieur brut a atteint quinze virgule cinq milliards de dollars en 2023.", True),
        ("ODILE", "Et l'emploi total tournait autour de cent trente-sept mille postes en 2025.", True),
        ("GHISLAIN", "Onze virgule deux pour cent des emplois en fabrication, et surtout une fabrication d'un type très précis.", True),
    ], consigne="Réécoutez. Vous pouvez arrêter et revenir en arrière.",
       notes="Passer l'extrait trois fois de suite si nécessaire. Le but n'est pas la "
             "performance d'écoute : c'est de vérifier un chiffre entendu.")

    d.dialogue('Reportage · le manque', "Onze candidatures en six mois", [
        ("GHISLAIN", "Ces postes-là, les postes de contrôle de la qualité, on ne les remplit plus. La relève ne suit pas.", True),
        ("GHISLAIN", "À Montréal, il y a moins de postes ouverts et plus de candidats. Ici, c'est l'inverse.", True),
        ("GHISLAIN", "Un employeur de Montréal choisit ; un employeur d'ici convainc.", True),
        ("FRÉDÉRICK", "Ils sont simplement tous ailleurs, et ils n'imaginent pas qu'on cherche ici.", True),
    ], notes="La troisième réplique est la phrase à retenir du module. La faire "
             "répéter et l'écrire au tableau à côté de celle de A1.")

    d.tableau('Analyse', "Les chiffres du reportage",
              ['Ce qui est mesuré', 'Le chiffre'],
              [["Population", "286 395 habitants, 11e sur 17"],
               ["PIB régional, 2023", "15,5 milliards de dollars"],
               ["Emploi total, 2025", "137 100 postes"],
               ["Secteur primaire", "4,2 % contre 2,0 % au Québec"],
               ["Construction", "8,9 % contre 7,0 % au Québec"]],
              cle=0,
              note="Deux dates dans le même document : 2023 et 2025.",
              notes="Diapositive à photographier. Signaler les deux dates : un portrait "
                    "économique n'est jamais tout entier de l'année en cours.")

    d.pratique('Compréhension', "Deuxième écoute : les chiffres",
               "Complétez d'après le reportage.", [
        ("La région se classe ___ sur les dix-sept régions du Québec.", "onzième"),
        ("Son produit intérieur brut a atteint ___ milliards de dollars.", "15,5"),
        ("L'emploi total tournait autour de ___ postes en 2025.", "137 100"),
        ("Le secteur primaire occupe ___ % de l'emploi régional.", "4,2"),
        ("La fabrication occupe ___ % des emplois.", "11,2"),
        ("La construction occupe ___ % de l'emploi.", "8,9"),
        ("Le laboratoire d'Alumico compte ___ personnes sur neuf.", "sept"),
        ("L'employeur n'a reçu que ___ candidatures en six mois.", "onze"),
    ], corrige=True,
       notes="Exercice `t1chiffres` du module interactif. Accepter le chiffre écrit "
             "en lettres ou en nombres : c'est l'écoute qu'on évalue, pas l'orthographe.")

    d.pratique('Compréhension', "Qui dit quoi ?",
               "Rendez à chacun ce qu'il a dit.", [
        ("« Le premier chiffre à retenir n'est pas le plus gros. »", "Ghislain Néron, économiste"),
        ("« J'ai deux postes affichés depuis février. »", "Frédérick Gauthier-Simard, employeur"),
        ("« La semaine prochaine, Chaudière-Appalaches. »", "Odile Pominville, journaliste"),
        ("« Ce que je ne peux pas enseigner, c'est la rigueur. »", "le chef du laboratoire"),
        ("« Un employeur de Montréal choisit ; un employeur d'ici convainc. »", "l'économiste"),
    ], corrige=True,
       notes="Exercice `t1qui` du module interactif. Faire remarquer que la nature de "
             "l'information change avec la personne : un chiffre, un témoignage, un "
             "résumé.")

    d.billet(
        "Écrivez le chiffre du reportage qui vous a le plus étonné, et pourquoi.",
        exemples=[
            "Un seul chiffre, une phrase d'explication.",
            "Comparez-le à ce que vous connaissez de votre région.",
        ],
        notes="Ressortir les billets de B1 en même temps : les élèves mesurent d'un "
              "coup d'œil ce que deux écoutes de plus leur ont donné.")

    return d.save(dossier)
