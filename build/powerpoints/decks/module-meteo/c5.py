# -*- coding: utf-8 -*-
"""C5 · Futur simple ou conditionnel présent ?
Bloc C · couleur ambre (écriture) · 75 min.
Source : exercice `t2futcond` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C5', section='ambre',
        titre='Futur ou conditionnel ?',
        chapeau="« Je commencerai la toiture lundi » ou « je partirais plus tôt si la "
                "poudrerie le permet » ? Une lettre de différence à l'écrit, et deux "
                "degrés de certitude complètement différents.",
        duree='75 minutes')

    d.titre(notes="Écrire les deux formes au tableau — commencerai, commencerais — et "
                  "les dire à voix haute. Beaucoup n'entendront aucune différence : "
                  "c'est le point de départ.")

    d.objectifs([
        "former le conditionnel présent à la première personne ;",
        "distinguer le futur simple du conditionnel présent ;",
        "employer le conditionnel avec une condition ;",
        "écrire correctement la terminaison qu'on n'entend presque pas.",
    ])

    d.regle('La formation',
            "Futur : infinitif + ai. Conditionnel : infinitif + ais.",
            precision="Je commencerai — le futur. Je commencerais — le conditionnel. "
                      "Une seule lettre les sépare à l'écrit, et le son est très "
                      "proche : c'est ce qui rend la distinction difficile.",
            notes="Écrire les deux formes l'une sous l'autre. La différence tient au s "
                  "final, invisible et presque inaudible.")

    d.tableau('Analyse', "Futur ou conditionnel : le sens",
              ['Le temps', 'Ce qu\'il dit', 'Un exemple'],
              [["futur simple", "ça va arriver, c'est certain", "Lundi, je commencerai la toiture."],
               ["conditionnel", "ça arrivera peut-être, sous condition", "Je partirais plus tôt si la poudrerie le permet."]],
              cle=0,
              note="Le conditionnel va presque toujours avec une condition, exprimée ou "
                   "sous-entendue.",
              notes="Le repère le plus fiable : y a-t-il un « si » dans la phrase, ou "
                    "une condition sous-entendue ? Si oui, conditionnel.")

    d.cartes('En apprendre plus', "Quatre emplois du conditionnel", [
        ("Une action sous condition",
         "« Je prendrais l'autoroute 10 si la visibilité s'améliorait. » C'est "
         "l'emploi principal, et le plus fréquent."),
        ("Une demande polie",
         "« Pourriez-vous vérifier la route ? » C'est le conditionnel du module 2. "
         "Même forme, autre usage."),
        ("Une information non confirmée",
         "« Un nid-de-poule serait à l'origine de l'accident. » C'est le conditionnel "
         "des nouvelles, vu au module 5."),
        ("Un conseil",
         "« À votre place, je partirais plus tard. » Plus doux qu'un ordre, et très "
         "employé entre collègues."),
    ], notes="Le conditionnel n'est pas seulement un temps de la condition. Ces quatre "
             "emplois expliquent pourquoi on l'entend partout.")

    d.pratique('Pratique · 1 de 4', "Futur ou conditionnel ?",
               "Cherchez la condition, exprimée ou sous-entendue.", [
        ("Lundi, je ___ (commencer) la toiture du garage.", "commencerai — c'est certain"),
        ("Je ___ (partir) plus tôt si la poudrerie le permet.", "partirais — sous condition"),
        ("Je ___ (finir) le rapport avant midi, c'est certain.", "finirai"),
        ("Je ___ (prendre) l'autoroute 10 si la visibilité s'améliorait.", "prendrais"),
    ], corrige=True,
       notes="Les deux items avec « si » prennent le conditionnel. Faire chercher le "
             "« si » avant d'écrire : c'est le test.")

    d.pratique('Pratique · 2 de 4', "Formez les deux",
               "Le futur, puis le conditionnel, à la première personne.", [
        ("commencer", "je commencerai · je commencerais"),
        ("partir", "je partirai · je partirais"),
        ("finir", "je finirai · je finirais"),
        ("prendre", "je prendrai · je prendrais"),
        ("être", "je serai · je serais"),
        ("avoir", "j'aurai · j'aurais"),
    ], corrige=True,
       notes="Les deux derniers sont irréguliers au radical, mais les terminaisons ne "
             "changent pas. Le faire remarquer : c'est ce qui rend les deux temps "
             "faciles une fois le radical connu.")

    d.piege("Le piège du s final",
            "Je partirai plus tôt si la poudrerie le permet.",
            "Je partirais plus tôt si la poudrerie le permet.",
            "Avec une condition, il faut le conditionnel : un s à la fin. Le son est "
            "presque identique et personne ne vous corrigera à l'oral. À l'écrit, "
            "l'erreur est visible et elle change le sens : le futur affirme, le "
            "conditionnel suppose.",
            notes="Faire dire les deux formes en alternance. Certains élèves entendront "
                  "la différence, d'autres non : les deux cas sont normaux.")

    d.piege("Le piège du futur après « si »",
            "Si la visibilité s'améliorera, je prendrai la 10.",
            "Si la visibilité s'améliore, je prendrais la 10.",
            "Après « si », jamais de futur ni de conditionnel : le présent ou "
            "l'imparfait. Le conditionnel va dans l'autre moitié de la phrase. C'est la "
            "règle de la séance C4, et elle vaut ici aussi.",
            notes="Relier explicitement à C4. Les deux séances se répondent : la "
                  "condition d'un côté, la conséquence de l'autre.")

    d.pratique('Pratique · 3 de 4', "Complétez la phrase",
               "Conditionnel dans la conséquence, présent après « si ».", [
        ("Si le vent ___ (tomber), je ___ (monter) sur le toit.",
         "tombe · monterais"),
        ("Si l'avertissement ___ (être) levé, je ___ (partir) tout de suite.",
         "est · partirais"),
        ("Si la chaussée ___ (rester) glacée, je ___ (attendre) à l'atelier.",
         "reste · attendrais"),
        ("Lundi matin, je ___ (commencer) le chantier — c'est prévu.", "commencerai"),
    ], corrige=True,
       notes="Le quatrième item n'a pas de condition : c'est le futur. Le contraste avec "
             "les trois autres est ce qui enseigne.")

    d.pratique('Pratique · 4 de 4', "Donnez un conseil",
               "Au conditionnel, à la première personne.", [
        ("Votre collègue veut partir malgré la poudrerie.",
         "À ta place, j'attendrais que le vent faiblisse."),
        ("Il veut monter sur un toit glacé.", "Moi, je ne monterais pas aujourd'hui."),
        ("Il hésite à prévenir le superviseur.", "Je l'appellerais tout de suite."),
        ("Il veut prendre l'autoroute avec 200 mètres de visibilité.",
         "Je prendrais plutôt la route secondaire."),
    ], corrige=True,
       notes="« À ta place, je… » est la formule la plus utile du conditionnel entre "
             "collègues. La faire répéter.")

    d.billet(
        "Écrivez deux phrases : une au futur simple, une au conditionnel.",
        exemples=[
            "Le futur pour quelque chose de certain, le conditionnel avec une condition.",
            "Soulignez la terminaison de chaque verbe.",
        ],
        notes="Corriger les billets en dehors du cours. Le s final demande une "
              "rétroaction individuelle : c'est une lettre, et elle change le sens.")

    return d.save(dossier)
