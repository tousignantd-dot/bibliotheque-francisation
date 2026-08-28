# -*- coding: utf-8 -*-
"""A1 · Ton horaire est affiché en haut.
Bloc A « Je découvre » · couleur acier · 75 min.
Source : dialogue `prep`, exercices `prVocab` et `pr1`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-horaire/images/')


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Ton horaire est affiché en haut",
        chapeau="Tout ce qu'un employé doit savoir tient sur un tableau "
                "blanc, dans la salle du personnel. Encore faut-il savoir "
                "le lire — et oser demander quand on ne comprend pas.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Fabiola travaille depuis deux semaines : "
                  "elle n'est plus la nouvelle, mais elle n'a encore rien osé demander. "
                  "C'est exactement la situation de beaucoup d'élèves du groupe.")

    d.objectifs([
        "nommer les lieux et les objets d'un lieu de travail ;",
        "comprendre ce qu'on lit sur un tableau d'horaire ;",
        "dire ce qu'on fait en arrivant : poinçonner, se changer ;",
        "reconnaître qui est le chef d'équipe et à quoi il sert.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qu'on regarde en arrivant au travail ?",
        image=IMG + 'tableau-horaire.jpg',
        pistes=[
            "Où sont écrites vos heures, à votre travail ?",
            "Qu'est-ce que vous faites en arrivant, avant de commencer ?",
            "À qui posez-vous vos questions ?",
            "Qu'est-ce qui arrive quand on a mal lu son horaire ?",
        ],
        notes="La quatrième question ramène des histoires vraies dans presque tous les "
              "groupes : une journée manquée, un quart oublié. Les laisser sortir, elles "
              "justifient tout le défi 1.")

    d.dialogue('Dialogue · 1 de 3', "Vous avez vu le tableau ?", [
        ("GAÉTAN", "Bonjour Fabiola ! Deux semaines déjà. Ça va, la cafétéria ?", False),
        ("FABIOLA", "Bonjour monsieur Roy. Ça va bien, merci. J'apprends.", True),
        ("GAÉTAN", "Vous avez vu le tableau, dans la salle du personnel ?", True),
        ("FABIOLA", "Le grand tableau blanc, à côté des casiers ?", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Relever le vouvoiement du chef d'équipe : il vouvoie Fabiola, elle le "
             "vouvoie aussi et l'appelle « monsieur Roy ». C'est l'usage au travail, et "
             "il vaut la peine d'être nommé dès la première minute.")

    d.dialogue('Dialogue · 2 de 3', "Une ligne par personne", [
        ("GAÉTAN", "Oui. Votre horaire de la semaine est affiché en haut.", True),
        ("FABIOLA", "Je l'ai regardé ce matin. Il y a beaucoup de chiffres.", True),
        ("GAÉTAN", "Une ligne par personne. Votre nom, puis vos cinq journées.", True),
        ("GAÉTAN", "En dessous. Les tâches de la journée, dans l'ordre.", True),
    ], notes="« Il y a beaucoup de chiffres » est la phrase la plus honnête du dialogue. "
             "Fabiola ne dit pas qu'elle ne comprend pas — elle le laisse entendre. Le "
             "défi 1 va lui apprendre à le demander franchement.")

    d.dialogue('Dialogue · 3 de 3', "On poinçonne avant", [
        ("MIGUEL", "Fabiola ! Ton uniforme propre est dans ton casier.", True),
        ("FABIOLA", "Merci Miguel. Le vestiaire, c'est la porte grise ?", True),
        ("MIGUEL", "La porte grise, oui. Ton numéro de casier, c'est le douze.", True),
        ("GAÉTAN", "Vous poinçonnez avant d'entrer dans la cuisine, pas après.", True),
    ], notes="Changement de registre à relever : Miguel tutoie Fabiola, ils sont "
             "collègues. Le chef vouvoie. Deux personnes, deux façons de s'adresser à "
             "elle, dans la même minute.")

    d.tableau('Analyse', "Ce qu'il y a sur le tableau du personnel",
              ["Ce qu'on y lit", "Ce que ça veut dire"],
              [["une ligne par personne", "cherchez votre nom, pas la date"],
               ["cinq journées sur la ligne", "vos heures, jour par jour"],
               ["les tâches, en dessous", "dans l'ordre où on les fait"],
               ["une case vide", "congé — vous ne venez pas"]],
              cle=1,
              note="La dernière ligne se lit dans le vide : personne n'écrit "
                   "jamais le mot « congé » sur un horaire.",
              notes="Diapo à photographier. Faire chercher au groupe ce qui n'est jamais "
                    "écrit sur un horaire : le congé, et la raison d'une absence.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Fabiola travaille à la cafétéria depuis deux semaines.", "vrai"),
        ("L'horaire est affiché sur un tableau blanc, dans la salle du personnel.", "vrai"),
        ("Il y a une ligne par journée de la semaine.", "faux — une ligne par personne"),
        ("Les tâches sont écrites en dessous des heures.", "vrai"),
        ("Le casier de Fabiola porte le numéro douze.", "vrai"),
        ("On poinçonne après être entré dans la cuisine.", "faux — avant d'entrer"),
    ], corrige=True,
       notes="C'est l'exercice `pr1` du module interactif, mot pour mot. La dernière ligne "
             "compte : poinçonner après, c'est du temps travaillé qui n'est pas payé.")

    d.billet(
        "Décrivez en trois lignes votre premier matin à un travail.",
        exemples=[
            "Où vous vous changez, ce que vous faites en arrivant.",
            "Une chose que vous n'avez pas osé demander.",
        ],
        notes="Devoir court. La deuxième ligne est le vrai matériau du module : les "
              "ramasser et en lire deux ou trois à voix haute en A2, sans nommer "
              "personne.")

    return d.save(dossier)
