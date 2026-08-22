# -*- coding: utf-8 -*-
"""A2 · Le son AN de content, le son IN de voisin.
Bloc A « Je découvre » · couleur indigo (graphie-phonie) · 60 min.
Source : mini-leçon `prPhon`, exercice `prPhon` (cartes à écouter).

Les sons sont nommés par un mot repère — « le son de content », « le son de
voisin » — plutôt que par un symbole phonétique : l'élève de niveau 3 n'a pas
l'alphabet phonétique, et le mot repère se retient sans être appris.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Content, voisin : deux sons qui passent par le nez",
        chapeau="Deux voyelles nasales se croisent sans arrêt dans un "
                "escalier d'immeuble. Beaucoup de langues n'en ont aucune, et "
                "l'oreille les confond pendant des mois.",
        duree='60 minutes')

    d.titre(notes="Séance de graphie-phonie. Prévoir de faire écouter beaucoup et "
                  "d'écrire peu : la difficulté est dans l'oreille, pas dans la main.")

    d.objectifs([
        "entendre la différence entre le son AN et le son IN ;",
        "produire les deux sons en tenant la bonne position de bouche ;",
        "reconnaître les quatre écritures les plus fréquentes ;",
        "ne plus prononcer la lettre N à la fin d'un mot nasal.",
    ])

    d.regle("L'air passe par le nez",
            "cont-en-t   ·   vois-in",
            precision="Dans ces mots, la lettre N ne se prononce pas toute "
                      "seule : elle rend la voyelle nasale, puis elle "
                      "disparaît. La bouche ne se ferme pas à la fin du mot.",
            notes="Diapo à photographier. Le truc à faire essayer : dire la voyelle en "
                  "se bouchant le nez avec deux doigts. Si le son change, l'air passait "
                  "bien par le nez — c'était le bon.")

    d.tableau('Analyse', "Le son AN — la bouche grande ouverte",
              ["On écrit", "On lit"],
              [["en", "content · comment · en avant"],
               ["an", "grand · dimanche · quatre ans"],
               ["am, em (devant b et p)", "chambre · ensemble"],
               ["Le piège", "« en » se dit AN, jamais « en »"]],
              cle=1,
              note="La mâchoire descend, les lèvres restent plates.",
              notes="Diapo à photographier. Faire répéter la colonne de droite en "
                    "exagérant l'ouverture de la bouche : c'est ce qui installe le son.")

    d.tableau('Analyse', "Le son IN — la bouche étirée",
              ["On écrit", "On lit"],
              [["in", "voisin · matin · invitation"],
               ["ain, ein", "demain · plein · le pain"],
               ["un", "lundi · quelqu'un · un"],
               ["Le truc", "souris en le disant, et c'est le bon son"]],
              cle=1,
              note="Les coins de la bouche s'écartent, comme pour sourire.",
              notes="Diapo à photographier. Demander à chacun de sourire franchement en "
                    "disant « voisin » : le son sort juste presque à tout coup.")

    d.pratique('Écoute', "Le son de content, ou le son de voisin ?",
               "Écoutez chaque mot et dites lequel des deux vous entendez.", [
        ("content", "le son de content"),
        ("un voisin", "le son de voisin"),
        ("un appartement", "le son de content"),
        ("le matin", "le son de voisin"),
        ("comment", "le son de content"),
        ("une invitation", "les deux : IN au début, AN à la fin"),
        ("en avant", "le son de content, deux fois"),
        ("le lendemain", "le son de voisin"),
    ], corrige=True,
       notes="Dire les mots plutôt que de les projeter d'abord : c'est un exercice "
             "d'oreille. Projeter le corrigé après. C'est l'exercice `prPhon` du module "
             "interactif, à cartes écoutables.")

    d.piege("Prononcer la lettre N",
            "voi-si-ne",
            "voi-sin",
            "« Un voisin » se termine sur une voyelle nasale : la bouche reste "
            "ouverte. « Une voisine », lui, se prononce bien avec le N — c'est le "
            "E final qui le réveille. Deux mots, deux fins de bouche différentes.",
            notes="Faire dire la paire « un voisin / une voisine » en tour de table. "
                  "C'est le meilleur exercice de la séance, et il tient en dix mots.")

    d.cartes("Le mot repère du module", "Une invitation", [
        ("Le mot contient les deux sons",
         "IN au début, AN à la fin : in-vi-ta-tion. Il traverse toute la difficulté du "
         "module en quatre syllabes."),
        ("À quoi il sert",
         "Quand un mot nouveau vous arrive et que vous hésitez, dites-le à côté de "
         "« content » puis à côté de « voisin ». Écoutez lequel se ressemble."),
        ("Ce qu'il faut retenir",
         "Deux mots repères, et rien d'autre : content pour le son AN, voisin pour le "
         "son IN. Les symboles phonétiques ne servent à rien à ce stade."),
        ("Où on l'entendra",
         "Toute la semaine : l'invitation est la matière du défi 2, et le mot revient "
         "dans presque chaque exercice."),
    ], notes="Faire écrire les deux mots repères en gros dans le cahier. C'est le seul "
             "aide-mémoire dont ils auront besoin.")

    d.pratique('Production', "À lire à voix haute",
               "Chacun lit une phrase. Le groupe dit combien de sons nasaux il a "
               "entendus.", [
        ("Mon voisin part travailler le matin.", "IN trois fois"),
        ("Je suis content de vous connaître.", "AN deux fois"),
        ("L'escalier monte en avant de l'immeuble.", "AN trois fois"),
        ("J'ai reçu une invitation ce matin.", "IN puis AN, puis IN"),
        ("Comment s'appelle le concierge ?", "AN au début et à la fin"),
        ("Demain, quelqu'un va venir.", "IN trois fois"),
    ], corrige=True,
       notes="Ne pas corriger la prononciation de chaque mot : signaler seulement les "
             "fins de mot où la bouche s'est fermée. Un seul point à la fois.")

    d.billet(
        "Écrivez deux mots de votre journée : un avec le son AN, un avec le son IN.",
        exemples=[
            "Le son AN : content, comment, grand, chambre…",
            "Le son IN : voisin, matin, demain, lundi…",
        ],
        notes="Devoir court. Ramasser et relire à voix haute au début de A3 : les "
              "erreurs de classement disent exactement où en est chaque oreille.")

    return d.save(dossier)
