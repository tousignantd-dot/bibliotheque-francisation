# -*- coding: utf-8 -*-
"""B4 · Ce sandwich-là, c'est quoi ?
Bloc B « Défi 1 · Lire le menu » · couleur ambre · 75 min.
Source : exercice `t1ce`, mini-leçon `t1ce`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="Ce sandwich-là, c'est quoi ?",
        chapeau="Il arrive qu'on voie ce qu'on veut sans savoir comment ça "
                "s'appelle. Une phrase règle ça, et elle tient en cinq mots.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire et de stratégie. Le point de langue est un moyen "
                  "de contourner un trou de vocabulaire : c'est ce qui le rend précieux "
                  "à ce niveau-ci.")

    d.objectifs([
        "employer ce, cet, cette et ces devant un nom ;",
        "ajouter le « -là » qui montre du doigt ;",
        "poser une question sur un plat sans connaître son nom ;",
        "écrire les quatre formes sans faute.",
    ])

    d.regle("Montrer plutôt que nommer",
            "« Ce sandwich-là, c'est quoi ? »",
            precision="C'est une stratégie, pas un pis-aller. Un élève qui "
                      "montre du doigt et pose la question obtient le nom du "
                      "plat, et il l'apprend en situation. Un élève qui se tait "
                      "prend au hasard.",
            notes="Diapo à photographier. Le dire clairement au groupe : montrer du "
                  "doigt n'est pas impoli au comptoir, c'est ce que tout le monde fait.")

    d.tableau('Analyse', "Les quatre formes",
              ['Devant un mot…', 'On écrit', 'Exemple'],
              [["masculin", "ce", "ce sandwich, ce trio"],
               ["qui commence par une voyelle", "cet", "cet accompagnement"],
               ["féminin", "cette", "cette soupe, cette portion"],
               ["au pluriel", "ces", "ces frites, ces breuvages"]],
              cle=1,
              note="« Cet » et « cette » se prononcent pareil : la différence est écrite.",
              notes="Diapo à photographier. Faire dire « cet » et « cette » l'un après "
                    "l'autre : le groupe entend qu'il n'y a aucune différence. C'est "
                    "rassurant à l'oral et exigeant à l'écrit.")

    d.regle("Le petit -là du Québec",
            "cette soupe-là  ·  ce trio-là",
            precision="Le trait d'union est obligatoire à l'écrit et le « -là » "
                      "se prononce un peu plus fort que le reste. Sans trait "
                      "d'union, « là » veut dire l'endroit, ce qui n'est pas la "
                      "même phrase.",
            notes="Diapo à photographier. Faire écrire trois exemples au tableau, avec "
                  "le trait d'union bien visible.")

    d.pratique('Écriture', "Ce, cet, cette ou ces ?",
               "Complétez la question.", [
        ("___ sandwich-là, c'est quoi ?", "Ce"),
        ("___ soupe est-elle aux légumes ?", "Cette"),
        ("Je voudrais ___ trio, s'il vous plaît.", "ce"),
        ("___ accompagnement est compris dans le prix ?", "Cet"),
        ("___ breuvages sont dans la colonne du bas.", "Ces"),
        ("___ portion est trop grande pour moi.", "Cette"),
    ], corrige=True,
       notes="Faire écrire dans le cahier avant de corriger. Demander à chaque fois le "
             "genre du nom, à voix haute.")

    d.piege("Écrire « cet » devant un mot féminin",
            "cet soupe",
            "cette soupe",
            "Comme les deux formes se prononcent exactement pareil, l'oreille ne peut "
            "pas trancher : il faut connaître le genre du nom. C'est une raison de plus "
            "d'apprendre chaque mot avec son article, dès la première fois qu'on le voit.",
            notes="Rappeler la séance A3 : « une serviette », « un plateau ». Les mots "
                  "appris avec leur article ne posent pas ce problème.")

    d.cartes("Quatre questions à poser en montrant", "À apprendre par cœur", [
        ("Ce sandwich-là, c'est quoi ?",
         "Quand on ne connaît pas le nom du plat. Le préposé le donne, et on l'apprend "
         "sur place."),
        ("Cette soupe-là, c'est combien ?",
         "Quand le prix n'est pas lisible d'où on est, ou quand la ligne porte trois "
         "chiffres et qu'on ne sait pas lequel prendre."),
        ("Cet accompagnement est compris ?",
         "Quand la ligne « servi avec » n'est pas visible. La réponse est presque "
         "toujours oui."),
        ("Je voudrais ce trio-là, s'il vous plaît.",
         "La commande la plus simple du module : on montre, on demande poliment, et "
         "c'est fini."),
    ], notes="Faire jouer les quatre questions debout, en montrant le tableau du menu "
             "projeté. Le geste et la phrase ensemble.")

    d.pratique('Production orale', "Montrez et demandez",
               "Une question par plat, en montrant du doigt.", [
        ("un plat que vous ne connaissez pas", "Ce plat-là, c'est quoi ?"),
        ("une soupe dont vous voulez le prix", "Cette soupe-là, c'est combien ?"),
        ("un accompagnement", "Cet accompagnement est compris ?"),
        ("le trio que vous choisissez", "Je voudrais ce trio-là, s'il vous plaît."),
    ], corrige=True,
       notes="Chaque élève passe une fois. Corriger la forme du déterminant et rien "
             "d'autre : le reste vient au bloc C.")

    d.billet(
        "Écrivez quatre questions à poser devant un menu.",
        exemples=[
            "Une avec ce, une avec cet, une avec cette, une avec ces.",
            "Ajoutez le « -là » à deux d'entre elles.",
        ],
        notes="Fin du bloc B. Ces quatre questions seront utilisées telles quelles dans "
              "le jeu de rôle du bloc E.")

    return d.save(dossier)
