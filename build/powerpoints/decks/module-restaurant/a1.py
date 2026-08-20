# -*- coding: utf-8 -*-
"""A1 · À l'entrée du restaurant — mise en situation.
Bloc A « Je découvre » · couleur teal · 75 min.
Source du module : dialogue `prep`, exercices `prVocab`, `pr1` et `prArrivee`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-restaurant/images/')


def build(dossier):
    d = Deck(
        code='A1', section='teal',
        titre="À l'entrée du restaurant",
        chapeau="Andrés invite Manon pour la remercier. C'est son premier "
                "repas assis dans un restaurant d'ici — et déjà, à l'entrée, "
                "il y a des choses qu'il ne connaît pas.",
        duree='75 minutes')

    d.titre(notes="Ouverture du module. Question d'entrée : « qui est déjà allé au "
                  "restaurant ici, assis, avec un serveur ? ». Souvent moins de mains "
                  "qu'on ne croit — beaucoup ne connaissent que le comptoir.")

    d.objectifs([
        "entrer dans un restaurant et répondre aux questions de l'accueil ;",
        "savoir qu'on attend qu'on nous place ;",
        "distinguer la carte, le menu du jour et la table d'hôte ;",
        "demander deux minutes avant de commander.",
    ])

    d.declencheur(
        'Mise en situation', "Vous entrez ici. Que faites-vous ?",
        image=IMG + 'salle-manger.jpg',
        pistes=[
            "Vous choisissez votre table, ou vous attendez ?",
            "Qu'est-ce qu'on va vous demander en premier ?",
            "Combien de temps avez-vous pour choisir ?",
            "Qu'est-ce qui vous met le plus mal à l'aise, dans un restaurant ?",
        ],
        notes="Cinq minutes. La première piste est la vraie découverte : dans un "
              "restaurant avec service aux tables, on n'entre pas s'asseoir où on veut. "
              "Un panneau le dit souvent, mais peu de gens le lisent.")

    d.cartes('La situation', "Ce qu'on sait d'Andrés", [
        ("D'où il vient",
         "Du Pérou. Il est au Québec depuis deux ans."),
        ("Pourquoi il invite",
         "Manon, une collègue, l'a aidé toute la semaine. Il veut la remercier."),
        ("Ce qu'il ne connaît pas",
         "Il n'a mangé qu'au comptoir jusqu'ici. La carte, le menu du jour, la table "
         "d'hôte : trois mots qu'il n'a jamais eu à distinguer."),
        ("Ce qu'il fait de bien",
         "Il demande à Manon. Poser la question à quelqu'un qui sait est plus rapide que "
         "de deviner."),
    ], notes="La deuxième carte donne le ton du module : c'est une invitation, pas un "
             "examen. Le repas est un plaisir.")

    d.dialogue('Dialogue · 1 de 3', "Les trois questions de l'accueil", [
        ("SOPHIE", "Bonsoir ! Vous êtes combien ?", True),
        ("ANDRÉS", "Bonsoir. Deux, s'il vous plaît.", True),
        ("SOPHIE", "Vous avez une réservation ?", True),
        ("ANDRÉS", "Non, je n'en ai pas. Est-ce qu'il y a de la place ?", True),
    ], consigne="Écoutez d'abord l'enregistrement, diapo masquée. Lisez ensuite.",
       notes="Quatre répliques, quatre teintées : ce sont les quatre premières phrases de "
             "n'importe quel repas au restaurant. Les faire répéter par le groupe.")

    d.dialogue('Dialogue · 2 de 3', "On vous place", [
        ("SOPHIE", "Oui, ça va. Vous préférez près de la fenêtre ou au fond ?", True),
        ("ANDRÉS", "Près de la fenêtre, si c'est possible.", True),
        ("SOPHIE", "Suivez-moi. Voici la carte. Le menu du jour est sur l'ardoise, là-bas.", True),
        ("MANON", "Merci. On peut prendre deux minutes avant de commander ?", True),
    ], notes="« Si c'est possible » et « on peut prendre deux minutes ? » : deux formules "
             "qui adoucissent tout. Les écrire au tableau.")

    d.dialogue('Dialogue · 3 de 3', "Trois mots à distinguer", [
        ("ANDRÉS", "Manon, c'est quoi la différence entre la carte et le menu du jour ?", True),
        ("MANON", "La carte, c'est tout ce qu'ils font. Le menu du jour change chaque jour et coûte moins cher.", True),
        ("ANDRÉS", "Et la table d'hôte ?", False),
        ("MANON", "C'est un prix fixe pour trois services : entrée, plat, dessert. Souvent le meilleur choix.", True),
    ], notes="Le cœur de la séance. Ces trois mots reviennent dans tous les restaurants du "
             "Québec, et l'écart de prix entre eux peut doubler.")

    d.tableau('Analyse', "Les trois formules",
              ['La formule', 'Ce que c\'est'],
              [["La carte", "tout ce que le restaurant sert, chaque plat à son prix"],
               ["Le menu du jour", "un choix limité, différent chaque jour, moins cher"],
               ["La table d'hôte", "un prix fixe pour trois services"],
               ["À la carte", "un plat seul, sans entrée ni dessert"]],
              cle=2,
              note="La table d'hôte est souvent le meilleur rapport si on a faim.",
              notes="Diapo à photographier. Faire recopier : c'est la compétence la plus "
                    "rentable du module.")

    d.vocabulaire('Vocabulaire · 1 de 2', "À l'entrée", [
        ("une réservation", "Une table réservée d'avance, à son nom."),
        ("l'hôtesse", "La personne qui accueille et qui place les clients."),
        ("la carte", "La liste de tout ce que le restaurant sert."),
        ("l'ardoise", "Le tableau noir où est écrit le menu du jour."),
        ("la salle à manger", "La partie du restaurant où on mange, avec les tables."),
    ], notes="« Ardoise » surprend souvent : c'est un objet, pas un document. La montrer "
             "sur l'image de A3.")

    d.vocabulaire('Vocabulaire · 2 de 2', "Les formules", [
        ("le menu du jour", "Un choix limité qui change chaque jour."),
        ("la table d'hôte", "Un prix fixe pour trois services."),
        ("à la carte", "Un plat seul, sans formule."),
        ("un service", "Une partie du repas : entrée, plat ou dessert."),
        ("le plat du jour", "Le plat préparé seulement aujourd'hui."),
    ], notes="Attention : « le menu » en français d'ici désigne souvent une formule à prix "
             "fixe, pas la liste complète. La liste, c'est la carte.")

    d.regle("Ce qu'il faut retenir",
            "On attend qu'on vous place, et on peut prendre deux minutes.",
            precision="Dans un restaurant avec service aux tables, on ne choisit pas sa "
                      "table. Et une fois assis, personne ne vous presse : « on peut "
                      "prendre deux minutes ? » est une phrase parfaitement ordinaire, que "
                      "le serveur entend vingt fois par soir.",
            notes="Faire répéter la phrase par deux élèves. C'est la diapo à photographier.")

    d.piege("Commander la première chose venue",
            "Euh… le poulet. [parce que le serveur attend]",
            "On peut prendre deux minutes avant de commander ?",
            "Beaucoup de gens commandent trop vite parce qu'ils se sentent pressés — et "
            "regrettent en voyant l'assiette du voisin. Le serveur, lui, s'attend à "
            "repasser : c'est même prévu dans son service.",
            notes="Ne pas présenter cela comme une faute de langue : c'est une question de "
                  "confort, et elle change complètement l'expérience du repas.")

    d.billet(
        "Écrivez les quatre premières phrases que vous direz en entrant dans un restaurant.",
        exemples=[
            "La salutation, le nombre de personnes, la réservation, la préférence de table.",
            "Ajoutez la phrase pour demander deux minutes.",
        ],
        notes="Ramasser. Ces phrases servent directement au jeu de rôle de E1.")

    return d.save(dossier)
