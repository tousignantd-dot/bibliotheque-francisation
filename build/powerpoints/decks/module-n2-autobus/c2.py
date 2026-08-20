# -*- coding: utf-8 -*-
"""C2 · Lire un horaire, lire un avis.
Bloc C « Défi 2 » · couleur ambre · 60 min.
Source : dialogue `t2b`, exercices `t2horaire`, `t2avis`, `t2b`.

La séance de lecture du module. Un horaire et un avis sur une porte sont les
deux seuls textes qu'un élève de niveau 2 doit pouvoir déchiffrer seul dans
la rue. Les deux se lisent par repérage, pas par lecture suivie.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-autobus/images/')


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Lire un horaire, lire un avis",
        chapeau="Deux textes de la rue. On ne les lit pas en entier : on y "
                "cherche une chose précise, et on s'arrête dès qu'on l'a.",
        duree='60 minutes')

    d.titre(notes="Prévenir le groupe : on ne va pas comprendre tous les mots, et ce n'est "
                  "pas le but. Un horaire se regarde ; il ne se lit pas.")

    d.objectifs([
        "trouver une heure dans un horaire ;",
        "comprendre à quoi sert une correspondance ;",
        "comprendre un avis affiché ;",
        "savoir ce qu'est un jour férié.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce que ce papier annonce ?",
        image=IMG + 'avis-porte.jpg',
        pistes=[
            "Où est ce papier ?",
            "Qui l'a mis là ?",
            "Qu'est-ce qu'il peut annoncer ?",
            "Que fait-on si on ne comprend pas ?",
        ],
        notes="Faire lister les avis qu'on trouve sur une porte : fermé, en congé, "
              "déménagé, ouvre plus tard. Trois ou quatre suffisent.")

    d.dialogue('Dialogue', "Un avis sur la porte", [
        ("HASSAN", "Nadia, il y a un papier sur la porte du CLSC.", True),
        ("NADIA", "Qu'est-ce qui est écrit ?", True),
        ("HASSAN", "« Fermé le lundi 5 septembre ». Je ne comprends pas pourquoi.", True),
        ("NADIA", "C'est un jour férié. Tout est fermé ce jour-là.", True),
        ("HASSAN", "Alors je viens mardi ?", True),
    ], consigne="Écoutez, puis dites ce que Hassan va faire.",
       notes="Hassan lit le papier, ne comprend pas la raison, et demande. C'est la bonne "
             "conduite : lire ce qu'on peut, demander le reste.")

    d.tableau('Analyse', "Ce qu'on cherche dans un horaire",
              ['On cherche', 'On regarde'],
              [["l'heure du prochain", "la colonne du jour, la ligne de l'heure"],
               ["la fréquence", "l'écart entre deux heures de la colonne"],
               ["le dernier passage", "la dernière heure, tout en bas"],
               ["le samedi et le dimanche", "une colonne à part, souvent moins remplie"]],
              cle=2,
              note="La fin de semaine a presque toujours un horaire différent. C'est la "
                   "surprise la plus fréquente.",
              notes="Diapositive à photographier. Si possible, distribuer un vrai horaire "
                    "papier de la ligne du quartier.")

    d.regle("La correspondance",
            "Le petit papier qui rend le deuxième autobus gratuit.",
            precision="On la demande ou on la prend en montant, et on la <b>garde</b>. "
                      "Sans elle, il faut payer une deuxième fois.",
            notes="Diapositive à photographier. Montrer une vraie correspondance si "
                  "quelqu'un en a une : l'objet vaut mieux que l'explication.")

    d.cartes("Trois mots des avis", "Ce qu'ils annoncent", [
        ("fermé", "Le lieu n'ouvre pas ce jour-là. Il faut revenir un autre jour."),
        ("un jour férié", "Un jour de congé où presque tout est fermé : bureaux, "
                          "cliniques, banques."),
        ("horaire modifié", "Le lieu ouvre, mais pas aux heures habituelles. Lire "
                            "l'heure écrite juste après."),
    ], cols=3, notes="Diapositive à photographier. Donner les trois ou quatre jours fériés "
                     "qui tombent pendant la session en cours.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Le papier annonce que le CLSC est fermé.", "vrai"),
        ("Il est fermé parce qu'il déménage.", "faux — c'est un jour férié"),
        ("Un jour férié, presque tout est fermé.", "vrai"),
        ("Hassan reviendra mardi.", "vrai"),
    ], corrige=True, cols=1,
       notes="Rapide : dix minutes. L'essentiel de la séance est dans la pratique qui "
             "suit.")

    d.pratique('Pratique · à deux', "Cherchez dans l'horaire",
               "Avec un horaire papier ou une photo d'écran d'arrêt.", [
        ("Étape 1", "Trouvez le premier passage du matin."),
        ("Étape 2", "Trouvez le dernier passage du soir."),
        ("Étape 3", "Trouvez tous les combien il passe."),
        ("Étape 4", "Comparez la semaine et le samedi."),
    ], cols=1,
       notes="Vingt minutes. Faire dire les heures à voix haute des deux façons — chiffres "
             "et mots — pour relier la séance à A2.")

    d.billet(
        "Notez une chose affichée près de chez vous.",
        exemples=[
            "Sur une porte, à un arrêt, dans l'entrée de votre immeuble.",
            "Écrivez ce qui est écrit, et ce que vous en comprenez.",
        ],
        notes="Devoir de terrain. En reparler à la séance suivante : les avis rapportés "
              "font toujours de bonnes discussions.")

    return d.save(dossier)
