# -*- coding: utf-8 -*-
"""A3 · Où la publicité vous rejoint
Bloc A « Je découvre » · couleur framboise · vocabulaire · 75 min.
Source : exercices `prImg` et `prPieces`, banc de mots de « Je retiens ».
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n7-publicite' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='A3', section='framboise',
        titre="Où la publicité vous rejoint",
        chapeau="Une personne croise plusieurs centaines d'annonces par jour "
                "et n'en remarque presque aucune. Cette séance nomme les "
                "endroits, et les pièces dont une annonce est faite.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire. Elle paraît facile et elle est structurante : "
                  "sans ces mots, le reste du module ne se dit pas.")

    d.objectifs([
        "nommer six lieux et supports où la publicité paraît ;",
        "associer chaque pièce d'une annonce au travail qu'elle fait ;",
        "employer les mots avec leur article et leur genre ;",
        "commencer sa liste de mots pour « Je retiens des mots ».",
    ], notes="Le deuxième objectif est celui qui compte : l'élève doit pouvoir dire "
             "à quoi sert un slogan, pas seulement reconnaître le mot.")

    d.declencheur(
        'Observation', "Combien d'annonces avez-vous vues avant d'arriver ici ?",
        image=IMG + 'boite-aux-lettres.jpg',
        pistes=[
            "Dans la rue, dans l'autobus, dans le métro ?",
            "Dans votre boîte aux lettres, ce matin ?",
            "Sur votre téléphone, avant une vidéo ?",
            "Combien pourriez-vous en nommer, de mémoire ?",
        ],
        notes="Les chiffres annoncés sont toujours très bas, et c'est le point : on "
              "ne remarque pas ce qu'on voit. La répétition travaille sans nous.")

    d.vocabulaire('Vocabulaire · 1 de 3', "Les endroits", [
        ("un abribus", "Le petit abri vitré où l'on attend l'autobus, dont un côté sert de support à des annonces."),
        ("un panneau-réclame", "Le grand panneau installé au bord d'une route pour qu'on le voie en roulant."),
        ("une circulaire", "Le journal de papier plein d'annonces qu'on reçoit chaque semaine sans l'avoir demandé."),
        ("un dépliant", "La feuille pliée en deux ou en trois qu'un commerce remet en main propre ou envoie par la poste."),
        ("une capsule publicitaire", "La très courte annonce enregistrée qu'on entend à la radio ou avant une vidéo."),
        ("l'affichage", "Tout ce qu'un commerce montre à l'extérieur et à l'intérieur pour se faire voir."),
    ], notes="Faire répéter avec l'article. « Panneau-réclame » prend un trait d'union. "
             "« Circulaire » est un nom au Québec, pas un adjectif.")

    d.vocabulaire('Vocabulaire · 2 de 3', "Les pièces d'une annonce", [
        ("un slogan", "La courte phrase qu'une entreprise répète partout pour qu'on la retienne."),
        ("une mention légale", "La partie qu'une loi oblige à donner, et qu'on place toujours à la fin."),
        ("un astérisque", "La petite étoile placée après un prix, qui renvoie à une condition écrite plus bas."),
        ("le débit", "La vitesse à laquelle une personne parle, comptée en mots par minute."),
        ("un rabais", "La somme retranchée du prix habituel pendant une période annoncée."),
        ("un message implicite", "Ce qu'une annonce fait comprendre sans jamais l'écrire ni le dire."),
    ], notes="« Un astérisque » est masculin, et c'est une erreur fréquente. Le faire "
             "dire avec l'article trois fois.")

    d.vocabulaire('Vocabulaire · 3 de 3', "Les personnes et les ententes", [
        ("un annonceur", "L'entreprise ou l'organisme qui paie pour faire passer un message."),
        ("un public cible", "Le groupe de personnes qu'une annonce cherche à atteindre."),
        ("un témoignage", "Le récit d'une personne qui dit ce que le produit a fait pour elle."),
        ("une commandite", "L'entente par laquelle une entreprise paie quelqu'un pour qu'il parle de son produit."),
        ("une publicité déguisée", "Une annonce présentée sous une forme qui cache qu'elle est une annonce."),
        ("un engagement", "La durée minimale pendant laquelle on est tenu de continuer à payer."),
    ], notes="Ces six mots serviront surtout au bloc D. Les poser ici pour que les "
             "élèves les aient entendus une première fois.")

    d.tableau('Analyse', "Chaque pièce a un travail",
              ['La pièce', 'Ce qu\'elle fait'],
              [["Le slogan", "se faire retenir, toujours dans les mêmes mots"],
               ["La mention légale", "dire ce que le reste a passé sous silence"],
               ["L'astérisque", "renvoyer à la condition écrite plus bas"],
               ["Le public cible", "décider de tout : la musique, l'heure, les mots"],
               ["L'annonceur", "payer le message, et en répondre devant la loi"]],
              cle=0,
              note="Une seule de ces pièces existe parce qu'une loi l'exige.",
              notes="Diapositive à photographier. La note est une question : laquelle ? "
                    "Réponse : la mention légale. Personne ne l'ajoute par générosité.")

    d.pratique('Pratique', "Chaque endroit, sa description",
               "Reliez ce qu'on voit à ce qu'on nomme.", [
        ("Un abri vitré éclairé au bord d'une rue enneigée.", "un abribus"),
        ("Une boîte de métal si pleine que le couvercle ne ferme plus.", "une circulaire"),
        ("Un écran allumé dans un salon vide, en fin de soirée.", "un téléviseur"),
        ("Une console, un micro suspendu, une chaise vide.", "un studio de radio"),
        ("Une structure d'acier au bord de l'autoroute.", "un panneau-réclame"),
        ("La devanture éclairée d'un commerce, un soir de pluie.", "l'affichage"),
    ], corrige=True,
       notes="Exercice `prImg` du module, en version projetée. Les six photos sont "
             "dans le module : les faire ouvrir sur les portables si possible.")

    d.billet(
        "Rapportez une circulaire ou un dépliant reçu chez vous cette semaine.",
        exemples=[
            "N'importe lequel, même en partie déchiré.",
            "S'il n'y en a pas, notez le nom d'un commerce vu sur la rue.",
        ],
        notes="Devoir matériel. Ces papiers serviront réellement en C1 : la séance du "
              "dépliant fonctionne beaucoup mieux avec de vrais dépliants sur les "
              "tables.")

    return d.save(dossier)
