# -*- coding: utf-8 -*-
"""A3 · Seize mots et six endroits
Bloc A « Je découvre » · couleur framboise · 75 min. Vocabulaire.
Source : `FC_CARDS` en entier, exercices `prVocab` et `prImg`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='framboise',
        titre="Seize mots et six endroits",
        chapeau="Les mots d'une matinée à l'hôpital, dans l'ordre où on les "
                "rencontre : l'entrée, l'attente, le bureau, l'enveloppe.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire. Les seize mots du module y passent tous. "
                  "Prévoir une pause au milieu : seize mots abstraits en une séance, "
                  "c'est beaucoup, et la fatigue se voit à la douzième.")

    d.objectifs([
        "nommer les quatre groupes de mots du module ;",
        "employer chaque mot avec son article ;",
        "reconnaître les six endroits du parcours d'un rendez-vous ;",
        "distinguer un mot qui décrit d'un mot qui nomme un papier.",
    ], notes="Le quatrième objectif est celui qui structure tout le reste : la "
             "moitié du vocabulaire du module désigne des papiers, l'autre décrit "
             "des états ou des démarches.")

    d.declencheur(
        'Observation', "Refaites de mémoire le parcours de Leyla",
        pistes=[
            "Par où entre-t-elle ? Où va-t-elle ensuite ?",
            "Combien de temps attend-elle, et où ?",
            "Que reçoit-elle en sortant ?",
        ],
        notes="Trois minutes, à deux. Le groupe reconstitue le parcours sans notes : "
              "ce qui manque à leur reconstitution est exactement ce que la séance "
              "doit nommer.")

    d.vocabulaire('Vocabulaire · 1', "Entrer à l'hôpital", [
        ("une clinique externe", "Le service d'un hôpital où l'on est reçu sans y être hospitalisé."),
        ("une demande de consultation", "Le papier par lequel un médecin en fait voir un autre."),
        ("la médecine interne", "La spécialité qui cherche la cause d'un problème touchant tout le corps."),
        ("un délai d'attente", "Le temps entre la demande et le rendez-vous."),
        ("un dossier médical", "Ce qui a été écrit sur vous, et qui vous suit d'un service à l'autre."),
    ], notes="Groupe le plus administratif des quatre. Faire remarquer que trois de "
             "ces cinq mots désignent un papier ou un ensemble de papiers.")

    d.vocabulaire('Vocabulaire · 2', "L'attente, et ce qu'on s'y dit", [
        ("un malaise", "Un dérangement du corps qu'on sent sans pouvoir le montrer du doigt."),
        ("la fatigue chronique", "Une fatigue qui dure des mois et que le repos ne fait pas partir."),
        ("un proche aidant", "Celui qui accompagne quelqu'un de sa famille sans être payé pour ça."),
        ("les heures de visite", "Les moments où l'on a le droit d'entrer voir quelqu'un d'hospitalisé."),
    ], notes="« Un proche aidant » est un mot que plusieurs élèves sont sans le "
             "savoir. Le leur dire : la reconnaissance du mot vaut souvent plus que "
             "le mot lui-même.")

    d.vocabulaire('Vocabulaire · 3', "Dans le bureau", [
        ("un antécédent", "Un évènement de santé déjà arrivé, qu'on redit à chaque nouveau médecin."),
        ("un prélèvement", "Le peu de sang ou de liquide qu'on prend pour le faire analyser."),
        ("un diagnostic", "Le nom donné à un problème une fois qu'on a assez vérifié pour l'écrire."),
        ("une anémie", "Un résultat d'analyse : le sang transporte l'oxygène moins bien qu'il le devrait."),
    ], notes="Insister sur « un diagnostic » : c'est le mot autour duquel tourne tout "
             "le Défi 2. Un diagnostic se mérite à force de vérifier ; on ne le "
             "choisit pas.")

    d.vocabulaire('Vocabulaire · 4', "Ce qui s'écrit après", [
        ("les effets secondaires", "Ce qu'un traitement fait en plus de ce qu'on lui demande."),
        ("un feuillet d'information", "La feuille remise en sortant, qui explique la marche à suivre."),
        ("un suivi", "Ce qui est prévu après : qui rappelle, quand, et ce qu'il faut avoir fait."),
    ], notes="Trois mots seulement, et ce sont ceux du Défi 3. Annoncer que le "
             "feuillet et le compte rendu seront lus en entier dans deux semaines.")

    d.tableau('Analyse', "Deux sortes de mots dans ce module",
              ['La sorte', 'Ce qu\'on en fait'],
              [["Un papier", "on le demande, on l'apporte, on le garde, on l'annote"],
               ["Un état", "on le décrit, on le date, on le compare à avant"],
               ["Une démarche", "on la suit, on en note les étapes et les délais"]],
              cle=0,
              note="Un mot mal rangé se retient mal : demander un état ou décrire un papier ne veut rien dire.",
              notes="Diapositive à photographier. Faire ranger les seize mots dans "
                    "les trois colonnes, oralement, à main levée.")

    d.pratique('Vocabulaire', "Le mot juste",
               "Complétez avec un mot du module.", [
        ("Le service où l'on est reçu sans être hospitalisé.", "une clinique externe"),
        ("Le papier envoyé par le médecin de famille.", "une demande de consultation"),
        ("Une fatigue de plusieurs mois que le repos ne répare pas.", "la fatigue chronique"),
        ("Celui qui accompagne sans être payé ni formé.", "un proche aidant"),
        ("Ce qu'on prend sur vous pour le faire analyser.", "un prélèvement"),
        ("La feuille qui explique la marche à suivre.", "un feuillet d'information"),
    ], corrige=True,
       notes="Faire répondre à l'oral avec l'article. Un mot donné sans son article "
             "compte comme à moitié su : c'est là-dessus qu'on butera à l'écrit.")

    d.billet(
        "Lequel de ces seize mots existe dans votre première langue ?",
        exemples=[
            "Un mot suffit, avec sa traduction si vous voulez.",
            "Est-ce qu'il veut dire exactement la même chose ?",
        ],
        notes="Deux minutes. La question fait travailler la nuance plutôt que la "
              "traduction : plusieurs de ces mots existent ailleurs et ne couvrent "
              "pas exactement la même réalité.")

    return d.save(dossier)
