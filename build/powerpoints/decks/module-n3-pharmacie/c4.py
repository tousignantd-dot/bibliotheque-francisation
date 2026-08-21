# -*- coding: utf-8 -*-
"""C4 · Les étapes du renouvellement.
Bloc C « Défi 2 · Renouveler l'ordonnance » · couleur framboise · 75 min.
Source : exercices `t2etapes` et `t2phrases`.

Séance de bilan du défi 2 : l'ordre des gestes, puis les phrases qu'on entend
au comptoir et qu'il faut comprendre du premier coup.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-pharmacie/images/')


def build(dossier):
    d = Deck(
        code='C4', section='framboise',
        titre='Les étapes du renouvellement',
        chapeau="Six gestes, toujours dans le même ordre, et six phrases "
                "qu'on entend chaque fois. Les connaître d'avance, c'est "
                "n'avoir qu'à répondre.",
        duree='75 minutes')

    d.titre(notes="Séance de bilan du défi 2. Elle réunit l'ordre des gestes et le "
                  "vocabulaire du comptoir. Prévoir de laisser le tableau des étapes "
                  "affiché jusqu'à la fin du module.")

    d.objectifs([
        "remettre les six étapes du renouvellement dans l'ordre ;",
        "comprendre six phrases fréquentes du comptoir ;",
        "reconnaître le mot « échue » sur une ordonnance ;",
        "mener un renouvellement du début à la fin, en paires.",
    ])

    d.declencheur(
        'Observation', "Que se passe-t-il pendant les vingt minutes d'attente ?",
        image=IMG + 'salle-attente.jpg',
        pistes=[
            "Qu'est-ce que le pharmacien fait pendant ce temps-là ?",
            "Qu'est-ce qui est écrit sur l'étiquette qu'il prépare ?",
            "Comment saurez-vous que c'est prêt ?",
        ],
        notes="Répondre à la dernière question tout de suite : on appelle votre nom, à "
              "voix haute. C'est pourquoi il faut l'avoir bien épelé au départ.")

    d.tableau('Analyse', "Les six étapes, dans l'ordre",
              ["Dans l'ordre", "Ce qui se passe"],
              [["1. Au comptoir", "votre nom, et pourquoi vous venez"],
               ["2. Votre carte", "on vérifie qui vous êtes"],
               ["3. Votre dossier", "il voit vos médicaments"],
               ["4. L'ordonnance finie", "il peut la prolonger"],
               ["5. Vingt minutes", "on prépare le flacon"],
               ["6. À la caisse", "vous payez votre part"]],
              cle=0,
              notes="Diapositive à photographier. Faire nommer chaque étape par un élève "
                    "différent, puis faire redire la suite complète sans regarder.")

    d.cartes("Les phrases du comptoir", "Quatre à comprendre du premier coup", [
        ("« Il vous reste un renouvellement. »",
         "Vous pouvez avoir ce médicament encore une fois, sans nouveau papier du "
         "médecin. Le nombre de renouvellements est écrit sur l'étiquette."),
        ("« Votre ordonnance est échue. »",
         "Le papier n'est plus bon : la date est passée. C'est exactement le cas où le "
         "pharmacien peut la prolonger en attendant votre rendez-vous."),
        ("« C'est couvert par votre assurance. »",
         "Vous ne payez pas tout le prix vous-même. Il reste presque toujours une "
         "partie à votre charge : c'est normal, ce n'est pas une erreur."),
        ("« Avez-vous des allergies ? »",
         "On demande si un médicament vous a déjà rendu malade. Répondez même si vous "
         "n'êtes pas certain : le pharmacien vérifiera."),
    ], notes="Faire répéter chaque phrase, puis la faire reformuler en mots simples par "
             "un élève. La reformulation est la vraie preuve de compréhension.")

    d.pratique('Association', "La phrase et ce qu'elle veut dire",
               "Dites ce que chaque phrase signifie.", [
        ("« Il vous reste un renouvellement. »", "je peux l'avoir encore une fois"),
        ("« Votre ordonnance est échue. »", "la date est passée"),
        ("« Je peux la prolonger en attendant. »", "le pharmacien me dépanne"),
        ("« On vous appelle quand c'est prêt. »", "je m'assois et j'attends mon nom"),
        ("« Avez-vous des allergies ? »", "un médicament vous a-t-il déjà rendu malade ?"),
    ], corrige=True,
       notes="Reprend l'exercice interactif `t2phrases`. Insister sur « échue » : le mot "
             "est rare mais il est écrit sur les étiquettes.")

    d.pratique('Production', "Le renouvellement complet",
               "En paires : menez l'échange du début à la fin.", [
        ("1. Saluez et dites ce qui vous amène.", "« Bonjour. Il me reste deux comprimés et mon ordonnance est finie. »"),
        ("2. Donnez votre nom, épelé, et votre carte.", "« Nadia Belhadj. B, E, L, H, A, D, J. Voici ma carte. »"),
        ("3. Demandez si c'est possible sans le médecin.", "« Est-ce que vous pouvez la prolonger en attendant ? »"),
        ("4. Demandez le délai et le prix.", "« Est-ce que ça prend beaucoup de temps ? Combien est-ce que je vais payer ? »"),
    ], corrige=False,
       notes="C'est la répétition générale du jeu de rôle de la séance E1. Circuler et "
             "noter ce qui manque le plus souvent : presque toujours l'étape 4.")

    d.billet(
        "Écrivez les six étapes du renouvellement, dans l'ordre, avec vos mots.",
        exemples=[
            "Une ligne par étape.",
            "Ajoutez la phrase que vous diriez à chacune.",
        ],
        notes="Devoir de fin de bloc. Ramasser : la liste sert de mémo à garder dans le "
              "portefeuille, à côté de la carte d'assurance maladie.")

    return d.save(dossier)
