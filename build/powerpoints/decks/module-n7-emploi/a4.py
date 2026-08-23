# -*- coding: utf-8 -*-
"""A4 · Lire un ordre du jour
Bloc A « Je découvre » · couleur teal (écoute et réponds) · 75 min.
Source du module : exercice `prOrdre` (type texte), mini-leçon `prOrdre`.
"""
import pathlib

from theme import Deck

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n7-emploi' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='A4', section='teal',
        titre="Lire un ordre du jour",
        chapeau="Six lignes qui décident de votre semaine : qui doit être là, "
                "ce qui va se discuter, dans quel ordre, pendant combien de "
                "temps, et ce qu'il faut avoir lu avant d'arriver.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc A. C'est le premier texte suivi du module - "
                  "l'exercice `prOrdre` est de type texte, avec des passages cliquables. "
                  "Prévoir vingt minutes sur le module, en fin de séance.")

    d.objectifs([
        "retrouver dans un ordre du jour la date, la durée et le convocateur ;",
        "comprendre ce que « varia » veut dire, et quand on le demande ;",
        "repérer le document joint à lire avant la réunion ;",
        "demander une place à l'ordre du jour d'une prochaine réunion.",
    ], notes="Le quatrième objectif est un acte de parole réel, que plusieurs élèves "
             "n'ont jamais posé. Il revient à la fin de la séance.")

    d.declencheur(
        'Observation', "Qu'est-ce qui est affiché sur ce babillard ?",
        image=IMG + 'babillard.jpg',
        pistes=[
            "Y a-t-il un babillard là où vous travaillez ?",
            "Qui le regarde vraiment ?",
            "Qu'est-ce qu'on y trouve : des horaires, des avis, des offres ?",
            "Vous est-il déjà arrivé de manquer quelque chose d'important ?",
        ],
        notes="Amener l'idée qu'un document affiché n'est pas un document lu. C'est "
              "exactement ce qui arrive à Aïcha avec le programme de prévention, qu'elle "
              "découvre au bloc C.")

    d.tableau('Analyse', "Ce qu'un ordre du jour contient",
              ['L\'élément', 'Ce que ça vous demande'],
              [["Date et durée", "la durée dit le temps dont vous disposez"],
               ["La convocation", "la personne à qui signaler une absence"],
               ["Les convoqués", "si vous y êtes, on vous attend"],
               ["Les points numérotés", "le numéro nomme un sujet en deux mots"],
               ["Le varia", "les points demandés en début de réunion"]],
              cle=0,
              note="La durée d'un point est une contrainte, pas une estimation. Le document joint se lit AVANT.",
              notes="Diapositive à photographier. Six rangées et une note : c'est la "
                    "densité maximale lisible de loin. Le document joint est volontairement "
                    "renvoyé à la note, pour qu'il ressorte.")

    d.regle("Un point de varia se demande au début",
            "Le varia n'est pas une permission d'interrompre.",
            precision="C'est un espace prévu à la fin de la réunion, et il se réclame "
                      "au moment où l'on adopte l'ordre du jour, pas au milieu du "
                      "point 2. Un point demandé en cours de route sera renvoyé au "
                      "varia de toute façon - avec, en prime, l'impression que vous ne "
                      "connaissez pas la procédure.",
            notes="Diapositive à photographier. Beaucoup d'élèves siègent à un conseil "
                  "d'établissement ou à une assemblée de copropriétaires : le même mot "
                  "y a le même sens.")

    d.pratique('Compréhension', "L'ordre du jour du 8 septembre",
               "Répondez d'après le document projeté au module.", [
        ("Quand la réunion a-t-elle lieu, et pendant combien de temps ?", "le lundi 8 septembre, de 8 h à 9 h 15"),
        ("Qui convoque la réunion ?", "Renaud Cormier, chef de production"),
        ("Combien de temps dure la présentation du point 1 ?", "douze minutes, puis les questions"),
        ("De quoi Thérèse Lapointe va-t-elle parler ?", "du rappel de la procédure de cadenassage"),
        ("À quel moment demande-t-on à ajouter un point ?", "en début de réunion, jamais pendant"),
        ("Qu'est-ce qu'il faut avoir lu avant d'arriver ?", "le relevé des temps d'attente, deux pages"),
    ], corrige=True,
       notes="Ouvrir l'exercice `prOrdre` du module en parallèle : les élèves cliquent "
             "dans le texte pendant que le groupe répond à l'oral. C'est le premier "
             "exercice de type texte du module ; montrer une fois comment on arme une "
             "question avant de cliquer un passage.")

    d.cartes('Analyse', "Demander une place à l'ordre du jour", [
        ("1 · Demander la place d'abord", "« Est-ce qu'il reste de la place à l'ordre du jour d'une prochaine réunion ? » On demande la place avant de préparer le contenu."),
        ("2 · Dire combien de temps", "« J'aurais besoin d'une quinzaine de minutes. » Une demande sans durée ne s'accorde pas."),
        ("3 · Confirmer par écrit", "Avant la date limite indiquée. Une place obtenue de vive voix et jamais confirmée n'existe pas."),
        ("4 · Tenir sa durée", "Demander quinze minutes et en prendre vingt-cinq est la façon la plus sûre de ne plus jamais en obtenir."),
    ], notes="Faire jouer la demande à deux, debout, en trente secondes : un élève "
             "demande, l'autre répond. Tout le monde passe.")

    d.piege('Lecture',
            "arriver sans avoir lu le document joint",
            "le lire la veille, crayon en main",
            "Le document joint est la seule partie de la réunion que vous pouvez "
            "maîtriser d'avance. C'est aussi ce qui vous permet de poser une question "
            "précise plutôt qu'une question générale - et une question précise est ce "
            "qui fait qu'on vous écoute la fois suivante.",
            notes="Le dire sans culpabiliser : presque personne ne lit les documents "
                  "joints, y compris les francophones. C'est justement pour ça que "
                  "celui qui le fait se distingue.")

    d.billet(
        "Écrivez la phrase par laquelle vous demanderiez une place à l'ordre du jour.",
        exemples=[
            "À qui vous adressez-vous, et comment le nommez-vous ?",
            "Combien de temps demandez-vous ?",
            "Que dites-vous du sujet, en cinq mots ?",
        ],
        notes="Ramasser. Corriger surtout la durée demandée : ceux qui n'en donnent "
              "aucune sont ceux qui n'obtiendront rien.")

    return d.save(dossier)
