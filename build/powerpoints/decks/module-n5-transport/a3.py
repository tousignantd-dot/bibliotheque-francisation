# -*- coding: utf-8 -*-
"""A3 · Ce qu'on voit sur la route
Bloc A « Je découvre » · couleur framboise · 75 min. Vocabulaire.
Source : exercices `prVocab` et `prImg`, banc FC_CARDS.
"""
import os
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-transport/images/')


def img(nom):
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='A3', section='framboise',
        titre="Ce qu'on voit sur la route",
        chapeau="Seize mots, et le bulletin cesse d'être un bruit. Ils ne "
                "s'apprennent pas dans un livre : ils s'entendent tous les "
                "matins, toujours les mêmes, dans le même ordre.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire. Les seize mots sont ceux du banc « Je retiens "
                  "des mots » de l'activité interactive : le travail fait ici se "
                  "retrouve tel quel à l'écran. Prévoir de la place au tableau, on y "
                  "écrira les seize.")

    d.objectifs([
        "nommer ce qui bloque : un carambolage, une entrave, une panne ;",
        "nommer les parties de la route : la voie, la chaussée, l'accotement ;",
        "nommer ce qui vient dégager : la remorqueuse, les véhicules d'urgence ;",
        "employer chaque mot avec son article.",
    ], notes="Le quatrième objectif est celui qu'on oublie : « voie » et « bretelle » "
             "sont féminins, « accotement » et « carambolage » masculins. L'article fait "
             "partie du mot, on ne l'apprend pas après.")

    d.declencheur(
        'Observation', "Cinq photos de la même route. Qu'est-ce qui change "
                       "d'une photo à l'autre ?",
        image=img('chantier-cones.jpg'),
        pistes=[
            "Qu'est-ce qui empêche de passer, sur cette photo ?",
            "Sur quelle partie de la route se trouve l'obstacle ?",
            "Est-ce que c'était prévu, à votre avis ?",
            "Qui va venir régler ça ?",
        ],
        notes="Les quatre pistes ramènent aux quatre informations du bulletin, vues en "
              "A1. Le vocabulaire n'est pas une liste : c'est ce qui permet de répondre "
              "à ces questions-là.")

    d.vocabulaire("Ce qui bloque", "Les mots de l'entrave", [
        ("une entrave", "tout ce qui empêche de circuler normalement"),
        ("un ralentissement", "ça avance, mais lentement"),
        ("un bouchon", "ça ne bouge presque plus"),
        ("un carambolage", "plusieurs véhicules qui se frappent"),
        ("un nid-de-poule", "un trou creusé par le gel et le dégel"),
    ], notes="« Nid-de-poule » fait toujours sourire : le mot vient de la forme du trou, "
             "rond et peu profond. Il s'écrit avec deux traits d'union. À Montréal, on "
             "les signale au 311.")

    d.vocabulaire("La route elle-même", "Les mots du bitume", [
        ("une voie", "une bande marquée où passe une file d'autos"),
        ("la chaussée", "la partie où les véhicules roulent"),
        ("l'accotement", "la bande sur le bord, en dehors des voies"),
        ("une bretelle", "la petite route courbée entre deux autoroutes"),
        ("un détour", "le chemin plus long qu'on prend à la place"),
    ], notes="« Bretelle » surprend : le mot désigne aussi ce qui tient un pantalon. Le "
             "sens routier vient de la forme, courbée. Faire remarquer que « voie » et "
             "« bretelle » sont féminins.")

    d.vocabulaire("Ce qui vient dégager", "Les véhicules du bulletin", [
        ("une remorqueuse", "le camion qui emporte un véhicule accidenté"),
        ("un véhicule d'urgence", "ambulance, pompiers, police en service"),
        ("le covoiturage", "faire la route à plusieurs, dans la même auto"),
        ("un stationnement incitatif", "où l'on laisse son auto pour le métro"),
        ("un imprévu", "ce qui change le plan de la journée"),
    ], notes="« Stationnement incitatif » est un mot d'ici : ces stationnements existent "
             "aux abords des gares et des terminus. Demander qui en utilise un.")

    d.tableau('Deux familles', "Ce qui bloque, et ce qui dégage",
              ['Ce qui bloque', 'Ce qui dégage'],
              [["un carambolage", "une remorqueuse"],
               ["un bouchon", "un véhicule d'urgence"],
               ["un nid-de-poule", "un détour"],
               ["une entrave", "une voie de rechange"]],
              cle=1,
              notes="Faire remplir la colonne de droite par le groupe. Le classement "
                    "compte moins que la discussion qu'il provoque : un détour "
                    "dégage-t-il vraiment, ou déplace-t-il le problème ?")

    d.piege("Oublier l'article, ou se tromper de genre",
            "Un voie, un bretelle, la accotement.",
            "Une voie, une bretelle, l'accotement.",
            "L'article fait partie du mot et s'apprend avec lui. Devant une voyelle, "
            "« le » et « la » deviennent « l' » : l'accotement, l'entrave — et on "
            "n'entend plus le genre, il faut donc le savoir.",
            notes="Faire dire chaque mot avec « un » ou « une », jamais seul. C'est la "
                  "seule façon de fixer le genre, et c'est aussi ce que demande "
                  "l'exercice de vocabulaire de l'activité interactive.")

    d.pratique('Vocabulaire', "Le mot juste",
               "Complétez avec le mot qui convient.", [
        ("Les autos roulent à quarante : on annonce un ___.", "ralentissement"),
        ("Plus rien ne bouge : c'est un vrai ___.", "bouchon"),
        ("Un camion est arrêté sur l'___.", "accotement"),
        ("Aucune ___ à signaler dans le tunnel.", "entrave"),
        ("Une ___ vient dégager le véhicule.", "remorqueuse"),
        ("La ___ de droite reste ouverte.", "voie"),
    ], corrige=True,
       notes="Les six mêmes phrases sont dans l'exercice `prEtat` de l'activité "
             "interactive, où elles sont corrigées automatiquement. Ici, on les fait à "
             "l'oral d'abord.")

    d.billet(
        "Choisissez trois des seize mots et écrivez une phrase avec chacun.",
        exemples=[
            "Une phrase vraie, tirée de votre trajet, vaut mieux qu'une phrase inventée.",
            "N'oubliez pas l'article : une voie, un détour, l'accotement.",
        ],
        notes="Ramasser les billets. Relever les erreurs de genre et les reprendre en "
              "début de séance A4, sans nommer personne.")

    return d.save(dossier)
