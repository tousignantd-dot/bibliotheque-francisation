# -*- coding: utf-8 -*-
"""A1 · Un départ précipité — mise en situation.
Bloc A « Je découvre » · couleur teal · 75 min.
Source du module : dialogue `prep`, exercices `prVocab` et `pr1`, cartes mémoire.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A1', section='teal',
        titre='Un départ précipité',
        chapeau="L'école appelle : la fille de Karim a de la fièvre. Il doit partir tout "
                "de suite. Mais c'est déjà sa deuxième absence ce mois-ci, et il a peur "
                "de la réaction de son superviseur.",
        duree='75 minutes')

    d.titre(notes="Ouverture du module 3. Écrire au tableau : AVANT DE PARTIR. C'est le "
                  "moment qui décide de tout, et c'est le sujet des seize séances.")

    d.objectifs([
        "distinguer un retard, une absence et un abandon ;",
        "savoir à quel moment prévenir, et pourquoi c'est celui-là ;",
        "expliquer une raison sans s'excuser longuement ;",
        "proposer une solution en même temps que le problème.",
    ], notes="Le troisième objectif surprend souvent. Le lire lentement : on peut "
             "expliquer sans se justifier pendant cinq minutes.")

    d.declencheur(
        'Mise en situation', "L'école appelle. Vous devez partir maintenant. Que faites-vous ?",
        pistes=[
            "Est-ce que vous prévenez avant de partir, ou après ?",
            "Qui prévenez-vous exactement ?",
            "Qu'est-ce que vous dites, en une phrase ?",
            "Est-ce que vous proposez quelque chose ?",
        ],
        notes="Cinq minutes en grand groupe. Beaucoup diront « je pars et j'explique "
              "demain ». Noter cette réponse : c'est celle que la séance va corriger.")

    d.cartes('La situation', "Ce qu'on sait de Karim", [
        ("Ce qui arrive",
         "L'école vient d'appeler : sa fille Sarah a de la fièvre. Il doit aller la "
         "chercher tout de suite."),
        ("Ce qui l'inquiète",
         "C'est sa deuxième absence du mois. Il a peur que son superviseur soit fâché."),
        ("À qui il en parle",
         "À Nadia, sa collègue. Elle lui donne trois conseils en une seule réplique."),
        ("Ce qu'il décide",
         "Il appelle son superviseur avant de partir, il explique calmement, et il "
         "propose de reprendre les heures."),
    ], notes="Insister sur la deuxième carte : la peur de Karim est légitime et très "
             "répandue. La séance ne la nie pas, elle donne les moyens de la gérer.")

    d.dialogue('Dialogue · 1 de 3', "Je dois aller la chercher tout de suite", [
        ("KARIM", "Nadia, je viens de recevoir un appel de l'école. Ma fille Sarah a de "
                  "la fièvre, je dois aller la chercher tout de suite. Mais c'est déjà "
                  "ma deuxième absence ce mois-ci… j'ai peur que mon superviseur soit "
                  "fâché.", True),
        ("NADIA", "Ne t'inquiète pas, la santé de ta fille passe avant tout. "
                  "L'important, c'est de prévenir ton superviseur tout de suite, avant "
                  "de partir, pas après.", True),
    ], consigne="Écoutez d'abord l'enregistrement, diapo masquée. Lisez ensuite.",
       notes="Passer l'audio de « Je découvre ». Faire relever la phrase clé de Nadia : "
             "« avant de partir, pas après ». L'écrire au tableau.")

    d.dialogue('Dialogue · 2 de 3', "Qu'est-ce que je dis ?", [
        ("KARIM", "Tu as raison. Mais qu'est-ce que je dis si on me demande pourquoi "
                  "c'est déjà la deuxième fois ce mois-ci ?", True),
        ("NADIA", "Explique la situation calmement, sans t'excuser trop longtemps, et "
                  "propose de reprendre les heures manquées plus tard dans la semaine. "
                  "Ça montre ta bonne volonté.", True),
    ], notes="Trois conseils dans une seule réplique : expliquer calmement, ne pas "
             "s'excuser longtemps, proposer une solution. Les faire compter par le "
             "groupe.")

    d.dialogue('Dialogue · 3 de 3', "Je l'appelle maintenant", [
        ("KARIM", "D'accord, je l'appelle maintenant. Merci pour le conseil, Nadia.",
         True),
    ], notes="Une réplique, un mot important : « maintenant ». C'est le mot de la "
             "séance.")

    d.regle('La règle de la séance',
            "On prévient avant de partir, pas après être revenu.",
            precision="Un superviseur prévenu à temps peut organiser le travail. Prévenu "
                      "le lendemain, il a passé la journée à chercher quelqu'un. Ce "
                      "n'est pas la faute qui dérange, c'est le silence.",
            notes="Écrire la règle au tableau et l'y laisser tout le module. C'est celle "
                  "qui revient dans les seize séances.")

    d.tableau('Analyse', "Les trois conseils de Nadia",
              ['Le conseil', 'Pourquoi'],
              [["prévenir avant de partir", "le travail peut être réorganisé"],
               ["expliquer calmement", "une explication vaut mieux qu'une excuse"],
               ["ne pas s'excuser longtemps", "cela donne l'air de cacher quelque chose"],
               ["proposer de reprendre", "cela montre la bonne volonté"]],
              cle=0,
              note="Le quatrième est celui qui change tout : proposer une solution "
                   "transforme un problème en arrangement.",
              notes="Faire écrire les quatre dans le cahier. Ils servent de plan pour "
                    "toutes les productions du module.")

    d.vocabulaire('Vocabulaire · 1 de 2', "Les trois mots à ne pas confondre", [
        ("un retard", "Le fait d'arriver après un moment fixé."),
        ("une absence", "Le fait de ne pas se trouver à un endroit où on est attendu."),
        ("un abandon", "Le fait de renoncer à une chose : un cours, un travail."),
        ("prévenir", "Informer à l'avance."),
        ("justifier", "Donner la raison d'un retard ou d'une absence."),
        ("reprendre des heures", "Travailler plus tard pour remplacer les heures manquées."),
    ], notes="Ces trois premiers mots sont le sujet de la séance A3. Les installer ici, "
             "les travailler là-bas.")

    d.vocabulaire('Vocabulaire · 2 de 2', "Le travail et l'école", [
        ("une superviseure", "La personne responsable des employés."),
        ("un billet médical", "Un document du médecin qui confirme une consultation."),
        ("une boîte vocale", "Le système qui enregistre un message quand personne ne répond."),
        ("remplacer", "Prendre la place de quelqu'un."),
        ("une pièce d'identité", "Un document officiel qui prouve qui on est."),
        ("une entrevue d'embauche", "Une rencontre pour obtenir un emploi."),
    ], notes="« Boîte vocale » est le mot du défi 1 : le faire prononcer et écrire "
             "correctement dès maintenant.")

    d.pratique('Pratique', "Vrai ou faux — un départ précipité",
               "Répondez sans relire le dialogue.", [
        ("C'est Nadia qui appelle Karim pour lui dire que sa fille est malade.",
         "FAUX — c'est l'école"),
        ("Karim doit aller chercher sa fille à l'école.", "VRAI"),
        ("C'est la première absence de Karim ce mois-ci.", "FAUX — la deuxième"),
        ("Nadia conseille de prévenir le superviseur avant de partir.", "VRAI"),
        ("Karim et Nadia travaillent ensemble.", "VRAI"),
        ("Sarah est la fille de Karim.", "VRAI"),
        ("Karim propose de reprendre les heures manquées.", "VRAI"),
        ("Karim doit s'excuser longuement avant d'expliquer.", "FAUX — sans s'excuser trop longtemps"),
    ], corrige=True,
       notes="Le dernier énoncé est le plus important du module. Le corriger lentement "
             "et en discuter : beaucoup d'élèves croient le contraire.")

    d.piege("Le piège de l'excuse trop longue",
            "Je suis vraiment désolé, je m'excuse, ça ne se reproduira plus, vraiment désolé…",
            "Ma fille est malade, je dois aller la chercher. Je peux reprendre les heures jeudi.",
            "Une longue excuse occupe le temps sans donner d'information. Le superviseur "
            "veut savoir deux choses : pourquoi, et comment on s'arrange. Les excuses "
            "répétées donnent au contraire l'impression qu'on cache quelque chose.",
            notes="Point culturel important. Dans plusieurs cultures, l'excuse longue est "
                  "une marque de respect. Ici, elle est lue comme de l'embarras. Le dire "
                  "sans juger ni l'une ni l'autre.")

    d.billet(
        "Vous devez partir du travail tout de suite. Écrivez ce que vous diriez, en deux phrases.",
        exemples=[
            "Une phrase pour la raison, une phrase pour la solution que vous proposez.",
            "Exemple : « Mon fils est malade, je dois aller le chercher. Je peux "
            "reprendre les heures vendredi. »",
        ],
        notes="Ramasser. Ces billets serviront en B4 et C4, où la même phrase sera dite "
              "au téléphone.")

    return d.save(dossier)
