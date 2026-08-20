# -*- coding: utf-8 -*-
"""B4 · Comparer deux modèles.
Bloc B · couleur acier · 55 min.
Source : exercices `t1compare` et `prMesure`, cartes mémoire.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='acier',
        titre='Comparer deux modèles',
        chapeau="Six questions font le tour de n'importe quel appareil. "
                "Posées dans le bon ordre, elles éliminent les mauvais choix "
                "avant qu'on parle de prix.",
        duree='55 minutes')

    d.titre(notes="Séance de synthèse du bloc B. Elle prépare directement le jeu de rôle "
                  "de E1.")

    d.objectifs([
        "poser les six questions dans l'ordre utile ;",
        "demander une comparaison quand un chiffre ne dit rien ;",
        "calculer le coût sur la durée de vie ;",
        "savoir quand un rabais oblige à décider vite.",
    ])

    d.tableau('Analyse', "Les six questions, dans l'ordre",
              ['Ordre', 'La question'],
              [["1", "Il fait quelles dimensions ?"],
               ["2", "Quelle est la capacité ?"],
               ["3", "Il consomme combien ?"],
               ["4", "Il est bruyant ?"]],
              cle=0,
              note="Puis : « quelle est la différence entre les deux ? » et « le spécial finit quand ? »",
              notes="Diapo centrale. L'ordre compte : les dimensions éliminent le plus de "
                    "modèles, le plus vite.")

    d.regle("Commencer par ce qui élimine",
            "Les dimensions d'abord. Le prix en dernier.",
            precision="Un appareil qui n'entre pas est éliminé quel que soit son prix. "
                      "Commencer par l'espace fait tomber la moitié du rayon en trente "
                      "secondes — et évite de s'attacher à un modèle impossible.",
            notes="C'est exactement ce que fait le vendeur dans le dialogue de A1. Le "
                  "rappeler.")

    d.cartes("Demander une comparaison", "Trois formules", [
        ("« C'est beaucoup ou peu ? »",
         "Pour un chiffre isolé : décibels, kilowattheures, litres. La question qui "
         "transforme un nombre en information."),
        ("« Ça change quoi pour nous ? »",
         "Pour une différence technique : un kilo de capacité, trente litres d'eau. Elle "
         "ramène le chiffre à la vie réelle."),
        ("« Sur combien d'années ? »",
         "Pour une économie annoncée. Un appareil se garde dix ans : le calcul doit porter "
         "sur cette durée, pas sur un mois."),
    ], notes="Ces trois formules valent bien au-delà des électroménagers : assurances, "
             "forfaits de téléphone, contrats de toutes sortes.")

    d.piege("Se laisser presser par un rabais",
            "Le spécial finit dimanche, il faut que je décide aujourd'hui.",
            "Le spécial finit dimanche. J'ai jusqu'à dimanche pour vérifier mes mesures.",
            "Un rabais qui se termine crée une vraie urgence, mais pas une urgence "
            "immédiate. Le temps qui reste est du temps pour mesurer, comparer et vérifier "
            "que l'appareil entre — trois choses qui coûtent bien plus cher qu'un rabais "
            "manqué.",
            notes="Point utile : plusieurs élèves achètent dans l'urgence et regrettent. "
                  "Nommer la pression sans dramatiser.")

    d.pratique('Pratique · 1 de 2', "Quelle question poser ?",
               "Vous voulez savoir ceci. Que demandez-vous ?", [
        ("Si l'appareil entre dans votre local", "Il fait quelles dimensions, porte ouverte ?"),
        ("Combien de linge entre dedans", "Quelle est la capacité ?"),
        ("Ce qu'il coûtera chaque mois", "Il consomme combien ?"),
        ("Si 52 décibels est acceptable", "Cinquante-deux, c'est beaucoup ou peu ?"),
        ("Ce qui justifie cent dollars d'écart", "Quelle est la différence entre les deux ?"),
    ], corrige=True, cols=1,
       notes="Accepter toutes les formulations qui obtiennent l'information.")

    d.pratique('Pratique · 2 de 2', "Le calcul sur la durée",
               "Le modèle A coûte 100 $ de plus mais consomme 30 L de moins par brassée.", [
        ("Trois brassées par semaine", "environ 90 L de moins par semaine"),
        ("Sur une année", "environ 4 700 L de moins"),
        ("Sur cinq ans", "l'économie dépasse largement 100 $"),
        ("Conclusion", "le modèle plus cher revient moins cher"),
    ], corrige=True, cols=1,
       notes="Faire le calcul au tableau, étape par étape. Le résultat surprend toujours.")

    d.vocabulaire('Vocabulaire', "Comparer", [
        ("la capacité", "Ce qui entre dans l'appareil."),
        ("la consommation", "L'eau ou l'électricité utilisée."),
        ("économe", "Qui consomme peu."),
        ("silencieux", "Qui fait peu de bruit."),
        ("un spécial", "Un rabais temporaire."),
    ], notes="Ces cinq mots sont ceux qu'un vendeur emploiera. Les reconnaître suffit à "
             "suivre la conversation.")

    d.billet(
        "Choisissez deux appareils réels et comparez-les en six lignes.",
        exemples=[
            "Une ligne par question du tableau.",
            "Terminez par votre choix et sa raison.",
        ],
        notes="Bilan du bloc B. Ce travail alimente directement le jeu de rôle de E1.")

    return d.save(dossier)
