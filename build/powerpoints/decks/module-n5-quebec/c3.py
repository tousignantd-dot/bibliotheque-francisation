# -*- coding: utf-8 -*-
"""C3 · Plus long, moins cher, aussi beau
Bloc C « Défi 2 » · couleur ambre · 75 min. Écriture et grammaire.
Source : exercice `t2comp` et sa mini-leçon (comparer, puis choisir).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="Plus long, moins cher, aussi beau",
        chapeau="L'autocar ou le train ? Le gîte ou le camping ? Le sentier "
                "du bord de l'eau ou celui de la montagne ? Comparer n'est "
                "pas énumérer : il faut dire lequel on choisit, et donner la "
                "raison qui a fait pencher.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire, mais la grammaire y est simple : le vrai travail "
                  "est de justifier un choix. Un élève de niveau 5 doit pouvoir dire "
                  "« je prends l'autocar parce que… », pas seulement « l'autocar est "
                  "moins cher ».")

    d.objectifs([
        "comparer deux choses avec plus, moins et aussi ;",
        "employer « meilleur » et « mieux » à la bonne place ;",
        "dire lequel on choisit et pourquoi, en une phrase ;",
        "accepter un inconvénient en le nommant, avec « même si ».",
    ], notes="Le quatrième objectif est ce qui distingue une comparaison d'adulte : "
             "« l'autocar est moins confortable, mais il est plus pratique ». Reconnaître "
             "le point faible de son choix est un signe de maîtrise.")

    d.regle("Trois degrés, une seule construction",
            "plus … que · moins … que · aussi … que.",
            precision="L'adjectif s'accorde avec ce dont on parle : la route est "
                      "plus longue, le trajet est plus long.",
            notes="Diapositive à photographier. L'accord de l'adjectif est l'erreur "
                  "d'écriture la plus fréquente ici, et elle ne s'entend pas toujours : "
                  "il faut la voir à la relecture.")

    d.tableau('Deux moyens', "L'autocar ou le train, pour Rimouski",
              ["L'autocar", "Le train"],
              [["Tous les jours", "Trois jours par semaine"],
               ["Départ le matin", "Départ à 18 h 30"],
               ["Arrivée à 15 h 10", "Arrivée en pleine nuit"],
               ["Moins confortable", "Plus confortable"]],
              cle=1,
              notes="Les faits sont réels : l'Océan de VIA Rail passe le mercredi, le "
                    "vendredi et le dimanche. Faire tirer la conclusion par le groupe "
                    "avant de la dire — c'est exactement ce que fait Thuy.")

    d.cartes("Deux mots qu'on confond", "« Meilleur » et « mieux »", [
        ("meilleur",
         "Adjectif : il accompagne un nom. « Un meilleur prix. »"),
        ("mieux",
         "Adverbe : il accompagne un verbe. « On dort mieux. »"),
        ("C'est un meilleur choix",
         "Choix est un nom, donc « meilleur »."),
        ("C'est mieux de partir tôt",
         "Il n'y a pas de nom, donc « mieux »."),
    ], notes="Le test : y a-t-il un nom juste après ? Si oui, « meilleur ». La "
             "règle tient en une question et elle règle presque tous les cas.")

    d.pratique('Comparaison', "Complétez avec plus, moins, aussi, meilleur ou mieux",
               "À l'oral, puis à l'écrit.", [
        ("Le gîte est … cher que le camping.", "plus"),
        ("L'autocar est … pratique que le train.", "plus"),
        ("Le sentier du bord de l'eau est … long que celui de la montagne.", "moins"),
        ("En basse saison, on obtient un … prix.", "meilleur"),
        ("On dort … dans un gîte chauffé qu'en tente à cinq degrés.", "mieux"),
        ("Le train est … confortable, mais il arrive la nuit.", "plus"),
    ], corrige=True,
       notes="Faire relire chaque phrase complète en vérifiant l'accord de l'adjectif. "
             "La quatrième et la cinquième vont ensemble : elles montrent le test du "
             "nom en action.")

    d.regle("Comparer, puis choisir",
            "« X est plus … que Y, mais je prends Y parce que … »",
            precision="Une comparaison qui ne débouche sur aucun choix ne sert à "
                      "rien. Le « parce que » est la moitié du travail.",
            notes="Diapositive à photographier. C'est la structure demandée dans la "
                  "fiche de voyage de C4 et dans le courriel de E2.")

    d.piege("Énumérer sans conclure",
            "Le train est confortable. L'autocar est pratique. Le gîte est cher.",
            "Je prends l'autocar : il part le matin et j'arrive de jour.",
            "Trois phrases côte à côte ne font pas une comparaison. Ce qu'on "
            "attend, c'est une décision et sa raison — et c'est aussi ce qu'un "
            "employeur, un propriétaire ou un médecin attendent.",
            notes="Faire remarquer que c'est exactement ce que Thuy fait à la fin du "
                  "dialogue : « Alors l'autocar est plus pratique que le train, même "
                  "s'il est moins confortable. » Une phrase, un choix, une nuance.")

    d.pratique('Production', "Choisissez, et dites pourquoi",
               "Une phrase complète, à l'oral, chacun son tour.", [
        ("Le gîte ou le camping ?", "nommez le prix et la température"),
        ("L'autocar ou le train ?", "nommez l'heure d'arrivée"),
        ("Le sentier du bord de l'eau ou celui de la montagne ?", "nommez la longueur"),
        ("Le tarif ferme ou le tarif qui se change ?", "nommez ce que vous ignorez encore"),
        ("Partir six nuits ou trois nuits ?", "nommez ce que vous voulez voir"),
    ], corrige=True,
       notes="Exiger la structure complète : la comparaison, le choix, la raison. "
             "Refuser gentiment « je préfère le gîte » tout seul, et redemander : "
             "« pourquoi ? ». C'est le cœur du niveau 5.")

    d.billet(
        "Comparez deux façons de faire votre propre voyage, et dites laquelle vous choisissez.",
        exemples=[
            "Deux phrases : la comparaison, puis le choix et sa raison.",
            "Nommez aussi l'inconvénient que vous acceptez.",
        ],
        notes="Ramasser les billets. Ils entrent tels quels dans la fiche de voyage de "
              "C4 : rien n'est à réécrire, seulement à compléter.")

    return d.save(dossier)
