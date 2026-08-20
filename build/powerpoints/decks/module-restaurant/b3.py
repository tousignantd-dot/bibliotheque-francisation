# -*- coding: utf-8 -*-
"""B3 · Ce qui est compris, ce qui s'ajoute.
Bloc B · couleur ambre (écriture) · 60 min.
Source : exercices `t1menu` et `prFormule`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Ce qui est compris, ce qui s'ajoute",
        chapeau="Deux plats au même prix ne comprennent pas la même chose. "
                "La différence est dans une petite ligne, sous le prix — et "
                "elle vaut souvent plusieurs dollars.",
        duree='60 minutes')

    d.titre(notes="Distribuer les menus rapportés au billet de A3. Toute la séance se fait "
                  "sur du vrai.")

    d.objectifs([
        "repérer la ligne qui dit ce qui est compris ;",
        "reconnaître « servi avec », « au choix », « supplément » ;",
        "calculer le prix réel d'une formule ;",
        "choisir la formule la plus avantageuse pour soi.",
    ])

    d.tableau('Analyse', "Les mots qui changent le prix",
              ['Le mot', 'Ce qu\'il veut dire'],
              [["servi avec", "c'est compris, rien à payer de plus"],
               ["au choix", "vous décidez, dans une liste"],
               ["inclus", "compris dans le prix affiché"],
               ["supplément", "ça coûte plus cher"],
               ["prix du marché", "il faut demander le prix"]],
              cle=3,
              note="Le quatrième est le seul qui augmente la facture. Il est toujours écrit petit.",
              notes="Diapo à photographier. Faire chercher ces cinq mots dans les menus "
                    "distribués.")

    d.regle("La ligne sous le prix",
            "C'est là qu'est la vraie différence.",
            precision="« Poulet grillé — 24 $ » et « Poulet grillé — 24 $, servi avec soupe "
                      "et café » sont deux offres très différentes au même prix affiché. "
                      "La deuxième vaut six ou sept dollars de plus.",
            notes="Faire comparer deux plats du même menu. L'écart de contenu au même prix "
                  "surprend souvent.")

    d.regle("Le calcul de la formule",
            "Prix fixe contre plats commandés séparément.",
            precision="Table d'hôte 32 $. Le même plat seul coûte 24 $, une soupe 6 $, un "
                      "dessert 8 $ — soit 38 $. La formule fait économiser six dollars, à "
                      "condition d'avoir assez faim pour trois services.",
            notes="Faire le calcul au tableau. C'est le raisonnement le plus concret du "
                  "module.")

    d.piege("Ne pas voir le supplément",
            "La table d'hôte est à 32 $, je prends le poisson.",
            "Table d'hôte 32 $ — supplément 4 $ pour le poisson. Ça fait 36 $.",
            "Le supplément est toujours écrit petit, souvent entre parenthèses, souvent à "
            "côté du plat concerné plutôt qu'à côté du prix. C'est le seul mot du menu qui "
            "augmente la facture sans qu'on s'en aperçoive.",
            notes="Faire chercher un supplément dans les menus distribués. Il y en a "
                  "presque toujours un.")

    d.pratique('Pratique · 1 de 2', "Ça coûte combien ?",
               "Calculez le prix réel.", [
        ("Table d'hôte 32 $, supplément 4 $ pour le poisson", "36 $"),
        ("Plat 24 $, soupe 6 $, dessert 8 $, commandés séparément", "38 $"),
        ("Menu du midi 18 $, café inclus", "18 $"),
        ("Plat 22 $, servi avec salade et café", "22 $ — tout est compris"),
        ("Plat du jour « prix du marché »", "il faut demander"),
    ], corrige=True, cols=1,
       notes="Les deux premières lignes se comparent : 36 $ contre 38 $. La formule reste "
             "avantageuse même avec le supplément.")

    d.pratique('Pratique · 2 de 2', "Quelle formule pour vous ?",
               "Choisissez et justifiez.", [
        ("Vous avez très faim et vous voulez un dessert.", "la table d'hôte"),
        ("Vous voulez seulement un plat.", "à la carte"),
        ("Vous êtes le midi et vous voulez un café.", "le menu du midi, café inclus"),
        ("Vous voulez le poisson frais du jour.", "le plat du jour, en demandant le prix"),
    ], corrige=True, cols=1,
       notes="Faire justifier oralement. Le raisonnement compte plus que la réponse.")

    d.cartes("Trois habitudes utiles", "Au moment de commander", [
        ("Lire la ligne sous le prix",
         "Deux secondes, et on sait ce qui est compris."),
        ("Demander le prix quand il n'est pas écrit",
         "« Prix du marché » veut dire qu'il faut demander. Personne ne trouve la question "
         "déplacée."),
        ("Compter les services",
         "Si vous ne mangez pas de dessert, une table d'hôte n'est pas une économie. La "
         "formule ne vaut que si on la consomme."),
    ], notes="La troisième carte évite l'erreur inverse : prendre une formule par principe, "
             "et laisser deux assiettes.")

    d.billet(
        "Choisissez un menu réel et composez deux repas : un à la carte, un en formule.",
        exemples=[
            "Calculez le prix de chacun.",
            "Dites lequel vous choisiriez, et pourquoi.",
        ],
        notes="Bilan du bloc B. Le calcul se retient parce qu'il porte sur de vrais prix.")

    return d.save(dossier)
