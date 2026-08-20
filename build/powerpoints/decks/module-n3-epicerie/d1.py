# -*- coding: utf-8 -*-
"""D1 · À la caisse.
Bloc D « Défi 3 · À la caisse » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3vf` et `t3caisse`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-epicerie/images/')


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre='À la caisse',
        chapeau="Trois questions, toujours les mêmes : la carte de points, "
                "les sacs, débit ou crédit. Les connaître d'avance, c'est "
                "passer la caisse sans stress.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc D. Demander au groupe ce qui est le plus intimidant à "
                  "la caisse : c'est presque toujours la vitesse.")

    d.objectifs([
        "comprendre les trois questions de la caisse ;",
        "y répondre en une phrase courte ;",
        "comprendre un montant et le faire répéter ;",
        "savoir ce qu'est une carte de points.",
    ])

    d.declencheur(
        'Observation', "Que se passe-t-il ici, et dans quel ordre ?",
        image=IMG + 'caisse-tapis.jpg',
        pistes=[
            "Qu'est-ce qu'on fait en arrivant ?",
            "Quelles questions pose la personne à la caisse ?",
            "Quand paie-t-on ?",
            "Qu'est-ce qu'on emporte en partant ?",
        ],
        notes="Faire reconstituer l'ordre complet : déposer, répondre aux questions, payer, "
              "emballer, prendre la facture.")

    d.dialogue('Dialogue · 1 de 3', "La carte de points", [
        ("STÉPHANE", "Bonjour ! Vous avez la carte de points ?", True),
        ("MARISOL", "La carte de points ? Non. C'est quoi ?", True),
        ("STÉPHANE", "C'est gratuit. Vous ramassez des points, et après vous avez des rabais.", True),
        ("MARISOL", "Ah. Je peux avoir une carte ?", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Marisol demande ce que c'est au lieu de dire non. C'est le réflexe du module : "
             "demander plutôt que subir.")

    d.dialogue('Dialogue · 2 de 3', "Les sacs", [
        ("STÉPHANE", "Oui, je vous donne le formulaire. Vous avez des sacs ?", True),
        ("MARISOL", "Non. Je dois acheter des sacs ?", True),
        ("STÉPHANE", "Les sacs de plastique, on n'en donne plus. Les sacs réutilisables sont à deux dollars.", True),
        ("MARISOL", "D'accord, un sac, s'il vous plaît.", True),
    ], notes="Les sacs de plastique à usage unique ne sont plus distribués au Québec. "
             "Beaucoup d'élèves le découvrent à la caisse, sans sac.")

    d.dialogue('Dialogue · 3 de 3', "Le montant", [
        ("STÉPHANE", "Ça fait quarante-deux dollars et quinze. Débit ou crédit ?", True),
        ("MARISOL", "Débit. Pardon, vous pouvez répéter le montant ?", True),
        ("STÉPHANE", "Quarante-deux quinze. Quarante-deux dollars et quinze cents.", True),
    ], notes="Marisol répond d'abord à la question, puis demande de répéter. L'ordre "
             "compte : on ne bloque pas la file.")

    d.tableau('Analyse', "Les trois questions",
              ['La question', 'Une réponse courte'],
              [["Vous avez la carte de points ?", "Oui, la voici. / Non, merci."],
               ["Vous avez des sacs ?", "J'en ai deux. / Non, j'en prends un."],
               ["Débit ou crédit ?", "Débit, s'il vous plaît."]],
              cle=2,
              note="Trois questions, trois réponses de quatre mots. Elles ne changent jamais.",
              notes="Diapo à photographier. Faire répéter les trois réponses jusqu'à ce "
                    "qu'elles viennent sans réfléchir.")

    d.regle("Comprendre un montant",
            "« Quarante-deux quinze » = 42 $ et 15 ¢.",
            precision="À l'oral, on dit souvent le montant sans le mot « dollars » ni le "
                      "mot « cents » : « quarante-deux quinze ». Le premier nombre est en "
                      "dollars, le second en cents. Si vous n'avez pas compris : "
                      "« <b>Pardon, vous pouvez répéter le montant ?</b> »",
            notes="Diapo à photographier. Le montant est aussi affiché sur le terminal : le "
                  "signaler, c'est un filet de sécurité.")

    d.cartes("La carte de points", "Trois choses à savoir", [
        ("Elle est gratuite",
         "On la demande à la caisse ou au service à la clientèle. Il faut donner un nom, un "
         "courriel, parfois une adresse."),
        ("Elle donne des rabais",
         "Les points s'accumulent et se transforment en argent sur une facture, ou en "
         "rabais réservés."),
        ("Elle enregistre vos achats",
         "C'est le prix à payer : le magasin sait ce que vous achetez. À vous de juger si "
         "l'échange vous convient."),
    ], notes="La troisième carte est une information honnête, rarement donnée. Elle permet "
             "un choix éclairé, sans militer dans un sens ou dans l'autre.")

    d.piege("Se taire quand on n'a pas compris",
            "Faire oui de la tête, et payer sans savoir combien.",
            "Pardon, vous pouvez répéter ?",
            "La file derrière n'est pas une raison : redire un montant prend deux secondes, "
            "et la personne à la caisse le fait cinquante fois par jour. Le montant est "
            "aussi affiché sur le terminal de paiement — on peut le lire.",
            notes="Rappeler le filet : l'écran affiche toujours le montant.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Marisol a déjà une carte de points.", "faux — elle n'en a pas"),
        ("La carte de points est gratuite.", "vrai"),
        ("Le magasin donne encore des sacs de plastique.", "faux"),
        ("Un sac réutilisable coûte deux dollars.", "vrai"),
        ("Marisol paie avec sa carte de crédit.", "faux — débit"),
        ("Elle demande de répéter le montant.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte.")

    d.billet(
        "Écrivez vos réponses aux trois questions de la caisse.",
        exemples=[
            "Une phrase courte par question.",
            "Ajoutez la phrase qui fait répéter un montant.",
        ],
        notes="Ramasser. Ces quatre phrases doivent être sues par cœur à la fin du bloc D.")

    return d.save(dossier)
