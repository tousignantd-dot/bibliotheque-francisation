# -*- coding: utf-8 -*-
"""C2 · Faire une évaluation sommaire
Bloc C « Défi 2 · Le poste 4 » · couleur teal · 75 min.
Source du module : exercices `t2eval` et `t2lex`, mini-leçon `t2eval`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='teal',
        titre="Faire une évaluation sommaire",
        chapeau="« Sommaire » ne veut pas dire « approximatif ». C'est un "
                "premier examen, pas un examen bâclé : il donne des ordres de "
                "grandeur, il dit d'où viennent ses chiffres, et il nomme ce "
                "qu'il ne sait pas.",
        duree='75 minutes')

    d.titre(notes="Séance d'assemblage. Chaque élève a maintenant quatre pièces de son "
                  "projet dans son cahier - constat, objectif, échéancier, conséquence. "
                  "Aujourd'hui, on les met en ordre et on ajoute ce qui manque.")

    d.objectifs([
        "nommer les sept éléments d'une évaluation sommaire ;",
        "dire d'où vient chaque chiffre qu'on avance ;",
        "proposer au moins deux options, dont une gratuite ;",
        "dire ce qu'on ne sait pas, et qui le sait.",
    ], notes="Le dernier objectif est celui qui distingue le module. Il ne s'évalue "
             "pas comme un point de langue : il s'évalue à la présence de la phrase.")

    d.declencheur(
        'Discussion', "Un chiffre que vous n'avez pas",
        pistes=[
            "On vous demande combien ça coûte, et vous ne le savez pas.",
            "Est-ce qu'il vaut mieux donner une estimation, ou dire qu'on ne sait pas ?",
            "Qu'est-ce qui arrive si votre estimation se révèle fausse ?",
            "Qu'est-ce qu'Aïcha a répondu à monsieur Cormier ?",
        ],
        notes="Laisser le débat s'installer trois ou quatre minutes. Plusieurs "
              "défendront l'estimation, et c'est une position raisonnable. Trancher "
              "avec la règle qui suit : un chiffre faux discrédite tous les vrais.")

    d.tableau('Analyse', "Ce que contient une évaluation sommaire",
              ['L\'élément', 'Ce qu\'il exige'],
              [["Le constat", "ce que vous avez observé, avec la période"],
               ["Les données", "d'où elles viennent : le registre, le relevé"],
               ["La cause probable", "dites « probable » si elle l'est"],
               ["Les conséquences", "en jours, en argent, en retards"],
               ["Les options", "deux au minimum, dont une gratuite"]],
              cle=0,
              note="Puis deux éléments que tout le monde saute : ce qui n'est pas connu, et la suite proposée avec une date.",
              notes="Diapositive à photographier. Les deux éléments de la note sont "
                    "ceux qui manquent dans quatre-vingts pour cent des présentations "
                    "de débutants.")

    d.regle("Un chiffre inventé discrédite tous les autres",
            "Dire ce qu'on ne sait pas, et nommer qui le sait.",
            precision="« Je n'ai pas le chiffre exact, madame Ouellet l'a et je ne "
                      "voulais pas l'inventer ici. » Cette phrase-là fait plus pour la "
                      "crédibilité d'Aïcha que tous les chiffres qu'elle a donnés "
                      "avant. La raison est simple : un chiffre faux qu'on découvre "
                      "jette le doute sur tous les autres, y compris les vrais.",
            notes="Diapositive à photographier. Faire recopier la phrase d'Aïcha telle "
                  "quelle : elle est réutilisable mot pour mot.")

    d.pratique('Pratique', "Quelle partie de l'évaluation ?",
               "À quel élément chaque phrase d'Aïcha appartient-elle ?", [
        ("« Jean-Marc a été absent onze jours ouvrables. »", "le constat"),
        ("« L'emballeur se penche quatre-vingt-deux fois par quart. »", "la cause"),
        ("« Quinze jours d'absence, plus un poste allégé. »", "la conséquence chiffrée"),
        ("« Faire tourner les gens : ça ne coûte rien. »", "le correctif gratuit"),
        ("« Je n'ai pas le chiffre exact, madame Ouellet l'a. »", "ce qui n'est pas connu"),
        ("« La rotation à l'essai à partir du lundi 22 septembre. »", "l'échéance"),
    ], corrige=True,
       notes="C'est l'exercice `t2eval` du module, qui en compte huit. Faire répondre "
             "sans regarder le tableau précédent.")

    d.cartes('Analyse', "Pourquoi le gratuit avant le payant", [
        ("Parce qu'on ne peut pas vous refuser les deux", "Une option unique et chère se refuse en une phrase. Deux options, dont une gratuite, obligent à choisir plutôt qu'à dire non."),
        ("Parce que ça montre votre sérieux", "Proposer d'abord ce qui ne coûte rien prouve que vous n'êtes pas venu chercher de l'argent par réflexe."),
        ("Parce que ça permet d'agir tout de suite", "La rotation peut commencer lundi. La table, elle, prendra deux mois. Un projet qui produit quelque chose vite se poursuit plus facilement."),
        ("Parce qu'elles doivent être indépendantes", "Si la table est refusée, la rotation reste possible. C'est ce qu'Aïcha dit explicitement, et c'est ce qui sauve son projet."),
    ], notes="Les quatre raisons se valent, mais la dernière est la plus fine. Faire "
             "relire la réplique d'Aïcha : « C'est voulu. »")

    d.pratique('Pratique', "Le mot juste",
               "Complétez avec le mot de l'évaluation sommaire.", [
        ("Ce que j'ai vu et compté moi-même, c'est le ...", "constat"),
        ("Pourquoi ça arrive, c'est la ...", "cause"),
        ("Ce que le problème coûte, c'est la ...", "conséquence"),
        ("Le changement que je propose est un ...", "correctif"),
        ("La date à laquelle ce sera fait est l'...", "échéance"),
        ("La personne nommée pour le faire est le ...", "responsable"),
    ], corrige=True,
       notes="Forme papier de l'exercice `t2lex`. Ces six mots sont ceux que tout le "
             "monde emploie en milieu de travail : les employer fait gagner du temps.")

    d.billet(
        "Assemblez votre évaluation sommaire, en sept lignes.",
        exemples=[
            "Une ligne par élément, dans l'ordre du tableau.",
            "N'oubliez ni « ce que je ne sais pas », ni la date.",
            "Deux options, dont une qui ne coûte rien.",
        ],
        notes="C'est le devoir le plus important du module. Ramasser, corriger, "
              "rendre : ce texte est ce que l'élève présentera à voix haute en E1.")

    return d.save(dossier)
