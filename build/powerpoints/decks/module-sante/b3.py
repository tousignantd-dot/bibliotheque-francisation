# -*- coding: utf-8 -*-
"""B3 · Comprendre la posologie.
Bloc B « Défi 1 · À la pharmacie » · couleur acier (compréhension orale) · 75 min.
Source du module : exercice `co3`, dialogue `t1`, cartes « la posologie », « le traitement ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='acier',
        titre='Comprendre la posologie',
        chapeau="« Un comprimé deux fois par jour, avec de la nourriture, pendant sept "
                "jours, sans alcool. » Quatre consignes en une phrase, dites une seule "
                "fois.",
        duree='75 minutes')

    d.titre(notes="Cœur du défi 1. Apporter, si possible, deux vraies étiquettes de "
                  "pilulier vides : rien ne remplace l'objet.")

    d.objectifs([
        "comprendre les quatre consignes d'un traitement ;",
        "traduire une consigne en gestes concrets ;",
        "lire une étiquette de pilulier ;",
        "repérer ce qui est interdit pendant un traitement.",
    ])

    d.pratique('Pratique · 1 de 4', "La consigne et son explication",
               "Associez.", [
        ("Deux fois par jour.", "Le matin et le soir."),
        ("Avec de la nourriture.", "Pendant le repas."),
        ("Pendant sept jours.", "Toute la semaine."),
        ("Pas d'alcool.", "Ne buvez pas de vin ni de bière."),
    ], corrige=True,
       notes="C'est l'exercice 3 du défi 1. Faire remarquer que la colonne de droite dit "
             "la même chose en mots de tous les jours : c'est ça, comprendre.")

    d.tableau('Analyse', "Quatre questions à se poser devant un médicament",
              ['La question', 'Ce qu\'on cherche sur l\'étiquette'],
              [["Combien ?", "un comprimé, deux comprimés, une cuillère"],
               ["Quand ?", "matin, soir, aux repas, au coucher"],
               ["Combien de temps ?", "sept jours, dix jours, jusqu'à la fin de la boîte"],
               ["Quoi éviter ?", "l'alcool, le soleil, la conduite"]],
              cle=0,
              note="Si une des quatre réponses manque, on la demande avant de partir.",
              notes="Faire chercher ces quatre réponses sur les vraies étiquettes "
                    "apportées. Dix minutes, à deux.")

    d.regle('La règle du traitement complet',
            "On finit la boîte, même si on va mieux.",
            precision="Pour un antibiotique surtout : arrêter dès qu'on se sent mieux "
                      "laisse survivre les bactéries les plus résistantes, et l'infection "
                      "revient plus forte.",
            notes="Point de santé publique, pas seulement de langue. Le dire simplement "
                  "et le laisser à l'écran une minute entière.")

    d.cartes('Analyse', "Les mots de l'étiquette", [
        ("par voie orale",
         "Par la bouche. S'oppose à « en application locale », sur la peau."),
        ("au besoin",
         "Seulement si vous avez mal. Ce n'est pas obligatoire, contrairement à un "
         "antibiotique."),
        ("à jeun",
         "L'estomac vide, souvent une heure avant le repas."),
        ("jusqu'à la fin",
         "Toute la boîte, même si les symptômes ont disparu."),
    ], notes="Ces quatre expressions sont sur les étiquettes mais absentes des "
             "dialogues du module : ce sont elles qui bloquent en pharmacie.")

    d.pratique('Pratique · 2 de 4', "Qu'est-ce que ça veut dire ?",
               "Dites la consigne en mots de tous les jours.", [
        ("« Un comprimé aux douze heures. »", "un le matin, un le soir"),
        ("« Deux comprimés au besoin, maximum six par jour. »",
         "seulement si j'ai mal, et jamais plus de six"),
        ("« À prendre à jeun. »", "l'estomac vide, avant de manger"),
        ("« Jusqu'à la fin du traitement. »", "toute la boîte, même si je vais mieux"),
    ], corrige=True,
       notes="Refuser la traduction mot à mot : on veut le geste, pas le synonyme.")

    d.pratique('Pratique · 3 de 4', "Il manque une information",
               "Quelle question posez-vous au pharmacien ?", [
        ("« Prenez un comprimé par jour. »",
         "Pendant combien de temps ? / À quel moment de la journée ?"),
        ("« Deux fois par jour, pendant dix jours. »",
         "Combien de comprimés à la fois ? / Avec ou sans nourriture ?"),
        ("« Un comprimé le matin, pendant une semaine. »",
         "Est-ce que je peux boire de l'alcool ? / Le prendre en mangeant ?"),
    ], corrige=True,
       notes="Chaque consigne est incomplète exprès. C'est l'exercice qui fait le plus "
             "travailler : il faut savoir ce qu'on ignore.")

    d.piege("Le piège du « je vais mieux »",
            "Je me sens mieux, j'arrête les antibiotiques.",
            "Je me sens mieux, mais je finis la boîte.",
            "Se sentir mieux au troisième jour est normal et attendu. L'infection n'est "
            "pas finie pour autant : c'est la raison même pour laquelle le pharmacien "
            "dit « pendant sept jours » plutôt que « jusqu'à ce que ça aille mieux ».",
            notes="Erreur très répandue, dans toutes les langues. La nommer sans "
                  "moraliser : l'important est la phrase à retenir.")

    d.pratique('Pratique · 4 de 4', "Votre propre étiquette",
               "Prenez une boîte que vous avez chez vous, ou celle du groupe.", [
        ("Combien ?", "notez le nombre exact"),
        ("Quand ?", "notez les moments de la journée"),
        ("Combien de temps ?", "notez la durée"),
        ("Quoi éviter ?", "notez l'interdiction, s'il y en a une"),
    ], corrige=False,
       notes="Quinze minutes. Ceux qui n'ont rien apporté travaillent sur les étiquettes "
             "du groupe. Ne jamais commenter le médicament de quelqu'un devant la classe.")

    d.billet(
        "Écrivez les quatre consignes d'un médicament, dans vos mots.",
        exemples=[
            "Combien, quand, combien de temps, quoi éviter.",
            "Un vrai médicament, le vôtre ou celui d'un proche.",
        ],
        notes="Ramasser. Vérifier surtout la quatrième ligne : c'est celle qu'on oublie "
              "de lire sur les vraies boîtes.")

    return d.save(dossier)
