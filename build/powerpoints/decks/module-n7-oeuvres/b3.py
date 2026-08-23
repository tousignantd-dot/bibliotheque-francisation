# -*- coding: utf-8 -*-
"""B3 · Qui parle ? L'incise et les guillemets
Bloc B « Défi 1 » · couleur teal · écoute et réponds · 75 min.
Source : exercices `t1inc` et `t1guil`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='teal',
        titre="Qui parle ? L'incise et les guillemets",
        chapeau="Un sketch est fait de paroles rapportées. Sans les incises, "
                "on ne sait plus qui parle, et tout le comique vient justement "
                "du passage d'une voix à l'autre.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire appliquée à l'écoute. Prévoir beaucoup d'oral : "
                  "les incises se sentent à la voix avant de s'écrire.")

    d.objectifs([
        "reconnaître le sujet quand il suit le verbe dans une incise ;",
        "écrire une incise avec le trait d'union et le t de liaison ;",
        "distinguer une parole citée d'une parole racontée ;",
        "ponctuer un discours direct : deux-points, guillemets, majuscule.",
    ], notes="Le premier objectif est de compréhension, les trois autres de "
             "production. C'est l'ordre du programme : on reconnaît avant d'employer.")

    d.declencheur(
        'Préparation', "Comment sait-on qui parle, dans une histoire racontée ?",
        pistes=[
            "À la voix de celui qui raconte ?",
            "Aux mots « il dit », « elle répond » ?",
            "Comment fait-on à l'écrit, où il n'y a pas de voix ?",
            "Dans votre langue première, comment marque-t-on cela ?",
        ],
        notes="La quatrième piste vaut le détour : plusieurs langues n'inversent "
              "jamais le sujet, d'autres n'emploient pas de guillemets. Nommer "
              "l'écart aide plus que le corriger.")

    d.tableau('Analyse', "L'incise, en trois cas",
              ['Le cas', 'Ce qu\'on écrit'],
              [["Avec un pronom", "dit-elle, répond-il, demandai-je"],
               ["Voyelle plus il, elle, on", "ajoute-t-elle, demanda-t-il, pensa-t-on"],
               ["Avec un nom", "reprend le gérant, murmure Marilou"]],
              cle=0,
              note="Le verbe passe toujours devant. Le trait d'union, seulement avec un pronom.",
              notes="Diapositive à photographier. Trois lignes, et la leçon entière y "
                    "est. Le t de liaison est le seul point qui demande de la "
                    "pratique.")

    d.regle("Le t de liaison ne veut rien dire",
            "Il sépare deux voyelles, et c'est tout ce qu'il fait.",
            precision="« Ajoute-elle » est impossible à dire : la bouche bute. Le "
                      "français glisse donc un t entre deux traits d'union, "
                      "uniquement devant il, elle ou on, et uniquement quand le "
                      "verbe finit par une voyelle.",
            notes="Diapositive à photographier. Rassurer : ce t n'a aucun sens à "
                  "apprendre, il est là pour l'oreille. On l'appelle euphonique.")

    d.tableau('Analyse', "Citer, ou raconter",
              ['La forme', 'Ce qu\'elle promet'],
              [["Il dit : « C'est dans le système. »",
                "les mots exacts, et le lecteur a le droit d'y croire"],
               ["Il dit que c'est dans le système.",
                "le contenu seulement, à votre façon"],
               ["Elle demande s'il en reste.",
                "une question rapportée passe par « si », jamais par « que »"]],
              cle=0,
              note="Les guillemets sont une promesse. Ne les mettez pas sur une phrase reconstruite.",
              notes="Diapositive à photographier. Le troisième cas est celui qu'on "
                    "manque le plus souvent à l'écrit.")

    d.cartes('Analyse', "Trois choses bougent en passant au rapporté", [
        ("Le pronom", "« je reviens » devient qu'elle revenait"),
        ("Le temps", "le présent devient l'imparfait"),
        ("Le mot du temps", "demain devient le lendemain, hier devient la veille"),
        ("Ce qui ne bouge pas", "le sens, et lui seul"),
    ], cols=1,
       notes="Le triple déplacement est ce qui rend le discours rapporté difficile. "
             "C'est aussi pourquoi la citation exacte est plus sûre quand la "
             "formulation compte.")

    d.piege('Écrit',
            "« Ça fait quarante minutes », elle dit.",
            "« Ça fait quarante minutes », dit-elle.",
            "L'ordre normal du français ne survit pas dans l'incise : le verbe "
            "passe devant, toujours, et le pronom s'y accroche par un trait "
            "d'union. C'est la seule inversion obligatoire du français "
            "ordinaire, avec la question.",
            notes="Erreur systématique chez les élèves dont la langue première "
                  "n'inverse jamais. Faire écrire dix incises d'affilée : "
                  "l'automatisme vient vite.")

    d.pratique('Grammaire', "Transformez en incise",
               "Placez l'incise après les paroles.", [
        ("Elle dit : « Ça fait quarante minutes. »", "« Ça fait quarante minutes », dit-elle."),
        ("Il ajoute : « C'est dans le système. »", "« C'est dans le système », ajoute-t-il."),
        ("Elle demande : « Est-ce qu'il en reste ? »", "« Est-ce qu'il en reste ? » demande-t-elle."),
        ("Le gérant reprend : « Je vérifie. »", "« Je vérifie », reprend le gérant."),
        ("On pense : « Ça ne se peut pas. »", "« Ça ne se peut pas », pense-t-on."),
        ("Marilou murmure : « Écoute la fin. »", "« Écoute la fin », murmure Marilou."),
    ], corrige=True,
       notes="Exercice `t1inc` du module. Faire lire chaque réponse à voix haute : le "
             "t de liaison s'entend, et c'est le meilleur contrôle.")

    d.pratique('Écoute', "Mot pour mot, ou raconté ?",
               "Écoutez et dites si l'on cite ou si l'on rapporte.", [
        ("Elle me dit : « Monsieur, ça fait quarante minutes. »", "mot pour mot"),
        ("Elle m'a dit que ça faisait quarante minutes.", "raconté"),
        ("Je lui réponds : « Madame, moi ça fait trente ans. »", "mot pour mot"),
        ("Ghyslaine m'a demandé si j'avais vu les trois œuvres.", "raconté"),
    ], corrige=True,
       notes="Exercice `t1guil` du module, qui en compte huit. Faire l'exercice à "
             "l'oreille d'abord : les guillemets ne s'entendent pas, mais le « que » "
             "et le changement de temps, oui.")

    d.billet(
        "Rapportez une phrase entendue cette semaine, des deux façons.",
        exemples=[
            "D'abord entre guillemets, avec une incise.",
            "Puis avec « que », en déplaçant le pronom et le temps.",
        ],
        notes="Devoir court et très révélateur : la version rapportée garde presque "
              "toujours le « je » de départ au premier essai.")

    return d.save(dossier)
