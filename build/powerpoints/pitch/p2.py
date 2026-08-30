# -*- coding: utf-8 -*-
"""P2 · Ce que la direction décide — les quatre interrupteurs et le mode séance.
Section acier · le quatrième quart d'heure d'une rencontre.
Source : la section « Le mode sans IA » du CLAUDE.md (le champ reste `ia` ;
c'est l'étiquette qui a changé) et le bac à sable.
"""
from theme import Deck
from chiffres import CH, n
from parcours import TEMPS


def build(dossier):
    d = Deck(
        code='P2', section='acier',
        titre="Ce que la direction décide",
        chapeau="Quatre réglages appartiennent au centre, et un seul geste les pose. "
                "Ils ne changent pas le cours : ils changent ce que le cours a le droit "
                "de faire.",
        duree='8 minutes')

    d.titre(surtitre="PRÉSENTATION  ·  2 SUR 3",
            notes="Dire d'entrée que rien ici n'est à négocier avec nous : ce sont des "
                  "champs, déjà construits, que la direction pose elle-même.")

    d.parcours(TEMPS, 1,
               notes="Rappeler où l'on en est : le matériel est vu, on parle "
                     "maintenant de ce que le centre décide.")

    d.chapitre("DEUXIÈME TEMPS", "Ce que la direction décide",
               "Quatre réglages, posés une fois, qui descendent sur tous les "
               "groupes du centre.",
               notes="Jalon. C'est le moment où la direction cesse d'être "
                     "spectatrice : les quatre décisions sont les siennes.")

    d.objectifs([
        "savoir quelles décisions appartiennent au centre, et lesquelles à l'enseignant ;",
        "voir ce que chaque réglage change, concrètement, chez l'élève ;",
        "comprendre comment un refus descend sur tous les groupes d'un coup ;",
        "repartir en sachant quoi trancher, et quand.",
    ])

    d.tableau('Les quatre interrupteurs', "Chacun se pose une fois, sur l'arbre",
              ['Le réglage', 'Qui le pose', 'Ce qu\'il ferme'],
              [["L'assistant", "la direction du centre ou du CSS",
                "dix routes, d'un coup"],
               ["Le micro", "la direction du centre",
                "la voix qui sort de l'appareil"],
               ["Le dépôt de la voix", "la direction du centre",
                "ce qu'on garde d'un enregistrement"],
               ["Les séances sans compte", "la direction autorise",
                "l'ouverture d'une classe anonyme"]],
              cle=0,
              note="Sans réglage, les quatre restent ouverts : une mise en service "
                   "n'éteint rien au passage.",
              notes="Si une seule diapositive doit être projetée devant un comité, "
                    "c'est celle-ci. Laisser le temps de la lire. Préciser que le "
                    "réglage vit sur l'organisation, jamais sur un groupe.")

    d.regle("L'héritage",
            "Le premier réglage explicite tranche, et il descend.",
            precision="« Interdit » posé sur un centre de services ferme ses douze "
                      "centres. Celui qui a négocié une exception la porte écrite sur "
                      "lui-même. Et un réglage absent ne ferme rien : une mise en "
                      "service n'éteint jamais rien au passage.",
            notes="Question qui vient toujours : « et si un centre veut l'inverse du "
                  "CSS ? ». Réponse : il le pose sur lui-même, et c'est lui qui gagne.")

    d.cartes('Sans assistant', "Ce qui tombe, et ce qui ne bouge pas",
             [("Ce qui tombe", "La barre d'outils de l'élève en entier — traduire, "
               "simplifier, demander. La correction avant l'envoi. « Pourquoi je me "
               "trompe ? »."),
              ("Ce qui reste", "Les dialogues enregistrés, les %s exercices corrigés sur "
               "l'appareil, les mini-leçons, le vocabulaire, la production orale et "
               "écrite." % "sept familles d'"),
              ("Pour l'élève", "La réponse attendue s'affiche après deux "
               "essais : il n'est jamais laissé devant un mur."),
              ("Pour l'enseignant", "Les textes arrivent non corrigés. "
               "C'est lui qui corrige — c'est le vrai coût du refus, et il se voit.")],
             notes="Ne pas vendre le mode sans assistance comme équivalent. Dire le coût : le "
                   "travail de correction revient à l'enseignant.")

    d.piege('Le malentendu le plus fréquent',
            "« Fermer l'assistant, c'est perdre le cours. »",
            "« Fermer l'assistant, c'est perdre l'aide immédiate, pas le cours. »",
            "Les %s pistes audio sont enregistrées d'avance et les exercices à réponse "
            "connue se corrigent sur l'appareil : un centre sans assistant garde le "
            "matériel entier et ne paie plus rien à l'usage."
            % n(CH['mp3']),
            notes="C'est ici qu'on ouvre le bac à sable si quelqu'un doute. Deux clics "
                  "suffisent à montrer la même page dans les deux états.")

    d.tableau('Le troisième mode', "Une classe sans compte d'élève",
              ['Ce que l\'élève donne', 'Ce que l\'enseignant voit', 'Ce qui est gardé'],
              [["Rien : un code à six caractères, scanné sur une feuille photocopiée",
                "Son tableau de classe, participant par participant, question par question",
                "Aucun nom, aucun pseudonyme, aucune voix ; une séance qui expire le soir"]],
              note="La direction autorise le mode ; l'enseignant décide de s'en servir "
                   "un mardi matin. Les deux gestes sont distincts.",
              notes="Utile pour les groupes qui changent chaque semaine et pour les "
                    "remplaçants : aucun compte à créer avant la première minute.")

    d.billet("La décision à prendre aujourd'hui n'est pas « oui ou non » : c'est "
             "« lesquels des quatre, et par qui ».",
             exemples=["Un centre peut ouvrir avec l'assistant fermé et le rouvrir plus tard.",
                       "Aucun réglage ne demande de développement : ce sont des champs."],
             notes="Terminer en proposant un groupe pilote avec le réglage le plus "
                   "prudent. C'est plus facile à accorder qu'un accord de principe.")

    return d.save(dossier)
