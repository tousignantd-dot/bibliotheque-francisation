# -*- coding: utf-8 -*-
"""D2 · Dites quoi faire, dites comment
Bloc D « Défi 3 · Ce qu'il faut apporter » · couleur ambre · 75 min.
Grammaire et écriture. Source : exercices `t3imper`, `t3ger` et `t3msg`,
et leurs mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="Dites quoi faire, dites comment",
        chapeau="L'impératif donne la consigne, le gérondif donne la manière. "
                "Séparément, ils font une phrase de plus ; ensemble, ils font "
                "un avis que personne ne rappelle pour faire préciser.",
        duree='75 minutes')

    d.titre(notes="Dernière séance avant « Je me lance ». Deux points de grammaire y "
                  "tiennent, et ils vont ensemble : l'impératif et le gérondif. "
                  "Commencer par rendre les billets de D1 et comparer avec la liste du "
                  "dialogue.")

    d.objectifs([
        "donner une consigne à l'impératif, deuxième personne du pluriel ;",
        "placer le pronom d'un verbe pronominal du bon côté ;",
        "former un gérondif et dire la manière avec ;",
        "écrire une consigne en trois morceaux : quoi, pourquoi, comment.",
    ])

    d.regle("L'impératif, c'est le présent sans le pronom",
            "Vous apportez devient : Apportez. Vous buvez devient : Buvez.",
            precision="Trois personnes seulement — tu, nous, vous — et devant un "
                      "groupe, c'est presque toujours vous. La négation entoure le "
                      "verbe : N'oubliez pas vos crampons. À l'oral on entend "
                      "« oubliez pas » ; dans un avis affiché, on garde le ne.",
            notes="Diapositive à photographier. Faire produire dix impératifs à partir "
                  "de dix phrases au présent, à l'oral, en chaîne. La forme s'installe "
                  "en cinq minutes ; c'est le reste qui prend du temps.")

    d.tableau('Analyse', "Ce qui bouge, et où",
              ["La forme", "Ce qu'elle devient"],
              [["être · avoir · savoir", "soyez · ayez · sachez"],
               ["vous vous habillez", "habillez-vous, avec un trait d'union"],
               ["au négatif", "ne vous découvrez pas la tête"],
               ["pour adoucir", "pensez à… · n'oubliez pas de… · prévoyez…"]],
              cle=1,
              note="Il faut prévoir deux litres d'eau par personne : l'impersonnel "
                   "adoucit encore, et dit la même chose.",
              notes="Diapositive à photographier. Les trois irréguliers reviennent tous "
                    "les trois dans un avis du Centre : soyez à midi quarante-cinq, "
                    "ayez vos crampons, sachez que la marche dure une heure.")

    d.pratique('Grammaire', "L'impératif des consignes",
               "Deuxième personne du pluriel : c'est un groupe, et Marisol le "
               "vouvoie.", [
        ("___ (apporter) des bottes à bonne semelle et vos crampons.", "Apportez"),
        ("___ (s'habiller) en trois couches plutôt qu'avec un gros manteau.", "Habillez-vous"),
        ("___ (ne pas oublier) votre gourde : deux litres par personne.", "N'oubliez pas"),
        ("___ (être) devant le Centre à midi quarante-cinq.", "Soyez"),
        ("___ (boire) toutes les vingt minutes, même sans avoir soif.", "Buvez"),
        ("___ (se couvrir) le visage : le vent est plus froid que le thermomètre.", "Couvrez-vous"),
    ], corrige=True, cols=2,
       notes="Ce sont les six items de l'exercice `t3imper`. Les deux verbes "
             "pronominaux sont ceux qui résistent : faire écrire le trait d'union au "
             "tableau, en gros.")

    d.regle("Le gérondif : en, plus le verbe en -ant",
            "Nous marchons devient : en marchant. Nous buvons devient : en buvant.",
            precision="On prend le « nous » du présent, on enlève -ons, on ajoute "
                      "-ant, et on met « en » devant. Trois exceptions seulement : en "
                      "étant, en ayant, en sachant.",
            notes="Diapositive à photographier. Faire fabriquer dix gérondifs à partir "
                  "de dix formes en « nous », à la chaîne. La règle est mécanique et "
                  "elle se retient en une séance.")

    d.cartes("À quoi sert le gérondif", "Deux emplois, et une règle qui les tient", [
        ("La manière — comment on s'y prend",
         "On évite un coup de chaleur en buvant avant d'avoir soif. On reste au chaud "
         "en s'habillant en trois couches. C'est l'emploi le plus utile du module."),
        ("La simultanéité — en même temps",
         "En marchant, regardez où vous mettez les pieds. Elle écoutait le bulletin en "
         "préparant le café. Les deux actions se déroulent ensemble."),
        ("Un seul sujet pour les deux verbes",
         "En sortant du Centre, vous verrez la promenade : c'est vous qui sortez et "
         "vous qui voyez. La promenade, elle, ne sort de nulle part."),
        ("À ne pas confondre avec « en train de »",
         "Il est en train de neiger décrit ce qui se passe maintenant. Les deux "
         "commencent par « en » et ne font pas le même travail."),
    ], notes="Diapositive à photographier. La troisième carte porte la faute classique "
             "du niveau, et elle est presque toujours écrite, jamais dite.")

    d.pratique('Grammaire', "Le gérondif : la manière et le moment",
               "Complétez avec « en » + le participe présent.", [
        ("On évite un coup de chaleur ___ (boire) avant d'avoir soif.", "en buvant"),
        ("Vous resterez au chaud ___ (s'habiller) en trois couches.", "en vous habillant"),
        ("___ (marcher), regardez toujours où vous mettez les pieds.", "En marchant"),
        ("Nous éviterons la chaleur ___ (partir) à neuf heures du matin.", "en partant"),
        ("___ (sortir) du Centre, vous verrez la promenade à votre droite.", "En sortant"),
        ("Elle a suivi le bulletin ___ (préparer) le café du groupe.", "en préparant"),
    ], corrige=True, cols=2,
       notes="Ce sont les six items de l'exercice `t3ger`. Le deuxième est le seul "
             "difficile : le pronom du verbe pronominal s'accorde avec le sujet — en "
             "vous habillant, et non en s'habillant.")

    d.regle("Trois morceaux, et personne ne rappelle",
            "La consigne, la raison, la manière — dans une seule phrase.",
            precision="Habillez-vous en trois couches, parce que nous entrerons au "
                      "café au milieu de la marche : vous resterez confortable en "
                      "enlevant une couche à l'intérieur. Quoi, pourquoi, comment.",
            notes="Diapositive à photographier et à laisser affichée pendant "
                  "l'écriture. C'est la structure de la production écrite de E2 : elle "
                  "s'installe ici ou nulle part.")

    d.pratique('Écriture', "La consigne, sa raison, sa manière",
               "Une phrase par consigne. Impératif, cause, gérondif.", [
        ("Crampons · trottoirs glacés à treize heures · les attacher avant de sortir.",
         "Apportez vos crampons, parce que les trottoirs seront encore glacés à treize heures : attachez-les en sortant du Centre."),
        ("Trois couches · on entre au café · enlever une couche à l'intérieur.",
         "Habillez-vous en trois couches, comme nous entrerons au café : vous resterez confortable en enlevant une couche à l'intérieur."),
        ("Deux litres d'eau · indice UV de neuf · boire toutes les vingt minutes.",
         "Apportez deux litres d'eau, puisque l'indice UV atteindra neuf : vous éviterez un coup de chaleur en buvant toutes les vingt minutes."),
        ("Arriver à midi quarante-cinq · l'autobus part à treize heures · dix minutes de plus pour le stationnement.",
         "Soyez au Centre à midi quarante-cinq, étant donné que l'autobus partira à treize heures précises : arrivez à temps en prévoyant dix minutes pour le stationnement."),
    ], corrige=True,
       notes="Ce sont les quatre situations de `t3msg`. Les corrigés ne sont pas les "
             "seuls justes : lire deux versions d'élèves avant d'afficher la "
             "correction. Deux lignes par consigne, jamais plus — le groupe lit debout, "
             "manteau sur le bras.")

    d.billet(
        "Écrivez la consigne d'équipement pour une sortie de juillet : quoi, pourquoi, comment.",
        exemples=[
            "Un impératif, un connecteur de cause, un gérondif. Deux lignes.",
            "Relisez-vous : la manière est ce qu'on oublie presque toujours.",
        ],
        notes="Ramasser les billets et les rendre en E2 : ils sont un morceau tout "
              "prêt de l'avis affiché.")

    return d.save(dossier)
