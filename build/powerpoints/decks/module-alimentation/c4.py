# -*- coding: utf-8 -*-
"""C4 · Je n'en prends pas aujourd'hui.
Bloc C · couleur acier · 55 min.
Source : dialogue `t2b`, exercice `t2b`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='acier',
        titre="Je n'en prends pas aujourd'hui",
        chapeau="Le produit qu'on cherche n'est pas là. Faut-il prendre autre "
                "chose, revenir, ou s'en passer ? Une décision de deux "
                "secondes qui coûte ou qui économise.",
        duree='55 minutes')

    d.titre(notes="Séance courte. Elle clôt le bloc C sur une compétence de décision autant "
                  "que de langue.")

    d.objectifs([
        "demander si un produit reviendra, et quand ;",
        "comparer deux formats avant de choisir ;",
        "dire qu'on ne prend pas quelque chose, et pourquoi ;",
        "demander où se trouve un autre rayon dans la foulée.",
    ])

    d.declencheur(
        'Mise en situation', "Le produit que vous cherchez n'est pas sur la tablette. Que faites-vous ?",
        pistes=[
            "Vous prenez un autre format ? Une autre marque ?",
            "Vous demandez s'il en reste en arrière ?",
            "Vous revenez un autre jour ?",
            "Comment savoir si le petit format est un bon achat ?",
        ],
        notes="Cinq minutes. La deuxième piste surprend souvent : oui, on peut demander, "
              "et il y en a fréquemment en réserve.")

    d.dialogue('Dialogue · 1 de 2', "Il n'y en a plus", [
        ("SIMON", "Vous avez trouvé tout ce que vous cherchiez ?", False),
        ("FARIDA", "Presque. Je voulais du riz basmati, mais il n'y en a plus.", True),
        ("SIMON", "Il en reste peut-être en arrière. Quel format vous voulez ?", True),
        ("FARIDA", "Le grand sac, celui de huit kilos.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="« Il en reste peut-être en arrière » : à faire remarquer. Demander est "
             "souvent payant, et personne n'y pense.")

    d.dialogue('Dialogue · 2 de 2', "Choisir de ne pas prendre", [
        ("SIMON", "Ah, celui-là, on n'en a plus jusqu'à jeudi. Il en reste des petits, par exemple.", True),
        ("FARIDA", "Je vais attendre jeudi. Je n'en prends pas de petits, ça revient plus cher.", True),
        ("SIMON", "Vous avez raison. Le grand format coûte presque moitié moins au kilo.", True),
        ("FARIDA", "Et le savon à vaisselle, il est dans quelle allée ?", False),
    ], notes="La décision de Farida est le cœur de la séance : ne pas acheter est aussi une "
             "décision, et elle se justifie par le prix au kilo vu en A3.")

    d.tableau('Analyse', "Quatre façons de dire qu'il n'y en a plus",
              ['La phrase', 'Ce qu\'elle laisse entendre'],
              [["Il n'y en a plus.", "épuisé, sans plus de précision"],
               ["On n'en a plus jusqu'à jeudi.", "ça revient — une date"],
               ["Il en reste peut-être en arrière.", "ça vaut la peine d'attendre deux minutes"],
               ["Il en reste des petits.", "un autre format existe"]],
              cle=2,
              note="Les trois dernières ouvrent une possibilité. La première ferme.",
              notes="Diapo centrale. Faire remarquer que la réponse dépend beaucoup de la "
                    "question posée.")

    d.regle('Demander la date de retour',
            "« Ça revient quand ? » — trois mots.",
            precision="Un produit épuisé revient presque toujours, et la personne au "
                      "comptoir connaît le jour de livraison. Le savoir permet de décider : "
                      "attendre, ou prendre autre chose.",
            notes="Faire répéter la question par le groupe. Elle est courte et très utile.")

    d.piege('Prendre plusieurs petits formats',
            "Il n'y a plus de grand sac, je vais prendre quatre petits.",
            "Le grand format coûte presque moitié moins au kilo. J'attends jeudi.",
            "Quatre petits sacs de deux kilos coûtent souvent le double d'un grand sac de "
            "huit. C'est le prix au kilo qui tranche — et il est écrit sur l'étiquette de "
            "la tablette.",
            notes="Faire le calcul avec des chiffres réels au tableau. C'est de "
                  "l'arithmétique simple qui économise chaque mois.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Il reste du riz basmati en grand format.", "faux — il n'y en a plus"),
        ("Le grand format revient jeudi.", "vrai"),
        ("Farida décide de prendre plusieurs petits sacs.", "faux — elle attend"),
        ("Le grand format coûte moins cher au kilo.", "vrai"),
        ("Le savon à vaisselle est dans l'allée huit.", "vrai"),
        ("Il n'y a aucun spécial cette semaine.", "faux — il y en a un"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte.")

    d.cartes("Enchaîner une deuxième question", "Le réflexe utile", [
        ("La personne est déjà là",
         "« Et le savon à vaisselle, il est dans quelle allée ? » Farida enchaîne sans "
         "transition : c'est du temps gagné."),
        ("Une question de plus ne dérange pas",
         "Un commis répond à des dizaines de questions par jour. Deux d'affilée ne "
         "changent rien pour lui."),
        ("Préparer sa deuxième question",
         "Avant d'aborder quelqu'un, pensez à ce que vous chercherez ensuite. Vous "
         "économiserez un deuxième tour du magasin."),
    ], notes="Conseil pratique simple, rarement donné. Il change la façon dont les élèves "
             "abordent un magasin.")

    d.billet(
        "Racontez en quatre phrases une fois où vous n'avez pas trouvé un produit.",
        exemples=[
            "Qu'avez-vous fait ? Avez-vous demandé ? Qu'auriez-vous pu faire ?",
            "Employez « en » au moins deux fois.",
        ],
        notes="Bilan du bloc C. Les récits alimentent le jeu de rôle de E1.")

    return d.save(dossier)
