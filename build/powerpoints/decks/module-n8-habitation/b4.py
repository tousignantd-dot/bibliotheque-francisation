# -*- coding: utf-8 -*-
"""B4 · Le passif, ou l'art de ne nommer personne
Bloc B « Défi 1 · Le rapport qu'on discute » · couleur ambre · 75 min.
Source : exercice `t1pass` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="« Par qui ? » — la question qui ouvre un dossier",
        chapeau="« Le drain n'a pas été entretenu. » La phrase affirme "
                "quelque chose de grave et ne dit pas qui. C'est tout le "
                "travail du passif, et il est partout dans ces documents.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc B. Elle boucle le défi : on a appris à "
                  "trier les phrases d'un rapport, on apprend maintenant à voir ce "
                  "que leur forme même leur permet de taire.")

    d.objectifs([
        "reconnaître le passif, le pronominal passif et l'impersonnel ;",
        "rétablir l'agent effacé par une tournure passive ;",
        "accorder le participe passé au passif ;",
        "écrire soi-même à la voix active, en nommant, datant et chiffrant.",
    ], notes="Le quatrième objectif est celui qui sépare une contestation qui pèse "
             "d'une contestation qui imite l'administration sans en avoir les "
             "moyens.")

    d.declencheur(
        'Observation', "« Le drain n'a pas été entretenu. » Par qui ?",
        pistes=[
            "Qui aurait dû l'entretenir, selon cette phrase ?",
            "La phrase le dit-elle quelque part ?",
            "Si elle ne le dit pas, à qui l'exclusion s'appliquera-t-elle ?",
            "Comment écririez-vous la même idée en nommant quelqu'un ?",
        ],
        notes="Laisser le groupe buter sur la deuxième question. C'est le moment de "
              "la séance : la phrase accuse sans nommer, et personne ne l'avait vu "
              "en la lisant la première fois.")

    d.regle("Le passif n'est pas malhonnête, il est prudent",
            "L'expert ne veut pas écrire « madame Vlaicu n'a pas entretenu "
            "son drain », parce qu'il ne l'a pas vérifié. Le passif lui "
            "permet d'affirmer sans accuser.",
            precision="Le geste de lecture est donc toujours le même : devant tout "
                      "passif d'un document officiel, demandez « par qui ? » à voix "
                      "haute. Si la phrase ne peut pas répondre, elle affirme "
                      "beaucoup moins qu'elle n'en a l'air.",
            notes="Diapositive à photographier. C'est exactement là que se gagne une "
                  "révision : en rétablissant le nom manquant et en montrant qu'il "
                  "ne convient pas.")

    d.cartes('Analyse', "Trois façons de ne nommer personne", [
        ("Le passif",
         "« Le drain n'a pas été entretenu. » · « Le dossier a été fermé la "
         "semaine dernière. » Le sujet subit l'action ; celui qui la fait "
         "disparaît."),
        ("Le pronominal à sens passif",
         "« Une obstruction se forme lentement. » · « La demande s'adresse "
         "par écrit. » Ils ont l'air actifs et ne le sont pas : personne ne "
         "forme, personne n'adresse."),
        ("L'impersonnel",
         "« Il appert que… » · « Il nous a été demandé de… » Le sujet « il » "
         "ne désigne rien du tout. C'est la forme la plus effacée des trois, "
         "et celle des mandats et des conclusions."),
    ], cols=1,
       notes="Le pronominal passif est le plus difficile à repérer parce qu'il "
             "ressemble à un verbe ordinaire. Faire chercher « qui forme ? » sur "
             "chaque exemple.")

    d.pratique('Grammaire', "Rendez son sujet à la phrase",
               "Récrivez à la voix active, en commençant par le sujet donné.", [
        ("Le drain n'a pas été entretenu. (Plomberie Chartier)", "Plomberie Chartier ne l'a pas entretenu"),
        ("Il nous a été demandé de déterminer la cause. (La Mutuelle)", "La Mutuelle nous a demandé de déterminer la cause"),
        ("Une inspection par caméra n'a pas été effectuée. (L'expert)", "L'expert n'a pas effectué d'inspection par caméra"),
        ("Le dossier a été fermé la semaine dernière. (Le service des sinistres)", "Le service des sinistres a fermé le dossier"),
        ("La facture n'a jamais été demandée. (Personne)", "Personne ne m'a jamais demandé la facture"),
        ("Ce type d'obstruction se constate à la caméra. (On)", "On ne le constate qu'à la caméra"),
    ], corrige=True,
       notes="Faire remarquer, à chaque ligne, que la version active est plus courte. "
             "Ce n'est pas un hasard : le passif coûte des mots pour cacher un nom.")

    d.regle("Quand vous écrivez, faites exactement l'inverse",
            "Une contestation nomme les agents. « Plomberie Chartier a "
            "nettoyé le drain le 3 mai. » Un sujet, un verbe, une date : "
            "c'est ce qui se vérifie, donc ce qui pèse.",
            precision="Une seule exception, et elle est utile : la concession. « Un "
                      "dépôt a bien été observé » est plus habile que « votre expert "
                      "a observé un dépôt » — on concède le fait sans concéder "
                      "l'autorité de celui qui l'a vu.",
            notes="Diapositive à photographier. Le réflexe d'imiter la langue "
                  "administrative pour se donner du sérieux est très répandu et "
                  "toujours contre-productif : le nommer explicitement.")

    d.piege(
        'Accord',
        "la facture a été transmis",
        "la facture a été transmise",
        "Au passif, le participe s'accorde TOUJOURS avec le sujet, sans "
        "aucune exception — c'est même le seul cas où la règle n'a pas de "
        "piège. « Les photographies ont été prises », « les deux drains ont "
        "été inspectés », « la contre-expertise a été jointe ».",
        notes="Rassurer : après les accords du plus-que-parfait vus en A4, celui-ci "
              "est le plus simple des trois. Il n'y a rien à chercher.")

    d.pratique('Repérage', "Passif, pronominal passif ou impersonnel ?",
               "Nommez la tournure, puis rétablissez l'agent quand c'est possible.", [
        ("Il a été constaté que le drain était bouché.", "impersonnel - qui l'a constaté ?"),
        ("Une obstruction se forme lentement.", "pronominal passif - personne ne forme"),
        ("Le dossier a été fermé la semaine dernière.", "passif - le service l'a fermé"),
        ("La demande s'adresse par écrit.", "pronominal passif - vous devez l'écrire"),
        ("Il nous a été demandé d'évaluer les dommages.", "impersonnel - la Mutuelle l'a demandé"),
        ("Aucune inspection n'a été effectuée.", "passif - l'expert ne l'a pas faite"),
    ], corrige=True,
       notes="Le premier est le plus intéressant : un impersonnel suivi d'une "
             "affirmation forte est le point faible d'un rapport. Demander la source, "
             "elle est parfois absente du document.")

    d.billet(
        "Récrivez trois phrases du rapport à la voix active, avec un nom et une date.",
        exemples=[
            "Choisissez trois passifs dans le rapport du module.",
            "Pour chacun, écrivez qui a fait quoi, et quand.",
            "Si la phrase ne permet pas de le savoir, écrivez-le aussi.",
        ],
        notes="La dernière consigne est la plus formatrice : découvrir qu'on ne peut "
              "pas rétablir l'agent, c'est découvrir l'argument.")

    return d.save(dossier)
