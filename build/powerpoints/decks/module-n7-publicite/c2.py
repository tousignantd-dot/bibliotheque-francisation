# -*- coding: utf-8 -*-
"""C2 · Qui a été effacé de la phrase ?
Bloc C « Défi 2 » · couleur ambre · 75 min.
Source : exercice `t2efface`, mini-leçon `t2efface`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Qui a été effacé de la phrase ?",
        chapeau="« Des frais sont exigibles. » Quelqu'un les exige, mais ce "
                "quelqu'un n'apparaît nulle part. Les conditions écrites sont "
                "faites de ces phrases-là.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire, et la plus utile du Défi 2. La phrase passive "
                  "sans agent est ce qui rend une condition écrite si difficile à "
                  "lire — et si difficile à contester.")

    d.objectifs([
        "reconnaître une phrase passive à son auxiliaire et à son accord ;",
        "retrouver l'auteur que la phrase n'a pas nommé ;",
        "récrire une phrase passive à l'actif ;",
        "savoir que le passif n'est pas suspect en soi.",
    ], notes="Le quatrième objectif évite la chasse aux sorcières : « le magasin a "
             "été construit en 1998 » n'efface personne d'important.")

    d.declencheur(
        'Observation', "Qui agit dans ces trois phrases ?",
        pistes=[
            "« Des frais d'adhésion sont exigibles à la signature. »",
            "« Le tarif hebdomadaire est prélevé aux quatre semaines. »",
            "« L'offre peut être modifiée sans préavis. »",
            "Quelle impression donnent ces trois phrases ensemble ?",
        ],
        notes="La réponse à la quatrième est presque toujours la bonne : ça arrive "
              "tout seul, comme la pluie. Personne n'agit, donc personne n'est "
              "responsable, donc il n'y a personne à qui se plaindre.")

    d.regle("Être + participe passé accordé avec le sujet",
            "Le centre prélève le tarif. Le tarif est prélevé par le "
            "centre. Le tarif est prélevé.",
            precision="Le complément devient sujet ; le sujet passe derrière « par », "
                      "ou disparaît. Dans les conditions écrites, il disparaît presque "
                      "toujours — et ce n'est pas un oubli de rédaction.",
            notes="Diapositive à photographier. Faire les trois étapes au tableau avec "
                  "une phrase proposée par le groupe.")

    d.tableau('Analyse', "L'accord trahit le passif",
              ['La phrase', 'Ce qui s\'accorde'],
              [["Le tarif est prélevé.", "masculin singulier"],
               ["L'offre est modifiée.", "féminin singulier"],
               ["Les conditions ont été changées.", "féminin pluriel"],
               ["Les frais seront facturés.", "masculin pluriel"]],
              cle=0,
              note="Le participe s'accorde toujours avec le sujet, jamais avec l'agent.",
              notes="Diapositive à photographier. C'est le signe le plus sûr qu'on est "
                    "au passif, et il est visible à l'œil nu.")

    d.cartes('Analyse', "Plus il y a d'auxiliaires, plus l'auteur est loin", [
        ("Présent", "Le tarif est prélevé."),
        ("Passé composé", "Le prix a été augmenté le premier mars."),
        ("Futur simple", "Ce montant vous sera facturé en avril."),
        ("Avec un modal", "L'offre peut être modifiée sans préavis."),
    ], cols=1,
       notes="Les quatre formes se rencontrent dans un seul contrat. Faire chercher "
             "l'auteur à chaque fois : il n'est jamais là.")

    d.pratique('Pratique', "Récrivez à l'actif",
               "Remettez l'auteur donné entre parenthèses comme sujet.", [
        ("Des frais sont exigibles à la signature. (le centre)", "Le centre exige des frais à la signature."),
        ("Le tarif est prélevé aux quatre semaines. (le centre)", "Le centre prélève le tarif aux quatre semaines."),
        ("L'offre peut être modifiée sans préavis. (l'annonceur)", "L'annonceur peut modifier l'offre sans préavis."),
        ("Le prix a été augmenté le premier mars. (la direction)", "La direction a augmenté le prix le premier mars."),
        ("Les conditions ont été changées en janvier. (l'entreprise)", "L'entreprise a changé les conditions en janvier."),
        ("Aucun remboursement n'est accordé après trente jours. (le centre)", "Le centre n'accorde aucun remboursement après trente jours."),
    ], corrige=True,
       notes="Exercice `t2efface` du module. Après correction, faire relire les deux "
             "colonnes à voix haute : la colonne de droite est nettement plus "
             "engageante pour l'entreprise, et c'est tout le point.")

    d.piege('Grammaire',
            "« elle est partie sans signer » est une phrase passive",
            "ce n'en est pas une : on ne peut pas ajouter « par quelqu'un »",
            "Le test est simple et il ne se trompe jamais. « Le contrat est "
            "signé par quelqu'un » se dit ; « elle est partie par quelqu'un » "
            "ne se dit pas. La première est un passif, la seconde un passé "
            "composé avec l'auxiliaire être.",
            notes="Confusion très fréquente, et la seule qui empêche de repérer les "
                  "vrais passifs. Le test tient en trois mots : « par quelqu'un ? »")

    d.billet(
        "Sur votre dépliant, trouvez une phrase passive et écrivez qui a été effacé.",
        exemples=[
            "Recopiez la phrase, puis écrivez le nom en marge.",
            "Si vous n'arrivez pas à le nommer, écrivez la question à poser.",
        ],
        notes="Devoir de lecture active. La seconde consigne est le vrai exercice : "
              "une question à poser au téléphone vaut mieux qu'une réponse devinée.")

    return d.save(dossier)
