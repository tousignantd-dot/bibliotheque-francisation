# -*- coding: utf-8 -*-
"""B4 · Où s'arrête ce qu'on raconte
Bloc B « Défi 1 · Ce que raconte l'histoire » · couleur ambre · 75 min.
Source : exercices `t1tri` et `t1red`, mini-leçon `t1tri`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="Où s'arrête ce qu'on raconte",
        chapeau="Tout ce qui met l'histoire en marche se raconte. Tout ce "
                "qui la termine se tait. Entre les deux, il y a une "
                "frontière nette : le moment où le personnage doit choisir. "
                "C'est la seule chose que Gilberte interrompt au milieu "
                "d'une phrase, en onze ans d'animation.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du défi 1. Rendre les billets de B3 et lire deux ou "
                  "trois phrases réécrites à voix haute — anonymement. Puis annoncer la "
                  "séance : aujourd'hui, on apprend à ne pas tout dire, et c'est plus "
                  "difficile qu'il n'y paraît.")

    d.objectifs([
        "distinguer ce qui donne envie de ce qui en dit trop ;",
        "reconnaître les phrases qui trahissent la fin sans la raconter ;",
        "poser la limite poliment : « je m'arrête ici », « lisez-le » ;",
        "écrire les quatre temps de son récit d'un seul tenant.",
    ], notes="Le deuxième objectif est le plus fin de la séance. « Vous allez pleurer à la "
             "fin » ne raconte rien et annonce tout : c'est la faute que personne ne voit "
             "en la commettant.")

    d.declencheur(
        'Discussion', "Quelqu'un vous a-t-il déjà raconté la fin d'un film "
                      "avant que vous le voyiez ?",
        pistes=[
            "Est-ce que vous l'avez vu quand même ? Est-ce que c'était pareil ?",
            "Est-ce que la personne pensait mal faire ?",
            "Y a-t-il des gens à qui ça ne dérange pas ? Pourquoi, à votre avis ?",
            "Comment auriez-vous voulu qu'elle vous en parle ?",
        ],
        notes="Cette discussion sort toujours bien : tout le monde a une histoire. La "
              "troisième piste est importante — il y a réellement des personnes que ça ne "
              "dérange pas, et la règle du club n'est pas une vérité morale, c'est une "
              "convention qui protège ceux que ça dérange.")

    d.regle("On s'arrête au moment du choix",
            "Vous racontez jusqu'à ce que le personnage doive décider quelque "
            "chose — et pas une phrase de plus.",
            precision="Ce n'est pas « la fin du livre » : c'est plus tôt que ça. Une "
                      "révélation du chapitre douze compte autant que la dernière "
                      "page. La question à se poser : est-ce que ce que je vais dire "
                      "enlève quelque chose à découvrir ?",
            notes="Diapositive à photographier. Faire trouver au groupe, pour l'œuvre de "
                  "chacun, le moment du choix. Certains ne le trouvent pas du premier "
                  "coup : c'est un bon signe, ça veut dire qu'ils y réfléchissent.")

    d.tableau('Trois façons d\'en dire trop', "Et ce qu'on dit à la place",
              ['Ce qui en dit trop', 'Ce qu\'on dit à la place'],
              [["À la fin, elle brûle les lettres.", "Elle trouve une boîte de lettres."],
               ["On apprend que sa sœur est morte.", "Il y a quelque chose qu'elle ignore."],
               ["Vous allez pleurer à la fin.", "La fin m'a beaucoup touchée."],
               ["Finalement, elle reste au village.", "Elle doit choisir. Je m'arrête ici."],
               ["Le coupable, c'est le voisin.", "On soupçonne tout le monde, à un moment."]],
              cle=1,
              notes="La troisième rangée est la plus utile : « la fin m'a touchée » dit "
                    "votre émotion sans annoncer celle de l'autre. C'est une nuance de "
                    "niveau 5, et elle prépare directement le défi 3.")

    d.cartes("Trois phrases pour toute une vie", "Comment refuser de dire la fin", [
        ("« Je ne vous dis pas la fin. »",
         "Annonce la limite d'avance : personne ne se sent floué."),
        ("« Je m'arrête ici. »",
         "Se dit au milieu d'une phrase, s'il le faut. Ferme et polie."),
        ("« Lisez-le, vous verrez. »",
         "La réponse du club à « comment ça finit ? ». Elle donne encore plus envie."),
    ], notes="Faire répéter les trois à voix haute, avec le sourire. Le ton compte autant "
             "que les mots : dites sèchement, elles ferment la conversation ; dites en "
             "souriant, elles l'ouvrent.")

    d.pratique('Tri', "On peut le dire, ou ça en dit trop ?",
               "Pour chaque phrase, dites si elle a sa place au club.", [
        ("C'est un roman de trois cents pages, une histoire de famille.", "on peut le dire"),
        ("Ça se passe dans un village au bord de la mer, aujourd'hui.", "on peut le dire"),
        ("À la dernière page, elle brûle toutes les lettres.", "ça en dit trop"),
        ("Une femme revient au village pour vendre la maison de sa mère.", "on peut le dire"),
        ("On apprend au chapitre douze que sa sœur est morte.", "ça en dit trop"),
        ("Elle trouve une boîte de lettres dans le grenier.", "on peut le dire"),
        ("Finalement, elle décide de rester au village pour de bon.", "ça en dit trop"),
        ("Vous allez pleurer aux vingt dernières pages, c'est certain.", "ça en dit trop"),
    ], corrige=True, cols=2,
       notes="C'est l'exercice `t1tri` du module interactif. La huitième ligne est celle "
             "qui fait discuter : plusieurs élèves la trouvent permise. Faire remarquer "
             "qu'elle annonce que ça finit mal — c'est ce qui la disqualifie.")

    d.piege("Répondre à « comment ça finit ? » par gentillesse",
            "Bon, d'accord, mais ne le répète pas : à la fin, elle…",
            "Ça finit d'une façon que je n'avais pas vue venir.",
            "La personne insiste, mais elle ne veut pas vraiment savoir : elle veut "
            "savoir si ça vaut la peine. Répondez à cette question-là, et tout le "
            "monde est content.",
            notes="Faire jouer la scène deux par deux : l'un insiste trois fois, l'autre "
                  "tient. C'est un exercice court et il fait rire, mais il installe une "
                  "façon de dire non qui servira bien au-delà du club.")

    d.pratique('Production écrite', "Racontez votre œuvre en quatre temps",
               "Une phrase complète par temps. Restez au présent.", [
        ("TEMPS 1 — le support, le genre, une mesure.",),
        ("TEMPS 2 — où et quand ça se passe.",),
        ("TEMPS 3 — le personnage principal et ce qu'il veut, avec « qui » ou « que ».",),
        ("TEMPS 4 — ce qui complique tout, puis la phrase où vous vous arrêtez.",),
    ], notes="C'est l'exercice `t1red` du module interactif. Vingt minutes d'écriture, "
             "puis échange deux par deux : le voisin lit et dit s'il a envie de lire "
             "l'œuvre — et s'il sait déjà comment elle finit.")

    d.billet(
        "Écrivez la phrase par laquelle vous arrêterez votre récit.",
        exemples=[
            "Nommez le moment du choix : « elle doit décider si… ».",
            "Ajoutez l'une des trois phrases de sortie : « je m'arrête ici », « lisez-le ».",
        ],
        notes="Ce billet ferme le défi 1. Les quatre temps écrits en séance et cette "
              "phrase de sortie forment la moitié de la production orale du bloc E : le "
              "dire au groupe, ça change la façon dont ils écrivent.")

    return d.save(dossier)
