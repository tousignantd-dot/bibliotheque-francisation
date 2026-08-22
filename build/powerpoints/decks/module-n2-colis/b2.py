# -*- coding: utf-8 -*-
"""B2 · Le code postal, et qui écrit à qui.
Bloc B « Défi 1 · J'écris l'adresse » · couleur ambre · 75 min.
Source : dialogue `t1b`, exercices `t1abrev`, `t1code`, `t1b`,
mini-leçon `t1code`.

Les abréviations liées aux adresses sont nommées telles quelles dans le
lexique du programme pour cette situation. Elles ne s'apprennent pas comme
du vocabulaire : ce sont des mots qu'on ne dit jamais et qu'on écrit
toujours.

La seconde moitié de la séance sépare l'expéditeur du destinataire. C'est la
notion qui fait revenir une lettre plutôt que de la perdre.
"""
import os

from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-colis/images/')


def _photo(nom):
    """La photo si elle est sur le disque, sinon rien. Voir `a1.py`."""
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre="Le code postal, et qui écrit à qui",
        chapeau="Lire et écrire un code postal, reconnaître les "
                "abréviations de l'adresse, et savoir où va son propre nom.",
        duree='75 minutes')

    d.titre(notes="Apporter les enveloppes du devoir de B1. La séance les complète : on y "
                  "ajoute le code postal, les abréviations et le coin de l'expéditeur.")

    d.objectifs([
        "lire un code postal caractère par caractère ;",
        "reconnaître app., boul., av., ch., C.P. et QC ;",
        "distinguer l'expéditeur du destinataire ;",
        "placer chaque nom au bon endroit sur l'enveloppe.",
    ])

    d.declencheur(
        'Observation', "Où va cette lettre quand elle tombe ?",
        image=_photo('poste-boite.jpg'),
        pistes=[
            "Que se passe-t-il si l'adresse est incomplète ?",
            "Que se passe-t-il si la personne a déménagé ?",
            "Comment la lettre peut-elle revenir chez vous ?",
            "Avez-vous déjà reçu une lettre qui n'était pas pour vous ?",
        ],
        notes="La troisième question amène l'expéditeur sans qu'on ait à l'annoncer. "
              "Laisser le groupe trouver que son propre nom doit être quelque part.")

    d.tableau('Analyse', "Six caractères, toujours",
              ['Le code postal', 'Ce qu\'il faut savoir'],
              [["H1T 1C5", "trois caractères, un espace, trois caractères"],
               ["lettre, chiffre, lettre", "puis chiffre, lettre, chiffre"],
               ["On le dit un par un", "H, un, T… un, C, cinq"],
               ["La première lettre dit la région", "H, Montréal · J, l'Estrie · G, Québec"]],
              cle=2,
              note="Sans code postal, la lettre part quand même, mais elle arrive plus "
                   "tard. On l'écrit toujours.",
              notes="Diapositive à photographier. Faire dire à voix haute le code postal "
                    "de l'école, un caractère à la fois. On ne dit jamais « cent quinze » "
                    "pour 1C5.")

    d.cartes("Les abréviations de l'adresse", "On les écrit, on ne les dit pas", [
        ("app.", "appartement"),
        ("boul.", "boulevard"),
        ("av.", "avenue"),
        ("ch.", "chemin"),
        ("C.P.", "case postale"),
        ("QC", "Québec, la province"),
    ], cols=3, notes="Diapositive à photographier. Insister : à l'oral on dit le mot en "
                     "entier — « appartement six », jamais « app six ». L'abréviation ne "
                     "sert qu'à la main qui écrit, quand la place manque.")

    d.dialogue('Dialogue', "Et vous, vous êtes qui ?", [
        ("LUC", "Madame, il manque une chose.", True),
        ("AMARA", "Ah bon ? Quoi ?", True),
        ("LUC", "Votre nom et votre adresse.", True),
        ("AMARA", "Mon adresse ? Pourquoi ?", True),
        ("LUC", "Vous êtes l'expéditeur.", True),
        ("AMARA", "Et mon frère ?", True),
        ("LUC", "Lui, c'est le destinataire.", True),
    ], consigne="Écoutez, puis trouvez qui est qui.",
       notes="Faire écouter deux fois. Les deux mots sont longs et se ressemblent : les "
             "écrire au tableau l'un sous l'autre et souligner « envoie » et « reçoit ».")

    d.regle("Deux personnes sur une enveloppe",
            "En haut à gauche, celui qui envoie. Au milieu, celui qui reçoit.",
            precision="L'<b>expéditeur</b> écrit son nom en haut, à gauche, en petit. Le "
                      "<b>destinataire</b> va au milieu, en plus gros. Le timbre reste en "
                      "haut, à droite. Si la personne a déménagé, la lettre revient chez "
                      "l'expéditeur : c'est à cela que sert ce coin-là.",
            notes="Diapositive à photographier. Dessiner l'enveloppe au tableau avec les "
                  "trois zones. Les élèves reprennent le dessin sur leur cahier : c'est "
                  "la page qu'ils regarderont chez eux.")

    d.pratique('Écriture', "Le code postal",
               "Complétez avec un seul mot.", [
        ("Un code postal a ___ caractères.", "six"),
        ("Le premier caractère est une ___.", "lettre"),
        ("Le deuxième caractère est un ___.", "chiffre"),
        ("Le code postal s'écrit à la ___ de l'adresse.", "fin"),
        ("H1T 1C5 : cette adresse est à ___.", "Montréal"),
    ], corrige=True, cols=2,
       notes="Les cinq mêmes phrases sont dans le module en ligne, exercice `t1code`, avec "
             "sa mini-leçon.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Il manque le nom d'Amara sur l'enveloppe.", "vrai"),
        ("Amara est l'expéditeur.", "vrai"),
        ("Son frère est l'expéditeur, lui aussi.", "faux — il est le destinataire"),
        ("L'adresse de l'expéditeur va en haut, à gauche.", "vrai"),
        ("Le préposé dit d'écrire en gros.", "faux — en petit"),
    ], corrige=True, cols=1,
       notes="Les cinq mêmes énoncés sont dans le module en ligne, exercice `t1b`.")

    d.pratique('Pratique · à deux', "L'enveloppe complète",
               "Deux par deux, avec l'enveloppe du devoir de B1.", [
        ("Étape 1", "Écrivez votre nom et votre adresse en haut, à gauche, en petit."),
        ("Étape 2", "Écrivez au milieu le nom et l'adresse de votre voisin."),
        ("Étape 3", "Dessinez un carré en haut, à droite : c'est la place du timbre."),
        ("Étape 4", "Échangez les enveloppes et vérifiez les six caractères du code."),
    ], cols=1,
       notes="Vingt minutes. Ramasser les enveloppes à la fin et les redonner à la séance "
             "E1 : elles servent de preuve du chemin parcouru, et l'effet est réel.")

    d.billet(
        "Écrivez trois adresses avec leur abréviation.",
        exemples=[
            "4520, rue Bélanger, app. 3",
            "88, boul. Saint-Laurent",
            "12, av. du Parc, C.P. 240",
        ],
        notes="Devoir court. Demander d'en relever au moins une vraie, sur une enveloppe "
              "ou une facture reçue à la maison.")

    return d.save(dossier)
