# -*- coding: utf-8 -*-
"""B2 · Expliquer un mot dans ses mots.
Bloc B · couleur framboise (vocabulaire) · 60 min.
Source : exercice `t1vocab` — définir sans le dictionnaire.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='framboise',
        titre='Expliquer un mot dans ses mots',
        chapeau="Quand un mot manque, on ne s'arrête pas : on le contourne. Savoir "
                "expliquer « une affiche » sans dire « affiche » est la compétence qui "
                "permet de parler de tout.",
        duree='60 minutes')

    d.titre(notes="Commencer par un jeu : décrire un objet de la classe sans le nommer. "
                  "Le groupe devine. C'est exactement l'exercice de la séance.")

    d.objectifs([
        "expliquer un mot sans l'employer ;",
        "employer les quatre façons de définir : catégorie, usage, lieu, exemple ;",
        "contourner un mot qui manque dans une conversation ;",
        "comprendre une définition entendue.",
    ])

    d.tableau('Analyse', "Quatre façons de définir un mot",
              ['La façon', 'Un exemple'],
              [["par la catégorie", "un quartier, c'est une partie d'une ville"],
               ["par l'usage", "une affiche, ça sert à informer les gens"],
               ["par le lieu", "un témoin, c'est quelqu'un qui était sur place"],
               ["par l'exemple", "un organisme, comme la Croix-Rouge"]],
              cle=0,
              note="La première est la plus sûre : on nomme la catégorie, puis on "
                   "précise. C'est ainsi que font les dictionnaires.",
              notes="Faire produire les quatre types de définition pour un même mot. "
                    "L'exercice montre qu'il y a toujours plusieurs chemins.")

    d.regle('La règle',
            "On commence par « c'est un » ou « c'est quelque chose qui ».",
            precision="« Un quartier, c'est une partie d'une ville. » « Avertir, c'est "
                      "quelque chose qu'on fait quand on veut informer quelqu'un. » Ces "
                      "deux ouvertures suffisent à définir n'importe quoi.",
            notes="Écrire les deux formules au tableau. Ce sont celles à employer quand "
                  "un mot manque en pleine conversation.")

    d.cartes('Ouvrir la mini-leçon', "Quatre stratégies quand un mot manque", [
        ("Décrire l'objet",
         "« C'est une feuille de papier qu'on colle sur un mur, avec un message "
         "dessus. » Cela prend dix secondes et fonctionne toujours."),
        ("Dire à quoi ça sert",
         "« Ça sert à retrouver un animal perdu. » Souvent plus rapide que la "
         "description."),
        ("Donner le contraire",
         "« C'est le contraire de trouver. » Utile pour les verbes et les adjectifs."),
        ("Nommer une situation",
         "« C'est ce qu'on fait quand on a vu un accident et qu'on raconte ce qu'on a "
         "vu. » Pour les mots abstraits."),
    ], notes="La quatrième stratégie est celle qui débloque les mots difficiles. La faire "
             "pratiquer sur « un témoin » et « un organisme ».")

    d.pratique('Pratique · 1 de 4', "Expliquez le mot",
               "Sans employer le mot lui-même.", [
        ("un quartier", "une partie d'une ville ou d'un village"),
        ("reconnaître", "identifier quelqu'un ou quelque chose qu'on a déjà vu"),
        ("avertir", "informer quelqu'un d'un danger ou d'une nouvelle importante"),
        ("une affiche", "une feuille avec un message, placée pour être vue de tous"),
    ], corrige=True,
       notes="Accepter toute définition juste. Refuser seulement celles qui emploient le "
             "mot ou un mot de la même famille.")

    d.pratique('Pratique · 2 de 4', "Quatre mots du module",
               "Une définition par mot, avec la façon de votre choix.", [
        ("un témoin", "une personne qui a vu un événement"),
        ("un organisme", "un groupe organisé qui offre un service ou mène une cause"),
        ("amasser", "réunir, accumuler peu à peu"),
        ("un franc succès", "une vraie réussite, un grand succès"),
    ], corrige=True,
       notes="« Un franc succès » est une expression : la définir demande de comprendre "
             "que « franc » ne veut pas dire « honnête » ici.")

    d.piege("Le piège du mot de la même famille",
            "Avertir, c'est donner un avertissement.",
            "Avertir, c'est informer quelqu'un d'une chose importante.",
            "Employer un mot de la même famille ne définit rien : celui qui ne connaît "
            "pas « avertir » ne connaît pas « avertissement » non plus. Il faut changer "
            "complètement de mots.",
            notes="Erreur très fréquente et facile à corriger une fois nommée. La "
                  "signaler à chaque occurrence pendant l'exercice.")

    d.piege("Le piège du silence",
            "Vous vous arrêtez parce que le mot ne vient pas.",
            "« C'est le papier qu'on met sur les murs pour informer les gens. »",
            "Un mot qui manque n'arrête pas une conversation : il oblige à faire un "
            "détour. Ce détour prend dix secondes et il est presque toujours compris. "
            "S'arrêter, lui, met fin à l'échange.",
            notes="Point de méthode important. Beaucoup d'élèves se taisent plutôt que de "
                  "contourner. En faire une règle de classe.")

    d.pratique('Pratique · 3 de 4', "Jeu · devinez le mot",
               "À deux. L'un explique, l'autre devine. Puis on échange.", [
        ("Les mots à faire deviner", "témoin, organisme, reportage, concours, affiche"),
        ("La règle", "interdiction d'employer le mot ou un mot de la même famille"),
        ("Le temps", "trente secondes par mot"),
        ("À la fin", "chacun note les deux mots qu'il a trouvés les plus difficiles"),
    ], corrige=False,
       notes="Quinze minutes. C'est un jeu, et c'est aussi l'entraînement le plus "
             "efficace de tout le module pour la production orale.")

    d.pratique('Pratique · 4 de 4', "Comprendre une définition",
               "De quel mot parle-t-on ?", [
        ("« C'est une personne qui était là et qui a vu ce qui s'est passé. »", "un témoin"),
        ("« C'est un texte qui explique une nouvelle en détail. »", "un reportage"),
        ("« C'est une compétition où quelqu'un gagne un prix. »", "un concours"),
        ("« Ça veut dire réunir peu à peu, en plusieurs fois. »", "amasser"),
    ], corrige=True,
       notes="L'exercice inverse : comprendre au lieu de produire. Il montre que les "
             "définitions du groupe fonctionnent vraiment.")

    d.billet(
        "Choisissez trois mots du module et définissez-les dans vos mots.",
        exemples=[
            "Sans employer le mot ni un mot de la même famille.",
            "Commencez par « c'est un » ou « c'est quelque chose qui ».",
        ],
        notes="Ramasser. Les meilleures définitions peuvent être affichées : elles valent "
              "souvent mieux que celles d'un dictionnaire pour ce niveau.")

    return d.save(dossier)
