# -*- coding: utf-8 -*-
"""B2 · Moins huit, plus quatre.
Bloc B « Défi 1 · Le bulletin du matin » · couleur ambre · 75 min.
Source : dialogue `t1b`, exercices `t1degre`, `t1saison` et `t1notes`,
mini-leçons « Lire une température au Québec », « En hiver, au printemps » et
« Prendre un bulletin météo en note ».

B1 a fait attraper trois choses dans un bulletin. B2 s'occupe de la seule des
trois qui demande vraiment un apprentissage : le nombre, et le petit mot qui
le précède. « Moins huit » et « plus huit » séparent deux journées qui n'ont
rien à voir, et un élève qui n'entend pas le signe s'habille de travers.

Le reste de la séance installe le calendrier : les quatre saisons, et le
« au » du printemps qui est la seule exception. Elle se termine par la fiche
de notes — trois lignes dans un carnet, la stratégie de tout le module.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-neige/vocab/')


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre="Moins huit, plus quatre",
        chapeau="Lire une température au-dessus et au-dessous de zéro, et "
                "nommer la saison.",
        duree='75 minutes')

    d.titre(notes="Ramasser d'abord les carnets du devoir de B1 : trois lignes par "
                  "élève. Lire deux ou trois carnets à voix haute — c'est le "
                  "déclencheur le moins cher et le plus juste.")

    d.objectifs([
        "dire une température sous zéro : moins huit ;",
        "dire une température au-dessus de zéro : plus quatre ;",
        "nommer les quatre saisons ;",
        "écrire un bulletin en trois lignes dans son carnet.",
    ])

    d.declencheur(
        'Observation', "Zéro degré : qu'est-ce que ça change dehors ?",
        image=IMG + 'temperature.jpg',
        pistes=[
            "Qu'est-ce qu'on voit sur le thermomètre ?",
            "À zéro degré, est-ce que la neige reste par terre ?",
            "Et à plus quatre ?",
            "Dans votre pays, il fait combien en janvier ?",
        ],
        notes="La quatrième piste vaut de l'or dans un groupe de niveau 2 : chacun "
              "donne un nombre, et l'écart avec moins vingt fait le reste du cours.")

    d.regle("Le signe se dit avant le nombre",
            "Moins huit. Plus quatre.",
            precision="Zéro est la ligne : l'eau y gèle. En dessous, on dit "
                      "« moins » ; au-dessus, on dit « plus », ou seulement le "
                      "nombre. Et plus le nombre est grand après « moins », plus "
                      "il fait froid : moins vingt est pire que moins huit.",
            notes="Diapositive à photographier. Dessiner une ligne graduée au tableau "
                  "avec zéro au milieu et y placer les nombres du groupe.")

    d.tableau('Analyse', "Ce qu'on entend, ce que ça veut dire",
              ["On entend", "Dehors"],
              [["moins vingt", "Très froid. Tuque, mitaines, foulard."],
               ["moins huit", "Froid. Il neige, la neige reste."],
               ["zéro degré", "L'eau gèle. Le trottoir est glissant."],
               ["plus quatre", "La neige fond. Il pleut souvent."],
               ["plus trente", "C'est l'été. On ne dit même plus « plus »."]],
              cle=1,
              note="Cinq nombres, cinq façons de s'habiller.",
              notes="Diapositive à photographier. Faire relire la colonne de droite "
                    "par cinq élèves différents, un par rangée.")

    d.pratique('Pratique · 1', "Moins ou plus ?",
               "Dites la température à voix haute, puis écrivez le mot.", [
        ("−8 degrés", "moins huit"),
        ("+25 degrés", "plus vingt-cinq"),
        ("−16 degrés", "moins seize"),
        ("+4 degrés", "plus quatre"),
        ("−30 degrés", "moins trente"),
        ("Il fait −2.", "Il fait moins deux degrés."),
    ], corrige=True, cols=2,
       notes="Faire dire avant de faire écrire. Le mot « moins » se perd à l'oral "
             "quand on le lit sans l'avoir prononcé.")

    d.dialogue('Dialogue', "À Québec, il fait plus froid", [
        ("ZINA", "Monsieur Pelchat, ma sœur habite à Québec.", True),
        ("ROLAND", "Ah oui ? Il fait plus froid là-bas. Ce matin, moins seize.", True),
        ("ZINA", "Moins seize ! C'est beaucoup.", True),
        ("ROLAND", "Et en Gaspésie, il vente très fort.", True),
        ("ZINA", "Et l'été ? Il fait chaud au Québec ?", True),
        ("ROLAND", "En juillet, il fait vingt-cinq, trente degrés.", True),
    ], consigne="Écoutez, puis notez les trois nombres que vous entendez.",
       notes="Trois nombres à attraper : moins seize, vingt-cinq, trente. Faire "
             "comparer les carnets deux par deux avant de corriger.")

    d.regle("Une seule saison prend « au »",
            "En hiver, en été, en automne — mais au printemps.",
            precision="Il n'y a pas de règle derrière : il faut l'apprendre par "
                      "cœur, comme les autres apprennent « au Québec ». Devant un "
                      "mois, c'est toujours « en » : en janvier, en juillet.",
            notes="Diapositive à photographier. Un seul mot à retenir dans toute la "
                  "diapositive : « au printemps ». Le faire répéter quatre fois.")

    d.vocabulaire('Vocabulaire', "Les quatre saisons du Québec", [
        ("l'hiver", "De décembre à mars. Neige, glace, souvent moins vingt."),
        ("le printemps", "Avril et mai. La neige fond, il pleut beaucoup."),
        ("l'été", "De juin à août. Vingt-cinq, trente degrés, mais court."),
        ("l'automne", "Septembre et octobre. La température descend, et il pleut."),
    ], notes="Diapositive à photographier. Demander à chacun quelle saison ressemble "
             "le plus à son pays : la réponse est souvent « aucune ».")

    d.pratique('Pratique · 2', "En hiver, au printemps",
               "Complétez avec « en » ou « au ».", [
        ("___ hiver, il neige beaucoup.", "En"),
        ("___ printemps, la neige fond.", "Au"),
        ("___ été, il fait trente degrés.", "En"),
        ("___ automne, il pleut souvent.", "En"),
        ("___ janvier, il fait très froid.", "En"),
        ("La première neige tombe ___ novembre.", "en"),
    ], corrige=True, cols=2,
       notes="Une seule bonne réponse est « Au ». Demander au groupe de la trouver "
             "avant de corriger : c'est l'exception, et elle se retient mieux ainsi.")

    d.pratique('Pratique · 3', "Ma fiche de notes",
               "Réécoutez le bulletin de B1 et remplissez les cinq lignes.", [
        ("Ville", "Montréal"),
        ("Aujourd'hui, temps", "neige"),
        ("Aujourd'hui, température", "moins 8"),
        ("Demain, temps", "soleil"),
        ("Demain, température", "moins 2"),
    ], corrige=True, cols=1,
       notes="C'est la fiche de l'exercice `t1notes` du module. Faire écrire les "
             "chiffres tout de suite, pendant l'écoute : un nombre entendu s'oublie "
             "en dix secondes.")

    d.billet(
        "Notez la température de trois matins de suite, avec le signe.",
        exemples=[
            "Lundi : moins 8",
            "Mardi : moins 2",
            "Mercredi : plus 1",
        ],
        notes="Trois lignes, pas plus. Comparer les trois nombres au début de C1 : "
              "c'est ce qui amène la question des vêtements.")

    return d.save(dossier)
