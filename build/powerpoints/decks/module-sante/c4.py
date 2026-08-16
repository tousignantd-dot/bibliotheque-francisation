# -*- coding: utf-8 -*-
"""C4 · Un peu, assez, très, trop.
Bloc C « Défi 2 · La langue » · couleur ambre (écriture) · 60 min.
Source du module : exercice `l4` et sa mini-leçon « Un peu / assez / très / trop ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre='Un peu, assez, très, trop',
        chapeau="Quatre mots pour doser ce qu'on ressent. Le quatrième n'est pas le plus "
                "fort des quatre : c'est un signal d'alarme.",
        duree='60 minutes')

    d.titre(notes="Séance courte mais dense. L'enjeu n'est pas grammatical : dire « trop »"
                  " à la place de « très » change ce que le médecin va faire.")

    d.objectifs([
        "placer l'adverbe devant le mot qu'il dose ;",
        "distinguer les trois crans : un peu, assez, très ;",
        "employer « trop » pour signaler un excès ;",
        "décrire une douleur avec la bonne intensité.",
    ])

    d.regle('La règle',
            "L'adverbe se place devant le mot qu'il dose.",
            precision="« Je suis très fatiguée. » « J'ai un peu mal. » Jamais après : "
                      "« fatiguée très » ne se dit pas.",
            notes="Règle simple, à installer vite pour passer au vrai sujet : la "
                  "différence entre très et trop.")

    d.tableau('Analyse', "Les quatre crans",
              ['L\'adverbe', 'Ce qu\'il dit'],
              [["un peu", "c'est léger — j'ai un peu mal à la tête"],
               ["assez", "c'est réel, sans être fort — ce médicament est assez efficace"],
               ["très", "c'est fort — je suis très fatiguée"],
               ["trop", "il y en a plus qu'il ne faut — je suis trop fatiguée pour "
                        "travailler"]],
              cle=0,
              note="Les trois premiers décrivent. Le quatrième alerte.",
              notes="Faire placer les quatre sur une ligne au tableau, avec « trop » "
                    "hors de la ligne, au-dessus. La géométrie fait comprendre.")

    d.pratique('Pratique · 1 de 4', "Complétez selon l'indice",
               "un peu · assez · très · trop.", [
        ("Je suis ___ fatiguée. (++)", "très"),
        ("J'ai ___ mal à la tête. (+)", "un peu"),
        ("J'ai ___ de travail, je suis épuisée. (excès)", "trop"),
        ("Ce médicament est ___ efficace. (bien)", "assez"),
        ("Le médecin est ___ gentil. (++)", "très"),
    ], corrige=True,
       notes="C'est l'exercice 4 du défi 2. Les indices entre parenthèses sont ceux du "
             "module : les garder, ils évitent de deviner.")

    d.piege("Le piège du trop qui veut dire très",
            "Ce médecin est trop gentil !",
            "Ce médecin est très gentil !",
            "À l'oral, entre amis, « trop » sert parfois d'intensif. Chez le médecin, il "
            "garde son sens strict : plus qu'il ne faut. « Trop gentil » y voudrait dire "
            "que sa gentillesse pose problème.",
            notes="Ne pas condamner l'usage familier : le situer. C'est une question de "
                  "registre, et les élèves l'entendent partout.")

    d.piege("Le piège de l'accumulation",
            "Je suis un peu très fatiguée.",
            "Je suis très fatiguée.",
            "Un seul adverbe d'intensité à la fois. On choisit son cran, on ne les "
            "additionne pas.",
            notes="Vient souvent d'une hésitation : l'élève commence par « un peu » par "
                  "politesse, puis corrige. Lui dire de choisir avant de parler.")

    d.pratique('Pratique · 2 de 4', "Très ou trop ?",
               "Le sens change complètement.", [
        ("Je suis ___ fatiguée, mais je vais travailler.", "très — c'est fort, ça passe"),
        ("Je suis ___ fatiguée pour conduire.", "trop — ça dépasse, je ne conduis pas"),
        ("Ce sirop est ___ sucré, j'aime ça.", "très"),
        ("Ce comprimé est ___ gros, je ne peux pas l'avaler.", "trop"),
    ], corrige=True,
       notes="Le test : est-ce que ça empêche quelque chose ? Si oui, c'est « trop ». "
             "L'écrire au tableau.")

    d.pratique('Pratique · 3 de 4', "Chez le médecin, dosez juste",
               "Décrivez la douleur avec le bon cran.", [
        ("Vous dormez mal mais vous travaillez normalement.",
         "Je suis un peu fatigué. / Je dors assez mal."),
        ("Vous ne pouvez plus monter l'escalier sans souffler.",
         "Je suis trop essoufflé pour monter l'escalier."),
        ("Vous avez mal, mais vous prenez seulement un comprimé le soir.",
         "J'ai un peu mal, surtout le soir."),
        ("La douleur vous réveille toutes les nuits.",
         "J'ai très mal la nuit — ça me réveille."),
    ], corrige=True,
       notes="Insister : exagérer fait perdre du temps, minimiser fait passer à côté. "
             "Le bon cran est une compétence de santé, pas seulement de langue.")

    d.pratique('Pratique · 4 de 4', "Votre échelle à vous",
               "Quatre phrases vraies, une par cran.", [
        ("un peu", "quelque chose de léger, aujourd'hui"),
        ("assez", "quelque chose de réel"),
        ("très", "quelque chose de fort"),
        ("trop", "quelque chose qui vous empêche de faire quelque chose"),
    ], corrige=False,
       notes="Dix minutes. La quatrième est la plus difficile à écrire : elle demande "
             "de nommer ce qui est empêché.")

    d.billet(
        "Écrivez comment vous vous sentez aujourd'hui, avec un des quatre adverbes.",
        exemples=[
            "Une seule phrase, le cran juste.",
            "Si vous écrivez « trop », dites ce que ça vous empêche de faire.",
        ],
        notes="Ramasser. Lire discrètement : un « trop » sincère mérite parfois un mot "
              "en privé après le cours.")

    return d.save(dossier)
