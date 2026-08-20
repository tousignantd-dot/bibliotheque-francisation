# -*- coding: utf-8 -*-
"""C2 · Situer sans montrer du doigt.
Bloc C · couleur ambre (écriture) · 75 min.
Source : mini-leçon `t2lieu`, exercice `t2lieu`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre='Situer sans montrer du doigt',
        chapeau="Expliquer un chemin en personne, c'est facile : on montre. Au "
                "téléphone ou par écrit, il faut des mots. Le français en a une "
                "dizaine, et ils suffisent à toute une ville.",
        duree='75 minutes')

    d.titre(notes="Commencer par une contrainte : demander à un élève d'expliquer un chemin "
                  "les mains dans les poches. La difficulté apparaît en dix secondes.")

    d.objectifs([
        "employer les quatre repères qui dirigent ;",
        "employer les trois repères qui décrivent ;",
        "situer dans un espace : au coin, au bout, au milieu ;",
        "éviter le piège du côté en donnant un repère fixe.",
    ])

    d.tableau('Analyse · 1 de 2', "Les quatre qui dirigent",
              ['Le repère', 'Ce que je fais'],
              [["tout droit", "je ne tourne nulle part"],
               ["à gauche / à droite", "je tourne"],
               ["en face de", "je change de côté de rue"],
               ["jusqu'à", "je marche puis j'arrête"]],
              cle=2,
              note="Sans ces quatre-là, aucun itinéraire n'est possible.",
              notes="Faire recopier. Ce sont les seuls dont on ne peut pas se passer.")

    d.tableau('Analyse · 2 de 2', "Les six qui situent",
              ['Le repère', 'Exemple'],
              [["devant / derrière", "devant la pharmacie"],
               ["à côté de", "à côté de la caisse"],
               ["au coin de", "au coin de deux rues"],
               ["au bout de", "au bout du corridor"],
               ["au milieu de", "au milieu du parc"],
               ["au-dessus de", "au-dessus de la porte"]],
              cle=0,
              notes="Tous se fusionnent : au coin DU parc, au bout DES escaliers. "
                    "La fusion revient pour la troisième fois du module — c'est voulu : "
                    "elle s'installe par répétition, pas par explication.")

    d.regle('Diriger et décrire',
            "Un bon itinéraire alterne les deux familles.",
            precision="Les repères qui dirigent tracent le chemin. Ceux qui décrivent "
                      "confirment qu'on ne s'est pas trompé. Un itinéraire qui ne fait que "
                      "décrire laisse la personne sur place ; un itinéraire qui ne fait que "
                      "diriger l'inquiète à chaque coin de rue.",
            notes="Reprendre le dialogue de C1 et faire classer chaque phrase. "
                  "L'alternance est presque parfaite.")

    d.piege('Le piège du côté',
            "C'est à votre droite. — Ma droite ou la vôtre ?",
            "C'est du côté de la pharmacie.",
            "« À droite » dépend de la personne qui marche, pas de celle qui parle. Quand "
            "vous expliquez, mettez-vous mentalement à la place de l'autre — ou mieux, "
            "donnez un repère fixe : la pharmacie, les numéros pairs, le parc. Un repère "
            "fixe ne se trompe jamais de côté.",
            notes="Faire l'expérience face à face : deux élèves, l'un explique « à droite ». "
                  "La confusion est immédiate.")

    d.pratique('Pratique · 1 de 2', "Le repère qui convient",
               "Complétez.", [
        ("Ne tournez nulle part, continuez ___.", "tout droit"),
        ("L'hôpital est juste ___ l'arrêt d'autobus.", "en face de"),
        ("L'enseigne est ___ la porte.", "au-dessus de"),
        ("Le sentier passe ___ parc.", "au milieu du"),
        ("L'escalier est ___ corridor.", "au bout du"),
        ("Vous allez passer ___ une pharmacie et une caisse.", "devant"),
    ], corrige=True,
       notes="Vérifier les fusions aux lignes 4 et 5 : au milieu DU, au bout DU.")

    d.pratique('Pratique · 2 de 2', "Dirige ou décrit ?",
               "Dites ce que fait chaque indication.", [
        ("Continuez tout droit jusqu'au feu.", "dirige"),
        ("Vous allez passer devant une caisse.", "décrit"),
        ("Tournez à gauche sur Chambly.", "dirige"),
        ("Il y a une petite enseigne au-dessus de la porte.", "décrit"),
        ("L'hôpital est juste en face.", "dirige"),
        ("Le stationnement est derrière l'édifice.", "décrit"),
    ], corrige=True,
       notes="La cinquième ligne se discute : « en face » dirige quand il dit où aller, "
             "décrit quand il situe. Accepter les deux si l'élève justifie.")

    d.cartes('Au téléphone', "Trois précautions", [
        ("Nommer le point de départ",
         "« Tu pars de l'école ? » — sans point de départ, aucun repère ne veut rien dire."),
        ("Donner des repères visibles de loin",
         "Un feu, un parc, une grande enseigne. Pas un numéro civique : personne ne le voit "
         "en marchant."),
        ("Faire répéter",
         "« Tu peux me le redire dans tes mots ? » C'est la seule façon de vérifier qu'on "
         "s'est fait comprendre."),
    ], notes="Ces trois précautions sont exactement ce que l'assistant demandera au jeu de "
             "rôle de E1. Le dire au groupe.")

    d.billet(
        "Expliquez par écrit, à quelqu'un au téléphone, comment venir de l'école chez vous.",
        exemples=[
            "Sans jamais employer « à droite » ou « à gauche » seuls : ajoutez un repère fixe.",
            "Cinq à six phrases.",
        ],
        notes="La contrainte est artificielle mais très formatrice. Corriger et rendre "
              "avant E1.")

    return d.save(dossier)
