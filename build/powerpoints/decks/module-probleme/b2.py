# -*- coding: utf-8 -*-
"""B2 · Leur ou leurs.
Bloc B · couleur ambre (écriture) · 75 min.
Source : mini-leçon `t1leur`, exercices `t1leur` et `t1leurGN`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre='Leur ou leurs',
        chapeau="« Les voisins nettoient leur balcon » ou « leurs balcon » ? "
                "La réponse ne dépend pas du nombre de voisins. Elle dépend d'un "
                "seul mot : celui qui suit.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire écrite. Commencer par écrire les deux phrases du "
                  "chapeau au tableau et demander un vote à main levée. Garder le résultat "
                  "affiché : on y reviendra à la fin.")

    d.objectifs([
        "savoir ce qui décide entre leur et leurs — et ce n'est pas ce qu'on croit ;",
        "utiliser le test « son / ses » pour trancher en deux secondes ;",
        "distinguer le déterminant leur du pronom leur, qui ne prend jamais de s ;",
        "entendre la liaison qui distingue les deux à l'oral.",
    ])

    d.piege("L'erreur de départ",
            "Les voisins sont plusieurs, donc j'écris leurs.",
            "Les voisins nettoient leur balcon.",
            "Beaucoup d'élèves croient que le s de leurs marque le nombre de propriétaires. "
            "C'est faux, et c'est justement ce qui cause l'erreur. Avec leur, les "
            "propriétaires sont toujours plusieurs — ils, elles. Le s ne peut donc pas "
            "servir à ça : il serait toujours là.",
            notes="Commencer la séance par cette diapo, avant toute règle. Défaire la "
                  "fausse croyance d'abord ; installer la bonne règle ensuite.")

    d.regle('La règle',
            "C'est le nom placé juste après qui décide, et lui seul.",
            precision="Un seul objet, nom au singulier : leur. Plusieurs objets, nom au "
                      "pluriel : leurs. Le nombre de personnes qui possèdent ne change "
                      "jamais rien — elles sont plusieurs de toute façon.",
            notes="Écrire la règle au tableau et l'y laisser pour toute la séance.")

    d.tableau('Analyse', "Un seul objet possédé",
              ['Ce qu\'on a', 'Le mot', 'Pourquoi'],
              [["Plusieurs personnes", "Les voisins", "ils sont trois"],
               ["Le déterminant", "leur", "parce que le nom qui suit est singulier"],
               ["Un seul nom, singulier", "balcon", "un seul balcon pour eux tous"]],
              cle=1,
              note="La phrase complète : « Les voisins nettoient leur balcon. » Test rapide : "
                   "« Il nettoie son balcon » fonctionne au singulier, donc leur au pluriel.",
              notes="Faire dire la phrase complète à voix haute par le groupe.")

    d.tableau('Analyse', "Plusieurs objets possédés",
              ['Ce qu\'on a', 'Le mot', 'Pourquoi'],
              [["Plusieurs personnes", "Les voisins", "toujours plusieurs"],
               ["Le déterminant", "leurs", "parce que le nom qui suit est pluriel"],
               ["Un nom au pluriel", "enfants", "chaque famille a les siens"]],
              cle=1,
              note="La phrase complète : « Les voisins surveillent leurs enfants. » Test "
                   "rapide : « Il surveille ses enfants » fonctionne, donc leurs.",
              notes="Faire comparer les deux tableaux côte à côte : seule la troisième "
                    "ligne change, et c'est elle qui commande la deuxième.")

    d.regle('Le test qui ne se trompe jamais',
            "Mettez la phrase au singulier. Si vous dites son ou sa, écrivez leur. Si vous dites ses, écrivez leurs.",
            precision="Ils rangent leur vélo : « Il range son vélo » fonctionne, donc leur. "
                      "Ils rangent leurs vélos : « Il range ses vélos » fonctionne, donc leurs. "
                      "Ce test fonctionne dans tous les cas, sans exception.",
            notes="Le faire pratiquer oralement sur cinq phrases inventées par le groupe "
                  "avant de passer aux exercices écrits.")

    d.cartes('Trois choses à savoir en plus', "Ce qui n'est pas dans la règle", [
        ("Le genre ne change rien",
         "Leur s'écrit pareil au masculin et au féminin : leur logement, leur porte. "
         "La forme « leure » n'existe pas."),
        ("Le pronom leur ne prend jamais de s",
         "« Je leur ai téléphoné. » Ici, leur remplace « à eux, à elles » : c'est un "
         "pronom, il est devant un verbe, jamais de s."),
        ("Comment reconnaître le pronom",
         "Regardez ce qui suit. Devant un nom, c'est un déterminant, il peut prendre un s. "
         "Devant un verbe, c'est un pronom, jamais de s."),
        ("La liaison, seul indice à l'oral",
         "Devant une voyelle, le s de leurs se prononce [z] : leurs_enfants, "
         "leurs_appareils. « Leur ami » et « leurs_amis » ne se disent pas pareil."),
    ], notes="La troisième carte est la plus utile : elle donne un critère mécanique. "
             "Nom après = déterminant. Verbe après = pronom.")

    d.pratique('Pratique', 'Leur ou leurs ?',
               "Complétez chaque phrase. Utilisez le test son / ses.", [
        ("Les locataires du deuxième ont fait refaire ___ installation électrique.", "leur"),
        ("Les voisins du 3B se plaignent parce que ___ enfants marchent dans la graisse.", "leurs"),
        ("Mes voisins laissent ___ vélos dans le corridor.", "leurs"),
        ("Camille et Samir ont signé ___ bail au mois de juillet.", "leur"),
        ("Les propriétaires doivent respecter ___ obligations.", "leurs"),
        ("Ces deux familles trouvent ___ logement trop humide.", "leur"),
    ], corrige=True,
       notes="La dernière est la plus difficile : deux familles, mais chacune a un seul "
             "logement, et le nom est au singulier. Le test tranche : « elle trouve son "
             "logement trop humide ».")

    d.pratique('Pratique', 'Singulier ou pluriel ?',
               "Le nom qui suit leur ou leurs — au singulier ou au pluriel ?", [
        ("leur concierge", "SINGULIER"),
        ("leurs clés", "PLURIEL"),
        ("leur nouvelle adresse", "SINGULIER"),
        ("leurs anciens locataires", "PLURIEL"),
        ("leur porte d'entrée", "SINGULIER"),
        ("leurs plaintes", "PLURIEL"),
    ], corrige=True, cols=2,
       notes="Exercice de repérage pur : on ne demande pas de choisir, seulement de voir "
             "le nombre du nom. C'est l'étape que les élèves sautent quand ils se trompent.")

    d.piege('Le piège du pronom',
            "Je leurs ai téléphoné.",
            "Je leur ai téléphoné.",
            "Ici, leur n'est pas un déterminant mais un pronom : il remplace « à eux, à "
            "elles ». Le pronom leur ne prend jamais de s, quelle que soit la situation. "
            "Le repère est simple : il est placé devant un verbe, pas devant un nom.",
            notes="C'est l'erreur qui subsiste le plus longtemps, parce que la règle "
                  "« nom singulier / nom pluriel » ne s'y applique pas du tout.")

    d.pratique('Vérification', 'Cinq questions rapides',
               "Répondez sans regarder vos notes.", [
        ("Les voisins rangent ___ vélos au sous-sol.", "leurs — il range ses vélos"),
        ("Ces deux familles paient ___ loyer le premier du mois.", "leur — il paie son loyer"),
        ("Je ___ ai envoyé un courriel hier.", "leur — pronom devant un verbe"),
        ("Qu'est-ce qui décide entre leur et leurs ?", "le nom qui suit"),
        ("Dans « leurs appareils », le s de leurs…", "se prononce [z] — il y a liaison"),
    ], corrige=True,
       notes="Revenir au vote du début de séance : combien de personnes avaient choisi "
             "« leurs balcon » ? La question a maintenant une réponse justifiée.")

    d.billet(
        "Écrivez deux phrases sur vos voisins : une avec leur, une avec leurs.",
        exemples=[
            "Soulignez le nom qui suit et indiquez s'il est au singulier ou au pluriel.",
            "Exemple : « Mes voisins ont repeint leur cuisine. » — cuisine, singulier.",
        ],
        notes="Corriger les billets en dehors du cours et rendre à la séance suivante : "
              "cette notion demande une rétroaction individuelle.")

    return d.save(dossier)
