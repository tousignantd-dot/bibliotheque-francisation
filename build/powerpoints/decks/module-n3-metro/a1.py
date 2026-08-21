# -*- coding: utf-8 -*-
"""A1 · La carte que j'ai dans ma poche.
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="La carte que j'ai dans ma poche",
        chapeau="Une carte qui dure des années, et des titres qu'on met "
                "dessus. Beaucoup de gens paient trop cher pendant des mois "
                "faute d'avoir demandé.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Demander au groupe qui prend l'autobus ou le "
                  "métro pour venir au centre, et ce que chacun achète comme titre. La "
                  "plupart répondront « un billet » ou « une passe » sans savoir qu'il "
                  "existe quatre ou cinq titres différents. C'est exactement la situation "
                  "de Rosario, et c'est la découverte de la séance.")

    d.objectifs([
        "distinguer la carte de transport et le titre qu'on met dessus ;",
        "nommer les quatre choses de la station : la carte, le titre, le passage, le point de service ;",
        "comprendre qu'un même trajet peut se payer de plusieurs façons ;",
        "savoir où aller pour se renseigner sur les prix.",
    ])

    d.declencheur(
        'Observation', "Combien payez-vous par mois pour vous déplacer ?",
        pistes=[
            "Qu'est-ce que vous achetez : un billet, une carte, autre chose ?",
            "Est-ce que vous achetez la même chose chaque semaine ?",
            "Combien de fois par semaine prenez-vous l'autobus ou le métro ?",
            "Qui vous a expliqué comment ça marche, en arrivant ?",
        ],
        notes="Laisser venir les réponses dans n'importe quelle langue, puis les traduire "
              "ensemble au tableau. Écrire les montants au tableau sans commenter : la "
              "comparaison viendra d'elle-même au bloc B. Personne n'a besoin de savoir "
              "encore ce qu'est le bon prix.")

    d.dialogue('Dialogue · 1 de 3', "Tu paies trop cher, Rosario", [
        ("MAXIME", "Rosario, tu achètes encore un dix passages ce matin ?", True),
        ("ROSARIO", "Oui. Trente-cinq dollars. Je fais ça chaque semaine depuis septembre.", True),
        ("MAXIME", "Chaque semaine ? Tu paies beaucoup trop cher.", True),
        ("ROSARIO", "Pourquoi ? Dix passages, c'est dix voyages. C'est simple.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire remarquer que Rosario n'a rien fait de mal : son calcul est juste, "
             "mais il est incomplet. C'est le raisonnement de presque tout le monde en "
             "arrivant. Ne pas donner la réponse encore.")

    d.dialogue('Dialogue · 2 de 3', "Et le samedi ?", [
        ("MAXIME", "Oui, mais tu viens à l'école cinq matins et tu retournes cinq soirs.", True),
        ("ROSARIO", "Ça fait dix. C'est correct, non ?", True),
        ("MAXIME", "Et le samedi ? Et l'épicerie ? Tu achètes un deuxième dix passages.", True),
        ("ROSARIO", "C'est vrai. Des fois, j'en achète deux dans la même semaine.", True),
    ], notes="C'est le cœur du problème : dix passages couvrent l'aller-retour de cinq "
             "jours, et rien d'autre. Faire compter au tableau les déplacements réels "
             "d'une semaine ordinaire d'un élève volontaire.")

    d.dialogue('Dialogue · 3 de 3', "Un seul prix pour tout le mois", [
        ("MAXIME", "Alors regarde ta carte. C'est une carte OPUS ?", True),
        ("ROSARIO", "Je pense que oui. C'est la carte bleue et blanche.", True),
        ("MAXIME", "Sur une carte OPUS, tu peux mettre un titre mensuel. Un seul prix pour tout le mois.", True),
        ("ROSARIO", "Un mois complet ? Et je peux prendre le métro et l'autobus ?", True),
        ("MAXIME", "Va au point de service de la station. Demande-leur.", True),
    ], notes="Maxime ne donne pas le prix : il envoie Rosario se renseigner. C'est ce que "
             "le module apprend à faire, et c'est tout le bloc B. Insister sur le verbe "
             "« se renseigner », qui est dans le lexique du programme.")

    d.tableau('Analyse', "La carte, le titre, le passage",
              ["Le mot", "Ce que c'est"],
              [["une carte OPUS", "la carte de plastique, gardée des années"],
               ["un titre de transport", "ce qu'on achète et qu'on met sur la carte"],
               ["un passage", "un seul voyage, d'un point à un autre"],
               ["le point de service", "le comptoir de la station, où on vend et on explique"]],
              cle=1,
              note="La carte ne se jette pas : on la recharge.",
              notes="Diapositive à photographier. La confusion carte / titre est la plus "
                    "fréquente et elle coûte de l'argent : un élève qui croit que la carte "
                    "est le titre en rachète une chaque mois. Faire répéter la note.")

    d.regle("Ce qu'il faut savoir avant d'acheter",
            "« Combien de fois par semaine est-ce que je me déplace ? »",
            precision="C'est la première question qu'on vous posera au comptoir, "
                      "et c'est elle qui décide du titre. Cinq jours aller-retour, "
                      "ce n'est pas dix déplacements par mois : c'est plus de "
                      "quarante.",
            notes="Diapositive à photographier. Demander à chacun de répondre pour "
                  "lui-même, à voix haute, en une phrase complète. C'est la phrase du "
                  "billet de sortie.")

    d.cartes("Les mots de la station", "Quatre mots", [
        ("une carte OPUS",
         "La carte de plastique bleue et blanche. Elle sert des années et elle ne "
         "contient rien par elle-même : c'est le titre qu'on met dessus qui donne "
         "le droit de monter."),
        ("un titre de transport",
         "Ce qu'on achète : un passage, dix passages, une semaine, un mois. Il "
         "s'ajoute sur la carte, et il a une durée."),
        ("un passage",
         "Un seul déplacement, d'un point à un autre. Il comprend le droit de "
         "changer de véhicule pendant deux heures."),
        ("le point de service",
         "Le comptoir de la station, avec une personne derrière la vitre. On y "
         "achète ses titres et on peut y poser toutes ses questions."),
    ], notes="Faire dire chaque mot avec son article. Les quatre reviennent dans les "
             "seize séances du module.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Rosario achète un titre de dix passages chaque semaine.", "vrai"),
        ("Elle vient au centre cinq matins par semaine.", "vrai"),
        ("Maxime dit qu'elle paie le bon prix.", "faux — il dit qu'elle paie trop cher"),
        ("Un titre mensuel est bon pour une semaine.", "faux — pour tout le mois"),
        ("Maxime lui dit d'aller au point de service.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte du dialogue.")

    d.billet(
        "Écrivez combien de fois par semaine vous vous déplacez, et ce que vous payez.",
        exemples=[
            "Je me déplace ___ fois par semaine.",
            "J'achète ___ et je paie ___ dollars.",
        ],
        notes="Devoir court. Les réponses servent au bloc B : chacun comparera son "
              "propre montant à la grille des tarifs. Ramasser les billets et les "
              "garder pour la séance B1.")

    return d.save(dossier)
