# -*- coding: utf-8 -*-
"""C2 · Le petit mot « en ».
Bloc C · couleur ambre (écriture) · 75 min.
Source : mini-leçon `t2en`, exercice `t2en`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Le petit mot « en »",
        chapeau="« — Combien de poitrines voulez-vous ? — J'en veux quatre. » "
                "Sans ce mot, il faudrait répéter « poitrines » à chaque "
                "phrase. Il remplace le produit et garde la quantité.",
        duree='75 minutes')

    d.titre(notes="Si le groupe a fait le module des déplacements, commencer par rappeler "
                  "« y » : la moitié de la leçon est déjà acquise.")

    d.objectifs([
        "remplacer un produit par « en » sans répéter son nom ;",
        "placer « en » devant le verbe ;",
        "garder la quantité à la fin de la phrase ;",
        "employer « en » à la forme négative.",
    ])

    d.tableau('Analyse', "y et en, les deux compagnons",
              ['Le pronom', 'Ce qu\'il remplace', 'Exemple'],
              [["y", "un lieu", "J'y vais le jeudi."],
               ["en", "une quantité", "J'en veux quatre."]],
              cle=1,
              note="Les deux se placent devant le verbe. Aucun des deux ne se répète après.",
              notes="Diapo centrale. Faire recopier. Le parallèle rend la leçon deux fois "
                    "plus courte.")

    d.regle('Sa place : devant le verbe',
            "Comme y, comme tous les petits pronoms du français.",
            precision="« J'en veux quatre », jamais « je veux en quatre ». Au passé "
                      "composé, il passe devant l'auxiliaire : « j'<b>en</b> ai pris "
                      "deux ». C'est l'inverse de plusieurs langues, et c'est ce qui "
                      "demande de la pratique.",
            notes="Faire produire trois phrases par trois élèves, au tableau.")

    d.regle('La quantité reste à la fin',
            "C'est la différence avec les autres pronoms.",
            precision="« J'en veux <b>quatre</b>. » · « J'en prends <b>une livre</b>. » · "
                      "« Il m'en reste <b>trois</b>. » Le produit disparaît, la quantité "
                      "demeure. C'est justement ce qui rend le mot utile au comptoir.",
            notes="Faire remarquer que « j'en veux » tout seul est correct mais vague. Au "
                  "comptoir, on donne presque toujours la quantité.")

    d.piege('Répéter le produit après « en »',
            "J'en prends deux poitrines.",
            "J'en prends deux.",
            "Le produit est déjà dans le <b>en</b>. Le répéter est une faute, et elle "
            "s'entend immédiatement — comme si on disait deux fois le même mot. La phrase "
            "juste est plus courte, et c'est tout l'intérêt.",
            notes="Faire entendre la faute : lire la phrase de gauche à voix haute, "
                  "lentement. Le groupe réagit.")

    d.pratique('Pratique · 1 de 2', "Remplacez par « en »",
               "Récrivez la réponse.", [
        ("— Combien de poitrines ? — Je veux quatre poitrines.", "J'en veux quatre."),
        ("— Il reste du bœuf haché ? — Il me reste du bœuf haché.", "Il m'en reste."),
        ("Je prends deux savons.", "J'en prends deux."),
        ("Il n'y a plus de riz.", "Il n'y en a plus."),
        ("Vous voulez combien de jambon ?", "Vous en voulez combien ?"),
    ], corrige=True, cols=1,
       notes="La quatrième ligne contient « y » et « en » ensemble : c'est la phrase la "
             "plus fréquente d'un magasin. La faire répéter.")

    d.pratique('Pratique · 2 de 2', "Corrigez la phrase",
               "Chaque phrase contient une faute de place ou une répétition.", [
        ("Je veux en quatre.", "J'en veux quatre."),
        ("J'en prends deux savons.", "J'en prends deux."),
        ("Il reste en trois.", "Il en reste trois."),
        ("Je ne prends pas en.", "Je n'en prends pas."),
    ], corrige=True, cols=1,
       notes="Faire nommer la faute avant de corriger : place du pronom, ou répétition du "
             "produit ?")

    d.cartes('Les phrases du comptoir', "Trois à savoir par cœur", [
        ("« J'en veux quatre. »",
         "La réponse standard à « combien en voulez-vous ? ». Trois mots."),
        ("« Il m'en reste. »",
         "Ce que dit la personne au comptoir quand il reste du produit."),
        ("« Il n'y en a plus. »",
         "La phrase qu'on entend quand un produit est épuisé. Elle contient y et en."),
    ], notes="Faire répéter les trois par le groupe. Elles couvrent la majorité des "
             "échanges d'un comptoir.")

    d.billet(
        "Écrivez six échanges courts au comptoir, avec « en » dans chaque réponse.",
        exemples=[
            "Une question, une réponse. Deux à la forme négative.",
            "Exemple : « — Vous en voulez combien ? — J'en veux une livre. »",
        ],
        notes="Corriger surtout la place du pronom et l'absence de répétition. Rendre avant "
              "E1.")

    return d.save(dossier)
