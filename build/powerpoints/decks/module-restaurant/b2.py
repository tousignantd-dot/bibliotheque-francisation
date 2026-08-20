# -*- coding: utf-8 -*-
"""B2 · Je voudrais, pourriez-vous.
Bloc B · couleur ambre (écriture) · 90 min.
Source : mini-leçon `t1poli`, exercice `t1poli`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre='Je voudrais, pourriez-vous',
        chapeau="« Je veux la table d'hôte » est correct, mais sec. Quatre "
                "expressions suffisent à adoucir n'importe quelle demande — "
                "et elles s'apprennent telles quelles.",
        duree='90 minutes')

    d.titre(notes="Écrire « je veux » et « je voudrais » au tableau et demander laquelle "
                  "on emploierait avec un inconnu. Le groupe sent la différence.")

    d.objectifs([
        "employer je voudrais, j'aimerais, je prendrais ;",
        "employer pourriez-vous et auriez-vous ;",
        "employer est-ce que ce serait possible de ;",
        "reconnaître ces formes comme du conditionnel.",
    ])

    d.tableau('Analyse', "Quatre formes, quatre usages",
              ['La forme', 'Pour'],
              [["je voudrais, j'aimerais", "dire ce que je veux"],
               ["je prendrais", "commander un plat"],
               ["pourriez-vous", "demander une action"],
               ["auriez-vous", "demander si c'est disponible"]],
              cle=0,
              note="Et « est-ce que ce serait possible de… » pour ce qui dérange un peu.",
              notes="Diapo centrale. Faire recopier : ces cinq formes couvrent toutes les "
                    "demandes du module.")

    d.regle("Ce que ça change vraiment",
            "Une question au lieu d'un ordre.",
            precision="« Réchauffez-le » est un ordre. « Pourriez-vous le réchauffer ? » "
                      "est une question, à laquelle l'autre peut répondre. Le sens est le "
                      "même, la relation est différente — et c'est cela qu'on entend.",
            notes="Diapo à photographier. C'est l'explication la plus claire de la "
                  "politesse en français.")

    d.regle("D'où viennent ces formes",
            "Le conditionnel : la base du futur, les terminaisons de l'imparfait.",
            precision="vouloir › je voudrais · pouvoir › pourriez-vous · avoir › auriez-vous "
                      "· être › ce serait. Les terminaisons sont <b>-ais, -ais, -ait, "
                      "-ions, -iez, -aient</b>. À ce niveau, apprenez-les comme des "
                      "expressions.",
            notes="Si le groupe a fait le module précédent, c'est un rappel : la base est "
                  "celle du futur simple.")

    d.cartes('Cinq expressions à savoir', "Elles couvrent presque tout", [
        ("« Je voudrais… »",
         "Pour commander, pour demander un service. La plus employée de toutes."),
        ("« Je prendrais… »",
         "Spécifique au restaurant, très naturelle : « je prendrais le poulet »."),
        ("« Est-ce que je pourrais avoir… »",
         "Pour une petite chose : du sel, de l'eau, un couvert."),
        ("« Pourriez-vous… ? » et « Auriez-vous… ? »",
         "Pour une action, ou pour savoir si quelque chose existe."),
    ], notes="Faire répéter les cinq par le groupe, deux fois. Elles s'emploient bien "
             "au-delà du restaurant.")

    d.piege("Employer l'impératif tout seul",
            "Donnez-moi l'addition.",
            "Pourriez-vous m'apporter l'addition ?",
            "L'impératif seul sonne comme un ordre donné à quelqu'un qui vous sert. Le "
            "transformer en question ne coûte que trois mots — et change complètement la "
            "façon dont la demande est reçue.",
            notes="Faire jouer les deux versions par deux élèves. La différence est "
                  "immédiate et parlante.")

    d.pratique('Pratique · 1 de 2', "Adoucissez",
               "Récrivez la demande à la forme polie.", [
        ("Je veux la table d'hôte.", "Je voudrais la table d'hôte."),
        ("Je veux un café.", "J'aimerais un café."),
        ("Réchauffez-le.", "Pourriez-vous le réchauffer ?"),
        ("Avez-vous une table près de la fenêtre ?", "Auriez-vous une table près de la fenêtre ?"),
        ("Donnez-moi l'addition.", "Pourriez-vous m'apporter l'addition ?"),
        ("C'est possible de changer de table ?", "Est-ce que ce serait possible de changer de table ?"),
    ], corrige=True, cols=1,
       notes="Faire lire les deux colonnes à voix haute, l'une après l'autre. L'écart de "
             "ton s'entend.")

    d.pratique('Pratique · 2 de 2', "Quelle forme employer ?",
               "Choisissez la forme qui convient à la situation.", [
        ("Vous commandez un plat.", "je voudrais / je prendrais"),
        ("Vous voulez du sel.", "est-ce que je pourrais avoir"),
        ("Vous voulez qu'on réchauffe votre plat.", "est-ce que ce serait possible de"),
        ("Vous demandez si une table est libre.", "auriez-vous"),
        ("Vous demandez l'addition.", "pourriez-vous"),
    ], corrige=True, cols=1,
       notes="Plusieurs réponses sont acceptables. Ce qui compte est que la forme soit "
             "adoucie.")

    d.cartes("Et « s'il vous plaît »", "Trois choses à savoir", [
        ("Il s'ajoute à presque tout",
         "Au Québec, il est très fréquent, y compris dans des échanges brefs. Son absence "
         "se remarque plus qu'ailleurs."),
        ("Il se place à la fin",
         "« Je voudrais la table d'hôte, s'il vous plaît. » Rarement au début, sauf pour "
         "attirer l'attention."),
        ("Et « merci »",
         "À chaque service rendu, même petit : quand on apporte l'eau, le pain, "
         "l'addition. Trois ou quatre fois par repas, c'est normal."),
    ], notes="Ces conventions sont un point du programme — « respecter les conventions de "
             "la communication ». Elles se remarquent beaucoup quand elles manquent.")

    d.billet(
        "Écrivez six demandes polies pour un repas au restaurant.",
        exemples=[
            "Deux avec « je voudrais », deux avec « pourriez-vous », deux avec « est-ce que je pourrais avoir ».",
            "Ajoutez « s'il vous plaît » à chacune.",
        ],
        notes="Corriger individuellement. Ces phrases sont le brouillon du jeu de rôle de "
              "E1.")

    return d.save(dossier)
