# -*- coding: utf-8 -*-
"""A1 · Un timbre, s'il vous plaît.
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercices `prVocab`, `pr1`.

Dixième module court du projet, neuvième du niveau 2. L'élève tient une
phrase à la fois : les diapositives portent peu de mots, et chaque phrase
projetée est une phrase qu'il pourra dire lui-même en sortant.

Le module entier se joue sur du papier — une enveloppe, un formulaire — mais
il commence par un comptoir, parce qu'il faut d'abord savoir nommer ce qu'on
envoie avant de savoir l'écrire.
"""
import os

from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-colis/images/')


def _photo(nom):
    """La photo si elle est sur le disque, sinon rien.

    Les vingt images du module sortent de
    `build/contenu/module-n2-colis/gen_images.py`, qui coûte de l'argent réel
    et n'a pas encore été lancé. Sans ce garde-fou, les huit séances ne se
    construiraient pas du tout ; avec lui, elles se construisent tout de
    suite et reprennent la photo d'elles-mêmes dès qu'elle existe.
    """
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Un timbre, s'il vous plaît",
        chapeau="Nommer ce qu'on envoie — une lettre, une enveloppe, un "
                "timbre, un colis — et dire ce qu'on veut en une phrase.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Apporter de vraies enveloppes, un timbre "
                  "déjà collé si possible, et une petite boîte. Les objets passent de "
                  "main en main pendant que le mot se dit : c'est ainsi qu'il reste.")

    d.objectifs([
        "nommer les quatre objets de la poste ;",
        "reconnaître un comptoir postal ;",
        "dire ce qu'on veut en une phrase courte ;",
        "demander le prix avec « Combien ça coûte ? ».",
    ])

    d.declencheur(
        'Observation', "Où est la poste, près de chez vous ?",
        image=_photo('poste-comptoir.jpg'),
        pistes=[
            "Avez-vous déjà envoyé une lettre au Québec ?",
            "Où avez-vous acheté le timbre ?",
            "Savez-vous qu'il y a un comptoir postal dans beaucoup de pharmacies ?",
            "Qu'est-ce qu'on peut y faire ?",
        ],
        notes="Beaucoup d'élèves cherchent un bureau de poste et n'en trouvent pas dans "
              "leur quartier. Dire tout de suite que le comptoir de la pharmacie fait la "
              "même chose, et qu'il est ouvert plus tard.")

    d.dialogue('Dialogue · 1 de 2', "Amara entre au comptoir", [
        ("AMARA", "Bonjour. Je veux envoyer cette lettre.", True),
        ("LUC", "Bonjour. C'est pour où ?", True),
        ("AMARA", "Pour Sherbrooke.", True),
        ("LUC", "D'accord. Il faut un timbre.", True),
        ("AMARA", "Combien ça coûte ?", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Faire écouter deux fois, diapositive masquée. Puis afficher et faire répéter "
             "réplique par réplique, en chœur. Amara Diallo est arrivée de Guinée il y a "
             "huit mois ; Luc Tremblay tient le comptoir.")

    d.dialogue('Dialogue · 2 de 2', "Le prix, et où coller le timbre", [
        ("LUC", "Un dollar quarante-quatre.", True),
        ("AMARA", "Un dollar quarante-quatre ?", True),
        ("LUC", "Oui. Voici votre timbre.", True),
        ("AMARA", "Merci. Je le mets où ?", True),
        ("LUC", "En haut, à droite.", True),
    ], notes="Faire remarquer la septième réplique : Amara redit le montant. Ce n'est pas "
             "une hésitation, c'est une vérification, et c'est la chose la plus utile du "
             "module. La faire répéter par tout le groupe.")

    d.tableau('Analyse', "Quatre objets, quatre mots",
              ['Ce que c\'est', 'Comment on le dit'],
              [["Le papier qu'on écrit et qu'on plie", "une lettre"],
               ["Le papier fermé qui la contient", "une enveloppe"],
               ["Le petit papier collé en haut, à droite", "un timbre"],
               ["La boîte, trop grosse pour une enveloppe", "un colis"]],
              cle=2,
              note="Le timbre, c'est le prix de l'envoi. On le paie une fois, au comptoir.",
              notes="Diapositive à photographier. Faire montrer chaque objet réel pendant "
                    "qu'on dit son nom, avec l'article : « une enveloppe », jamais "
                    "« enveloppe » tout seul.")

    d.vocabulaire('Vocabulaire', "Les mots du comptoir", [
        ("un comptoir postal", "L'endroit où on paie et où on envoie, souvent dans une "
                               "pharmacie."),
        ("une boîte aux lettres", "La grosse boîte rouge de la rue, où on met les lettres."),
        ("un colis", "La boîte qu'on envoie quand c'est trop gros pour une enveloppe."),
        ("un timbre", "Le petit papier collé sur l'enveloppe : c'est le prix de l'envoi."),
    ], notes="Diapositive à photographier. Ces quatre mots reviennent dans les sept autres "
             "séances : les faire répéter jusqu'à ce qu'ils sortent sans effort.")

    d.regle("Dire ce qu'on veut, en une phrase",
            "Un timbre, s'il vous plaît.",
            precision="Trois mots suffisent au comptoir. On peut aussi dire "
                      "« Je veux envoyer cette lettre. » ou « Je veux envoyer ce colis. » "
                      "Puis on demande le prix : <b>Combien ça coûte ?</b>",
            notes="Diapositive à photographier. Insister : une phrase courte est polie si "
                  "elle finit par « s'il vous plaît ». Beaucoup d'élèves se taisent parce "
                  "qu'ils cherchent une phrase longue.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Amara veut envoyer une lettre.", "vrai"),
        ("La lettre est pour Sherbrooke.", "vrai"),
        ("Le timbre coûte deux dollars.", "faux — un dollar quarante-quatre"),
        ("Amara répète le prix pour vérifier.", "vrai"),
        ("Le timbre se colle en bas, à gauche.", "faux — en haut, à droite"),
    ], corrige=True, cols=1,
       notes="Les faire d'abord à l'oral, en groupe, avant de les faire écrire. Les cinq "
             "mêmes énoncés sont dans le module en ligne, exercice `pr1`.")

    d.pratique('Pratique · à deux', "Au comptoir, chacun son tour",
               "Deux par deux. L'un tient le comptoir, l'autre entre.", [
        ("Étape 1", "Saluez, puis dites ce que vous voulez envoyer."),
        ("Étape 2", "Demandez le prix : « Combien ça coûte ? »"),
        ("Étape 3", "Redites le montant que vous avez entendu."),
        ("Étape 4", "Remerciez, puis changez de rôle."),
    ], cols=1,
       notes="Vingt minutes. Donner à celui qui tient le comptoir un prix écrit sur un "
             "papier, différent à chaque paire : sans cela, tout le monde dit « un dollar "
             "quarante-quatre » et personne n'écoute vraiment.")

    d.billet(
        "Écrivez trois phrases que vous pourriez dire au comptoir postal.",
        exemples=[
            "Un timbre, s'il vous plaît.",
            "Je veux envoyer ce colis.",
            "Combien ça coûte ?",
        ],
        notes="Devoir court. Demander de les dire à voix haute trois fois à la maison : "
              "ce sont les phrases de la dernière séance.")

    return d.save(dossier)
