# -*- coding: utf-8 -*-
"""A2 · Le son [s] et le son [z].
Bloc A « Je découvre » · couleur indigo · 75 min.
Source : exercice `prSons`, mini-leçon `prSons`.

La séance de phonétique du module. Le programme du niveau 2 demande de
discriminer /f/, /s/, /v/ et /z/ ; le rayon des fruits et légumes en est
plein — cerise, raisin, framboise, saucisse — et c'est là qu'on l'exerce.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-panier/images/')


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Le son [s] et le son [z]",
        chapeau="Une seule lettre, deux sons. Ce qui décide, c'est ce qu'il "
                "y a autour d'elle.",
        duree='75 minutes')

    d.titre(notes="Séance d'oreille avant tout. Parler peu, faire écouter beaucoup. "
                  "Prévoir que certains élèves n'entendront pas la différence au premier "
                  "cours : c'est normal, et elle vient avec la répétition.")

    d.objectifs([
        "entendre la différence entre [s] et [z] ;",
        "savoir quand la lettre s se dit [z] ;",
        "prononcer les mots du rayon des fruits ;",
        "faire la liaison de « des » et « les » devant une voyelle.",
    ])

    d.declencheur(
        'Observation', "Comment dit-on ces mots ?",
        image=IMG + 'balance-fruits.jpg',
        pistes=[
            "Que fait cette machine ?",
            "Quels fruits achetez-vous le plus souvent ?",
            "Écoutez : cerise, saucisse. Est-ce le même son ?",
            "Où est la différence, à votre avis ?",
        ],
        notes="Dire les deux mots plusieurs fois, lentement, sans expliquer. Laisser le "
              "groupe chercher. La règle vient après l'oreille, jamais avant.")

    d.tableau('Analyse', "Une lettre, deux sons",
              ['Ce qui est écrit', 'Ce qu\'on entend'],
              [["une ceri<b>s</b>e", "[z] — le s est doux"],
               ["du rai<b>s</b>in", "[z] — le s est doux"],
               ["une sauci<b>ss</b>e", "[s] — le s est dur"],
               ["<b>s</b>alade", "[s] — le s est dur"]],
              cle=2,
              note="Le s entre deux voyelles se dit [z]. Partout ailleurs, il est dur.",
              notes="Diapositive à photographier. Faire lire à voix haute les quatre mots "
                    "par chaque élève, une fois, sans correction serrée.")

    d.regle("Le s entre deux voyelles",
            "Une voyelle avant, une voyelle après : le s se dit [z].",
            precision="ceri<b>s</b>e, rai<b>s</b>in, framboi<b>s</b>e. Pour garder le son "
                      "dur entre deux voyelles, le français écrit <b>deux s</b> : "
                      "sauci<b>ss</b>e, de<b>ss</b>ert, poi<b>ss</b>on.",
            notes="Diapositive à photographier. Écrire au tableau « poisson » et « poison » "
                  "et expliquer pourquoi le deuxième s compte : à l'épicerie, on parle "
                  "toujours de poisson.")

    d.cartes("Trois positions, deux sons", "Où est le s ?", [
        ("Entre deux voyelles : [z]", "une cerise, du raisin, une framboise"),
        ("Deux s collés : [s]", "une saucisse, un dessert, un poisson"),
        ("Au début du mot : [s]", "salade, savon, sac, spécial"),
    ], cols=3, notes="Diapositive à photographier. Faire ajouter par le groupe deux mots "
                     "de leur langue de cuisine, et les classer dans la bonne colonne.")

    d.pratique('Écoute', "[s] ou [z] ?",
               "Écoutez chaque mot et écrivez le son que vous entendez.", [
        ("un dessert", "[s]"),
        ("une cerise", "[z]"),
        ("de la saucisse", "[s]"),
        ("du raisin", "[z]"),
        ("de la salade", "[s]"),
        ("une framboise", "[z]"),
    ], corrige=True, cols=2,
       notes="Dire chaque mot trois fois, dans le désordre. Ne pas montrer l'écriture "
             "pendant l'écoute : c'est l'oreille qui travaille.")

    d.piege('Le piège', "de[s] oranges", "de[z] oranges",
            "Devant une voyelle, le s de « des », « les » et « deux » se prononce [z] et "
            "se colle au mot suivant : « de-z-oranges », « le-z-œufs », « deu-z-œufs ». "
            "C'est la liaison, et elle est obligatoire.",
            notes="Faire répéter les trois exemples en chœur, lentement, puis à vitesse "
                  "normale. C'est la difficulté qui reste le plus longtemps.")

    d.pratique('Pratique · à deux', "Le marché des sons",
               "Deux par deux, chacun son tour.", [
        ("Étape 1", "Choisissez cinq fruits ou légumes que vous achetez."),
        ("Étape 2", "Dites-les à votre voisin, un par un."),
        ("Étape 3", "Votre voisin dit [s] ou [z] pour chaque mot."),
        ("Étape 4", "Changez de rôle."),
    ], cols=1,
       notes="Vingt minutes. Circuler et redire soi-même le mot quand les deux élèves "
             "hésitent : ils ont besoin d'un modèle, pas d'un arbitre.")

    d.billet(
        "Dites ces trois phrases à voix haute, trois fois chacune.",
        exemples=[
            "Je prends des cerises.",
            "Je prends de la salade.",
            "Les framboises sont en spécial.",
        ],
        notes="Devoir d'oreille. Rappeler que la mini-leçon en ligne fait entendre chaque "
              "phrase autant de fois qu'on veut.")

    return d.save(dossier)
