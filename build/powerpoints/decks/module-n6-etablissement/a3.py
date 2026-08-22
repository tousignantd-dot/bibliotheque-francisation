# -*- coding: utf-8 -*-
"""A3 · Sept papiers, sept choses différentes
Bloc A « Je découvre » · couleur ambre · 75 min.
Source : exercice `prPapiers`, son bandeau de savoir et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='ambre',
        titre="Sept papiers, sept choses différentes",
        chapeau="Dans un établissement, tout finit en papier. Mais chaque "
                "papier ne dit qu'une chose, et cinq endroits d'une page "
                "suffisent à savoir laquelle.",
        duree='75 minutes')

    d.titre(notes="Séance de lecture, pas d'écriture. Demander aux élèves d'apporter "
                  "un papier reçu du centre : la moitié en aura un dans son sac, et "
                  "un document réel vaut mieux qu'un exemple.")

    d.objectifs([
        "nommer sept papiers d'un établissement et dire ce que chacun contient ;",
        "distinguer ce qui prouve, ce qui décide et ce qu'on écrit soi-même ;",
        "regarder cinq endroits d'un document avant d'en lire la première phrase ;",
        "repérer les deux dates d'un document officiel et savoir laquelle oblige.",
    ], notes="Le quatrième objectif est celui qui sauve une année : la date de "
             "l'envoi n'est jamais celle qui compte.")

    d.declencheur(
        'Observation', "Quel papier as-tu reçu de ton centre cette année ?",
        pistes=[
            "L'as-tu gardé ? Sais-tu où il est ?",
            "L'as-tu lu en entier, ou seulement le début ?",
            "Est-ce qu'il y avait une date à respecter ?",
        ],
        notes="Question qui met mal à l'aise et qu'il faut poser sans reproche : "
              "presque personne ne lit un document officiel en entier, et c'est "
              "normal. La séance existe pour donner une méthode, pas une leçon.")

    d.tableau('Analyse', "Trois familles de papiers",
              ['La famille', 'Ce qu\'elle fait'],
              [["Ceux qui prouvent", "relevé de notes, attestation, évaluation comparative : ils disent ce qui a eu lieu"],
               ["Ceux qui décident", "avis officiel, plan de formation, convocation : ils portent une décision et une date"],
               ["Ceux que tu écris", "demande de rencontre, courriel, compte rendu : les seuls sur lesquels tu as la main"]],
              cle=0,
              note="Les deux premières familles se demandent ; la troisième s'écrit. C'est la seule où votre précision change quelque chose.",
              notes="Diapositive à photographier. Faire classer à voix haute les "
                    "papiers que les élèves ont apportés.")

    d.cartes('Analyse', "Sept papiers, et ce que chacun dit", [
        ("Un relevé de notes", "Les cours que tu as réussis et le résultat obtenu à chacun."),
        ("Un avis officiel", "Une décision de l'établissement, avec sa date et parfois sa condition."),
        ("Un plan de formation", "L'ordre des cours à suivre et le temps prévu pour chacun."),
        ("Une évaluation comparative", "À quel niveau d'ici se comparent des études faites ailleurs."),
        ("Une demande de rencontre", "Ce que tu cherches, en deux lignes, avant un rendez-vous."),
        ("Un compte rendu", "Ce qui a été dit et décidé pendant une rencontre."),
    ], cols=2,
       notes="Ne pas tout lire à voix haute : faire lire une carte par élève. "
             "S'arrêter sur « une évaluation comparative », qui reviendra en B4 et "
             "qui est le document le plus mal compris de tout le module.")

    d.tableau('Analyse', "Cinq endroits, avant de lire une seule phrase",
              ['Où regarder', 'Ce que ça vous apprend'],
              [["En haut à gauche", "quel établissement parle, et il ne parle jamais pour un autre"],
               ["La ligne en gras", "le genre du document, donc ce que le reste va contenir"],
               ["Votre nom", "une lettre adressée à quelqu'un d'autre n'engage personne"],
               ["Les deux dates", "celle de l'envoi, et celle avant laquelle vous devez agir"],
               ["Les petits chiffres", "le numéro de dossier, sans lequel un appel ne mène nulle part"]],
              cle=0,
              note="Un lecteur pressé qui sait regarder comprend plus vite qu'un lecteur appliqué qui lit tout dans l'ordre.",
              notes="Diapositive à photographier. Faire appliquer les cinq points, "
                    "dans l'ordre, sur un document apporté par un élève volontaire.")

    d.regle("Il y a toujours deux dates",
            "Celle du haut est passée le jour où vous lisez ; celle du milieu est celle à écrire dans votre calendrier.",
            precision="La date de l'envoi ne vous demande rien. La date limite, elle, "
                      "décide de tout, et elle est presque toujours plus bas dans la "
                      "page, souvent dans un encadré. Soulignez-la au crayon dès la "
                      "première lecture.",
            notes="Diapositive à photographier. Distribuer un surligneur si possible : "
                  "le geste s'installe mieux que la consigne.")

    d.piege('Lecture',
            "se fier à ce qu'on vous a dit",
            "demander où c'est écrit",
            "« On m'avait dit que ça comptait » ne sauve personne, parce que la "
            "personne qui l'a dit n'a rien noté. La question à poser est simple "
            "et parfaitement polie : « Est-ce que je peux avoir ça par écrit ? »",
            notes="Faire répéter la question par tout le groupe, à voix haute, deux "
                  "fois. Beaucoup d'élèves croient qu'elle est agressive. Elle ne "
                  "l'est pas, et ils l'entendront eux-mêmes en la disant.")

    d.pratique('Pratique', "Quel papier vous faut-il ?",
               "Lisez la situation, puis nommez le papier à demander.", [
        ("Un employeur veut la preuve des cours que vous avez réussis.", "un relevé de notes"),
        ("Vous voulez savoir l'ordre des cours et le temps prévu pour chacun.", "un plan de formation"),
        ("Vous voulez garder la trace de ce qui s'est décidé en réunion.", "un compte rendu"),
        ("Vous voulez rencontrer le conseiller d'orientation.", "une demande de rencontre"),
        ("Le centre vous annonce sa décision par la poste.", "un avis officiel"),
        ("Vous voulez situer vos études de votre pays par rapport à celles d'ici.", "une évaluation comparative"),
    ], corrige=True,
       notes="Faire répondre le groupe avant d'afficher la correction. Le dernier "
             "item est le plus difficile : bien redire que ce document situe, mais "
             "ne remplace rien.")

    d.billet(
        "Quel papier vas-tu demander cette semaine, et à qui ?",
        exemples=[
            "Une phrase, avec le nom du papier et l'endroit où tu iras.",
            "Écris aussi la question exacte que tu diras.",
        ],
        notes="Trois minutes. Reprendre deux ou trois formulations à voix haute et "
              "les corriger ensemble : c'est la première production orale du module.")

    return d.save(dossier)
