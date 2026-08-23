# -*- coding: utf-8 -*-
"""A4 · Un goût, un avis, un argument
Bloc A « Je découvre » · couleur ambre · écriture et grammaire · 75 min.
Source : exercice `prAvis` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="Un goût, un avis, un argument",
        chapeau="Trois phrases de la même personne, sur la même œuvre. Une "
                "seule permet à la discussion de continuer.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc A. C'est la séance la plus importante du "
                  "module : tout ce qui suit en dépend. Prévoir du temps pour "
                  "l'écriture, et ramasser les productions.")

    d.objectifs([
        "distinguer un goût, un avis et un argument ;",
        "transformer un goût en argument en ajoutant le pourquoi ;",
        "appuyer un jugement sur un moment précis de l'œuvre ;",
        "annoncer son avis comme un avis, et non comme un fait.",
    ], notes="Le quatrième objectif surprend souvent : dire « je trouve » n'est pas "
             "une faiblesse, c'est ce qui laisse à l'autre le droit d'avoir vu "
             "autre chose.")

    d.declencheur(
        'Observation', "Qu'est-ce qu'on peut répondre à « c'est bon » ?",
        pistes=[
            "Essayez : quelqu'un dit « c'est bon », vous répondez quoi ?",
            "Et à « le refrain revient quatre fois » ?",
            "Laquelle des deux phrases donne du travail à l'autre ?",
            "Laquelle des deux avez-vous dite le plus souvent ?",
        ],
        notes="Faire jouer les deux répliques pour de vrai, en dyades, trente "
              "secondes. La première conversation meurt au deuxième tour ; la "
              "seconde continue. La démonstration vaut mieux qu'une explication.")

    d.tableau('Analyse', "Trois niveaux, trois effets",
              ['Ce qu\'on dit', 'Ce que l\'autre peut faire'],
              [["Un goût",
                "rien, sinon dire le sien : la conversation s'arrête là"],
               ["Un avis",
                "être d'accord ou non, et dire pourquoi à son tour"],
               ["Un argument",
                "aller vérifier, puis approuver, nuancer ou contredire"]],
              cle=0,
              note="Le troisième niveau coûte une phrase de plus, et il vaut la réunion.",
              notes="Diapositive à photographier. Le tableau se lit de haut en bas : "
                    "chaque niveau contient le précédent et ajoute une chose.")

    d.cartes('Analyse', "Les trois morceaux d'un argument", [
        ("Ce que l'œuvre fait", "le début ne contient aucune parole"),
        ("Ce que vous en pensez", "j'ai trouvé le début long"),
        ("Le moment précis", "aucune parole avant la douzième minute"),
        ("Ce qui manque presque toujours", "le troisième"),
    ], cols=1,
       notes="Faire compter au groupe combien de fois le troisième morceau apparaît "
             "dans leurs billets de A1. En général : une ou deux fois sur douze.")

    d.regle("Un argument s'appuie sur ce que les autres ont vu aussi",
            "Un moment précis se vérifie ; une impression générale ne se "
            "vérifie pas.",
            precision="« Il y a plein de belles scènes » ne s'appuie sur rien : "
                      "personne ne peut aller compter « plein ». « À la quatrième "
                      "nuit, il la laisse pétrir seule et il sort fumer » est une "
                      "scène que tout le monde peut retrouver.",
            notes="Diapositive à photographier. C'est la phrase à répéter à chaque "
                  "production orale du module, y compris en E1.")

    d.piege('Écrit',
            "« Ce film est ennuyant. »",
            "« J'ai trouvé le premier quart d'heure long. »",
            "La première phrase se présente comme un fait et n'en est pas un : "
            "elle braque l'interlocuteur, qui doit choisir entre vous croire ou "
            "vous contredire. La seconde dit d'où vous parlez, et laisse à "
            "l'autre la place d'avoir vu autre chose.",
            notes="Point de posture, pas de politesse. Beaucoup d'élèves croient que "
                  "« je trouve » affaiblit. C'est le contraire : ça ouvre la "
                  "discussion au lieu de la fermer.")

    d.pratique('Compréhension', "Un goût, ou un avis ?",
               "Pour chaque phrase, dites si l'on peut en discuter.", [
        ("Cette chanson-là, c'est ma préférée.", "un goût"),
        ("Le refrain revient quatre fois, et la quatrième il monte trop haut.", "un avis"),
        ("Moi, l'humour, j'embarque jamais.", "un goût"),
        ("On a ri deux fois en six minutes, jamais aux mêmes endroits.", "un avis"),
        ("C'est bon.", "un goût"),
        ("Le film ne dit jamais ce que les personnages pensent.", "un avis"),
    ], corrige=True,
       notes="Exercice `prAvis` du module. Après correction, faire transformer les "
             "trois goûts en arguments à l'oral : c'est l'exercice qui compte.")

    d.pratique('Production écrite', "Transformez trois goûts",
               "Ajoutez à chacun le pourquoi et un moment précis.", [
        ("« J'aime pas les films tranquilles. »", "je décroche quand une scène dure trois minutes sans parole"),
        ("« Le spectacle est bon. »", "on a ri deux fois en six minutes, à des moments différents"),
        ("« La chanson est belle. »", "le refrain revient quatre fois et change de sens chaque fois"),
        ("Votre goût, tiré du billet d'hier", "à transformer de la même façon"),
    ], corrige=False,
       notes="Quinze minutes d'écriture. Ramasser : ce sont les phrases qui "
             "reviendront en E1 et en E2, et l'on voit tout de suite qui a compris "
             "que le pourquoi doit porter sur l'œuvre et non sur soi.")

    d.billet(
        "Écrivez un argument complet sur l'œuvre de votre billet d'hier.",
        exemples=[
            "Trois morceaux : ce qu'elle fait, ce que vous en pensez, le moment.",
            "Trois phrases suffisent.",
        ],
        notes="Fin du bloc A. Le bloc B commence avec un sketch, et l'argument "
              "demandé y portera sur ce qui fait rire.")

    return d.save(dossier)
