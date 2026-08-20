# -*- coding: utf-8 -*-
"""B3 · Le plus, le moins.
Bloc B · couleur ambre (écriture) · 75 min.
Source : mini-leçon `t1sup`, exercice `t1sup`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre='Le plus, le moins',
        chapeau="Un dépliant municipal contient une trentaine d'activités. "
                "Pour choisir, on compare : la moins chère, la plus proche, "
                "celle qui a le plus de places.",
        duree='75 minutes')

    d.titre(notes="Commencer par une comparaison réelle : projeter ou distribuer un vrai "
                  "dépliant et demander laquelle est la moins chère.")

    d.objectifs([
        "comparer deux activités avec plus, moins ou aussi ;",
        "comparer une activité à toutes les autres avec le superlatif ;",
        "accorder le petit mot : le, la ou les ;",
        "employer meilleur au lieu de « plus bon ».",
    ])

    d.tableau('Analyse', "Comparer deux choses, ou toutes",
              ['On compare', 'La forme'],
              [["deux choses", "plus / moins / aussi … que"],
               ["à toutes les autres", "le / la / les plus, le / la / les moins"],
               ["le groupe", "s'introduit par de : la moins chère de toutes"]],
              cle=1,
              note="Le test : y a-t-il un « que » après ? Alors on compare deux choses.",
              notes="Diapo centrale. Faire recopier. Le test de la note règle presque tous "
                    "les cas.")

    d.regle('Le superlatif, en un mot de plus',
            "Ajoutez le, la ou les devant plus ou moins. C'est tout.",
            precision="« moins chère que la natation » compare deux activités. « la moins "
                      "chère de toutes » la compare à l'ensemble. La différence tient à "
                      "deux lettres.",
            notes="Écrire les deux phrases l'une sous l'autre au tableau et souligner le "
                  "petit mot ajouté.")

    d.regle("L'accord du petit mot",
            "le, la ou les s'accorde avec le nom, comme un article.",
            precision="le cours <b>le plus</b> court · l'activité <b>la plus</b> chère · "
                      "les places <b>les moins</b> chères. Si vous savez mettre l'article, "
                      "vous savez faire l'accord.",
            notes="Faire produire les trois formes par trois élèves différents.")

    d.piege('Dire « plus bon »',
            "La chorale, c'est plus bon que la natation.",
            "La chorale, c'est mieux que la natation.",
            "Un seul adjectif fait exception, et c'est l'un des plus employés : <b>bon</b> "
            "devient <b>meilleur</b>. L'adverbe <b>bien</b> devient <b>mieux</b>. « Plus "
            "bon » n'existe pas, dans aucune situation.",
            notes="Donner la paire complète : meilleur (adjectif), mieux (adverbe). "
                  "L'erreur est fréquente et facile à corriger.")

    d.pratique('Pratique · 1 de 2', "Deux choses, ou toutes ?",
               "Complétez.", [
        ("La chorale coûte 30 $ : c'est ___ chère de toutes.", "la moins"),
        ("La natation coûte 85 $ : c'est ___ chère des deux.", "la plus"),
        ("Le cours du samedi est ___ proche que celui du mardi.", "plus"),
        ("De toutes les activités, c'est celle qui a ___ de places.", "le moins"),
        ("Ces places-là sont ___ chères du dépliant.", "les moins"),
        ("Le jeudi soir, c'est ___ moment de la semaine pour elle.", "le meilleur"),
    ], corrige=True,
       notes="Faire dire le test à voix haute : « y a-t-il un que après ? »")

    d.pratique('Pratique · 2 de 2', "Comparez pour de vrai",
               "Écrivez une phrase comparant les deux activités.", [
        ("Natation : 85 $, 12 semaines. Chorale : 30 $, 10 semaines.", "La chorale est moins chère que la natation."),
        ("Soccer : 120 $. Natation : 85 $. Chorale : 30 $.", "La chorale est la moins chère des trois."),
        ("Natation : 12 semaines. Chorale : 10 semaines. Soccer : 16 semaines.", "Le soccer est le plus long des trois."),
        ("Chorale : 3 places. Natation : 8 places. Soccer : 20 places.", "La chorale est celle qui a le moins de places."),
    ], corrige=True, cols=1,
       notes="Faire écrire au tableau par quatre élèves. Les chiffres viennent du module : "
             "les élèves les reconnaissent.")

    d.cartes('Ce que la comparaison sert à décider', "Trois vraies questions", [
        ("Laquelle je peux me permettre ?",
         "« C'est la moins chère de toutes. » — la première question de bien des familles."),
        ("Laquelle est la plus proche ?",
         "Une activité à quarante minutes d'autobus se termine souvent par un abandon en "
         "novembre."),
        ("Laquelle risque d'être pleine ?",
         "« Celle qui a le moins de places » est celle où il faut s'inscrire cette "
         "semaine, pas le mois prochain."),
    ], notes="Ces trois questions sont celles que se posent réellement les familles. Le "
             "dire : la grammaire sert ici à une décision concrète.")

    d.billet(
        "Comparez trois activités de votre ville en quatre phrases.",
        exemples=[
            "Deux comparaisons entre deux activités, deux superlatifs.",
            "Employez au moins une fois meilleur ou mieux.",
        ],
        notes="Corriger surtout l'accord du petit mot et l'emploi de « de » pour le groupe.")

    return d.save(dossier)
