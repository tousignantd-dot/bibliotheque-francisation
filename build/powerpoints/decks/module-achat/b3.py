# -*- coding: utf-8 -*-
"""B3 · Ce modèle-ci, celui-là.
Bloc B · couleur ambre (écriture) · 75 min.
Source : mini-leçon `t1demo`, exercice `t1demo`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre='Ce modèle-ci, celui-là',
        chapeau="Devant deux appareils presque identiques, il faut désigner "
                "l'un plutôt que l'autre. Le français a deux outils — et il ne "
                "faut pas les mélanger.",
        duree='75 minutes')

    d.titre(notes="Poser deux objets identiques sur la table, à distance l'un de l'autre. "
                  "Toute la leçon se joue là.")

    d.objectifs([
        "employer ce, cet, cette, ces devant un nom ;",
        "employer celui, celle, ceux, celles à la place d'un nom ;",
        "distinguer -ci et -là ;",
        "reprendre un nom par un autre pour ne pas se répéter.",
    ])

    d.tableau('Analyse', "Accompagner, ou remplacer",
              ['', 'Accompagne le nom', 'Remplace le nom'],
              [["Masculin", "ce modèle · cet appareil", "celui"],
               ["Féminin", "cette laveuse", "celle"],
               ["Pluriel", "ces modèles", "ceux, celles"]],
              cle=1,
              note="Le test : le nom est-il écrit juste après ? Si oui, ce/cet/cette.",
              notes="Diapo centrale. Faire recopier. Le test de la note règle tous les cas.")

    d.regle("cet, devant une voyelle",
            "« cet appareil », jamais « ce appareil ».",
            precision="<b>cet</b> existe précisément pour éviter la rencontre de deux "
                      "voyelles : cet appareil, cet écran, cet homme. Devant une consonne, "
                      "c'est <b>ce</b> : ce modèle, ce magasin.",
            notes="Faire produire cinq exemples de chaque par le groupe. La règle est "
                  "mécanique et se retient vite.")

    d.regle("Jamais celui tout seul",
            "-là, -ci, qui, que ou de : il faut toujours une suite.",
            precision="« celui-là », « celui de gauche », « celui qui consomme le moins ». "
                      "« Celui » seul ne veut rien dire. Dans le doute, employez <b>-là</b> : "
                      "c'est toujours correct.",
            notes="Si le groupe a fait le module des déplacements, c'est un rappel : la "
                  "règle y était déjà.")

    d.cartes('-ci et -là', "Deux choses côte à côte", [
        ("-ci désigne le plus proche",
         "« Ce modèle-ci » : celui devant lequel on se tient."),
        ("-là désigne le plus éloigné",
         "« Celui-là » : l'autre, plus loin dans le rayon."),
        ("À l'oral, -là l'emporte",
         "Beaucoup de gens emploient « celui-là » pour les deux, en montrant du doigt. Ce "
         "n'est pas une faute, c'est l'usage courant."),
    ], notes="Rassurer : la distinction -ci / -là est nette à l'écrit, floue à l'oral. Les "
             "élèves n'ont pas à s'en inquiéter en parlant.")

    d.regle("Reprendre par un autre nom",
            "« la laveuse » devient « l'appareil », « le modèle », « la machine ».",
            precision="C'est ce que fait le vendeur pour ne pas répéter le même mot. "
                      "<b>appareil</b> est général, <b>modèle</b> désigne une version "
                      "précise, <b>machine</b> est familier. Les alterner allège beaucoup "
                      "un texte.",
            notes="Faire relever les trois mots dans le dialogue de B1. Le vendeur les "
                  "emploie tous.")

    d.piege("Mélanger les deux outils",
            "Celui modèle est plus économe.",
            "Ce modèle est plus économe. / Celui-là est plus économe.",
            "Soit le nom est là, et on emploie <b>ce</b>. Soit il disparaît, et on emploie "
            "<b>celui</b>. Jamais les deux ensemble — c'est comme dire « le il ».",
            notes="Faire produire les deux formes correctes par deux élèves différents.")

    d.pratique('Pratique · 1 de 2', "Accompagner ou remplacer ?",
               "Complétez.", [
        ("Quelle est la différence entre ___ modèle-ci et celui-là ?", "ce"),
        ("___ appareil est plus économe que l'autre.", "Cet"),
        ("___ laveuse fait soixante-huit centimètres.", "Cette"),
        ("___ deux modèles se ressemblent beaucoup.", "Ces"),
        ("Prenez ___ de gauche : il entre partout.", "celui"),
        ("___ est trop large pour votre local.", "Celle-là"),
    ], corrige=True,
       notes="Faire dire à chaque ligne : le nom est-il écrit après ?")

    d.pratique('Pratique · 2 de 2', "Supprimez la répétition",
               "Récrivez la deuxième phrase.", [
        ("Prenez la laveuse. La laveuse de gauche entre partout.", "Prenez celle de gauche."),
        ("Regardez ce modèle. Ce modèle consomme le moins.", "Celui-là consomme le moins."),
        ("Les deux appareils se ressemblent. Les appareils ont la même garantie.", "Les deux ont la même garantie."),
        ("J'aime cette laveuse. Cette laveuse est silencieuse.", "Celle-ci est silencieuse."),
    ], corrige=True, cols=1,
       notes="Plusieurs récritures sont bonnes. Ce qui compte est que la répétition "
             "disparaisse.")

    d.billet(
        "Comparez deux appareils en cinq phrases, sans jamais répéter leur nom.",
        exemples=[
            "Employez ce/cet/cette une fois, celui/celle deux fois.",
            "Reprenez au moins une fois par un autre nom : l'appareil, le modèle.",
        ],
        notes="Corriger surtout le mélange des deux outils. Rendre avant E1.")

    return d.save(dossier)
