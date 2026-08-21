# -*- coding: utf-8 -*-
"""D2 · « Je serai absente du 19 au 23 »
Bloc D « Défi 3 » · couleur ambre · 75 min. Futur simple, interrogation
indirecte, courriel de réponse automatique.
Source : exercices `t3fut`, `t3int` et `t3courriel`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-travail/images/')


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="« Je serai absente du 19 au 23 »",
        chapeau="À l'oral, « je vais être absente » se dit très bien. Mais "
                "un message d'accueil, une réponse automatique et un "
                "formulaire sont des écrits, et l'écrit préfère le futur "
                "simple.",
        duree='75 minutes')

    d.titre(notes="Séance qui ferme le défi 3 et prépare les deux productions du bloc E. "
                  "Trois points s'y suivent : le futur simple, la question posée "
                  "poliment, et le courriel d'absence. Ne pas laisser filer le temps sur "
                  "le premier.")

    d.objectifs([
        "employer le futur simple à l'écrit, y compris ses irréguliers ;",
        "mettre le futur après « quand » et « dès que » ;",
        "poser une question à l'intérieur d'une phrase, devant un supérieur ;",
        "écrire un courriel de réponse automatique en cinq lignes.",
    ])

    d.regle("L'infinitif entier, plus six terminaisons",
            "ai, as, a, ons, ez, ont — les mêmes pour tous les verbes.",
            precision="Les verbes en « re » perdent leur e : répondre donne je "
                      "répondrai. Ce sont les terminaisons du verbe avoir au présent, "
                      "et c'est ainsi que le futur s'est formé.",
            notes="Le rapprochement avec « avoir » aide beaucoup d'élèves : ai, as, a, "
                  "avons, avez, ont. Il rend la conjugaison presque inutile à mémoriser.")

    d.tableau('Les irréguliers du bureau', "Huit bases, et ce sont celles qu'on emploie",
              ['Verbe', 'Au futur, à je'],
              [["être · avoir", "je serai · j'aurai"],
               ["faire · aller", "je ferai · j'irai"],
               ["pouvoir · devoir", "je pourrai · je devrai"],
               ["voir · venir", "je verrai · je viendrai"]],
              cle=1,
              note="Les terminaisons ne changent jamais : seule la base est irrégulière.",
              notes="Faire répéter la liste comme une gamme, deux fois. Le double r de "
                    "« pourrai » et « verrai » s'entend, et c'est lui qui distingue "
                    "« je verrai » de « je vais ».")

    d.piege("Mettre le présent après « dès que »",
            "Je vous répondrai dès que je suis de retour.",
            "Je vous répondrai dès que je serai de retour.",
            "Après quand, dès que, lorsque, aussitôt que, tant que, le français met le "
            "futur. Deux futurs dans la même phrase : c'est correct, et c'est même "
            "obligatoire.",
            notes="Faute très fréquente, et elle vient d'autres langues où le présent "
                  "suffit. La nommer ainsi évite qu'un élève croie mal comprendre le "
                  "français.")

    d.pratique('Futur simple', "Complétez au futur",
               "Employez le verbe entre parenthèses.", [
        ("Je ___ (être) absente du 19 au 23 août.", "serai"),
        ("Je ___ (répondre) à vos courriels à mon retour.", "répondrai"),
        ("Kevin ___ (prendre) les appels de l'avant-midi.", "prendra"),
        ("Nous ___ (avoir) une réponse de la paie avant vendredi.", "aurons"),
        ("Vous ___ (pouvoir) joindre Amel au poste dix-huit.", "pourrez"),
        ("Elle ___ (faire) suivre le formulaire dès aujourd'hui.", "fera"),
        ("Je vous ___ (rappeler) dans les meilleurs délais.", "rappellerai"),
        ("Je vous écrirai dès que je ___ (être) de retour.", "serai"),
    ], cols=2, corrige=True,
       notes="La septième garde son e : rappeler donne je rappellerai. On l'écrit même "
             "si on l'entend à peine. La huitième est le piège du « dès que ».")

    d.regle("Poser sa question à l'intérieur d'une phrase",
            "Je voudrais savoir combien de jours il me reste.",
            precision="La question perd son inversion, son « est-ce que » et son point "
                      "d'interrogation. Devant un supérieur, c'est la forme qui permet "
                      "d'enchaîner trois questions sans avoir l'air d'un interrogatoire.",
            notes="Faire le lien avec B3 : le mécanisme est le même que celui du discours "
                  "rapporté. « Si » pour une question fermée, le mot interrogatif pour "
                  "une question ouverte, et l'ordre sujet-verbe qui revient.")

    d.tableau('Trois amorces', "Elles se suivent d'une phrase, jamais d'une question",
              ['La question directe', 'Posée poliment'],
              [["Combien de jours me reste-t-il ?", "Je voudrais savoir combien de jours il me reste."],
               ["Est-ce que la journée est payée ?", "Je voudrais savoir si la journée est payée."],
               ["Quand est-ce que j'aurai la réponse ?", "Pourriez-vous me dire quand j'aurai la réponse."],
               ["Qu'est-ce qu'il faut remplir ?", "J'aimerais savoir ce qu'il faut remplir."]],
              cle=1,
              notes="La faute typique est de garder les deux : « Pourriez-vous me dire "
                    "où est-ce que je dois l'envoyer ? » Il faut choisir. La faire "
                    "entendre à voix haute.")

    d.pratique('Question indirecte', "Posez la question poliment",
               "Transformez chaque question directe.", [
        ("Combien de jours me reste-t-il ?", "Je voudrais savoir combien de jours il me reste."),
        ("Est-ce que la journée est payée ?", "Je voudrais savoir si la journée est payée."),
        ("Où est-ce que j'envoie le formulaire ?", "J'aimerais savoir où j'envoie le formulaire."),
        ("Qui me remplacera l'après-midi ?", "Je voudrais savoir qui me remplacera l'après-midi."),
        ("Qu'est-ce qu'il faut écrire dans cette case ?", "J'aimerais savoir ce qu'il faut écrire dans cette case."),
        ("Est-ce que je dois écrire les deux dates ?", "Pourriez-vous me dire si je dois écrire les deux dates."),
    ], corrige=True,
       notes="Ces six questions sont exactement celles à poser dans le jeu de rôle de "
             "E1. Le dire au groupe : ils les réemploieront demain.")

    d.declencheur(
        'Observation', "Un écran, quelques lignes grises. Cinq lignes qui "
                       "répondent à votre place pendant une semaine.",
        image=IMG + 'ecran-courriel.jpg',
        pistes=[
            "Qu'est-ce que la personne qui vous écrit doit savoir en dix secondes ?",
            "Écrit-on la durée de l'absence, ou la date du retour ?",
            "Faut-il prévenir la personne dont on donne le nom ?",
            "Quand met-on la réponse en marche, et quand l'éteint-on ?",
        ],
        notes="La deuxième piste est celle qui compte : une durée oblige le lecteur à "
              "calculer, et il calcule à partir du jour où il lit. La date du retour, "
              "avec le jour de la semaine, ne se calcule pas.")

    d.pratique('Production écrite', "Le courriel de réponse automatique",
               "Complétez les cinq lignes.", [
        ("Bonjour, je suis ___ du 19 au 23 août.", "absente"),
        ("Je ne ___ (lire) pas mes courriels pendant cette période.", "lirai"),
        ("Pour toute question, écrivez à Kevin Dorais ou faites le ___ dix-neuf.", "poste"),
        ("Je serai de ___ le lundi 26 août.", "retour"),
        ("Je ___ (répondre) à votre message à mon retour.", "répondrai"),
        ("On l'éteint le matin du ___ , avant toute autre chose.", "retour"),
    ], cols=2, corrige=True,
       notes="Faire remarquer que trois des six réponses sont au futur simple : la "
             "grammaire de la première heure sert dans la dernière. C'est ce qui donne "
             "son unité à la séance.")

    d.billet(
        "Écrivez votre courriel de réponse automatique en cinq lignes.",
        exemples=[
            "Vos dates, la date du retour avec le jour de la semaine, un nom et un poste.",
            "Signez avec votre nom et votre fonction.",
        ],
        notes="C'est le brouillon de la production écrite de la séance E2. Ramasser et "
              "annoter, sans corriger toutes les fautes : les élèves le reprendront.")

    return d.save(dossier)
