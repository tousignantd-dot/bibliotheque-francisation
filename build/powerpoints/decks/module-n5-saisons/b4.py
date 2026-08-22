# -*- coding: utf-8 -*-
"""B4 · Est-ce que ça nous touche ?
Bloc B « Défi 1 · Ce que l'avertissement annonce » · couleur ambre · 75 min.
Source : exercices `t1qui` et `t1red`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="Est-ce que ça nous touche ?",
        chapeau="Un avertissement pour la Gaspésie ne concerne pas Rimouski. "
                "Un avis en vigueur vendredi soir ne touche pas une sortie du "
                "samedi après-midi — sauf par ce qu'il laisse au sol. Trois "
                "filtres, dans l'ordre, et la moitié des annulations tombent.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du Défi 1. Elle referme l'écoute et prépare la "
                  "décision. Ouvrir en affichant une carte du Québec avec les régions de "
                  "prévision et en faisant trouver la nôtre : beaucoup d'élèves ne "
                  "savent pas dans quelle région ils habitent, au sens de la météo.")

    d.objectifs([
        "reconnaître sa région de prévision et la guetter dans le bulletin ;",
        "comparer le créneau de l'avis à celui de son activité ;",
        "juger ce que l'effet devient à l'heure exacte de l'activité ;",
        "redire un avis en une phrase, avec ses quatre morceaux.",
    ], notes="Le quatrième objectif est une production, et c'est la première du module : "
             "on passe de comprendre à redire. Y garder la dernière demi-heure, sans "
             "l'écourter.")

    d.declencheur(
        'Décision', "La sortie est samedi de 13 h à 16 h, à Rimouski. "
                    "Lesquels de ces avis vous concernent ?",
        pistes=[
            "Avertissement de tempête hivernale pour la Gaspésie, samedi après-midi.",
            "Avertissement de poudrerie pour le Bas-Saint-Laurent, samedi midi à 18 h.",
            "Bulletin spécial pour le Bas-Saint-Laurent, mardi prochain.",
            "Avertissement de pluie abondante pour le Bas-Saint-Laurent, levé jeudi midi.",
        ],
        notes="Quatre cas, deux réponses « oui » et deux « non ». Faire justifier chaque "
              "réponse par le filtre qui tranche : la région, le moment, ou le fait que "
              "l'avis a été levé.")

    d.regle("Trois filtres, dans cet ordre",
            "La région, puis le moment, puis l'effet qui reste au sol.",
            precision="Et ce qui n'est pas un filtre : un titre alarmant, la "
                      "télévision nationale, trois personnes du groupe qui téléphonent.",
            notes="Diapositive à photographier. La précision compte autant que la règle : "
                  "l'inquiétude des autres n'est pas une information, et c'est elle qui "
                  "fait annuler pour rien.")

    d.tableau('Trois filtres', "Ce que chacun élimine",
              ['Filtre', "Ce qu'il demande", "Ce qu'il élimine"],
              [["La région", "Est-ce que le Bas-Saint-Laurent est nommé ?", "Les avis de Gaspésie, de l'Estrie"],
               ["Le moment", "L'avis couvre-t-il samedi 13 h à 16 h ?", "Les avis de mardi prochain"],
               ["L'effet", "Que reste-t-il au sol à 13 h ?", "Rien — c'est celui qui ajoute"],
               ["Aucun", "L'avis a-t-il été levé ?", "Tout, s'il l'a été"]],
              note="Le troisième filtre n'élimine pas : il rattrape ce que les deux premiers laissent passer.",
              notes="La dernière ligne surprend toujours. Un avis levé la veille au soir "
                    "n'a plus d'existence — et personne ne pense à vérifier.")

    d.pratique('Tri', "Est-ce que ça touche la sortie ?",
               "Sortie à Rimouski, samedi de 13 h à 16 h. Répondez oui ou non, "
               "et dites quel filtre tranche.", [
        ("Avertissement de pluie verglaçante, Bas-Saint-Laurent, vendredi soir à samedi matin.", "oui — l'effet reste au sol"),
        ("Avertissement de tempête hivernale, Gaspésie, samedi après-midi.", "non — la région"),
        ("Avertissement de poudrerie, Bas-Saint-Laurent, samedi de midi à 18 h.", "oui — région et moment"),
        ("Bulletin météorologique spécial, Bas-Saint-Laurent, mardi prochain.", "non — le moment"),
        ("Avertissement de froid extrême, Bas-Saint-Laurent, samedi toute la journée.", "oui — région et moment"),
        ("Avertissement de pluie abondante, Bas-Saint-Laurent, levé jeudi midi.", "non — l'avis est levé"),
    ], corrige=True,
       notes="Ce sont six des huit énoncés de l'exercice t1qui du module. Exiger le "
             "filtre autant que la réponse : c'est le raisonnement qu'on évalue, pas le "
             "oui ou le non.")

    d.regle("Redire un avis en une phrase",
            "Le phénomène, la région, le moment, l'effet — dans cet ordre, "
            "et en une seule phrase.",
            precision="Votre conclusion vient après les quatre morceaux, jamais "
                      "avant : l'autre doit pouvoir juger avec les mêmes faits que vous.",
            notes="Écrire la phrase modèle au tableau et la laisser pendant tout "
                  "l'exercice suivant : « Il y a un avertissement de pluie verglaçante "
                  "pour notre région, de vendredi soir à samedi matin ; on attend jusqu'à "
                  "cinq millimètres de glace sur les trottoirs. »")

    d.piege("Commencer par la conclusion",
            "Je pense qu'il faut annuler, parce qu'il va faire mauvais.",
            "Il y a un avertissement de pluie verglaçante chez nous, de vendredi soir à samedi matin, avec jusqu'à cinq millimètres de glace — donc je pense qu'on devrait reporter.",
            "Si vous commencez par la conclusion, l'autre discutera la conclusion "
            "au lieu d'écouter les faits. Et « il va faire mauvais » n'est pas un fait.",
            notes="Faire l'expérience à deux : un élève annonce d'abord la conclusion, "
                  "puis les faits, et son partenaire dit laquelle des deux versions l'a "
                  "convaincu. Le résultat est toujours le même.")

    d.pratique('Écriture', "Redites l'avis en une phrase",
               "Quatre morceaux donnés ; écrivez la phrase que vous diriez à "
               "quelqu'un qui n'a rien entendu.", [
        ("Pluie verglaçante · Bas-Saint-Laurent · vendredi soir à samedi matin · 3 à 5 mm de glace.", "une phrase, quatre morceaux, dans l'ordre"),
        ("Tempête hivernale · Bas-Saint-Laurent · nuit de jeudi à vendredi · 25 à 35 cm de neige.", "idem, avec la quantité en chiffres"),
        ("Froid extrême · Bas-Saint-Laurent · samedi toute la journée · refroidissement éolien de −38.", "idem, avec les deux températures"),
        ("Chaleur extrême · Bas-Saint-Laurent · de jeudi à dimanche · 32 degrés, indice UV de 9.", "idem, avec les deux chiffres"),
    ],
       notes="Ce sont les quatre items de l'exercice t1red du module ; ils n'ont pas de "
             "réponse unique et c'est voulu. Faire lire deux ou trois phrases à voix "
             "haute et faire dire au groupe si les quatre morceaux y sont.")

    d.billet(
        "Écrivez la phrase que vous diriez à un voisin qui part en auto demain matin.",
        exemples=[
            "Prenez l'avis de votre choix parmi les quatre de l'exercice.",
            "Les quatre morceaux, une seule phrase, et votre conseil à la fin.",
        ],
        notes="Ramasser les billets : c'est le premier vrai brouillon du jeu de rôle de "
              "E1. Les rendre annotés avant le bloc E, pas après.")

    return d.save(dossier)
