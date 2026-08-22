# -*- coding: utf-8 -*-
"""E2 · Écrire pour inviter, et retenir les mots.
Bloc E « Je me lance » · framboise · 60 min. Production écrite et bilan.
Source du module : production écrite de « Je me lance », exercice `aComp`,
banc de vocabulaire FC_CARDS et autoévaluation.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="Écrire pour inviter",
        chapeau="Se renseigner ne sert à rien si l'on y va seul et sans le "
                "dire. Dernière tâche : écrire à quelqu'un pour l'emmener — "
                "le jour, l'heure, le prix, ce qu'il faut apporter, et une "
                "question à la fin.",
        duree='60 minutes')

    d.titre(notes="Dernière séance du module. Deux temps : la production écrite, puis "
                  "le bilan du vocabulaire et l'autoévaluation. Garder vingt minutes "
                  "pour le second, qui se bâcle toujours.")

    d.objectifs([
        "écrire un court message d'invitation, de cinq à huit phrases ;",
        "y mettre le jour, l'heure, le tarif et ce qu'il faut apporter ;",
        "employer « le mardi soir » et « de sept heures à neuf heures » ;",
        "faire le bilan de ce que je suis maintenant capable de faire.",
    ])

    d.tableau('La tâche', "Ce que le message doit contenir",
              ["L'élément", "Un exemple"],
              [["le nom de l'activité et l'endroit",
                "du badminton, au centre de la rue Galt"],
               ["le jour, avec « le » si c'est chaque semaine",
                "le mardi soir"],
               ["l'heure du début et de la fin",
                "de sept heures à neuf heures"],
               ["le tarif et ce qu'il faut apporter",
                "trois dollars, des espadrilles propres"],
               ["une question, à la fin",
                "Est-ce que ça te tente de venir avec moi ?"]],
              cle=0,
              notes="Diapo à photographier — c'est la grille de correction. La laisser à "
                    "l'écran pendant l'écriture. Cinq éléments, cinq à huit phrases : "
                    "on peut en mettre deux dans la même phrase.")

    d.regle("Ce qui se relit avant d'envoyer",
            "« le » devant le jour · « de… à… » devant les heures",
            precision="Ce sont les deux formes travaillées au bloc A et au bloc C, et "
                      "les deux qui sautent aux yeux quand elles manquent. « Mardi » "
                      "sans « le » dit une seule fois ; « à sept heures » sans « de… "
                      "à… » ne dit pas quand ça finit.",
            notes="Diapo à photographier. Faire relire le message une fois en ne "
                  "cherchant que ces deux choses-là : une relecture qui cherche tout ne "
                  "trouve rien.")

    d.pratique('Écriture', "Un message d'invitation",
               "De cinq à huit phrases. Vous écrivez à quelqu'un que vous voulez "
               "emmener avec vous.", [
        ("À qui écrivez-vous ?", "une voisine, un camarade de classe, votre sœur"),
        ("Quelle activité ?", "celle que vous avez choisie depuis la séance A1"),
        ("Où et quand ?", "le nom du centre, le jour avec « le », l'heure avec « de… à… »"),
        ("Combien, et quoi apporter ?", "le tarif, et ce qu'il faut avoir avec soi"),
        ("Comment finir ?", "une question : est-ce que ça te tente de venir ?"),
    ], notes="L'écriture se fait dans le module, section « Je me lance ». La correction "
             "de l'assistant reste privée ; l'élève choisit ensuite d'envoyer ou non. "
             "Circuler pendant l'écriture plutôt que de corriger après.")

    d.vocabulaire('Bilan · 1 de 3', "Le centre et son horaire", [
        ("un centre communautaire", "La maison du quartier, où l'on entre sans rendez-vous."),
        ("un babillard", "Le panneau de liège de l'entrée, couvert de feuilles."),
        ("un feuillet", "Le petit journal plié qui annonce les activités."),
        ("une session", "Les semaines pendant lesquelles une activité a lieu."),
        ("le tarif", "Le prix demandé pour participer."),
        ("une séance", "Une fois où l'activité a lieu : un soir, une heure précise."),
    ], notes="Six mots du bloc A et du bloc B. Faire dire chacun avec son article, puis "
             "faire donner un exemple de phrase.")

    d.vocabulaire('Bilan · 2 de 3', "Le ciné-club et la cuisine", [
        ("un ciné-club", "Le petit cinéma de quartier, un film par semaine."),
        ("un téléhoraire", "Le journal qui donne l'heure des films et une phrase sur chacun."),
        ("un documentaire", "Un film qui montre des choses vraies, sans acteurs."),
        ("une cuisine collective", "Un groupe qui cuisine ensemble et partage ce qu'il prépare."),
        ("une recette", "Le papier qui dit les aliments à prendre et les gestes à faire."),
        ("une tasse à mesurer", "Le contenant transparent avec des traits sur le côté."),
    ], notes="Six mots des blocs C et D. Les cartes mémoire du module reprennent les "
             "seize mots : renvoyer les élèves à l'outil « Réviser » de leur barre "
             "d'outils.")

    d.pratique('Bilan · 3 de 3', "Le mot juste",
               "Complétez avec un mot du module.", [
        ("Le panneau de l'entrée où on affiche les annonces est un ___ .", "babillard"),
        ("Les semaines pendant lesquelles une activité a lieu forment une ___ .", "session"),
        ("Le prix demandé pour participer est le ___ .", "tarif"),
        ("Une activité qui ne coûte rien est ___ .", "gratuite"),
        ("Une fois où l'activité a lieu s'appelle une ___ .", "séance"),
        ("Un film qui montre des choses vraies est un ___ .", "documentaire"),
        ("Le papier qui dit les aliments et les gestes est une ___ .", "recette"),
        ("Les souliers de sport à semelle de caoutchouc sont des ___ .", "espadrilles"),
    ], corrige=True,
       notes="C'est l'exercice aComp du module. Le faire à livre fermé : c'est le seul "
             "moment du module où l'on demande de retrouver un mot sans indice.")

    d.billet(
        "Qu'est-ce que vous êtes maintenant capable de faire ?",
        exemples=[
            "Répondez aux onze énoncés de l'autoévaluation, dans le module.",
            "Puis dites-en un à voix haute : celui dont vous êtes le plus content.",
        ],
        notes="L'autoévaluation est dans la section « Je retiens des mots ». Finir par "
              "le tour de table : chacun nomme une chose qu'il sait faire maintenant et "
              "qu'il ne savait pas faire il y a quatre avant-midis. C'est la meilleure "
              "minute du module.")

    return d.save(dossier)
