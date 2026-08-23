# -*- coding: utf-8 -*-
"""B4 · Dire précisément ce qu'on n'a pas compris
Bloc B « Défi 1 » · couleur ambre · 75 min.
Source : exercices `t1refor` et `t1trois`, et leurs mini-leçons. Savoir
lexical du niveau 8 : phrases clés pour faire clarifier les points
équivoques et reprendre une partie d'un discours.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="« Je n'ai pas compris » est presque toujours faux",
        chapeau="Vous avez compris quinze mots sur seize. Dire que vous "
                "n'avez rien compris oblige l'autre à tout reprendre, et vous "
                "fait passer pour plus loin du compte que vous ne l'êtes.",
        duree='75 minutes')

    d.titre(notes="Séance très utile et très courte à expliquer : le contenu tient en "
                  "quatre formules. Tout le temps doit aller à la pratique orale.")

    d.objectifs([
        "faire préciser un mot, un seul, sans faire reprendre la phrase ;",
        "dire où le fil s'est rompu plutôt que de dire qu'on est perdu ;",
        "vérifier ce qu'on a compris en changeant les mots ;",
        "résumer avant de conclure une conversation.",
    ], notes="Les quatre gestes sont dans le programme sous « exprimer une "
             "incompréhension partielle ». Le mot qui compte est partielle.")

    d.declencheur(
        'Discussion', "Que faites-vous, au téléphone, quand un mot vous échappe ?",
        pistes=[
            "Vous dites « pardon » ? Vous dites « oui oui » ?",
            "Vous attendez la suite en espérant comprendre ?",
            "Combien de temps dure la gêne, et combien de temps dure l'erreur qui suit ?",
            "Qu'est-ce que ça coûte, à l'autre, de tout reprendre ?",
        ],
        notes="La question sur le coût pour l'autre renverse la perspective. Beaucoup "
              "d'élèves se taisent par politesse, et c'est le contraire de poli.")

    d.cartes('Analyse', "Quatre gestes, quatre formules", [
        ("Faire préciser un mot",
         "Excusez-moi, le mot « vérifiable », vous l'entendez comment ? "
         "Qu'est-ce que vous mettez exactement sous « polyvalence » ? On "
         "demande le sens dans cette phrase-ci, pas une définition."),
        ("Faire répéter une partie",
         "Je vous suis jusqu'à « après dix-huit heures » ; après, je perds "
         "le fil. Vous avez dit trois dates ; j'ai la première et la "
         "troisième. On montre où, on ne dit pas que."),
        ("Vérifier qu'on a compris",
         "Si je comprends bien, l'équipe reste à constituer ? Autrement dit, "
         "c'est le raisonnement que vous regardez. On reformule avec ses "
         "propres mots : répéter ceux de l'autre ne prouve rien."),
        ("Résumer avant de conclure",
         "En somme, trois étapes réparties sur deux semaines. Pour résumer, "
         "vous cherchez quelqu'un qui bâtira l'équipe. On se souvient "
         "toujours de la dernière phrase."),
    ], notes="Faire choisir à chaque élève deux formules qu'il apprendra par cœur. Au "
             "téléphone, on n'a pas le temps de composer une phrase.")

    d.tableau('Analyse', "Ce qu'on dit, ce que l'autre entend",
              ['La formule', 'L\'effet réel'],
              [["« Je n'ai pas compris. »",
                "il faut tout reprendre : trois minutes perdues"],
               ["« Le mot vérifiable, vous l'entendez comment ? »",
                "une seule chose à préciser : dix secondes"],
               ["« Oui, oui. »",
                "l'autre continue, et vous répondrez à côté"],
               ["« Si je comprends bien, l'équipe reste à constituer ? »",
                "l'autre confirme ou corrige tout de suite"],
               ["« En somme, trois étapes sur deux semaines. »",
                "vous laissez l'impression d'avoir tout suivi"]],
              cle=0,
              notes="Diapositive à photographier. Le tableau se lit de haut en bas : "
                    "les formules vagues coûtent du temps, les formules précises en "
                    "rapportent.")

    d.pratique('Pratique 1 de 2', "Quelle formule employer ?",
               "Choisissez le geste qui convient.", [
        ("Un mot que vous connaissez, mais dont vous doutez du sens ici.", "faire préciser le mot"),
        ("Vous avez suivi le début, puis vous avez décroché à un endroit précis.", "faire répéter une partie"),
        ("Vous croyez avoir compris et vous voulez en être sûre.", "vérifier avec ses propres mots"),
        ("Vous fermez la conversation en rassemblant ce qui a été dit.", "résumer"),
        ("Trois chiffres ont été donnés, vous n'en avez retenu que deux.", "faire répéter une partie"),
    ], corrige=True,
       notes="Faire dire la formule complète, pas seulement le nom du geste. C'est la "
             "phrase qu'il faut avoir en bouche, pas la catégorie.")

    d.piege('Piège', "hocher la tête au téléphone",
            "dire un mot",
            "Votre interlocuteur n'entend rien de vos gestes. Le silence se "
            "lit comme une absence, et l'autre finit par demander « vous êtes "
            "toujours là ? ». Un « d'accord » ou un « je note » toutes les "
            "deux ou trois phrases suffit à tenir la ligne vivante.",
            notes="Défaut très fréquent et jamais nommé. Le faire remarquer une fois, "
                  "et il disparaît.")

    d.regle("Trois étapes, trois choses observées",
            "L'examen écrit regarde comment vous raisonnez. L'entrevue de "
            "groupe regarde comment vous êtes avec les autres. L'entrevue "
            "individuelle regarde qui vous êtes et ce que vous voulez.",
            precision="Rien ne s'efface entre les étapes : ce qu'on écrit sur vous à "
                      "la première est relu avant la troisième. Et c'est à la "
                      "deuxième que la majorité des candidats sont écartés, parce "
                      "qu'ils croient qu'il faut briller alors qu'on observe s'ils "
                      "écoutent.",
            notes="Diapositive à photographier. C'est le conseil le plus rentable du "
                  "module : consacrer à l'entrevue de groupe autant de préparation "
                  "qu'à l'entrevue finale.")

    d.pratique('Pratique 2 de 2', "À quelle étape ?",
               "Dites de quelle étape il s'agit.", [
        ("On vous donne quatre-vingt-dix minutes et une ligne arrêtée.", "l'examen écrit"),
        ("Vous êtes quatre autour d'une table et l'on observe qui écoute.", "l'entrevue de groupe"),
        ("On vous demande pourquoi vous êtes restée cinq ans au même poste.", "l'entrevue individuelle"),
        ("C'est le seul moment où l'on parle d'argent.", "l'entrevue individuelle"),
        ("C'est l'étape où la majorité des candidats sont écartés.", "l'entrevue de groupe"),
    ], corrige=True,
       notes="Le quatrième est celui à retenir : négocier l'échelon devant trois "
             "autres candidats met tout le monde mal à l'aise et vous écarte.")

    d.billet(
        "Deux par deux, jouez un appel de trois minutes. Celui qui écoute doit employer deux des quatre formules.",
        exemples=[
            "L'autre parle vite et donne trois chiffres d'affilée.",
            "On change de rôle après trois minutes.",
        ],
        notes="À faire en classe s'il reste du temps, en devoir sinon. C'est la "
              "préparation directe du jeu de rôle de E1.")

    return d.save(dossier)
