# -*- coding: utf-8 -*-
"""B3 · Compris dans le loyer, ou à payer en plus ?
Bloc B « Défi 1 · Lire la petite annonce » · couleur teal · 75 min.
Source : exercices `t1incl` et `t1annonce`, mini-leçon `t1annonce`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='teal',
        titre='Compris dans le loyer, ou à payer en plus ?',
        chapeau="Deux logements au même prix affiché ne coûtent pas le même "
                "prix. Ce qui décide tient dans une ligne de six mots.",
        duree='75 minutes')

    d.titre(notes="Séance de calcul, pas de grammaire. Ouvrir avec les billets de la "
                  "séance B1 : plusieurs élèves auront découvert qu'ils paient des "
                  "choses qu'ils croyaient comprises. Partir de là.")

    d.objectifs([
        "distinguer ce qui est compris dans le loyer et ce qui s'ajoute ;",
        "estimer ce que coûte un chauffage non compris, l'hiver ;",
        "écrire un loyer correctement, avec le signe après le nombre ;",
        "comparer deux annonces affichées au même prix.",
    ])

    d.tableau('Analyse', "Ce que dit la ligne, ce que ça coûte",
              ["Dans l'annonce", "Pour votre portefeuille"],
              [["chauffé", "rien de plus à payer l'hiver"],
               ["éclairé", "aucun compte d'électricité"],
               ["non chauffé", "environ 90 $ par mois l'hiver"],
               ["internet non compris", "un compte à ouvrir soi-même"]],
              cle=0,
              note="Les montants sont des ordres de grandeur, pas des tarifs.",
              notes="Diapositive à photographier. Préciser que le 90 $ est une "
                    "estimation pour un logement moyen : il sert à comparer deux "
                    "annonces, pas à faire un budget exact.")

    d.tableau('Analyse', "Deux annonces au même prix affiché",
              ["L'annonce", "Ce qu'on paie vraiment"],
              [["A · 1 150 $, chauffé et éclairé", "1 150 $"],
               ["B · 1 150 $, non chauffé", "environ 1 280 $ l'hiver"],
               ["La différence", "environ 130 $ par mois"],
               ["Sur douze mois", "plusieurs centaines de dollars"]],
              cle=0,
              note="Le nombre affiché ne dit rien tout seul.",
              notes="Diapositive à photographier. Faire le calcul au tableau avec le "
                    "groupe plutôt que de le montrer fini : c'est la démonstration la "
                    "plus utile du module.")

    d.regle("Écrire un loyer en français",
            "1 150 $, et non $1150",
            precision="Le signe de dollar se met après le nombre, séparé par "
                      "une espace. Les milliers se séparent par une espace, "
                      "jamais par une virgule : 1 150 $. La virgule, en "
                      "français, sépare les dollars des cents.",
            notes="Diapositive à photographier. La règle du signe après le nombre "
                  "surprend beaucoup d'élèves venus de systèmes anglophones. Elle sera "
                  "corrigée dans la production écrite de la séance E2.")

    d.tableau('Analyse', "Dire un loyer à voix haute",
              ["On écrit", "On dit"],
              [["1 150 $", "mille cent cinquante dollars"],
               ["1 150 $", "onze cent cinquante dollars"],
               ["850 $", "huit cent cinquante dollars"],
               ["780 $", "sept cent quatre-vingts dollars"]],
              cle=1,
              note="Les deux premières formes sont bonnes. La seconde est très courante ici.",
              notes="Diapositive à photographier. Faire dire les quatre montants à voix "
                    "haute. « Quatre-vingts » est le nombre qui pose problème : le faire "
                    "répéter seul, puis dans la phrase.")

    d.piege('Méthode',
            "comparer deux loyers sans lire la ligne des inclusions",
            "ramener les deux au même point avant de comparer",
            "Deux annonces à 1 150 $ peuvent différer de cent trente dollars "
            "par mois. Le prix affiché est un début de renseignement, pas un "
            "renseignement.",
            notes="C'est l'erreur qui coûte le plus cher dans une recherche de logement, "
                  "et elle est facile à éviter. Le dire simplement.")

    d.piege('Méthode',
            "choisir un logement libre après la fin de son bail",
            "vérifier la date avant même de téléphoner",
            "Si votre bail finit le 30 juin et que le logement est libre le "
            "1er août, vous payez un mois pour rien, ou vous n'avez pas de "
            "logement pendant un mois.",
            notes="Demander au groupe à quelle date finit leur bail. Beaucoup ne le "
                  "sauront pas : c'est un devoir à leur donner.")

    d.pratique('Lecture', "Compris, ou à payer en plus ?",
               "Dites ce que chaque ligne veut dire.", [
        ("« Chauffé »", "compris : rien à payer l'hiver"),
        ("« Éclairé »", "compris : aucun compte d'électricité"),
        ("« Non chauffé »", "à payer en plus, environ 90 $ l'hiver"),
        ("« Internet non compris »", "à payer en plus"),
        ("« Buanderie au sous-sol »", "à payer chaque fois, 2 $ la brassée"),
        ("« Meublé »", "compris : les meubles sont déjà là"),
    ], corrige=True, cols=2,
       notes="C'est l'exercice 5 du Défi 1. Faire remarquer que « buanderie » n'est ni "
             "compris ni exclu : c'est un service qui se paie à l'usage.")

    d.pratique('Écriture', "Écrivez le montant",
               "En chiffres, avec le signe après le nombre.", [
        ("Mille cent cinquante dollars", "1 150 $"),
        ("Huit cent cinquante dollars", "850 $"),
        ("Sept cent quatre-vingts dollars", "780 $"),
        ("Quatre-vingt-dix dollars", "90 $"),
        ("Deux dollars", "2 $"),
        ("Onze cent cinquante dollars", "1 150 $, le même montant"),
    ], corrige=True, cols=2,
       notes="La dernière ligne est là pour montrer que deux façons de dire donnent le "
             "même nombre. C'est ce qui déroute au téléphone, et c'est préparé ici pour "
             "le bloc C.")

    d.billet(
        "Comparez deux annonces au même prix : laquelle coûte vraiment le moins cher ?",
        exemples=[
            "L'annonce ___ coûte moins cher parce que ___ .",
            "La différence est d'environ ___ $ par mois.",
        ],
        notes="Devoir court. Distribuer deux annonces au même prix affiché, l'une "
              "chauffée et l'autre non. Les réponses se reprennent en début de séance "
              "B4.")

    return d.save(dossier)
