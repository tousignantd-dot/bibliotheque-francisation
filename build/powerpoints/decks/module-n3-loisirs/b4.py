# -*- coding: utf-8 -*-
"""B4 · Au comptoir du centre.
Bloc B « Défi 1 · Quand, combien, quoi apporter ? » · teal · 60 min.
Source du module : dialogue `t1b`, exercices `t1comptoir` et `t1rep`.
"""
import os

from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-loisirs/images/')


def img(nom):
    """Le chemin de la photo, ou None tant qu'elle n'existe pas.

    Voir la note de a1.py : les images sont produites par gen_images.py, et
    `theme.image()` ouvrirait un fichier absent.
    """
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='B4', section='teal',
        titre="Au comptoir du centre",
        chapeau="Le téléphone ne dit pas tout. Marisol se présente au "
                "comptoir, et deux renseignements nouveaux arrivent : l'heure "
                "des familles, et la preuve d'adresse qui fait baisser le "
                "tarif de cinq dollars à trois.",
        duree='60 minutes')

    d.titre(notes="Dernière séance du défi 1. Elle ferme la boucle : on a téléphoné, on "
                  "se présente, et on découvre ce qu'on n'avait pas pensé à demander.")

    d.objectifs([
        "comprendre un échange au comptoir d'un service ;",
        "poser une question qu'on n'avait pas prévue ;",
        "savoir ce qu'est une preuve d'adresse et à quoi elle sert ;",
        "associer chaque question à la réponse qui lui correspond.",
    ])

    d.declencheur(
        'Observation', "Que fait-on à ce comptoir-là ?",
        image=img('comptoir-accueil.jpg'),
        pistes=[
            "Qu'est-ce qu'il y a sur le comptoir, et à quoi ça sert ?",
            "Qu'est-ce qu'on peut demander à la personne qui est derrière ?",
            "Est-ce qu'il faut un rendez-vous pour se présenter ici ?",
            "Qu'est-ce qu'on peut avoir à montrer, et pourquoi ?",
        ],
        notes="La dernière piste amène la preuve d'adresse. Si personne n'y pense, "
              "laisser passer : le dialogue l'apporte deux minutes plus tard, et la "
              "surprise vaut mieux que l'annonce.")

    d.dialogue('Dialogue · 1 de 3', "L'heure des familles", [
        ("MARISOL", "Bonjour. J'ai téléphoné mardi passé, pour le badminton.", True),
        ("ROXANE", "Ah oui ! Vous êtes venue. Le gymnase est au fond du corridor, à gauche.", True),
        ("MARISOL", "Merci. J'aimerais savoir autre chose : ma fille a huit ans. Est-ce qu'elle peut venir ?", True),
        ("ROXANE", "Le mardi soir, c'est pour les adultes. Mais le samedi matin, il y a une heure pour les familles.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="« J'aimerais savoir autre chose » est la formule à relever : elle ouvre une "
             "question nouvelle sans avoir l'air de déranger. La faire répéter.")

    d.dialogue('Dialogue · 2 de 3', "La preuve d'adresse", [
        ("MARISOL", "Parfait. Est-ce que je dois montrer une carte ?", True),
        ("ROXANE", "Une preuve d'adresse, la première fois. Un compte d'électricité ou votre bail, ça suffit.", True),
        ("MARISOL", "Je n'ai pas ça avec moi aujourd'hui.", True),
        ("ROXANE", "Ce n'est pas grave. Aujourd'hui, vous payez le tarif visiteur : cinq dollars.", True),
    ], notes="Beaucoup d'élèves croient qu'il faut une carte d'identité officielle. La "
             "réponse — un compte d'électricité, un bail — surprend et rassure. Demander "
             "à chacun quel papier il aurait sous la main chez lui.")

    d.dialogue('Dialogue · 3 de 3', "Deux dollars de différence", [
        ("MARISOL", "Et avec la preuve d'adresse ?", True),
        ("ROXANE", "Trois dollars, le tarif du quartier. Apportez-la samedi et je la note à votre dossier.", True),
        ("MARISOL", "Très bien. Merci de votre patience.", True),
        ("ROXANE", "Ça me fait plaisir. Bon badminton !", False),
    ], notes="« Merci de votre patience » est une formule de sortie utile et rare chez "
             "les élèves. L'écrire au tableau à côté de « merci beaucoup » : deux façons "
             "de finir, l'une plus chaleureuse que l'autre.")

    d.tableau('Analyse', "Deux tarifs, une seule différence",
              ["Le tarif", "Combien", "Ce qu'il faut"],
              [["tarif visiteur", "5 $", "rien — on paie et on entre"],
               ["tarif du quartier", "3 $", "une preuve d'adresse, une seule fois"],
               ["heure des familles", "gratuit pour les enfants", "l'adulte paie son tarif"]],
              cle=0,
              note="La preuve d'adresse ne se montre qu'une fois : elle reste au dossier.",
              notes="Diapo à photographier. Faire calculer l'économie sur une session de "
                    "douze semaines : vingt-quatre dollars pour un papier qu'on a déjà "
                    "chez soi.")

    d.regle("Le mot à retenir",
            "« une preuve d'adresse »",
            precision="C'est un papier qui montre où l'on habite : un compte "
                      "d'électricité, un compte de téléphone, un bail. Ce n'est pas une "
                      "carte d'identité : le centre ne veut pas savoir qui vous êtes, "
                      "mais où vous habitez, pour appliquer le tarif du quartier.",
            notes="Diapo à photographier. La distinction identité / adresse est le point "
                  "à faire passer : elle revient dans presque toutes les démarches "
                  "municipales.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Le gymnase est au fond du corridor, à gauche.", "vrai"),
        ("La fille de Marisol peut venir le mardi soir.",
         "faux — le mardi soir est pour les adultes"),
        ("L'heure des familles est le samedi matin.", "vrai"),
        ("Il faut montrer une preuve d'adresse la première fois.", "vrai"),
        ("Sans preuve d'adresse, Marisol paie trois dollars.",
         "faux — cinq dollars, le tarif visiteur"),
        ("Un compte d'électricité peut servir de preuve d'adresse.", "vrai"),
    ], corrige=True,
       notes="C'est l'exercice t1comptoir du module, rattaché au deuxième dialogue.")

    d.pratique('Association', "La question et la réponse",
               "Reliez chaque question à la réponse de la préposée.", [
        ("C'est quel jour ?", "Le mardi soir, toutes les semaines."),
        ("C'est à quelle heure ?", "De dix-neuf heures à vingt et une heures."),
        ("C'est combien ?", "Trois dollars par séance, payables à l'entrée."),
        ("Qu'est-ce qu'il faut apporter ?", "Des espadrilles propres et une bouteille d'eau."),
        ("C'est où, exactement ?", "Au gymnase, au fond du corridor à gauche."),
        ("Est-ce que ça dure longtemps ?", "Jusqu'à la fin de la session, en décembre."),
    ], corrige=True,
       notes="C'est l'exercice t1rep du module. Le faire d'abord à l'oral, réponses "
             "masquées, puis découvrir : la moitié se devine, et c'est justement ce "
             "qu'on veut installer avant le défi 2.")

    d.billet(
        "Quel papier avez-vous chez vous qui pourrait servir de preuve d'adresse ?",
        exemples=[
            "Un compte, une facture, un bail — écrivez lequel.",
            "Vérifiez qu'il porte bien votre nom et votre adresse.",
        ],
        notes="Devoir court et concret. Plusieurs élèves reviendront en disant qu'ils "
              "n'en ont trouvé aucun à leur nom : c'est une vraie difficulté de vie, et "
              "elle mérite deux minutes en début de séance suivante.")

    return d.save(dossier)
