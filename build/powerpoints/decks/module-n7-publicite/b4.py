# -*- coding: utf-8 -*-
"""B4 · Trois jours, et pas un de plus
Bloc B « Défi 1 » · couleur ambre · 75 min.
Source : exercices `t1que` et `t1proc`, mini-leçons `t1que` et `t1proc`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="Trois jours, et pas un de plus",
        chapeau="« Il ne reste que trois jours. » Votre oreille entend « ne » "
                "et se prépare à une négation. Il n'y en a aucune : il reste "
                "bel et bien trois jours.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du Défi 1. Elle réunit un point de grammaire et le "
                  "bilan des six procédés : garder du temps pour le second, qui est "
                  "ce que les élèves emporteront.")

    d.objectifs([
        "comprendre que « ne… que » limite au lieu de nier ;",
        "placer « que » à l'endroit qui donne le sens voulu ;",
        "employer la tournure aux temps composés et devant une voyelle ;",
        "nommer les six procédés du Défi 1 et l'effet de chacun.",
    ], notes="Le deuxième objectif est le seul point vraiment difficile : déplacer "
             "« que » d'un mot change complètement la phrase.")

    d.declencheur(
        'Observation', "Combien de jours restent-ils ?",
        pistes=[
            "« Il ne reste que trois jours à notre vente. »",
            "Trois jours, ou aucun jour ?",
            "Comment dirait-on la même chose avec « seulement » ?",
            "Pourquoi l'annonce choisit-elle « ne… que » ?",
        ],
        notes="La dernière question amène la vraie leçon : « ne… que » dit d'abord "
              "« dépêchez-vous », et seulement ensuite « trois jours ». « La vente "
              "finit jeudi » ne presse personne.")

    d.regle("Ce n'est pas une négation, c'est une limite",
            "« Il ne reste que trois jours » veut dire : il reste seulement "
            "trois jours. Il en reste, donc.",
            precision="« ne » se place devant le verbe, « que » juste devant ce qu'on "
                      "limite. Devant une voyelle, les deux s'élident : « il n'y a "
                      "qu'un matelas ». Aux temps composés, « que » suit le participe.",
            notes="Diapositive à photographier. Le piège numéro un du niveau : le "
                  "« ne » fait entendre une négation là où il n'y en a aucune.")

    d.cartes('Analyse', "La place du « que » fait le sens", [
        ("Elle n'a payé que trente dollars.", "la somme est limitée : trente, pas plus"),
        ("Elle n'a que payé : elle n'a rien signé.", "l'action est limitée, pas la somme"),
        ("Il n'y a qu'elle qui a lu le bas.", "la personne est limitée : elle, et personne d'autre"),
        ("Ils n'ont annoncé que le prix.", "temps composé : « que » suit le participe"),
    ], cols=1,
       notes="Quatre placements, quatre sens. Faire lire chaque phrase à voix haute "
             "en accentuant ce qui suit « que » : le sens s'entend.")

    d.pratique('Pratique', "Récrivez avec « ne… que »",
               "Dites la même chose que « seulement ».", [
        ("Il reste seulement trois jours à la vente.", "Il ne reste que trois jours."),
        ("L'offre s'applique seulement aux nouveaux membres.", "L'offre ne s'applique qu'aux nouveaux membres."),
        ("Le rabais touche seulement les matelas sélectionnés.", "Le rabais ne touche que les matelas sélectionnés."),
        ("Elle a payé seulement trente dollars.", "Elle n'a payé que trente dollars."),
        ("Un seul matelas est à quarante pour cent.", "Il n'y a qu'un matelas à quarante pour cent."),
        ("La mention légale dure seulement cinq secondes.", "La mention légale ne dure que cinq secondes."),
    ], corrige=True,
       notes="Exercice `t1que` du module. Attention à la cinquième : deux élisions de "
             "suite, « il n'y a qu'un », ce qui surprend mais est correct.")

    d.piege('Grammaire',
            "« il n'y a pas que le prix » = seul le prix compte",
            "« il n'y a pas que le prix » = le prix, et autre chose aussi",
            "« pas que » nie la limite : c'est presque le contraire de « il "
            "n'y a que le prix ». Un seul mot change, et le sens s'inverse. "
            "La tournure est très fréquente à l'oral, et l'erreur coûte cher "
            "dans une conversation avec un commerçant.",
            notes="Faire produire les deux phrases par deux élèves différents et "
                  "demander au groupe laquelle veut dire quoi.")

    d.tableau('Bilan', "Six procédés, six effets",
              ['Le procédé', 'Ce qu\'il produit'],
              [["Le conditionnel", "une image du résultat, sans engagement"],
               ["Le comparatif tronqué", "vous choisissez le point de comparaison"],
               ["Le prix par semaine", "un petit nombre à la place d'un gros"],
               ["« Il ne reste que »", "une urgence qui empêche de comparer"],
               ["« Jusqu'à »", "le meilleur cas donné pour l'ordinaire"],
               ["La fin au double du débit", "l'obligation respectée sans être comprise"]],
              cle=0,
              notes="Diapositive à photographier, et à garder affichée jusqu'à E1 : "
                    "c'est la grille d'analyse de l'exposé oral.")

    d.billet(
        "Reprenez votre annonce et nommez un procédé de la liste des six.",
        exemples=[
            "Lequel, et dans quelle phrase exactement ?",
            "Recopiez la phrase entre guillemets.",
        ],
        notes="Devoir de repérage. La consigne de recopier entre guillemets prépare "
              "l'exposé de E1 et la lettre de E2, où la citation exacte est exigée.")

    return d.save(dossier)
