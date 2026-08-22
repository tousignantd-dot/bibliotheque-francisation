# -*- coding: utf-8 -*-
"""B4 · Ce qui durait, et les mots qui placent un moment
Bloc B « Défi 1 · Le déroulement du film » · couleur ambre · 75 min.
Bilan du bloc. Source : exercices `t1imp`, `t1temps` et `t1ordre`, et leurs
mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="Ce qui durait, et les mots qui placent un moment",
        chapeau="Le passé composé fait avancer l'histoire ; l'imparfait la "
                "fait tenir. Et six marqueurs de temps suffisent à placer "
                "n'importe quelle scène.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du Défi 1. Elle referme la chronologie du film et "
                  "prépare la biographie du Défi 2, qui pose les mêmes questions sur "
                  "un texte écrit.")

    d.objectifs([
        "employer l'imparfait pour une action en cours dans le passé ;",
        "partager le travail entre imparfait et passé composé ;",
        "placer une scène avec un marqueur de temps précis ;",
        "remettre les trois jours du film dans l'ordre de l'histoire.",
    ], notes="Le quatrième objectif est l'exercice de synthèse du bloc : si le groupe "
             "le réussit, le Défi 1 est acquis.")

    d.declencheur(
        'Observation', "Qu'est-ce qui durait, et qu'est-ce qui est arrivé ?",
        pistes=[
            "« Elle vidait la cuisine quand le téléphone a sonné. »",
            "Laquelle des deux actions a duré le plus longtemps ?",
            "Essaie de mettre « pendant que » devant l'une des deux.",
            "Que se passe-t-il si on échange les deux temps ?",
        ],
        notes="La dernière piste vaut la démonstration : « elle a vidé la cuisine "
              "quand le téléphone sonnait » ne raconte plus la même scène du tout.")

    d.tableau('Analyse', "Deux temps, deux métiers",
              ['Le temps', 'Ce qu\'il fait dans le récit'],
              [["imparfait", "le décor, ce qui durait : elle vidait la cuisine"],
               ["passé composé", "l'événement : le téléphone a sonné"],
               ["plus-que-parfait", "ce qui était déjà fait : elle avait pris l'autobus"],
               ["le test", "si « pendant que » passe devant, c'est l'imparfait"]],
              cle=0,
              note="La quatrième ligne est un test, pas une règle : elle ne se retient pas, elle s'utilise.",
              notes="Diapositive à photographier. Les trois temps du récit sont "
                    "maintenant réunis sur une seule diapositive : c'est la référence "
                    "du bloc.")

    d.regle("Avec ou sans « être en train de »",
            "« Elle lisait » et « elle était en train de lire » disent la même chose.",
            precision="La forme longue insiste davantage, et elle est plus fréquente à "
                      "l'oral. Aucune des deux n'est plus correcte que l'autre. Ce "
                      "qu'il faut savoir, c'est qu'elles s'équivalent : entendre l'une "
                      "et écrire l'autre ne change rien au sens.",
            notes="Diapositive à photographier. Rassurer : beaucoup d'élèves croient "
                  "que la forme longue est une faute de débutant. Elle ne l'est pas.")

    d.tableau('Analyse', "Six marqueurs qui placent un moment",
              ['Le marqueur', 'Ce qu\'il dit'],
              [["la veille", "le jour d'avant celui dont on parle"],
               ["le lendemain", "le jour d'après"],
               ["trois semaines plus tôt", "une distance mesurée vers l'arrière"],
               ["depuis deux jours", "ça a commencé et ça continue"],
               ["dès son arrivée", "le point de départ exact"],
               ["avant, tout seul", "avant quoi ? - il ne place rien"]],
              cle=0,
              notes="Diapositive à photographier. La dernière ligne est celle qui "
                    "corrige le plus de copies : « avant » sans repère ne dit rien.")

    d.pratique('Grammaire', "Imparfait ou passé composé ?",
               "Complétez avec le temps qui convient.", [
        ("Pendant que la mère parlait, elle ... les sous-titres.", "lisait"),
        ("Elle ... des boîtes quand le téléphone a sonné.", "faisait"),
        ("Le vent ... depuis deux jours quand le bateau est parti.", "soufflait"),
        ("Chaque fois que l'image changeait, la musique ...", "s'arrêtait"),
        ("Elle arrive le vendredi soir ; ..., elle vide la cuisine.", "le lendemain"),
        ("Elle n'avait pas revu la voisine ... quarante ans.", "depuis"),
    ], corrige=True, cols=2,
       notes="Les deux derniers items changent de nature : ils portent sur les "
             "marqueurs, pas sur les temps. Le dire avant de commencer.")

    d.pratique('Compréhension', "Remettez les trois jours dans l'ordre",
               "Numérotez de 1 à 6, selon l'ordre de l'histoire.", [
        ("Une lettre est écrite, trois semaines avant le départ du bateau.", "1"),
        ("Estelle prend l'autobus du matin, qui tombe en panne à Matane.", "2"),
        ("Elle arrive au village et ouvre la maison de sa mère.", "3"),
        ("Elle vide la cuisine et trouve la lettre dans le tiroir.", "4"),
        ("Elle va frapper chez la voisine, celle qui savait.", "5"),
        ("Le ciné-club reste une demi-heure à discuter du film.", "6"),
    ], corrige=True,
       notes="Exercice de synthèse du bloc. Faire remarquer que l'ordre du film n'est "
             "pas celui-là : c'est l'ordre de l'histoire, celui qu'on emploie pour "
             "raconter à quelqu'un.")

    d.billet(
        "Raconte en trois phrases ce qui se passe le samedi, dans l'ordre.",
        exemples=[
            "Trois phrases, pas plus.",
            "Emploie au moins un plus-que-parfait.",
        ],
        notes="Trois minutes. C'est la première production du module, en miniature. "
              "Ramasser : ces billets préparent le compte rendu oral de E1.")

    return d.save(dossier)
