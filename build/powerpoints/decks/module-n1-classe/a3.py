# -*- coding: utf-8 -*-
"""A3 · Un livre, une chaise.
Bloc A « Je découvre » · couleur framboise · 60 min. Vocabulaire.
Source du module : exercices `prVocab`, `prImg` et `prNom`, mini-leçon `prNom`.

La séance ferme le bloc de découverte : les six objets sont sus, on leur donne
maintenant leur petit mot. C'est le premier point de grammaire du module, et
le seul du bloc A.
"""
import os

from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n1-classe/images/')


def photo(nom):
    """Le chemin de l'image, ou rien si elle n'est pas encore produite."""
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='A3', section='framboise',
        titre='Un livre, une chaise',
        chapeau="En français, le nom vient rarement seul. Un petit mot le "
                "précède, et il s'apprend avec lui.",
        duree='60 minutes')

    d.titre(notes="Séance de vocabulaire. Reprendre d'abord les six objets de A1 en les "
                  "montrant, sans article, puis annoncer qu'on va ajouter un mot devant "
                  "chacun.")

    d.objectifs([
        "dire « un » ou « une » devant les six objets ;",
        "comprendre que le petit mot s'apprend avec le nom ;",
        "associer une photo et une phrase ;",
        "écrire les six mots avec leur article.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qui change entre les deux ?",
        image=photo('livre-ouvert.jpg'),
        pistes=[
            "un livre — une chaise",
            "un stylo — une porte",
            "Qu'est-ce qui est pareil ?",
            "Qu'est-ce qui change ?",
        ],
        notes="Laisser chercher deux minutes. Quelqu'un dira que c'est « un » et "
              "« une ». Ne pas donner de règle : il n'y en a pas.")

    d.regle("Le petit mot devant",
            "un livre, une chaise.",
            precision="On ne dit pas « livre » tout seul. Le petit mot dit qu'il y en a "
                      "un, et à quel groupe le nom appartient : le groupe des "
                      "<b>un</b> ou le groupe des <b>une</b>.",
            notes="Diapositive à photographier. Le dire une fois et passer : la règle "
                  "n'explique rien, c'est l'usage qui compte.")

    d.tableau('Analyse', "Les deux groupes",
              ['Le groupe des un', 'Le groupe des une'],
              [["un livre", "une chaise"],
               ["un stylo", "une porte"],
               ["un sac", "une horloge"]],
              cle=2,
              note="Rien dans l'objet ne dit le groupe. Une chaise n'a rien de féminin.",
              notes="Diapositive à photographier. Si un élève demande pourquoi, répondre "
                    "franchement : il n'y a pas de raison, on l'apprend avec le mot.")

    d.piege("Apprendre le mot tout seul",
            "Retenir « porte ».",
            "Retenir « une porte ».",
            "L'article ne se devine jamais. Le seul moyen fiable est de l'apprendre "
            "collé au nom, dès la première fois. Sur votre feuille de mots, écrivez "
            "toujours les deux.",
            notes="C'est le conseil le plus utile de la séance. Le répéter à chaque "
                  "nouveau mot du module.")

    d.pratique('Vocabulaire', "Un ou une ?",
               "Écrivez le petit mot devant chaque nom.", [
        ("___ livre", "un livre"),
        ("___ chaise", "une chaise"),
        ("___ stylo", "un stylo"),
        ("___ porte", "une porte"),
        ("___ horloge", "une horloge"),
        ("___ sac", "un sac"),
    ], corrige=True, cols=2,
       notes="Six items, les six mots de A1. Corriger à voix haute, tous ensemble.")

    d.cartes('Écoute', "Devant une voyelle", [
        ("une horloge",
         "Le petit mot se colle au nom et s'entend mal. Écoutez la fin de « une » : il "
         "reste un petit son « n »."),
        ("Ce qu'on entend",
         "« u-n-horloge ». Les deux mots n'en font plus qu'un à l'oreille, mais on en "
         "écrit toujours deux."),
        ("À l'écrit",
         "une horloge, une école, une adresse. Jamais collés."),
    ], notes="Diapositive à photographier. Faire dire « une horloge » lentement, puis "
             "vite, pour entendre la différence.")

    d.pratique('Pratique · à deux', "Dans la salle",
               "Deux par deux, debout, avec un papier.", [
        ("Étape 1", "Trouvez dix objets dans la salle."),
        ("Étape 2", "Écrivez chacun avec son petit mot."),
        ("Étape 3", "Demandez à l'enseignante ceux que vous ne savez pas."),
        ("Étape 4", "Lisez votre liste à une autre équipe."),
    ], cols=1,
       notes="Vingt minutes. C'est le moment de donner des mots hors du module — une "
             "fenêtre, un mur, un crayon : ils entrent dans la feuille personnelle.")

    d.billet(
        "Écrivez les six mots du module avec leur petit mot.",
        exemples=[
            "un livre, un stylo, une chaise, un sac, une porte, une horloge.",
            "Puis ajoutez trois objets de chez vous, avec « un » ou « une ».",
        ],
        notes="Les trois objets de la maison seront demandés au début de B1 : c'est ce "
              "qui rattache le module à la vie de l'élève.")

    return d.save(dossier)
