# -*- coding: utf-8 -*-
"""B2 · Répéter pour être sûr.
Bloc B « Défi 1 » · couleur ambre · 60 min.
Source : dialogue `t1b`, exercices `t1repeter`, `t1b`, mini-leçon `t1repeter`.

La séance de technique du module. Elle n'apprend pas de vocabulaire : elle
apprend ce qu'on fait quand le vocabulaire manque. C'est ce qui distingue un
élève qui se débrouille d'un élève qui reste bloqué.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-autobus/images/')


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre="Répéter pour être sûr",
        chapeau="Vous ne comprendrez pas tout. Ce qui compte, c'est de redire "
                "ce que vous avez compris — la personne corrige aussitôt.",
        duree='60 minutes')

    d.titre(notes="Dire d'emblée au groupe que cette séance ne contient presque pas de "
                  "mots nouveaux. Elle contient une méthode. Le dire change la façon dont "
                  "les élèves l'écoutent.")

    d.objectifs([
        "demander de parler plus lentement ;",
        "demander de répéter ;",
        "redire ce qu'on a compris pour vérifier ;",
        "relancer quand on n'a saisi qu'un mot.",
    ])

    d.declencheur(
        'Situation', "Que faites-vous dans ce cas ?",
        image=IMG + 'plan-quartier.jpg',
        pistes=[
            "Quelqu'un vous explique un chemin, très vite.",
            "Vous avez compris deux mots sur dix.",
            "Que faites-vous ?",
            "Est-ce qu'on peut dire qu'on n'a pas compris ?",
        ],
        notes="Laisser le groupe répondre longuement. Beaucoup diront qu'ils font semblant "
              "d'avoir compris. C'est exactement le point de départ de la séance.")

    d.dialogue('Dialogue', "C'est loin ?", [
        ("HASSAN", "Nadia, tu connais le CLSC ?", True),
        ("NADIA", "Oui, il est près du parc.", True),
        ("HASSAN", "C'est loin de chez moi ?", True),
        ("NADIA", "À pied, vingt minutes. En autobus, cinq.", True),
        ("HASSAN", "Quel autobus ?", True),
    ], consigne="Écoutez, puis comptez les questions de Hassan.",
       notes="Trois questions, une à la fois. Faire remarquer qu'il ne demande jamais deux "
             "choses dans la même phrase : c'est ce qui rend la conversation possible.")

    d.cartes("Trois phrases à savoir par cœur", "Elles servent partout, toute la vie", [
        ("Plus lentement, s'il vous plaît.",
         "La plus utile de toutes. Ce n'est presque jamais le volume qui manque : c'est "
         "la vitesse."),
        ("Vous pouvez répéter ?",
         "Pour réentendre la même phrase. On peut la dire deux fois de suite sans "
         "gêner personne."),
        ("Je n'ai pas compris.",
         "Une phrase honnête et suffisante. Elle n'a jamais fâché personne."),
    ], cols=3, notes="Diapositive à photographier. Faire dire les trois phrases par chaque "
                     "élève, à voix haute. C'est le cœur de la séance.")

    d.regle("Redire, puis vérifier",
            "On répète les mots importants, et on demande « c'est ça ? ».",
            precision="« Tout droit, à droite au feu. <b>C'est ça ?</b> » — On ne redit "
                      "pas toute la phrase : seulement la direction et le repère.",
            notes="Diapositive à photographier. Montrer le dialogue de B1 : Hassan fait "
                  "exactement cela, deux fois.")

    d.piege('Piège', "demander « plus fort »", "demander « plus lentement »",
            "La personne se met à crier, et c'est toujours aussi rapide. Ce dont on a "
            "besoin, c'est de temps entre les mots, pas de volume.",
            notes="Le faire vivre : dire une phrase très vite et fort, puis lentement et "
                  "doucement. Le groupe comprend en dix secondes.")

    d.pratique('Compréhension', "Qu'est-ce qu'on dit ?",
               "Choisissez la bonne phrase.", [
        ("On parle trop vite.", "Plus lentement, s'il vous plaît."),
        ("On n'a rien compris.", "Pardon, je n'ai pas compris. Vous pouvez répéter ?"),
        ("On a saisi un seul mot.", "Au feu ? Et après ?"),
        ("On veut vérifier avant de partir.", "À droite au feu. C'est ça ?"),
    ], corrige=True, cols=1,
       notes="Faire d'abord à l'oral, en groupe. Puis chacun choisit les deux phrases "
             "qu'il apprendra par cœur.")

    d.pratique('Pratique · à trois', "Le chemin brouillé",
               "Un élève explique vite, un autre écoute, le troisième observe.", [
        ("Étape 1", "L'élève A explique un chemin, vite, en une seule phrase."),
        ("Étape 2", "L'élève B fait ralentir, fait répéter, puis redit ce qu'il a compris."),
        ("Étape 3", "L'élève C dit si le chemin est juste."),
        ("Étape 4", "On tourne : chacun passe par les trois rôles."),
    ], cols=1,
       notes="Vingt-cinq minutes. C'est l'exercice le plus utile du module. Insister pour "
             "que A parle vraiment vite : sinon B n'a rien à faire.")

    d.billet(
        "Apprenez deux phrases par cœur, et écrivez-les.",
        exemples=[
            "Plus lentement, s'il vous plaît.",
            "Vous pouvez répéter ?",
        ],
        notes="Devoir minuscule. Demander à la séance suivante qui s'en est servi pour de "
              "vrai. Il y en aura.")

    return d.save(dossier)
