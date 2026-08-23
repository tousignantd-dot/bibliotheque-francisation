# -*- coding: utf-8 -*-
"""D1 · Ce que l'offre demande vraiment
Bloc D « Défi 3 · Mon curriculum vitæ parle à cette région » · acier · 75 min.
Source : dialogue `t3` (répliques 1 à 9), exercices `t3vf` et `t3offre`.
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n7-recherche' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Ce que l'offre demande vraiment",
        chapeau="Une annonce se lit deux fois : la première pour savoir si "
                "le poste est pour vous, la seconde pour y récolter les mots "
                "avec lesquels vous allez écrire.",
        duree='75 minutes')

    d.titre(notes="Ouverture du Défi 3. Distribuer l'offre d'emploi imprimée — le "
                  "texte de l'exercice `t3offre` — et travailler dessus, surligneur "
                  "en main, comme sur le portrait de C2.")

    d.objectifs([
        "distinguer une exigence d'un atout ;",
        "retrouver dans une annonce le passage qui répond à une question ;",
        "relever ce que l'annonce ne dit pas, et en faire des questions ;",
        "comprendre pourquoi un curriculum vitæ se retaille pour chaque offre.",
    ], notes="Le premier objectif fait renoncer ou postuler : plusieurs élèves "
             "écartent une offre parce qu'il leur manque un atout, qui n'élimine "
             "personne.")

    d.declencheur(
        'Observation', "Que faut-il regarder en premier dans une annonce ?",
        image=IMG + 'route-region.jpg',
        pistes=[
            "Le titre du poste, le salaire, le lieu, la date de fin ?",
            "Qu'est-ce qui décide si votre dossier sera lu ?",
            "Et si vous devez déménager pour l'occuper ?",
            "Combien de temps donneriez-vous à une annonce, la première fois ?",
        ],
        notes="La bonne réponse à la dernière question est « une minute ». On lit "
              "d'abord pour trier, pas pour comprendre.")

    d.dialogue('Dialogue · 1 de 2', "Cette ligne pourrait être celle de n'importe qui", [
        ("MARIE-ÈVE", "Votre curriculum vitæ, en haut, sous votre nom, qu'est-ce qu'il annonce ?", True),
        ("HAFIDA", "« Recherche d'emploi dans le domaine scientifique. »", True),
        ("MARIE-ÈVE", "Voilà le problème, et il est en trois mots. Cette ligne pourrait être celle de n'importe qui.", True),
        ("MARIE-ÈVE", "Ce que l'employeur veut lire là, c'est le titre du poste qu'il a affiché, pas une catégorie.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire écrire à chacun la première ligne de son propre curriculum vitæ, "
             "puis la comparer à cette réplique. L'effet est immédiat.")

    d.dialogue('Dialogue · 2 de 2', "Ranger autrement n'est pas mentir", [
        ("MARIE-ÈVE", "Un curriculum vitæ ne se rédige pas une fois pour toutes : il se retaille pour chaque offre.", True),
        ("MARIE-ÈVE", "Une personne qui reçoit quarante dossiers ne lit d'abord que les premières lignes.", True),
        ("HAFIDA", "On a le droit de faire ça ?", True),
        ("MARIE-ÈVE", "On a le droit d'organiser. On n'a pas le droit de mentir. Tant que les dates y sont, l'ordre vous appartient.", True),
    ], notes="La question de Hafida est celle de tout le groupe, et elle est "
             "légitime. Y répondre sans détour : les dates sont vérifiables, l'ordre "
             "ne l'est pas.")

    d.regle("« Exigé » et « atout » ne sont pas la même chose",
            "Ce qui est exigé vous élimine si vous ne l'avez pas. Ce qui est "
            "un atout vous distingue si vous l'avez.",
            precision="Ne renoncez jamais à une offre parce qu'il vous manque un "
                      "atout. Et regardez la formule « ou expérience équivalente "
                      "vérifiable » : elle ouvre la porte quand le diplôme d'ici "
                      "vous manque.",
            notes="Diapositive à photographier. C'est la règle la plus utile du bloc "
                  "pour un élève dont le diplôme vient d'ailleurs.")

    # Six rangées **et** une note ne tiennent pas sur une diapositive projetée
    # (le garde-fou de `theme.py` refuse au plancher de corps). La note est
    # descendue dans les notes de l'enseignante, et les cellules raccourcies :
    # une diapositive se lit de loin, elle ne se lit pas en entier.
    d.tableau('Analyse', "Les six lignes à surligner dans toute annonce",
              ['Ce qu\'on cherche', 'Ce que ça décide'],
              [["Le titre exact", "votre première ligne et votre objet"],
               ["Les exigences", "si votre dossier est lu"],
               ["Les atouts", "si vous passez devant"],
               ["Les tâches", "les mots de votre lettre"],
               ["Ce qui manque", "vos questions au téléphone"],
               ["La date de fin", "tout le reste"]],
              cle=0,
              notes="Diapositive à photographier. Faire surligner les six dans "
                    "l'offre distribuée, avec six couleurs si le groupe en a. "
                    "Dire à voix haute la règle qui ne tient pas sur la "
                    "diapositive : envoyer trois jours d'avance, parce qu'un "
                    "ennui d'imprimante ne se prévoit pas.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("La première ligne du curriculum vitæ doit reprendre le titre du poste.", "vrai"),
        ("On doit toujours placer l'emploi le plus récent en premier.", "faux - le plus pertinent"),
        ("Marie-Ève conseille de créer deux blocs d'expérience.", "vrai"),
        ("Réorganiser son expérience revient à mentir.", "faux - tant que les dates sont exactes"),
        ("Un chiffre vaut mieux que trois adjectifs pour décrire une tâche.", "vrai"),
        ("La lettre d'accompagnement répète le curriculum vitæ.", "faux - elle dit pourquoi vous"),
    ], corrige=True,
       notes="Exercice `t3vf` du module interactif.")

    d.pratique('Lecture', "Ce que dit l'offre d'Alumico",
               "Retrouvez le passage exact.", [
        ("Quel est le titre exact du poste ?", "technicienne ou technicien de laboratoire, contrôle de la qualité"),
        ("Quel est le statut et l'horaire ?", "permanent, 37,5 h, quart de jour"),
        ("Quelle formation est exigée ?", "un DEC en techniques de laboratoire, ou une expérience équivalente vérifiable"),
        ("Quelle expérience est un atout ?", "le contrôle de la qualité en transformation des métaux"),
        ("Qu'offre l'entreprise à quelqu'un d'ailleurs ?", "un programme d'aide à l'installation"),
        ("Jusqu'à quand peut-on envoyer son dossier ?", "au plus tard le 30 novembre"),
    ], corrige=True,
       notes="Exercice `t3offre` du module interactif. Faire relever ce que l'offre "
             "ne dit pas : ni salaire, ni supérieur, ni nombre exact de postes. "
             "Ce sont les trois questions du jeu de rôle de E1.")

    d.billet(
        "Écrivez les trois questions que vous poseriez au téléphone au sujet de cette offre.",
        exemples=[
            "Trois questions que l'annonce ne permet pas de trancher.",
            "Une question par silence de l'annonce.",
        ],
        notes="Ces trois questions servent directement au jeu de rôle de E1 : les "
              "faire garder.")

    return d.save(dossier)
