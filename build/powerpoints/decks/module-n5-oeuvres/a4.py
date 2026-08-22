# -*- coding: utf-8 -*-
"""A4 · La première phrase, et où on la dit
Bloc A « Je découvre » · couleur ambre · écriture · 75 min.
Source : exercice `prImg`, mini-leçon `prMot`, dialogue `prep`.
"""
import pathlib

from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-oeuvres/images/')


def photo(nom):
    """La photo si elle est sur le disque, None sinon — voir a1.py."""
    p = pathlib.Path(IMG + nom)
    return str(p) if p.exists() else None


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="La première phrase, et où on la dit",
        chapeau="Une bibliothèque de quartier, c'est un rayon, un comptoir, "
                "une salle du fond et un babillard à l'entrée. Chacun de ces "
                "endroits demande une façon de parler d'une œuvre — et tous "
                "commencent par la même phrase.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc A. Rendre les billets de A1 : chacun a nommé "
                  "une œuvre. C'est celle qu'il présentera au bloc E, et la séance "
                  "d'aujourd'hui lui donne sa première phrase. Prévoir du temps pour la "
                  "faire écrire et dire par tout le monde.")

    d.objectifs([
        "reconnaître les lieux d'une bibliothèque de quartier et ce qu'on y fait ;",
        "écrire la première phrase d'une présentation : support, genre, longueur ;",
        "la dire à voix haute sans la lire ;",
        "comprendre ce qu'un carton de coup de cœur contient et ne contient pas.",
    ], notes="Le troisième objectif est celui qu'il faut vraiment obtenir aujourd'hui. "
             "Écrire une phrase est facile ; la dire sans la lire l'est moins, et c'est "
             "exactement ce que le bloc E demandera pendant deux minutes.")

    d.declencheur(
        'Observation', "Un comptoir, des livres debout, de petits cartons "
                       "écrits à la main. Qu'est-ce qui est écrit dessus ?",
        image=photo('comptoir-coups-de-coeur.jpg'),
        pistes=[
            "Qui a écrit ces cartons, à votre avis ?",
            "Combien de temps prend-on pour en lire un ?",
            "Qu'est-ce qu'on veut savoir avant de prendre le livre ?",
            "Qu'est-ce qu'on ne veut surtout pas y trouver ?",
        ],
        notes="La quatrième piste ramène la règle du club : un carton qui raconte la fin "
              "gâche le livre pour tous ceux qui passent. Faire remarquer que ces cartons "
              "sont écrits par des lecteurs, pas par la bibliothèque : c'est exactement "
              "ce que l'élève écrira à la séance E2.")

    d.cartes("Quatre endroits, quatre façons de parler", "Dans une bibliothèque de quartier", [
        ("Le rayon",
         "On cherche seul. On lit les dos, on ouvre, on repose."),
        ("Le comptoir",
         "On demande conseil. Il faut dire ce qu'on a aimé avant qu'on nous conseille."),
        ("La salle du fond",
         "Le club. On parle deux minutes, personne ne coupe, on justifie."),
        ("Le babillard",
         "On écrit pour quelqu'un qu'on ne verra jamais. Sept à dix phrases."),
    ], notes="Les quatre endroits sont les quatre situations du module : le rayon en A, le "
             "comptoir au défi 2, la salle du fond au défi 3 et le babillard à la "
             "production écrite. Le dire au groupe : il verra où il s'en va.")

    d.regle("La première phrase dit toujours trois choses",
            "Le support, le genre, et une mesure : trois cents pages, huit "
            "épisodes, deux heures.",
            precision="« C'est un roman, une histoire de famille, à peu près trois "
                      "cents pages. » Après cette phrase-là, la personne en face sait "
                      "dans quoi elle s'embarque, et tout ce que vous ajoutez ensuite "
                      "se range tout seul. Sans elle, les dix premières secondes "
                      "servent à deviner de quoi vous parlez.",
            notes="Diapositive à photographier. Faire écrire la phrase par chacun, avec "
                  "son œuvre à lui, puis la faire dire debout, sans la lire. Trois ou "
                  "quatre passages par séance jusqu'à la fin du module.")

    d.tableau('Cinq moules', "La même phrase, selon le support",
              ['Support', 'La première phrase'],
              [["Un roman", "C'est un roman, une histoire de famille, trois cents pages."],
               ["Une bande dessinée", "C'est le premier tome d'une série de quatre albums."],
               ["Une série", "C'est une série de huit épisodes de quarante minutes."],
               ["Un film", "C'est un film de deux heures, une histoire vraie."],
               ["Une chanson", "C'est une chanson de quatre minutes, mon coup de cœur du mois."]],
              cle=1,
              notes="Ce sont des moules : on garde la structure et on change les chiffres. "
                    "Faire choisir à chacun la ligne qui correspond à son œuvre et "
                    "remplir. C'est le laboratoire de la mini-leçon `prMot` du module "
                    "interactif, en version projetée.")

    d.pratique('Repérage', "Où est-on, et qu'est-ce qu'on y voit ?",
               "Associez chaque description au lieu ou à l'objet.", [
        ("Une affiche collée sur la porte vitrée d'une salle.", "l'annonce du club"),
        ("Une dizaine de chaises placées en cercle.", "la salle du fond, le jeudi"),
        ("Un rayon rempli de romans du plancher au plafond.", "le rayon"),
        ("Des livres debout et de petits cartons écrits à la main.", "le comptoir des coups de cœur"),
        ("Un grand livre dont la page est découpée en petits carrés.", "une planche de bande dessinée"),
        ("Une femme assise près d'une fenêtre, un casque sur les oreilles.", "l'écoute sur place"),
    ], corrige=True,
       notes="C'est l'exercice `prImg` du module interactif, où les six photos se glissent "
             "sur les six phrases. Ici, sans les photos, l'exercice devient une "
             "association orale — et il prépare la lecture des images à l'écran.")

    d.piege("Écrire un carton qui ne dit pas ce que c'est",
            "Un livre magnifique, je l'ai adoré, courez le lire !",
            "C'est un roman, une histoire de famille. Ce qui m'a touchée, c'est…",
            "Un carton de babillard est lu par quelqu'un qui passe et qui n'a pas "
            "trente secondes. S'il ne sait pas ce que c'est en une ligne, il continue "
            "son chemin — et l'enthousiasme tout seul n'a jamais fait lire personne.",
            notes="Faire lire les deux versions à voix haute. Demander laquelle donne "
                  "envie : le groupe choisit toujours la seconde, et il sait dire "
                  "pourquoi. C'est la meilleure préparation à la séance E2.")

    d.pratique('À l\'oral', "Dites votre première phrase",
               "Debout, sans lire. Trois choses : le support, le genre, une mesure.", [
        ("Dites-la une première fois, en lisant si nécessaire.",),
        ("Redites-la sans regarder votre feuille.",),
        ("Redites-la une troisième fois, plus lentement.",),
        ("Écoutez celle de votre voisin et dites ce que vous avez retenu.",),
    ], notes="Quatre passages, deux par deux, puis trois ou quatre devant le groupe. La "
             "dernière consigne est la vérification : si le voisin peut redire le support "
             "et le genre, la phrase a fait son travail.")

    d.billet(
        "Écrivez la première phrase de votre présentation, telle que vous la direz.",
        exemples=[
            "Trois choses : le support, le genre, et une mesure — pages, épisodes, minutes.",
            "Relisez-la à voix basse : si elle ne tient pas en une respiration, coupez.",
        ],
        notes="Ramasser les billets et les garder : ils reviendront à la séance E1, quand "
              "l'élève enregistrera sa présentation. Plusieurs auront changé d'œuvre d'ici "
              "là — c'est normal, la phrase se refait en une minute.")

    return d.save(dossier)
