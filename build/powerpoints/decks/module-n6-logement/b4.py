# -*- coding: utf-8 -*-
"""B4 · Ne pas tout redire
Bloc B « Défi 1 · Ce que dit le site » · couleur ambre · 90 min.
Source : exercices `t1en` et `t1ou`, leurs mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="Ne pas tout redire",
        chapeau="« Il en dispose », « elle le sait », « le jour où ». Les "
                "petits mots qui tiennent un texte suivi, et qui font perdre "
                "le fil quand on ne les rattache pas.",
        duree='90 minutes')

    d.titre(notes="Séance de grammaire du texte. C'est ce qui distingue le niveau 6 "
                  "des niveaux 3 et 5 : on ne travaille plus la phrase seule, on "
                  "travaille ce qui relie deux phrases.")

    d.objectifs([
        "rattacher « en » à ce qui vient après « de » ;",
        "rattacher « le » à toute une idée ;",
        "employer « où » pour un lieu et pour un moment ;",
        "choisir entre qui, que et où en trois essais.",
    ], notes="Les deux premiers objectifs sont de compréhension, les deux derniers de "
             "production. Ne pas mélanger : on ne demande pas d'employer « en » "
             "spontanément à ce stade, on demande de savoir à quoi il renvoie.")

    d.declencheur(
        'Observation', "« Il en dispose. » De quoi parle-t-on ?",
        pistes=[
            "Que faut-il avoir lu avant pour comprendre ?",
            "Pourquoi la page n'écrit-elle pas « il dispose de quinze jours » ?",
            "Que se passe-t-il si on saute la phrase d'avant ?",
        ],
        notes="Projeter la phrase seule, sans contexte. Personne ne peut répondre — "
              "c'est la démonstration. Ajouter ensuite la phrase précédente : tout "
              "s'éclaire d'un coup.")

    d.tableau('Analyse', "Le verbe commande le pronom",
              ['Le verbe demande', 'Le pronom'],
              [["parler de, disposer de", "en"],
               ["avoir besoin de, répondre de", "en"],
               ["savoir, dire, ignorer", "le"],
               ["voir, comprendre", "le"]],
              cle=0,
              note="Posez la question au verbe, pas au mot repris.",
              notes="Diapositive à photographier. La règle est mécanique et c'est ce "
                    "qui la rend sûre : ce n'est pas le sens du mot qui décide, c'est "
                    "la construction du verbe.")

    d.cartes('Détail', "Deux emplois, deux tests", [
        ("« en » reprend un groupe en « de »", "La page parle du délai : elle en parle. Elle a besoin d'une preuve : elle en a besoin. Le test : le verbe demande-t-il « de » ?"),
        ("« le » reprend une idée entière", "Le silence vaut consentement. Elle le sait. Ici, « le » ne remplace pas un objet mais toute la phrase d'avant. Le test : peut-on dire « cela » ?"),
        ("La place du pronom", "Devant le verbe conjugué, toujours. Aux temps composés, devant l'auxiliaire : « elle en a parlé », jamais « elle a en parlé »."),
        ("« en » ne remplace pas une personne", "Je parle de monsieur Tardif donne « je parle de lui », pas « j'en parle ». Les personnes gardent leur pronom à elles."),
    ], notes="Faire produire un exemple de classe pour chaque carte, tiré du dossier "
             "et non inventé de nulle part. Un exemple qui vient du texte se retient ; "
             "un exemple abstrait se perd.")

    d.pratique('Pratique', "« en » ou « le » ?",
               "Complétez la deuxième phrase.", [
        ("La page parle d'un délai. Farida … parle aussi.", "en"),
        ("Le silence vaut consentement. Elle … sait.", "le"),
        ("Elle a besoin d'une preuve. Elle … a besoin.", "en"),
        ("L'avis doit nommer la personne. La page … répète deux fois.", "le"),
        ("Il dispose de quinze jours. Il … dispose jusqu'au 3 décembre.", "en"),
        ("Le refus doit être écrit. Beaucoup ne … savent pas.", "le"),
    ], corrige=True,
       notes="Faire justifier chaque réponse par la question au verbe. Corriger le "
             "raisonnement, pas seulement le mot : c'est le raisonnement qui servira "
             "sur une phrase nouvelle.")

    d.regle("« où » rattache un lieu, et aussi un moment",
            "Le jour où, l'année où, le mois où.",
            precision="C'est l'emploi qu'on oublie. « Le trois décembre est le "
                      "jour où le délai finit » — pas « que ». À l'oral, « le jour "
                      "que je suis arrivée » s'entend partout ; à l'écrit, dans un "
                      "avis ou un courriel, « où » est ce qui distingue tout de "
                      "suite un texte tenu d'un texte parlé.",
            notes="Diapositive à photographier. Trois essais pour trancher : « il » "
                  "donne qui, « le » donne que, « là » donne où. Le faire dire à voix "
                  "haute avant l'exercice.")

    d.pratique('Pratique', "qui, que ou où ?",
               "Complétez chaque phrase avec un seul mot.", [
        ("Limoilou est le quartier … elle habite.", "où"),
        ("Le trois décembre est le jour … le délai finit.", "où"),
        ("L'avis … elle a remis porte un nom.", "qu'"),
        ("Le locateur … refuse doit écrire ses motifs.", "qui"),
        ("L'année … elle est arrivée, elle ne parlait pas français.", "où"),
        ("La page … elle a lue répond à ses questions.", "qu'"),
    ], corrige=True,
       notes="Les trois essais à chaque ligne, à voix haute. L'exercice interactif "
             "reprend la même liste ; ce qui se fait ici de vive voix s'y fera au "
             "clavier, avec la correction immédiate.")

    d.billet(
        "Écrivez une phrase avec « le jour où ».",
        exemples=[
            "Une seule phrase.",
            "Parlez d'une vraie date, la vôtre.",
        ],
        notes="Deux minutes. Ceux qui écrivent « le jour que » sont ceux à reprendre "
              "individuellement : la faute est tenace parce qu'elle est correcte à "
              "l'oreille.")

    return d.save(dossier)
