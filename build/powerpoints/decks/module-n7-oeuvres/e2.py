# -*- coding: utf-8 -*-
"""E2 · Le compte rendu, et le bilan
Bloc E « Je me lance » · couleur framboise · production écrite · 75 min.
Source : section `appli` (production écrite) et « Je retiens des mots ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="Le compte rendu, et le bilan",
        chapeau="Un compte rendu qui ne garde que l'avis du gagnant n'est plus "
                "un compte rendu : c'est une affiche. Celui qui a perdu le "
                "vote doit s'y reconnaître.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du module. Redistribuer les phrases de concession "
                  "de D2 et les arguments de C4 : le compte rendu s'écrit avec les "
                  "deux sous les yeux.")

    d.objectifs([
        "écrire un compte rendu en trois paragraphes ;",
        "rapporter honnêtement l'avis contraire, avec sa raison ;",
        "employer une concession, une mise en relief et deux connecteurs ;",
        "faire le bilan de ce qu'on sait maintenant faire.",
    ], notes="Le deuxième objectif est ce qui distingue ce texte d'un texte "
             "d'opinion : on rapporte l'avis de l'autre sans l'affaiblir en le "
             "rapportant.")

    d.declencheur(
        'Préparation', "À qui écrit-on un compte rendu, et pourquoi ?",
        pistes=[
            "Aux gens qui étaient là, ou à ceux qui n'y étaient pas ?",
            "Qu'est-ce qu'ils ont besoin de savoir en premier ?",
            "Que se passe-t-il si quelqu'un ne se reconnaît pas dans le texte ?",
            "Est-ce qu'on écrit ce qu'on aurait aimé entendre ?",
        ],
        notes="La troisième piste est la vraie règle du genre : celui qui ne se "
              "reconnaît pas dans le compte rendu ne revient pas à la réunion "
              "suivante. C'est une question pratique, pas morale.")

    d.tableau('Analyse', "Trois paragraphes, trois travaux",
              ['Le paragraphe', 'Ce qu\'il contient'],
              [["L'œuvre", "de quelle œuvre on a parlé, et ce qu'elle raconte"],
               ["Les deux avis", "le vôtre et le contraire, chacun avec sa raison"],
               ["La décision", "ce qui a été décidé, et l'argument qui l'a emporté"]],
              cle=0,
              note="Dix à quatorze phrases en tout. Un compte rendu long ne se lit pas.",
              notes="Diapositive à photographier. La structure vaut pour tout compte "
                    "rendu de rencontre, quel qu'en soit l'objet.")

    d.cartes('Analyse', "Huit exigences, tirées du module", [
        ("Le titre et le résumé", "deux phrases, sans la fin"),
        ("Votre avis annoncé", "j'ai trouvé, il m'a semblé"),
        ("Le moment précis", "à la quatrième nuit, il..."),
        ("L'avis contraire", "rapporté avec sa raison, honnêtement"),
        ("Une concession", "bien que le début soit lent"),
        ("Une mise en relief", "ce qui m'a convaincue, c'est"),
        ("Un connecteur qui annonce", "quant à, en ce qui concerne"),
        ("Un connecteur qui ramasse", "en somme, par conséquent"),
    ], cols=1,
       notes="Les huit exigences sont celles du module. Les faire cocher une à une "
             "avant l'envoi : c'est la grille de correction.")

    d.piege('Écrit',
            "« Gaétan n'était pas d'accord, mais il n'avait pas de raison. »",
            "« Gaétan a fait valoir que le rire est contagieux dans une salle. »",
            "La première phrase rapporte l'avis contraire en le vidant : "
            "personne ne se reconnaît là-dedans, et le compte rendu perd sa "
            "valeur de preuve. La seconde donne la raison telle qu'elle a été "
            "dite, et elle ne coûte rien à votre propre position.",
            notes="Point d'éthique de l'écrit, et point pratique : un compte rendu "
                  "contesté est un compte rendu qu'il faut réécrire.")

    d.pratique('Production écrite', "Votre compte rendu",
               "Dix à quatorze phrases, en trois paragraphes.", [
        ("Paragraphe 1", "l'œuvre, et ce qu'elle raconte en deux phrases"),
        ("Paragraphe 2", "votre avis avec son moment, puis l'avis contraire avec sa raison"),
        ("Paragraphe 3", "la décision, et l'argument qui l'a emportée"),
        ("Avant d'envoyer", "cochez les huit exigences, une par une"),
    ], corrige=False,
       notes="Le module corrige le texte par l'assistant et permet de le déposer. En "
             "classe, faire relire par un pair avec la grille des huit exigences "
             "avant la correction automatique.")

    d.tableau('Bilan', "Ce que vous savez maintenant faire",
              ['La situation', 'Ce que vous employez'],
              [["Un sketch", "l'ironie, la caricature, la chute"],
               ["Une chanson", "le refrain, l'image, ce que reprend « ils »"],
               ["Une critique", "le fait, l'opinion, la nuance, la condition finale"],
               ["Un désaccord", "la concession, puis votre position"],
               ["Un refus poli", "si plus imparfait, puis le conditionnel"],
               ["Un écrit officiel", "le registre soutenu, et les connecteurs"]],
              cle=0,
              notes="Diapositive à photographier, et dernière du module. C'est la "
                    "grille que l'élève emporte : six lignes, et elles suffisent.")

    d.billet(
        "Qu'est-ce que vous direz autrement, la prochaine fois qu'on vous "
        "demandera votre avis ?",
        exemples=[
            "Une chose, en une phrase.",
            "Nommez ce que vous ajouterez, pas seulement ce que vous éviterez.",
        ],
        notes="Billet de sortie du module. Les réponses valent d'être lues à voix "
              "haute à la fin : elles disent ce que seize séances ont réellement "
              "déposé.")

    return d.save(dossier)
