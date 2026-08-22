# -*- coding: utf-8 -*-
"""C1 · Trois dates dans un avis
Bloc C « Défi 2 · Lire l'avis du centre » · couleur acier · 75 min.
Source du module : dialogue `t2`, exercice `t2a`.
"""
import os
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-ecole/images/')


def img(nom):
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Trois dates dans un avis",
        chapeau="Trois jours plus tard, un avis arrive. Une page, quatre "
                "paragraphes, trois dates — et une seule de ces dates est "
                "une échéance. Amelia apporte la feuille au bureau du "
                "conseiller, parce qu'elle n'est pas sûre de laquelle.",
        duree='75 minutes')

    d.titre(notes="Première séance du défi 2, et la seule du module consacrée à la "
                  "compréhension écrite. Ouvrir en demandant qui, dans le groupe, a déjà "
                  "reçu une lettre officielle en français sans la lire jusqu'au bout. "
                  "Toutes les mains montent, y compris celle de l'enseignante.")

    d.objectifs([
        "reconnaître la structure d'un avis officiel : objet, décision, action, condition ;",
        "distinguer une échéance d'un simple rappel parmi plusieurs dates ;",
        "comprendre le paragraphe qui commence par « en cas de » ;",
        "savoir ce qu'on fait d'un avis reçu : le signer, le rapporter, en garder copie.",
    ], notes="Le deuxième objectif est le cœur de la séance. Une échéance oblige, un "
             "rappel informe : chercher le verbe est la méthode, et elle marche sur "
             "n'importe quel document officiel.")

    d.declencheur(
        'Observation', "Une feuille officielle. Où regardez-vous en premier ?",
        image=img('babillard-avis.jpg'),
        pistes=[
            "Le titre, la date, votre nom, le paragraphe en gras : par quoi commencez-vous ?",
            "Qu'est-ce qui vous fait abandonner avant la fin ?",
            "Qu'est-ce qui est écrit en gras, d'habitude, et pourquoi ?",
            "Combien de dates attendez-vous dans une page comme celle-là ?",
        ],
        notes="Laisser le groupe répondre franchement. La stratégie la plus répandue est "
              "de chercher son nom, puis d'abandonner. La séance donne une meilleure "
              "porte d'entrée : l'objet, puis la seule date qui oblige.")

    d.dialogue('Dialogue · 1 de 3', "Il y a trois dates dedans", [
        ("AMELIA", "Monsieur Gauthier, j'ai reçu un avis du centre. Je ne "
                   "suis pas sûre.", True),
        ("RÉMI", "Montrez-moi ça. Ah oui, c'est l'avis de confirmation "
                 "d'absence.", True),
        ("AMELIA", "Il y a trois dates dedans. Je mélange tout.", True),
        ("RÉMI", "Regardez : votre absence court du 9 mars jusqu'au 27 mars "
                 "inclusivement.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire remarquer le premier geste de monsieur Gauthier : il nomme le "
             "document avant d'en parler. « C'est l'avis de confirmation d'absence » — "
             "l'objet est en haut, et il répond déjà à la moitié des questions.")

    d.dialogue('Dialogue · 2 de 3', "D'ici le 6 mars", [
        ("AMELIA", "Et le 6 mars, en gras, en haut ? C'est quoi, cette "
                   "date-là ?", True),
        ("RÉMI", "C'est l'échéance. Le formulaire doit être remis d'ici le "
                 "6 mars.", True),
        ("AMELIA", "D'ici le 6, ça veut dire le 6 au plus tard ?", True),
        ("RÉMI", "Exactement. Après cette date-là, la demande n'est plus "
                 "recevable.", True),
    ], notes="Voici la séance en quatre répliques. Faire relever les trois dates au "
             "tableau et demander laquelle oblige. Le groupe hésite entre la première et "
             "la troisième : c'est la deuxième.")

    d.dialogue('Dialogue · 3 de 3', "Vous le signez et vous le rapportez", [
        ("AMELIA", "En bas, il est écrit « en cas de prolongation ». Je ne "
                   "comprends pas.", True),
        ("RÉMI", "Si vous devez rester plus longtemps, vous nous appelez "
                 "avant le 27.", True),
        ("AMELIA", "Je dois répondre à cet avis ?", True),
        ("RÉMI", "Non. Vous le signez et vous le rapportez au secrétariat. "
                 "Et gardez une copie : un avis signé sans copie, c'est un "
                 "avis qu'on n'a jamais reçu.", False),
    ], notes="La dernière réplique porte la règle la plus transférable du module. La "
             "faire recopier telle quelle. Une photo prise avec le téléphone avant de "
             "rendre la feuille suffit largement.")

    d.regle("Une seule date oblige",
            "Cherchez le verbe. « Le retour est prévu » informe. « Doit nous "
            "parvenir » oblige.",
            precision="Celle qui oblige est presque toujours en gras. Les autres "
                      "sont des rappels.",
            notes="Diapositive à photographier. Elle est la méthode du bloc C entier et "
                  "elle marche sur n'importe quel document officiel, scolaire ou non.")

    d.tableau('Quatre paragraphes, quatre rôles', "Ce que chacun fait",
              ['Le paragraphe', 'Ce qu'"'"'il vous demande'],
              [["Ce qui est confirmé", "Rien — il informe"],
               ["Ce que vous devez faire", "Tout — c'est l'échéance"],
               ["Votre retour", "Rien — c'est un rappel"],
               ["Si la situation change", "Un appel, si le cas se présente"]],
              cle=1,
              notes="Faire compléter la colonne de droite avant de l'afficher. Le "
                    "quatrième paragraphe est celui qu'on saute et qui coûte le plus "
                    "cher : une situation change toujours un peu.")

    d.piege("Prendre un rappel pour une échéance",
            "Le 30 mars est écrit : je dois faire quelque chose avant le 30.",
            "Le 30 mars est ma date de retour. L'échéance, c'est le 6.",
            "Une date de retour vous informe ; une échéance vous oblige. Les "
            "confondre fait manquer la vraie limite tout en s'inquiétant d'une "
            "fausse, ce qui est la pire combinaison possible.",
            notes="Ce piège se vérifie facilement : demander au groupe, avis en main, de "
                  "montrer du doigt la date qui oblige. Ceux qui montrent la dernière "
                  "n'ont pas cherché le verbe.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("L'avis reçu par Amelia porte trois dates.", "vrai"),
        ("Le 6 mars est la date de son retour.", "faux — c'est l'échéance"),
        ("« D'ici le 6 mars » veut dire le 6 mars au plus tard.", "vrai"),
        ("Après l'échéance, la demande n'est plus recevable.", "vrai"),
        ("Amelia doit répondre à l'avis par un courriel.",
         "faux — elle le signe et le rapporte"),
        ("Il vaut mieux garder une copie de l'avis signé.", "vrai"),
    ], corrige=True,
       notes="Faire justifier par la réplique exacte. La cinquième reprend le piège de "
             "A4 : beaucoup d'élèves écrivent ce courriel-là et attendent une réponse "
             "qui ne vient jamais.")

    d.billet(
        "Écrivez ce qu'Amelia doit faire, et pour quelle date.",
        exemples=[
            "Une seule phrase, avec une seule date.",
            "Ajoutez ce qui arrivera si elle ne le fait pas.",
        ],
        notes="Ramasser les billets. Ceux qui écrivent le 30 mars ont pris le rappel "
              "pour l'échéance : les reprendre en C2, avis en main.")

    return d.save(dossier)
