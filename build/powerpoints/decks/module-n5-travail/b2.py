# -*- coding: utf-8 -*-
"""B2 · « Laissez-moi un message »
Bloc B « Défi 1 » · couleur ambre · 75 min. Impératif et place du pronom.
Source : exercice `t1imp`, mini-leçon `t1imp`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre="« Laissez-moi un message »",
        chapeau="Un message d'accueil, une note collée sur un appareil, un "
                "courriel qui demande quelque chose : tous sont faits "
                "d'impératifs. Et le pronom y change de place selon que la "
                "phrase affirme ou nie.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire. Ouvrir en projetant le message d'accueil de B1 et "
                  "en demandant au groupe de souligner les verbes. Il n'y en a que trois, "
                  "et deux sont à l'impératif. C'est le point de départ.")

    d.objectifs([
        "former l'impératif présent aux trois personnes ;",
        "placer le pronom après le verbe dans une phrase affirmative ;",
        "le replacer devant le verbe dans une phrase négative ;",
        "employer deux pronoms à la suite sans se tromper d'ordre.",
    ])

    d.regle("L'impératif n'a jamais de pronom sujet",
            "Trois personnes seulement, et aucun « je », « tu » ou « vous » "
            "devant le verbe.",
            precision="Au travail, c'est presque toujours la forme en « vous » : "
                      "Laissez, Appuyez, Envoyez. La forme en « tu » sert entre "
                      "collègues, la forme en « nous » pour inviter le groupe.",
            notes="Diapositive à photographier. La faute « vous laissez-moi un message » "
                  "vient de langues où le sujet est obligatoire ; la nommer aide.")

    d.tableau('La formation', "On enlève le pronom sujet",
              ['Au présent', 'À l\'impératif'],
              [["vous laissez", "laissez"],
               ["nous laissons", "laissons"],
               ["tu laisses", "laisse — le s tombe"],
               ["tu finis", "finis — le s reste"],
               ["tu rappelles", "rappelle — le s tombe"]],
              cle=1,
              note="Les verbes en « er » perdent leur s à la deuxième personne du "
                   "singulier. Les autres le gardent.",
              notes="Le s revient devant « y » et « en » : vas-y, parles-en. C'est pour "
                    "l'oreille, pas pour la grammaire. Le mentionner sans en faire un "
                    "point d'apprentissage.")

    d.cartes("La place du pronom", "Elle dépend d'une seule chose", [
        ("Phrase affirmative : derrière, avec un trait d'union",
         "Laissez-moi un message. Rappelez-la. Envoyez-le."),
        ("« me » devient « moi », « te » devient « toi »",
         "Dites-moi. Assoyez-vous. Assois-toi."),
        ("Phrase négative : devant, sans trait d'union",
         "Ne me rappelez pas. Ne la faites pas attendre."),
        ("Deux pronoms : l'ordre s'inverse aussi",
         "Donnez-le-moi. Mais : Ne me le donnez pas."),
    ], notes="Retenir la règle par l'image : l'affirmative pousse le pronom derrière ; la "
             "négative, en encadrant le verbe, le ramène devant, à sa place habituelle.")

    d.tableau('Les deux formes', "La même phrase, affirmée puis niée",
              ['Affirmative', 'Négative'],
              [["Laissez-moi un message", "Ne me laissez pas de message"],
               ["Rappelez-la avant midi", "Ne la rappelez pas après midi"],
               ["Envoyez-le à la paie", "Ne l'envoyez pas sans signature"],
               ["Donnez-le-moi aujourd'hui", "Ne me le donnez pas demain"]],
              cle=1,
              notes="Faire lire les paires à voix haute, en alternance, par deux élèves. "
                    "Le déplacement du pronom s'entend, et c'est ainsi qu'il s'apprend : "
                    "par le rythme, pas par la règle.")

    d.piege("Laisser le pronom derrière à la négative",
            "Ne rappelez-la pas avant midi.",
            "Ne la rappelez pas avant midi.",
            "Dès qu'il y a une négation, le pronom revient devant le verbe, sans trait "
            "d'union. C'est la place normale du pronom : celle de « vous la rappelez ».",
            notes="C'est la faute la plus fréquente de la séance, et elle vient de ce "
                  "qu'on apprend d'abord l'affirmative. Faire produire trois négatives à "
                  "partir d'affirmatives données par le groupe.")

    d.pratique('Transformation', "Remplacez les mots soulignés par un pronom",
               "Récrivez la phrase à l'impératif.", [
        ("Vous laissez un message.", "Laissez-le."),
        ("Vous rappelez madame Thériault avant midi.", "Rappelez-la avant midi."),
        ("Vous envoyez le formulaire à la paie.", "Envoyez-le à la paie."),
        ("Vous écoutez les quatre messages ce matin.", "Écoutez-les ce matin."),
        ("Vous ne faites pas attendre la cliente.", "Ne la faites pas attendre."),
        ("Vous ne me rappelez pas après midi.", "Ne me rappelez pas après midi."),
        ("Vous donnez votre numéro à moi.", "Donnez-le-moi."),
        ("Vous n'envoyez pas la note à Ghislain.", "Ne la lui envoyez pas."),
    ], cols=2, corrige=True,
       notes="Les huit énoncés sont ceux de l'exercice interactif. Faire répondre à "
             "l'oral d'abord : le pronom se place mieux quand on l'entend.")

    d.pratique('Production', "Trois consignes à écrire",
               "Écrivez chaque consigne à l'impératif, en « vous ».", [
        ("Demander de laisser un nom et un numéro.", "Laissez-moi votre nom et votre numéro."),
        ("Demander de ne pas rappeler après dix-sept heures.", "Ne me rappelez pas après dix-sept heures."),
        ("Demander de transmettre le message au chef d'équipe.", "Transmettez-le-lui."),
        ("Demander de ne pas envoyer le formulaire sans signature.", "Ne l'envoyez pas sans signature."),
    ], corrige=True,
       notes="Le troisième énoncé est le plus difficile : deux pronoms à la suite. "
             "Accepter aussi « Transmettez le message au chef d'équipe » : l'important "
             "est l'impératif, le double pronom est un bonus.")

    d.billet(
        "Écrivez quatre consignes à l'impératif que vous pourriez coller au mur de "
        "votre travail.",
        exemples=[
            "Deux à l'affirmative, deux à la négative.",
            "Employez un pronom dans au moins deux d'entre elles.",
        ],
        notes="Ces consignes serviront en C4, où l'on comparera l'impératif et l'infinitif "
              "de consigne. Demander aux élèves de garder leur billet.")

    return d.save(dossier)
