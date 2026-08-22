# -*- coding: utf-8 -*-
"""B4 · Les cinq morceaux d'une annonce d'absence
Bloc B « Défi 1 · Prévenir de son absence » · couleur ambre · 75 min.
Séance d'assemblage. Source du module : exercice `t1red`, dialogue `t1`.
"""
import os
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-ecole/images/')


def img(nom):
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="Les cinq morceaux d'une annonce d'absence",
        chapeau="Trois séances ont donné les pièces : l'ordre du comptoir, "
                "la question glissée, la promesse au futur. Il reste à les "
                "assembler et à les dire d'un seul tenant, devant quelqu'un "
                "qui ne vous connaît pas.",
        duree='75 minutes')

    d.titre(notes="Séance d'assemblage, la dernière du défi 1. Prévoir la moitié du temps "
                  "en production réelle, deux par deux. Rendre aux élèves leurs billets "
                  "de B1, B2 et B3 : ils ont déjà écrit les trois quarts de leur texte "
                  "sans le savoir.")

    d.objectifs([
        "assembler les cinq morceaux d'une annonce d'absence, dans l'ordre ;",
        "tenir le tout en moins de deux minutes ;",
        "poser deux questions glissées sans perdre le fil ;",
        "reformuler ce qu'on a compris avant de quitter le comptoir.",
    ], notes="Le quatrième objectif est le plus négligé et le plus utile. Deux secondes "
             "de reformulation évitent le retour de la semaine suivante.")

    d.regle("Les cinq morceaux",
            "Qui je suis · ce que je viens faire · les dates · le motif · "
            "ce que je ferai et ce que je demande.",
            precision="Le motif tient en une phrase. Les dates en portent deux : "
                      "à partir de quand, jusqu'à quand.",
            notes="Diapositive à photographier. Elle reprend la règle de B1 en l'ouvrant "
                  "au cinquième morceau. La faire recopier à la main, elle sert en E1.")

    d.cartes("Les cinq morceaux, en exemple", "L'annonce complète d'Amelia", [
        ("1 · Qui je suis",
         "Bonjour, je m'appelle Amelia Dumitrescu, groupe 4, en francisation."),
        ("2 · Ce que je viens faire",
         "Je viens vous annoncer une absence prévue."),
        ("3 · Les dates",
         "Je serai absente à partir du 9 mars, jusqu'au 27 inclusivement."),
        ("4 · Le motif",
         "Ma mère est opérée à l'étranger et je suis la seule à pouvoir y aller."),
        ("5 · Ce que je ferai et ce que je demande",
         "Je reviendrai le 30 et je vous apporterai la pièce justificative. "
         "Je voudrais savoir si je dois remplir un formulaire."),
    ], cols=1,
       notes="Faire lire les cinq à voix haute par cinq élèves différents, à la suite, "
             "sans pause. Le groupe entend alors que l'ensemble dure une minute et "
             "demie, pas dix.")

    d.declencheur(
        'Mise en situation', "Le comptoir est libre. Vous avez deux minutes.",
        image=img('comptoir-secretariat.jpg'),
        pistes=[
            "Qui commence ? Vous, ou la personne au comptoir ?",
            "Que faites-vous si on vous coupe au milieu de vos dates ?",
            "Que faites-vous si on vous renvoie à quelqu'un d'autre ?",
            "Comment savez-vous que vous pouvez partir ?",
        ],
        notes="La deuxième piste vaut la peine d'être jouée : la personne au comptoir "
              "coupe souvent pour ouvrir le dossier. Ce n'est pas de l'impolitesse, et "
              "on reprend là où on en était.")

    d.pratique('Production orale', "Deux par deux, au comptoir",
               "L'un joue le secrétariat, l'autre expose son absence. Puis on échange.", [
        ("Le secrétariat ouvre : Bonjour, qu'est-ce que je peux faire pour vous ?",
         "l'élève enchaîne avec les morceaux 1 et 2"),
        ("Le secrétariat demande : À partir de quand ?",
         "morceau 3, les deux dates, avec « inclusivement »"),
        ("Le secrétariat demande : Et le motif ?",
         "morceau 4, une seule phrase"),
        ("Le secrétariat dit : Il faudra le mettre par écrit.",
         "morceau 5, au futur, puis une question glissée"),
        ("Le secrétariat répond quelque chose que l'élève n'a pas compris.",
         "faire répéter poliment, puis reformuler"),
    ], corrige=False,
       notes="Chronométrer discrètement. La première tentative dure trois minutes, la "
             "troisième une minute et demie. Le dire au groupe à la fin : le progrès est "
             "mesurable et c'est rare.")

    d.piege("Repartir sans avoir noté l'échéance",
            "Bon, parfait, merci beaucoup. Bonne journée !",
            "Donc je remplis le formulaire et je le rapporte avant le 6. C'est bien ça ?",
            "La phrase de reformulation coûte deux secondes et évite un retour "
            "complet. Elle sert aussi à la personne au comptoir, qui entend alors ce "
            "qu'elle a réellement dit.",
            notes="Faire ajouter cette phrase à toutes les productions de la séance. "
                  "C'est le geste le plus transférable de tout le module : il vaut à la "
                  "clinique, à la banque et au bureau du propriétaire.")

    d.pratique('Écriture', "Votre annonce, en cinq phrases",
               "Écrivez les cinq morceaux, une phrase chacun.", [
        ("Morceau 1 : nom complet, groupe.", "une phrase"),
        ("Morceau 2 : ce que vous venez faire.", "une phrase, au présent"),
        ("Morceau 3 : les deux dates.", "à partir du... jusqu'au... inclusivement"),
        ("Morceau 4 : le motif.", "une phrase, sans détail"),
        ("Morceau 5 : deux promesses au futur et une question glissée.",
         "deux ou trois phrases"),
    ], corrige=False,
       notes="Ce texte est la première version de ce qui sera enregistré en E1. Le faire "
             "garder dans le cahier : on ne le réécrira pas de zéro, on le reprendra.")

    d.billet(
        "Écrivez la phrase de reformulation que vous direz avant de partir.",
        exemples=[
            "Ce que vous devez faire, et pour quelle date.",
            "Terminez par « C'est bien ça ? »",
        ],
        notes="Ramasser les billets. Ceux qui n'y mettent pas de date n'ont pas encore "
              "compris ce qu'est une échéance : c'est exactement ce que le bloc C va "
              "travailler.")

    return d.save(dossier)
