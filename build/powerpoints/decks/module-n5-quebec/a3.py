# -*- coding: utf-8 -*-
"""A3 · Les seize mots du voyage
Bloc A « Je découvre » · couleur framboise · 75 min. Vocabulaire.
Source : exercices `prVocab` et `prImg`, banc de mots FC_CARDS.
"""
import os
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-quebec/images/')


def img(nom):
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='A3', section='framboise',
        titre="Les seize mots du voyage",
        chapeau="Le programme ne fournit aucun lexique pour cette situation. "
                "Les seize mots du banc ont donc été composés à partir des "
                "savoirs : les régions et leurs attraits, l'hébergement, les "
                "bagages, les itinéraires, et la conversation sur place.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire. Elle est plus visuelle que les autres : la "
                  "moitié des mots désignent des choses que les élèves n'ont jamais "
                  "vues. Projeter les images du banc et faire nommer avant de montrer "
                  "le mot écrit. L'ordre compte : on voit, on nomme, on lit.")

    d.objectifs([
        "nommer ce qu'on voit quand on sort de la ville ;",
        "employer les mots du départ : un horaire, la soute, un aller-retour ;",
        "employer les mots du séjour : un gîte, un sentier, la marée ;",
        "dire ce qu'on trouve dans une région sans chercher ses mots.",
    ], notes="Les quatre groupes correspondent aux quatre sections du module. Les "
             "annoncer ainsi aide les élèves à ranger les mots au lieu de les empiler.")

    d.declencheur(
        'Observation', "Six photos, six phrases. Laquelle va avec laquelle ?",
        image=img('gare-autocars.jpg'),
        pistes=[
            "Qu'est-ce qui est numéroté, dans cette gare ?",
            "Que font les gens qu'on voit de dos ?",
            "Où mettra-t-on les grosses valises ?",
            "À quoi voit-on que ce n'est pas une gare de métro ?",
        ],
        notes="C'est l'exercice `prImg` de l'activité, posé à l'oral d'abord. Les quais "
              "numérotés sont le détail qui distingue une gare d'autocars d'un terminus "
              "d'autobus urbain : on y attend un départ précis, à une heure précise.")

    d.vocabulaire('Le paysage', "Ce qu'on va voir", [
        ("un attrait", "Ce qu'on va voir dans une région : un parc, un musée, une chute."),
        ("le fleuve", "Le très grand cours d'eau qui traverse le Québec."),
        ("un phare", "La tour dont la lumière tourne pour guider les bateaux."),
        ("un sentier", "Le petit chemin de terre où l'on marche, dans un parc."),
        ("un belvédère", "L'endroit aménagé, en hauteur, d'où l'on regarde le paysage."),
        ("la marée", "Le mouvement de l'eau qui monte et qui descend deux fois par jour."),
    ], notes="« La marée » est le mot le plus important des six, et le moins évident : "
             "il décide de l'heure d'une promenade et il revient en D1. Faire expliquer "
             "par quelqu'un qui vient d'un pays côtier, s'il y en a dans le groupe.")

    d.vocabulaire('Le départ', "Ce qu'on prépare", [
        ("un horaire", "La liste des heures de départ et d'arrivée, jour par jour."),
        ("la soute", "L'espace fermé, sous le plancher de l'autocar, pour les valises."),
        ("un dépliant", "La feuille pliée qui présente un endroit, avec une carte."),
        ("un gîte", "Une maison où l'on loue une chambre et où le déjeuner est compris."),
        ("le prêt-à-camper", "La tente ou le chalet déjà installé, avec les lits."),
        ("un vacancier", "Une personne en vacances dans une région où elle n'habite pas."),
    ], notes="« Un gîte » et « le prêt-à-camper » sont des réalités québécoises que le "
             "mot seul n'explique pas. Dire ce que ça coûte, à peu près, et à qui ça "
             "convient : c'est la question que les élèves poseront de toute façon.")

    d.cartes("Quatre mots qui se confondent", "Ils ne désignent pas la même chose", [
        ("Un horaire · un dépliant",
         "Le premier donne des heures. Le second donne des images et un plan."),
        ("Un gîte · le prêt-à-camper",
         "Le premier est une maison chauffée. Le second est dehors."),
        ("Un sentier · une rue",
         "Le premier est en terre, dans le bois. Le second est en ville."),
        ("Un vacancier · un touriste",
         "Le premier est en congé. Le second visite, et peut être d'ici."),
    ], notes="Ces quatre distinctions sont celles que le groupe manque à l'exercice "
             "d'appariement. Les faire dire avant l'exercice fait gagner dix minutes.")

    d.pratique('Emploi', "Complétez avec le bon mot",
               "À l'oral, puis à l'écrit dans le cahier.", [
        ("Les grosses valises vont dans …", "la soute"),
        ("J'ai regardé … pour connaître l'heure du départ.", "l'horaire"),
        ("À … basse, on voit les phoques sur les roches.", "marée"),
        ("On dort dans … : le déjeuner est compris.", "un gîte"),
        ("Du …, on voit les îles et l'autre rive.", "belvédère"),
        ("J'ai pris … du parc au comptoir d'accueil.", "un dépliant"),
    ], corrige=True,
       notes="Faire répéter la phrase entière une fois la réponse trouvée, avec "
             "l'article. Un mot appris sans son article se redit mal au comptoir.")

    d.piege("Apprendre le mot sans son article",
            "Marée, soute, gîte, sentier.",
            "La marée, la soute, un gîte, un sentier.",
            "Le genre ne se devine pas et il ne s'ajoute pas après coup : « le "
            "soute » se corrige beaucoup plus difficilement que « la soute » ne "
            "s'apprend. C'est cinq secondes de plus par mot, une fois.",
            notes="Règle de la maison pour tout le module : aucun mot n'est écrit au "
                  "tableau sans son article, et aucun n'est répété sans lui non plus.")

    d.billet(
        "Choisissez trois mots des seize et écrivez une phrase qui les contient tous les trois.",
        exemples=[
            "La phrase doit avoir un sens : ce n'est pas une liste.",
            "Prenez les trois mots qui vous semblent les plus difficiles.",
        ],
        notes="Ramasser les billets. Les phrases servent d'amorce en A4 et montrent tout "
              "de suite quels mots sont compris de travers.")

    return d.save(dossier)
