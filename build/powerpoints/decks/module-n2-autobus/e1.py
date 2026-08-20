# -*- coding: utf-8 -*-
"""E1 · Je me lance.
Bloc E « Je me lance » · couleur teal · 60 min. Dernière séance du module.
Source : dialogue `appli`, jeu de rôle `autobus`, productions orale et écrite.

Séance de production. Tout ce que le module a montré revient ici, et rien de
neuf n'y est introduit — sauf un mot, « correspondance », que le dialogue
apporte parce qu'il ne s'apprend nulle part ailleurs.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-autobus/images/')


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="Je me lance",
        chapeau="Demander son chemin à voix haute, puis écrire le trajet "
                "qu'on fait chaque semaine.",
        duree='60 minutes')

    d.titre(notes="Dernière séance. Prévoir que la moitié du temps se passe en production "
                  "réelle : jeu de rôle, enregistrement, écriture. Les diapositives ne "
                  "sont qu'un cadre.")

    d.objectifs([
        "demander son chemin dans une vraie conversation ;",
        "demander l'heure d'un autobus et une correspondance ;",
        "s'enregistrer et s'écouter ;",
        "écrire son trajet de la semaine.",
    ])

    d.dialogue('Dialogue', "Une correspondance", [
        ("HASSAN", "Excusez-moi. Je vais à l'hôpital. C'est le bon autobus ?", True),
        ("CLAUDE", "Non, celui-ci va vers l'est. Vous devez prendre le 32.", True),
        ("HASSAN", "Le 32. Où est l'arrêt ?", True),
        ("CLAUDE", "De l'autre côté de la rue, devant la pharmacie.", True),
        ("HASSAN", "Et ça prend combien de temps ?", True),
        ("CLAUDE", "Une vingtaine de minutes. Gardez votre correspondance.", True),
    ], consigne="Écoutez, puis comptez ce que Hassan a appris.",
       notes="Quatre choses en six répliques : le bon numéro, l'endroit de l'arrêt, la "
             "durée, la correspondance. Faire compter par le groupe.")

    d.tableau('Analyse', "Ce qui revient de tout le module",
              ['Ce qu\'on dit', 'Vu en'],
              [["Je vais à l'hôpital.", "A1 — à la, au, à l'"],
               ["De l'autre côté, devant la pharmacie.", "B1 — les mots de la direction"],
               ["Le 32. Où est l'arrêt ?", "B2 — répéter pour vérifier"],
               ["Ça prend combien de temps ?", "C1 — l'heure et la durée"]],
              cle=2,
              note="Rien de neuf dans cette colonne, sauf un mot : la correspondance.",
              notes="Diapositive à photographier. Elle sert de révision de tout le module "
                    "en une seule page.")

    d.regle("La correspondance",
            "Le petit papier qui rend le deuxième autobus gratuit.",
            precision="On la garde à la main jusqu'au second autobus. Si on ne connaît "
                      "pas le mot, on peut demander : « <b>C'est quoi, une "
                      "correspondance ?</b> »",
            notes="Insister sur la question elle-même : demander le sens d'un mot est une "
                  "compétence, pas un aveu.")

    d.cartes("Trois situations pour le jeu de rôle", "Choisissez la vôtre", [
        ("Dans la rue",
         "Vous cherchez la bibliothèque. Vous arrêtez quelqu'un sur le trottoir."),
        ("À l'arrêt",
         "Vous attendez le 51. Vous ne savez pas si c'est le bon arrêt, ni à quelle "
         "heure il passe."),
        ("Dans l'autobus",
         "Vous allez à l'hôpital. Vous n'êtes pas sûr d'avoir pris le bon autobus."),
    ], cols=3, notes="Ce sont les trois situations du jeu de rôle en ligne. L'élève y joue "
                     "avec l'assistant, qui parle lentement et pose une question à la "
                     "fois.")

    d.pratique('Production orale', "Demandez votre chemin",
               "Trois temps. Enregistrez-vous, écoutez-vous, recommencez.", [
        ("TEMPS 1", "Excusez-moi, madame. Je cherche la bibliothèque."),
        ("TEMPS 2", "C'est loin d'ici ? Plus lentement, s'il vous plaît."),
        ("TEMPS 3", "Tout droit, à droite au feu. C'est ça ? Merci beaucoup."),
    ], cols=1,
       notes="Vingt minutes. Laisser recommencer autant de fois qu'il le faut : c'est "
             "l'écoute de soi qui fait progresser, pas la première prise.")

    d.pratique('Production écrite', "Écrivez votre trajet",
               "De quatre à six phrases sur le trajet que vous faites chaque semaine.", [
        ("À dire", "Le lieu où vous allez."),
        ("À dire", "Le numéro de l'autobus, ou « à pied »."),
        ("À dire", "Où se trouve l'arrêt."),
        ("À dire", "L'heure, ou le temps que ça prend."),
    ], cols=1,
       notes="Vingt minutes. Rappeler d'employer « je vais à la / au / à l' » et les mots "
             "de la direction : c'est ce qui sera regardé.")

    d.billet(
        "Faites votre trajet en le disant tout haut, dans votre tête.",
        exemples=[
            "Le lundi, je vais à l'école.",
            "Je prends le 51 à l'arrêt devant la pharmacie.",
            "Ça prend vingt minutes.",
        ],
        notes="Dernier devoir du module. Beaucoup diront que c'est la première fois qu'ils "
              "pensent leur trajet en français.")

    return d.save(dossier)
