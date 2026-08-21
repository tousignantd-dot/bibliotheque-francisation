# -*- coding: utf-8 -*-
"""A4 · Petit, moyen, grand.
Bloc A « Je découvre » · couleur ambre · 75 min.
Source : exercice `prFormats`, mini-leçon `prFormats`.

Le programme de niveau 3 nomme explicitement « les types de formats » dans le
lexique de cette situation : c'est l'un des deux seuls blocs de vocabulaire
qu'il donne pour le service de restauration.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-restaurant/images/')


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre='Petit, moyen, grand',
        chapeau="Trois prix à côté d'un même plat ne veulent pas dire trois "
                "plats. Ils veulent dire trois formats — et le préposé va "
                "demander lequel.",
        duree='75 minutes')

    d.titre(notes="Séance d'écriture et de grammaire. Prévoir trois contenants de "
                  "grandeurs différentes si possible : le mot se retient mieux avec "
                  "l'objet dans la main.")

    d.objectifs([
        "nommer les trois formats du comptoir ;",
        "accorder petit, moyen et grand au féminin ;",
        "répondre à « Quel format ? » en deux mots ;",
        "comprendre qu'un format change la portion, pas le plat.",
    ])

    d.declencheur(
        'Observation', "Pourquoi trois verres ?",
        image=IMG + 'trois-formats.jpg',
        pistes=[
            "Est-ce que c'est trois boissons différentes ?",
            "Qu'est-ce qui change entre les trois ?",
            "Comment on demande celui du milieu ?",
            "Est-ce que le prix est le même ?",
        ],
        notes="Laisser le groupe trouver seul que c'est la quantité qui change. Le mot "
              "« portion » arrive naturellement à ce moment-là.")

    d.regle("Trois mots, et pas un de plus",
            "petit  ·  moyen  ·  grand",
            precision="Au comptoir, il n'y a que ces trois grandeurs, et le "
                      "préposé les dit toujours dans cet ordre. On ne dit ni "
                      "« large », ni « numéro deux », ni « moyen-grand » : ces "
                      "mots-là n'existent pas ici.",
            notes="Diapo à photographier. Faire répéter les trois mots dans l'ordre, à "
                  "voix haute, deux fois. L'ordre compte : c'est celui qu'on entendra.")

    d.tableau('Analyse', "Le même mot, deux formes",
              ['Masculin', 'Féminin', 'Exemple'],
              [["petit", "petite", "un petit café / une petite soupe"],
               ["moyen", "moyenne", "un format moyen / une portion moyenne"],
               ["grand", "grande", "un grand jus / une grande salade"]],
              cle=1,
              note="« Moyen » double son n au féminin : moyenne.",
              notes="Diapo à photographier. La ligne du milieu est celle qui coûte le "
                    "plus cher en écriture : faire écrire « moyenne » au tableau par un "
                    "élève, puis vérifier les deux n avec tout le groupe.")

    d.tableau('Analyse', "Le genre des mots du comptoir",
              ['Masculins', 'Féminins'],
              [["un café, un jus, un format", "une soupe, une salade, une portion"],
               ["un sandwich, un plateau", "une frite, une boîte, une caisse"],
               ["un breuvage, un trio", "une commande, une serviette"]],
              cle=0,
              note="Le genre du plat décide de la forme du format.",
              notes="Faire chercher un indice : plusieurs féminins finissent par un e "
                    "qu'on n'entend presque pas. C'est un indice, pas une règle.")

    d.regle("La réponse la plus courte est la bonne",
            "« Quel format ? — Petit, s'il vous plaît. »",
            precision="Le nom du plat vient d'être dit : inutile de le répéter. "
                      "Un mot et « s'il vous plaît », c'est complet, poli, et "
                      "c'est ce que la file attend.",
            notes="Diapo à photographier. Faire jouer l'échange par paires, debout, cinq "
                  "fois de suite avec des plats différents. Vingt secondes chacun.")

    d.pratique('Écriture', "Petit, moyen ou grand ?",
               "Complétez avec la forme juste.", [
        ("Une ___ soupe, s'il vous plaît.  (la plus petite)", "petite"),
        ("Un ___ café pour emporter.  (le plus grand)", "grand"),
        ("Une frite de format ___ .  (entre les deux)", "moyen"),
        ("Une ___ salade, ça suffit pour deux.  (la plus grande)", "grande"),
        ("Une portion ___ , c'est celle du milieu.  (féminin)", "moyenne"),
    ], corrige=True,
       notes="Faire écrire dans le cahier avant de corriger. Les trois derniers items "
             "sont ceux où l'accord se joue.")

    d.piege("Oublier le e au féminin",
            "une petit soupe",
            "une petite soupe",
            "L'erreur ne s'entend presque pas à l'oral, ce qui la rend difficile à "
            "corriger : l'élève ne l'entend pas non plus. Elle se voit seulement à "
            "l'écrit. Le réflexe à installer : nommer le plat, se demander s'il est "
            "masculin ou féminin, puis écrire le format.",
            notes="Faire relire à voix haute en exagérant le e final : « petit-eu ». "
                  "C'est faux à l'oral, mais ça installe le réflexe à l'écrit.")

    d.pratique('Production orale', "Commandez trois fois",
               "Le même plat, trois formats, à voix haute.", [
        ("une soupe", "Une petite soupe, une soupe moyenne, une grande soupe."),
        ("un café", "Un petit café, un café moyen, un grand café."),
        ("une frite", "Une petite frite, une frite moyenne, une grande frite."),
        ("un jus", "Un petit jus, un jus moyen, un grand jus."),
    ], corrige=True,
       notes="En paires, debout. Un élève dit le plat, l'autre le décline en trois "
             "formats. On change de rôle après deux plats.")

    d.billet(
        "Écrivez trois commandes, chacune avec un format.",
        exemples=[
            "Une petite soupe aux légumes, s'il vous plaît.",
            "Variez le genre : un plat masculin, un plat féminin.",
        ],
        notes="Devoir court. Ces trois phrases serviront de commande de départ au "
              "bloc C, quand on entrera au comptoir pour de vrai.")

    return d.save(dossier)
