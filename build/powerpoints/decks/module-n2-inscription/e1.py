# -*- coding: utf-8 -*-
"""E1 · Je me lance.
Bloc E « Je me lance » · couleur teal · 60 min. Dernière séance du module.
Source : dialogue `appli`, jeu de rôle `inscription`, productions orale et
écrite.

Séance de production. Rien de neuf n'y est introduit : tout ce que le module
a montré revient, et l'élève passe du côté de celui qui sait — c'est Yara qui
explique la case « scolarité » à quelqu'un d'autre.

Le programme ne demande aucune production orale pour cette situation : ses
deux intentions sont écrites. La prise orale est donc là pour la démarche
elle-même, qui se fait debout et de vive voix, et l'écrit reste ce qu'un
débutant écrit vraiment — un message de trois à cinq phrases.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-inscription/images/')


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="Je me lance",
        chapeau="S'inscrire au comptoir de vive voix, puis écrire pour "
                "demander une place.",
        duree='60 minutes')

    d.titre(notes="Dernière séance. Prévoir que la moitié du temps se passe en production "
                  "réelle : jeu de rôle, enregistrement, écriture. Les diapositives ne "
                  "sont qu'un cadre.")

    d.objectifs([
        "dire pourquoi on vient, en une phrase ;",
        "épeler son nom lentement ;",
        "donner ses renseignements case par case ;",
        "écrire de trois à cinq phrases pour demander une place.",
    ])

    d.declencheur(
        'Observation', "Une personne s'inscrit pour la première fois. Qu'est-ce qui l'arrête ?",
        image=IMG + 'comptoir-secretariat.jpg',
        pistes=[
            "Qu'est-ce que vous n'avez pas compris, votre première fois ?",
            "Quelle case vous a arrêté ?",
            "Qui vous a aidé ?",
            "Qu'est-ce que vous diriez à quelqu'un qui arrive demain ?",
        ],
        notes="La quatrième piste ouvre la séance : noter au tableau ce que le groupe "
              "dit — c'est le plan de la production orale, et il vient d'eux.")

    d.dialogue('Dialogue', "Cette fois, c'est Yara qui explique", [
        ("HAMID", "Yara, je ne comprends pas cette case.", True),
        ("YARA", "Laquelle ? Montre-moi.", True),
        ("HAMID", "Ici. « Scolarité ».", True),
        ("YARA", "C'est le nombre d'années d'école. Toi, tu as fait combien d'années ?", True),
        ("HAMID", "Neuf ans.", True),
        ("YARA", "Alors tu écris neuf. Dans la case.", True),
    ], consigne="Écoutez, puis dites comment Yara explique le mot.",
       notes="Elle ne définit pas : elle pose une question. C'est la meilleure façon "
             "d'expliquer un mot à un débutant, et elle est à portée du groupe.")

    d.tableau('Analyse', "Ce qui revient de tout le module",
              ["Ce qu'on dit", "Vu en"],
              [["Je voudrais m'inscrire.", "A1 - la phrase qui ouvre la porte"],
               ["H, A, deux D, A, D.", "A2 - épeler son nom"],
               ["Du 7 septembre au 11 décembre.", "B2 - lire et noter une date"],
               ["Mon nom, c'est Haddad.", "C2 - mon, ma, mes"]],
              cle=1,
              note="Rien de neuf dans cette colonne : le module entier tient en quatre lignes.",
              notes="Diapositive à photographier. Elle sert de révision de tout le "
                    "module en une seule page.")

    d.regle("Répondre, c'est dire une chose à la fois",
            "Trois mots par case, et le formulaire se remplit.",
            precision="« Haddad. » « Yara. » « Le 7 mars 1994. » « 3420, rue "
                      "Papineau. » Quatre réponses, quatre cases, et personne n'a "
                      "besoin d'une phrase complète. Ce qui compte, c'est de "
                      "s'arrêter et d'attendre la question suivante.",
            notes="Diapositive à photographier. Rappeler le vouvoiement : c'est ce que "
                  "la correction en ligne regarde en premier.")

    d.cartes("Trois situations pour le jeu de rôle", "Choisissez la vôtre", [
        ("Je téléphone au sujet de l'annonce",
         "L'annonce ne dit ni la date, ni l'heure, ni le local. Vous appelez."),
        ("Je remplis mon formulaire",
         "Vous êtes au comptoir, avec une feuille vide et un stylo."),
        ("Comment ça s'écrit ?",
         "La secrétaire ne sait pas écrire votre nom. Vous l'épelez."),
    ], cols=3, notes="Ce sont les trois situations du jeu de rôle en ligne. L'élève y joue "
                     "avec l'assistant, qui tient madame Bourgeois : une case à la fois, "
                     "et elle répète sans s'impatienter quand on le lui demande.")

    d.pratique('Production orale', "Inscrivez-vous au comptoir du secrétariat",
               "Trois temps. Enregistrez-vous, écoutez-vous, recommencez.", [
        ("TEMPS 1", "Bonjour. Je voudrais m'inscrire au cours de français."),
        ("TEMPS 2", "Mon nom de famille, c'est… H, A, deux D, A, D."),
        ("TEMPS 3", "Ma date de naissance, c'est le… Mon adresse, c'est…"),
    ], cols=1,
       notes="Vingt minutes. Le vouvoiement doit tenir du début à la fin. Laisser "
             "recommencer autant de fois qu'il le faut : c'est le but du panneau "
             "d'enregistrement.")

    d.pratique('Production écrite', "Écrivez au secrétariat pour demander une place",
               "De trois à cinq phrases, pour une personne que vous ne connaissez pas.", [
        ("À écrire", "« Bonjour madame », au début."),
        ("À écrire", "Ce que vous voulez : je voudrais m'inscrire au cours de français."),
        ("À écrire", "Votre nom de famille et votre prénom."),
        ("À écrire", "Votre date de naissance, écrite année, mois, jour."),
        ("À écrire", "Votre numéro de téléphone, et « merci » à la fin."),
    ], cols=1,
       notes="Vingt minutes. Le cadre reprend le billet de sortie de C2 : ceux qui "
             "l'ont fait n'ont qu'à le recopier et l'améliorer.")

    d.billet(
        "Cette semaine, demandez au secrétariat de votre centre un renseignement, en français.",
        exemples=[
            "Bonjour. Le cours finit quand ?",
            "C'est quoi, cette case ?",
            "C'est bien écrit ?",
        ],
        notes="Dernier devoir du module. Demander au cours suivant qui l'a fait et ce "
              "qu'on lui a répondu : c'est la seule évaluation qui compte vraiment pour "
              "cette situation du programme.")

    return d.save(dossier)
