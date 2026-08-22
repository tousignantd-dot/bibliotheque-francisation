# -*- coding: utf-8 -*-
"""C2 · Lire une note de service en trente secondes
Bloc C « Défi 2 · Ce que disent les documents » · couleur ambre · 75 min.
Source : exercice `t2note` — un exercice du type `texte`, où l'élève clique
dans la note même — et sa mini-leçon. Intention : lire de la documentation
interne reliée à son emploi.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Lire une note de service en trente secondes",
        chapeau="Une note se lit par en haut et par en bas, jamais du début "
                "à la fin. En haut, deux lignes disent si elle vous "
                "concerne ; en bas, l'encadré dit ce qu'il ne faut pas "
                "manquer.",
        duree='75 minutes')

    d.titre(notes="Séance de lecture. L'exercice du module est du type « texte » : la "
                  "note reste affichée à côté des questions, et l'élève clique dans le "
                  "document le passage qui répond. Prévoir les postes.")

    d.objectifs([
        "trouver dans une note à qui elle s'adresse et de quoi elle parle ;",
        "relever une date limite exacte, heure comprise ;",
        "suivre les puces comme une suite de gestes ;",
        "repérer l'encadré de rappel avant de lire le corps du texte.",
    ], notes="Le deuxième objectif est celui qui se mesure : « avant vendredi » n'est "
             "pas une réponse, « vendredi 25 septembre, 16 h » en est une.")

    d.declencheur(
        'Observation', "Une note affichée depuis trois semaines : est-elle encore valable ?",
        pistes=[
            "Où regarde-t-on pour le savoir ?",
            "Qu'est-ce qu'un babillard garde trop longtemps ?",
            "Que fait-on quand deux notes se contredisent ?",
        ],
        notes="La date d'une note est la première chose à vérifier, et presque "
              "personne ne le fait. Un babillard garde des papiers périmés pendant "
              "des mois.")

    d.tableau('Analyse', "La note du module, morceau par morceau",
              ['L\'endroit', 'Ce qu\'il apprend'],
              [["À l'ensemble du personnel", "la note vous concerne, vous aussi"],
               ["Objet : affichage du poste", "de quoi il s'agit, en une ligne"],
               ["dix jours ouvrables", "combien de temps l'affichage reste au mur"],
               ["vendredi 25 septembre, 16 h", "le moment exact de la fin"],
               ["les trois puces", "ce qu'il faut faire, et dans quel ordre"],
               ["l'encadré RAPPEL", "la date limite et le numéro du bureau"]],
              cle=0,
              notes="Diapositive à photographier. Faire relire la note du module en "
                    "suivant ce tableau ligne à ligne, avant d'ouvrir les postes.")

    d.regle("Par en haut, puis par en bas",
            "Le milieu d'une note est la partie la moins urgente.",
            precision="Trois lignes lues en haut évitent parfois deux pages lues pour "
                      "rien : c'est le meilleur rendement de toute la lecture "
                      "professionnelle. Puis on descend jusqu'au bas de page, parce "
                      "qu'un encadré est petit et que le regard le manque. Le corps "
                      "du texte vient en dernier.",
            notes="Diapositive à photographier. Faire chronométrer : trente secondes "
                  "pour dire à qui la note s'adresse, de quoi elle parle et quelle "
                  "est la date limite. La plupart y arrivent au deuxième essai.")

    d.pratique('Lecture', "Où est la réponse dans la note ?",
               "Nommez le passage exact. On ne résume pas : on cite.", [
        ("À qui cette note s'adresse-t-elle ?", "à l'ensemble du personnel"),
        ("De quoi la note parle-t-elle ?", "objet : affichage du poste de vérificateur ou vérificatrice"),
        ("Combien de temps l'affichage reste-t-il ?", "dix jours ouvrables"),
        ("À quel moment exact sera-t-il retiré ?", "le vendredi 25 septembre, à 16 h"),
        ("Que faut-il avoir pour être admissible ?", "six mois d'ancienneté et la formation sur les allergènes"),
        ("Qu'est-ce qui n'est pas nécessaire ?", "la signature du chef d'équipe"),
    ], corrige=True,
       notes="Même exercice que celui du module, en version projetée. Exiger la "
             "citation, pas le résumé : c'est ce que l'exercice interactif demande "
             "aussi, puisqu'on y clique dans le texte.")

    d.piege('Piège', "répondre « avant vendredi »",
            "répondre « vendredi 25 septembre, 16 h »",
            "Une date limite se cite entière, heure comprise. « Avant vendredi » laisse "
            "croire qu'on a la journée ; la note dit seize heures, et le bureau ferme. "
            "Dans une démarche, l'imprécision d'un délai coûte la démarche entière.",
            notes="Insister : c'est le même piège qu'en B1, et il reviendra en E1 "
                  "quand l'élève décrira la démarche à voix haute.")

    d.cartes('Analyse', "Ce que la note ne fait pas", [
        ("Elle ne crée aucune règle",
         "Elle explique une règle écrite ailleurs. « Veuillez consulter l'article 4 » n'est pas une formule de politesse : c'est un renvoi."),
        ("Elle ne vaut pas éternellement",
         "Elle porte une date. Un babillard garde parfois des notes périmées, et la démarche a pu changer depuis."),
        ("Elle ne dit pas tout",
         "Une note tient sur une page. Les cas particuliers, les exceptions et les recours sont dans la politique."),
        ("Elle ne remplace pas une question",
         "Ce qui reste obscur après deux lectures se demande au service qui l'a écrite — le nom est sur la ligne « De : »."),
    ], notes="Diapositive à photographier. La quatrième carte est celle qui débloque "
             "les élèves timides : la personne à qui écrire est nommée sur le papier.")

    d.billet(
        "Écris la date limite de la note, complète.",
        exemples=[
            "Jour, date, mois, heure.",
            "Puis écris ce que tu ferais si tu la manquais.",
        ],
        notes="Trois minutes. La seconde partie ouvre C3 : la politique dit ce qui "
              "arrive quand un délai est manqué, la note ne le dit pas.")

    return d.save(dossier)
