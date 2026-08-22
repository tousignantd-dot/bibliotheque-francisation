# -*- coding: utf-8 -*-
"""E1 · Explique la démarche à quelqu'un qui doute
Bloc E « Je me lance » · couleur teal · 75 min. Production orale.
Source : bloc `appli` de `custom.js` — jeu de rôle « chroniquepratique »,
les sept sujets à couvrir, le compte rendu oral en trois temps.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="Explique la démarche à quelqu'un qui doute",
        chapeau="Ton interlocuteur n'a rien écouté, il t'interrompt et il "
                "trouve que c'est trop compliqué. C'est la situation la plus "
                "ordinaire qui soit : expliquer quelque chose à quelqu'un "
                "qui n'y croit pas.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Rendre les billets de D2 corrigés : chacun a "
                  "déjà sa première phrase. Annoncer les deux temps de la séance : le "
                  "jeu de rôle avec l'assistant, puis l'enregistrement du compte rendu.")

    d.objectifs([
        "expliquer une démarche en étapes à quelqu'un qui n'a rien "
        "entendu ;",
        "donner les détails nécessaires : les chiffres, les délais, les "
        "noms ;",
        "illustrer un point par un exemple annoncé ;",
        "répondre à une objection sans rejeter la personne.",
    ], notes="Le deuxième objectif vient directement des attentes de fin de cours du "
             "niveau 6 : décrire les étapes d'une démarche administrative en donnant "
             "les détails nécessaires. Le dire au groupe, ça donne du poids.")

    d.declencheur(
        'Mise en situation', "Quelqu'un de ton entourage a un appareil brisé",
        pistes=[
            "Il n'a pas écouté la chronique et il ne te croit pas.",
            "Il te dit : d'où tu tiens ça ?",
            "Il te dit : c'est bien trop compliqué pour rien.",
            "Qu'est-ce que tu réponds, sans te fâcher ?",
        ],
        notes="Faire jouer les deux dernières répliques par l'enseignante, à voix haute, "
              "en interrompant vraiment. Le groupe voit alors ce qu'on attend de lui, "
              "et ça détend l'atmosphère.")

    d.cartes("Trois situations au choix", "Choisis celle que tu connais le mieux", [
        ("La laveuse de Nadège",
         "780 $, elle a cessé de vidanger après trois ans et quatre mois."),
        ("Les trois étapes",
         "le commerçant, la mise en demeure avec dix jours, les petites créances."),
        ("La pièce qui n'arrive pas",
         "le technicien est venu deux fois et attend une pièce depuis cinq semaines."),
    ], cols=3,
       notes="Trois cas, dans l'activité interactive. Encourager les élèves qui ont "
             "raconté un cas réel au billet de C1 à le prendre à la place : le module "
             "l'accepte, et l'oral en est bien meilleur.")

    d.tableau('Analyse', "Les sept sujets à couvrir",
              ['Le sujet', 'Ce que ça donne'],
              [["De quoi il s'agit", "une chronique, mardi, à la radio"],
               ["Le résumé", "trois ou quatre phrases"],
               ["Les étapes", "dans l'ordre, sans en sauter"],
               ["Un exemple", "prenons une laveuse de 780 dollars"],
               ["Une objection", "y répondre sans rejeter la personne"],
               ["Une hypothèse", "si ça ne bouge pas, tu écris"],
               ["Ton point de vue", "à mon avis, trois ans, c'est court"]],
              cle=0,
              notes="Diapositive à photographier. La faire copier avant de commencer : "
                    "l'élève coche au fur et à mesure, et il sait où il en est.")

    d.regle("Répondre à une objection sans rejeter la personne",
            "« Tu as raison que c'est du temps. Mais six jours, c'est ce que ça a pris à madame Berthiaume. »",
            precision="On commence par accorder ce qui est vrai dans l'objection, puis "
                      "on oppose un fait. C'est ce que fait Myriam Vaugeois en C1 : "
                      "« c'est vrai que c'est long, je ne le nierai pas, mais beaucoup "
                      "de dossiers se règlent avant l'audience ». Contredire d'un bloc "
                      "ferme la discussion ; concéder d'abord la garde ouverte.",
            notes="Diapositive à photographier. C'est la compétence la plus transférable "
                  "de tout le module : elle sert au travail, à l'école des enfants et "
                  "au comptoir d'un commerce.")

    d.cartes("Réemploie ce que tu viens d'apprendre", "Cinq structures, une par bloc", [
        ("Ne répète pas, reprends",
         "« Tout le monde en a une, et personne ne le sait. »"),
        ("Place les étapes",
         "« D'abord tu retournes voir le marchand ; si ça ne bouge pas, tu écris. »"),
        ("Illustre",
         "« Prenons une laveuse de sept cent quatre-vingts dollars. »"),
        ("Dis ce qu'il faut",
         "« Il faut que tu gardes ta facture. »"),
        ("Annonce ton avis",
         "« À mon avis, trois ans, ce n'est pas une durée raisonnable. »"),
    ], notes="Ces cinq exemples sont affichés dans l'activité, sous le jeu de rôle. Les "
             "faire répéter à voix haute avant de commencer : ce sont des phrases "
             "toutes faites, et à ce moment du module elles sont légitimes.")

    d.tableau('Analyse', "Le compte rendu oral, en trois temps",
              ['Le temps', 'Ce qu\'on y dit'],
              [["Temps 1", "de quoi il s'agit, et d'où tu le sais"],
               ["Temps 2", "les étapes, dans l'ordre, avec les chiffres et les délais"],
               ["Temps 3", "un exemple, puis ton point de vue annoncé comme tel"]],
              cle=0,
              note="Environ quatre-vingt-dix secondes en tout. On peut recommencer autant de fois qu'on veut.",
              notes="Diapositive à photographier. Le plan est affiché dans l'activité. "
                    "Insister sur la note : personne n'est enregistré du premier coup, "
                    "et l'élève choisit la prise qu'il envoie.")

    d.piege("Donner son avis dès la première phrase",
            "C'est scandaleux, les appareils ne durent plus rien.",
            "J'ai écouté une chronique sur la garantie légale mardi matin.",
            "Celui qui t'écoute ne sait pas encore de quoi tu parles : une opinion "
            "livrée avant l'information le laisse sans prise, et il se braque. "
            "L'information d'abord, l'avis ensuite - c'est le conseil de Raphaël à "
            "Nadège, et c'est aussi le plan du courriel de la dernière séance.",
            notes="Erreur attendue chez la moitié du groupe, surtout chez ceux qui ont "
                  "vécu la situation. Le nommer avant l'enregistrement fait gagner une "
                  "prise à tout le monde.")

    d.pratique('Production orale', "Quatre-vingt-dix secondes, en trois temps",
               "Enregistre-toi, écoute-toi, corrige, puis envoie.", [
        ("Temps 1", "j'ai écouté une chronique pratique mardi matin, à la radio"),
        ("Temps 2", "d'abord le commerçant, puis la lettre avec dix jours, puis le tribunal"),
        ("Temps 3", "prenons une laveuse de 780 dollars... à mon avis, trois ans, c'est court"),
        ("Avant d'envoyer", "coche les sept sujets : il en manque presque toujours un"),
        ("Le débit", "parle lentement : un compte rendu trop rapide ne s'écoute pas"),
    ], corrige=False,
       notes="Enregistrement dans l'activité, avec une rétroaction de l'assistant avant "
             "l'envoi. La rétroaction n'est pas conservée ; seul l'enregistrement "
             "envoyé arrive à l'enseignante.")

    d.billet(
        "Quelle objection t'a le plus fait hésiter, et qu'est-ce que tu as répondu ?",
        exemples=[
            "Une objection, une réponse.",
            "Si tu n'as pas su quoi répondre, dis-le : c'est utile aussi.",
        ],
        notes="Trois minutes. Les objections restées sans réponse valent la peine d'être "
              "reprises en groupe au début de E2 : cinq minutes, et tout le monde y "
              "gagne une phrase pour sa lettre.")

    return d.save(dossier)
