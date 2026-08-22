# -*- coding: utf-8 -*-
"""B4 · Qui, que, où - et les mots qui annoncent un exemple
Bloc B « Défi 1 · La chronique pratique » · couleur ambre · 75 min.
Source : exercices `t1rel` et `t1exempl`, mini-leçons « Qui, que, où : dire
long en une phrase » et « Les mots qui annoncent un exemple ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="Qui, que, où - et les mots qui annoncent un exemple",
        chapeau="Deux outils pour dire long sans s'essouffler : la phrase "
                "qui complète un nom, et le connecteur qui avertit qu'un "
                "exemple arrive. Les deux sont partout dans une chronique.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du Défi 1. Deux notions en une séance, c'est "
                  "beaucoup : prévoir quarante minutes pour les relatives et trente "
                  "pour les connecteurs, et ne pas hésiter à reporter les connecteurs "
                  "en C1 si le groupe peine.")

    d.objectifs([
        "réunir deux phrases en une avec « qui », « que » ou « où » ;",
        "employer « où » pour un moment, et pas seulement pour un lieu ;",
        "reconnaître à l'oral le mot qui annonce un exemple ;",
        "employer par exemple, ainsi, notamment, comme et prenons.",
    ], notes="Le deuxième objectif surprend toujours et il est très fréquent dans les "
             "journaux : le jour où, l'année où, le moment où.")

    d.declencheur(
        'Observation', "Comment dire les deux phrases en une seule ?",
        pistes=[
            "C'est une chronique. Elle passe le mardi.",
            "Voici la lettre. Elle a écrit cette lettre.",
            "Je me souviens du jour. Le commerçant a rappelé ce jour-là.",
            "Quel mot faut-il, et pourquoi pas le même dans les trois cas ?",
        ],
        notes="Laisser le groupe proposer. Beaucoup mettront « que » partout : c'est le "
              "point de départ de la leçon, pas une faute à corriger tout de suite.")

    d.tableau('Analyse', "Qui, que, où : le test qui tranche",
              ['Le mot', 'Quand l\'employer'],
              [["qui", "le verbe qui suit n'a pas de sujet : le technicien qui est venu"],
               ["que", "le verbe qui suit a son sujet, mais pas d'objet : la pièce qu'il a commandée"],
               ["où", "un lieu : l'endroit où on trouve les modèles"],
               ["où", "un moment : le jour où elle a téléphoné"]],
              cle=0,
              note="Enlève le mot et remets les deux phrases droites : ce qui manque te donne la réponse.",
              notes="Diapositive à photographier. Faire le test à voix haute sur les "
                    "trois phrases du déclencheur, une par une, avant de passer à "
                    "l'exercice.")

    d.regle("Déterminant, nom, puis la phrase qui le complète",
            "La lettre que j'ai écrite. Le jour où il a rappelé.",
            precision="C'est la structure que le programme du niveau 6 demande, et "
                      "c'est ce qui permet de dire long sans faire deux phrases "
                      "courtes. Un texte d'adulte tient debout par ces phrases-là ; "
                      "sans elles, on écrit comme au niveau 3, correctement mais par "
                      "petits morceaux.",
            notes="Diapositive à photographier. Dire au groupe que c'est le signe le "
                  "plus visible du passage au niveau 6, à l'écrit comme à l'oral.")

    d.pratique('Grammaire', "Une seule phrase au lieu de deux",
               "Complétez avec qui, que ou où.", [
        ("C'est une chronique ... passe le mardi.", "qui"),
        ("Voici la lettre ... elle a écrite.", "qu'"),
        ("Je me souviens du jour ... le commerçant a rappelé.", "où"),
        ("L'Office est un organisme ... ne prend pas ton dossier en main.", "qui"),
        ("C'est le site ... on trouve les modèles.", "où"),
        ("Mille neuf cent vingt-quatre est l'année ... les fabricants se sont entendus.", "où"),
    ], corrige=True, cols=2,
       notes="Le sixième prépare le documentaire de C3. Le faire remarquer : c'est "
             "l'année dont parlera la narratrice, au passé simple.")

    d.tableau('Analyse', "Cinq façons d'annoncer un exemple",
              ['Le connecteur', 'Ce qu\'il fait'],
              [["par exemple", "le plus simple, après une virgule, n'importe où"],
               ["ainsi", "le plus écrit : un cas qui démontre ce qu'on vient de dire"],
               ["notamment", "il y en a d'autres, je n'en nomme qu'un"],
               ["comme", "il rapproche de quelque chose de connu"],
               ["prenons, c'est le cas de", "on s'arrête et on raconte un cas entier"]],
              cle=0,
              note="À l'oral, le connecteur t'avertit : ce qui vient ne fait que répéter autrement.",
              notes="Diapositive à photographier. La note est la stratégie d'écoute la "
                    "plus payante du module : dès qu'un exemple s'annonce, l'élève peut "
                    "cesser de chercher une information nouvelle et respirer.")

    d.pratique('Grammaire', "Le mot qui annonce l'exemple",
               "Complétez. Chaque connecteur ne sert qu'une fois.", [
        ("Un appareil peut briser pour trois raisons. ... , il peut avoir été mal conçu.", "par exemple"),
        ("... une laveuse de sept cent quatre-vingts dollars qui cesse de vidanger.", "prenons"),
        ("Certains recours, ... les petites créances, ne demandent pas d'avocat.", "notamment"),
        ("Un organisme public ... l'Office répond gratuitement au téléphone.", "comme"),
        ("... , une photo de la facture prend trente secondes et peut tout changer.", "ainsi"),
        ("Beaucoup de dossiers se règlent avant l'audience. ... celui de madame Berthiaume.", "c'est le cas de"),
    ], corrige=True, cols=2,
       notes="Le cinquième est le plus difficile : « ainsi » veut aussi dire « de cette "
             "façon », et c'est la virgule qui distingue les deux emplois. Le dire "
             "avant la correction.")

    d.piege("Confondre les deux « ainsi »",
            "Ainsi il a rempli le formulaire et il l'a envoyé.",
            "Ainsi, une photo de la facture peut valoir des centaines de dollars.",
            "Sans virgule, « ainsi » veut dire « de cette façon » et décrit une manière. "
            "Avec la virgule et en tête de phrase, il annonce un exemple qui démontre. "
            "C'est le seul cas du module où un signe de ponctuation change le sens d'un "
            "mot - et c'est aussi ce qu'on a vu en A3 avec les guillemets.",
            notes="Faire le lien avec A3 explicitement : la ponctuation n'est pas "
                  "décorative. C'est le fil du bloc A qui se referme ici.")

    d.billet(
        "Écris une phrase avec « qui », « que » ou « où », sur ta propre semaine.",
        exemples=[
            "Par exemple : « le jour où j'ai reçu ma facture ».",
            "Une seule phrase, mais longue.",
        ],
        notes="Deux minutes. Le Défi 1 se termine ici : annoncer l'entrevue et le "
              "documentaire du Défi 2, et prévenir que le passé simple arrive.")

    return d.save(dossier)
