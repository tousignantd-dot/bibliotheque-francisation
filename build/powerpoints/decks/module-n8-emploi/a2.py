# -*- coding: utf-8 -*-
"""A2 · La voix qui dit « ce n'est pas fini ».
Bloc A « Je découvre » · couleur indigo · 75 min.
Source : exercice `prProso` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="La voix qui dit « ce n'est pas fini »",
        chapeau="À ce niveau, les sons sont acquis. Ce qui trahit encore, "
                "c'est la mélodie : où la voix monte, où elle descend, et où "
                "l'on respire dans une phrase de vingt-cinq mots.",
        duree='75 minutes')

    d.titre(notes="Séance de prosodie. Elle surprend souvent : les élèves s'attendent à "
                  "travailler des sons. Annoncer d'emblée qu'on ne travaillera aucun son "
                  "aujourd'hui, seulement le rythme et la mélodie.")

    d.objectifs([
        "découper une phrase longue en groupes de souffle ;",
        "faire monter la voix quand la phrase continue ;",
        "la faire descendre franchement quand elle finit ;",
        "placer l'accent sur la dernière syllabe du groupe, jamais sur chaque mot.",
    ], notes="Le quatrième objectif est le plus difficile pour les locuteurs de langues "
             "à accent de mot — l'espagnol, l'arabe, le russe.")

    d.regle("La règle, en une ligne",
            "La voix monte tant que la phrase n'est pas finie ; elle descend au dernier groupe.",
            precision="C'est tout. Un groupe qui finit en haut annonce une suite ; un "
                      "groupe qui finit en bas ferme la porte et rend la parole. Une "
                      "énumération monte, monte, monte, puis descend au dernier "
                      "élément : « les décisions, la personne, la date ».",
            notes="Diapositive à photographier. Le reste de la séance n'est que "
                  "l'application de cette phrase.")

    d.cartes("Le groupe de souffle", "Le français découpe par le sens", [
        ("Ce que c'est",
         "Un groupe de mots qui va ensemble et se dit d'un seul souffle. Le sens décide du découpage, pas le nombre de mots."),
        ("Où l'on respire",
         "Entre les groupes, jamais au milieu de l'un d'eux. Respirer après « le premier » et avant « bloc » rend la phrase incompréhensible."),
        ("Où tombe l'accent",
         "Sur la dernière syllabe du groupe. Une seule par groupe — accentuer chaque mot revient à n'accentuer nulle part."),
        ("Pourquoi ça compte ici",
         "Une réunion dure une heure. Un collègue qui doit travailler pour vous écouter finira par ne plus écouter."),
    ], notes="Faire dire « Le premier bloc, c'est la réception des commandes, avant "
             "midi » d'abord d'un trait, puis en trois souffles. La différence s'entend "
             "immédiatement.")

    d.tableau('Analyse · 1 de 2', "Trois phrases du module, découpées",
              ['La phrase, barres aux souffles', 'La mélodie'],
              [["Le premier bloc / c'est la réception des commandes / avant midi.",
                "monte, monte, descend"],
               ["Si l'écart est en bas de vingt-cinq dollars / tu approuves.",
                "monte, descend"],
               ["Tu appelles le transporteur / le mardi et le jeudi / et tu notes les retards.",
                "monte, monte, descend"]],
              note="Le dernier groupe descend toujours.",
              notes="Lire chaque ligne à voix haute, puis la faire lire. Marquer la "
                    "montée du geste : la main monte, la main descend.")

    d.tableau('Analyse · 2 de 2', "Trois phrases plus longues",
              ['La phrase, barres aux souffles', 'La mélodie'],
              [["On veut les décisions / qui les applique / et pour quand.",
                "monte, monte, descend"],
               ["Ce que je vois / c'est que j'ai travaillé quatre heures / au-delà de quarante.",
                "monte, monte, descend"],
               ["Je vous saurais gré / de me confirmer la correction / avant le vingt-sept août.",
                "monte, monte, descend"]],
              note="Une énumération monte à chaque élément, puis descend au dernier.",
              notes="La troisième est une formule de lettre d'affaires : elle revient "
                    "en B4. La faire lire deux fois.")

    d.piege("Monter à la fin d'une affirmation",
            "La majoration n'a pas été appliquée ?  (la voix monte)",
            "La majoration n'a pas été appliquée.  (la voix descend)",
            "Une affirmation qui monte se lit comme une question ou comme une "
            "hésitation. Au téléphone, où l'interlocuteur n'a pas votre visage, il "
            "répondra « oui ? » au lieu d'agir — et le dossier n'avance pas. La "
            "descente franche dit : j'ai fini, à vous.",
            notes="Ce piège vaut de l'or au Défi 1. Le rappeler avant le jeu de rôle "
                  "de E1.")

    d.pratique('Écoute', "Ça continue, ou ça finit ?",
               "Écoutez le groupe de mots. La voix monte-t-elle, ou descend-elle ?", [
        ("Le premier bloc, c'est la réception des commandes", "ça continue"),
        ("et c'est moi qui tranche.", "ça finit"),
        ("Si l'écart est en bas de vingt-cinq dollars", "ça continue"),
        ("Envoie-le au groupe avant jeudi.", "ça finit"),
        ("Quand un bon arrive à deux heures de l'après-midi", "ça continue"),
        ("la production planifie sa journée à partir de ça.", "ça finit"),
        ("C'est noté.", "ça finit"),
        ("Les décisions, la personne", "ça continue"),
    ], corrige=True,
       notes="Les extraits sont dans le module, exercice « La phrase continue, ou elle "
             "finit ? ». Les faire écouter deux fois avant de répondre.")

    d.pratique('Production', "Lisez à voix haute",
               "Respectez les barres. Une respiration par barre, pas une de plus.", [
        ("Madame, / je donne suite / à notre conversation téléphonique du 19 août.", ""),
        ("Les 10 et 11 août, / j'ai travaillé quatre heures / au-delà de quarante.", ""),
        ("Si je résume ce que vous venez de dire, / l'écart de prix est réel.", ""),
        ("Je proposerais un partage : / les pièces courantes chez l'un, / l'urgent chez l'autre.", ""),
    ], notes="Chacun lit une phrase. Corriger seulement la mélodie, jamais les sons — "
             "ce n'est pas la séance pour ça, et deux corrections à la fois n'en font "
             "aucune.")

    d.billet(
        "Enregistrez-vous en lisant les quatre phrases de la dernière diapositive.",
        exemples=[
            "Réécoutez-vous : est-ce que le dernier groupe descend ?",
            "Refaites-en une jusqu'à ce que la descente soit franche.",
        ],
        notes="L'enregistrement est le seul moyen d'entendre sa propre mélodie. "
              "Le téléphone suffit.")

    return d.save(dossier)
