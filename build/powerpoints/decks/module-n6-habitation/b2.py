# -*- coding: utf-8 -*-
"""B2 · La cause, ou le résultat ?
Bloc B « Défi 1 · Le diagnostic » · couleur teal · 75 min.
Source : exercices `t1cause` et `t1ordre`, mini-leçon `t1cause`. Savoirs du
programme : employer des connecteurs de relations logiques ; comprendre
l'ordre des étapes d'une consigne à partir d'indices linguistiques.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='teal',
        titre="La cause, ou le résultat ?",
        chapeau="Réparer un résultat coûte une fois, puis une deuxième, puis "
                "une troisième. Réparer la cause coûte une fois.",
        duree='75 minutes')

    d.titre(notes="Séance de raisonnement autant que de langue. C'est la séance la "
                  "plus rentable du bloc : elle change la façon dont les élèves "
                  "écoutent un homme de métier pour le reste de leur vie.")

    d.objectifs([
        "distinguer une cause d'un résultat ;",
        "employer les connecteurs de cause et de conséquence ;",
        "dire pourquoi chaque étape d'un chantier vient à sa place ;",
        "poser la question qui vérifie qu'on regarde bien la cause.",
    ], notes="Le quatrième objectif est une phrase à faire apprendre par cœur : « si "
             "vous réparez seulement ça, est-ce que ça revient ? »")

    d.declencheur(
        'Observation', "Une tache d'eau revient chaque printemps au même endroit. Que répare-t-on ?",
        pistes=[
            "La tache, ou ce qui la produit ?",
            "Qu'est-ce qui se passe si on repeint seulement ?",
            "Combien de fois peut-on repeindre avant de se poser la question ?",
        ],
        notes="Presque tout le monde répond « on repeint » en premier. C'est le "
              "meilleur départ possible : personne n'a tort, et l'erreur est celle "
              "qu'on veut nommer.")

    d.tableau('Analyse', "Les mots qui annoncent une cause",
              ['Le mot', 'Un exemple'],
              [["parce que", "Le mur fend parce que le sol pousse."],
               ["à cause de", "La fondation est humide à cause de la gouttière."],
               ["grâce à", "Le sol reste sec grâce à la nouvelle pente."],
               ["car", "L'injection attendra, car le mur reçoit de l'eau."]],
              cle=0,
              note="« À cause de » annonce un mauvais résultat, « grâce à » un bon.",
              notes="Diapositive à photographier. L'écart entre « à cause de » et "
                    "« grâce à » n'existe pas dans toutes les langues : le signaler.")

    d.tableau('Analyse', "Les mots qui annoncent une conséquence",
              ['Le mot', 'Un exemple'],
              [["donc", "Le sol pousse, donc le mur fend."],
               ["de sorte que", "L'eau reste au mur, de sorte qu'il ne sèche pas."],
               ["par conséquent", "La cause n'a pas été traitée ; par conséquent, la fissure est revenue."],
               ["d'où", "Le sol se gorge d'eau, d'où la pression sur le mur."]],
              cle=0,
              note="« D'où » est suivi d'un nom, jamais d'une phrase complète.",
              notes="Diapositive à photographier. « D'où » est le seul des quatre qui "
                    "demande une construction particulière ; c'est aussi le plus "
                    "fréquent dans les documents techniques.")

    d.regle("Le test qui ne trompe pas",
            "« Si je répare seulement ça, est-ce que ça revient ? »",
            precision="Posez la question à voix haute, devant l'entrepreneur. S'il "
                      "répond oui, vous regardez un résultat, et le devis que vous "
                      "avez en main ne réglera rien. Cette phrase-là vaut plusieurs "
                      "milliers de dollars, et elle ne coûte rien à dire.",
            notes="Diapositive à photographier. Faire répéter la phrase par tout le "
                  "groupe, à voix haute. C'est un des rares moments du module où la "
                  "répétition chorale a du sens.")

    d.pratique('Pratique', "Cause ou résultat ?",
               "Pour chaque élément, dites s'il est la cause ou le résultat.", [
        ("La descente de gouttière se vide au pied du mur.", "la cause"),
        ("Le mur de fondation a fendu en biais.", "le résultat"),
        ("La terre s'est tassée et la pente ramène l'eau.", "la cause"),
        ("Le taux d'humidité du mur est de dix-neuf pour cent.", "le résultat"),
        ("On a refermé le mur avant qu'il soit sec.", "la cause"),
        ("De la moisissure pousse derrière le gypse neuf.", "le résultat"),
    ], corrige=True,
       notes="Faire justifier chaque réponse par le test de la règle. Le quatrième "
             "fait discuter : l'humidité est un résultat ici, mais elle devient une "
             "cause à l'étape suivante. Accepter la discussion, elle est juste.")

    d.piege('Piège', "croire qu'une seule cause explique tout",
            "accepter qu'il y en ait deux ou trois",
            "La gouttière, et la pente, et le drain d'origine. Les causes "
            "s'additionnent souvent, et traiter une seule des trois ne règle qu'un "
            "tiers du problème. C'est pour ça qu'un entrepreneur sérieux propose "
            "trois postes là où le voisin en propose un.",
            notes="C'est aussi ce qui explique l'écart entre deux soumissions. Le "
                  "signaler : la moins chère est parfois celle qui traite le moins "
                  "de causes.")

    d.pratique('Pratique', "Pourquoi cette étape vient là ?",
               "Associez chaque étape à ce qui l'oblige à venir à cette place.", [
        ("1. rallonger les gouttières", "tant que l'eau arrive au mur, tout sera refait"),
        ("2. refaire la pente", "on creuse dehors, et on ne creuse pas deux fois"),
        ("3. injecter la fissure", "le produit ne tient que dans un mur qui ne reçoit plus d'eau"),
        ("4. laisser sécher", "un mur refermé sur son humidité fait pousser de la moisissure"),
        ("5. isoler et poser le gypse", "c'est la première étape qu'on ne peut plus défaire"),
    ], corrige=True,
       notes="Exercice central de la séance. Faire dire la raison à voix haute avant "
             "de corriger. La cinquième est celle qui reste : à partir du gypse, on "
             "ne revient plus en arrière sans tout casser.")

    d.billet(
        "Raconte un problème que quelqu'un a réparé sans traiter la cause.",
        exemples=[
            "Chez toi, au travail, ou ailleurs.",
            "Dis ce qui est arrivé ensuite.",
        ],
        notes="Trois minutes. Les histoires rapportées sont excellentes et servent en "
              "B3 : la moitié d'entre elles contiennent un « il », un « en » ou un "
              "« y » dont le référent se perd.")

    return d.save(dossier)
