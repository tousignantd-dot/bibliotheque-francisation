# -*- coding: utf-8 -*-
"""A1 · Qui parle, quand la radio parle ?
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n7-actualite/images/')


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Qui parle, quand la radio parle ?",
        chapeau="Suivre l'actualité, ce n'est pas seulement comprendre les "
                "mots. C'est savoir qui les dit, et à quel titre : un "
                "journaliste qui rapporte n'engage pas la même chose qu'une "
                "chroniqueuse qui juge.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Commencer par une question ouverte au "
                  "groupe : où prenez-vous vos nouvelles ? La radio, la télé, un groupe "
                  "de messagerie, la famille restée au pays. Les réponses donnent le ton "
                  "et montrent tout de suite que la question des sources est vivante.")

    d.objectifs([
        "nommer les grands genres de l'information : reportage, chronique, "
        "éditorial, billet ;",
        "dire ce que chacun fait, et ce qu'il ne fait pas ;",
        "reconnaître qu'un texte peut mêler des faits et des jugements ;",
        "employer les premiers mots du dossier : une source, une manchette.",
    ], notes="Le troisième objectif est le cœur du module et il ne sera pas atteint "
             "aujourd'hui. Le poser quand même : tout le reste y revient.")

    d.declencheur(
        'Observation', "Où prenez-vous vos nouvelles ?",
        image=IMG + 'studio-radio.jpg',
        pistes=[
            "À la radio, à la télévision, sur un téléphone ?",
            "En français, ou dans votre première langue ?",
            "Est-ce que vous vérifiez ce qu'on vous envoie ?",
            "Qu'est-ce qui vous a le plus surpris depuis votre arrivée ?",
        ],
        notes="Question sans mauvaise réponse. Plusieurs élèves suivent surtout "
              "l'actualité de leur pays d'origine, et parfois par des groupes de "
              "messagerie. Ne pas dévaloriser : s'en servir plus loin, quand on parlera "
              "de vérifier une source.")

    d.dialogue('Dialogue · 1 de 3', "Ils parlent de notre rue", [
        ("SUZIE", "Farida ! Monte le son deux secondes, ils parlent de notre rue.", True),
        ("FARIDA", "De la rue Boisjoli ? Attends... je n'ai pas tout saisi. Il a dit qu'un local allait ouvrir.", True),
        ("SUZIE", "Un point de dépôt pour les contenants consignés. Dans l'ancien local de la caisse, au coin.", True),
        ("FARIDA", "Un point de dépôt. C'est là qu'on rapporte les canettes et les bouteilles vides ?", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Farida dit « je n'ai pas tout saisi » : c'est exactement la situation de "
             "l'élève devant une radio. Le nommer tout de suite, et dire qu'on ne "
             "comprend jamais un reportage d'un seul coup.")

    d.dialogue('Dialogue · 2 de 3', "Je ne sais toujours pas qui parle", [
        ("FARIDA", "Suzie, il faut que je te dise quelque chose. J'écoute la radio depuis trois ans et je ne sais toujours pas qui parle.", True),
        ("SUZIE", "Comment ça, qui parle ?", True),
        ("FARIDA", "Le matin, il y a un homme qui raconte ce qui s'est passé. Le samedi, il y a une femme qui parle du même sujet, mais elle se fâche. Est-ce que c'est le même métier ?", True),
        ("SUZIE", "Ah non. Pas du tout. L'homme du matin fait des reportages : il va sur place, il pose des questions, il rapporte ce qu'il a vu et entendu.", True),
    ], notes="C'est la question qui ouvre le module. La faire reformuler par un élève "
             "avant de donner la réponse de Suzie.")

    d.dialogue('Dialogue · 3 de 3', "L'opinion assumée", [
        ("FARIDA", "Et il ne dit pas ce qu'il en pense ?", True),
        ("SUZIE", "Il n'a pas le droit. Son travail, c'est de te donner les faits et de te faire entendre les gens concernés. Toi, tu décides après.", True),
        ("FARIDA", "Donc quand elle dit que la Ville a mal choisi l'endroit, ce n'est pas une nouvelle.", True),
        ("SUZIE", "Voila. C'est son avis. Par contre, si elle dit que la consigne est passée à dix cents, ça, c'est un fait, et tu peux le vérifier.", True),
    ], notes="La dernière réplique contient déjà toute la séance A4. La faire répéter "
             "et l'écrire au tableau : on y reviendra.")

    d.tableau('Analyse', "Quatre façons de parler d'une même nouvelle",
              ['Le genre', 'Ce qu\'il fait'],
              [["Le reportage", "rapporte ce qu'un journaliste a constaté sur place"],
               ["La chronique", "donne l'avis signé d'une personne, chaque semaine"],
               ["L'éditorial", "exprime la position du journal lui-même"],
               ["Le billet de blogue", "un texte court, personnel, que les lecteurs commentent"]],
              cle=0,
              note="Les quatre peuvent parler du même sujet le même jour, sans dire la même chose.",
              notes="Diapositive à photographier. C'est le tableau de référence de tout "
                    "le module ; il revient en A3 sous forme d'exercice.")

    d.regle("Un genre, un engagement",
            "Le reportage rapporte ; la chronique juge, et elle le dit.",
            precision="Ce n'est pas que l'un serait honnête et l'autre non. Une "
                      "chronique est parfaitement honnête : elle annonce qu'elle donne "
                      "un avis. Le problème commence quand le lecteur ne voit pas la "
                      "différence et prend le jugement pour de l'information.",
            notes="Diapositive à photographier. Insister : on ne demande pas à l'élève "
                  "de se méfier de tout, mais de savoir ce qu'il lit.")

    d.vocabulaire('Vocabulaire', "Six mots pour commencer", [
        ("un reportage", "Le compte rendu d'un journaliste qui va sur place et rapporte ce qu'il a constaté."),
        ("une chronique", "Un texte où quelqu'un donne régulièrement son point de vue signé."),
        ("un éditorial", "Le texte qui exprime la position du journal lui-même."),
        ("un billet de blogue", "Un texte court publié en ligne, que les lecteurs peuvent commenter."),
        ("une manchette", "Le titre principal, mis bien en vue, qui annonce la nouvelle importante."),
        ("une source", "La personne ou le document d'où vient une information, et qui permet de la vérifier."),
    ], notes="Faire répéter avec l'article. « Une source » est le mot le plus important "
             "des six : il revient dans les quatre blocs.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Le local dont on parle est situé rue Boisjoli.", "vrai"),
        ("Ludovic Chagnon donne son opinion dans ses reportages.", "faux - il n'a pas le droit"),
        ("Thérèse Vaillancourt signe une chronique le samedi.", "vrai"),
        ("Suzie dit qu'une chronique ne contient jamais de faits.", "faux - elle en contient souvent"),
        ("On paie la consigne au moment de rapporter le contenant vide.", "faux - on la paie à l'achat"),
        ("Suzie propose à Farida d'écrire un billet.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le cinquième "
             "porte sur la consigne : y revenir en B2, avec les chiffres.")

    d.billet(
        "Nommez une nouvelle que vous avez entendue cette semaine.",
        exemples=[
            "Qui vous l'a apprise : la radio, un journal, quelqu'un ?",
            "Est-ce que vous sauriez dire d'où venait l'information ?",
        ],
        notes="Devoir concret. Les réponses servent de matière première en A4, quand "
              "on triera les faits et les opinions.")

    return d.save(dossier)
