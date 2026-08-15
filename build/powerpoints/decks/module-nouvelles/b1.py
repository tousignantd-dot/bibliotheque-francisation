# -*- coding: utf-8 -*-
"""B1 · Une fillette retrouve son chat.
Bloc B · couleur acier (compréhension orale) · 60 min.
Source : nouvelle `t1` et exercice `t1chat`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre='Une fillette retrouve son chat',
        chapeau="Quatre phrases à la radio, et toute une histoire : un chat disparu, une "
                "affiche fabriquée en classe, une voisine attentive. Le fait divers "
                "type, en trente secondes.",
        duree='60 minutes')

    d.titre(notes="Ouverture du défi 1. Rappeler la grille des cinq questions de A4 : "
                  "c'est avec elle qu'on écoute.")

    d.objectifs([
        "comprendre un fait divers lu à la radio ;",
        "repérer l'ordre réel des événements, différent de l'ordre du texte ;",
        "répondre par une phrase complète ;",
        "reconnaître le vocabulaire d'un fait divers.",
    ])

    d.dialogue('La nouvelle · 1 de 2', "À Gatineau, une fillette de six ans", [
        ("LE JOURNALISTE", "À Gatineau, une fillette de six ans a retrouvé son chat "
                           "disparu grâce à une affiche fabriquée dans le cadre d'un "
                           "projet scolaire.", True),
        ("LE JOURNALISTE", "Le chat, prénommé Mistigri, s'était sauvé par une fenêtre "
                           "entrouverte il y a trois jours.", True),
    ], consigne="Écoutez deux fois, diapo masquée. Cherchez les cinq réponses.",
       notes="Passer l'audio du défi 1. La première phrase répond à quatre des cinq "
             "questions. Faire compter.")

    d.dialogue('La nouvelle · 2 de 2', "Une voisine a reconnu l'animal", [
        ("LE JOURNALISTE", "La fillette a distribué des affiches dans le quartier avec "
                           "l'aide de sa classe.", True),
        ("LE JOURNALISTE", "Une voisine a reconnu l'animal dans sa cour hier matin et a "
                           "aussitôt averti la famille.", True),
    ], notes="Faire remarquer « aussitôt » : un marqueur de temps de la séance A3, dans "
             "un vrai texte.")

    d.tableau('Analyse', "Le texte et l'ordre réel",
              ['Ordre du texte', 'Ordre réel'],
              [["le chat est retrouvé", "le chat se sauve, il y a trois jours"],
               ["le chat s'était sauvé", "la classe fabrique des affiches"],
               ["la classe fabrique des affiches", "la fillette les distribue"],
               ["la voisine reconnaît l'animal", "la voisine reconnaît l'animal, hier"],
               ["la voisine avertit la famille", "la famille est avertie"]],
              cle=1,
              note="Le texte commence par la fin. C'est la règle des nouvelles : on donne "
                   "le résultat d'abord.",
              notes="Faire relire le texte en suivant l'ordre réel. Les élèves "
                    "comprendront pourquoi ils avaient l'impression de perdre le fil.")

    d.regle("La règle du fait divers",
            "On commence par le résultat, puis on remonte dans le temps.",
            precision="« Une fillette a retrouvé son chat » — c'est la fin de "
                      "l'histoire, et c'est la première phrase. Le lecteur pressé a "
                      "l'essentiel ; celui qui continue apprend comment on en est "
                      "arrivé là.",
            notes="Relier à la séance A4 : c'est la même logique du plus important au "
                  "moins important, appliquée au temps.")

    d.pratique('Pratique · 1 de 4', "Le chat retrouvé",
               "Répondez par une phrase complète.", [
        ("Qu'est-ce que la fillette a perdu ?", "Elle a perdu son chat, Mistigri."),
        ("Comment a-t-elle retrouvé son chat ?",
         "Grâce à une affiche fabriquée avec sa classe."),
        ("Qui a reconnu le chat dans sa cour ?", "Une voisine."),
        ("Depuis combien de temps le chat était-il disparu ?", "Depuis trois jours."),
        ("Par où le chat s'était-il sauvé ?", "Par une fenêtre entrouverte."),
    ], corrige=True,
       notes="Insister sur la phrase complète : « son chat » seul ne répond pas à la "
             "question. C'est un travail d'expression, pas seulement de compréhension.")

    d.pratique('Pratique · 2 de 4', "Les cinq questions",
               "Appliquez la grille de la séance A4.", [
        ("Qui ?", "une fillette de six ans, sa classe, une voisine"),
        ("Quoi ?", "elle a retrouvé son chat disparu"),
        ("Où ?", "à Gatineau, dans son quartier"),
        ("Quand ?", "le chat s'est sauvé il y a trois jours, retrouvé hier matin"),
        ("Pourquoi ?", "grâce à une affiche d'un projet scolaire"),
    ], corrige=True,
       notes="Le « quand » demande deux réponses : c'est fréquent dans un fait divers qui "
             "couvre plusieurs jours.")

    d.piege("Le piège du « il y a trois jours »",
            "Le chat est parti il y a trois jours à partir d'aujourd'hui.",
            "Trois jours avant le moment du reportage.",
            "Un marqueur de temps se compte à partir du moment où la nouvelle est dite. "
            "Si vous réécoutez le bulletin une semaine plus tard, « il y a trois jours » "
            "ne désigne plus le même jour. Cherchez toujours la date de diffusion.",
            notes="Point pratique pour les élèves qui écoutent des balados ou des "
                  "rediffusions.")

    d.pratique('Pratique · 3 de 4', "Vrai ou faux",
               "D'après la nouvelle.", [
        ("Le chat s'appelle Mistigri.", "VRAI"),
        ("La fillette a fabriqué l'affiche toute seule.", "FAUX — avec l'aide de sa classe"),
        ("Le chat est sorti par une porte ouverte.", "FAUX — par une fenêtre entrouverte"),
        ("C'est une voisine qui a trouvé le chat.", "VRAI"),
        ("La famille a été avertie tout de suite.", "VRAI — aussitôt"),
    ], corrige=True,
       notes="Les deuxième et troisième énoncés changent un seul mot du texte. C'est le "
             "type de piège des vrais examens de compréhension.")

    d.pratique('Pratique · 4 de 4', "Racontez dans l'ordre réel",
               "Cinq phrases, du plus ancien au plus récent.", [
        ("Étape 1", "Il y a trois jours, le chat s'est sauvé par une fenêtre entrouverte."),
        ("Étape 2", "La classe de la fillette a fabriqué des affiches."),
        ("Étape 3", "La fillette a distribué les affiches dans le quartier."),
        ("Étape 4", "Hier matin, une voisine a reconnu le chat dans sa cour."),
        ("Étape 5", "Elle a aussitôt averti la famille."),
    ], corrige=True,
       notes="Faire dire les cinq phrases d'un seul trait par un élève. C'est le récit "
             "chronologique, celui qu'on emploie à l'oral.")

    d.billet(
        "Racontez le fait divers du chat en cinq phrases, dans l'ordre réel.",
        exemples=[
            "Un marqueur de temps au début de chaque phrase.",
            "Du plus ancien au plus récent.",
        ],
        notes="Ces récits serviront en B5, où ils seront racontés à voix haute sans "
              "notes.")

    return d.save(dossier)
