# -*- coding: utf-8 -*-
"""A3 · Où est… ? Où sont… ?
Bloc A « Je découvre » · couleur teal · 60 min. Fin du bloc de découverte.
Source : exercices `prImg` et `prOu`, mini-leçon `prOu`.

Une seule question, et le module entier repose dessus. C'est l'intention de
production orale du programme, mot pour mot : se renseigner sur la
localisation.

Le seul point de langue de la séance est l'accord du verbe : « où est » pour
un endroit, « où sont » pour plusieurs. Les toilettes et les casiers, qui
sont toujours au pluriel en français, suffisent à l'installer.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-couloirs/images/')


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre="Où est… ? Où sont… ?",
        chapeau="Poser la question qui sert tous les jours, au singulier "
                "comme au pluriel.",
        duree='60 minutes')

    d.titre(notes="Séance courte et très parlée. Objectif : que chaque élève ait posé "
                  "la question à voix haute au moins dix fois avant de sortir.")

    d.objectifs([
        "reconnaitre six endroits du centre sur une photo ;",
        "poser la question avec « où est » ;",
        "poser la question avec « où sont » ;",
        "commencer par « excusez-moi » et finir par « merci ».",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qu'on voit sur cette photo ?",
        image=IMG + 'comptoir-accueil.jpg',
        pistes=[
            "Qu'est-ce qu'il y a juste après la porte d'entrée ?",
            "À qui est-ce qu'on parle en premier, dans un centre ?",
            "Qu'est-ce qu'on lui demande ?",
            "Comment est-ce qu'on commence la phrase ?",
        ],
        notes="L'accueil est le premier endroit de tout bâtiment public. Faire dire "
              "que c'est là qu'on va quand on ne sait pas : c'est une stratégie, pas "
              "seulement un mot de vocabulaire.")

    d.vocabulaire('Vocabulaire', "Six endroits à reconnaitre", [
        ("l'accueil", "Le premier comptoir, juste après la porte d'entrée."),
        ("le secrétariat", "Le bureau où on va pour son inscription et ses papiers."),
        ("la cafétéria", "La grande salle où on mange le midi."),
        ("les toilettes", "La petite salle avec les lavabos, à chaque étage."),
        ("un casier", "La petite armoire de métal où on laisse son manteau."),
        ("la sortie", "La porte par où on quitte le bâtiment."),
    ], notes="Diapositive à photographier. Insister sur « les toilettes », toujours au "
             "pluriel en français, même quand il n'y a qu'une porte.")

    d.tableau('Analyse', "Un endroit, ou plusieurs ?",
              ["On dit", "Parce que"],
              [["Où est la cafétéria ?", "il y a une cafétéria"],
               ["Où est le secrétariat ?", "il y a un secrétariat"],
               ["Où sont les toilettes ?", "toujours au pluriel en français"],
               ["Où sont les casiers ?", "il y en a beaucoup"]],
              cle=1,
              note="Ce n'est pas le masculin ou le féminin qui décide : c'est le nombre.",
              notes="Diapositive à photographier. Faire chercher d'autres endroits du "
                    "vrai centre et les classer dans les deux colonnes.")

    d.regle("Excusez-moi, où est… ? Merci beaucoup.",
            "Trois temps, toujours les mêmes.",
            precision="On aborde avec « <b>excusez-moi</b> », on pose <b>une seule</b> "
                      "question, on <b>remercie</b>. Deux questions à la fois donnent "
                      "une réponse trop longue, dont on ne retient rien.",
            notes="Diapositive à photographier. C'est la structure que le jeu de rôle "
                  "en ligne vérifie, et celle que la correction regarde en premier.")

    d.pratique('Production orale', "Posez la question",
               "Est-ce que c'est « où est » ou « où sont » ?", [
        ("le local 214", "Où est le local 214 ?"),
        ("les toilettes", "Où sont les toilettes ?"),
        ("la cafétéria", "Où est la cafétéria ?"),
        ("les casiers", "Où sont les casiers ?"),
        ("l'ascenseur", "Où est l'ascenseur ?"),
        ("les escaliers", "Où sont les escaliers ?"),
    ], corrige=True, cols=2,
       notes="Six items, faits à l'oral d'abord. Faire ajouter « excusez-moi » devant "
             "chaque phrase au deuxième tour.")

    d.pratique('Pratique · en circulant', "Dix questions, dix personnes",
               "Debout, chacun pose sa question à quelqu'un d'autre.", [
        ("Étape 1", "Chacun tire un endroit du centre au hasard."),
        ("Étape 2", "Il pose la question à un camarade, avec « excusez-moi »."),
        ("Étape 3", "L'autre répond ce qu'il sait, même approximativement."),
        ("Étape 4", "On remercie, et on change de partenaire."),
    ], cols=1,
       notes="Quinze minutes, et personne ne reste assis. L'étape 3 n'a pas besoin "
             "d'être juste : les vraies réponses viennent au bloc B, avec le plan.")

    d.billet(
        "Écrivez trois questions que vous poseriez demain, au centre, en français.",
        exemples=[
            "Excusez-moi, où est la cafétéria ?",
            "Où sont les toilettes, s'il vous plait ?",
            "Excusez-moi, où est le local 214 ?",
        ],
        notes="Devoir court. Vérifier « est » et « sont » : c'est le seul point de "
              "langue de la séance, et il se corrige en une seconde.")

    return d.save(dossier)
