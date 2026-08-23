# -*- coding: utf-8 -*-
"""D2 · Rapporter ce que chacun a dit
Bloc D « Défi 3 » · couleur ambre · grammaire · 75 min.
Source : exercices `t3rapp`, `t3emph` et `t3cr` ; mini-leçons du même nom.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="Rapporter ce que chacun a dit",
        chapeau="Un compte rendu est fait, du début à la fin, de phrases "
                "rapportées. Le verbe qui introduit est au passé, donc tout "
                "ce qui suit recule d'un cran. Ce n'est pas un choix : c'est "
                "un mécanisme.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire la plus rentable du module : sans la "
                  "concordance, le compte rendu devient une transcription de trois "
                  "pages que personne ne lit.")

    d.objectifs([
        "reculer d'un cran le temps du verbe rapporté ;",
        "changer les personnes, les possessifs et les repères de temps ;",
        "rapporter une question sans inversion ni point d'interrogation ;",
        "mettre en relief ce qui compte avec c'est… qui et ce que…, c'est.",
    ], notes="Les trois premiers objectifs sont la concordance ; le quatrième est un "
             "outil d'écriture qui sert au compte rendu comme à l'exposé.")

    d.declencheur(
        'Observation', "Ce qu'il a dit, et ce que vous écrivez",
        pistes=[
            "Il a dit : « Je propose qu'on compte les arbres. »",
            "Vous écrivez : « Youssouf a proposé qu'on compte les arbres. »",
            "Qu'est-ce qui a changé, à part les guillemets ?",
            "Et si vous écriviez plutôt : « Il a dit qu'il propose » ?",
        ],
        notes="La quatrième piste est la faute la plus courante, et elle sonne mal à "
              "l'oreille avant d'être expliquée. Faire dire les deux versions.")

    d.tableau('Analyse', "Les quatre reculs",
              ['Au style direct', 'Rapporté au passé'],
              [["présent : je pars", "imparfait : qu'il partait"],
               ["passé composé : je suis parti", "plus-que-parfait : qu'il était parti"],
               ["futur : je partirai", "conditionnel : qu'il partirait"],
               ["va partir", "allait partir"]],
              cle=0,
              note="Ne bougent pas : imparfait, conditionnel, subjonctif. Ils sont déjà en arrière.",
              notes="Diapositive à photographier. Le troisième recul explique le "
                    "retour du conditionnel vu en B3 : ici, il n'exprime aucun doute, "
                    "il exprime l'avenir.")

    d.pratique('Grammaire', "Mettez au discours indirect passé",
               "Le verbe qui introduit est déjà au passé.", [
        ("« Je propose qu'on compte. » devient : Il a dit qu'il ___", "proposait"),
        ("« Ça ne prouve rien. » devient : Il a répondu que ça ne ___ rien", "prouvait"),
        ("« J'ai pris la mesure en juillet. » devient : Elle a précisé qu'elle ___", "avait pris"),
        ("« Je vérifierai mes notes. » devient : Il a promis qu'il ___", "vérifierait"),
        ("« Je vais envoyer le compte rendu. » devient : Elle a annoncé qu'elle ___", "allait envoyer"),
        ("« Ce résumé est trop proche. » devient : Elle a expliqué qu'il ___", "était trop proche"),
    ], corrige=True,
       notes="Faire lire la phrase entière après correction. Les élèves entendent la "
             "concordance bien avant de la produire.")

    d.tableau('Analyse', "Ce qui change aussi",
              ['Ce qui bouge', 'Exemple'],
              [["Les personnes", "je devient il ou elle"],
               ["Les possessifs", "mon devient son, notre devient leur"],
               ["Aujourd'hui", "devient ce jour-là"],
               ["Demain", "devient le lendemain"],
               ["Hier", "devient la veille"]],
              cle=0,
              note="Un compte rendu se relit des semaines plus tard : « demain » n'y veut plus rien dire.",
              notes="Diapositive à photographier. C'est l'oubli le plus fréquent, et "
                    "le plus coûteux : une date qui ne veut plus rien dire.")

    d.piege('Grammaire',
            "« Elle a demandé quand partait-il ? »",
            "« Elle a demandé quand il partait. »",
            "Une question rapportée n'a ni inversion, ni point "
            "d'interrogation, ni « est-ce que ». Trois formes seulement : "
            "s'il venait, ce qu'il comptait, quand il partait.",
            notes="Piège de la séance. Le « ce que » qui remplace « quoi » et "
                  "« qu'est-ce que » est la transformation la plus ratée : la faire "
                  "répéter trois fois.")

    d.tableau('Analyse', "Mettre en relief, à l'écrit",
              ['La construction', 'Un exemple'],
              [["c'est… qui", "C'est Miguel qui a proposé de noter l'ombre."],
               ["c'est… que", "C'est samedi qu'on y va, et non vendredi."],
               ["ce que…, c'est", "Ce qu'on cherche, c'est une différence."],
               ["ce qui…, c'est", "Ce qui manque, c'est l'ombre au sol."]],
              cle=0,
              note="En parlant, la voix appuie. À l'écrit, la construction fait ce travail.",
              notes="Diapositive à photographier. Attention à l'accord : c'est moi "
                    "qui anime, c'est nous qui avons décidé. Le verbe suit la "
                    "personne encadrée.")

    d.pratique('Production écrite', "Le compte rendu de votre dernière rencontre",
               "Une page, six sections, à écrire pendant la séance.", [
        ("Le cadre", "date, heures de début et de fin, présents, absents"),
        ("Les positions", "une phrase rapportée par personne, avec son nom"),
        ("Le désaccord", "sur quoi il portait, et comment il s'est réglé"),
        ("Les décisions", "numérotées, chacune avec sa raison"),
        ("À faire", "un nom, un verbe et une date par ligne"),
        ("À l'absent", "ce que vous attendez de lui, et avant quand"),
    ], corrige=False,
       notes="Le produit du Défi 3, et le brouillon de la lettre du bloc E. Ramasser "
             "et corriger deux choses seulement : la concordance, et la présence "
             "d'un nom sur chaque engagement.")

    d.billet(
        "Rapportez au passé une phrase que quelqu'un a dite en classe aujourd'hui.",
        exemples=[
            "Le nom, le verbe introducteur au passé, puis la phrase.",
            "Attention au temps du verbe rapporté.",
        ],
        notes="Billet de sortie du Défi 3. Les lire à voix haute : entendre ses "
                  "propres mots rapportés par quelqu'un d'autre est la meilleure "
                  "démonstration de ce que le compte rendu fait.")

    return d.save(dossier)
