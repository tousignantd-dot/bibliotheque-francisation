# -*- coding: utf-8 -*-
"""A3 · Les seize mots du dossier
Bloc A « Je découvre » · couleur framboise (vocabulaire) · 75 min.
Source du module : `FC_CARDS`, exercices `prVocab` et `prImg`.
"""
import pathlib

from theme import Deck

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n7-emploi' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='A3', section='framboise',
        titre="Les seize mots du dossier",
        chapeau="Un projet se présente avec les mots du métier, pas avec des "
                "périphrases. Seize mots suffisent pour tout le module : "
                "quatre pour la réunion, quatre pour la présentation, quatre "
                "pour le poste de travail, quatre pour les écrits.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire. Le banc du module en compte seize, répartis "
                  "sur les quatre sections. Les donner tous aujourd'hui : ils "
                  "reviendront en contexte à chaque bloc, et l'élève doit les avoir "
                  "entendus une première fois avant de les rencontrer dans un dialogue.")

    d.objectifs([
        "reconnaître et employer les seize mots du dossier ;",
        "distinguer un correctif d'une conséquence, une échéance d'un échéancier ;",
        "associer un mot à la photo de ce qu'il désigne ;",
        "employer l'article juste devant chacun.",
    ], notes="Le deuxième objectif vise les deux confusions certaines du module. Les "
             "traiter frontalement plutôt que d'attendre qu'elles se produisent.")

    d.declencheur(
        'Observation', "Que voyez-vous sur cette photo ?",
        image=IMG + 'quai-expedition.jpg',
        pistes=[
            "Où est-ce qu'on est ? Qu'est-ce qui se passe ici ?",
            "Qui travaille là, et à quoi ?",
            "Avez-vous déjà travaillé dans un endroit comme celui-là ?",
            "Quels mots vous manquent pour le décrire ?",
        ],
        notes="Faire décrire librement pendant cinq minutes. Noter au tableau les mots "
              "que le groupe cherche : ce sont ceux de la séance, et les voir arriver "
              "par manque plutôt que par liste change tout.")

    d.vocabulaire('Vocabulaire · 1 de 4', "Le projet et la réunion", [
        ("un projet", "Ce qu'on veut faire, avec les étapes, le coût et la date qui vont avec."),
        ("une évaluation sommaire", "Un premier examen rapide, qui donne des ordres de grandeur."),
        ("un ordre du jour", "La liste écrite des points dont une réunion va traiter, dans l'ordre."),
        ("une réunion de production", "La rencontre régulière où l'équipe fait le point sur le travail."),
    ], notes="Faire répéter avec l'article. « Ordre du jour » se dit aussi pour une "
             "assemblée de copropriété ou un conseil d'école : donner ces exemples.")

    d.vocabulaire('Vocabulaire · 2 de 4', "Présenter et planifier", [
        ("un échéancier", "Le calendrier d'un projet : ce qui se fait, et à quelle date."),
        ("une étape", "Un des moments d'un travail, qui vient après le précédent."),
        ("la mise en oeuvre", "Le moment où l'on passe du plan au travail réel, sur le terrain."),
        ("un budget", "L'argent prévu pour faire quelque chose, avant de le dépenser."),
    ], notes="Distinguer « échéance » (la date) et « échéancier » (le calendrier "
             "complet). C'est la première des deux confusions annoncées.")

    d.vocabulaire('Vocabulaire · 3 de 4', "Le poste de travail", [
        ("la manutention", "Le fait de déplacer des charges à la main : soulever, porter, déposer."),
        ("un poste de travail", "L'endroit précis où une personne fait sa tâche, avec ce qu'il y a autour."),
        ("un correctif", "Le changement qu'on apporte pour régler un problème constaté."),
        ("un programme de prévention", "Le document où un employeur écrit les dangers et ce qu'il fait pour les enlever."),
    ], notes="« Correctif » contre « conséquence » : la seconde confusion. Le correctif "
             "vient après, la conséquence vient du problème. Faire donner un exemple "
             "de chaque par un élève.")

    d.vocabulaire('Vocabulaire · 4 de 4', "Les écrits d'affaires", [
        ("une soumission", "Le prix écrit qu'un fournisseur propose pour un travail précis."),
        ("un fournisseur", "L'entreprise qui vend à une autre entreprise ce dont elle a besoin."),
        ("une note de service", "Un court texte officiel qui informe le personnel d'une entreprise."),
        ("un accusé de réception", "Le mot par lequel on confirme qu'on a bien reçu une lettre."),
    ], notes="Ces quatre-là ne serviront qu'au bloc D. Les donner quand même "
             "aujourd'hui : l'élève les reverra trois fois d'ici là, ce qui vaut mieux "
             "qu'une seule fois au moment où il en a besoin.")

    d.tableau('Analyse', "Deux couples qui se confondent",
              ['Ne pas confondre', 'La différence'],
              [["échéance / échéancier", "l'échéance est UNE date ; l'échéancier est le calendrier entier"],
               ["correctif / conséquence", "le correctif est ce qu'on fait ; la conséquence est ce que le problème coûte"],
               ["soumission / commande", "la soumission est un prix proposé ; la commande engage à acheter"],
               ["note / lettre", "la note reste dans l'entreprise ; la lettre en sort et l'engage"]],
              cle=0,
              note="Les deux derniers couples reviendront au bloc D, et le troisième coûte de l'argent quand on se trompe.",
              notes="Diapositive à photographier. Le couple soumission / commande est "
                    "celui qui a des conséquences réelles : monsieur Cormier y revient "
                    "au dialogue du Défi 2.")

    d.pratique('Pratique', "Le mot juste",
               "Complétez avec un mot de la liste.", [
        ("Le calendrier complet du projet s'appelle un ...", "échéancier"),
        ("Le prix écrit que le fournisseur propose est une ...", "soumission"),
        ("Déplacer des charges à la main, c'est de la ...", "manutention"),
        ("Le changement qu'on propose pour régler le problème est un ...", "correctif"),
        ("Le document où l'employeur écrit les dangers est le ... de prévention", "programme"),
        ("La liste des points d'une réunion est l'...", "ordre du jour"),
    ], corrige=True,
       notes="C'est la forme papier de l'exercice `prVocab` du module. Faire répondre "
             "à l'oral d'abord, puis ouvrir le module pour la version à glisser.")

    d.pratique('Pratique', "Six photos, six phrases",
               "De quelle photo chaque phrase parle-t-elle ?", [
        ("Les caisses vides attendent au sol, sur une palette.", "le poste 4"),
        ("Le plateau garde la palette toujours à la même hauteur.", "la table élévatrice"),
        ("Les camions se présentent ici pour charger.", "le quai d'expédition"),
        ("On s'y réunit le lundi matin, à huit heures.", "la salle de réunion"),
        ("Les résultats des relevés y seront affichés.", "le babillard de la cafétéria"),
        ("On le pousse à la main dans l'allée, fourches sous la palette.", "le transpalette"),
    ], corrige=True,
       notes="C'est la forme papier de l'exercice `prImg` du module. Faire répondre à "
             "l'oral, puis ouvrir le module pour la version à glisser. Le transpalette "
             "et la table élévatrice se confondent pour qui n'a jamais travaillé en "
             "entrepôt : montrer les deux photos côte à côte.")

    d.billet(
        "Choisissez quatre mots de la liste et écrivez une phrase avec chacun.",
        exemples=[
            "Une phrase qui parle de votre travail, ou du poste 4.",
            "Vérifiez l'article : un, une, la, le.",
        ],
        notes="Ramasser et corriger seulement l'article et l'emploi du mot, pas le "
              "reste : c'est un devoir de vocabulaire.")

    return d.save(dossier)
