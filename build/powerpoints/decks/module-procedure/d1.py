# -*- coding: utf-8 -*-
"""D1 · Réserver le véhicule de service.
Bloc D · couleur teal (lire et répondre) · 60 min.
Source : exercices `t3vehicule` et `t3correct`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D1', section='teal',
        titre='Réserver le véhicule de service',
        chapeau="Une directive écrite, affichée sur un mur ou dans une application. "
                "Personne ne l'explique : il faut la lire seul, et ne rien oublier.",
        duree='60 minutes')

    d.titre(notes="Ouverture du défi 3. Prévenir : ici, personne ne parle. Toute "
                  "l'information est écrite, et c'est ce qui rend l'exercice difficile.")

    d.objectifs([
        "lire une directive écrite et en tirer toutes les exigences ;",
        "repérer ce qu'on doit fournir et ce qu'on recevra ;",
        "savoir quoi faire quand la procédure ne fonctionne pas ;",
        "corriger un énoncé faux à partir du texte.",
    ])

    d.tableau('Analyse', "La directive, en trois blocs",
              ['Le bloc', 'Ce qu\'il dit'],
              [["pour réserver", "nom, numéro d'employé, date, heures, raison du déplacement"],
               ["ensuite", "vérifier la disponibilité, réserver, recevoir la confirmation"],
               ["en cas de conflit", "communiquer avec le répartiteur, au poste 4"]],
              cle=0, props=[0.25, 0.75],
              note="Toute directive a ces trois blocs : ce qu'on fournit, ce qui se "
                   "passe, et quoi faire si ça bloque.",
              notes="Écrire les trois au tableau. C'est la grille de lecture de toute "
                    "directive, et elle sert aussi en D2.")

    d.regle('La règle de lecture',
            "Cherchez d'abord la liste de ce qu'il faut fournir.",
            precision="Nom, numéro d'employé, date, heure de départ, heure de retour, "
                      "raison du déplacement. Six éléments. Une directive qui en "
                      "demande six et à qui on en donne cinq ne fonctionne pas — et "
                      "elle ne dit pas toujours lequel manque.",
            notes="Faire compter les six éléments dans le texte. Beaucoup d'élèves n'en "
                  "verront que quatre à la première lecture.")

    d.cartes('Analyse', "Ce que la directive ne dit pas explicitement", [
        ("Le numéro d'employé compte autant que le nom",
         "Deux personnes peuvent porter le même nom. Le numéro est ce qui identifie "
         "sans ambiguïté."),
        ("La raison du déplacement n'est pas une formalité",
         "Elle sert à trancher quand deux personnes veulent le véhicule le même jour. "
         "Une raison vague fait perdre la priorité."),
        ("La confirmation par courriel est votre preuve",
         "Gardez-la. Sans elle, vous ne pouvez pas prouver que la réservation "
         "existait."),
        ("Le poste 4 s'appelle avant, pas après",
         "Le répartiteur règle les conflits d'horaire. L'appeler après avoir pris le "
         "véhicule ne règle rien."),
    ], notes="Ces quatre points ne sont pas écrits dans la directive : ils se déduisent. "
             "C'est la lecture avancée qu'on travaille ici.")

    d.pratique('Pratique · 1 de 4', "Vrai ou faux — la directive",
               "D'après le texte affiché.", [
        ("Pour réserver, vous devez indiquer seulement votre nom.",
         "FAUX — le nom et le numéro d'employé"),
        ("Vous devez indiquer l'heure de départ et de retour.", "VRAI"),
        ("Vous n'avez pas besoin d'indiquer la raison du déplacement.",
         "FAUX — la raison est demandée"),
        ("Vous recevrez une confirmation par courriel.", "VRAI"),
        ("En cas de conflit d'horaire, vous pouvez appeler le répartiteur.", "VRAI"),
    ], corrige=True,
       notes="Faire pointer, pour chaque réponse, la phrase exacte de la directive. "
             "C'est la seule justification acceptée.")

    d.pratique('Pratique · 2 de 4', "Corrigez les énoncés faux",
               "Réécrivez-les correctement, d'après le texte.", [
        ("« Pour réserver, vous devez indiquer seulement votre nom. »",
         "Vous devez indiquer votre nom et votre numéro d'employé."),
        ("« Vous n'avez pas besoin d'indiquer la raison du déplacement. »",
         "Vous devez indiquer la raison du déplacement."),
    ], corrige=True,
       notes="Corriger un énoncé faux est plus difficile que de le repérer : il faut "
             "retrouver l'information juste et la reformuler.")

    d.piege("Le piège du « seulement »",
            "« Vous devez indiquer seulement votre nom » paraît vrai parce que le nom est demandé.",
            "Le mot « seulement » rend l'énoncé faux.",
            "Un seul petit mot peut renverser un énoncé. « Seulement », « toujours », "
            "« jamais », « uniquement » : ce sont eux qu'il faut chercher en premier "
            "dans un vrai ou faux. Le reste de la phrase peut être exact.",
            notes="Faire relever ces mots dans les cinq énoncés de l'exercice. C'est une "
                  "stratégie de lecture qui sert bien au-delà du cours.")

    d.pratique('Pratique · 3 de 4', "Les six éléments à fournir",
               "Complétez le formulaire de réservation.", [
        ("Votre identité", "nom et numéro d'employé"),
        ("Quand", "la date"),
        ("Combien de temps", "heure de départ et heure de retour"),
        ("Pourquoi", "la raison du déplacement"),
        ("Ce que vous faites ensuite", "vérifier la disponibilité, puis réserver"),
        ("Ce que vous recevez", "une confirmation par courriel"),
    ], corrige=True,
       notes="Faire remplir un formulaire fictif au tableau, avec des données réelles. "
             "L'exercice devient concret en trois minutes.")

    d.piege("Le piège de la confirmation non lue",
            "J'ai cliqué sur Réserver, c'est réservé.",
            "Je vérifie que le courriel de confirmation est arrivé.",
            "Un clic ne garantit rien : le système peut refuser, le véhicule peut avoir "
            "été pris entre-temps, le courriel peut atterrir dans les indésirables. La "
            "confirmation est ce qui prouve la réservation, pas le clic.",
            notes="Lier à l'accusé de réception vu en A3. C'est le même réflexe, appliqué "
                  "à une autre démarche.")

    d.pratique('Pratique · 4 de 4', "Écrivez votre réservation",
               "Une phrase par élément demandé.", [
        ("La situation",
         "Vous devez livrer du matériel à un autre entrepôt jeudi prochain, de 8 h à "
         "midi."),
        ("Ce que vous inscrivez", "les six éléments demandés par la directive"),
        ("Ce que vous vérifiez ensuite", "la confirmation par courriel"),
    ], corrige=False,
       notes="Quinze minutes. Ramasser : ces réservations montrent qui a vraiment relevé "
             "les six éléments.")

    d.billet(
        "Relevez les trois blocs d'une directive de votre travail ou de votre école.",
        exemples=[
            "Ce qu'il faut fournir · ce qui se passe · quoi faire si ça bloque.",
            "Si vous n'en avez pas, servez-vous de celle du véhicule de service.",
        ],
        notes="Les directives réelles apportées par les élèves sont la meilleure matière "
              "pour E1. En garder quelques-unes.")

    return d.save(dossier)
