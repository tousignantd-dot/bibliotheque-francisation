# -*- coding: utf-8 -*-
"""C1 · Vous m'avez remis un copier-coller poli
Bloc C « Défi 2 » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t2vf`, vocabulaire de la section `t2`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Vous m'avez remis un copier-coller poli",
        chapeau="Un résumé qui reprend les phrases du texte ne prouve rien : "
                "l'enseignante ne sait pas si vous avez compris ou si vous "
                "avez copié. Résumer, ce n'est pas raccourcir.",
        duree='75 minutes')

    d.titre(notes="Première séance du Défi 2. La scène est une correction, et c'est "
                  "délibéré : les élèves reconnaîtront le moment. Ne pas en faire un "
                  "reproche — le personnage n'en fait pas un non plus.")

    d.objectifs([
        "comprendre pourquoi un résumé ne se recopie pas ;",
        "rattacher chaque phrase d'un résumé à la question de départ ;",
        "nommer les trois outils qui évitent le copier-coller ;",
        "employer les mots du travail écrit : une source fiable, un résumé.",
    ], notes="Le deuxième objectif est le critère qui servira toute la semaine. "
             "L'écrire au tableau et l'y laisser.")

    d.declencheur(
        'Observation', "Deux résumés de la même page",
        pistes=[
            "Le premier reprend les phrases du texte, dans l'ordre.",
            "Le second répond à une question, avec d'autres mots.",
            "Lequel prouve que la personne a compris ?",
            "Lequel est le plus rapide à écrire ?",
        ],
        notes="La quatrième piste est honnête : le copier-coller est plus rapide, et "
              "il faut le dire. C'est ce qui rend la règle crédible.")

    d.dialogue('Dialogue · 1 de 3', "D'où vient cette phrase ?", [
        ("GHISLAINE", "Regardez la troisième phrase et dites-moi d'où elle vient.", True),
        ("MIGUEL", "De la fiche de la ville. On l'a prise telle quelle parce qu'elle était claire.", True),
        ("GHISLAINE", "Elle est claire parce que quelqu'un a été payé pour l'écrire. Et c'est justement pour ça qu'on ne la recopie pas.", True),
        ("GHISLAINE", "Un résumé qui reprend les phrases du texte ne prouve rien : je ne sais pas si vous avez compris ou si vous avez copié.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Deux écoutes. La réponse de Miguel est raisonnable, et les élèves la "
             "trouveront juste : c'est ce qui rend la suite intéressante.")

    d.dialogue('Dialogue · 2 de 3', "La question de départ décide", [
        ("NEUSA", "Mais si la phrase dit exactement ce qu'on veut dire, pourquoi la changer ?", True),
        ("GHISLAINE", "Parce que ce n'est pas votre travail de dire ce que le texte dit. Votre travail, c'est de dire ce que le texte apporte à votre question.", True),
        ("NEUSA", "Elle parle du budget du programme. Ça ne répond pas à la question.", True),
        ("GHISLAINE", "Et pourtant vous l'avez gardée. Pourquoi ? Parce qu'elle était intéressante. C'est le piège de tous les résumés.", True),
    ], notes="Le point de la séance. Faire relire le mandat écrit en A3 : chaque "
             "équipe doit pouvoir dire sa question de départ sans regarder.")

    d.dialogue('Dialogue · 3 de 3', "Trois outils", [
        ("GHISLAINE", "Le premier : remplacez un morceau de phrase par un nom. La ville a planté quatre cents arbres, ça devient la plantation de quatre cents arbres.", True),
        ("GHISLAINE", "Deuxième outil : quand une chose revient, ne la renommez pas pareil.", True),
        ("GHISLAINE", "Les connecteurs. Un résumé sans connecteurs est une liste.", True),
        ("NEUSA", "Est-ce qu'on a le droit de citer une phrase du texte, quand même ?", True),
    ], notes="Les trois outils sont les trois séances qui suivent, dans l'ordre : C3, "
             "C4 et la fin de C4. La réponse à la question de Neusa est oui, une, "
             "entre guillemets, avec la source.")

    d.tableau('Analyse', "Ce qu'un résumé garde",
              ['On garde', 'On enlève'],
              [["La définition", "les coordonnées"],
               ["La cause", "le financement"],
               ["Les chiffres datés", "l'histoire de l'organisme"],
               ["Les réserves de la source", "la date de la page elle-même"]],
              cle=0,
              note="Une seule question devant chaque phrase : est-ce que ça répond à ma question ?",
              notes="Diapositive à photographier. La quatrième ligne de gauche est "
                    "celle qu'on oublie : reprendre la prudence d'une source, c'est "
                    "ce qui distingue un travail honnête d'un travail rapide.")

    d.vocabulaire('Vocabulaire', "Les mots du travail écrit", [
        ("la question de départ", "Ce que l'équipe cherche à savoir, et à quoi chaque phrase doit se rattacher."),
        ("une source fiable", "Un document dont on connaît l'auteur, la date, et qui peut être vérifié ailleurs."),
        ("une fiche d'information", "Une page courte, écrite par un organisme, présentée par sections titrées."),
        ("un résumé", "Un texte court qui redit avec ses propres mots ce qu'un texte apporte à la question posée."),
        ("une citation", "Une phrase reprise mot pour mot, entre guillemets, avec sa source."),
    ], notes="Faire distinguer « citation » et « copier-coller » : la première est "
             "signalée et attribuée, le second est caché. C'est toute la différence.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Le résumé était trop long.", "faux - il faisait la bonne longueur"),
        ("La troisième phrase venait telle quelle de la fiche.", "vrai"),
        ("La phrase sur le budget répondait à la question.", "faux - elle était hors sujet"),
        ("Ils l'avaient gardée parce qu'elle était intéressante.", "vrai"),
        ("Ghislaine interdit toute citation.", "faux - une, avec la source"),
        ("Un résumé sans connecteurs devient une liste.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique. Le premier surprend : "
             "le problème n'était pas la longueur, et les élèves s'attendent au "
             "contraire.")

    d.billet(
        "Écrivez votre question de départ, puis une phrase de votre source qui n'y répond pas.",
        exemples=[
            "La question en haut, la phrase en dessous.",
            "Dites en trois mots pourquoi elle ne répond pas.",
        ],
        notes="Devoir concret. Repérer une phrase hors sujet est plus facile que d'en "
              "garder une bonne, et c'est par là qu'on commence.")

    return d.save(dossier)
