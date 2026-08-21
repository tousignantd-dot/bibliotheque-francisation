# -*- coding: utf-8 -*-
"""D2 · Accorder, mettre en avant, restreindre
Bloc D « Défi 3 · L'opinion » · couleur ambre · 75 min.
Source : exercices `t3conc`, `t3clivage`, `t3nuance` et `t3verbes`, et leurs
mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="Accorder, mettre en avant, restreindre",
        chapeau="Trois outils pour répondre sans se faire fermer la porte : "
                "donner raison avant d'objecter, placer en tête ce qui "
                "compte, et dire « seulement » sans dire « non ».",
        duree='75 minutes')

    d.titre(notes="Dernière séance avant les productions. Elle est dense : trois points "
                  "de langue. Les traiter dans l'ordre, chacun avec son exercice, sans "
                  "chercher à tout maîtriser aujourd'hui.")

    d.objectifs([
        "employer « bien que » avec le subjonctif et « même si » avec l'indicatif ;",
        "mettre un élément en relief avec « c'est... qui » et « ce qui... c'est » ;",
        "restreindre avec « ne... que » sans en faire une négation ;",
        "choisir une formule d'opinion selon la force qu'on veut lui donner.",
    ], notes="Si le temps manque, sacrifier le troisième objectif : la concession et la "
             "mise en relief sont exigées dans la production écrite, pas « ne... que ».")

    d.declencheur(
        'Observation', "Deux façons de dire la même chose",
        pistes=[
            "« La consultation a manqué, mais le projet est bon. »",
            "« Bien que le projet soit bon, la consultation a manqué. »",
            "Après laquelle continue-t-on de vous lire ?",
            "Que retenez-vous, dans chaque cas ?",
        ],
        notes="Faire voter le groupe. La deuxième version convainc davantage, et la "
              "raison est l'ordre : on retient ce qui vient en second.")

    d.regle("Bien que et même si ne se conduisent pas pareil",
            "Bien que + subjonctif. Même si + indicatif. Jamais l'inverse.",
            precision="« Bien que le projet soit utile » - subjonctif, toujours. « Même "
                      "si je trouve son ton un peu fort » - indicatif, toujours. Les "
                      "deux marqueurs se ressemblent par le sens et ne se ressemblent "
                      "en rien par la construction. Dans le doute, employez « même si » : "
                      "il ne demande rien de particulier.",
            notes="Diapositive à photographier. Le conseil final est sérieux : mieux "
                  "vaut une phrase juste avec « même si » qu'une phrase fautive avec "
                  "« bien que ».")

    d.cartes("Les cinq subjonctifs à connaître", "Après « bien que »", [
        ("être", "bien que ce soit, bien qu'ils soient"),
        ("avoir", "bien qu'il ait, bien qu'ils aient"),
        ("pouvoir", "bien qu'elle puisse"),
        ("venir", "bien que ça vienne"),
        ("faire", "bien qu'il fasse"),
    ], notes="Ces cinq verbes couvrent la quasi-totalité des emplois réels. Les faire "
             "apprendre par coeur plutôt que d'enseigner la formation du subjonctif.")

    d.regle("Mettre en relief, c'est déplacer et encadrer",
            "En français, on n'insiste pas en criant un mot : on l'encadre.",
            precision="« C'est le comité qui a retenu Boisjoli » encadre le sujet. "
                      "« C'est le 14 octobre qu'on décide » encadre un moment. « Ce qui "
                      "m'inquiète, c'est les heures » encadre une idée entière. Le "
                      "repère : « qui » quand ce qui suit a besoin d'un sujet, « que » "
                      "dans tous les autres cas.",
            notes="Diapositive à photographier. La troisième tournure est la plus utile "
                  "pour ouvrir un billet de blogue : elle annonce le sujet dès la "
                  "première ligne.")

    d.piege("Bien que suivi de l'indicatif",
            "Bien que c'est une bonne idée, la consultation a manqué.",
            "Bien que ce soit une bonne idée, la consultation a manqué.",
            "C'est l'erreur numéro un du niveau, et elle est audible. Elle vient de ce "
            "que « bien que » se traduit dans beaucoup de langues par un mot qui "
            "n'exige rien. La parade est mécanique : après « bien que », on écrit "
            "d'abord le verbe au subjonctif, on relit ensuite.",
            notes="Faire répéter « bien que ce soit » une dizaine de fois à voix haute. "
                  "L'automatisme s'installe par l'oreille plus que par la règle.")

    d.tableau('Analyse', "Dire une opinion, plus ou moins fort",
              ['La formule', 'La force'],
              [["Il me semble que...", "très prudent : je le pense, sans en être sûr"],
               ["Je trouve que...", "ordinaire : mon avis, sans prétention"],
               ["À ma connaissance...", "prudent sur un fait : d'après ce que je sais"],
               ["Je suis convaincue que...", "fort : je n'ai plus de doute"],
               ["Il est inacceptable que...", "très fort : je juge et j'attends que ça change"]],
              cle=0,
              note="« À ma connaissance » est la formule la plus utile du tableau : elle protège celui qui écrit.",
              notes="Diapositive à photographier. Insister sur « à ma connaissance » : "
                    "elle permet d'écrire publiquement sans risquer d'affirmer ce qu'on "
                    "n'a pas vérifié.")

    d.pratique('Application', "Concéder, puis objecter",
               "Complétez avec le mode qui convient.", [
        ("Bien que le projet ____ (être) utile, la façon de faire dérange.", "soit"),
        ("Même si je ____ (trouver) son ton un peu fort, elle a raison sur un point.", "trouve"),
        ("Bien que la Ville ____ (avoir) consulté le comité, les citoyens n'ont rien vu venir.", "ait"),
        ("Bien que les chiffres ____ (être) exacts, la conclusion reste discutable.", "soient"),
        ("Même si le dépôt ____ (ouvrir) au printemps, je ne pourrai pas y aller après le travail.", "ouvre"),
        ("Bien que ça ____ (venir) du comité exécutif, ça reste une recommandation.", "vienne"),
    ], corrige=True,
       notes="Faire repérer le marqueur avant de conjuguer. Le réflexe à installer : "
             "je lis le marqueur, je choisis le mode, puis j'écris.")

    d.pratique('Application', "Mettez en avant ce qui compte",
               "Récrivez en encadrant l'élément indiqué.", [
        ("Le comité a retenu Boisjoli. (le comité)", "C'est le comité qui a retenu Boisjoli."),
        ("Le conseil décide le 14 octobre. (la date)", "C'est le 14 octobre que le conseil décide."),
        ("Les heures d'ouverture m'inquiètent. (les heures)", "Ce qui m'inquiète, c'est les heures d'ouverture."),
        ("Je demande une réponse claire. (la réponse)", "Ce que je demande, c'est une réponse claire."),
        ("Vous devriez poser la question. (vous)", "C'est vous qui devriez poser la question."),
    ], corrige=True,
       notes="La dernière piège sur l'accord : « c'est vous qui devriez », pas "
             "« devrait ». Le verbe suit l'élément encadré.")

    d.billet(
        "Écrivez une phrase de concession sur le projet du quartier.",
        exemples=[
            "Commencez par « Bien que » ou par « Même si ».",
            "Reprenez le point d'accord que vous avez noté en D1.",
        ],
        notes="Fin du Défi 3. Cette phrase sera la première ligne du billet de blogue "
             "de E2 : le dire, ça motive.")

    return d.save(dossier)
