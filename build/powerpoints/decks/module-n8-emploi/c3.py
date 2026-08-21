# -*- coding: utf-8 -*-
"""C3 · Proposer, nuancer, regretter : les deux conditionnels.
Bloc C « Défi 2 » · couleur ambre · 75 min.
Source : exercice `t2cond` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="Proposer, nuancer, regretter",
        chapeau="« Je veux qu'on partage » se fait répondre non. « Je "
                "proposerais un partage » avance la même idée en laissant à "
                "l'autre la liberté d'y venir — et c'est ce qui la fait passer.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire au service de la diplomatie. Ouvrir en projetant "
                  "les deux phrases du chapeau et en demandant laquelle obtient un oui.")

    d.objectifs([
        "former le conditionnel présent et le conditionnel passé ;",
        "employer le présent pour proposer et demander ;",
        "employer le passé pour le regret et le reproche atténué ;",
        "ne pas confondre -ai et -ais à l'écrit.",
    ], notes="L'objectif 4 est un vrai enjeu de compte rendu : « je proposerai » engage, "
             "« je proposerais » n'engage pas.")

    d.regle("Le conditionnel présent",
            "Le radical du futur, les terminaisons de l'imparfait.",
            precision="proposer- plus -ais donne « je proposerais ». Si vous savez faire "
                      "le futur, vous savez faire le conditionnel : c'est le même "
                      "radical. Les irréguliers sont ceux du futur, et ce sont toujours "
                      "les mêmes : je serais, j'aurais, je ferais, j'irais, je voudrais, "
                      "je pourrais.",
            notes="Diapositive à photographier. Faire conjuguer trois verbes du module : "
                  "proposer, mettre, rester.")

    d.cartes("Le présent : ce qui pourrait être", "Quatre emplois en réunion", [
        ("Proposer", "Je proposerais un partage des commandes."),
        ("Chiffrer une conséquence envisagée", "Ça me ferait deux heures de plus par mois."),
        ("Demander poliment", "Est-ce que vous pourriez chiffrer l'espace d'ici le douze ?"),
        ("Souhaiter", "J'aimerais qu'on tranche à la réunion du seize."),
    ], notes="Faire remarquer que les quatre sont tirées de la réunion de C1. Nadia "
             "emploie le conditionnel quatre fois, et elle obtient que sa proposition "
             "soit étudiée.")

    d.cartes("Le passé : ce qui aurait pu être", "Trois emplois, tous délicats", [
        ("Le regret partagé", "On aurait dû demander leurs délais avant de comparer les prix."),
        ("Le résultat non réalisé", "Il serait resté vingt mille dollars, et non quarante mille."),
        ("L'hypothèse manquée", "Si j'avais lu la page quatre, je vous en aurais parlé avant."),
    ], cols=1,
       notes="« On aurait dû » est le seul reproche qui ne fâche personne : il n'a pas "
             "de sujet accusé. Manon l'accepte immédiatement et reconnaît sa part.")

    d.tableau('Analyse', "Lequel choisir ?",
              ['Ce que vous voulez dire', 'Le temps'],
              [["La chose peut encore arriver", "conditionnel présent"],
               ["La chose ne peut plus arriver", "conditionnel passé"],
               ["C'est décidé, je m'engage", "futur simple, pas de conditionnel"]],
              cle=1,
              note="Test rapide : si c'est encore possible, présent. Si c'est trop tard, passé.",
              notes="Diapositive à photographier. La troisième ligne est celle qui compte "
                    "pour un compte rendu.")

    d.piege("Écrire je proposerai pour une idée",
            "Je proposerai un partage. (dans un compte rendu)",
            "Je proposerais un partage.",
            "Un seul son à l'oral, deux sens à l'écrit. « -ai » est un futur : c'est "
            "décidé, je m'engage. « -ais » est un conditionnel : c'est une idée à "
            "discuter. Dans un compte rendu qui circule, la confusion crée un "
            "engagement que personne n'a pris — et on vous le rappellera dans un mois.",
            notes="Faire écrire les deux formes côte à côte. C'est la seule façon de "
                  "les distinguer, puisque l'oreille ne le fait pas.")

    d.pratique('Grammaire', "Présent ou passé ?",
               "Complétez avec le verbe entre parenthèses.", [
        ("Je ___ (proposer) qu'on partage les commandes.", "proposerais"),
        ("Ça me ___ (faire) deux heures de plus par mois.", "ferait"),
        ("Nous ___ (devoir) demander leurs délais avant de comparer.", "aurions dû"),
        ("Il ___ (rester) vingt mille dollars, et non quarante mille.", "resterait"),
        ("Si j'avais lu la page quatre, je vous en ___ (parler) avant.", "aurais parlé"),
        ("Est-ce que vous ___ (pouvoir) chiffrer l'espace ?", "pourriez"),
        ("On ___ (ne pas devoir) faire circuler la soumission si vite.", "n'aurait pas dû"),
        ("Demain, je ___ (envoyer) la demande de prix. C'est décidé.", "enverrai — futur"),
    ], corrige=True,
       notes="Le dernier item vérifie l'objectif 4. Le corriger en écrivant les deux "
             "formes au tableau.")

    d.pratique('Production', "Adoucissez",
               "Réécrivez la phrase au conditionnel pour qu'elle soit discutable.", [
        ("Je veux qu'on partage les commandes.", "Je proposerais qu'on partage les commandes."),
        ("Vous devez chiffrer l'espace avant le douze.", "Est-ce que vous pourriez chiffrer l'espace avant le douze ?"),
        ("Il faut trancher le seize.", "J'aimerais qu'on tranche le seize."),
        ("Vous avez fait circuler la soumission trop vite.", "On aurait dû prendre le temps de la lire."),
    ], corrige=True,
       notes="La quatrième transformation change de sujet en même temps que de temps : "
             "« vous » devient « on ». C'est ce qui la rend acceptable.")

    d.billet(
        "Écrivez la proposition que vous feriez à votre employeur.",
        exemples=[
            "Une phrase au conditionnel présent.",
            "Une phrase au conditionnel passé qui dit ce qui a manqué.",
        ],
        notes="Ces deux phrases nourrissent la production orale de E1.")

    return d.save(dossier)
