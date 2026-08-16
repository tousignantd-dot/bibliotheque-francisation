# -*- coding: utf-8 -*-
"""A3 · Les mots de la santé.
Bloc A « Je découvre » · couleur forêt (vocabulaire) · 60 min.
Source du module : exercice `prVocab` et les douze cartes mémoire.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='foret',
        titre='Les mots de la santé',
        chapeau="Douze mots qui reviennent à chaque rendez-vous et à chaque passage à "
                "la pharmacie. Les comprendre à l'oral compte plus que de savoir les "
                "écrire.",
        duree='60 minutes')

    d.titre(notes="Séance de vocabulaire. Les douze mots sont ceux des cartes mémoire du "
                  "module : l'élève les retrouvera chez lui, dans l'activité.")

    d.objectifs([
        "comprendre les douze mots du rendez-vous et de la pharmacie ;",
        "distinguer une ordonnance, une posologie et un traitement ;",
        "employer l'article juste : un comprimé, une ordonnance ;",
        "reconnaître ces mots à l'oral, dites vite.",
    ])

    d.vocabulaire('Vocabulaire · 1 de 2', "Prendre rendez-vous", [
        ("prendre un rendez-vous", "Fixer un moment pour voir un médecin."),
        ("une clinique", "Un endroit où on consulte des médecins."),
        ("la salle d'attente", "L'endroit où on attend avant de voir le médecin."),
        ("Info-Santé (811)", "Un service téléphonique de conseils de santé, jour et nuit."),
        ("la carte d'assurance maladie",
         "Le document qui donne accès aux soins gratuits au Québec."),
        ("une urgence", "Une situation grave qui demande des soins immédiats."),
    ], notes="Faire répéter chaque mot AVEC son article : c'est lui qui porte le genre, "
             "et le genre ne se devine pas.")

    d.vocabulaire('Vocabulaire · 2 de 2', "À la pharmacie", [
        ("une ordonnance", "Le papier du médecin pour acheter des médicaments."),
        ("la posologie", "La façon de prendre un médicament (combien et quand)."),
        ("un comprimé", "Un petit médicament solide à avaler."),
        ("le traitement", "L'ensemble des soins pour guérir."),
        ("un pharmacien", "La personne qui prépare et vend les médicaments."),
        ("se sentir", "Percevoir son état physique ou moral."),
    ], notes="« Posologie » est le mot difficile et le plus utile : il est écrit sur "
             "chaque étiquette de pilulier. Le faire chercher sur une vraie boîte.")

    d.tableau('Analyse', "Trois mots qu'on confond",
              ['Le mot', 'Ce que c\'est exactement'],
              [["une ordonnance", "le papier signé par le médecin"],
               ["la posologie", "combien de comprimés, et quand les prendre"],
               ["le traitement", "toute la durée des soins, du début à la guérison"]],
              cle=0,
              note="Trois choses différentes, souvent dites dans la même phrase.",
              notes="Exemple à donner : « Voici votre ordonnance ; la posologie est "
                    "d'un comprimé deux fois par jour ; le traitement dure sept jours. »")

    d.pratique('Pratique · 1 de 3', "Le mot et sa définition",
               "Associez.", [
        ("Fixer un moment pour voir un médecin.", "prendre un rendez-vous"),
        ("L'endroit où on attend avant de voir le médecin.", "la salle d'attente"),
        ("Le papier du médecin pour acheter des médicaments.", "une ordonnance"),
        ("La façon de prendre un médicament.", "la posologie"),
        ("La personne qui prépare et vend les médicaments.", "un pharmacien"),
        ("Le document qui donne accès aux soins gratuits.", "la carte d'assurance maladie"),
    ], corrige=True,
       notes="C'est l'exercice de vocabulaire du module, dans l'autre sens : ici on part "
             "de la définition. Plus difficile, et plus proche de la vraie compréhension.")

    d.pratique('Pratique · 2 de 3', "Un ou une ?",
               "L'article fait partie du mot.", [
        ("___ ordonnance", "une ordonnance"),
        ("___ comprimé", "un comprimé"),
        ("___ clinique", "une clinique"),
        ("___ pharmacien", "un pharmacien"),
        ("___ urgence", "une urgence"),
        ("___ traitement", "un traitement"),
    ], corrige=True,
       notes="Faire remarquer que les mots en -tion, -ance et -ence sont presque tous "
             "féminins. Une régularité utile, sans en faire une règle absolue.")

    d.pratique('Pratique · 3 de 3', "La phrase du jour",
               "Employez le mot dans une phrase vraie, sur vous.", [
        ("se sentir", "Je me sens fatigué depuis lundi."),
        ("une ordonnance", "J'ai une ordonnance pour mes allergies."),
        ("la salle d'attente", "J'ai attendu une heure dans la salle d'attente."),
        ("Info-Santé", "J'ai appelé Info-Santé pour mon fils."),
    ], corrige=False,
       notes="Quinze minutes à deux. Exiger une phrase VRAIE : le mot se retient par la "
             "situation, pas par la répétition.")

    d.billet(
        "Choisissez les trois mots les plus utiles pour vous, et écrivez pourquoi.",
        exemples=[
            "Un mot par ligne, avec la raison en quelques mots.",
            "Ces trois mots iront dans « Mes mots utiles », à la fin du module.",
        ],
        notes="Ramasser. Ces choix nourrissent la liste personnelle de E2 — le lien "
              "entre les deux séances se dit à voix haute.")

    return d.save(dossier)
