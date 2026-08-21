# -*- coding: utf-8 -*-
"""B4 · Les prix, les délais, et faire répéter.
Bloc B « Défi 1 · Demander avant de choisir » · couleur ambre (écriture) · 75 min.
Source : mini-leçon `t1prix`, exercices `t1prix` et `t1qui`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre='Les prix, les délais, et faire répéter',
        chapeau="Un prix dit en français va vite : « un dollar quarante-quatre », "
                "« treize dollars quinze ». La parade tient en une phrase, et "
                "elle se dit avant de payer, pas après.",
        duree='75 minutes')

    d.titre(notes="Séance d'écriture et de nombres. Prévoir de dire chaque prix deux "
                  "fois : une fois vite, comme au comptoir, une fois lentement.")

    d.objectifs([
        "comprendre un prix dit à voix haute ;",
        "répéter un prix pour le vérifier ;",
        "écrire un prix en chiffres à partir d'une phrase entendue ;",
        "comprendre ce qu'est un jour ouvrable.",
    ])

    d.regle("La phrase qui évite toutes les erreurs de prix",
            "Vingt-deux dollars ? Vingt-deux ?",
            precision="On répète le chiffre, seul, avec la voix qui monte. La "
                      "préposée confirme ou corrige en un mot. C'est court, c'est "
                      "poli, et ça se fait des dizaines de fois par jour au "
                      "comptoir sans que personne ne s'en étonne.",
            notes="Diapo à photographier. Faire pratiquer l'intonation montante : c'est "
                  "elle qui transforme le chiffre répété en question.")

    d.tableau('Analyse', "Deux façons de faire répéter",
              ['La situation', 'Ce qu\'on dit'],
              [["Vous avez cru entendre le prix",
                "« Vingt-deux dollars ? Vingt-deux ? »"],
               ["Vous n'avez rien saisi du tout",
                "« Est-ce que vous pouvez répéter, s'il vous plaît ? »"],
               ["C'est allé trop vite",
                "« Un peu moins vite, s'il vous plaît. »"],
               ["Vous voulez le voir écrit",
                "« Est-ce que vous pouvez me l'écrire ? »"]],
              cle=1,
              note="Les quatre sont normales. Aucune ne gêne la personne devant vous.",
              notes="Diapo à photographier. La dernière ligne surprend souvent : dire au "
                    "groupe qu'un préposé écrit un chiffre sans hésiter si on le demande.")

    d.vocabulaire('Les prix du comptoir', "En toutes lettres", [
        ("un dollar quarante-quatre", "un timbre à l'unité — 1,44 $"),
        ("un dollar vingt-quatre", "un timbre acheté en carnet — 1,24 $"),
        ("vingt-deux dollars", "le colis standard de Québec à Calgary — 22 $"),
        ("trente-huit dollars", "le même colis en Xpresspost — 38 $"),
        ("treize dollars quinze", "le supplément du courrier recommandé — 13,15 $"),
        ("huit dollars cinquante", "un mandat-poste, jusqu'à mille dollars — 8,50 $"),
    ], notes="Lire chaque prix à voix haute, une fois vite, une fois lentement. Faire "
             "écrire les chiffres sur la fiche pendant la lecture rapide : c'est "
             "l'exercice réel du comptoir.")

    d.regle("Un mot à connaître pour les délais",
            "un jour ouvrable",
            precision="Un jour où les bureaux sont ouverts : du lundi au vendredi, "
                      "sans les jours fériés. « Deux jours ouvrables » un vendredi "
                      "veut dire mardi, pas dimanche.",
            notes="Diapo à photographier. Faire calculer ensemble : un colis Xpresspost "
                  "déposé le vendredi arrive le mardi. C'est la source de malentendu la "
                  "plus fréquente avec les délais.")

    d.pratique('Écoute', "Écrivez le prix en chiffres",
               "Écoutez la phrase, puis écrivez le prix.", [
        ("« Un timbre à l'unité, ça coûte un dollar quarante-quatre. »", "1,44 $"),
        ("« En carnet, un dollar vingt-quatre par timbre. »", "1,24 $"),
        ("« Le colis standard, vingt-deux dollars. »", "22 $"),
        ("« L'Xpresspost, trente-huit dollars. »", "38 $"),
        ("« Le recommandé, treize dollars quinze en plus. »", "13,15 $"),
        ("« Un mandat-poste, huit dollars cinquante. »", "8,50 $"),
    ], corrige=True, cols=2,
       notes="Lire chaque phrase deux fois, à vitesse normale. Ne pas ralentir : c'est "
             "précisément l'entraînement. Les élèves qui n'y arrivent pas emploient la "
             "phrase de la diapositive précédente.")

    d.pratique('Compréhension', "Quelle réponse donne la préposée ?",
               "Associez la question à la réponse.", [
        ("« Un timbre à l'unité, ça coûte combien ? »", "un dollar quarante-quatre"),
        ("« Et si je prends un carnet ? »", "un dollar vingt-quatre par timbre : c'est moins cher"),
        ("« Combien de temps, le colis standard ? »", "à peu près une semaine, d'un bout à l'autre du pays"),
        ("« Et l'Xpresspost ? »", "un ou deux jours ouvrables, avec une garantie"),
        ("« Le recommandé, c'est en plus ? »", "treize dollars quinze, en plus de l'affranchissement"),
        ("« Un mandat-poste, ça coûte quelque chose ? »", "huit dollars cinquante, jusqu'à mille dollars"),
    ], corrige=True,
       notes="C'est l'exercice `t1prix` du module interactif, qui se fait par "
             "glisser-déposer. Le faire ici à l'oral, puis à l'écran.")

    d.piege(
        "Après la réponse",
        "D'accord, merci. (sans avoir compris)",
        "Vingt-deux dollars ? Vingt-deux ?",
        "Dire « d'accord » quand on n'a pas compris est le réflexe le plus coûteux du "
        "module : on paie un prix qu'on n'a pas choisi, et on ne s'en aperçoit qu'en "
        "regardant le reçu dehors. Répéter le chiffre prend deux secondes.",
        notes="Demander qui l'a déjà fait. Presque tout le monde. C'est le moment de la "
              "semaine où le groupe se détend le plus : le dire, et en profiter.")

    d.billet(
        "Écrivez un prix que vous avez entendu cette semaine, en toutes lettres.",
        exemples=[
            "À l'épicerie, à l'autobus, à la pharmacie ?",
            "Est-ce que vous l'avez fait répéter ?",
        ],
        notes="Deux minutes. Corriger l'orthographe des nombres au passage : « quarante-"
              "quatre », « treize », « huit ». Le trait d'union se perd souvent.")

    return d.save(dossier)
