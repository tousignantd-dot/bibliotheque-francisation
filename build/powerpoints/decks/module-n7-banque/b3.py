# -*- coding: utf-8 -*-
"""B3 · Demander sans exiger, supposer sans promettre
Bloc B « Défi 1 · Emprunter moins cher » · couleur ambre · 75 min.
Source : exercice `t1cond` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre='Demander sans exiger, supposer sans promettre',
        chapeau="Le conditionnel présent sert trois fois dans le même "
                "rendez-vous : pour demander, pour supposer, et pour annoncer "
                "un chiffre sans l'engager.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire, mais entièrement tournée vers l'oral du bloc E. "
                  "Chaque forme travaillée ici est une phrase que l'élève dira au "
                  "conseiller.")

    d.objectifs([
        "former le conditionnel présent de six verbes courants ;",
        "demander au conditionnel sans perdre en précision ;",
        "construire une hypothèse avec si et l'imparfait ;",
        "distinguer à l'écrit -rai et -rais.",
    ], notes="Le quatrième objectif est le seul qui soit purement écrit, et il compte "
             "pour la lettre du bloc E : « je paierai » engage, « je paierais » suppose.")

    d.declencheur(
        'Observation', "« Je veux le papier » ou « je voudrais le papier » : qu'est-ce "
                       "qui change ?",
        pistes=[
            "Le contenu de la demande change-t-il ?",
            "Laquelle des deux laisse à l'autre la possibilité de dire non ?",
            "Laquelle des deux obtient le papier, selon toi ?",
            "Est-ce que la politesse rend la demande plus floue ?",
        ],
        notes="La dernière question est la vraie : beaucoup d'élèves croient qu'être "
              "poli, c'est être vague. Montrer que le chiffre reste le même.")

    d.regle("Radical du futur, terminaisons de l'imparfait",
            "Il n'y a rien d'autre à savoir : -ais, -ais, -ait, -ions, -iez, -aient.",
            precision="Tout verbe irrégulier au futur l'est au conditionnel, de la même "
                      "façon. Si vous savez dire « je serai », vous savez dire « je "
                      "serais ». Le radical garde toujours son r : c'est lui qu'on "
                      "entend avant la terminaison.",
            notes="Diapositive à photographier. Faire conjuguer « pouvoir » au tableau "
                  "aux six personnes, puis au futur, pour montrer le radical commun.")

    d.cartes('Conjugaison', "Les six du rendez-vous", [
        ('être', 'ce serait possible de'),
        ('avoir', 'vous auriez un exemple'),
        ('pouvoir', 'pourriez-vous répéter'),
        ('vouloir', 'je voudrais comprendre'),
        ('devoir', 'je devrais regarder mon dossier'),
        ('faire', 'ça ferait combien par mois'),
    ], notes="Faire répéter chaque forme dans sa phrase, jamais isolée. C'est la phrase "
             "que l'élève réemploiera, pas le verbe.")

    d.tableau('Analyse', "La même chose, sans et avec",
              ['Sans conditionnel', 'Avec conditionnel'],
              [['Je veux le papier.', "Je voudrais le papier, s'il vous plaît."],
               ['Répétez.', 'Pourriez-vous répéter ?'],
               ['Vous avez un exemple ?', 'Vous auriez un exemple ?'],
               ['Ça fait combien ?', 'Ça ferait combien, sur mille dollars ?'],
               ["C'est possible d'attendre ?", "Ce serait possible d'attendre ?"]],
              cle=0,
              notes="Diapositive à photographier. Faire remarquer que la colonne de "
                    "droite ne contient aucun mot vague : le chiffre y est toujours.")

    d.regle("Après si, jamais de conditionnel",
            "Si je prenais la marge, je paierais moitié moins.",
            precision="La moitié de phrase qui commence par « si » porte l'imparfait ; "
                      "l'autre moitié porte le conditionnel. L'ordre des deux moitiés "
                      "n'a aucune importance, mais la répartition, si. « Si je "
                      "prendrais » s'entend souvent et se corrige vite.",
            notes="Diapositive à photographier. Faire produire cinq phrases sur ce "
                  "patron avec les chiffres du module.")

    d.pratique('Application', "Mettez le verbe au conditionnel présent",
               "Le verbe est entre parenthèses.", [
        ("(Pouvoir) ___-vous me mettre ce calcul sur un papier ?", "Pourriez"),
        ("Je (vouloir) ___ comprendre la différence avant de signer.", "voudrais"),
        ("Si je prenais la marge, je (payer) ___ moitié moins.", "paierais"),
        ("Avec le prêt, la dette (être) ___ finie dans six ans.", "serait"),
        ("Sur mille dollars, ça (faire) ___ combien ?", "ferait"),
        ("Vous (avoir) ___ un exemple avec mes chiffres ?", "auriez"),
        ("Je (devoir) ___ d'abord regarder mon dossier.", "devrais"),
    ], corrige=True,
       notes="Faire lire chaque phrase à voix haute après correction, avec la bonne "
             "intonation : la demande monte à la fin.")

    d.piege('Le piège', "je paierai / je paierais",
            "décidé / hypothétique",
            "Une lettre, et la promesse devient une supposition. À l'oral la différence "
            "est mince ; à l'écrit, elle engage. Dans la lettre du bloc E, écrire « je "
            "paierai » là où l'on voulait dire « je paierais » revient à s'engager sur "
            "un montant qu'on n'a pas accepté.",
            notes="Faire écrire les deux formes côte à côte au tableau. Le -s final est "
                  "la seule marque, et il ne s'entend pas.")

    d.billet("Écris deux phrases que tu diras à ton prochain rendez-vous : une demande "
             "et une hypothèse.",
             exemples=["Pourriez-vous me mettre le calcul par écrit ?",
                       "Si je payais deux cents dollars de plus, je finirais quand ?"],
             notes="Deux minutes. Corriger surtout la deuxième : c'est là que le "
                   "conditionnel après « si » réapparaît.")

    return d.save(dossier)
