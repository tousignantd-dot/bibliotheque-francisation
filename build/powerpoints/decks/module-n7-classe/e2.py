# -*- coding: utf-8 -*-
"""E2 · La lettre au camarade absent, et le bilan
Bloc E « Je me lance » · couleur framboise · production écrite · 75 min.
Source : section `appli` (production écrite) et « Je retiens des mots ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="La lettre au camarade absent, et le bilan",
        chapeau="Ce n'est pas une lettre officielle : vous écrivez à "
                "quelqu'un de votre classe, que vous tutoyez. Mais il doit "
                "pouvoir travailler dès demain sans appeler personne.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du module. Redistribuer le compte rendu écrit en "
                  "D2 : la lettre s'écrit avec lui sous les yeux, et elle en est la "
                  "version adressée à quelqu'un.")

    d.objectifs([
        "écrire une lettre personnelle à un camarade de classe ;",
        "rapporter au passé ce que chacun a proposé ;",
        "nommer le désaccord et dire comment il s'est réglé ;",
        "faire le bilan de ce qu'on sait maintenant conduire.",
    ], notes="Le premier objectif est une intention du programme, mot pour mot : "
             "rédiger une lettre personnelle destinée à un camarade de classe.")

    d.declencheur(
        'Préparation', "Il n'était pas là. De quoi a-t-il besoin ?",
        pistes=[
            "De savoir ce qui a été décidé sans lui, et pourquoi.",
            "De savoir ce qu'on attend de lui, et pour quand.",
            "A-t-il besoin de savoir qui a dit quoi ?",
            "Que se passe-t-il s'il apprend la décision trois jours plus tard ?",
        ],
        notes="La troisième piste mérite d'être discutée : oui, il en a besoin, "
              "parce que c'est à cette personne-là qu'il parlera s'il n'est pas "
              "d'accord. Sans les noms, il ne peut rien faire.")

    d.tableau('Analyse', "Six sections, une page",
              ['La section', 'Ce qu\'elle contient'],
              [["Le cadre", "le jour, les heures, qui était là"],
               ["Les positions", "une phrase rapportée par personne, avec son nom"],
               ["Le désaccord", "sur quoi il portait, et comment il s'est réglé"],
               ["Les décisions", "numérotées, chacune avec sa raison"],
               ["À faire", "un nom, un verbe et une date par ligne"],
               ["À l'absent", "ce qu'on attend de lui, et avant quand"]],
              cle=0,
              notes="Diapositive à photographier. Une page, jamais deux : un compte "
                    "rendu de trois pages n'est pas lu, donc il ne sert à rien.")

    d.cartes('Analyse', "Huit exigences, tirées du module", [
        ("Le cadre", "mardi, de 19 h 05 à 19 h 35, trois présents"),
        ("Deux positions", "avec le nom de qui les a portées"),
        ("Quatre verbes rapportés", "a dit que, a proposé que, a répondu que"),
        ("Un repère de temps", "le lendemain, et non demain"),
        ("Le désaccord", "nommé, et réglé"),
        ("Une concession", "bien que… soit… ou même si… est…"),
        ("Une mise en relief", "ce qu'on a décidé, c'est…"),
        ("Deux engagements", "un nom et une date pour chacun"),
    ], cols=1,
       notes="Les huit exigences sont la grille de correction. Les faire cocher une "
             "à une avant l'envoi, comme on coche une liste d'épicerie.")

    d.piege('Écrit',
            "« On a décidé qu'on irait samedi, faut que tu viennes. »",
            "« Nous avons décidé d'y aller samedi à 10 h. Dis-moi avant vendredi si tu peux venir. »",
            "La première phrase donne un ordre sans donner l'heure, et elle "
            "mélange deux variétés de langue. La seconde donne un fait, une "
            "heure, une demande et une date. Écrire à un camarade n'oblige "
            "pas à écrire vite.",
            notes="Point de la séance, et il ramène le savoir de A4 : familier avec "
                  "un camarade, oui ; mais organisé, parce que c'est un document de "
                  "travail.")

    d.pratique('Production écrite', "Votre lettre",
               "De dix à quatorze phrases, adressées à un camarade absent.", [
        ("Le début", "le cadre, en deux ou trois phrases"),
        ("Le milieu", "les positions rapportées, puis le désaccord et sa solution"),
        ("Les décisions", "numérotées, chacune avec sa raison"),
        ("La fin", "les engagements, puis ce que vous attendez de lui"),
        ("Avant d'envoyer", "cochez les huit exigences, une par une"),
    ], corrige=False,
       notes="Le module corrige la lettre par l'assistant et permet de la déposer. En "
             "classe, faire relire par un pair avec la grille des huit exigences "
             "avant la correction automatique.")

    d.tableau('Bilan', "Ce que vous savez maintenant conduire",
              ['Le geste', 'La phrase qui le fait'],
              [["Ouvrir une rencontre", "je rappelle où on en est"],
               ["Faire préciser", "combien, exactement ?"],
               ["Reformuler", "je reformule, dis-moi si je me trompe"],
               ["Accorder sans céder", "bien que ce soit vrai, je pense que…"],
               ["Fermer", "je résume les décisions"],
               ["Rendre compte", "il a proposé que…, elle a répondu que…"]],
              cle=0,
              notes="Diapositive à photographier, et dernière du module. C'est la "
                    "grille que l'élève emporte : six lignes, et elles servent dans "
                    "n'importe quel emploi.")

    d.billet(
        "Quel geste allez-vous essayer la prochaine fois qu'on vous fera travailler en équipe ?",
        exemples=[
            "Un seul geste, en une phrase.",
            "Écrivez la phrase que vous direz.",
        ],
        notes="Billet de sortie du module. Les lire à voix haute à la fin : elles "
              "disent ce que seize séances ont réellement déposé, et c'est presque "
              "toujours « faire préciser » ou « reformuler ».")

    return d.save(dossier)
