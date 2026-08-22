# -*- coding: utf-8 -*-
"""B1 · Le bulletin de dix-sept heures
Bloc B « Défi 1 · Ce que l'avertissement annonce » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t1a`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Le bulletin de dix-sept heures",
        chapeau="Le mot a changé : ce n'est plus une veille, c'est un "
                "avertissement. De trois à cinq millimètres de glace, de "
                "vendredi soir à samedi matin. Marisol a maintenant quatre "
                "choses à tirer d'un bulletin qui dure quarante secondes.",
        duree='75 minutes')

    d.titre(notes="Première séance du Défi 1. Elle est entièrement d'écoute. Faire "
                  "écouter le bulletin de Gilles trois fois : la première sans rien "
                  "demander, la deuxième pour le phénomène et la région, la troisième "
                  "pour le moment et les chiffres. Ne pas donner la transcription avant "
                  "la troisième écoute.")

    d.objectifs([
        "tirer d'un bulletin le phénomène annoncé et la région visée ;",
        "relever le moment : quand ça commence, jusqu'à quand ça dure ;",
        "relever l'effet attendu, en chiffres ;",
        "comprendre que l'effet dure plus longtemps que le phénomène.",
    ], notes="Le quatrième objectif est celui qui fait décider juste, et c'est celui "
             "qu'on rate le plus souvent : la pluie s'arrête à huit heures, la glace "
             "reste au sol jusqu'au milieu de l'après-midi. Y consacrer la dernière "
             "demi-heure.")

    d.declencheur(
        'Écoute', "Écoutez quarante secondes de bulletin. Qu'avez-vous "
                  "retenu ?",
        pistes=[
            "Quel phénomène est annoncé ?",
            "Pour quelle région ?",
            "Pour quel moment : quand ça commence, jusqu'à quand ?",
            "Combien : de glace, de neige, de degrés ?",
        ],
        notes="Les quatre pistes sont les quatre morceaux du défi. Les écrire au tableau "
              "et faire remplir les cases à la deuxième écoute. Presque personne "
              "n'attrape les quatre du premier coup, et il faut le dire.")

    d.dialogue('Dialogue · 1 de 3', "L'avertissement est émis", [
        ("GILLES", "Environnement Canada a émis cet après-midi un "
                   "avertissement de pluie verglaçante pour le Bas-Saint-"
                   "Laurent, y compris le secteur de Rimouski.", True),
        ("MARISOL", "Un avertissement. Le mot a changé.", True),
        ("GILLES", "La pluie verglaçante débutera vendredi en soirée et se "
                   "poursuivra jusqu'à samedi matin.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire relever les deux bornes de temps : « débutera vendredi en soirée », "
             "« jusqu'à samedi matin ». Le bulletin en donne toujours deux, jamais une "
             "seule — c'est un repère fiable.")

    d.dialogue('Dialogue · 2 de 3', "Trois à cinq millimètres", [
        ("GILLES", "On attend de trois à cinq millimètres de glace sur les "
                   "surfaces exposées.", True),
        ("RÉJEAN", "Cinq millimètres de glace, ça casse des branches. Et ça "
                   "ferme des routes.", True),
        ("MARISOL", "« Deviendront », « sera » : il parle au futur du début à "
                    "la fin.", False),
    ], notes="La remarque de Marisol amène la grammaire de B2 sans l'annoncer. La laisser "
             "venir du groupe si possible : « à quel temps parle-t-il ? » suffit "
             "généralement.")

    d.dialogue('Dialogue · 3 de 3', "L'effet dure plus longtemps", [
        ("MARISOL", "Samedi après-midi, ça remonte ? Notre sortie est à "
                    "treize heures.", True),
        ("RÉJEAN", "Entre le moment où ça remonte et le moment où la glace "
                   "fond, il y a des heures. Le sol reste glacé longtemps "
                   "après.", True),
        ("MARISOL", "Alors les trottoirs seront encore dangereux à une heure "
                    "de l'après-midi.", False),
    ], notes="C'est le raisonnement central du module, et il n'est pas évident : le "
             "bulletin annonce un phénomène, pas un état du sol. Faire chercher d'autres "
             "exemples — la neige tombée la nuit, la chaleur accumulée dans un logement.")

    d.regle("Quatre morceaux, toujours les mêmes",
            "Le phénomène, la région, le moment, l'effet attendu en chiffres.",
            precision="Et un cinquième, que le bulletin ne dit pas : ce que cet "
                      "effet devient à l'heure exacte de votre activité.",
            notes="Diapositive à photographier. Elle sert de grille d'écoute pour tout le "
                  "bloc B et de plan de phrase pour l'exercice t1red de B4.")

    d.tableau('Deux durées', "Le phénomène et son effet",
              ['Le phénomène', "L'effet au sol"],
              [["Pluie verglaçante : vendredi soir à samedi matin", "Glace au sol toute la journée de samedi"],
               ["Bordée de neige : la nuit de jeudi", "Trottoirs non dégagés jusqu'à midi"],
               ["Chaleur extrême : de jeudi à dimanche", "Logements encore chauds lundi soir"],
               ["Crue printanière : deux semaines", "Sentiers boueux quinze jours de plus"]],
              cle=1,
              notes="Faire compléter la colonne de droite par le groupe. Chaque ligne "
                    "vient d'une saison différente : c'est ce qui justifie que le module "
                    "s'appelle « Quand la météo décide » et non « L'hiver ».")

    d.piege("S'arrêter au nom du phénomène",
            "Il y a un avertissement de pluie verglaçante. Bon.",
            "Avertissement de pluie verglaçante, chez nous, vendredi soir à samedi matin, trois à cinq millimètres.",
            "Le nom seul ne permet de décider de rien. Ce sont la région, le "
            "moment et le chiffre qui disent si ça vous touche.",
            notes="Faire l'expérience : demander au groupe de décider avec le nom seul, "
                  "puis avec les quatre morceaux. La différence se voit immédiatement.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le bulletin et la discussion.", [
        ("L'avertissement vise le Bas-Saint-Laurent, Rimouski compris.", "vrai"),
        ("La pluie verglaçante commencera samedi midi.", "faux — vendredi en soirée"),
        ("On attend de trois à cinq millimètres de glace.", "vrai"),
        ("Gilles parle au passé composé pendant tout le bulletin.", "faux — au futur"),
        ("Une amélioration est prévue samedi en après-midi.", "vrai"),
        ("La glace fondra tout de suite après la pluie.", "faux — le sol reste glacé des heures"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la phrase exacte du bulletin. La "
             "dernière est la plus importante des six : elle porte tout le Défi 2.")

    d.billet(
        "Écrivez les quatre morceaux d'un avis que vous avez déjà reçu ou entendu.",
        exemples=[
            "Le phénomène, la région, le moment, le chiffre.",
            "Si vous n'en avez pas en tête, prenez celui du bulletin de Gilles.",
        ],
        notes="Ramasser les billets : ils serviront en B4, où chacun doit dire si l'avis "
              "touche une activité donnée. Les billets incomplets sont les plus utiles à "
              "montrer — anonymement.")

    return d.save(dossier)
