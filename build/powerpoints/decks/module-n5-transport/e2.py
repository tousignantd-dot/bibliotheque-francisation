# -*- coding: utf-8 -*-
"""E2 · Écrire, et faire le point
Bloc E « Je me lance » · couleur framboise · 75 min. Production écrite et bilan.
Source : production écrite de l'activité interactive, banc FC_CARDS,
autoévaluation.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="Écrire, et faire le point",
        chapeau="La bretelle sera fermée toute la fin de semaine et les "
                "travaux se poursuivront lundi matin. Vous écrivez à votre "
                "équipe pour que personne ne se fasse prendre — puis vous "
                "faites le point sur les seize mots et sur ce que vous savez "
                "faire.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du module. Deux temps : la production écrite d'abord, "
                  "le bilan ensuite. Garder trente minutes pleines pour l'écriture — "
                  "c'est peu, et c'est déjà le minimum pour six à neuf phrases relues.")

    d.objectifs([
        "écrire un courriel qui prévient d'une entrave à venir ;",
        "employer une relative, un gérondif et deux futurs simples ;",
        "mettre l'information la plus importante dans la première phrase ;",
        "faire le point sur les seize mots du module.",
    ], notes="Le troisième objectif est une compétence d'écrit professionnel qui dépasse "
             "le module : un courriel se lit debout, sur un téléphone, en dix secondes. "
             "Ce qui n'est pas dans la première et la dernière phrase n'est pas lu.")

    d.regle("La première phrase et la dernière",
            "La première dit ce qui arrive. La dernière dit ce qu'il faut "
            "faire.",
            precision="Le milieu donne les détails : la date, l'heure, le chemin de "
                      "rechange. C'est utile, mais c'est ce qu'on lit en dernier.",
            notes="Diapositive à photographier. Faire relire les courriels reçus cette "
                  "semaine par le groupe, s'il y en a : la règle se vérifie toute seule.")

    d.tableau('Le courriel', "Ce qu\'il doit contenir",
              ['Élément', 'Exemple'],
              [["Une relative", "la bretelle qui mène à la 40"],
               ["Une durée", "pendant toute la fin de semaine"],
               ["Deux futurs simples", "sera fermée, se poursuivront"],
               ["Un gérondif", "en sortant à Marcel-Laurin"],
               ["Une consigne finale", "partez quinze minutes plus tôt"]],
              cle=1,
              notes="Les cinq éléments sont exactement les points de langue du module. "
                    "Le courriel n'est pas un exercice de plus : c'est le lieu où tout "
                    "se retrouve.")

    d.piege("Écrire un courriel qui commence par des excuses",
            "Bonjour, désolée de vous déranger avec ça, je ne sais pas si c'est utile…",
            "Bonjour à tous, la bretelle vers la 40 ouest sera fermée en fin de semaine.",
            "Une information utile n'a pas à s'excuser d'exister. Les excuses "
            "poussent l'information vers le bas, là où personne ne la lit.",
            notes="Très fréquent, et pas seulement chez les élèves. Le montrer sans "
                  "moquerie : c'est une habitude de politesse, pas une faute de langue.")

    d.pratique('Écriture', "Écrivez votre courriel",
               "Six à neuf phrases, avec « vous ».", [
        ("Objet", "Travaux sur la 15 : partez plus tôt lundi"),
        ("Phrase 1", "ce qui arrive, en une ligne"),
        ("Phrases 2-3", "quoi exactement, avec une relative"),
        ("Phrases 4-5", "quand, et ce qui arrivera lundi matin"),
        ("Phrase 6", "le chemin de rechange, avec un gérondif"),
        ("Dernière phrase", "la consigne, et la signature"),
    ], corrige=True,
       notes="Faire écrire au brouillon, puis relire à deux avec la grille des cinq "
             "éléments avant de saisir dans l'activité interactive. La relecture par un "
             "pair trouve plus d'oublis que la relecture par soi-même.")

    d.vocabulaire("Les seize mots", "Premier tiers du banc", [
        ("un ralentissement", "ça avance, mais lentement"),
        ("un bouchon", "ça ne bouge presque plus"),
        ("une entrave", "tout ce qui empêche de circuler"),
        ("l'accotement", "la bande en dehors des voies"),
        ("un carambolage", "plusieurs véhicules qui se frappent"),
        ("une remorqueuse", "le camion qui emporte l'accidenté"),
    ], notes="Faire dire chaque mot avec son article, sans le lire. Ceux qui ne viennent "
             "pas tout seuls sont ceux à revoir avec les cartes mémoire.")

    d.vocabulaire("Les seize mots", "Deuxième et troisième tiers", [
        ("une voie", "une bande marquée sur la chaussée"),
        ("une bretelle", "la route courbée entre deux autoroutes"),
        ("un nid-de-poule", "un trou creusé par le dégel"),
        ("un détour", "le chemin plus long qu'on prend"),
        ("un imprévu", "ce qui change le plan de la journée"),
        ("prévenir", "dire à l'avance, pour qu'on s'organise"),
    ], notes="Les quatre mots qui manquent — la chaussée, un véhicule d'urgence, le "
             "covoiturage, un stationnement incitatif — se révisent avec les cartes "
             "mémoire de l'activité interactive.")

    d.tableau('Le module en quatre temps', "Ce que vous savez faire maintenant",
              ['Le défi', 'Ce que vous savez faire'],
              [["Je découvre", "Nommer l'état d'une route"],
               ["Défi 1", "Dire ce qui bloque, où, depuis quand"],
               ["Défi 2", "Suivre un bulletin entier et le noter"],
               ["Défi 3", "Expliquer le détour et annoncer l'heure"]],
              cle=1,
              notes="Faire remplir la colonne de droite par le groupe avant de "
                    "l'afficher. Ce qu'ils nomment eux-mêmes est ce qui restera.")

    d.billet(
        "Écrivez une chose que vous ferez différemment demain matin, en écoutant la radio.",
        exemples=[
            "Une seule chose, concrète : écrire le nom de ma route, écouter deux fois.",
            "Ajoutez à quelle heure vous écouterez le bulletin.",
        ],
        notes="Dernier billet du module. Les ramasser et les relire au groupe à la "
              "séance suivante, sans nommer personne : c'est ce qui transforme le module "
              "en habitude.")

    return d.save(dossier)
