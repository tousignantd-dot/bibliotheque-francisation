# -*- coding: utf-8 -*-
"""B4 · Six lignes, et personne n'a besoin de vous
Bloc B « Défi 1 » · couleur ambre · 75 min. La note d'appel.
Source : dialogue `t1` (fin), exercice `t1note`, mini-leçon `t1note`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="Six lignes, et personne n'a besoin de vous",
        chapeau="Le test d'une bonne note : posez-la sur le bureau de "
                "quelqu'un d'autre et partez en congé. Si cette personne "
                "peut agir sans vous téléphoner, la note est bonne.",
        duree='75 minutes')

    d.titre(notes="Séance qui ferme le défi 1. Commencer par le test : projeter une note "
                  "volontairement incomplète — « Mme T. a appelé, rappeler » — et demander "
                  "au groupe ce qui manque. La liste qu'ils produisent est exactement "
                  "celle des six lignes.")

    d.objectifs([
        "écrire une note d'appel en six lignes ;",
        "employer les abréviations que tout le monde comprend ;",
        "distinguer ce qu'une note contient de ce qu'elle ne contient jamais ;",
        "signer et dater sa note.",
    ])

    d.dialogue('Dialogue', "La note que Dorine écrit", [
        ("DORINE", "Alors : madame Thériault, ce matin, 5680 Beaubien, appartement 3. "
                   "Elle dit que son aide du mercredi ne viendra pas. Elle demande un "
                   "remplacement avant son rendez-vous de jeudi.", True),
        ("GHISLAIN", "Continuez.", True),
        ("DORINE", "Numéro : 514 225-1440. Elle demande qu'on la rappelle avant midi ; "
                   "après, elle ne répond pas.", True),
        ("GHISLAIN", "Voilà une note. Six lignes, et je peux agir sans vous poser une "
                     "seule question. Ajoutez la date et votre nom en bas.", True),
        ("DORINE", "Pourquoi mon nom ? C'est elle qui a appelé.", True),
        ("GHISLAIN", "Parce que dans trois jours, quelqu'un voudra savoir qui a pris "
                     "le message. Une note sans nom, c'est une note sans personne "
                     "derrière.", False),
    ], notes="La dernière réplique est celle à retenir. Faire remarquer que Dorine "
             "emploie exactement les formes de B3 : « elle dit que », « elle demande ».")

    d.regle("Six lignes, toujours les mêmes",
            "Qui a appelé, quand, pourquoi, ce qu'on demande, comment "
            "joindre, ce qui presse.",
            precision="Toujours dans cet ordre : c'est ce qui permet de les remplir "
                      "pendant que la personne parle, sans réfléchir à la structure.",
            notes="Diapositive à photographier, et à afficher au mur de la classe pendant "
                  "tout le module. C'est la seule liste que les élèves auront à retenir "
                  "par cœur.")

    d.cartes("Ce qu'une note ne contient jamais", "Trois choses qui l'alourdissent", [
        ("Vos impressions",
         "« Elle avait l'air fâchée », « encore elle » : jamais."),
        ("Les mots exacts entre guillemets",
         "Une note résume ; elle ne transcrit pas."),
        ("Les répétitions de la personne",
         "Elle l'a dit trois fois : vous l'écrivez une fois."),
        ("Pourquoi c'est important",
         "Une note reste dans un dossier longtemps, et peut être lue par la personne "
         "concernée."),
    ], notes="La quatrième carte est un argument, pas une règle : c'est celui qui "
             "convainc. Demander au groupe ce qu'ils écriraient s'ils savaient que la "
             "personne lira la note.")

    d.tableau('Les abréviations', "Celles que tout le monde lit",
              ['Abréviation', 'Ce que ça veut dire'],
              [["RDV", "rendez-vous"],
               ["tél.", "téléphone"],
               ["app.", "appartement"],
               ["a.m. et p.m.", "avant-midi et après-midi"],
               ["SVP", "s'il vous plaît"]],
              cle=0,
              note="Une abréviation inventée ce matin n'est pas une abréviation : "
                   "c'est un code personnel.",
              notes="Demander au groupe quelles abréviations ils emploient déjà. "
                    "Distinguer celles qui sont partagées de celles qui sont "
                    "personnelles : la note est la limite entre les deux.")

    d.piege("Noter sans le numéro de téléphone",
            "Mme Thériault a appelé, rappeler.",
            "Mme Thériault, tél. 514 225-1440, rappeler avant midi.",
            "Sans numéro, votre collègue doit chercher dans un dossier ou vous appeler. "
            "Le numéro s'écrit pendant que la personne parle, pas après.",
            notes="Faire remarquer que c'est la seule ligne d'une note qu'une erreur rend "
                  "entièrement inutile. La relire à voix haute avant de raccrocher.")

    d.pratique('Écoute', "Remplissez la note",
               "Réécoutez le message de madame Thériault, puis complétez.", [
        ("Qui : madame ___ , 5680 rue Beaubien, app. 3.", "Thériault"),
        ("Motif : son aide du ___ matin ne pourra pas venir.", "mercredi"),
        ("Demande : un ___ avant son rendez-vous.", "remplacement"),
        ("Son rendez-vous à la clinique est le ___ .", "jeudi"),
        ("Tél. : 514 ___ -1440.", "225"),
        ("Urgent : rappeler avant ___ .", "midi"),
    ], cols=2, corrige=True,
       notes="Faire écouter une seule fois avant de remplir, puis une seconde fois pour "
             "vérifier. C'est ainsi que ça se passe en vrai : on n'a droit qu'à une "
             "écoute et demie.")

    d.pratique('Production', "Trois notes à partir de trois appels",
               "Écrivez chaque note en six lignes.", [
        ("Un fournisseur annonce que la livraison de jeudi est reportée à lundi.",
         "qui · quand · motif · demande de confirmer · tél. au dossier · rien d'urgent"),
        ("Une collègue est malade et ne rentrera pas aujourd'hui.",
         "qui · ce matin · malade · reprend demain · aviser Ghislain · tél. cellulaire"),
        ("Un homme veut parler à la directrice et ne dit pas pourquoi.",
         "qui : sans nom · ne dit pas le motif · rappellera lui-même p.m. · aucun numéro laissé"),
    ], corrige=True,
       notes="Le troisième cas est le plus formateur : écrire « aucun numéro laissé » "
             "vaut mieux que de laisser la ligne vide, qui fait croire à un oubli. Dire "
             "ce qui manque est aussi une information.")

    d.billet(
        "Prenez une note d'appel à partir d'un vrai message de votre boîte vocale.",
        exemples=[
            "Six lignes, sans impressions et sans guillemets.",
            "Signez et datez. Relisez-la comme si vous étiez quelqu'un d'autre.",
        ],
        notes="Si des élèves n'ont pas de message à traiter, leur faire raconter un appel "
                  "reçu récemment, à l'oral, pendant qu'un camarade prend la note.")

    return d.save(dossier)
