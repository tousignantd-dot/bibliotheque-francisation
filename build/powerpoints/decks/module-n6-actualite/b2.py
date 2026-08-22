# -*- coding: utf-8 -*-
"""B2 · Suivre une démarche en étapes
Bloc B « Défi 1 · La chronique pratique » · couleur teal · 75 min.
Source : exercice `t1ordre` et sa mini-leçon « Suivre une démarche en
étapes ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='teal',
        titre="Suivre une démarche en étapes",
        chapeau="D'une chronique pratique, on ne retient pas les mots : on "
                "retient l'ordre. Et l'ordre n'est pas toujours annoncé - il "
                "se cache parfois dans une condition ou dans un seul verbe.",
        duree='75 minutes')

    d.titre(notes="Deuxième séance du Défi 1. Le groupe connaît le sujet ; il peut donc "
                  "écouter pour autre chose. Rappeler la méthode des trois écoutes, "
                  "affichée depuis B1.")

    d.objectifs([
        "remettre dans l'ordre les trois étapes d'un recours ;",
        "reconnaître un rang annoncé : premièrement, d'abord, enfin ;",
        "reconnaître un rang caché dans une condition en « si » ;",
        "reconnaître un rang caché dans un verbe comme « retourner ».",
    ], notes="Les deux derniers objectifs sont le cœur de la séance. Le premier et le "
             "deuxième vont vite ; garder le temps pour les rangs cachés.")

    d.declencheur(
        'Observation', "Comment sais-tu ce qui vient avant ?",
        pistes=[
            "« Si ça ne bouge pas, vous écrivez une mise en demeure. »",
            "« Vous retournez voir le commerçant. »",
            "Où est le mot qui dit que c'est la deuxième étape ?",
            "Est-ce qu'il y en a un ?",
        ],
        notes="Laisser le groupe chercher le mot d'ordre pendant une bonne minute. Il "
              "n'y en a pas, et c'est la découverte de la séance : l'ordre se déduit du "
              "sens, pas d'un mot.")

    d.tableau('Analyse', "La démarche de la chronique, dans l'ordre",
              ['Le rang', 'Ce qu\'on fait'],
              [["Premièrement", "retourner voir le commerçant, en nommant la garantie légale"],
               ["Deuxièmement", "écrire une mise en demeure, avec un délai de dix jours"],
               ["Troisièmement", "les petites créances, seul et sans avocat"],
               ["Dès l'achat", "garder la facture, ou en prendre une photo"],
               ["N'importe quand", "téléphoner à l'Office pour savoir si on a un recours"]],
              cle=0,
              note="Les deux dernières lignes ne sont pas des étapes : elles se font hors de l'ordre.",
              notes="Diapositive à photographier. C'est le tableau que l'élève devra "
                    "restituer à l'oral en E1. Le faire recopier au complet.")

    d.regle("L'ordre se retient, les mots s'oublient",
            "Sauter une étape fait perdre le recours.",
            precision="On ne peut pas écrire une mise en demeure sans être retourné "
                      "voir le commerçant, et on ne peut pas aller aux petites créances "
                      "sans avoir écrit. Chaque étape suppose que la précédente a "
                      "échoué. C'est pour cela que la seule chose à retenir d'une "
                      "chronique pratique, c'est l'ordre.",
            notes="Diapositive à photographier. Faire redire l'ordre par trois élèves "
                  "différents, sans le tableau sous les yeux.")

    d.cartes("Quatre façons de marquer un rang", "Et deux d'entre elles ne se voient pas", [
        ("Les rangs annoncés",
         "premièrement, deuxièmement, troisièmement. Le plus clair, et le plus rare à l'oral."),
        ("Les rangs déguisés en récit",
         "d'abord, ensuite, enfin. Même chose, mais ça se parle."),
        ("Le rang caché dans une condition",
         "« si ça ne bouge pas, vous écrivez » : cette étape ne se fait que si l'autre a échoué."),
        ("Le rang caché dans un verbe",
         "« vous retournez voir le commerçant » : retourner suppose qu'on y est déjà allé."),
    ], notes="Une carte à la fois. Pour les deux dernières, demander un autre exemple "
             "au groupe : reprendre, rappeler, réessayer portent tous le même sens de "
             "seconde fois.")

    d.pratique('Association', "Les étapes, dans leur ordre",
               "Associez chaque rang à ce qu'on fait.", [
        ("Premièrement", "retourner voir le commerçant et nommer la garantie légale"),
        ("Deuxièmement, si ça ne bouge pas", "écrire une mise en demeure et donner un délai de dix jours"),
        ("Troisièmement, en dernier recours", "s'adresser à la Division des petites créances, seul"),
        ("À faire dès le jour de l'achat", "garder la facture, ou en prendre une photo"),
        ("À faire à n'importe quel moment", "téléphoner à l'Office pour savoir si on a un recours"),
    ], corrige=True,
       notes="Faire répondre sans notes. Si le groupe hésite entre les deux dernières, "
             "reposer la question autrement : laquelle des deux peut se faire même "
             "avant que l'appareil brise ?")

    d.piege("Écrire avant d'être allé voir",
            "L'appareil a brisé, alors j'ai envoyé une mise en demeure.",
            "Je suis retourné voir le marchand ; comme il refusait, j'ai écrit.",
            "Une mise en demeure envoyée avant toute démarche verbale surprend le "
            "commerçant et durcit la discussion pour rien. La chronique le dit : "
            "beaucoup de dossiers se règlent à la première étape, simplement parce "
            "qu'on a employé le mot « garantie légale ». Sauter cette étape, c'est se "
            "compliquer la vie soi-même.",
            notes="Piège réel, et il coûte cher. Le lier au conseil de Myriam Vaugeois "
                  "en C1 : une lettre change le ton d'une discussion, donc on ne "
                  "l'envoie pas en premier.")

    d.pratique('Repérage', "Où est l'ordre dans ces phrases ?",
               "Dites ce qui marque le rang : un mot, une condition ou un verbe.", [
        ("Premièrement, vous retournez voir le commerçant.", "un mot de rang, et aussi le verbe retourner"),
        ("Si ça ne bouge pas, vous écrivez une mise en demeure.", "une condition en « si »"),
        ("Vous vous représentez vous-même, sans avocat.", "aucun rang : c'est une précision"),
        ("Gardez vos factures, le jour de l'achat.", "un moment précis, hors de la suite des étapes"),
        ("J'y reviens toujours, parce que c'est là qu'on trouve les modèles.", "aucun rang : c'est un ajout"),
    ], corrige=True,
       notes="Les trois dernières lignes sont des pièges volontaires : tout ce qui est "
             "dit dans une chronique n'est pas une étape. Le groupe a tendance à tout "
             "numéroter ; c'est ce qu'il faut corriger ici.")

    d.billet(
        "Redis les trois étapes dans l'ordre, en une phrase chacune.",
        exemples=[
            "Sans regarder tes notes.",
            "Trois phrases courtes valent mieux qu'une longue.",
        ],
        notes="Trois minutes. Ce billet est la répétition directe du TEMPS 2 de la "
              "production orale de E1. Le dire au groupe.")

    return d.save(dossier)
