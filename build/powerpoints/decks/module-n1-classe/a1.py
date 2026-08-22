# -*- coding: utf-8 -*-
"""A1 · Voici ta place.
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source du module : dialogue `prep`, exercices `pr1` et `prImg`.

Deuxième module du niveau 1 : le stade reste celui du grand débutant. Les
phrases projetées font deux à six mots, et chacune est une phrase que l'élève
pourra dire — ou faire — lui-même.
"""
import os

from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n1-classe/images/')


def photo(nom):
    """Le chemin de l'image, ou rien si elle n'est pas encore produite.

    Les séances se construisent avant que le générateur d'images ait tourné :
    sans ce garde-fou, `Deck.image()` ouvrirait un fichier absent et le build
    s'arrêterait sur une erreur de PIL, loin de sa cause.
    """
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre='Voici ta place',
        chapeau="Le premier matin dans une classe de français : une chaise, un "
                "livre, un stylo, et des mots pour les nommer.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Commencer sans parler : montrer un objet, "
                  "dire son nom, faire répéter. Cinq objets, cinq fois. Le dialogue vient "
                  "après.")

    d.objectifs([
        "nommer six objets de la classe ;",
        "comprendre « voici votre place » ;",
        "dire merci ;",
        "montrer l'objet qu'on entend nommer.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qu'il y a dans cette salle ?",
        image=photo('salle-vide.jpg'),
        pistes=[
            "Où sommes-nous ?",
            "Qu'est-ce qu'on voit ?",
            "Qu'est-ce qu'il y a sur les tables ?",
            "Qu'est-ce qu'il y a au mur ?",
        ],
        notes="Laisser nommer dans la langue qu'on peut, puis redire le mot en français "
              "et le faire répéter. À ce stade, montrer du doigt est une bonne réponse.")

    d.dialogue('Dialogue · 1 de 2', "L'arrivée", [
        ("MADAME CYR", "Bonjour ! Vous êtes Bopha ?", True),
        ("BOPHA", "Oui. Bonjour, madame.", True),
        ("MADAME CYR", "Voici votre place. La chaise est ici.", True),
        ("BOPHA", "Merci.", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Faire écouter deux fois, diapositive masquée. Puis afficher et faire "
             "répéter réplique par réplique, en chœur.")

    d.dialogue('Dialogue · 2 de 2', "Les objets", [
        ("MADAME CYR", "Voici un livre. Et voici un stylo.", True),
        ("BOPHA", "Un livre. Un stylo. Merci, madame.", True),
        ("MADAME CYR", "Le tableau est devant. L'horloge est là.", True),
    ], notes="Bopha répète ce qu'elle entend : c'est exactement ce qu'on demande au "
             "groupe. Le faire remarquer — répéter n'est pas tricher.")

    d.vocabulaire('Vocabulaire', "Six objets, six mots", [
        ("un livre", "On l'ouvre pour lire. Il a beaucoup de pages."),
        ("un stylo", "On écrit avec. Bleu ou noir."),
        ("une chaise", "On s'assoit dessus."),
        ("un sac", "On met le livre et le stylo dedans."),
        ("une porte", "On l'ouvre pour entrer dans la classe."),
        ("une horloge", "Elle est ronde, au mur. Elle donne l'heure."),
    ], notes="Diapositive à photographier. Montrer chaque objet dans la salle en le "
             "nommant. Les élèves touchent l'objet et répètent le mot.")

    d.regle("Voici…",
            "Le mot qui montre.",
            precision="« <b>Voici</b> votre place. » « <b>Voici</b> un livre. » On le dit "
                      "en montrant l'objet de la main. C'est le premier mot du module, et "
                      "il suffit à donner ou à demander n'importe quoi.",
            notes="Diapositive à photographier. Faire circuler un objet : chacun le "
                  "donne au voisin en disant « voici un stylo ».")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("La femme s'appelle Bopha.", "vrai"),
        ("Madame Cyr donne un livre à Bopha.", "vrai"),
        ("Madame Cyr donne un sac à Bopha.", "faux — un livre et un stylo"),
        ("Le tableau est devant la classe.", "vrai"),
    ], corrige=True, cols=1,
       notes="Quatre énoncés seulement : à ce stade, six seraient trop.")

    d.pratique('Pratique · à deux', "Montre-moi",
               "Deux par deux. L'un dit le mot, l'autre montre l'objet.", [
        ("Étape 1", "A dit : « le livre ». B montre le livre."),
        ("Étape 2", "On change de rôle."),
        ("Étape 3", "Six objets chacun, deux fois."),
        ("Étape 4", "Puis B nomme, A montre — sans regarder la liste."),
    ], cols=1,
       notes="Vingt minutes. Circuler. Ne corriger que le mot, jamais l'article au "
             "premier tour : l'article vient à la séance A3.")

    d.billet(
        "Écrivez le nom de cinq objets de votre sac ou de votre table.",
        exemples=[
            "Un mot par ligne, en lettres détachées.",
            "Dites-les à voix haute chez vous, trois fois.",
        ],
        notes="Devoir minuscule. Accepter le mot sans article : on le regarde ensemble à "
              "la séance A3.")

    return d.save(dossier)
