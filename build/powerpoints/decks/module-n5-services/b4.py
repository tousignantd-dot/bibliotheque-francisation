# -*- coding: utf-8 -*-
"""B4 · Écrire pendant qu'on écoute.
Bloc B « Défi 1 · L'appel » · couleur ambre · 75 min. Séance de production orale.
Source : exercices `t1notes` et `t1phrases`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="Écrire pendant qu'on écoute",
        chapeau="Comprendre et écrire en même temps, dans une langue qu'on "
                "apprend : beaucoup choisissent de tout comprendre et de "
                "ne rien noter. La solution n'est pas d'écrire plus vite, "
                "c'est d'écrire moins.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du défi 1, et la plus pratique. Prévoir des feuilles "
                  "de prise de notes vierges, et deux téléphones si le groupe accepte de "
                  "faire un appel réel en classe.")

    d.objectifs([
        "préparer une feuille d'appel avant de composer le numéro ;",
        "noter cinq renseignements et pas davantage ;",
        "répéter un numéro à voix haute pour le confirmer ;",
        "employer les formules qui font ralentir sans gêner personne.",
    ])

    d.declencheur(
        'Expérience', "Je vous dicte un numéro de requête. Notez-le.",
        pistes=[
            "24-118-7690, trois jours ouvrables, madame Micheline, jeudi.",
            "Combien de choses avez-vous notées ?",
            "Qu'est-ce que vous avez perdu en écrivant ?",
            "Qui a osé demander de répéter ?",
        ],
        notes="Dire la ligne une seule fois, au rythme normal du téléphone. L'échec est "
              "le but : il ouvre la séance mieux que n'importe quelle explication. "
              "Presque personne ne demandera de répéter — le relever.")

    d.regle("Cinq choses, jamais plus",
            "Le numéro, le délai, la date, le nom de la personne, ce qu'il faut faire ensuite.",
            precision="La feuille se prépare avant l'appel, avec ces cinq lignes déjà "
                      "écrites : il ne reste qu'à remplir des trous. Le reste, on s'en "
                      "souvient — ou ça ne comptait pas.",
            notes="Diapositive à photographier. Faire dessiner la feuille tout de suite, "
                  "avant de continuer : elle servira pendant le reste de la séance.")

    d.tableau('La feuille d\'appel', "Cinq lignes, préparées d\'avance",
              ['Ligne', 'Pourquoi elle y est'],
              [["Date de l'appel", "sans elle, « trois jours ouvrables » ne veut rien dire"],
               ["Numéro de requête", "la seule chose qu'on ne peut pas reconstituer"],
               ["Délai annoncé", "en jours ouvrables, pas en jours de calendrier"],
               ["Nom de la personne", "au deuxième appel, il fait gagner cinq minutes"],
               ["Ce qu'il faut faire ensuite", "rappeler, se déplacer, attendre"]],
              cle=0,
              note="Le numéro s'écrit pendant qu'il se dit, jamais de mémoire après coup.",
              notes="Diapositive à photographier. C'est l'outil que les élèves emporteront "
                    "hors du cours ; le dire explicitement.")

    d.cartes("Six formules pour ralentir", "Sans gêner personne", [
        ("Avant de commencer",
         "« Un instant, je prends une feuille. » — cinq secondes gagnées."),
        ("La plus utile de toutes",
         "« Pouvez-vous répéter plus lentement, s'il vous plaît ? »"),
        ("Pendant qu'on écrit",
         "« Je vous répète le numéro : … C'est bien ça ? »"),
        ("Pour vérifier qu'on a compris",
         "« Trois jours ouvrables. Donc pas avant vendredi, si je comprends bien ? »"),
    ], notes="La troisième carte règle le vrai problème : le silence pendant qu'on écrit. "
             "Répéter à voix haute le remplit utilement et vérifie en même temps.")

    d.piege("Ne pas oser faire répéter",
            "Il va trouver que je comprends mal le français.",
            "Pouvez-vous répéter plus lentement, s'il vous plaît ?",
            "Un préposé répète vingt fois par jour, à des gens de toutes les langues. "
            "Faire répéter est le signe qu'on prend la démarche au sérieux. Ne pas le "
            "faire, c'est repartir avec un numéro faux — ce qui coûte un deuxième appel.",
            notes="Nommer la honte ouvertement : c'est le vrai obstacle de cette séance, "
                  "bien plus que la langue. Beaucoup d'élèves seront soulagés qu'on le dise.")

    d.pratique('Prise de notes', "Remplissez la fiche",
               "D'après l'appel de la séance B1.", [
        ("Service appelé", "le 311 de la Ville"),
        ("Motif", "le bac brun n'a pas été ramassé depuis deux semaines"),
        ("Personne rencontrée", "madame Micheline"),
        ("Jour de collecte du secteur", "le mardi matin"),
        ("Heure limite pour sortir le bac", "avant sept heures"),
        ("Numéro de requête", "24-118-7690"),
        ("Délai annoncé", "trois jours ouvrables"),
        ("Si rien n'arrive d'ici vendredi", "rappeler avec le numéro de requête"),
    ], corrige=True,
       notes="Refaire écouter l'appel une fois pendant qu'ils remplissent, puis une "
             "seconde fois pour vérifier. La deuxième écoute est celle qui apprend.")

    d.pratique('Jeu de rôle', "Deux par deux, dos à dos",
               "L'un appelle, l'autre est le préposé. Cinq minutes, puis on inverse.", [
        ("Le bac brun n'est plus ramassé", "requête 24-118-7690, trois jours ouvrables"),
        ("Un vieux réfrigérateur à jeter", "écocentre, gratuit, preuve de résidence exigée"),
        ("Une demande bloquée en ligne", "se présenter au comptoir, deux pièces d'identité"),
    ], corrige=False,
       notes="Dos à dos : c'est la seule façon de reproduire le téléphone en classe. "
             "Circuler et noter les questions oubliées sans interrompre. Bilan collectif "
             "à la fin, au tableau, sans nommer personne.")

    # `capture` n'existe que dans theme.Deck : les présentations la portent, les
    # fiches imprimées non (build/powerpoints/fiche.py n'a pas la méthode). Une
    # fiche noir et blanc n'a de toute façon rien à faire d'une capture d'écran.
    if hasattr(d, 'capture'):
        d.capture('t1phrases', "L'exercice à l'écran",
                  consigne="À quel moment de l'appel dit-on chaque phrase ?",
                  notes="Dix minutes au casque. Les élèves qui ont échoué au déclencheur "
                        "réussissent presque toujours ici : le dire, ça se voit sur les "
                        "visages.")

    d.billet(
        "Faites un vrai appel cette semaine, avec votre feuille préparée.",
        exemples=[
            "Ville, école, clinique, assurance — n'importe quelle démarche réelle.",
            "Apportez votre feuille remplie. Nous les regarderons ensemble.",
        ],
        notes="Le devoir le plus exigeant du module. Prévenir que certains n'oseront pas, "
              "et offrir de faire l'appel en classe, à côté de vous, à ceux qui le "
              "demandent. Plusieurs le demanderont.")

    return d.save(dossier)
