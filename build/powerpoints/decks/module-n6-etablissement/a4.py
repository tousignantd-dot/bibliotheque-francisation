# -*- coding: utf-8 -*-
"""A4 · Les lieux du centre, et ce qu'on y règle
Bloc A « Je découvre » · couleur teal · 75 min. Bilan du bloc A.
Source : exercice `prImg`, reprise de `prVocab` et du dialogue `prep`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='teal',
        titre="Les lieux du centre, et ce qu'on y règle",
        chapeau="Un comptoir, un petit bureau fermé, une classe, une salle de "
                "réunion. Quatre endroits, quatre façons de parler — et une "
                "seule chose qui se règle dans chacun.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc A. Elle rassemble ce qui précède et "
                  "prépare le rendez-vous d'orientation de B1. Prévoir vingt minutes "
                  "pour la mise en situation finale.")

    d.objectifs([
        "associer un lieu de l'établissement à ce qui s'y règle ;",
        "choisir le bon endroit avant de poser une question ;",
        "réemployer les cinq mots du bloc dans une phrase complète ;",
        "préparer une demande de rencontre en deux lignes précises.",
    ], notes="Le dernier objectif produit un vrai document : les élèves repartent "
             "avec leur demande écrite, et ils peuvent la déposer pour de bon.")

    d.declencheur(
        'Observation', "Dans quel local du centre es-tu déjà entré ?",
        pistes=[
            "Le comptoir de l'accueil, la classe, autre chose ?",
            "Es-tu déjà allé dans un bureau fermé, avec une seule autre personne ?",
            "Qu'est-ce qui change quand la porte est fermée ?",
        ],
        notes="La question du bureau fermé est importante : beaucoup d'élèves n'ont "
              "jamais eu de rendez-vous individuel dans un établissement d'ici, et "
              "l'idée même les intimide. Nommer cette intimidation, ne pas la nier.")

    d.tableau('Analyse', "Quatre lieux, quatre travaux",
              ['Le lieu', 'Ce qui s\'y règle'],
              [["Le comptoir", "un papier à donner ou à demander, en deux minutes debout"],
               ["Le bureau fermé", "une situation qui demande d'être expliquée, sur rendez-vous"],
               ["La classe", "ce que vous savez faire, et ce qui vous manque encore"],
               ["La salle de réunion", "une décision prise à plusieurs, avec un écrit à la fin"]],
              cle=0,
              note="Une question posée dans le mauvais lieu ne reçoit pas une mauvaise réponse : elle ne reçoit rien.",
              notes="Diapositive à photographier. Faire nommer, pour chaque lieu, une "
                    "question du groupe recueillie en A1 sur les billets.")

    d.pratique('Pratique', "Où faut-il aller ?",
               "Lisez la situation, puis nommez le lieu et la personne.", [
        ("Vous voulez une copie de vos résultats de l'an dernier.", "au comptoir"),
        ("Vous ne savez pas quel programme choisir après la francisation.", "au bureau de l'orientation, sur rendez-vous"),
        ("Vous voulez savoir si votre français est assez avancé.", "en classe, à votre enseignant"),
        ("Vous avez reçu un avis et vous ne comprenez pas la condition.", "à la personne nommée dans la dernière ligne de l'avis"),
        ("Vous voulez changer votre horaire de cours.", "au comptoir"),
        ("Plusieurs personnes doivent s'entendre sur votre dossier.", "en salle de réunion, à une rencontre de suivi"),
    ], corrige=True,
       notes="Le quatrième item est le plus utile : la réponse n'est pas « au "
             "comptoir », c'est la personne nommée en bas de la lettre. Y insister.")

    d.pratique('Vocabulaire', "Complétez avec le mot juste",
               "Employez les cinq mots du bloc, chacun une seule fois.", [
        ("Rien ne compte tant que ce n'est pas au ...", "dossier scolaire"),
        ("Elle a demandé son ... au comptoir, et il arrive dans deux jours.", "relevé de notes"),
        ("Au centre, presque tout se fait en ...", "enseignement individualisé"),
        ("Il lui manque des unités dans deux ...", "matières"),
        ("La ... reçoit le lundi et le jeudi, sur rendez-vous.", "conseillère d'orientation"),
    ], corrige=True,
       notes="Faire écrire les réponses avant de corriger. Vérifier les articles : "
             "c'est là que se perdent les points, pas sur le mot lui-même.")

    d.regle("Une demande précise obtient une réponse précise",
            "« Je veux de l'information » ne veut rien dire ; « je veux savoir quels préalables il me manque » veut dire quelque chose.",
            precision="Une demande de rencontre tient en deux lignes. Elle dit ce que "
                      "vous cherchez, pas ce que vous ressentez. Plus elle est "
                      "précise, plus la personne d'en face peut préparer votre "
                      "dossier avant de vous voir — et plus l'heure sert.",
            notes="Diapositive à photographier. C'est la règle qui décide de la "
                  "qualité du rendez-vous de B1.")

    d.cartes('Analyse', "Deux demandes, deux résultats", [
        ("Ce qui ne mène nulle part", "« Bonjour, je voudrais de l'information sur les cours. Merci. »"),
        ("Ce qui prépare une heure utile", "« Je termine ma francisation en février. Je vise un programme de formation professionnelle et je veux savoir quels préalables il me manque. »"),
    ], cols=2,
       notes="Faire trouver au groupe ce qui change : la deuxième demande donne une "
             "date, un but et une question. Trois choses, deux lignes.")

    d.billet(
        "Écris ta propre demande de rencontre, en deux lignes.",
        exemples=[
            "Ligne 1 : où tu en es, avec une date.",
            "Ligne 2 : ce que tu veux savoir, précisément.",
        ],
        notes="Dix minutes, et c'est le cœur de la séance. Faire lire trois demandes "
              "à voix haute et les améliorer ensemble. Les élèves qui le souhaitent "
              "peuvent déposer la leur pour vrai au comptoir du centre.")

    return d.save(dossier)
