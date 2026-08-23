# -*- coding: utf-8 -*-
"""A1 · Ce que le site de l'entreprise ne dit pas
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.
"""
from theme import Deck

import pathlib

# Chemin déduit du fichier, jamais écrit en dur : le dépôt est aussi construit
# depuis un worktree git, où un chemin absolu vers la copie principale
# pointerait sur des images qui n'y sont pas encore.
IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n8-recherche' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Le dossier est parti. Et maintenant ?",
        chapeau="Au niveau 8, on ne cherche plus une offre : on soutient une "
                "candidature d'un bout à l'autre. Ce module se passe pendant "
                "le processus de sélection, pas avant.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir par une question au groupe : "
                  "qui a déjà passé plus d'une rencontre pour un même emploi ? "
                  "Presque personne ne répond oui, et c'est exactement le sujet.")

    d.objectifs([
        "nommer les trois étapes d'un processus de sélection ;",
        "distinguer un poste neuf d'un poste à remplacer, et dire pourquoi cela change tout ;",
        "comprendre ce qu'une page « À propos » dit et ce qu'elle tait ;",
        "employer les premiers mots du dossier : un processus de sélection, la présélection.",
    ], notes="Le deuxième objectif est celui qui surprend le plus. Le poser dès "
             "aujourd'hui : toutes les séances y reviennent.")

    d.declencheur(
        'Observation', "Que savez-vous d'un employeur avant d'y postuler ?",
        image=IMG + 'plancher-usine.jpg',
        pistes=[
            "Où avez-vous lu ce que vous savez : le site, une annonce, quelqu'un ?",
            "Savez-vous pourquoi le poste est ouvert ?",
            "Connaissez-vous quelqu'un qui y travaille ?",
            "Qu'auriez-vous voulu savoir avant votre dernière entrevue ?",
        ],
        notes="Question sans mauvaise réponse. La plupart des élèves ne savent que "
              "ce que dit l'annonce. Ne pas conclure à leur place : la séance le fera.")

    d.dialogue('Dialogue 1 de 3', "Le registre se tient, même entre anciens collègues", [
        ("SHIRIN", "Merci d'avoir accepté de me rencontrer, monsieur Pouliot-Nadeau. Je sais que vous finissez tard.", True),
        ("ALEXANDRE", "Ça me fait plaisir. Et on a travaillé ensemble deux ans, vous pouvez laisser tomber le nom de famille.", True),
        ("SHIRIN", "Je le garderai, si ça ne vous dérange pas. Vous êtes chez Boréalis maintenant, et j'y postule.", True),
        ("ALEXANDRE", "Comme vous voulez. Alors, le poste de superviseure de production, quart de soir.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire remarquer le refus poli du tutoiement. Ce n'est pas de la froideur : "
             "Shirin est candidate, et elle tient le registre du processus. Le module "
             "vouvoie partout pour cette raison, et c'est un savoir du niveau 8 — "
             "reconnaître la variété de langue et en tenir compte.")

    d.dialogue('Dialogue 2 de 3', "Ce que le site ne raconte pas", [
        ("ALEXANDRE", "Boréalis, sur son site, dit trois choses : quarante ans d'existence, deux cent dix employés, et « une entreprise à échelle humaine ».", True),
        ("ALEXANDRE", "Tout ça est vrai. Mais ça ne raconte pas la dernière année.", True),
        ("ALEXANDRE", "L'usine a été rachetée en janvier. La production a été réorganisée en trois quarts au lieu de deux, et le quart de soir a été créé de toutes pièces.", True),
        ("SHIRIN", "Autrement dit, on ne remplace personne. On ouvre.", True),
    ], notes="La reformulation de Shirin est le geste à faire remarquer : elle redit "
             "en six mots ce qu'Alexandre a mis trois phrases à expliquer. On y "
             "revient en B4.")

    d.dialogue('Dialogue 3 de 3', "L'objection que personne ne pose", [
        ("SHIRIN", "Ils vont me demander pourquoi je suis restée opératrice cinq ans.", True),
        ("ALEXANDRE", "Ils ne le demanderont pas. C'est bien pire : ils vont se le demander tout seuls, et vous ne saurez jamais qu'ils se le sont demandé.", True),
        ("ALEXANDRE", "À vous d'y répondre avant qu'ils y pensent.", True),
        ("SHIRIN", "Comment sait-on ce que les gens ne demandent pas ?", True),
    ], notes="C'est la thèse du module. L'écrire au tableau et l'y laisser jusqu'à la "
             "séance E2 : « ce qui gêne ne se dit presque jamais à voix haute ».")

    d.tableau('Analyse', "Trois étapes, trois choses observées",
              ['Étape', "Ce qu'on regarde"],
              [["L'examen écrit",
                "comment vous raisonnez, et la raison que vous donnez"],
               ["L'entrevue de groupe",
                "comment vous écoutez et laissez la parole"],
               ["L'entrevue individuelle",
                "qui vous êtes, vos exemples, vos conditions"]],
              cle=0,
              note="La deuxième est celle qui élimine, et celle que personne ne prépare.",
              notes="Diapositive à photographier. Demander au groupe laquelle des trois "
                    "leur fait le plus peur : ce sera la troisième, presque toujours.")

    d.regle("Un poste neuf n'est pas un poste vacant",
            "Remplacer quelqu'un et bâtir une équipe sont deux métiers "
            "différents. Savoir lequel des deux on vous propose change tout "
            "ce que vous direz de vous-même.",
            precision="Chez Boréalis, sept personnes sont en poste sur les seize "
                      "prévues : neuf restent à recruter. La personne embauchée "
                      "participera donc au choix de ces neuf-là, ce que l'annonce "
                      "ne dit nulle part.",
            notes="Diapositive à photographier. Question fréquente : « comment le "
                  "savoir ? » Réponse : en le demandant, et c'est tout le défi 1.")

    d.vocabulaire('Vocabulaire', "Six mots pour commencer", [
        ("un processus de sélection", "L'ensemble des étapes qu'un employeur fait franchir avant de choisir quelqu'un."),
        ("la présélection", "Le premier tri, souvent fait par téléphone, avant les vraies rencontres."),
        ("un accusé de réception", "Le court message qui confirme qu'un envoi est bien arrivé, sans rien décider."),
        ("un contremaître", "La personne qui dirige une équipe directement sur le plancher d'une usine."),
        ("un quart de soir", "La période de travail qui commence en après-midi et se termine tard le soir."),
        ("une chaîne de production", "La suite de machines et de postes où un produit se fabrique du début à la fin."),
    ], notes="Faire répéter avec l'article. Signaler que « quart » se dit aussi "
             "« shift » sur bien des planchers d'usine : les deux s'entendent, un "
             "seul des deux s'écrit dans une lettre.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Shirin a posé sa candidature mardi et n'a reçu qu'un accusé de réception.", "vrai"),
        ("Alexandre propose de la recommander à la direction.", "faux - elle ne le lui demande pas"),
        ("Le poste existe parce que quelqu'un a quitté l'entreprise.", "faux - il a été créé"),
        ("Boréalis a été rachetée en janvier par un groupe ontarien.", "vrai"),
        ("Selon Alexandre, la plupart des candidats tombent à la dernière étape.", "faux - à la deuxième"),
        ("Shirin choisit de continuer à vouvoyer un ancien collègue.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le troisième est "
             "le plus important : c'est la différence entre remplacer et bâtir.")

    d.billet(
        "Pensez à un employeur qui vous intéresse. Qu'est-ce que vous ne savez pas de lui ?",
        exemples=[
            "Écrivez trois questions, pas trois qualités.",
            "Une des trois doit commencer par « pourquoi ».",
        ],
        notes="Devoir concret. Les questions servent de matière première au bloc B : "
              "chaque élève arrive avec trois questions à poser au téléphone.")

    return d.save(dossier)
