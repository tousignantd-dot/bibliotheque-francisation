# -*- coding: utf-8 -*-
"""B4 · Les mots du transport.
Bloc B · couleur acier · 60 min.
Source : exercices `t1metro` et `t1quai`, cartes mémoire.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-deplacement/images/')


def build(dossier):
    d = Deck(
        code='B4', section='acier',
        titre='Les mots du transport',
        chapeau="Terminus, quai, correspondance, direction, fréquence. Six mots "
                "suffisent pour lire n'importe quel réseau de transport — et "
                "pour poser les bonnes questions.",
        duree='60 minutes')

    d.titre(notes="Séance de vocabulaire qui clôt le bloc B. Si possible, projeter le plan "
                  "de réseau réel de la région : les élèves reconnaissent leur trajet.")

    d.objectifs([
        "nommer les six éléments d'un réseau de transport ;",
        "comprendre qu'un même numéro circule dans les deux sens ;",
        "distinguer une fréquence d'une heure de départ ;",
        "poser les quatre questions du tableau de B1 sans les relire.",
    ])

    d.declencheur(
        'Observation', "Où sommes-nous ? Quels mots connaissez-vous déjà ?",
        image=IMG + 'quai-metro.jpg',
        pistes=[
            "Comment s'appelle l'endroit où on attend ?",
            "À quoi sert la ligne peinte au sol ?",
            "Où regarde-t-on pour savoir si on est du bon côté ?",
            "Que se passe-t-il si on se trompe de quai ?",
        ],
        notes="Attendre le mot « quai ». La ligne au sol est une ligne de sécurité : "
              "l'expliquer, plusieurs élèves ne l'ont jamais remarquée.")

    d.vocabulaire('Vocabulaire · 1 de 2', "Le réseau", [
        ("un terminus", "Le dernier arrêt d'une ligne — c'est lui qui donne la direction."),
        ("un quai", "L'endroit où on attend avant de monter."),
        ("une correspondance", "Le changement d'une ligne à une autre pendant le même trajet."),
        ("la direction", "Le sens dans lequel va un véhicule."),
        ("le trajet", "Le chemin complet, du départ à l'arrivée."),
    ], notes="Faire répéter chaque mot avec son article. « Une correspondance » est le mot "
             "le plus long et le plus utile : le faire dire trois fois.")

    d.vocabulaire('Vocabulaire · 2 de 2', "Ce qui se lit et ce qui se paie", [
        ("un titre de transport", "La carte ou le billet qui donne le droit de monter."),
        ("la fréquence", "Le temps entre deux passages : « aux quinze minutes »."),
        ("un horaire", "Le tableau des heures de passage."),
        ("desservir un arrêt", "S'y arrêter. Un autobus qui ne dessert pas un arrêt passe tout droit."),
        ("une interruption de service", "L'arrêt temporaire d'une ligne."),
    ], notes="« Desservir » et « interruption de service » sont les deux mots des annonces. "
             "Ils reviennent au bloc D.")

    d.tableau('Analyse', "Fréquence ou heure de départ ?",
              ['Ce qu\'on entend', 'Ce que ça veut dire'],
              [["Aux quinze minutes", "un passage toutes les 15 minutes"],
               ["À 7 h 51", "un seul départ, à cette heure-là"],
               ["Aux heures", "un passage par heure, souvent à l'heure pile"],
               ["Toutes les heures", "la même chose que « aux heures »"]],
              cle=0,
              note="Une fréquence ne dit pas quand le prochain passe : elle dit combien de "
                   "temps il faut attendre, au pire.",
              notes="La confusion entre les deux fait manquer beaucoup d'autobus. Y "
                    "consacrer cinq minutes pleines.")

    d.regle("Le même numéro, deux directions",
            "L'autobus 45 existe dans les deux sens, avec le même numéro.",
            precision="Ce qui les distingue, c'est le nom du terminus — et le côté de la "
                      "rue. L'arrêt d'en face porte le même numéro de ligne, mais va dans "
                      "l'autre direction. Vérifier avant de monter coûte cinq secondes.",
            notes="Diapo à photographier. C'est l'erreur que Nour commet vraiment au bloc C.")

    d.piege('Suivre la foule',
            "Tout le monde descend là, je descends aussi.",
            "Je vérifie le nom de la station avant de descendre.",
            "La foule descend souvent à la station la plus fréquentée, qui n'est presque "
            "jamais la vôtre. Suivre le mouvement fonctionne une fois sur trois — c'est-à-dire "
            "qu'il vous fait descendre au mauvais endroit deux fois sur trois.",
            notes="Faire raconter au groupe une fois où c'est arrivé. Il y en a toujours.")

    d.pratique('Pratique', "Le mot juste",
               "Complétez avec le mot du vocabulaire.", [
        ("Le dernier arrêt de la ligne s'appelle le ___.", "terminus"),
        ("Changer de ligne en cours de trajet, c'est faire une ___.", "correspondance"),
        ("Attendez sur le ___, derrière la ligne jaune.", "quai"),
        ("« Aux quinze minutes » indique la ___.", "fréquence"),
        ("Cet autobus ne ___ pas l'arrêt aujourd'hui, à cause des travaux.", "dessert"),
        ("Il faut avoir un ___ de transport valide pour monter.", "titre"),
    ], corrige=True,
       notes="Ces six mots sont dans le banc de vocabulaire du module.")

    d.billet(
        "Décrivez votre ligne d'autobus ou de métro : numéro, terminus, fréquence, durée.",
        exemples=[
            "Si vous venez à pied, décrivez la ligne la plus proche de chez vous.",
            "Indiquez le nom du terminus dans les deux directions.",
        ],
        notes="Bilan du bloc B. Le dernier point — les deux directions — demande souvent "
              "une vérification à la maison. C'est voulu.")

    return d.save(dossier)
