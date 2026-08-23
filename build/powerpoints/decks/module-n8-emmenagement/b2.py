# -*- coding: utf-8 -*-
"""B2 · Les six mots qui décident d'une police
Bloc B « Défi 1 · Ce qui est couvert » · couleur framboise · 75 min.
Vocabulaire. Source du module : `FC_CARDS` (t1) et le bloc `savoir` de `t11`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='framboise',
        titre="Les six mots qui décident d'une police",
        chapeau="Prime, franchise, plafond, sous-limite, avenant, exclusion. "
                "Six mots, et ils décident à eux seuls de ce que vous "
                "toucherez.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire, mais chaque mot se traduit ici en "
                  "un calcul ou une conséquence. Ne pas s'arrêter à la "
                  "définition : faire faire les soustractions.")

    d.objectifs([
        "nommer les six mots d'une police et ce que chacun engage ;",
        "calculer une indemnité : dommage retenu moins franchise ;",
        "distinguer un plafond d'une sous-limite ;",
        "expliquer pourquoi on lit les exclusions en premier.",
    ], notes="Le deuxième objectif est celui qui surprend le plus : beaucoup "
             "d'élèves croient qu'assuré veut dire remboursé en entier.")

    d.declencheur(
        'Pour commencer', "Un dégât de 940 $, une franchise de 500 $. Combien "
                          "recevez-vous ?",
        pistes=[
            "Et si le dégât était de 400 $ ?",
            "Trois objets abîmés dans le même dégât d'eau : la franchise s'applique combien de fois ?",
            "Pourquoi une franchise plus haute fait-elle baisser le prix ?",
        ],
        notes="Faire calculer de tête, à main levée. La deuxième piste est "
              "celle qui étonne : sous une franchise de 500 $, un dommage de "
              "400 $ ne se réclame pas du tout.")

    d.vocabulaire('Vocabulaire', 'Six mots, six effets', [
        ("une prime", "Ce qu'on paie par année, quoi qu'il arrive."),
        ("une franchise", "La part qui reste toujours à sa charge, une fois par sinistre."),
        ("un plafond", "Le maximum que l'assureur versera — jamais une promesse."),
        ("une sous-limite", "Un plafond particulier caché sous le plafond général."),
        ("un avenant", "Une protection ajoutée par écrit à un contrat qui ne l'offrait pas."),
        ("une exclusion", "Un cas annoncé d'avance comme non couvert."),
    ], notes="Faire répéter avec l'article. Opposer avenant et exclusion en "
             "une phrase : l'un ajoute, l'autre retire.")

    d.tableau('Analyse', "Trois protections dans un seul contrat",
              ['La section', 'Ce qu\'elle paie'],
              [["Vos biens", "ce qui vous appartient, jusqu'à 50 000 $, franchise de 500 $"],
               ["Votre responsabilité civile", "ce que vous faites subir aux autres, jusqu'à 2 000 000 $, sans franchise"],
               ["Vos frais de subsistance", "le supplément de logement si l'appartement devient inhabitable"]],
              cle=0,
              note="Une réclamation refusée sous une section peut parfois être présentée sous une autre.",
              notes="Diapositive à photographier. La note du bas est le "
                    "premier réflexe à avoir devant un refus, et personne ne "
                    "l'a spontanément.")

    d.regle("Un plafond n'est pas une promesse",
            "« Jusqu'à cinquante mille dollars » veut dire qu'on ne dépassera pas ce montant, pas qu'on le versera.",
            precision="Ce que vous toucherez dépend de trois choses, dans cet "
                      "ordre : ce que votre inventaire démontre, le mode "
                      "d'indemnisation, puis la franchise.",
            notes="Diapositive à photographier. Faire faire l'exercice une "
                  "fois dans sa vie : estimer ce que coûterait de tout "
                  "racheter neuf. La plupart des gens sous-estiment de "
                  "moitié.")

    d.cartes('Attention', "Valeur à neuf ou valeur au jour du sinistre ?", [
        ("Valeur au jour du sinistre", "on retranche l'âge : un téléviseur de huit ans vaut presque rien."),
        ("Valeur à neuf", "on paie l'équivalent neuf, souvent sur preuve de remplacement."),
        ("L'écart", "il peut atteindre les trois quarts du montant sur un appareil de huit ans."),
        ("Où c'est écrit", "une seule ligne, au bas d'un bloc du sommaire. C'est celle que personne ne lit."),
    ], cols=2,
       notes="« Sur présentation d'une preuve de remplacement » veut dire "
             "qu'on verse d'abord la valeur au jour du sinistre, et le "
             "complément une fois le bien racheté. Le préciser : la surprise "
             "est désagréable au mauvais moment.")

    d.pratique('Pratique', "Le mot et son effet",
               "Reliez chaque mot à ce qu'il change pour vous.", [
        ("une prime", "ce qu'on paie par année, quoi qu'il arrive"),
        ("une franchise", "ce qui se soustrait à chaque sinistre"),
        ("un plafond", "le maximum versé, jamais une promesse"),
        ("une sous-limite", "un plafond caché sous le plafond général"),
        ("un avenant", "une protection ajoutée par écrit"),
        ("une exclusion", "un cas annoncé d'avance comme non couvert"),
    ], corrige=True, cols=1,
       notes="Version projetée du banc de vocabulaire du défi 1. Après la "
             "correction, redemander le calcul du déclencheur : 940 moins "
             "500. La répétition est le but.")

    d.billet(
        "Nomme un objet chez toi qui dépasse probablement sa sous-limite.",
        exemples=[
            "Bijoux, argent comptant, vélo, instrument de musique, objet d'art.",
            "Une phrase : l'objet, et ce que tu vas faire à ce sujet.",
        ],
        notes="Trois minutes. La bonne réponse à « ce que je vais faire » est "
              "toujours la même : appeler et demander un avenant. Le dire à "
              "voix haute avant de sortir.")

    return d.save(dossier)
