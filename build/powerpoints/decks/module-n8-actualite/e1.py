# -*- coding: utf-8 -*-
"""E1 · L'appel à la tribune et la production orale
Bloc E « Je me lance » · couleur teal · 75 min.
Source : bloc `custom` du module - jeu de rôle `tribune` (trois cas de
`ROLE_CAS`) et production orale en trois temps.
Intention du programme : commenter l'actualité en justifiant son point de
vue, la seule intention de production orale de la situation au niveau 8.
Dossier inventé : Rivière-aux-Cèdres, le boisé Sainte-Perpétue, la radio CIRC.
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n8-actualite' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="C'est à vous : la ligne est ouverte",
        chapeau="Deux minutes d'antenne, comme tout le monde. Le jeu de rôle "
                "sert de répétition, l'enregistrement de preuve - et une "
                "intervention se juge à sa première et à sa dernière phrase.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Ouvrir en faisant relire à voix haute les "
                  "trois phrases préparées en devoir de D2. Chacun les dit une fois, "
                  "debout, avant qu'on ouvre le module.")

    d.objectifs([
        "tenir un appel à la tribune avec l'assistant, du début à la fin ;",
        "annoncer sa position en une phrase, puis résumer le fait sans le déformer ;",
        "concéder un point, puis avancer un argument chiffré et un argument vécu ;",
        "refuser une rumeur qu'on vous tend, et terminer par une demande précise.",
    ], notes="Séance de production, pas d'enseignement. Le temps de parole de "
             "l'enseignante doit rester sous dix minutes : tout le reste est aux "
             "élèves.")

    d.declencheur(
        'Préparation', "Quatre choses à avoir devant soi avant d'appeler",
        image=IMG + 'salle-communautaire.jpg',
        pistes=[
            "Votre position, écrite en une seule phrase.",
            "Votre argument chiffré, et d'où vient le chiffre.",
            "Votre argument vécu : qui, quand, quoi.",
            "Votre demande, adressée à quelqu'un qui peut agir.",
        ],
        notes="Cinq minutes en silence, au crayon. Personne ne commence l'appel sans "
              "avoir les quatre écrites devant soi - c'est ce qui distingue une "
              "intervention d'une plainte.")

    d.tableau('Jeu de rôle', "Trois sujets, une même tribune",
              ['Le sujet', 'Ce qui s\'y joue'],
              [["Le boisé Sainte-Perpétue",
                "onze hectares pour un dollar, un vote à vingt-deux heures cinquante"],
               ["Le terrain derrière l'aréna",
                "un délai de vingt et un mois que personne n'a mis par écrit"],
               ["Quatre-vingt-dix, ou trois cent quarante-deux",
                "deux comptages d'arbres, et le désaccord sur ce qu'on appelle un arbre"]],
              cle=0,
              note="L'assistant joue l'animateur. Il demande vos sources, il vous oppose le camp adverse, et il vous tend une rumeur.",
              notes="Diapositive à photographier. Prévenir le groupe : la rumeur "
                    "arrivera, une fois au moins, et c'est voulu. C'est là que sert "
                    "la phrase apprise en D1.")

    d.cartes('Jeu de rôle', "Ce qu'on rate le plus souvent", [
        ("Commencer par le contexte",
         "Une intervention qui explique avant de se situer perd son temps "
         "d'antenne. Dites d'abord de quel côté vous êtes, puis expliquez."),
        ("Concéder puis se taire",
         "La concession sans la suite est une reddition. La seconde phrase "
         "est obligatoire : c'est vrai, et voici pourquoi cela ne règle pas "
         "la question."),
        ("Répondre à la rumeur",
         "Même pour la nuancer, y répondre la fait exister. « Je n'en sais "
         "rien, et ce n'est pas mon argument. » Rien d'autre."),
        ("Finir sur l'indignation",
         "« C'est scandaleux » ne se répond pas. Terminez par ce que vous "
         "voulez qu'il arrive, avec une date."),
    ], notes="Les huit sujets à couvrir sont dans le module. Ces quatre-là sont ceux "
             "qu'on manque, et il vaut mieux les nommer avant de commencer qu'après.")

    d.regle("Réutilisez ce que vous venez d'apprendre",
            "Certes le besoin de logements est réel, mais une décision prise "
            "devant onze personnes ne tiendra pas. Si la Ville avait publié "
            "l'évaluation, je n'aurais pas eu besoin d'appeler. Ce que je "
            "demande, c'est la publication avant mardi.",
            precision="Une concession, une hypothèse irréelle, une mise en relief : "
                      "les trois points de langue du bloc, chacun dans une phrase. "
                      "Et pour renverser avec un fait : on nous dit que tout a été "
                      "étudié ; or, le terrain de l'aréna ne l'a jamais été.",
            notes="Diapositive à photographier, et à garder affichée pendant tout le "
                  "jeu de rôle. Un élève qui emploie les trois une fois chacune se "
                  "distingue sans avoir à hausser le ton.")

    d.tableau('Production orale', "Deux minutes, en trois temps",
              ['Temps', 'Ce qu\'on dit'],
              [["1. Position, puis le fait",
                "Je suis pour le projet, et je vais quand même signer. Le conseil a cédé onze hectares lundi soir, par quatre voix contre trois."],
               ["2. Deux arguments, puis une concession",
                "Trois de mes collègues ont quitté la ville faute de logement. Mais un vote pris devant onze personnes ne tiendra pas dix ans. Certes un report mettrait le financement en péril."],
               ["3. L'irréel, puis la demande",
                "Si la Ville avait publié l'évaluation, je n'aurais pas eu besoin d'appeler. Ce que je demande, c'est qu'elle la publie avant mardi."]],
              cle=0,
              notes="Diapositive à photographier. Deux minutes environ, debout, sans "
                    "lire ses notes mot à mot. Le sujet peut être le boisé ou une "
                    "actualité qui touche l'élève, à condition qu'il en ait les faits.")

    d.pratique('Production orale', "Ce qu'on écoute chez l'autre",
               "Pendant que quelqu'un parle, cochez ce que vous entendez.", [
        ("Une position annoncée en une phrase", "avant toute explication"),
        ("Un résumé du fait en deux phrases", "sans déformation"),
        ("Un chiffre et sa provenance", "et non « on dit que »"),
        ("Une concession suivie d'une avancée", "certes..., mais..."),
        ("Une hypothèse irréelle", "si... avait..., ... aurait..."),
        ("Une demande précise, avec une date", "la dernière phrase"),
    ], corrige=False,
       notes="Grille d'écoute mutuelle, et elle vaut mieux qu'une correction de "
             "l'enseignante : entendre ce qui manque chez l'autre fait entendre ce "
             "qui manque chez soi.")

    d.piege('Piège', "élever la voix quand on vous coupe",
            "ralentir",
            "Celui qui monte le ton perd, à la radio comme en assemblée. "
            "Ralentir oblige l'autre à ralentir aussi, et cela s'entend comme "
            "de l'assurance. Même chose devant trois objections lancées "
            "ensemble : n'en prenez qu'une, la plus forte, et dites-le - je "
            "réponds sur le calendrier, qui est le vrai point.",
            notes="Le faire essayer une fois : l'enseignante coupe la parole à un "
                  "volontaire, qui doit répondre plus lentement qu'avant. L'effet "
                  "surprend tout le monde, y compris celui qui parle.")

    d.billet(
        "Enregistrez votre intervention de deux minutes et déposez-la.",
        exemples=[
            "Réécoutez-vous : entend-on votre position dans les dix premières secondes ?",
            "Entend-on une demande dans les dix dernières ? Sinon, refaites-le.",
        ],
        notes="Le dépôt se fait dans « Je me lance ». Rappeler que la rétroaction de "
              "l'IA reste privée : seul ce que l'élève envoie parvient à "
              "l'enseignante.")

    return d.save(dossier)
