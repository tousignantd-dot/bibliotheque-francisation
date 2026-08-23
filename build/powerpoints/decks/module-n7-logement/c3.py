# -*- coding: utf-8 -*-
"""C3 · Lequel, auquel, duquel
Bloc C « Défi 2 · La visite avec la courtière » · couleur ambre · grammaire ·
75 min.
Source : exercice `t2int` et sa mini-leçon ; savoir « pronoms interrogatifs »
du niveau 7 (trois points).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="Lequel, auquel, duquel",
        chapeau="« Lequel est inclus ? » est plus court que de répéter les "
                "deux stationnements — et ça montre qu'on a lu la fiche.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire. Elle sert directement la visite : ces pronoms "
                  "sont l'outil des questions précises travaillées en C2.")

    d.objectifs([
        "employer lequel, laquelle, lesquels, lesquelles à bon escient ;",
        "souder la préposition : auquel, duquel, auxquels, desquels ;",
        "trouver la préposition à partir du verbe ;",
        "distinguer quel (avec un nom) de lequel (à la place du nom).",
    ], notes="Le troisième objectif est la clé : on ne mémorise pas le tableau, on "
             "cherche le verbe et sa préposition, et la forme suit.")

    d.declencheur(
        'Observation', "Deux stationnements sur la fiche",
        pistes=[
            "« Est-ce que le numéro trois ou le numéro huit est inclus ? »",
            "« Lequel est inclus ? »",
            "Laquelle des deux questions est la plus claire ?",
            "Qu'est-ce que la seconde montre, en plus de poser la question ?",
        ],
        notes="Elle montre qu'on a lu la fiche avant d'arriver. Le dire : la forme "
              "d'une question dit quelque chose de celui qui la pose.")

    d.tableau('Analyse', "Trois séries, une seule logique",
              ['Sans préposition', 'Avec à / avec de'],
              [["lequel", "auquel · duquel"],
               ["laquelle", "à laquelle · de laquelle"],
               ["lesquels", "auxquels · desquels"],
               ["lesquelles", "auxquelles · desquelles"],
               ["Le féminin singulier reste en deux mots", "à laquelle, de laquelle"]],
              cle=0,
              notes="Diapositive à photographier. La dernière rangée est la seule "
                    "irrégularité, et elle se retient parce qu'elle est unique.")

    d.regle("C'est le verbe qui impose la préposition",
            "Cherchez le verbe d'abord ; la forme du pronom suit toute seule.",
            precision="On s'adresse à quelqu'un, on tient à quelque chose, on répond à "
                      "une offre : à + lequel donne auquel. On parle de quelque chose, "
                      "on a besoin de, il s'agit de : de + lequel donne duquel. Le "
                      "tableau ne s'apprend pas par cœur — on cherche le verbe, on "
                      "trouve sa préposition, et on soude.",
            notes="Diapositive à photographier. Le vérifier au tableau sur trois verbes "
                  "proposés par le groupe. La méthode tient à chaque fois.")

    d.pratique('Écriture', "Complétez la question",
               "Attention au genre, au nombre et à la préposition du verbe.", [
        ("Il y a deux stationnements. ___ est inclus dans le prix ?", "Lequel"),
        ("Vous parlez de deux immeubles. ___ des deux parlez-vous ?", "Duquel"),
        ("Ces trois courtiers travaillent ici. ___ vous êtes-vous adressée ?", "Auquel"),
        ("Deux conditions sont écrites. ___ tenez-vous le plus ?", "À laquelle"),
        ("Le procès-verbal parle de plusieurs réparations. ___ sont payées ?", "Lesquelles"),
        ("Deux dates sont inscrites sur l'avis. ___ fait courir le délai ?", "Laquelle"),
    ], corrige=True,
       notes="Six des huit items de `t2int`. Faire nommer le verbe et sa préposition "
             "avant de donner la réponse : c'est la méthode qu'on installe, pas la liste.")

    d.piege('Grammaire',
            "Quel est inclus, le trois ou le huit ?",
            "Lequel est inclus, le trois ou le huit ?",
            "« Quel » accompagne toujours un nom : quel stationnement, quelle date, "
            "quels travaux. « Lequel » remplace le nom et se tient tout seul. Le test "
            "prend une seconde : y a-t-il un nom juste après ? Si oui, quel. Si non, "
            "lequel.",
            notes="Faire produire les deux versions de la même question par le groupe, "
                  "à l'oral, sur trois exemples du module.")

    d.billet(
        "Écris deux questions de visite avec « lequel » ou « auquel ».",
        exemples=[
            "« Duquel des deux immeubles parlez-vous ? »",
            "Deux lignes.",
        ],
        notes="Deux minutes. Ajouter ces questions à la liste de six commencée en C2 : "
              "la liste finit la semaine à une dizaine de questions, toutes utilisables.")

    return d.save(dossier)
