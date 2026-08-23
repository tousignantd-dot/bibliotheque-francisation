# -*- coding: utf-8 -*-
"""A1 · « Votre réclamation est refusée »
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercices `prVocab` et `pr1`.
"""
from theme import Deck

import pathlib

# Chemin déduit du fichier, jamais écrit en dur : le dépôt est aussi construit
# depuis un worktree git, où un chemin absolu vers la copie principale
# pointerait sur des images qui n'y sont pas encore.
IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n8-habitation' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="La lettre dit non. Ce n'est pas la fin.",
        chapeau="Quatre modules du programme parlent déjà de problèmes de "
                "logement. Celui-ci commence là où ils s'arrêtent : le "
                "problème a été examiné, jugé, et refusé par écrit.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir par une question au groupe : "
                  "qui a déjà reçu une lettre qui disait non ? Presque toutes les "
                  "mains se lèvent — assurance, immigration, banque, employeur. "
                  "C'est exactement le sujet, et il dépasse l'assurance.")

    d.objectifs([
        "distinguer être couvert et être indemnisé ;",
        "nommer les pièces d'un dossier de réclamation refusée ;",
        "comprendre ce qu'une exclusion de contrat veut dire ;",
        "employer les premiers mots du dossier : un sinistre, une réclamation, un avenant.",
    ], notes="Le premier objectif est celui qui surprend, et c'est aussi celui qui "
             "fait perdre le plus de dossiers : on répond à côté pendant des "
             "semaines. Le poser dès aujourd'hui.")

    d.declencheur(
        'Observation', "Qu'est-ce qui s'est passé dans ce sous-sol ?",
        image=IMG + 'sous-sol-inonde.jpg',
        pistes=[
            "D'où vient l'eau, à votre avis ?",
            "Qu'est-ce qui est perdu, sur cette photo ?",
            "Qui paie, normalement ?",
            "Avez-vous déjà vu un dégât d'eau, ici ou ailleurs ?",
        ],
        notes="Question sans mauvaise réponse. Laisser venir « l'assurance paie » : "
              "c'est justement ce que le module va compliquer. Ne pas corriger tout "
              "de suite.")

    d.dialogue('Dialogue 1 de 3', "Le motif tient en trois mots", [
        ("TEODORA", "Bonjour madame. Teodora Vlaicu, dossier 2026-41837. J'ai reçu une lettre hier.", True),
        ("MARJOLAINE", "Refoulement d'égout, rue Sainte-Julie, Trois-Rivières, sinistre du 14 septembre. C'est bien ça ?", True),
        ("TEODORA", "C'est ça. La lettre dit que la réclamation est refusée. Je voudrais comprendre pourquoi.", True),
        ("MARJOLAINE", "Le motif retenu est le défaut d'entretien du drain de plancher.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire remarquer la première phrase de Teodora : son nom, son numéro de "
             "dossier, la date. Trois données en une phrase. C'est ce qui fait qu'on "
             "lui répond, et le module y reviendra à chaque séance.")

    d.dialogue('Dialogue 2 de 3', "Couverte, et refusée quand même", [
        ("TEODORA", "Ma lettre parle d'un avenant « eau du sol et égout ». Je l'ai, cet avenant ?", True),
        ("MARJOLAINE", "Vous l'avez depuis 2023, avec une franchise de mille dollars. Ce n'est pas la protection qui manque. C'est l'exclusion qui a été appliquée.", True),
        ("TEODORA", "Donc je suis couverte, mais on refuse de payer.", True),
        ("MARJOLAINE", "Formulé comme ça, oui. Le contrat couvre le refoulement ; il ne couvre pas un refoulement causé par un défaut d'entretien.", True),
    ], notes="C'est la diapositive la plus importante de la séance. La reformulation "
             "de Teodora — « couverte, mais on refuse de payer » — est ce que la "
             "plupart des gens mettent des semaines à comprendre. L'écrire au "
             "tableau et l'y laisser tout le bloc A.")

    d.dialogue('Dialogue 3 de 3', "Ce que l'assureur n'a pas, il ne l'a pas cherché", [
        ("TEODORA", "Le drain a été nettoyé au mois de mai. Par une entreprise. J'ai la facture.", True),
        ("MARJOLAINE", "Cette information n'apparaît pas au dossier. Vous l'aviez transmise ?", True),
        ("TEODORA", "Personne ne me l'a demandée. L'expert est venu, il a regardé vingt minutes, et je ne l'ai jamais revu.", True),
        ("MARJOLAINE", "Ce que je peux faire aujourd'hui, c'est noter votre appel au dossier. Je ne peux pas rouvrir une décision moi-même.", True),
    ], notes="Deux choses à faire remarquer. Un : la facture existait, et elle n'est "
             "pas au dossier — personne ne l'a demandée. Deux : l'agente ne décide "
             "rien, et se fâcher contre elle ne servirait à rien.")

    d.regle("Être couvert et être indemnisé sont deux choses",
            "Un contrat peut couvrir un événement et refuser de payer "
            "celui-là, parce qu'une exclusion s'applique. Ne discutez donc "
            "jamais de votre protection quand on vous parle de l'exclusion.",
            precision="C'est la façon la plus fréquente de perdre un mois : on "
                      "envoie ses papiers d'assurance pour prouver qu'on est assuré, "
                      "et personne ne l'avait contesté. L'exclusion, elle, tient "
                      "toujours.",
            notes="Diapositive à photographier. Demander au groupe de la reformuler à "
                  "voix haute avant de passer à la suite.")

    d.vocabulaire('Vocabulaire', "Six mots pour commencer", [
        ("un refoulement d'égout", "La remontée des eaux usées par les drains d'un bâtiment, souvent pendant une grosse pluie."),
        ("un sinistre", "L'événement qui cause les dommages et qui déclenche une réclamation."),
        ("une réclamation", "La demande d'indemnité qu'un assuré adresse à son assureur après un sinistre."),
        ("un avenant", "Une protection ajoutée à un contrat d'assurance, en plus de celles qui y sont déjà."),
        ("une franchise", "La part des dommages qui reste à la charge de l'assuré à chaque réclamation."),
        ("une exclusion", "Un cas nommé dans le contrat pour lequel l'assureur ne paie pas."),
    ], notes="Faire répéter avec l'article. « Avenant » et « exclusion » sont les deux "
             "qui font le sens du module : l'un ajoute, l'autre retranche, et un "
             "contrat porte les deux en même temps.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("La réclamation porte sur un refoulement d'égout du 14 septembre.", "vrai"),
        ("Le motif du refus est le défaut d'entretien du drain de plancher.", "vrai"),
        ("Teodora n'a pas d'avenant « eau du sol et égout ».", "faux - elle l'a depuis 2023"),
        ("La franchise prévue au contrat est de mille dollars.", "vrai"),
        ("La facture du nettoyage figure déjà au dossier de l'assureur.", "faux - personne ne l'a demandée"),
        ("Madame Pelchat peut rouvrir elle-même la décision.", "faux - elle ne fait que noter"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le cinquième est "
             "celui qui compte : le dossier ne se remplit pas tout seul.")

    d.billet(
        "Pensez à une décision qu'on vous a annoncée par lettre. Que disait-elle exactement ?",
        exemples=[
            "Écrivez le motif en une phrase, dans les mots de la lettre.",
            "Puis écrivez ce que vous auriez voulu répondre.",
        ],
        notes="Devoir concret. Les deux phrases servent de matière première au bloc C, "
              "où chacun aura un motif à contester — le sien ou celui de Teodora.")

    return d.save(dossier)
