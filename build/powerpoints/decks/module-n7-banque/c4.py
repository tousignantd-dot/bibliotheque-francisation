# -*- coding: utf-8 -*-
"""C4 · Les mots qui tiennent une comparaison debout
Bloc C « Défi 2 · Faire travailler l'argent » · couleur ambre · 90 min.
Source : exercice `t2conn` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre='Les mots qui tiennent une comparaison debout',
        chapeau="On peut aligner tous les chiffres du monde : tant qu'aucun "
                "mot ne dit le rapport entre eux, le lecteur doit le deviner.",
        duree='90 minutes')

    d.titre(notes="Dernière séance du bloc C, et la plus tournée vers la production. "
                  "Tout ce qui est travaillé ici sert directement à l'exposé de E1.")

    d.objectifs([
        "poser deux faits côte à côte avec tandis que ;",
        "renverser une impression avec en revanche ;",
        "ajouter un argument avec de plus ;",
        "conclure une comparaison, ce qu'on oublie presque toujours.",
    ], notes="Le quatrième objectif est celui qui fait la différence entre un exposé de "
             "niveau 5 et un exposé de niveau 7.")

    d.declencheur(
        'Observation', "Deux colonnes de chiffres, est-ce que c'est une comparaison ?",
        pistes=[
            "Qu'est-ce qui manque pour que ça en devienne une ?",
            "Qui fait le travail, quand le rapport n'est pas dit ?",
            "As-tu déjà lu un tableau sans savoir quoi en conclure ?",
            "Quelle phrase manquait ?",
        ],
        notes="La réponse à la deuxième question est le lecteur, et il ne le fait pas "
              "toujours dans le bon sens. C'est l'argument de la séance.")

    d.tableau('Analyse', "Quatre travaux, huit mots",
              ['Ce que je veux faire', 'Les mots'],
              [['poser côte à côte', 'tandis que, alors que'],
               ['renverser', 'en revanche, par contre'],
               ['ajouter', 'de plus, par ailleurs'],
               ['conclure', "en somme, c'est pourquoi"]],
              cle=0,
              note="Ponctuation : virgule devant tandis que, point-virgule devant en revanche.",
              notes="Diapositive à photographier. La note sur la ponctuation est celle "
                    "que les élèves oublient le plus, et elle se voit tout de suite.")

    d.regle("Puisque et parce que ne font pas le même travail",
            "Puisque s'appuie sur une raison que l'autre connaît déjà ; parce que en "
            "apporte une nouvelle.",
            precision="« Puisque votre projet a une date, le dépôt à terme convient » "
                      "suppose que la date a déjà été dite. « Parce que je n'ai jamais "
                      "remboursé une marge » apporte une information neuve. Employer "
                      "l'un pour l'autre ne fait pas de faute, mais fait perdre une "
                      "nuance que le niveau 7 attend.",
            notes="Diapositive à photographier. Faire produire deux phrases, une avec "
                  "chaque connecteur, sur le même contenu.")

    d.pratique('Application', "Complétez avec le bon connecteur",
               "Chacun ne sert qu'une fois.", [
        ("Le taux de la marge est variable, ___ celui du prêt reste fixe.", "tandis que"),
        ("Le dépôt rapporte 3,10 % ; ___, l'argent est bloqué deux ans.", "en revanche"),
        ("Le prêt se termine ; ___, il n'y a aucune pénalité si je paie plus vite.", "de plus"),
        ("___ votre projet a une date précise, le dépôt à terme convient.", "Puisque"),
        ("___, la marge coûte moins cher, mais c'est le prêt qui finit.", "En somme"),
        ("Les intérêts s'accumulent ; ___ une dette qui ne baisse pas coûte pareil.", "c'est pourquoi"),
    ], corrige=True,
       notes="Faire lire chaque phrase complète avec la pause de la ponctuation. Le "
             "point-virgule s'entend.")

    d.regle("Une comparaison sans conclusion n'est qu'une liste",
            "Terminez par « en somme », « c'est pourquoi » ou « je prends x parce que "
            "y ».",
            precision="Un exposé qui s'arrête sur les deux colonnes laisse le travail "
                      "au lecteur. La méthode qui marche : écrire d'abord la phrase de "
                      "conclusion, puis remonter. Les deux colonnes s'organisent toutes "
                      "seules autour d'elle.",
            notes="Diapositive à photographier. C'est la consigne exacte de la "
                  "production orale de E1 : le troisième temps est la décision.")

    d.pratique('Production', "Reliez les deux faits",
               "À deux : l'un donne les deux faits, l'autre fait la phrase.", [
        ("marge moins chère / rien n'oblige à finir", "en revanche"),
        ("prêt avec date de fin / aucune pénalité", "de plus"),
        ("dépôt à 3,10 % / argent bloqué deux ans", "par contre"),
        ("projet dans deux ans / dépôt à terme", "puisque"),
        ("taux variable / taux fixe", "tandis que"),
        ("les deux se défendent / je choisis le prêt", "en somme"),
    ], corrige=False,
       notes="Circuler et écouter la ponctuation orale : la pause avant le connecteur "
             "est ce qui rend la phrase compréhensible de loin.")

    d.piege('Le piège', "un connecteur à chaque phrase",
            "un connecteur par rapport réel",
            "Un texte saturé de connecteurs se lit plus mal qu'un texte qui n'en a "
            "pas : le lecteur cherche des rapports qui n'existent pas et se fatigue. "
            "Trois ou quatre dans un exposé de quatre-vingt-dix secondes suffisent "
            "largement.",
            notes="À rappeler en E1 : les enregistrements où chaque phrase commence par "
                  "« de plus » sont plus difficiles à suivre, pas plus riches.")

    d.billet("Écris ta phrase de conclusion pour l'exposé du bloc E : quel produit, et "
             "pourquoi.",
             exemples=["En somme, je prends le prêt parce que je veux une date de fin.",
                       "C'est pourquoi je choisis le dépôt à terme."],
             notes="Trois minutes. Ces billets sont le premier jet de la production "
                   "orale : les rendre au début de E1.")

    return d.save(dossier)
