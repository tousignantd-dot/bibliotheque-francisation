# -*- coding: utf-8 -*-
"""B1 · Vingt-cinq secondes chaudes, cinq secondes froides
Bloc B « Défi 1 · Trente secondes, et la moitié à la fin » · acier · 75 min.
Source : dialogue `t1`, exercices `t1vf` et `t1capsule`.
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n7-publicite' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Vingt-cinq secondes chaudes, cinq secondes froides",
        chapeau="Une capsule de radio dure trente secondes. Vingt-cinq sont "
                "lentes et souriantes ; les cinq dernières sont plates et "
                "deux fois plus rapides. Ce n'est pas un hasard.",
        duree='75 minutes')

    d.titre(notes="Première séance du Défi 1. Faire écouter la capsule d'Élan Cardio "
                  "en entier avant d'ouvrir quoi que ce soit — et demander ensuite "
                  "ce que le groupe a retenu. Presque personne n'aura la fin.")

    d.objectifs([
        "reconnaître les quatre temps d'une capsule publicitaire ;",
        "situer la mention légale et savoir ce qu'elle contient ;",
        "relever les chiffres d'une annonce entendue ;",
        "expliquer pourquoi un prix s'annonce par semaine et non par année.",
    ], notes="Le quatrième objectif est le plus rentable de la séance : c'est un "
             "calcul, et il se refait devant n'importe quelle annonce.")

    d.declencheur(
        'Écoute', "Qu'avez-vous retenu de cette annonce ?",
        image=IMG + 'console-radio.jpg',
        pistes=[
            "Le nom de l'entreprise ? Le prix ?",
            "Combien de temps dure l'engagement ?",
            "Y a-t-il des frais en plus ? Combien ?",
            "Qu'est-ce qui était dit à la toute fin ?",
        ],
        notes="Les deux premières questions trouvent toujours réponse, les deux "
              "dernières presque jamais. C'est la démonstration de la séance, et "
              "elle se fait toute seule.")

    d.dialogue('Dialogue · 1 de 3', "La capsule, mot pour mot", [
        ("ANNONCEUR", "Cet hiver, à Élan Cardio, prenez enfin soin de vous.", True),
        ("ANNONCEUR", "Nos entraîneurs pourraient vous faire découvrir un corps que vous ne connaissez pas encore.", True),
        ("ANNONCEUR", "Plus de vingt appareils neufs. Un environnement plus chaleureux. Et tout ça pour seulement neuf quatre-vingt-dix-neuf par semaine.", True),
        ("ANNONCEUR", "Offre valable sur adhésion de douze mois, frais d'adhésion de soixante dollars applicables, taxes en sus, certaines conditions s'appliquent.", True),
    ], consigne="Écoutez d'abord, diapositive masquée. Puis lisez.",
       notes="Le contraste entre l'écoute et la lecture est l'objet de la séance. "
             "Écrite, la capsule se démonte en deux minutes ; entendue, elle passe.")

    d.dialogue('Dialogue · 2 de 3', "La fin, et pourquoi elle est rapide", [
        ("YAMILÉ", "La fin, je ne l'ai pas comprise. Pas un mot.", True),
        ("RÉGINALD", "Bien sûr que non. Et pourtant c'est la fin qui contient tout ce que vous aviez besoin de savoir.", True),
        ("RÉGINALD", "Douze mois. Soixante dollars. Taxes en sus. Trois choses en cinq secondes.", True),
        ("YAMILÉ", "Donc ils respectent la loi en la rendant incompréhensible.", True),
    ], notes="La dernière réplique est de l'élève, pas du spécialiste, et c'est voulu. "
             "Laisser le groupe la commenter : c'est la meilleure entrée dans la "
             "notion de mention légale.")

    d.dialogue('Dialogue · 3 de 3', "La deuxième capsule", [
        ("ANNONCEUR", "Vous ne dormez plus comme avant. Chez Boréa Literie, il ne reste que trois jours à notre grande vente d'entrepôt.", True),
        ("ANNONCEUR", "Jusqu'à quarante pour cent de rabais sur les matelas sélectionnés.", True),
        ("YAMILÉ", "« Il ne reste que trois jours. » Ça, je comprends. Il faut se dépêcher.", True),
        ("RÉGINALD", "Et le lundi suivant, la vente recommence sous un autre nom.", True),
    ], notes="Deuxième capsule, plus courte et plus fine. Elle sert au travail des "
             "séances B3 et B4 : le comparatif et la restriction y sont tous les deux.")

    d.tableau('Analyse', "Les quatre temps d'une capsule",
              ['Le temps', 'Ce qu\'il contient'],
              [["L'accroche", "une saison, un malaise, un impératif"],
               ["La promesse", "ce que vous obtiendriez, souvent au conditionnel"],
               ["L'offre", "le chiffre : un prix, un rabais, une durée limitée"],
               ["Le nom et le slogan", "répétés sur la musique, ce que vous retiendrez"],
               ["La mention légale", "hors musique, au double du débit"]],
              cle=0,
              note="La cinquième n'est pas un temps : elle est collée à la fin.",
              notes="Diapositive à photographier. Ce plan est celui de presque toutes "
                    "les capsules commerciales, quel que soit le produit.")

    d.regle("Le prix par semaine n'est pas le prix",
            "Neuf dollars quatre-vingt-dix-neuf par semaine, c'est cinq cent "
            "dix-neuf dollars par année.",
            precision="Les deux chiffres disent la même chose ; le premier se laisse "
                      "écouter, le second fait réfléchir. Par jour pour une "
                      "assurance, par semaine pour un abonnement, par mois pour une "
                      "voiture : l'unité de temps se choisit toujours.",
            notes="Diapositive à photographier. Faire faire le calcul au tableau, "
                  "calculatrice permise. Le rapport entre les deux nombres frappe.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après les deux capsules.", [
        ("La partie chaude dure environ vingt-cinq secondes.", "vrai"),
        ("La mention légale est dite au même débit que le reste.", "faux - deux fois plus vite"),
        ("L'abonnement suppose un engagement de douze mois.", "vrai"),
        ("Les taxes sont comprises dans le prix annoncé.", "faux - taxes en sus"),
        ("La vente de matelas porte sur tous les matelas du magasin.", "faux - les matelas sélectionnés"),
        ("« Il ne reste que trois jours » veut dire : trois jours, pas un de plus.", "vrai"),
    ], corrige=True,
       notes="Exercice `t1vf` du module. Faire justifier chaque « faux » par le mot "
             "exact de la capsule : c'est l'entraînement à la citation.")

    d.billet(
        "Réécoutez la capsule d'Élan Cardio et notez tous les chiffres entendus.",
        exemples=[
            "Il y en a cinq. Combien en attrapez-vous ?",
            "Notez aussi celui que vous avez manqué deux fois.",
        ],
        notes="Devoir d'écoute répétée. Cinq chiffres : vingt appareils, neuf "
              "quatre-vingt-dix-neuf, douze mois, soixante dollars, et le rang de "
              "« plus grand centre ». Personne ne les a tous à la première écoute.")

    return d.save(dossier)
