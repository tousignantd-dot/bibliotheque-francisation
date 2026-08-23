# -*- coding: utf-8 -*-
"""B3 · Concéder avant de demander
Bloc B « Défi 1 · Frapper à la porte d'en haut » · couleur ambre · grammaire ·
75 min.
Source : exercice `t1conc` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Concéder avant de demander",
        chapeau="Votre voisin a un argument, et il l'attend. Si vous le dites "
                "avant lui, il ne lui reste rien à opposer — et il est obligé "
                "d'écouter la suite.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire au service d'une stratégie. Ce n'est pas de la "
                  "gentillesse : concéder retire à l'autre son meilleur argument.")

    d.objectifs([
        "employer « même si » avec l'indicatif ;",
        "employer « bien que » avec le subjonctif ;",
        "employer « malgré » devant un nom ;",
        "placer la concession avant la demande, jamais après.",
    ], notes="Le quatrième objectif n'est pas une règle de grammaire mais une règle "
             "d'effet : la phrase se termine sur ce qu'on veut qu'on retienne.")

    d.declencheur(
        'Observation', "Quel argument ton voisin te sortira-t-il en premier ?",
        pistes=[
            "Il travaille tôt ? Il a des enfants ? Il est chez lui ?",
            "Est-ce que cet argument est vrai ?",
            "Que se passe-t-il si tu le dis avant lui ?",
            "Et si tu attends qu'il le dise ?",
        ],
        notes="Faire nommer trois arguments plausibles au tableau. Ils serviront de "
              "matière aux phrases de concession de la pratique.")

    d.regle("Même si, bien que, malgré",
            "Trois marqueurs, trois constructions différentes.",
            precision="« Même si » + indicatif : même si votre horaire est difficile. "
                      "« Bien que » + subjonctif : bien que je comprenne votre horaire. "
                      "« Malgré » + un nom, jamais un verbe : malgré le caoutchouc. "
                      "Le premier se dit, le deuxième s'écrit, le troisième fait les "
                      "deux.",
            notes="Diapositive à photographier. Faire produire les trois formes sur la "
                  "même idée, oralement, avant de passer au tableau.")

    d.tableau('Analyse', "La même idée, à l'oral et à l'écrit",
              ['Version orale', 'Version écrite'],
              [["Même si votre horaire est difficile", "Bien que votre horaire soit difficile"],
               ["Même si je comprends votre situation", "Bien que je comprenne votre situation"],
               ["Même s'il fait des efforts", "Bien qu'il fasse des efforts"],
               ["Même si le bruit a diminué", "Bien que le bruit ait diminué"],
               ["Même si je suis la seule à me plaindre", "Bien que je sois la seule à me plaindre"]],
              notes="Diapositive à photographier. Le passage de gauche à droite est "
                    "exactement le travail du bloc D : on transpose sa conversation en "
                    "lettre.")

    d.cartes('Analyse', "Les subjonctifs qui reviennent", [
        ("être", "que je sois, que vous soyez"),
        ("avoir", "que j'aie, que vous ayez"),
        ("faire", "que je fasse, qu'il fasse"),
        ("pouvoir", "que je puisse, qu'il puisse"),
        ("comprendre", "que je comprenne, qu'il comprenne"),
        ("savoir", "que je sache, qu'il sache"),
    ], cols=3,
       notes="Six verbes, et ils suffisent à toutes les concessions du module. Les "
             "faire écrire dans le cahier avant la pratique.")

    d.piege('Grammaire',
            "Bien que je comprends votre horaire",
            "Bien que je comprenne votre horaire",
            "« Bien que » entraîne le subjonctif sans exception. Si le subjonctif ne "
            "vient pas, il y a une sortie honorable : écrire « même si », qui prend "
            "l'indicatif et que personne ne vous reprochera. Ce qui ne passe pas, "
            "c'est l'indicatif après « bien que ».",
            notes="Le test le plus rapide : remplacer par le verbe être. « Bien que je "
                  "suis » sonne faux à tout le monde ; « bien que je comprends » aussi, "
                  "mais on l'entend moins.")

    d.pratique('Pratique', "Complétez avec même si, bien que ou malgré",
               "Attention au mode du verbe qui suit.", [
        ("___ votre horaire est difficile, le mien l'est aussi.", "Même si"),
        ("___ je comprenne les contraintes de votre horaire, je ne peux plus dormir.", "Bien que"),
        ("___ le tapis de caoutchouc, je suis réveillée neuf matins sur quatorze.", "Malgré"),
        ("___ il fasse des efforts, l'appareil est toujours au-dessus de ma chambre.", "Bien qu'"),
        ("___ que vous ayez le droit de vous entraîner chez vous, l'heure pose problème.", "Bien"),
        ("___ nos deux conversations, la situation est la même qu'en février.", "Malgré"),
        ("___ je sois la seule à me plaindre, cela ne rend pas le bruit normal.", "Bien que"),
    ], corrige=True,
       notes="Faire relire chaque phrase complète après la correction : ce sont les "
             "phrases mêmes de la lettre du bloc D.")

    d.billet(
        "Écris une concession suivie de ta demande, dans cet ordre.",
        exemples=[
            "Commence par « Même si » ou par « Bien que ».",
            "La demande vient après la virgule, jamais avant.",
        ],
        notes="Deux minutes. Ceux qui inversent l'ordre écrivent un reproche déguisé : "
              "leur relire leur propre phrase à l'envers pour qu'ils l'entendent.")

    return d.save(dossier)
