# -*- coding: utf-8 -*-
"""A4 · Savoir d'avance ce qu'un texte va donner
Bloc A « Je découvre » · couleur teal · 75 min. Révision du bloc.
Source : exercices `prGenres` et `prImg`, mini-leçon « Savoir d'avance ce
qu'un texte va donner ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='teal',
        titre="Savoir d'avance ce qu'un texte va donner",
        chapeau="Dernière séance avant le premier défi. Le genre s'annonce "
                "en trois secondes : par sa longueur, par sa place dans la "
                "page, par la première phrase. Ensuite, on sait quoi "
                "chercher.",
        duree='75 minutes')

    d.titre(notes="Quatrième séance du bloc A. Elle sert de révision : le groupe a vu "
                  "les cinq genres, la graphie-phonie et la ponctuation. Aujourd'hui "
                  "on assemble, et on annonce le Défi 1.")

    d.objectifs([
        "reconnaître un genre à sa longueur et à sa place dans la page ;",
        "dire ce qu'un genre donne et ce qu'il ne donnera jamais ;",
        "distinguer un article informatif d'un texte d'opinion ;",
        "réviser les cinq mots des genres et les trois cas de "
        "graphie-phonie.",
    ], notes="Le troisième objectif est nouveau : l'article informatif n'était pas "
             "dans le dialogue. Il entre ici parce qu'il complète les cinq genres et "
             "qu'il est partout dans un journal.")

    d.declencheur(
        'Mise en situation', "Trois secondes pour reconnaître un texte",
        pistes=[
            "Quinze lignes seules dans un coin de page : quel genre ?",
            "Un texte qui finit par un nom et le nom d'un quartier ?",
            "Un texte de cinquante lignes sans jamais le mot « je » ?",
            "Une émission d'une heure avec de vieilles images ?",
        ],
        notes="Poser les quatre questions rapidement, une par une, sans laisser "
              "réfléchir longtemps. Le but est justement d'installer un jugement "
              "rapide : c'est celui qu'on a devant un vrai journal.")

    d.tableau('Analyse', "Ce que chaque genre donne, et ce qu'il ne donne pas",
              ['Le genre', 'Ce qu\'il ne te donnera jamais'],
              [["La chronique pratique", "une nouvelle : rien n'y est arrivé cette semaine"],
               ["L'entrevue", "ce que l'invité a décidé de ne pas dire"],
               ["Le documentaire", "l'actualité des derniers jours"],
               ["Le fait divers", "un avis, une cause certaine, un coupable"],
               ["Le courrier des lecteurs", "la position du journal lui-même"]],
              cle=0,
              note="Chercher dans un genre ce qu'il ne donne pas, c'est la première cause de découragement.",
              notes="Diapositive à photographier. Ce tableau est le miroir de celui de "
                    "A1 : l'un dit ce qu'on trouve, l'autre ce qu'on ne trouvera pas. "
                    "Les afficher côte à côte si le tableau le permet.")

    d.regle("L'article informatif, le sixième genre",
            "Les faits d'une nouvelle, présentés sans que l'auteur dise « je ».",
            precision="C'est le genre le plus courant d'un journal, et le plus "
                      "discret : personne ne s'y met en avant. Il ne se confond avec "
                      "aucun autre, parce qu'il n'a ni le « je » de la lettre, ni les "
                      "étapes de la chronique, ni la brièveté du fait divers. Quand un "
                      "texte de journal ne ressemble à rien, c'est presque toujours "
                      "celui-là.",
            notes="Diapositive à photographier. Faire remarquer que le module n'en "
                  "travaille pas la lecture : il est nommé pour compléter la série, "
                  "parce que le programme du niveau 6 le mentionne.")

    d.pratique('Association', "À quoi sert chaque genre ?",
               "Associez chaque genre à ce qu'il donne.", [
        ("une chronique pratique", "une démarche à suivre, expliquée étape par étape"),
        ("une entrevue", "ce qu'une seule personne accepte de dire, en réponse à des questions"),
        ("un documentaire", "l'histoire longue d'un sujet, racontée par une voix hors champ"),
        ("un fait divers", "quinze lignes sur un accident ou un incendie, sans aucun avis"),
        ("le courrier des lecteurs", "des opinions signées par des gens qui ne sont pas journalistes"),
        ("un article informatif", "les faits d'une nouvelle, présentés sans que l'auteur dise « je »"),
    ], corrige=True,
       notes="Laisser le groupe répondre entièrement avant d'afficher. Le dernier est "
             "le seul nouveau ; les cinq autres doivent venir sans hésitation, sinon "
             "il faut reprendre A1 avant d'entrer dans le Défi 1.")

    d.pratique('Observation', "Où l'information se fabrique, où elle se lit",
               "Décrivez ce que montre chaque image de l'exercice interactif.", [
        ("Le comptoir d'accueil d'une bibliothèque, avec ses piles de livres.", "le travail de Nadège"),
        ("Une laveuse ouverte, le panier encore plein d'eau.", "le problème de départ"),
        ("Un petit poste de radio sur un comptoir de cuisine, tôt le matin.", "la chronique du Défi 1"),
        ("Deux places face à face dans un studio, chacune devant un micro.", "l'entrevue du Défi 2"),
        ("Une page de journal remplie de courtes lettres.", "le courrier du Défi 3"),
        ("Un écran de télévision qui montre de vieilles images d'usine.", "le documentaire du Défi 2"),
    ], corrige=True,
       notes="L'exercice se fait à l'écran, avec les photos. Ici, la diapositive sert à "
             "annoncer le parcours : chaque image correspond à un moment du module. Le "
             "dire explicitement, ça donne une carte au groupe.")

    d.vocabulaire('Révision', "Ce qu'il faut savoir avant le Défi 1", [
        ("une chronique pratique", "Elle t'apprend quoi faire, pas ce qui est arrivé."),
        ("une entrevue", "Écoute les questions autant que les réponses."),
        ("un documentaire", "Un sujet large, raconté au passé, par une voix hors champ."),
        ("un fait divers", "Quinze lignes, aucun avis, jamais."),
        ("le courrier des lecteurs", "Des lettres signées, choisies par le journal."),
        ("une chronique, un schéma, soixante", "Trois graphies à ne plus rater : ch dur, sch, x qui siffle."),
    ], notes="Révision rapide, cinq minutes. Les cinq premières lignes sont des cartes "
             "mémoire de l'activité ; la dernière rappelle A2.")

    d.billet(
        "Quel genre te semble encore le plus difficile, et pourquoi ?",
        exemples=[
            "Une phrase honnête vaut mieux qu'une réponse polie.",
            "Le documentaire ? l'entrevue ? Dis pourquoi.",
        ],
        notes="Deux minutes. Lire les réponses avant B1 : elles disent où ralentir. Le "
              "documentaire arrive presque toujours en tête, à cause du passé simple - "
              "et il est travaillé en C3.")

    return d.save(dossier)
