# -*- coding: utf-8 -*-
"""B2 · De… à, jusqu'à, à partir de.
Bloc B « Défi 1 · Mon quart commence à quelle heure ? » · couleur ambre · 60 min.
Source : exercice `t1prep`, mini-leçon `t1prep`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre="De… à, jusqu'à, à partir de",
        chapeau="Quatre petits mots encadrent une heure, et chacun dit "
                "autre chose : les deux bouts, la fin seule, le début seul, "
                "ou la durée sans aucune heure.",
        duree='60 minutes')

    d.titre(notes="Séance d'écriture. Commencer par écrire au tableau le quart de trois "
                  "élèves, tel qu'ils l'ont noté en A4, et faire dire la phrase complète "
                  "avant d'expliquer quoi que ce soit.")

    d.objectifs([
        "dire un quart entier avec « de… à… » ;",
        "employer « jusqu'à » quand on ne donne que la fin ;",
        "employer « à partir de » quand on ne donne que le début ;",
        "employer « pendant » pour la durée.",
    ])

    d.regle("Les deux bouts : de… à…",
            "Je travaille de six heures à quatorze heures.",
            precision="C'est la forme de l'horaire, et la plus utile de "
                      "toutes : elle donne le début et la fin dans la même "
                      "phrase. Les deux petits mots vont ensemble — l'un "
                      "sans l'autre laisse la phrase en suspens.",
            notes="Diapo à photographier. Faire produire la phrase par chaque élève, avec "
                  "ses vraies heures. Cinq minutes, tout le monde parle.")

    d.tableau('Analyse', "Quatre façons d'encadrer une heure",
              ["La forme", "Ce qu'elle dit"],
              [["de six heures à quatorze heures", "le début et la fin"],
               ["jusqu'à quatorze heures", "la fin seulement"],
               ["à partir de six heures", "le début seulement"],
               ["pendant huit heures", "la durée — aucune heure d'horloge"]],
              cle=1,
              note="La quatrième ne place rien dans la journée : elle compte "
                   "le temps. « Pendant huit heures » ne dit pas quand.",
              notes="Diapo à photographier. Faire trouver au groupe une situation pour "
                    "chaque ligne : « la cuisine est ouverte à partir de… », « je reste "
                    "jusqu'à… ».")

    d.pratique('Écriture', "De, à, jusqu'à, à partir de ou pendant",
               "Complétez avec le petit mot qui convient.", [
        ("Je travaille ___ six heures à quatorze heures.", "de"),
        ("Je travaille de six heures ___ quatorze heures.", "à"),
        ("La pause dure ___ onze heures et demie à midi.", "de"),
        ("Miguel reste ___ vingt-deux heures.", "jusqu'à"),
        ("La cuisine est ouverte ___ cinq heures du matin.", "à partir de"),
        ("Le quart dure huit heures : je travaille ___ huit heures.", "pendant"),
    ], corrige=True,
       notes="C'est l'exercice `t1prep` du module interactif, mot pour mot. Les trois "
             "premières lignes se répondent : « de… à » se travaille en bloc, pas "
             "mot par mot.")

    d.piege("Dire « je travaille à six heures à quatorze heures »",
            "Je travaille à six heures à quatorze heures.",
            "Je travaille de six heures à quatorze heures.",
            "Le premier bout prend « de », jamais « à ». L'erreur est "
            "minuscule et elle s'entend beaucoup : c'est celle qui signale "
            "le plus vite qu'on récite un horaire sans le comprendre.",
            notes="Ne pas s'attarder : nommer, corriger, faire répéter trois fois la "
                  "forme juste, et passer. L'erreur disparaît d'elle-même avec l'usage.")

    d.pratique('Écriture', "Dites votre semaine",
               "Une phrase complète par situation.", [
        ("Votre quart de lundi.", "Lundi, je travaille de… à…"),
        ("L'heure où vous finissez, sans dire quand vous commencez.", "Je reste jusqu'à…"),
        ("L'heure où vous commencez, sans dire quand vous finissez.", "Je suis là à partir de…"),
        ("La durée de votre quart.", "Je travaille pendant… heures."),
        ("Votre pause.", "Ma pause est de… à…"),
    ], corrige=False, cols=1,
       notes="Chacun écrit ses vraies heures, puis les lit à son voisin. Corriger "
             "seulement les petits mots : les heures sont personnelles, elles ne se "
             "corrigent pas.")

    d.regle("Attention à « à » devant « le »",
            "au plus tard — jamais « à le plus tard »",
            precision="Devant midi et minuit, rien ne change : « jusqu'à "
                      "midi », « à partir de minuit ». C'est seulement "
                      "devant « le » que « à » se transforme.",
            notes="Diapo à photographier. Ne pas ouvrir tout le chapitre des articles "
                  "contractés ici : donner la forme « au plus tard », qui est celle qu'on "
                  "entend au travail, et laisser le reste au niveau suivant.")

    d.billet(
        "Écrivez vos cinq journées avec « de… à… ».",
        exemples=[
            "Une ligne par jour, les heures en chiffres et en lettres.",
            "« Mardi : de 7 h à 15 h — de sept heures à trois heures. »",
        ],
        notes="Devoir court. La double écriture — chiffres et lettres — est exactement "
              "l'exercice de B3 : l'horaire écrit d'un côté, l'heure parlée de l'autre.")

    return d.save(dossier)
