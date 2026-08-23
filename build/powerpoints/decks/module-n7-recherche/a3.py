# -*- coding: utf-8 -*-
"""A3 · Les outils, et les lieux qui vont avec
Bloc A « Je découvre » · couleur framboise · vocabulaire · 75 min.
Source : exercices `prVocab`, `prOutils`, `prImg`.
"""
from theme import Deck

import pathlib

# Chemin déduit du fichier, jamais écrit en dur : le dépôt est aussi construit
# depuis un worktree git, où un chemin absolu vers la copie principale
# pointerait sur des images qui n'y sont pas encore.
IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n7-recherche' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='A3', section='framboise',
        titre="Les outils, et les lieux qui vont avec",
        chapeau="Dix-huit mots tiennent tout le module : ceux de la "
                "recherche, ceux de l'économie d'une région, ceux de la "
                "candidature écrite. Aujourd'hui, on les installe.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire. Le piège serait d'en faire une liste à "
                  "apprendre : chaque mot est ici rattaché à un lieu, à un geste ou "
                  "à un document réel. Garder ce rattachement.")

    d.objectifs([
        "associer chaque outil de la recherche d'emploi à ce qu'il fait ;",
        "nommer les lieux du travail industriel en région ;",
        "employer les dix-huit mots du module avec leur article ;",
        "distinguer un secteur d'activité d'un métier.",
    ], notes="Le dernier objectif règle une confusion tenace : « la construction » "
             "est un secteur, « charpentier » est un métier.")

    d.declencheur(
        'Observation', "Qu'est-ce qu'on voit sur cette photo ?",
        image=IMG + 'babillard-offres.jpg',
        pistes=[
            "Où trouve-t-on encore des offres punaisées comme celles-là ?",
            "Et où les trouve-t-on autrement ?",
            "Qu'est-ce qu'une offre doit dire pour être utile ?",
            "Avez-vous déjà répondu à une annonce affichée ?",
        ],
        notes="Beaucoup d'élèves n'ont vu que des offres en ligne. Le babillard "
              "existe encore dans les usines, les CPE et les épiceries : c'est un "
              "canal réel, et souvent moins encombré.")

    d.tableau('Analyse', "Chaque outil a son travail",
              ['Outil', 'Ce qu\'il fait — et rien d\'autre'],
              [["IMT en ligne", "les salaires et les perspectives, par région"],
               ["Le curriculum vitæ", "résume la formation et l'expérience"],
               ["La lettre d'accompagnement", "pourquoi ce poste-là, et pourquoi vous"],
               ["Le portrait économique", "de quoi vit un territoire, en chiffres"]],
              cle=0,
              note="Aucun ne remplace un autre.",
              notes="Diapositive à photographier. Exercice `prOutils` du module "
                    "interactif : les élèves le referont seuls, en glisser-déposer.")

    d.vocabulaire('Vocabulaire · 1 de 2', "L'économie d'une région", [
        ("un secteur d'activité", "Un grand groupe d'entreprises qui font le même genre de travail : la forêt, la santé."),
        ("la transformation", "Le travail qui change une matière brute en produit : l'arbre en planche, le minerai en métal."),
        ("une usine", "Le grand bâtiment où l'on fabrique ou transforme des produits à l'aide de machines."),
        ("la main-d'œuvre", "L'ensemble des personnes qui travaillent, ou qui pourraient travailler, dans une région."),
        ("la relève", "Les personnes plus jeunes qui prendront la place de celles qui partent à la retraite."),
        ("un quart de travail", "La tranche d'heures pendant laquelle une équipe travaille : le jour, le soir, la nuit."),
    ], notes="« La main-d'œuvre » et « la relève » sont les deux mots que l'employeur "
             "emploiera en B2. Les installer maintenant.")

    d.vocabulaire('Vocabulaire · 2 de 2', "Lire, comparer, se présenter", [
        ("le produit intérieur brut", "La valeur totale de ce qui est produit dans un territoire pendant une année."),
        ("un portrait économique", "Le document qui décrit, chiffres à l'appui, de quoi vit un territoire."),
        ("l'embauche", "Le fait d'engager quelqu'un, et le moment où ça se décide."),
        ("une offre d'emploi", "L'annonce par laquelle un employeur fait savoir qu'il cherche quelqu'un."),
        ("une candidature", "L'ensemble des documents qu'une personne envoie pour se proposer à un poste."),
        ("un atout", "Ce qui joue en votre faveur et vous distingue des autres personnes qui postulent."),
    ], notes="« Un atout » revient au bloc D, dans l'offre d'emploi : ce n'est pas "
             "la même chose qu'une exigence, et la distinction décide de tout.")

    d.cartes('Analyse', "Les lieux du dossier", [
        ("La salle multiservice", "des postes informatiques, une imprimante, un agent — et rien à payer"),
        ("Le laboratoire de contrôle", "une paillasse, des éprouvettes, une balance de précision"),
        ("L'usine de transformation", "des bâtiments de tôle, des cheminées, un stationnement d'employés"),
        ("Le babillard", "des feuilles punaisées, dans un couloir d'usine ou d'école"),
        ("La table de cuisine", "deux feuilles imprimées, un stylo, une tasse — le vrai bureau"),
        ("La route régionale", "de la forêt, un village au loin, quatre cents kilomètres de Montréal"),
    ], cols=2,
       notes="Exercice `prImg` du module interactif. Le dernier n'est pas décoratif : "
             "un déménagement en région est aussi une question de distance, et le "
             "module ne le cache pas.")

    d.pratique('Vocabulaire', "Le mot juste",
               "Complétez avec un mot du dossier.", [
        ("La construction est le ___ qui a le plus grandi cette année.", "secteur d'activité"),
        ("Il manque de ___ dans les laboratoires de la région.", "main-d'œuvre"),
        ("Le poste affiché est sur le ___ de jour.", "quart de travail"),
        ("Dans ce métier-là, la ___ ne suit plus depuis dix ans.", "relève"),
        ("Il n'a reçu que onze ___ en six mois.", "candidatures"),
        ("Neuf ans de cahier de laboratoire, c'est un ___ sérieux.", "atout"),
    ], corrige=True,
       notes="Faire dire la phrase entière à voix haute une fois corrigée. L'article "
             "compte autant que le mot.")

    d.billet(
        "Nommez le secteur d'activité de votre métier, puis un autre où il pourrait servir.",
        exemples=[
            "Un même métier sert souvent dans deux ou trois secteurs.",
            "Exemple : un mécanicien, dans le transport et dans la fabrication.",
        ],
        notes="Cette question prépare le bloc B : c'est en changeant de secteur, pas "
              "de métier, que plusieurs élèves trouveront.")

    return d.save(dossier)
