# -*- coding: utf-8 -*-
"""B2 · Ce titre-là, cette carte-là.
Bloc B « Défi 1 · Comprendre ce qu'on me répond » · couleur ambre · 75 min.
Source : exercice `t1demons` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre='Ce titre-là, cette carte-là',
        chapeau="Devant une grille affichée, on ne connaît pas le nom de tout. "
                "Quatre petits mots remplacent le doigt qui montre.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire. Ouvrir en montrant un objet de la classe sans le "
                  "nommer : « Passez-moi ça, là. » Demander au groupe comment on dit ça "
                  "correctement. La réponse est le sujet de la séance.")

    d.objectifs([
        "choisir entre ce, cet, cette et ces devant un nom ;",
        "employer cet devant un mot qui commence par une voyelle ;",
        "ajouter -là pour montrer une chose précise ;",
        "poser une question sur un titre qu'on ne sait pas nommer.",
    ])

    d.regle("Le mot qui remplace le doigt",
            "« Combien coûte ce titre-là ? »",
            precision="Quand on ne connaît pas le nom exact de ce qu'on voit sur "
                      "la grille, on le montre. Ces quatre petits mots servent "
                      "exactement à cela : désigner la chose qu'on a sous les "
                      "yeux, sans avoir à la nommer.",
            notes="Diapositive à photographier. C'est la phrase la plus utile du bloc B : "
                  "elle permet de poser une question sur n'importe quelle ligne de la "
                  "grille, même sans en connaître le vocabulaire.")

    d.tableau('Analyse', "Les quatre formes",
              ["On dit", "Quand"],
              [["ce titre", "devant un mot masculin"],
               ["cet autobus", "devant une voyelle"],
               ["cette carte", "devant un mot féminin"],
               ["ces titres", "devant un pluriel, masculin ou féminin"]],
              cle=0,
              note="Au pluriel, plus de choix : c'est « ces » dans tous les cas.",
              notes="Diapositive à photographier. Faire trouver le genre en essayant "
                    "« un » ou « une » : un titre, une carte. C'est la seule méthode "
                    "fiable et elle marche toujours.")

    d.tableau('Analyse', "Le « -là » qu'on ajoute au Québec",
              ["À l'écrit", "Ce que ça veut dire"],
              [["ce titre-là", "celui que je montre du doigt"],
               ["cette carte-là", "celle-ci, pas une autre"],
               ["ces prix-là", "ceux qui sont affichés devant nous"]],
              cle=0,
              note="Le trait d'union est obligatoire à l'écrit.",
              notes="Diapositive à photographier. À l'oral, le « -là » s'entend dans "
                    "presque toutes les phrases du guichet. Un élève qui ne l'emploie "
                    "pas sera compris, mais un élève qui ne le comprend pas manquera la "
                    "moitié de ce qu'on lui dit.")

    d.piege('Grammaire',
            "« ce autobus-là »",
            "« cet autobus-là »",
            "Deux voyelles ne se suivent pas facilement en français. Devant un mot "
            "masculin qui commence par une voyelle, on ajoute un t : ce-t-autobus. "
            "Le mot reste masculin, c'est seulement sa forme qui change.",
            notes="Faire chercher au groupe d'autres mots masculins à voyelle : "
                  "appareil, argent, horaire, escalier, arrêt. Tous prennent « cet ».")

    d.piege('Orthographe',
            "« ses prix-là »",
            "« ces prix-là »",
            "Deux mots différents, exactement le même son. « ces » montre du "
            "doigt : ces prix, là, sur la grille. « ses » dit à qui c'est : ses "
            "prix à lui. Si on peut remplacer par « ces… -là », c'est « ces ».",
            notes="Piège d'écriture, pas d'oral. Il reviendra dans la production écrite "
                  "de la séance E2. Donner l'astuce du « -là » comme test.")

    d.pratique('Grammaire', "Ce, cet, cette ou ces ?",
               "Complétez chaque phrase.", [
        ("Combien coûte ___ titre-là ?", "ce"),
        ("Est-ce que ___ carte-là est encore bonne ?", "cette"),
        ("___ autobus-là va vers le nord.", "Cet"),
        ("Je ne comprends pas ___ prix-là.", "ces"),
        ("___ zone-là, c'est la zone A.", "Cette"),
        ("___ deux titres-là coûtent le même prix.", "Ces"),
    ], corrige=True, cols=2,
       notes="C'est l'exercice 3 du défi 1. Faire justifier chaque réponse par le genre "
             "et le nombre du nom qui suit, jamais par l'habitude.")

    d.pratique('Répétition', "Six phrases du comptoir",
               "Écoutez, puis répétez en gardant le -là.", [
        ("Combien coûte ce titre-là ?", "masculin"),
        ("Est-ce que cette carte-là est encore bonne ?", "féminin"),
        ("Cet autobus-là va vers le nord.", "voyelle"),
        ("Je ne comprends pas ces prix-là.", "pluriel"),
        ("Cette zone-là, c'est la zone A.", "féminin"),
        ("Ces deux titres-là coûtent le même prix.", "pluriel"),
    ], corrige=True,
       notes="Répétition en chœur puis individuellement. Faire accompagner chaque "
             "phrase d'un geste de la main vers un point de la classe : le geste "
             "installe le sens du « -là » mieux qu'une explication.")

    d.billet(
        "Écrivez trois questions que vous poseriez devant une grille des tarifs.",
        exemples=[
            "Combien coûte ce ___ -là ?",
            "Est-ce que cette ___ -là est ___ ?",
        ],
        notes="Devoir court. Les questions produites servent de matière première à la "
              "séance C2, où l'on travaillera la forme interrogative elle-même.")

    return d.save(dossier)
