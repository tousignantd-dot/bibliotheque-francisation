# -*- coding: utf-8 -*-
"""A3 · Lire un menu.
Bloc A « Je découvre » · couleur teal · 75 min.
Source : mini-leçon `t1menu`, exercices `prFormule` et `t1menu`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-restaurant/images/')


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre='Lire un menu',
        chapeau="Quatre formules, quatre prix. L'écart entre elles peut "
                "atteindre le double pour un repas comparable — et tout tient "
                "dans quelques mots.",
        duree='75 minutes')

    d.titre(notes="Apporter deux ou trois menus de restaurants du quartier si possible. "
                  "Beaucoup en distribuent, et la séance prend tout son sens sur du vrai.")

    d.objectifs([
        "distinguer les quatre formules ;",
        "repérer la ligne qui dit ce qui est compris ;",
        "reconnaître les mots « servi avec », « au choix », « supplément » ;",
        "calculer si une formule vaut la peine.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qui est écrit sur cette ardoise, à votre avis ?",
        image=IMG + 'ardoise-menu.jpg',
        pistes=[
            "Pourquoi une ardoise plutôt qu'un papier imprimé ?",
            "Qu'est-ce qui change chaque jour, dans un restaurant ?",
            "Est-ce plus cher ou moins cher que la carte ?",
            "Où l'avez-vous déjà vue, une ardoise comme celle-là ?",
        ],
        notes="L'ardoise sert précisément parce que le contenu change : on l'efface. C'est "
              "ce qui explique que ce soit moins cher — la cuisine a acheté en fonction.")

    d.tableau('Analyse', "Les quatre formules",
              ['Formule', 'Ce que ça comprend'],
              [["La carte", "chaque plat à son prix"],
               ["Le menu du jour", "un choix limité, moins cher"],
               ["La table d'hôte", "trois services à prix fixe"],
               ["À la carte", "un plat seul"]],
              cle=2,
              note="« La carte » est le document ; « à la carte » est une façon de commander.",
              notes="Diapo centrale. La note lève la confusion la plus fréquente.")

    d.regle("La ligne qui dit ce qui est compris",
            "« Servi avec », « au choix », « inclus ».",
            precision="Deux plats au même prix ne comprennent pas la même chose. « Servi "
                      "avec soupe et café » vaut plusieurs dollars de plus que le même plat "
                      "seul. C'est la petite ligne sous le prix qu'il faut lire.",
            notes="Faire chercher cette ligne sur les menus apportés. Elle est presque "
                  "toujours en italique ou en plus petit.")

    d.cartes('Les mots à repérer', "Cinq mots qui changent le prix", [
        ("servi avec",
         "Ce qui vient avec le plat, sans supplément : une soupe, une salade, un café."),
        ("au choix",
         "Vous décidez : « dessert au choix », « accompagnement au choix »."),
        ("supplément",
         "Ça coûte plus cher. « Table d'hôte 32 $, supplément 4 $ pour le poisson » veut "
         "dire 36 $."),
        ("selon arrivage · prix du marché",
         "Ça change chaque jour, et il faut demander le prix. Fréquent pour le poisson et "
         "les fruits de mer."),
    ], notes="« Supplément » est le mot à ne pas manquer : il transforme un prix affiché en "
             "prix plus élevé, et il est toujours écrit petit.")

    d.regle("Le calcul de la table d'hôte",
            "Comparez le prix fixe au prix du plat seul.",
            precision="Table d'hôte à 32 $ contre plat seul à 24 $ : les huit dollars de "
                      "plus donnent une entrée et un dessert. Une soupe et un dessert "
                      "commandés séparément coûteraient douze ou quatorze dollars. La "
                      "formule est donc avantageuse — si on a faim.",
            notes="Faire le calcul au tableau. C'est de l'arithmétique simple, et elle "
                  "change les décisions.")

    d.piege("Confondre la carte et le menu",
            "Je vais prendre le menu. — Lequel ?",
            "En français d'ici, « le menu » désigne souvent une formule à prix fixe.",
            "Dans plusieurs pays, « le menu » est la liste complète. Ici, la liste complète "
            "s'appelle <b>la carte</b>, et « le menu » désigne une formule : menu du jour, "
            "menu du midi, menu à 25 $. La confusion est fréquente et sans gravité, mais "
            "elle fait perdre du temps.",
            notes="Point de vocabulaire utile pour tout le monde, y compris les "
                  "francophones venus d'ailleurs.")

    d.pratique('Pratique · 1 de 2', "Quelle formule ?",
               "Associez chaque situation à la formule qui convient.", [
        ("Vous avez très faim, le soir.", "la table d'hôte"),
        ("Vous n'avez pas très faim.", "à la carte"),
        ("Vous mangez le midi, en semaine.", "le menu du midi"),
        ("Vous voulez goûter le poisson frais du jour.", "le plat du jour"),
        ("Vous êtes pressé.", "le menu du jour — la cuisine est prête"),
    ], corrige=True, cols=1,
       notes="La dernière ligne est un vrai conseil pratique : un choix limité veut dire "
             "que les plats sont préparés d'avance.")

    d.pratique('Pratique · 2 de 2', "Ça coûte combien ?",
               "Calculez le prix réel.", [
        ("Table d'hôte 32 $, supplément 4 $ pour le poisson", "36 $"),
        ("Plat seul 24 $, soupe 6 $, dessert 8 $", "38 $ — la table d'hôte est plus avantageuse"),
        ("Menu du midi 18 $, café inclus", "18 $"),
        ("Plat du jour « prix du marché »", "il faut demander"),
    ], corrige=True, cols=1,
       notes="La deuxième ligne fait la démonstration du calcul de la table d'hôte. La "
             "faire au tableau.")

    d.billet(
        "Prenez un menu réel et relevez les quatre formules et leurs prix.",
        exemples=[
            "Un menu de restaurant du quartier, ou un menu trouvé en ligne.",
            "Calculez laquelle serait la plus avantageuse pour vous.",
        ],
        notes="Devoir concret. Les menus rapportés servent aussi aux séances suivantes.")

    return d.save(dossier)
