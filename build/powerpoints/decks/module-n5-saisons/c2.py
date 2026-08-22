# -*- coding: utf-8 -*-
"""C2 · Trois décisions, trois messages
Bloc C « Défi 2 · La décision, et pourquoi » · couleur ambre · 75 min.
Source : exercice `t2dec` et sa mini-leçon du même nom.
"""
import os
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-saisons/images/')


def img(nom):
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Trois décisions, trois messages",
        chapeau="Huit situations du Centre communautaire, quatre saisons, et "
                "chaque fois la même méthode : est-ce que ça touche mon "
                "créneau, est-ce dangereux ou seulement désagréable, y "
                "a-t-il une date de rechange ?",
        duree='75 minutes')

    d.titre(notes="Séance d'application. Elle se fait par équipes de trois, avec les huit "
                  "cas distribués sur cartons. Chaque équipe décide, puis défend sa "
                  "décision devant le groupe. L'enseignante ne tranche qu'à la fin, et "
                  "seulement quand deux équipes s'opposent.")

    d.objectifs([
        "appliquer les trois questions dans l'ordre, chaque fois ;",
        "distinguer ce qui est dangereux de ce qui est seulement désagréable ;",
        "reconnaître le cas où l'on déplace l'heure au lieu de toucher à la date ;",
        "savoir qu'on ne décide pas trop tôt, mais qu'on annonce quand on décidera.",
    ], notes="Le deuxième objectif est le plus délicat : la limite entre désagréable et "
             "dangereux dépend du groupe. Huit personnes de plus de soixante-dix ans "
             "déplacent la limite, et c'est exactement ce qu'il faut apprendre à dire.")

    d.declencheur(
        'Observation', "Un sentier sous l'eau au printemps. Faut-il annuler "
                       "la visite guidée ?",
        image=img('crue-sentier.jpg'),
        pistes=[
            "Le parc rouvre dans deux semaines. Est-ce que ça change quelque chose ?",
            "L'autobus est réservé, mais pas encore payé. Et maintenant ?",
            "Vingt-deux personnes sont inscrites. Qui faut-il prévenir en premier ?",
            "Que diriez-vous à quelqu'un qui trouve qu'on exagère ?",
        ],
        notes="C'est le cas « crue » du jeu de rôle de E1. Le poser ici en groupe permet "
              "aux élèves d'arriver au jeu de rôle avec des arguments déjà éprouvés.")

    d.regle("Trois questions, toujours dans cet ordre",
            "Est-ce que ça touche mon créneau ? Est-ce dangereux ou seulement "
            "désagréable ? Existe-t-il une date de rechange ?",
            precision="La première vient du Défi 1, la deuxième dépend de votre "
                      "groupe, la troisième ne dépend pas du tout de la météo.",
            notes="Diapositive à photographier. Faire remarquer que seule la première "
                  "question porte sur le bulletin : les deux autres portent sur les gens "
                  "et sur le calendrier.")

    d.tableau('Deux catégories', "Désagréable, ou dangereux ?",
              ['Désagréable', 'Dangereux'],
              [["De la pluie, du vent ordinaire", "De la glace au sol"],
               ["Du froid d'hiver normal", "Un refroidissement éolien de −35"],
               ["Un ciel gris toute la journée", "Une visibilité nulle en poudrerie"],
               ["Une journée chaude d'été", "Une chaleur extrême, indice UV de 9"]],
              cle=1,
              note="Et la limite bouge : huit personnes de plus de 70 ans la déplacent.",
              notes="Faire compléter la colonne de droite avant de l'afficher. Puis poser "
                    "la question qui fâche : est-ce que la limite est la même pour un "
                    "groupe de vingt ans et pour celui de Marisol ?")

    d.cartes("Quatre décisions", "Ce qu'on dit dans chaque cas", [
        ("On maintient",
         "« L'atelier de cuisine est maintenu : il a lieu à l'intérieur. »"),
        ("On reporte",
         "« La marche est reportée au samedi 22, même heure, même endroit. »"),
        ("On annule",
         "« Le spectacle est annulé : la chorale ne repasse pas cette saison. »"),
        ("On déplace",
         "« La pétanque est maintenue, mais déplacée à neuf heures. »"),
    ], notes="Faire répéter les quatre phrases entières. Ce sont des modèles à copier, "
             "pas des exemples à commenter : l'élève doit pouvoir en produire une "
             "semblable en dix secondes.")

    d.pratique('Décision', "Maintenir, reporter ou annuler ?",
               "Pour chaque situation du Centre, choisissez et justifiez.", [
        ("Verglas samedi matin ; la marche peut se refaire le 22.", "on reporte — une date existe"),
        ("Ciel gris, averses ; l'atelier de cuisine est à l'intérieur.", "on maintient — ça ne touche pas"),
        ("Tempête samedi ; le spectacle de la chorale passe ce soir-là seulement.", "on annule — aucune date"),
        ("Crue printanière ; le parc rouvre dans deux semaines.", "on reporte — après la réouverture"),
        ("Chaleur extrême, UV de 9 ; la pétanque était à 14 h.", "on déplace à 9 h"),
        ("Froid extrême ; l'autobus loué est payé et non remboursable.", "on annule — l'argent, pas la météo"),
    ], corrige=True,
       notes="Six des huit énoncés de l'exercice t2dec du module. Exiger la "
             "justification autant que la décision. Le dernier surprend toujours : c'est "
             "l'argent qui force l'annulation, pas le froid.")

    d.piege("Décider trop tôt",
            "Mercredi : « J'annule, il y a une veille pour samedi. »",
            "Mercredi : « Je vous confirme vendredi à midi. »",
            "Les prévisions changeront d'ici là, souvent dans le bon sens. On "
            "annonce le moment de la décision, on écoute jusque-là, et on tranche "
            "à l'heure dite — même si l'on n'est pas plus sûr.",
            notes="Rappeler la formule de A1 : elle revient ici avec tout son poids. "
                  "Décider trop tôt coûte aussi cher que décider trop tard, et c'est "
                  "beaucoup moins évident.")

    d.billet(
        "Écrivez la décision et sa raison pour l'un des huit cas, en une seule phrase.",
        exemples=[
            "Choisissez le cas que votre équipe a défendu.",
            "La décision doit contenir la date, l'heure ou le lieu, selon le cas.",
        ],
        notes="Ramasser les billets : ils sont le brouillon direct de l'exercice t2msg de "
              "C4. Relever surtout les décisions incomplètes — « reportée » sans date — "
              "et les montrer anonymement au début de C4.")

    return d.save(dossier)
