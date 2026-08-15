# -*- coding: utf-8 -*-
"""A1 · Trente secondes en ondes — mise en situation.
Bloc A « Je découvre » · couleur teal · 75 min.
Source du module : dialogue `prep`, exercices `prVocab` et `pr1`, cartes mémoire.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A1', section='teal',
        titre='Trente secondes en ondes',
        chapeau="Solange a écrit une minute quarante pour annoncer l'atelier de "
                "réparation du quartier. La radio en accorde trente secondes. Il va "
                "falloir choisir — et choisir, c'est décider à qui l'on parle.",
        duree='75 minutes')

    d.titre(notes="Ouverture du module 7. Écrire au tableau : TRENTE SECONDES. Faire "
                  "chronométrer trente secondes en silence : c'est plus long qu'on "
                  "croit, et beaucoup plus court qu'un texte de cent mots.")

    d.objectifs([
        "comprendre à quoi sert une publicité et à qui elle s'adresse ;",
        "distinguer l'émetteur du récepteur ;",
        "savoir ce qu'on garde et ce qu'on coupe dans un message court ;",
        "reconnaître un slogan.",
    ])

    d.declencheur(
        'Mise en situation', "Vous avez trente secondes pour annoncer un événement. Que dites-vous ?",
        pistes=[
            "À qui parlez-vous, exactement ?",
            "Quelles trois informations sont indispensables ?",
            "Qu'est-ce que vous laissez tomber ?",
            "Comment finissez-vous, pour qu'on s'en souvienne ?",
        ],
        notes="Cinq minutes en grand groupe. La première question est celle qui compte : "
              "presque personne n'y pense, et c'est elle qui décide de tout le reste.")

    d.cartes('La situation', "Ce qu'on sait de Solange", [
        ("Ce qu'elle veut annoncer",
         "L'atelier de réparation du quartier : des bénévoles réparent gratuitement les "
         "objets qu'on apporte."),
        ("Son problème",
         "Son texte dure une minute quarante. La capsule à Radio Limoilou doit durer "
         "trente secondes, pas une de plus."),
        ("Ce qu'Omar lui demande",
         "Non pas de couper au hasard, mais de choisir à qui elle parle. Le reste "
         "découle de ce choix."),
        ("Ce qu'elle trouve",
         "Son récepteur : les gens qui gardent un appareil brisé dans une armoire parce "
         "qu'ils n'osent pas le jeter."),
    ], notes="La quatrième carte est le moment décisif du dialogue. Une fois le récepteur "
             "nommé, le texte se coupe tout seul.")

    d.dialogue('Dialogue · 1 de 3', "Une minute quarante", [
        ("SOLANGE", "Omar, j'ai écrit le texte pour annoncer notre atelier de "
                    "réparation. Je l'ai lu à voix haute : il dure une minute quarante.",
         True),
        ("OMAR", "Une minute quarante ! Solange, une capsule à Radio Limoilou, c'est "
                 "trente secondes, pas une de plus. Il va falloir couper.", True),
        ("SOLANGE", "Couper quoi ? Je parle des grille-pain, des lampes, des vélos, des "
                    "vêtements déchirés, des bénévoles, du café gratuit…", True),
    ], consigne="Écoutez d'abord l'enregistrement, diapo masquée. Lisez ensuite.",
       notes="Passer l'audio de « Je découvre ». Faire compter les objets nommés par "
             "Solange : six. C'est exactement le problème.")

    d.dialogue('Dialogue · 2 de 3', "À qui veux-tu parler ?", [
        ("OMAR", "Justement, tu parles de tout. À qui veux-tu parler, au juste ? Choisis "
                 "les gens que tu veux rejoindre, puis garde seulement ce qui les "
                 "touche.", True),
        ("SOLANGE", "Aux gens du quartier qui gardent un appareil brisé dans une armoire "
                    "parce qu'ils n'osent pas le jeter. C'est eux, mon récepteur.", True),
    ], notes="La question d'Omar est la question de tout le module. L'écrire au tableau : "
             "À QUI VEUX-TU PARLER ?")

    d.dialogue('Dialogue · 3 de 3', "Rien ne se jette, tout se répare", [
        ("OMAR", "Alors garde l'objet brisé, la date et l'adresse. Termine par une phrase "
                 "courte, facile à retenir. Le reste, tu l'écriras sur l'affiche.", True),
        ("SOLANGE", "« Rien ne se jette, tout se répare. » Voilà, je viens de la trouver, "
                    "ma phrase courte !", True),
    ], notes="Trois éléments gardés : l'objet, la date, l'adresse. Plus un slogan. C'est "
             "le contenu d'une capsule de trente secondes.")

    d.regle('La règle du module',
            "On choisit d'abord à qui l'on parle. Le reste suit.",
            precision="Une publicité qui parle à tout le monde ne touche personne. Une "
                      "fois le récepteur choisi, on sait quoi garder : ce qui le "
                      "concerne. Et on sait quoi couper : tout le reste.",
            notes="Écrire la règle au tableau et l'y laisser tout le module. C'est elle "
                  "qui revient dans les seize séances.")

    d.tableau('Analyse', "Ce que Solange garde et ce qu'elle coupe",
              ['Elle garde', 'Elle coupe'],
              [["l'objet brisé", "la liste des six sortes d'objets"],
               ["la date", "le nom des bénévoles"],
               ["l'adresse", "le café gratuit"],
               ["un slogan court", "les détails d'organisation"]],
              cle=0,
              note="Ce qui est coupé n'est pas perdu : ça se retrouve sur l'affiche, où "
                   "il y a de la place.",
              notes="Insister sur la note : chaque canal a sa longueur. Ce n'est pas "
                    "moins d'information, c'est une autre répartition.")

    d.vocabulaire('Vocabulaire · 1 de 2', "Les quatre éléments", [
        ("l'émetteur", "La personne ou l'organisme qui envoie le message publicitaire."),
        ("le récepteur", "Les gens à qui le message publicitaire est destiné."),
        ("le canal", "Le moyen choisi pour diffuser le message : radio, affiche, courriel."),
        ("le message", "Ce qu'on annonce : un événement, un produit ou un service."),
        ("un slogan", "Une phrase courte et facile à retenir, placée à la fin."),
    ], notes="Ces cinq mots sont le vocabulaire d'analyse du module. Ils reviennent dans "
             "toutes les séances : les installer solidement.")

    d.vocabulaire('Vocabulaire · 2 de 2', "Le quartier et la radio", [
        ("une capsule", "Une très courte annonce diffusée à la radio."),
        ("une infolettre", "Un courriel envoyé régulièrement aux personnes inscrites."),
        ("un bénévole", "Une personne qui donne son temps sans être payée."),
        ("une valeur morale", "Ce qu'une personne ou une société considère comme important."),
        ("un préfixe", "Un élément placé devant un mot pour en changer le sens."),
        ("un suffixe", "Un élément placé à la fin d'un mot pour former un nouveau mot."),
    ], notes="« Préfixe » et « suffixe » sont les mots des séances B4 et B5. Les "
             "installer ici, les travailler là-bas.")

    d.pratique('Pratique', "Vrai ou faux",
               "Répondez sans relire le dialogue.", [
        ("La capsule de Solange doit durer trente secondes.", "VRAI"),
        ("Le premier texte de Solange était beaucoup trop court.",
         "FAUX — une minute quarante, trop long"),
        ("Solange veut rejoindre les gens qui gardent un appareil brisé chez eux.", "VRAI"),
        ("Omar conseille de garder la date et l'adresse.", "VRAI"),
        ("Omar demande de nommer tous les objets qu'on répare.", "FAUX — le contraire"),
        ("Les détails coupés se retrouveront sur l'affiche.", "VRAI"),
        ("Solange trouve son slogan à la fin de la discussion.", "VRAI"),
    ], corrige=True,
       notes="Le cinquième énoncé inverse le conseil d'Omar. C'est le piège utile : il "
             "vérifie qu'on a compris la logique, pas seulement les mots.")

    d.piege("Le piège du message pour tout le monde",
            "Je parle des grille-pain, des lampes, des vélos, des vêtements…",
            "Je parle aux gens qui gardent un appareil brisé dans une armoire.",
            "Vouloir toucher tout le monde donne un message que personne ne retient. "
            "Choisir un récepteur précis paraît réduire la portée ; en réalité, cela "
            "l'augmente, parce que ceux qui sont visés se reconnaissent.",
            notes="Contre-intuitif et important. Faire chercher, dans les publicités "
                  "connues du groupe, à qui elles s'adressent vraiment.")

    d.billet(
        "Choisissez un événement et nommez son récepteur en une phrase.",
        exemples=[
            "Un événement de votre quartier, de votre école, de votre travail.",
            "Le récepteur : qui, exactement, et pourquoi ça les touche.",
        ],
        notes="Ramasser. Ces récepteurs serviront en E1, où chacun écrira une capsule "
              "pour eux.")

    return d.save(dossier)
