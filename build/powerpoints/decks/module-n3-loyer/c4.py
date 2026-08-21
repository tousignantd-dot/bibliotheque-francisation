# -*- coding: utf-8 -*-
"""C4 · Je vais venir samedi.
Bloc C « Défi 2 · Téléphoner pour visiter » · couleur framboise · 75 min.
Source : exercice `t2futur` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='framboise',
        titre='Je vais venir samedi',
        chapeau="Pour dire ce qui arrive bientôt, le français prend le verbe "
                "aller et pose derrière lui le verbe qui compte. Six formes à "
                "savoir, et c'est tout.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc C. Ouvrir en demandant au groupe ce que "
                  "chacun va faire ce soir. Les réponses arriveront au présent : c'est "
                  "l'occasion de montrer la forme du jour en reformulant.")

    d.objectifs([
        "employer le futur proche pour prendre un rendez-vous ;",
        "connaître les six formes du verbe aller au présent ;",
        "savoir que le second verbe ne se conjugue jamais ;",
        "distinguer un déplacement et un futur proche.",
    ])

    d.regle("Deux verbes, et un seul se conjugue",
            "« Je vais venir samedi matin. »",
            precision="Le verbe aller se conjugue, le second reste comme dans "
                      "le dictionnaire. C'est de loin la façon la plus "
                      "employée de parler de ce qui arrive bientôt — au "
                      "téléphone, on n'entend presque que celle-là.",
            notes="Diapositive à photographier. Souligner les deux verbes de couleurs "
                  "différentes au tableau : l'un bouge, l'autre jamais. L'image tient "
                  "toute la séance.")

    d.tableau('Analyse', "Les six formes du verbe aller",
              ["Qui", "On dit"],
              [["je", "je vais"],
               ["tu", "tu vas"],
               ["il, elle", "il va, elle va"],
               ["nous, vous, ils", "nous allons, vous allez, ils vont"]],
              cle=1,
              note="Trois se ressemblent : vais, vas, va. C'est le mot d'avant qui les distingue.",
              notes="Diapositive à photographier. Faire réciter les six à voix haute, "
                    "deux fois, avant tout exercice écrit. Ce sont elles, et rien "
                    "d'autre, qu'il faut savoir.")

    d.tableau('Analyse', "Le futur proche au téléphone",
              ["Le moment", "La phrase"],
              [["prendre un rendez-vous", "Je vais venir samedi matin."],
               ["annoncer qui vient", "Nous allons visiter à dix heures."],
               ["promettre un rappel", "Je vais vous rappeler demain."],
               ["parler du logement", "Il va être libre le premier juillet."]],
              cle=0,
              note="Quatre phrases qui reviennent dans presque tous les appels.",
              notes="Diapositive à photographier. Faire remarquer que les quatre "
                    "viennent du dialogue de la séance C1 : le futur proche y est "
                    "partout, et personne ne l'avait remarqué.")

    d.tableau('Analyse', "Aller tout seul, aller avec un verbe",
              ["La phrase", "Ce que ça veut dire"],
              [["Je vais à Villeray.", "un déplacement"],
               ["Je vais visiter.", "quelque chose qui arrive bientôt"],
               ["Je vais aller à Villeray.", "les deux à la fois"],
               ["Ce qui décide", "le mot qui suit : un lieu ou un verbe"]],
              cle=0,
              note="Si le mot qui suit est un verbe, c'est le futur proche.",
              notes="Diapositive à photographier. La troisième ligne fait toujours rire "
                    "le groupe et c'est tant mieux : « je vais aller » est correct, très "
                    "courant, et il montre bien la mécanique.")

    d.piege('Grammaire',
            "« je vais je viens samedi »",
            "« je vais venir samedi »",
            "Un seul verbe se conjugue : aller. Le second reste comme dans le "
            "dictionnaire, quelle que soit la personne qui parle.",
            notes="Même erreur qu'avec « je voudrais », vue à la séance C2. Faire le "
                  "rapprochement : c'est la même mécanique, et l'avoir comprise une fois "
                  "sert deux fois.")

    d.piege('Grammaire',
            "« nous vont visiter »",
            "« nous allons visiter »",
            "La forme du « nous » repart du verbe aller en entier : nous "
            "allons, vous allez. Ce sont les deux qui surprennent, parce "
            "qu'elles ne ressemblent pas aux autres.",
            notes="Faire réciter la conjugaison à l'envers — ils vont, vous allez, nous "
                  "allons — pour que les deux formes longues ne soient pas toujours en "
                  "fin de liste.")

    d.pratique('Grammaire', "Complétez avec le verbe aller",
               "Vais, vas, va, allons ou vont ?", [
        ("Je ___ venir samedi matin avec mon mari.", "vais"),
        ("Nous ___ visiter le logement à dix heures.", "allons"),
        ("Le logement ___ être libre le premier juillet.", "va"),
        ("Est-ce que tu ___ appeler la propriétaire ?", "vas"),
        ("Mes voisins ___ déménager la semaine prochaine.", "vont"),
        ("Je ___ vous rappeler demain matin.", "vais"),
    ], corrige=True, cols=2,
       notes="C'est l'exercice 4 du Défi 2. Faire justifier chaque réponse par le sujet, "
             "à voix haute : « le logement, c'est il, donc va ».")

    d.pratique('Production', "Dites ce que vous allez faire",
               "Une phrase complète, au futur proche.", [
        ("Ce soir.", "Je vais ___ ."),
        ("Demain matin.", "Je vais ___ ."),
        ("Samedi.", "Je vais ___ ."),
        ("Avec votre famille, la semaine prochaine.", "Nous allons ___ ."),
        ("Après le module.", "Je vais ___ ."),
    ], corrige=True,
       notes="Production libre et rapide, chacun une phrase. Corriger seulement la forme "
             "d'aller et l'infinitif qui suit : le reste n'est pas le sujet de la "
             "séance.")

    d.billet(
        "Écrivez trois choses que vous allez faire pour chercher un logement.",
        exemples=[
            "Je vais ___ les petites annonces.",
            "Je vais ___ et je vais ___ .",
        ],
        notes="Devoir court, et dernier du bloc C. Les phrases produites servent "
              "d'ouverture à la séance D1 : le bloc D commence au moment de la visite, "
              "donc après ces gestes-là.")

    return d.save(dossier)
