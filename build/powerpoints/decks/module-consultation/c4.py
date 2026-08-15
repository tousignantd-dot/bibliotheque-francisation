# -*- coding: utf-8 -*-
"""C4 · Lire une ordonnance.
Bloc C · couleur foret (vocabulaire) · 60 min.
Source : exercices `t2med` et `t2vf2` — les indications d'un médicament.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='foret',
        titre='Lire une ordonnance',
        chapeau="« Deux fois par jour, à jeun, jusqu'à la fin du traitement. » Trois "
                "indications, trois erreurs possibles. Un médicament mal pris ne soigne "
                "pas — et parfois il nuit.",
        duree='60 minutes')

    d.titre(notes="Séance de lecture fonctionnelle. Apporter, si possible, une vraie "
                  "boîte de médicament vide avec son étiquette : la lecture réelle vaut "
                  "mieux que la lecture simulée.")

    d.objectifs([
        "comprendre les indications écrites sur une étiquette de pharmacie ;",
        "savoir ce que veulent dire « à jeun », « au besoin », « application locale » ;",
        "savoir pourquoi il faut finir un traitement ;",
        "poser les bonnes questions à la pharmacienne.",
    ])

    d.tableau('Analyse', "Cinq indications et leur sens",
              ['Ce qui est écrit', 'Ce que ça veut dire'],
              [["deux fois par jour", "le matin et le soir"],
               ["à jeun", "sans avoir mangé"],
               ["application locale", "sur la peau, à l'endroit qui fait mal"],
               ["jusqu'à la fin du traitement", "même si on se sent mieux avant"],
               ["au besoin", "seulement quand la douleur revient"]],
              cle=0,
              note="Ces cinq formules couvrent la grande majorité des ordonnances.",
              notes="Faire lire la colonne de gauche seule et demander le sens avant "
                    "d'afficher la droite. Les élèves connaissent souvent « à jeun » "
                    "sans savoir l'écrire.")

    d.regle('La règle qui sauve un traitement',
            "« Jusqu'à la fin du traitement » veut dire jusqu'à la dernière dose, même si on va mieux.",
            precision="Arrêter un antibiotique dès qu'on se sent bien laisse survivre "
                      "les bactéries les plus résistantes. Le problème revient, et le "
                      "même médicament ne fonctionne plus. C'est la consigne la plus "
                      "souvent ignorée, et la plus coûteuse.",
            notes="Demander qui a déjà arrêté un traitement avant la fin. Beaucoup de "
                  "mains se lèvent. Ne juger personne : expliquer la conséquence.")

    d.cartes('Analyse', "Quatre questions à poser à la pharmacienne", [
        ("« Est-ce que je le prends avec de la nourriture ? »",
         "Certains médicaments irritent l'estomac s'ils sont pris à jeun ; d'autres ne "
         "sont pas absorbés si on a mangé. La réponse change tout."),
        ("« Combien de temps est-ce que je dois le prendre ? »",
         "La durée n'est pas toujours écrite en toutes lettres sur l'étiquette. "
         "Demandez-la et notez-la."),
        ("« Qu'est-ce que je fais si j'oublie une dose ? »",
         "La réponse n'est pas la même selon le médicament. Ne jamais doubler la dose "
         "suivante sans avoir posé la question."),
        ("« Est-ce que ça va avec mes autres médicaments ? »",
         "La pharmacienne a la liste de tout ce que vous prenez. C'est la seule "
         "personne qui peut vérifier les interactions."),
    ], notes="Rappeler que ces quatre questions sont gratuites et sans rendez-vous. "
             "C'est le service de santé le plus accessible du Québec.")

    d.vocabulaire('Vocabulaire', "Les mots de la pharmacie", [
        ("une ordonnance", "Le papier du médecin pour obtenir un médicament."),
        ("un comprimé", "Un médicament solide, en petit disque, à avaler."),
        ("une dose", "La quantité à prendre en une fois."),
        ("un traitement", "L'ensemble des doses à prendre, du début à la fin."),
        ("un effet secondaire", "Un effet non désiré causé par un médicament."),
        ("renouveler", "Obtenir de nouveau le même médicament, sans revoir le médecin."),
    ], notes="« Renouveler » est le mot pratique de la liste : c'est ce qu'on demande au "
             "téléphone quand une ordonnance se termine.")

    d.pratique('Pratique · 1 de 3', "Que veut dire cette indication ?",
               "Donnez le sens en vos propres mots.", [
        ("« deux fois par jour »", "le matin et le soir"),
        ("« à jeun »", "sans avoir mangé"),
        ("« application locale »", "sur la peau, à l'endroit qui fait mal"),
        ("« jusqu'à la fin du traitement »", "même si on se sent mieux avant"),
        ("« au besoin »", "seulement quand la douleur revient"),
    ], corrige=True, cols=2,
       notes="Exercice de reconnaissance rapide. Enchaîner tout de suite sur la mise en "
             "situation suivante.")

    d.pratique('Pratique · 2 de 3', "Vrai ou faux — chez la pharmacienne",
               "Un comprimé, 2 fois par jour, 7 jours, avec de la nourriture, "
               "jusqu'à la fin.", [
        ("Elle doit prendre deux comprimés par jour.", "VRAI"),
        ("Le traitement dure sept jours.", "VRAI"),
        ("Elle doit prendre le médicament à jeun.", "FAUX — avec de la nourriture"),
        ("Elle peut arrêter dès qu'elle se sent mieux.", "FAUX — jusqu'à la fin"),
        ("C'est la pharmacienne qui donne les explications.", "VRAI"),
    ], corrige=True,
       notes="Lire la situation complète deux fois à voix haute avant d'afficher les "
             "énoncés : « Madame Okonkwo apporte son ordonnance. La pharmacienne lui "
             "explique de prendre un comprimé deux fois par jour, pendant sept jours, "
             "avec de la nourriture, et de finir tout le traitement même si la douleur "
             "disparaît avant. » C'est un exercice d'écoute autant que de lecture.")

    d.piege("Le piège du « je me sens mieux »",
            "Je vais mieux, j'arrête le médicament.",
            "Je vais mieux, je finis quand même le traitement.",
            "Se sentir mieux est le premier effet du médicament, pas la preuve que le "
            "problème est réglé. Pour un antibiotique, arrêter à mi-chemin est la "
            "meilleure façon de faire revenir l'infection en plus résistante.",
            notes="C'est la diapo la plus importante de la séance. Y consacrer dix "
                  "minutes s'il le faut : c'est un savoir de santé publique, pas "
                  "seulement de langue.")

    d.piege("Le piège de « au besoin »",
            "Au besoin, je le prends tous les jours pour être sûr.",
            "Au besoin, je le prends seulement quand ça fait mal.",
            "« Au besoin » veut dire : quand le symptôme est là, pas avant. Prendre un "
            "médicament « au besoin » de façon préventive dépasse la dose prévue et "
            "peut abîmer l'estomac ou le foie.",
            notes="Faire chercher un exemple concret : l'anti-inflammatoire que Yannick "
                  "prend « au besoin » selon son questionnaire de santé, en D1.")

    d.pratique('Pratique · 3 de 3', "Lisez l'étiquette et répondez",
               "« 1 comprimé, 3 fois par jour, avec de la nourriture, pendant 10 jours. »", [
        ("Combien de comprimés par jour ?", "trois"),
        ("Faut-il manger avant ?", "oui, avec de la nourriture"),
        ("Combien de comprimés en tout ?", "trente — trois par jour, dix jours"),
        ("Peut-on arrêter au bout de cinq jours si ça va mieux ?", "non, dix jours"),
    ], corrige=True,
       notes="Le troisième item est un calcul : c'est aussi une compétence de lecture. "
             "Le faire faire à voix haute.")

    d.billet(
        "Écrivez deux questions que vous poseriez à la pharmacienne.",
        exemples=[
            "Une sur la façon de prendre le médicament, une sur la durée.",
            "Écrivez-les comme vous les diriez vraiment, au comptoir.",
        ],
        notes="Relire quelques billets à voix haute. Corriger la forme de la question — "
              "c'est la révision de B3 dans une situation nouvelle.")

    return d.save(dossier)
