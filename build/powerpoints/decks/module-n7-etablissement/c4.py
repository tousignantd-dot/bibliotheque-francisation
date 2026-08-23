# -*- coding: utf-8 -*-
"""C4 · Concéder sans s'effacer
Bloc C « Défi 2 · L'entrevue de sélection » · couleur teal · 90 min.
Source : exercices `t2conc` et `t2img`, et la mini-leçon de la concession.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='teal',
        titre="Concéder sans s'effacer",
        chapeau="Un comité connaît vos points faibles avant de vous "
                "rencontrer : ils sont au dossier. Les nommer d'abord, puis "
                "dire comment on les organise, est ce qui change tout.",
        duree='90 minutes')

    d.titre(notes="Séance de synthèse du bloc C : la concession, puis une simulation "
                  "d'entrevue en équipes de trois. Prévoir quarante minutes pour la "
                  "simulation, elle est le vrai contenu de la séance.")

    d.objectifs([
        "employer « bien que » avec le subjonctif ;",
        "employer « même si » avec l'indicatif ;",
        "employer « malgré » devant un nom ;",
        "placer l'obstacle avant la réponse, jamais après.",
    ], notes="Le quatrième objectif est une règle de rhétorique, pas de grammaire, et "
             "c'est celle qui décide de l'effet produit.")

    d.declencheur(
        'Observation', "Que répondre à une question qui touche un point faible ?",
        pistes=[
            "« Vous n'avez pas votre préalable de mathématiques. »",
            "Faire semblant que ce n'est rien ?",
            "S'excuser pendant deux minutes ?",
            "Ou dire quelque chose entre les deux ?",
        ],
        notes="Faire répondre trois élèves avant de donner la règle. Les deux extrêmes "
              "sortiront tout seuls, et la voie du milieu se laisse alors nommer.")

    d.tableau('Analyse', "Trois marqueurs, trois constructions",
              ['Le marqueur', 'Ce qui suit'],
              [['bien que', "le subjonctif : bien que j'aie, bien que ce soit"],
               ['même si', "l'indicatif : même si l'horaire est serré"],
               ['malgré', "un nom : malgré la distance, malgré mon accent"]],
              cle=0,
              note="Les trois disent la même chose ; ce qui les sépare est le mode du "
                   "verbe qui suit.",
              notes="Diapositive à photographier. C'est une paire d'erreurs "
                    "symétriques : subjonctif après « même si », indicatif après "
                    "« bien que ». Les deux se corrigent d'un seul geste.")

    d.regle("L'obstacle d'abord, la réponse ensuite",
            "« Bien que je n'aie pas encore mon préalable, je suis inscrite à la mise "
            "à niveau de septembre. »",
            precision="Dans l'autre sens, le comité n'entend que l'obstacle : c'est le "
                      "dernier mot qui reste. La concession sert à montrer qu'on a vu "
                      "l'objection, pas à la souligner.",
            notes="Diapositive à photographier. Faire dire la phrase dans les deux "
                  "sens par le même élève : la différence d'effet est immédiate.")

    d.pratique('Grammaire', "Complétez la concession",
               "Le marqueur, ou le verbe au bon mode.", [
        ("___ j'aie déjà suivi ce cours en Syrie, je le referais sans discuter.", "Bien que"),
        ("Bien que je n'(avoir) ___ pas encore mon préalable, je suis inscrite.", "aie"),
        ("___ l'horaire est serré, il est prévu depuis le mois de février.", "Même si"),
        ("Même si ce (être) ___ ma deuxième demande, je ne recommence pas la même lettre.", "est"),
        ("___ la distance, je serai au centre à huit heures tous les matins.", "Malgré"),
        ("Bien que la formation (être) ___ à temps plein, j'ai gardé deux quarts.", "soit"),
    ], corrige=True,
       notes="Corriger d'abord le mode, ensuite la prononciation : « aie » et « soit » "
             "sont courts et se mangent facilement.")

    d.piege('Piège', "Je sais que je ne suis pas la meilleure candidate.",
            "Bien que mon dossier soit incomplet, j'ai déjà réglé mon horaire.",
            "La première n'est pas une concession : c'est un argument contre soi, "
            "offert gratuitement à un comité qui ne l'avait pas demandé.",
            notes="Insister : la modestie n'est pas une stratégie d'entrevue. Ce qui "
                  "impressionne, c'est de nommer un manque et de montrer qu'on le "
                  "règle déjà.")

    d.cartes('Simulation', "Entrevue en équipes de trois", [
        ("Qui joue quoi",
         "Une personne candidate, deux membres du comité. On tourne toutes les huit "
         "minutes."),
        ("Les six questions",
         "Pourquoi ce diplôme · votre parcours · l'horaire · le plus difficile · une "
         "difficulté du dossier · vos questions."),
        ("Ce qu'on écoute",
         "Un fait daté par réponse, un exemple au lieu d'un adjectif, une concession "
         "bien tournée."),
        ("Ce qu'on note",
         "Une chose réussie, une chose à reprendre. Rien d'autre, et on la dit à la "
         "personne."),
    ], notes="Quarante minutes. Passer dans les équipes sans interrompre : on note, on "
             "ne corrige pas pendant. Le retour se fait en grand groupe, cinq minutes "
             "avant la fin.")

    d.billet("Écris une concession sur ton propre dossier : l'obstacle, puis ce que "
             "tu fais déjà.",
             exemples=["Bien que je n'aie pas encore mon préalable, je suis inscrite à la mise à niveau.",
                       "Même si j'écris lentement, je ne remets jamais une note incomplète."],
             notes="Ramasser les billets : ce sont les phrases que les élèves diront "
                   "au jeu de rôle du bloc E, et elles gagnent à être déjà écrites.")

    return d.save(dossier)
