# -*- coding: utf-8 -*-
"""E2 · Je retiens des mots.
Bloc E « Je me lance » · couleur forêt (vocabulaire et bilan) · 60 min.
Source du module : section `retiens` — les douze cartes mémoire, les quatre listes
personnelles et l'autoévaluation en cinq énoncés.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre='Je retiens des mots',
        chapeau="Dernière séance : on range le vocabulaire par usage, on refait les "
                "cartes mémoire, et chacun dit où il en est.",
        duree='60 minutes')

    d.titre(notes="Séance de bilan. Rendre tous les billets du module : ils forment déjà "
                  "le carnet personnel de chacun.")

    d.objectifs([
        "classer le vocabulaire par situation d'usage ;",
        "réviser les douze mots avec les cartes mémoire ;",
        "dire ce qu'on sait faire, et ce qui reste difficile ;",
        "savoir où retrouver ces mots après le cours.",
    ])

    d.tableau('Bilan', "Quatre listes, quatre moments",
              ['La situation', 'Les mots à y ranger'],
              [["se présenter au téléphone", "je m'appelle, je suis déjà venu, la clinique"],
               ["décrire comment on se sent", "je me sens, j'ai mal à, depuis, très"],
               ["demander un rendez-vous", "j'ai besoin de, est-ce que, je vais être libre"],
               ["comprendre le pharmacien", "une ordonnance, la posologie, un comprimé, "
                                            "le traitement"]],
              cle=0,
              notes="Ce sont les quatre listes de l'activité. Les faire remplir dans le "
                    "module, pas sur papier : elles y restent d'une session à l'autre.")

    d.vocabulaire('Révision · 1 de 2', "Les mots du rendez-vous", [
        ("prendre un rendez-vous", "Fixer un moment pour voir un médecin."),
        ("une clinique", "Un endroit où on consulte des médecins."),
        ("la salle d'attente", "L'endroit où on attend avant de voir le médecin."),
        ("Info-Santé (811)", "Un service téléphonique de conseils, jour et nuit."),
        ("la carte d'assurance maladie", "Le document qui donne accès aux soins gratuits."),
        ("une urgence", "Une situation grave qui demande des soins immédiats."),
    ], notes="Révision rapide : cacher la colonne de droite, faire redire la définition "
             "de mémoire. Cinq minutes, pas plus.")

    d.vocabulaire('Révision · 2 de 2', "Les mots de la pharmacie", [
        ("une ordonnance", "Le papier du médecin pour acheter des médicaments."),
        ("la posologie", "La façon de prendre un médicament."),
        ("un comprimé", "Un petit médicament solide à avaler."),
        ("le traitement", "L'ensemble des soins pour guérir."),
        ("un pharmacien", "La personne qui prépare et vend les médicaments."),
        ("se sentir", "Percevoir son état physique ou moral."),
    ], notes="Même chose dans l'autre sens : donner la définition, faire retrouver le "
             "mot avec son article.")

    d.pratique('Pratique · 1 de 3', "Les cartes mémoire",
               "Dans l'activité : « Je retiens des mots », puis les cartes.", [
        ("Étape 1", "passez les douze cartes une fois, sans vous arrêter"),
        ("Étape 2", "mettez de côté celles que vous savez"),
        ("Étape 3", "refaites seulement les autres, deux fois"),
        ("Étape 4", "traduisez dans votre langue celles qui résistent"),
    ], corrige=False,
       notes="Quinze minutes. L'étape 4 emploie le bouton « Traduire » des cartes : le "
             "montrer une fois au tableau, beaucoup ne l'ont pas remarqué.")

    d.pratique('Pratique · 2 de 3', "Le mot juste",
               "Complétez avec le bon mot du module.", [
        ("Le médecin me donne une ___ pour la pharmacie.", "ordonnance"),
        ("La ___ est écrite sur l'étiquette : un comprimé, deux fois par jour.",
         "posologie"),
        ("J'attends dans la ___ depuis vingt minutes.", "salle d'attente"),
        ("N'oubliez pas votre ___ à chaque visite.", "carte d'assurance maladie"),
        ("J'appelle ___ la nuit quand je ne sais pas quoi faire.", "Info-Santé (811)"),
    ], corrige=True,
       notes="Cinq phrases, cinq situations différentes. C'est le contrôle de "
             "compréhension le plus rapide du module.")

    d.pratique('Pratique · 3 de 3', "Qu'est-ce que je suis capable de faire ?",
               "Pour chaque énoncé : pas encore · un peu · oui.", [
        ("Je sais où m'adresser selon mon problème de santé.", "bloc A"),
        ("Je peux prendre un rendez-vous au téléphone.", "blocs A et E"),
        ("Je comprends les consignes du pharmacien.", "bloc B"),
        ("Je peux parler de mon état : fatigue, douleur.", "blocs A et C"),
        ("Je connais le vocabulaire de la santé.", "blocs A et E"),
    ], corrige=False,
       notes="L'autoévaluation de l'activité. Dire clairement qu'elle ne compte pas dans "
             "la note : elle sert à savoir quoi refaire. La colonne de droite indique où "
             "retourner pour chaque énoncé.")

    d.cartes('Après le cours', "Où retrouver tout ça", [
        ("Dans l'activité",
         "Les douze cartes mémoire et les quatre listes restent accessibles, avec la "
         "traduction dans votre langue."),
        ("Vos billets",
         "Votre phrase de symptôme, votre formule pour faire répéter, vos besoins : "
         "gardez-les ensemble."),
        ("Les mini-leçons",
         "Les quatre points de langue sont expliqués dans l'activité, sous « En "
         "apprendre plus »."),
        ("Le vrai monde",
         "Le prochain rendez-vous, la prochaine ordonnance. C'est là que ça se vérifie."),
    ], notes="Terminer là-dessus. Le module ne se referme pas sur un test mais sur la "
             "prochaine occasion réelle.")

    d.billet(
        "Écrivez la phrase du module que vous allez utiliser en premier, et quand.",
        exemples=[
            "Une phrase, une occasion précise.",
            "« Je vais appeler la clinique lundi pour prendre un rendez-vous. »",
        ],
        notes="Ramasser, ou faire lire à voix haute si le groupe s'y prête. C'est le "
              "dernier geste du module : une intention datée, pas un souhait.")

    return d.save(dossier)
