# -*- coding: utf-8 -*-
"""A3 · Cinq rôles, et ce que chacun fait vraiment
Bloc A « Je découvre » · couleur teal · 75 min.
Source : exercice `prRoles`, vocabulaire de la section `prep`.
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n7-classe' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre="Cinq rôles, et ce que chacun fait vraiment",
        chapeau="Un rôle n'est pas un titre : c'est une liste de gestes. "
                "Aujourd'hui, chaque équipe de la classe repart avec ses "
                "rôles attribués, son mandat écrit et son échéancier.",
        duree='75 minutes')

    d.titre(notes="Séance d'organisation, et la plus concrète du bloc A. À la fin, "
                  "chaque équipe doit avoir une feuille avec trois noms, trois rôles "
                  "et trois dates. Sans cette feuille, le module reste théorique.")

    d.objectifs([
        "associer chaque rôle au travail qui lui revient ;",
        "écrire le mandat de son équipe en trois lignes ;",
        "poser un échéancier avec une date par étape ;",
        "dire ce qu'on attend des autres, sans reproche.",
    ], notes="Le quatrième objectif est de langue autant que d'organisation : « je "
             "compte sur toi pour… » se dit, et il s'apprend.")

    d.declencheur(
        'Observation', "Ce que l'équipe de Neusa doit remettre",
        image=IMG + 'stationnement-asphalte.jpg',
        pistes=[
            "Trois semaines, une question, un exposé de quatre minutes.",
            "Qui va chercher les documents ? Qui va sur le terrain ?",
            "Quand faut-il avoir fini de chercher pour commencer à écrire ?",
            "Que se passe-t-il si une personne manque une rencontre ?",
        ],
        notes="La dernière piste amène le compte rendu, vu au bloc D. La photo est "
              "le stationnement que l'équipe ira observer : la montrer sans "
              "l'expliquer, elle revient en B4.")

    d.tableau('Analyse', "Le rôle et les gestes",
              ['Le rôle', 'Les gestes'],
              [["Animer",
                "ouvrir, donner la parole, faire préciser, reformuler, fermer"],
               ["Prendre les notes",
                "écrire ce qui se dit, relire à voix haute quand on le demande"],
               ["Surveiller le temps",
                "annoncer les minutes qui restent, avant qu'il n'en reste plus"],
               ["Tenir les sources",
                "noter l'auteur, la date et l'adresse de chaque document"],
               ["Présenter",
                "parler au nom de l'équipe, avec les mots que l'équipe approuve"],
               ["Être absent",
                "lire le compte rendu et répondre avant la rencontre suivante"]],
              cle=0,
              notes="Diapositive à photographier. La sixième ligne fait sourire, et "
                    "c'est voulu : l'absent a un rôle, et c'est le plus facile à "
                    "oublier. Elle prépare la lettre du bloc E.")

    d.regle("Le mandat s'écrit, sinon il se devine",
            "Tant que le mandat n'est pas écrit, chacun en a une version "
            "différente dans la tête — et personne ne s'en aperçoit avant la "
            "dernière semaine.",
            precision="Trois lignes suffisent : ce qu'on cherche, ce qu'on remet, "
                      "et pour quand. C'est la première chose que fait une "
                      "personne qui anime, avant même la première rencontre.",
            notes="Diapositive à photographier. Faire écrire le mandat de chaque "
                  "équipe pendant la séance, pas à la maison.")

    d.vocabulaire('Vocabulaire', "Les mots de l'organisation", [
        ("un échéancier", "La liste de ce qui doit être fait, avec la date de chaque étape."),
        ("une étape", "Une partie du travail qui se termine avant que la suivante commence."),
        ("une remise", "Le moment où le travail est donné à l'enseignante."),
        ("un empêchement", "Ce qui vous rend absent sans que vous l'ayez choisi."),
        ("se répartir", "Se partager le travail entre personnes de l'équipe."),
    ], notes="« Se répartir » est un verbe pronominal : le faire employer à la "
             "première personne du pluriel, « nous nous répartissons ».")

    d.pratique('Grammaire', "Dire ce qu'on attend, sans reproche",
               "Complétez la phrase à voix haute, chacun votre tour.", [
        ("Je compte sur toi pour…", "…apporter la carte du quartier samedi."),
        ("Est-ce que tu pourrais…", "…m'envoyer tes notes avant mardi ?"),
        ("Il faudrait que quelqu'un…", "…écrive à la personne-ressource."),
        ("Je m'occupe de…", "…rédiger le compte rendu et de l'envoyer."),
        ("Si tu ne peux pas, dis-le…", "…avant jeudi, pour qu'on se réorganise."),
    ], corrige=False,
       notes="Exercice oral. Le dernier est le plus utile et le plus rarement dit : "
             "prévoir l'empêchement à l'avance évite le reproche après coup.")

    d.pratique('Organisation', "Votre équipe, aujourd'hui",
               "Une feuille par équipe, à remettre à la fin de la séance.", [
        ("Les noms", "qui est dans l'équipe, et qui manque aujourd'hui"),
        ("Les rôles", "un par personne, et deux si vous n'êtes que trois"),
        ("Le mandat", "trois lignes : ce qu'on cherche, ce qu'on remet, pour quand"),
        ("L'échéancier", "trois dates, une par étape"),
        ("Les rencontres", "quand, où, et combien de temps"),
    ], corrige=False,
       notes="Cœur de la séance. Passer dans les équipes et vérifier une chose : "
             "que le mandat commence par une question, pas par un thème. « Les "
             "arbres » n'est pas un mandat.")

    d.billet(
        "Écrivez le mandat de votre équipe en une seule phrase.",
        exemples=[
            "Commencez par « Nous cherchons… ».",
            "Une question, pas un thème.",
        ],
        notes="Billet de sortie. Ramasser les feuilles et les relire : celles qui "
              "commencent par un thème demandent une reprise en B1, sinon tout le "
              "reste du module portera à faux.")

    return d.save(dossier)
