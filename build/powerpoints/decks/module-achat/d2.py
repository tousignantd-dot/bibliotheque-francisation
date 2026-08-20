# -*- coding: utf-8 -*-
"""D2 · Le tableau des problèmes.
Bloc D · couleur ambre (écriture) · 75 min.
Source : dialogue `t3b`, exercices `t3probleme` et `t3b`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre='Le tableau des problèmes',
        chapeau="Deux colonnes à la fin du livret : le problème à gauche, quoi "
                "vérifier à droite. Neuf appels de service sur dix s'y règlent "
                "— et un déplacement coûte quatre-vingt-dix dollars.",
        duree='75 minutes')

    d.titre(notes="Séance très concrète. Si vous avez apporté un livret, ouvrez-le à cette "
                  "page dès le début et laissez-la affichée.")

    d.objectifs([
        "lire un tableau à deux colonnes ;",
        "vérifier trois choses avant d'appeler le service ;",
        "décrire un problème avec précision ;",
        "savoir quand il ne faut PAS vérifier soi-même.",
    ])

    d.dialogue('Dialogue · 1 de 2', "Le problème", [
        ("YIN", "Elle vibre beaucoup à l'essorage. J'ai regardé le tableau.", True),
        ("THÉRÈSE", "Qu'est-ce qu'il dit ?", False),
        ("YIN", "Trois choses : vérifier les boulons de transport, vérifier que l'appareil est de niveau, répartir le linge.", True),
        ("THÉRÈSE", "Tu as enlevé les boulons ?", False),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Yin a déjà fait la bonne chose : elle a consulté le tableau avant d'appeler. "
             "Le souligner.")

    d.dialogue('Dialogue · 2 de 2', "La cause", [
        ("YIN", "Oui, le technicien les a enlevés. Et le plancher est droit.", False),
        ("THÉRÈSE", "Alors c'est le linge. Tu as mis quoi dedans ?", True),
        ("YIN", "Deux serviettes de bain, rien d'autre.", True),
        ("THÉRÈSE", "C'est ça. Deux serviettes se collent d'un côté et le tambour tourne de travers. Ajoute des petites pièces.", True),
    ], notes="Le raisonnement est un diagnostic : on élimine les causes une à une. C'est "
             "exactement ce que fait le tableau.")

    d.tableau('Analyse', "Le tableau, en pratique",
              ['Le problème', 'Quoi vérifier'],
              [["L'appareil vibre fort", "boulons, niveau, répartition du linge"],
               ["L'eau ne se vide pas", "le tuyau n'est ni plié ni bouché"],
               ["L'appareil ne démarre pas", "la porte est fermée, l'appareil branché"],
               ["Le linge sort trempé", "la brassée n'est pas trop petite"]],
              cle=0,
              note="Trois causes possibles pour le premier problème : on les élimine dans l'ordre.",
              notes="Diapo centrale. Faire recopier : ce sont les quatre problèmes les plus "
                    "fréquents d'une laveuse.")

    d.regle("Éliminer les causes dans l'ordre",
            "Le tableau les donne de la plus fréquente à la plus rare.",
            precision="Pour une vibration : les boulons d'abord (le plus fréquent sur un "
                      "appareil neuf), le niveau ensuite, la répartition du linge en "
                      "dernier. Suivre l'ordre du tableau fait gagner du temps.",
            notes="C'est une méthode de diagnostic, transférable à beaucoup d'autres "
                  "appareils.")

    d.cartes("Décrire un problème avec précision", "Trois éléments", [
        ("Quand ça arrive",
         "« À l'essorage », « au démarrage », « après cinq minutes ». Le moment oriente "
         "vers la cause."),
        ("Ce qu'on observe",
         "« Elle vibre », « l'eau ne se vide pas », « ça sent le brûlé ». Un fait, pas une "
         "interprétation."),
        ("Ce qu'on a déjà vérifié",
         "« J'ai regardé les boulons et le niveau. » C'est ce qui fait gagner le plus de "
         "temps au téléphone avec le service."),
    ], notes="Ces trois éléments sont exactement ce que la production écrite de E1 demande. "
             "Le dire.")

    d.piege("Appeler avant de vérifier",
            "Elle vibre, j'appelle le service.",
            "Elle vibre. Le tableau dit de vérifier trois choses. Je commence par là.",
            "Un déplacement de technicien coûte environ quatre-vingt-dix dollars, et si la "
            "cause est la répartition du linge, il ne fera rien de plus que vous. Cinq "
            "minutes de vérification contre quatre-vingt-dix dollars.",
            notes="Le calcul est le meilleur argument. L'écrire au tableau.")

    d.regle("Quand il ne faut PAS vérifier soi-même",
            "Odeur de brûlé, fumée, choc électrique : on débranche et on appelle.",
            precision="Le tableau des problèmes couvre les pannes ordinaires. Tout ce qui "
                      "touche à la chaleur, à la fumée ou à l'électricité sort de son "
                      "domaine. Dans ces cas-là, on débranche l'appareil et on appelle — "
                      "sans rien ouvrir.",
            notes="Diapo à photographier. C'est la limite de la séance, et elle est "
                  "importante.")

    d.pratique('Pratique · 1 de 2', "Quoi vérifier ?",
               "Donnez la première chose à regarder.", [
        ("L'appareil vibre fort à l'essorage", "les boulons de transport"),
        ("L'eau ne se vide pas", "le tuyau, plié ou bouché"),
        ("L'appareil ne démarre pas", "la porte fermée, l'appareil branché"),
        ("Le linge sort encore trempé", "la brassée, trop petite ou mal répartie"),
        ("Il y a une odeur dans le tambour", "un cycle à vide à l'eau chaude"),
        ("Ça sent le brûlé", "on débranche et on appelle — rien d'autre"),
    ], corrige=True,
       notes="La dernière ligne est celle qui compte le plus. La faire dire à voix haute "
             "par le groupe.")

    d.pratique('Pratique · 2 de 2', "Décrivez le problème",
               "Écrivez une phrase précise pour le service.", [
        ("La laveuse bouge beaucoup pendant le dernier cycle", "Elle vibre fort à l'essorage. J'ai vérifié les boulons et le niveau."),
        ("L'eau reste dans le tambour à la fin", "L'eau ne se vide pas en fin de cycle. Le tuyau n'est pas plié."),
        ("Rien ne se passe quand j'appuie", "L'appareil ne démarre pas. La porte est fermée et il est branché."),
    ], corrige=True, cols=1,
       notes="Vérifier que les trois éléments sont là : quand, quoi, ce qui a été vérifié.")

    d.billet(
        "Décrivez un problème d'appareil que vous avez déjà eu, en trois phrases.",
        exemples=[
            "Quand ça arrivait, ce que vous observiez, ce que vous aviez vérifié.",
            "Si vous n'en avez pas eu, inventez-en un à partir du tableau.",
        ],
        notes="Bilan du bloc D. Ce billet est le brouillon direct de la production écrite "
              "de E1.")

    return d.save(dossier)
