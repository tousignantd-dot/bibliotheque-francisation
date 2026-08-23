# -*- coding: utf-8 -*-
"""A1 · Ce n'est pas le rôle que je voulais
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`, vocabulaire de la section `prep`.
"""
from theme import Deck

import pathlib

# Chemin déduit du fichier, jamais écrit en dur : le dépôt est aussi construit
# depuis un worktree git, où un chemin absolu vers la copie principale
# pointerait sur des images qui n'y sont pas encore.
IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n7-classe' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Ce n'est pas le rôle que je voulais",
        chapeau="Dans une équipe, quelqu'un doit conduire. Sinon la rencontre "
                "conduit toute seule, et elle conduit mal. Ce module apprend "
                "à faire parler les autres, puis à rendre compte de ce "
                "qu'ils ont dit.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir par une question au groupe : "
                  "avez-vous déjà travaillé en équipe, ici ou au travail ? Qu'est-ce "
                  "qui s'est mal passé ? Les réponses tournent presque toujours "
                  "autour des mêmes trois choses : personne ne conduisait, personne "
                  "ne notait, personne ne surveillait le temps.")

    d.objectifs([
        "nommer les rôles d'une équipe de travail et ce que chacun fait ;",
        "comprendre ce qu'on attend d'une personne qui anime ;",
        "dire ce qu'on préférerait faire, et pourquoi ;",
        "employer les premiers mots du dossier : un mandat, un échéancier, "
        "la répartition des rôles.",
    ], notes="Le deuxième objectif est le cœur du module et il ne sera pas atteint "
             "aujourd'hui. Le poser quand même : les quinze séances y reviennent.")

    d.declencheur(
        'Observation', "Qui parle le plus dans une rencontre d'équipe ?",
        image=IMG + 'ruelle-ombragee.jpg',
        pistes=[
            "Est-ce que c'est la même personne à chaque fois ?",
            "Qui, dans une équipe, ne dit presque jamais rien ?",
            "Est-ce que celui qui parle le plus décide le plus ?",
            "Qu'est-ce qui fait qu'une rencontre finit sans rien décider ?",
        ],
        notes="Question sans mauvaise réponse. La deuxième piste est la plus utile : "
              "presque chaque groupe compte une personne silencieuse, et c'est "
              "souvent celle qui a le plus travaillé. Ne pas nommer personne.")

    d.dialogue('Dialogue · 1 de 3', "Les rôles sont attribués", [
        ("GHISLAINE", "Il reste une chose, et c'est celle dont personne ne parle jamais : les rôles.", True),
        ("YOUSSOUF", "Madame, on ne peut pas juste travailler ensemble, tout le monde pareil ?", True),
        ("GHISLAINE", "Ça donne trois personnes qui parlent en même temps pendant vingt minutes, et une feuille blanche à la fin.", True),
        ("GHISLAINE", "Équipe trois : Youssouf aux notes, Miguel au temps, Neusa à l'animation.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Laisser deux écoutes. La réplique de Youssouf est celle que la moitié "
             "de la classe pense : la prendre au sérieux avant de la contredire.")

    d.dialogue('Dialogue · 2 de 3', "Pourquoi elle, justement", [
        ("NEUSA", "Madame, il y a une erreur. Moi, je cherche bien. Mais faire parler les autres, ce n'est pas moi.", True),
        ("GHISLAINE", "Je sais. C'est exactement pour ça.", True),
        ("GHISLAINE", "Vous n'êtes pas silencieuse parce que vous n'avez pas d'idées. Vous êtes silencieuse parce que vous attendez d'être sûre.", True),
        ("GHISLAINE", "Animer, ça oblige à parler avant d'être sûre.", True),
    ], notes="Le point de posture du module, et il vaut d'être dit au groupe : on ne "
             "donne pas un rôle à qui le fait déjà bien. Beaucoup d'élèves se "
             "reconnaîtront dans « attendre d'être sûre ».")

    d.dialogue('Dialogue · 3 de 3', "Ce que fait une animatrice", [
        ("NEUSA", "Mais concrètement, qu'est-ce qu'une animatrice doit faire ? Décider ?", True),
        ("GHISLAINE", "Presque jamais. Elle ouvre la rencontre en rappelant ce qu'on cherche. Elle donne la parole, et surtout elle la reprend.", True),
        ("GHISLAINE", "Elle fait préciser : quand quelqu'un dit qu'il y a beaucoup d'arbres, elle demande combien, et où, et comment il le sait.", True),
        ("NEUSA", "Et si les deux autres ne sont pas d'accord entre eux ?", True),
    ], notes="La réponse à la dernière question est la matière du Défi 3 : on ne "
             "tranche pas, on reformule. L'annoncer sans l'expliquer aujourd'hui.")

    d.tableau('Analyse', "Cinq rôles, cinq travaux",
              ['Le rôle', 'Ce que la personne fait'],
              [["Animer",
                "ouvrir, donner la parole, faire préciser, résumer les décisions"],
               ["Prendre les notes",
                "écrire ce qui se dit sans le juger, et le relire quand on le demande"],
               ["Surveiller le temps",
                "dire combien il reste, et le dire avant qu'il n'en reste plus"],
               ["Tenir les sources",
                "noter d'où vient chaque chiffre, avec sa date et son auteur"],
               ["Présenter",
                "parler devant la classe au nom de l'équipe"]],
              cle=0,
              note="Cinq rôles, mais trois ou quatre personnes : certains se cumulent.",
              notes="Diapositive à photographier. Faire attribuer les rôles dans les "
                    "équipes de la classe dès aujourd'hui, et les écrire au tableau.")

    d.regle("Animer, c'est faire parler",
            "La personne qui anime parle souvent, et elle parle peu. Elle "
            "ouvre, elle distribue, elle fait préciser, elle reformule, elle "
            "ferme.",
            precision="Elle ne décide presque jamais, et elle donne son avis en "
                      "dernier — ou pas du tout. Dès que celle qui anime prend "
                      "parti, les autres se rangent ou se taisent.",
            notes="Diapositive à photographier. Question fréquente : « alors "
                  "l'animateur n'a pas le droit d'avoir une opinion ? » Si, mais il "
                  "annonce qu'il quitte son rôle un instant. C'est vu en D1.")

    d.vocabulaire('Vocabulaire', "Cinq mots pour commencer", [
        ("un sujet de recherche", "La question précise qu'une équipe reçoit et sur laquelle elle présentera ses trouvailles."),
        ("un mandat", "Ce qu'on demande à quelqu'un de faire, avec ce qui est attendu à la fin."),
        ("animer une rencontre", "Conduire une réunion : ouvrir, donner la parole, faire préciser, résumer."),
        ("la répartition des rôles", "Le partage du travail entre les personnes d'une équipe, décidé au début."),
        ("un échéancier", "La liste de ce qui doit être fait, avec la date de chaque étape."),
    ], notes="Faire répéter avec l'article. « Échéancier » est difficile à prononcer : "
             "le découper en quatre syllabes et le faire dire trois fois.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Les rôles ont été attribués par l'enseignante.", "vrai"),
        ("Neusa aurait préféré chercher les documents.", "vrai"),
        ("Selon Ghislaine, Neusa manque d'idées.", "faux - elle attend d'être sûre"),
        ("L'animatrice tranche les désaccords tout de suite.", "faux - elle reformule d'abord"),
        ("Youssouf a reçu le rôle de la prise de notes.", "vrai"),
        ("Le compte rendu part le soir même aux absents.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le troisième "
             "demande d'écouter une deuxième fois : la distinction est fine.")

    d.billet(
        "Quel rôle prendriez-vous dans une équipe, et lequel vous fait peur ?",
        exemples=[
            "Une phrase pour chacun des deux.",
            "Dites pourquoi, sans vous excuser.",
        ],
        notes="Devoir concret. Les réponses servent en A3, quand les rôles seront "
              "attribués pour de bon : on donne à chacun celui qui lui fait un peu "
              "peur, comme Ghislaine le fait avec Neusa.")

    return d.save(dossier)
