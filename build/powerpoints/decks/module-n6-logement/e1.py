# -*- coding: utf-8 -*-
"""E1 · Décrire la démarche à voix haute
Bloc E « Je me lance » · couleur teal · 75 min. Production orale.
Source : bloc « Je me lance » du module — jeu de rôle `souslocation` et
production orale. La tâche vient des **attentes de fin de cours** du niveau,
la situation « Location d'un logement » n'ayant aucune intention de
production : « il décrit les étapes d'une démarche administrative en donnant
les détails nécessaires ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="Décrire la démarche à voix haute",
        chapeau="Quatre semaines de lecture tiennent dans quatre-vingt-dix "
                "secondes de parole : ce qu'on a lu, on doit pouvoir le "
                "redire à quelqu'un qui n'a rien lu.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Le dire clairement : la situation du "
                  "programme ne demande que de la lecture, mais les attentes de fin "
                  "de cours demandent, elles, de décrire une démarche à l'oral. C'est "
                  "de là que vient la tâche.")

    d.objectifs([
        "dire de quoi il s'agit avant d'entrer dans les détails ;",
        "nommer les étapes dans l'ordre, avec leurs délais ;",
        "annoncer un exemple par « par exemple » ou « notamment » ;",
        "distinguer ce que le site écrit de ce qu'on en pense.",
    ], notes="Le deuxième objectif distingue une bonne production d'une production "
             "moyenne : « il a quinze jours » compte, « il a un certain temps » ne "
             "compte pas.")

    d.declencheur(
        'Retour', "Expliquez la démarche à votre voisin, sans notes. Deux minutes.",
        pistes=[
            "Commencez par dire de quoi il s'agit et où vous l'avez lu.",
            "Nommez les étapes dans l'ordre : trouver, écrire, prouver, attendre.",
            "Donnez au moins un délai exact.",
        ],
        notes="Faire circuler et relever qui saute l'étape « prouver la date ». C'est "
              "celle qu'on oublie le plus, et c'est celle qui fait tenir tout le "
              "reste. Ne rien corriger pendant : on relève.")

    d.tableau('Le plan', "Trois temps, quatre-vingt-dix secondes",
              ['Le temps', 'Ce qu\'on y dit'],
              [["Temps 1", "de quoi il s'agit, et où vous l'avez lu"],
               ["Temps 2", "les étapes dans l'ordre, avec les dates"],
               ["Temps 3", "un exemple, puis ce que vous feriez"]],
              cle=0,
              note="Le même plan paraît à l'écran dans le module, mot pour mot.",
              notes="Diapositive à photographier. Le faire recopier au dos du cahier : "
                    "c'est le seul papier autorisé pendant l'enregistrement.")

    d.cartes('Modèles', "Une phrase pour ouvrir chaque temps", [
        ("Temps 1",
         "« Quand on part pour un temps, on peut sous-louer son logement au lieu de le perdre. C'est écrit sur le site du Tribunal administratif du logement. »"),
        ("Temps 2",
         "« D'abord, on trouve quelqu'un. Ensuite, on écrit un avis avec son nom et son adresse. À partir du jour où le locateur le reçoit, il a quinze jours pour répondre. »"),
        ("Temps 3",
         "« Prenons le refus : il faut un motif sérieux, par exemple un défaut de paiement au dossier. À votre place, je ferais signer la copie de l'avis. »"),
        ("Ce qu'on évite",
         "« Il faut aller voir le propriétaire » n'est pas une démarche : c'est un début de phrase. Une démarche a des étapes, un ordre et des dates."),
    ], notes="Faire lire les trois premières cartes par trois élèves différents, à voix "
             "haute et debout. Entendre le modèle avant d'enregistrer vaut mieux que "
             "toutes les consignes.")

    d.regle("Citez au lieu d'affirmer",
            "« Selon la page du Tribunal… » plutôt que « la loi dit ».",
            precision="Vous rapportez une règle que vous avez lue, vous ne rendez "
                      "pas un jugement. La différence est de trois mots et elle "
                      "change tout : elle vous met à l'abri, et elle laisse à "
                      "l'autre la possibilité de vérifier. Même chose pour votre "
                      "opinion : « à mon avis » avant, toujours.",
            notes="Diapositive à photographier. C'est le critère que la correction par "
                  "l'IA cherchera en premier. Le laisser au tableau pendant les "
                  "enregistrements.")

    d.cartes('Jeu de rôle', "Trois moments, deux rôles", [
        ("Le projet, annoncé", "Vous exposez votre projet à un locateur qui ne sait rien. Il croit d'abord que vous résiliez, et il doute qu'un étudiant paie."),
        ("Le refus, à peser", "Il a répondu dans le délai et il refuse, avec deux motifs. Un seul se vérifie. Vous répondez sans vous fâcher."),
        ("Les deux cents dollars", "Il exige des frais fixes. Vous ne refusez pas : vous demandez par écrit à quoi ils correspondent."),
        ("Les deux rôles", "Vous jouez la locataire qui a lu, ou le locateur méfiant. Jouer le locateur apprend autant : on voit ce qui, dans un discours, ne convainc pas."),
    ], notes="Le jeu de rôle se fait avec l'assistant, sur les postes, avant "
             "l'enregistrement. Il sert de répétition : personne n'enregistre sans "
             "avoir tenu la conversation au moins une fois.")

    d.pratique('Autocorrection', "Ce que je vérifie avant d'envoyer",
               "Réécoutez-vous une fois et cochez.", [
        ("J'ai dit de quoi il s'agit avant les détails.", "oui / à refaire"),
        ("J'ai nommé les étapes dans l'ordre.", "oui / à refaire"),
        ("J'ai donné au moins une date ou un délai exact.", "oui / à refaire"),
        ("J'ai annoncé un exemple.", "oui / à refaire"),
        ("J'ai dit d'où vient la règle.", "oui / à refaire"),
        ("J'ai séparé mon avis de ce que dit le site.", "oui / à refaire"),
    ], corrige=False,
       notes="Faire écouter chacun son propre enregistrement une fois avant d'envoyer. "
             "La liste est la même que celle du module : elle est déjà à l'écran, à "
             "côté du micro.")

    d.billet(
        "Quelle étape avez-vous oubliée à votre première tentative ?",
        exemples=[
            "Une phrase.",
            "Personne ne les dit toutes du premier coup.",
        ],
        notes="Deux minutes, à la toute fin. Le dire soi-même désamorce le sentiment "
              "d'échec, et l'enseignante voit d'un coup d'œil quelle étape reprendre "
              "avec le groupe entier.")

    return d.save(dossier)
