# -*- coding: utf-8 -*-
"""A2 · Le son AN et le son IN.
Bloc A « Je découvre » · couleur indigo (graphie-phonie) · 60 min.
Source : exercice `prPhon`, mini-leçon `prPhon`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre='Le son AN et le son IN',
        chapeau="Deux sons qui passent par le nez, et qui servent tous les "
                "deux à dire quand : une absence, un rendez-vous, demain "
                "matin, le trente.",
        duree='60 minutes')

    d.titre(notes="Séance de graphie-phonie. Prévoir l'audio du module : les huit cartes "
                  "de l'exercice 2 s'écoutent une par une, et la répétition en groupe "
                  "vaut mieux que l'explication.")

    d.objectifs([
        "distinguer à l'oreille le son an et le son in ;",
        "reconnaître leurs écritures : an, en, am, em · in, ain, ein ;",
        "prononcer les mots du module qui les contiennent ;",
        "dire une date sans se faire redemander.",
    ])

    d.regle("Deux voyelles qui sortent par le nez",
            "absence  ·  matin",
            precision="Pour ces sons, une partie de l'air passe par le nez. "
                      "Beaucoup de langues n'en ont aucune : si l'oreille les "
                      "mélange, ce n'est pas un défaut, c'est un son qu'on n'a "
                      "jamais eu à distinguer.",
            notes="Diapo à photographier. Faire l'essai des deux doigts sur le nez : "
                  "dire « a », puis « an ». Le son change quand on bouche — c'est la "
                  "preuve que l'air y passait.")

    d.tableau('Analyse', "Le son AN, la bouche ouverte",
              ["On écrit", "Exemples du module"],
              [["an", "avant · enfant · quarante"],
               ["en", "absence · prévenir · septembre"],
               ["am, em", "chambre · ensemble"],
               ["Le piège", "« en » se dit « an » dans absence"]],
              cle=1,
              note="La bouche est ouverte comme pour « a », et les lèvres ne sont "
                   "pas rondes.",
              notes="Diapo à photographier. Faire lire la colonne de droite à voix "
                    "haute, deux fois, en exagérant l'ouverture de la bouche.")

    d.tableau('Analyse', "Le son IN, la bouche étirée",
              ["On écrit", "Exemples du module"],
              [["in", "matin · clinique · vingt"],
               ["ain", "demain · prochain"],
               ["ein, en après i", "plein · bien · combien"],
               ["Le piège", "après un i, « en » se dit « in » : bien"]],
              cle=1,
              note="Les lèvres s'étirent sur les côtés, presque comme pour sourire.",
              notes="Faire remarquer que « bien » rime avec « matin » et non avec "
                    "« avant ». C'est l'erreur la plus fréquente du niveau.")

    d.pratique('Écoute', "AN comme ABSENCE, ou IN comme MATIN ?",
               "Écoutez, puis classez.", [
        ("une absence", "AN"),
        ("le matin", "IN"),
        ("un enfant", "AN"),
        ("demain", "IN"),
        ("trente", "AN"),
        ("vingt", "IN"),
    ], corrige=True,
       notes="Les huit cartes sont dans l'exercice 2 du module interactif. Faire d'abord "
             "à l'oreille, sans le mot écrit, puis montrer l'orthographe.")

    d.piege("Prononcer la lettre n",
            "ab-sen-ne-ce",
            "ab-sence",
            "Dans « absence », le n ne se prononce pas tout seul : il rend la voyelle "
            "nasale, puis il disparaît. La langue ne touche pas le palais et la bouche "
            "ne se ferme pas à la fin du mot.",
            notes="Erreur très répandue chez les élèves dont la langue prononce toutes "
                  "les consonnes écrites. Faire tenir le son deux secondes, bouche "
                  "ouverte, sans jamais fermer.")

    d.cartes("Trois mots qui contiennent les deux sons", "À dire tous les jours", [
        ("« Mon enfant a un rendez-vous demain matin. »",
         "La phrase du comptoir, et celle qui contient les deux sons trois fois. À "
         "apprendre telle quelle."),
        ("« Je vais être absente lundi matin. »",
         "An dans absente, in dans matin et lundi. C'est la phrase du défi 1."),
        ("« Le trente, à vingt heures. »",
         "Deux nombres, deux sons. Une date mal comprise, c'est une journée manquée "
         "pour rien."),
    ], cols=3,
       notes="Faire répéter les trois phrases en chœur, puis un élève à la fois. Cinq "
             "minutes, et le reste de la séance devient facile.")

    d.pratique('Prononciation', "Lisez à voix haute",
               "Une phrase par élève, à tour de rôle.", [
        ("Je vais être absente demain matin.", "an puis in"),
        ("Mon enfant a un rendez-vous à la clinique.", "an trois fois"),
        ("Le trente septembre, à vingt heures.", "les deux sons"),
        ("Avant le cours, je passe au comptoir.", "an deux fois"),
        ("Lundi matin, ça va bien.", "in trois fois"),
    ], corrige=False,
       notes="Ne corriger qu'un son à la fois. Un élève qui entend « c'est presque ça » "
             "recommence ; un élève qui entend trois corrections abandonne.")

    d.billet(
        "Écrivez trois mots avec le son an et trois mots avec le son in.",
        exemples=[
            "Prenez-les dans le vocabulaire du module.",
            "Soulignez la ou les lettres qui font le son.",
        ],
        notes="Devoir court. Il prépare A3 : les mots trouvés servent d'entrée au banc "
              "de vocabulaire.")

    return d.save(dossier)
