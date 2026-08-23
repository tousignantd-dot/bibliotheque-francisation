# -*- coding: utf-8 -*-
"""B2 · Le rapport d'expertise, lu par blocs
Bloc B « Défi 1 · Le rapport qu'on discute » · couleur acier · 75 min.
Source : exercice `t1rap`, de type `texte`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='acier',
        titre="Cinq blocs, et on lit le mandat en premier",
        chapeau="Un rapport d'expertise a toujours la même structure. La "
                "repérer avant de lire une ligne change tout : la conclusion "
                "se comprend mal si l'on ne sait pas d'où chaque fait vient.",
        duree='75 minutes')

    d.titre(notes="Séance de compréhension écrite. Prévoir le rapport projeté et une "
                  "copie papier par équipe de deux, avec un crayon : la lecture se "
                  "fait crayon en main, pas des yeux.")

    d.objectifs([
        "repérer les cinq blocs d'un rapport d'expertise ;",
        "prélever un fait mesuré et le distinguer d'une opinion ;",
        "trouver dans un rapport ce qu'il avoue ne pas avoir vérifié ;",
        "comparer le rapport à la lettre de refus.",
    ], notes="Le troisième objectif est le plus rentable : ce que le rapport avoue "
             "est ce qui se conteste le mieux.")

    d.declencheur(
        'Lecture', "Lisez la première ligne du rapport. À qui s'adresse-t-il ?",
        pistes=[
            "Qui l'a demandé ? Qui l'a payé ?",
            "Est-ce qu'il s'adresse à Teodora quelque part ?",
            "Est-ce qu'il répond à une seule de ses questions ?",
            "Pourquoi est-ce important de le savoir avant de le lire ?",
        ],
        notes="La réponse est encourageante et il faut la dire : le rapport n'a pas "
              "été écrit pour convaincre Teodora. Il a été écrit pour être exact — "
              "et l'exactitude, ça se vérifie.")

    d.regle("Cinq blocs, toujours les mêmes",
            "Mandat, constatations, renseignements obtenus, analyse, "
            "conclusion. Repérez-les avant de lire une seule ligne.",
            precision="Le mandat est le bloc que personne ne lit, et c'est souvent le "
                      "plus utile : un expert à qui l'on n'a pas demandé d'inspecter "
                      "le drain n'a pas inspecté le drain.",
            notes="Diapositive à photographier. Faire marquer les cinq blocs au crayon "
                  "dans la copie papier, avant tout le reste.")

    d.cartes('Analyse', "Ce que chaque bloc vaut", [
        ("Mandat",
         "Ce qu'on a demandé à l'expert, et donc ce qu'il n'a pas eu à "
         "faire. Ici : déterminer la cause et évaluer les dommages. Rien sur "
         "l'entretien passé, rien sur l'historique du drain."),
        ("Constatations",
         "Ce qu'il a vu et mesuré, avec une heure d'arrivée et de départ. "
         "Vingt-cinq minutes sur les lieux : c'est un fait, il est écrit, et "
         "il se retourne."),
        ("Renseignements obtenus",
         "Ce qu'on lui a dit — par l'assurée, par la ville. Non vérifié, et "
         "le rapport le signale en le rangeant ici."),
        ("Analyse et conclusion",
         "Ce qu'il en déduit. C'est le bloc qui fonde le refus, et c'est "
         "celui qui n'engage rien : « la cause probable est »."),
    ], notes="Faire relever les vingt-cinq minutes : le rapport les écrit lui-même. "
             "Personne n'a besoin de les contester, il suffit de les citer.")

    d.pratique('Compréhension écrite', "Où trouve-t-on la réponse ?",
               "Pour chaque question, nommez le bloc et citez le passage.", [
        ("Que l'expert avait-il reçu comme mandat ?", "mandat - déterminer la cause et évaluer les dommages"),
        ("Combien de temps est-il resté sur les lieux ?", "constatations - de 10 h 15 à 10 h 40"),
        ("Quelle mesure a-t-il prise avec un instrument ?", "constatations - une pente de 2 cm sur 3 m"),
        ("Quel passage rapporte une parole plutôt qu'une observation ?", "renseignements - « selon l'assurée »"),
        ("Quel passage est une déduction ?", "analyse - « il appert que l'obstruction s'est formée progressivement »"),
        ("Qu'est-ce que le rapport avoue ne pas avoir fait ?", "analyse - aucune inspection par caméra"),
    ], corrige=True,
       notes="Le sixième est celui qui gagne le dossier, et personne ne le trouve du "
             "premier coup : c'est une phrase négative au milieu du bloc d'analyse. "
             "Laisser chercher trois bonnes minutes avant d'aider.")

    d.piege(
        'Lecture',
        "Le rapport fait quatre pages, il est donc solide",
        "Comptez les constats, puis comptez les déductions",
        "Quatre pages peuvent contenir six constats et douze déductions. La "
        "longueur ne prouve rien ; la proportion, oui. Et ici, la "
        "vérification décisive — passer une caméra dans le tuyau — n'a "
        "jamais été faite : le rapport l'écrit lui-même, en une ligne, au "
        "milieu de l'analyse.",
        notes="Faire compter réellement, en équipes : combien de phrases « vu », "
              "combien de phrases « déduit ». Le résultat frappe plus qu'une "
              "explication.")

    d.tableau('Analyse', "Trois phrases, trois poids",
              ['La phrase du rapport', 'Ce qu\'elle vaut'],
              [["J'ai mesuré une pente de deux centimètres sur trois mètres.",
                "constat mesuré — solide"],
               ["Selon l'assurée, aucun refoulement depuis 2019.",
                "rapporté — non vérifié"],
               ["Il appert que l'obstruction s'est formée progressivement.",
                "déduction — c'est ici qu'on conteste"]],
              cle=0,
              note="Le conditionnel d'un rapport n'est pas une politesse : c'est un aveu.",
              notes="Diapositive à photographier. Le conditionnel de « le drain "
                    "n'aurait pas été entretenu » veut dire : je le rapporte, je ne "
                    "l'ai pas vérifié.")

    d.billet(
        "Trouvez dans le rapport une phrase qui aide Teodora, et dites pourquoi.",
        exemples=[
            "Recopiez-la telle quelle, avec ses mots exacts.",
            "En une phrase : pourquoi elle l'aide.",
        ],
        notes="Plusieurs réponses sont bonnes : les vingt-cinq minutes, l'absence "
              "d'inspection par caméra, le drain de fondation nommé à la place du "
              "drain de plancher. Les trois se retrouveront dans la lettre du bloc E.")

    return d.save(dossier)
