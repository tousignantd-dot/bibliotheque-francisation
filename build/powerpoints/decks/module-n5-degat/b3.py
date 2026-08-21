# -*- coding: utf-8 -*-
"""B3 · En rentrant, en ouvrant : le gérondif.
Bloc B « Défi 1 · Le constat » · couleur ambre · 75 min. Grammaire.
Source : exercice `t1ger`, mini-leçon `t1ger`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="En rentrant, en ouvrant : le gérondif",
        chapeau="Une forme courte pour dire deux choses à la fois. Le "
                "programme du niveau 5 l'attend explicitement — et elle rend "
                "un récit deux fois plus fluide.",
        duree='75 minutes')

    d.titre(notes="Séance plus légère que B2, et bienvenue après elle. Le gérondif "
                  "s'installe vite : une règle de formation, deux emplois, une "
                  "contrainte.")

    d.objectifs([
        "former le gérondif à partir de la forme « nous » du présent ;",
        "connaître les trois formes irrégulières ;",
        "employer le gérondif pour la simultanéité et pour la manière ;",
        "respecter la règle du sujet unique.",
    ])

    d.regle("en + le radical de « nous » + -ant",
            "nous rentrons donne en rentrant. Une seule règle de formation.",
            precision="On prend le verbe à « nous » au présent, on enlève -ons, on ajoute "
                      "-ant, et on met « en » devant. La forme est invariable : elle ne "
                      "s'accorde jamais, ni en genre ni en nombre. En rentrant, qu'on "
                      "soit un, deux ou dix.",
            notes="Faire produire cinq gérondifs au tableau à partir de verbes donnés par "
                  "le groupe. La règle du « nous » se vérifie tout de suite.")

    d.cartes("Les trois irrégulières", "Et ce sont les seules", [
        ("être, en étant",
         "« En étant sur place, j'ai pu ouvrir aux ouvriers. »"),
        ("avoir, en ayant",
         "« En ayant les photos, la réclamation a été acceptée. »"),
        ("savoir, en sachant",
         "« En sachant que l'assureur passerait, je n'ai rien jeté. »"),
        ("Toutes les autres suivent la règle",
         "nous prenons, en prenant · nous ouvrons, en ouvrant · nous voyons, en voyant."),
    ], notes="Les faire apprendre ensemble, en trois mots : étant, ayant, sachant. "
             "C'est plus court qu'une liste de verbes.")

    d.tableau('Deux emplois, pas un de plus', "À quoi il sert",
              ['L\'emploi', 'Un exemple du module'],
              [["en même temps",
                "En rentrant du travail, j'ai vu que la tache avait doublé."],
               ["la manière ou le moyen",
                "Elle a limité les dommages en plaçant une chaudière."],
               ["ce qu'il remplace",
                "« quand je suis rentrée » ou « parce qu'elle a placé »"],
               ["ce qu'il fait gagner",
                "deux ou trois mots, et beaucoup de fluidité"]],
              cle=0,
              note="Le premier emploi domine dans un récit ; le second, dans une "
                   "explication.",
              notes="Faire chercher au groupe lequel des deux emplois convient à chacune "
                    "des phrases de l'exercice suivant, avant de les transformer.")

    d.regle("Le même sujet, toujours",
            "Le gérondif appartient au sujet de la phrase.",
            precision="« En rentrant, j'ai vu la tache » : c'est moi qui rentre et moi "
                      "qui vois — correct. « En rentrant, la tache avait doublé » : la "
                      "tache ne rentre pas — incorrect. Avant d'écrire un gérondif, "
                      "posez-vous la question : qui fait cette action ? Si ce n'est pas "
                      "le sujet, il faut une subordonnée.",
            notes="C'est la seule vraie difficulté du point, et elle produit des phrases "
                  "involontairement drôles. En donner une ou deux : le groupe retient.")

    d.pratique('Pratique · exercice t1ger', "Récrivez avec un gérondif",
               "Remplacez la partie soulignée par « en » + participe présent.",
               [("Quand je suis rentrée du travail, j'ai vu la tache.",
                 "En rentrant du travail…"),
                ("Quand elle a ouvert la porte, elle a senti l'humidité.",
                 "En ouvrant la porte…"),
                ("Elle a limité les dommages parce qu'elle a placé une chaudière.",
                 "…en plaçant une chaudière"),
                ("Quand il est monté au troisième, Kim a trouvé le réservoir percé.",
                 "En montant au troisième…"),
                ("On prouve un dégât si on prend des photos datées.",
                 "…en prenant des photos datées"),
                ("Comme je savais que l'assureur passerait, je n'ai rien jeté.",
                 "En sachant que l'assureur passerait…")],
               corrige=True, cols=1,
               notes="Faire compter les mots avant et après pour deux ou trois phrases : "
                     "le gain est visible, et c'est un argument plus convaincant que la "
                     "règle.")

    d.piege("Changer de sujet en cours de route",
            "En rentrant du travail, la tache avait doublé.",
            "Quand je suis rentrée du travail, la tache avait doublé.",
            "La tache ne rentre pas du travail. Dès que les deux actions ont des sujets "
            "différents, le gérondif est interdit et il faut une subordonnée — « quand », "
            "« pendant que », « comme ». Ce n'est pas une nuance de style : la phrase "
            "veut dire autre chose que ce qu'on voulait.",
            notes="Faire produire au groupe deux autres phrases fautives du même genre, "
                  "puis les corriger. Fabriquer l'erreur volontairement aide à la "
                  "reconnaître.")

    d.tableau('Ne pas confondre', "Le gérondif et l\'adjectif verbal",
              ['La forme', 'Ce qu\'elle fait'],
              [["une fuite coulante", "décrit la fuite, et s'accorde"],
               ["en coulant, l'eau a traversé", "dit comment, et ne s'accorde jamais"],
               ["Le repère", "le petit mot « en » devant : il règle la question"]],
              cle=0,
              note="Sans « en », ce n'est pas un gérondif.",
              notes="Distinction rapide, à ne pas approfondir : elle sert surtout à "
                    "rassurer les élèves qui ont déjà rencontré « -ant » ailleurs.")

    d.billet(
        "Écrivez une phrase avec un gérondif à propos de votre logement.",
        exemples=[
            "« En ouvrant la fenêtre, j'ai vu qu'il pleuvait dans la cour. »",
            "Vérifiez : est-ce bien vous qui faites les deux actions ?",
        ],
        notes="Deux minutes. La vérification du sujet est la seule chose à corriger.")

    return d.save(dossier)
