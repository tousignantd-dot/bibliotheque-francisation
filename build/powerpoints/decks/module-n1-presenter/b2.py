# -*- coding: utf-8 -*-
"""B2 · Je suis, j'ai, je viens de.
Bloc B « Défi 1 » · couleur ambre · 60 min.
Source : mini-leçons `t1etre` et `t1venir`, exercices du même nom.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre="Je suis, j'ai, je viens de",
        chapeau="Trois verbes portent presque toute la présentation. Et un "
                "petit mot change devant le nom du pays.",
        duree='60 minutes')

    d.titre(notes="Séance de langue. Elle donne la grammaire des cinq phrases de B1.")

    d.objectifs([
        "employer être devant un métier et une nationalité ;",
        "employer avoir pour l'âge et les enfants ;",
        "choisir entre de, du, d' et des devant un pays ;",
        "distinguer « à » (la ville) et « au » (le pays).",
    ])

    d.declencheur(
        'Écoute', "Laquelle de ces phrases est juste ?",
        pistes=[
            "« Je suis trente ans. »",
            "« J'ai trente ans. »",
            "« Je suis une infirmière. »",
            "« Je suis infirmière. »",
        ],
        notes="Faire choisir avant d'expliquer. Les deux erreurs proposées sont les plus "
              "fréquentes, et elles viennent d'autres langues où elles sont correctes.")

    d.tableau('Analyse', "Être ou avoir ?",
              ['Avec être', 'Avec avoir'],
              [["Je suis mécanicienne.", "J'ai trente ans."],
               ["Je suis algérienne.", "J'ai un enfant."],
               ["Je suis élève.", "J'ai deux fils."]],
              cle=1,
              note="En français, on A un âge. On N'EST PAS un âge.",
              notes="Diapo à photographier. C'est l'erreur la plus fréquente du niveau 1, "
                    "et la plus facile à corriger une fois nommée.")

    d.regle("Pas d'article devant le métier",
            "Je suis mécanicienne.",
            precision="Devant un métier ou une nationalité, on ne met ni « un » ni "
                      "« une » : « je suis infirmière », « je suis brésilien », « je suis "
                      "élève ». C'est différent de l'anglais et de plusieurs autres "
                      "langues.",
            notes="Diapo à photographier. Faire dire son métier par chaque élève, sans "
                  "article.")

    d.tableau('Analyse', "Devant le pays",
              ['On dit', 'Exemples'],
              [["d'", "d'Algérie, d'Haïti, d'Iran"],
               ["du", "du Vietnam, du Maroc, du Brésil"],
               ["de", "de France, de Chine, de Syrie"],
               ["des", "des Philippines, des États-Unis"]],
              cle=0,
              note="Une seule chose à apprendre par cœur : votre pays à vous.",
              notes="Diapo à photographier. Faire écrire à chaque élève sa phrase, et la "
                    "vérifier une par une — c'est celle qu'il dira toute sa vie.")

    d.regle("À la ville, au pays",
            "J'habite à Montréal. J'habite au Canada.",
            precision="Devant une <b>ville</b> : <b>à</b> Montréal, <b>à</b> Laval, "
                      "<b>à</b> Québec. Devant un <b>pays</b> : <b>au</b> Canada, "
                      "<b>en</b> France, <b>au</b> Vietnam.",
            notes="Diapo à photographier. Au niveau 1, s'en tenir à « à + ville », qui "
                  "suffit pour se présenter ici.")

    d.piege("Confondre la ville et le pays",
            "J'habite à Canada.",
            "J'habite à Montréal. J'habite au Canada.",
            "« À » va devant une ville, « au » devant un pays masculin. Pour se présenter "
            "ici, la ville suffit presque toujours — c'est celle qu'on vous demande.",
            notes="Le dire sans insister : au niveau 1, l'erreur ne gêne pas la "
                  "compréhension.")

    d.pratique('Pratique · 1 de 2', "Être ou avoir ?",
               "Complétez.", [
        ("Je ___ mécanicienne.", "suis"),
        ("J'___ trente ans.", "ai"),
        ("Je ___ algérienne.", "suis"),
        ("J'___ un enfant.", "ai"),
        ("Je ___ élève.", "suis"),
        ("Je n'___ pas d'enfants.", "ai"),
    ], corrige=True,
       notes="Utiliser l'exercice 2 du module.")

    d.pratique('Pratique · 2 de 2', "De, du, d' ou des ?",
               "Complétez : je viens ___", [
        ("Algérie", "d'"),
        ("Vietnam", "du"),
        ("France", "de"),
        ("Philippines", "des"),
        ("Haïti", "d'"),
        ("Colombie", "de"),
    ], corrige=True,
       notes="Utiliser l'exercice 3. Terminer en faisant dire à chacun la phrase de son "
             "propre pays, à voix haute.")

    d.billet(
        "Écrivez trois phrases sur vous.",
        exemples=[
            "Une avec « je suis », une avec « j'ai », une avec « je viens de ».",
            "Vérifiez le petit mot devant votre pays.",
        ],
        notes="Fin du bloc B. Ramasser et corriger surtout la phrase du pays.")

    return d.save(dossier)
