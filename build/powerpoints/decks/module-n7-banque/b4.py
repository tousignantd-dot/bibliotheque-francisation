# -*- coding: utf-8 -*-
"""B4 · Comparer, et savoir ce qu'on vaut
Bloc B « Défi 1 · Emprunter moins cher » · couleur teal · 90 min.
Source : exercices `t1comp` et `t1cote`, et leurs mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='teal',
        titre="Comparer, et savoir ce qu'on vaut",
        chapeau="« C'est moins cher » ne veut rien dire. Une comparaison, "
                "c'est deux termes nommés, un mot de rapport et une preuve "
                "chiffrée.",
        duree='90 minutes')

    d.titre(notes="Séance en deux temps : la langue de la comparaison d'abord, le "
                  "dossier de crédit ensuite. Les deux se rejoignent à la fin, quand on "
                  "compare deux taux offerts à deux cotes différentes.")

    d.objectifs([
        "comparer avec plus, moins, aussi et autant ;",
        "employer ne... que sans le confondre avec une négation ;",
        "lier deux mouvements avec d'autant plus que ;",
        "dire ce que contient un dossier de crédit, et ce qu'il ignore.",
    ], notes="Le deuxième objectif est un contresens fréquent qui se corrige en une "
             "minute et qui, sans cela, fausse la lecture de tout document financier.")

    d.declencheur(
        'Observation', "« C'est moins cher. » Moins cher que quoi ?",
        pistes=[
            "As-tu déjà vu cette phrase dans une publicité ?",
            "Qu'est-ce qui manque pour qu'elle veuille dire quelque chose ?",
            "Est-ce que le deuxième terme est absent par hasard ?",
            "Qu'est-ce que tu demanderais, toi ?",
        ],
        notes="La troisième question est le coeur de la séance : le deuxième terme est "
              "absent exprès, et le lecteur le remplit tout seul, à l'avantage de "
              "celui qui vend.")

    d.tableau('Analyse', "Six façons de comparer",
              ['La tournure', 'Ce qu\'elle fait'],
              [['plus, moins, aussi... que', 'compare avec un adjectif'],
               ['plus de, autant de... que', 'compare avec un nom'],
               ['ne... que', 'limite, ne nie pas'],
               ["d'autant plus... que", 'lie deux mouvements'],
               ['tandis que, alors que', 'pose deux vérités côte à côte']],
              cle=0,
              notes="Diapositive à photographier. Faire produire une phrase sur chaque "
                    "ligne avec les chiffres du bloc B avant de passer à l'exercice.")

    d.piege('Le piège', "on ne paie que sur la partie utilisée = on ne paie pas",
            "on paie, mais seulement là-dessus",
            "« Ne... que » limite, il ne nie pas. Le réflexe qui marche à tous les "
            "coups : remplacer mentalement par « seulement ». « On ne paie de l'intérêt "
            "que sur la partie utilisée » devient « on paie de l'intérêt seulement sur "
            "la partie utilisée », et le sens saute aux yeux.",
            notes="Contresens fréquent et coûteux : il fait croire qu'une marge est "
                  "gratuite. Y consacrer cinq minutes pleines.")

    d.pratique('Application', "Complétez la comparaison",
               "Un seul mot ou groupe de mots par trou.", [
        ("La marge coûte ___ la carte : 9,45 contre 19,90.", "moins cher que"),
        ("Sur une marge, on ne paie de l'intérêt ___ sur la partie utilisée.", "que"),
        ("Le prêt est ___ la marge, mais il a une date de fin.", "plus cher que"),
        ("La dette est ___ le solde reste élevé longtemps.", "d'autant plus chère que"),
        ("Le taux de la marge est variable, ___ celui du prêt est fixe.", "tandis que"),
        ("Un dépôt à terme rapporte ___ un compte chèque.", "plus que"),
    ], corrige=True,
       notes="Faire relire chaque phrase complète à voix haute. La comparaison est une "
             "affaire de rythme autant que de mots.")

    d.regle("Une comparaison a trois éléments",
            "Les deux termes nommés, le mot de rapport, et une preuve chiffrée.",
            precision="Sans le deuxième terme, la phrase ne dit rien. Sans le chiffre, "
                      "elle n'est qu'une impression. C'est le patron exact de la "
                      "production orale du bloc E, où il faut comparer deux produits en "
                      "quatre-vingt-dix secondes.",
            notes="Diapositive à photographier. La reprendre telle quelle en E1.")

    d.tableau('Le dossier de crédit', "Ce qu'il regarde, ce qu'il ignore",
              ['Il regarde', 'Il ignore'],
              [['payer à temps', 'votre salaire'],
               ['la part du crédit utilisée', 'votre métier'],
               ["l'ancienneté des comptes", 'votre épargne'],
               ['les demandes de prêteurs', 'votre pays d\'origine']],
              cle=0,
              note="Pointage de 300 à 900, chez Equifax et TransUnion.",
              notes="Diapositive à photographier. Fait vérifié : la consultation de son "
                    "propre dossier est gratuite et sans effet sur le pointage.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Le dossier de crédit, d'après ce que le conseiller a expliqué.", [
        ("Il y a deux agences d'évaluation du crédit au Canada.", "vrai"),
        ("Le pointage va de 300 à 900.", "vrai"),
        ("Demander son propre dossier coûte une trentaine de dollars.", "faux - c'est gratuit"),
        ("Demander son propre dossier fait baisser le pointage.", "faux - aucun effet"),
        ("Le dossier indique le salaire de la personne.", "faux - il ignore le revenu"),
        ("Payer à temps compte davantage que gagner beaucoup.", "vrai"),
    ], corrige=True,
       notes="Le cinquième et le sixième vont ensemble, et ils sont encourageants : "
             "insister. Une personne à petit revenu qui paie à temps a une bonne cote.")

    d.billet("Compare deux produits du bloc en une phrase, avec un chiffre.",
             exemples=["La marge coûte moins cher que la carte : 9,45 contre 19,90.",
                       "Le prêt est plus cher que la marge, mais il finit en 80 mois."],
             notes="Trois minutes. Refuser les phrases sans deuxième terme et sans "
                   "chiffre : c'est tout l'objet de la séance.")

    return d.save(dossier)
