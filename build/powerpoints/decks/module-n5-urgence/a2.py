# -*- coding: utf-8 -*-
"""A2 · « Ambulance » et « nom » : deux sons qui passent par le nez.
Bloc A « Je découvre » · couleur indigo · 75 min. Graphie-phonie.
Source : exercice `prPhon` et sa mini-leçon.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-urgence/images/')


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="« Ambulance » et « nom »",
        chapeau="Deux voyelles nasales, une seule différence : la bouche "
                "s'ouvre ou s'arrondit. Au téléphone, avec du bruit "
                "derrière, c'est tout ce que le répartiteur a pour vous "
                "comprendre.",
        duree='75 minutes')

    d.titre(notes="Séance de phonétique. Prévenir dès le départ que la difficulté n'est "
                  "pas de reconnaître les sons, mais de les produire sous pression. "
                  "Faire ouvrir l'activité interactive en fin de séance seulement.")

    d.objectifs([
        "distinguer à l'oreille le son de « ambulance » et celui de « nom » ;",
        "produire les deux en surveillant l'ouverture de la bouche ;",
        "reconnaître les quatre graphies de chaque son ;",
        "savoir quand la voyelle cesse d'être nasale.",
    ])

    d.declencheur(
        'Écoute', "« Elle est tombée » ou « elle est tendue » ? Une seule voyelle "
                  "sépare les deux.",
        image=IMG + 'telephone-nuit.jpg',
        pistes=[
            "Est-ce que ce sont deux prononciations d'un même mot ?",
            "Qu'est-ce que le répartiteur comprend, dans chaque cas ?",
            "Où passe l'air, quand on dit « on » ?",
            "Qu'est-ce qui bouge : la langue, les lèvres, la mâchoire ?",
        ],
        notes="Dire les deux phrases soi-même, dos tourné au groupe, et faire lever la "
              "main. L'erreur de perception est fréquente : elle justifie la séance.")

    d.regle("Deux nasales, une seule différence",
            "Pour « an », la bouche s'ouvre grand ; pour « on », les lèvres s'arrondissent.",
            precision="Dans les deux cas, l'air passe par le nez et la consonne écrite — "
                      "le n ou le m — ne se prononce pas. Elle indique la nasalité, rien "
                      "de plus.",
            notes="Diapositive à photographier. Faire poser une main devant la bouche : "
                  "pour « on », très peu d'air sort. S'il en sort beaucoup, on dit « o ».")

    d.tableau('Les graphies', "Ce qu'on écrit, ce qu'on entend",
              ['On écrit', 'On entend', 'Dans le module'],
              [["an, am", "« an »", "quarante · une ambulance"],
               ["en, em", "« an »", "l'attente · le temps"],
               ["on", "« on »", "le salon · on répond"],
               ["om", "« on »", "elle est tombée · le nom"],
               ["in, ain, ein", "« in » — la troisième", "quinze · un médecin"]],
              cle=1,
              note="Le m remplace le n devant b et p : chambre, ambulance, temps.",
              notes="La cinquième ligne prévient la confusion la plus fréquente après "
                    "celle du jour : « quinze » n'est ni « quand » ni « quond ».")

    d.pratique('Discrimination', "« an » ou « on » ?",
               "L'enseignante dit le mot ; les élèves lèvent une main ou deux.", [
        ("une ambulance", "« an »"),
        ("le nom", "« on »"),
        ("elle est tombée", "« on »"),
        ("l'attente", "« an »"),
        ("on répond", "« on »"),
        ("la chambre", "« an »"),
        ("un moment", "« an »"),
        ("le salon", "« on »"),
        ("quarante", "« an »"),
        ("ils sont", "« on »"),
    ], corrige=True,
       notes="Dix mots, dos tourné au groupe pour couper l'indice visuel des lèvres. "
             "Reprendre ensuite face à eux, en exagérant : c'est là qu'ils comprennent "
             "ce qui bouge.")

    d.cartes("Cinq paires à faire entendre", "Une seule voyelle change", [
        ("sans / son", "Elle est arrivée sans son sac."),
        ("banc / bon", "Le banc de la salle d'attente n'est pas bon pour son dos."),
        ("temps / ton", "Prends ton temps pour répondre."),
        ("lent / long", "Le triage est lent et le corridor est long."),
        ("tombée / tendue", "Elle est tombée. Elle est tendue. Ce n'est pas pareil."),
        ("bon / bonne", "Le premier est nasal, le second ne l'est pas."),
    ], cols=3,
       notes="La dernière paire introduit la dénasalisation : dès qu'une double consonne "
             "ou une voyelle suit, le son redevient oral. C'est le point suivant.")

    d.regle("La nasale disparaît devant une voyelle ou une double consonne",
            "bon devient bonne · an devient année · immédiat n'est pas nasal.",
            precision="Le n ou le m qui « ferme » la voyelle doit rester seul, en fin de "
                      "syllabe. Dès qu'il commence la syllabe suivante, la voyelle "
                      "redevient orale.",
            notes="Faire dire la paire bon / bonne dix fois en alternance. C'est le seul "
                  "exercice qui installe vraiment la règle.")

    d.piege("Prononcer le n ou le m",
            "am-bou-lan-ce, avec un m entendu.",
            "ambulance, en trois syllabes, sans aucun m.",
            "Dans une voyelle nasale, la consonne écrite ne se prononce jamais. Elle dit "
            "seulement que l'air passe par le nez.",
            notes="Erreur presque universelle chez les personnes hispanophones et "
                  "arabophones. La nommer sans dramatiser : elle se corrige en une "
                  "semaine de répétition.")

    d.pratique('Production', "À dire d'un trait",
               "Chacun lit une phrase à voix haute ; le groupe dit ce qu'il entend.", [
        ("Une ambulance s'en vient, restez près d'elle.", "« an » trois fois"),
        ("On ne la déplace pas et on ne lui donne rien.", "« on » partout"),
        ("Elle est tombée dans l'escalier vers deux heures.", "« on » au début"),
        ("L'attente peut être longue.", "les deux dans la même phrase"),
        ("La tension est bonne, la température descend.", "un mot contient les deux"),
    ], corrige=True,
       notes="La quatrième et la cinquième sont les plus dures : elles obligent la bouche "
             "à changer de forme en cours de phrase. Les faire répéter au ralenti.")

    d.billet(
        "Écrivez trois mots du module avec « an » et trois avec « on ».",
        exemples=[
            "Soulignez la lettre ou les lettres qui font le son.",
            "Ajoutez un mot où les deux se suivent, si vous en trouvez un.",
        ],
        notes="« Tension », « infection » et « intervention » sont les réponses attendues "
              "pour la dernière consigne. Les garder pour la séance C1.")

    return d.save(dossier)
