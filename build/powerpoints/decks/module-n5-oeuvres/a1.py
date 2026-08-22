# -*- coding: utf-8 -*-
"""A1 · « Deux minutes, et personne ne vous coupe. »
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.
"""
import pathlib

from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-oeuvres/images/')


def photo(nom):
    """La photo si elle est sur le disque, None sinon.

    Les vingt-deux images du module sortent de
    `build/contenu/module-n5-oeuvres/gen_images.py`, qui coûte de l'argent
    réel et n'a pas encore tourné. Sans ce garde-fou, `build.py` s'arrêterait
    sur un fichier absent au lieu de produire les seize séances — et la
    photo apparaîtra d'elle-même au prochain build, une fois les images
    générées.
    """
    p = pathlib.Path(IMG + nom)
    return str(p) if p.exists() else None


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="« Deux minutes, et personne ne vous coupe. »",
        chapeau="Mai Trinh a trente-huit ans. Elle travaille de nuit dans "
                "une buanderie industrielle et elle lit le jour, parce "
                "qu'elle dort mal. Un mardi, une affiche sur la porte de la "
                "petite salle du fond lui propose exactement ce qui lui fait "
                "peur : parler deux minutes, en français, devant des "
                "inconnus.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir par une question au groupe : "
                  "quelqu'un vous a-t-il déjà conseillé un livre, un film ou une série ? "
                  "Qu'est-ce qui vous a donné envie — ou pas ? Les réponses contiennent "
                  "déjà tout le module : le genre, l'histoire, l'avis, la raison. Ne rien "
                  "corriger à cette étape, seulement écouter.")

    d.objectifs([
        "comprendre ce qu'on appelle une œuvre, et sur quels supports elle existe ;",
        "dire en une phrase de quoi on parle : le titre, le genre, le support ;",
        "comprendre ce qu'un club de lecture demande, et ce qu'il interdit ;",
        "reconnaître la différence entre répondre à des questions et tenir un discours.",
    ], notes="Le quatrième objectif est celui qui distingue ce module du niveau 4. Au "
             "niveau 4, on nommait un loisir et on disait qu'on l'aimait. Ici, personne "
             "ne pose de questions pendant que l'élève parle : il avance seul, du début "
             "à la fin. C'est nouveau, et c'est le travail de tout le module.")

    d.declencheur(
        'Observation', "Une affiche sur une porte : « Apportez une œuvre "
                       "que vous avez aimée. » Vous apporteriez quoi ?",
        image=photo('affiche-club.jpg'),
        pistes=[
            "Est-ce qu'il faut avoir lu un livre pour venir ?",
            "Une chanson, est-ce que ça compte ?",
            "Qu'est-ce que vous diriez pendant deux minutes ?",
            "Et si quelqu'un vous demandait comment ça finit ?",
        ],
        notes="Les quatre pistes annoncent les quatre séances du bloc A. La dernière — "
              "« comment ça finit ? » — amène la règle du club, qui tient tout le défi 1. "
              "Laisser le groupe débattre : il y a toujours quelqu'un pour dire qu'il "
              "raconte la fin sans problème, et quelqu'un d'autre pour s'en indigner.")

    d.dialogue('Dialogue · 1 de 3', "Un club de lecture, c'est quoi au juste ?", [
        ("MAI", "Excusez-moi. L'affiche sur la porte, là : « Club du jeudi ». "
                "C'est quoi ?", True),
        ("NADIA", "Un club de lecture. On se réunit dans la petite salle du fond.", True),
        ("MAI", "Un club de lecture… il faut avoir lu quelque chose de précis ?", True),
        ("NADIA", "Non. Chacun apporte une œuvre et la présente aux autres.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire relever la question de Mai : « il faut avoir lu quelque chose de "
             "précis ? » C'est la crainte de tout le monde devant un club de lecture. La "
             "réponse de Nadia — chacun apporte ce qu'il veut — enlève l'obstacle.")

    d.dialogue('Dialogue · 2 de 3', "Une œuvre, ce n'est pas seulement un livre", [
        ("MAI", "Une œuvre, ça veut dire un livre ?", True),
        ("NADIA", "Un livre, oui. Mais aussi un film, une série, une chanson, "
                  "une bande dessinée.", True),
        ("MAI", "Ah bon. Même une chanson ?", True),
        ("NADIA", "Même une chanson. Ce qui compte, c'est d'expliquer pourquoi "
                  "vous l'aimez.", True),
    ], notes="Écrire au tableau les cinq supports nommés : un livre, un film, une série, "
             "une chanson, une bande dessinée. Demander au groupe d'en ajouter — une "
             "pièce de théâtre, un balado, un album de musique. Tous comptent.")

    d.dialogue('Dialogue · 3 de 3', "La règle qui tient tout le module", [
        ("MAI", "Toute l'histoire ? Même la fin ?", True),
        ("NADIA", "Surtout pas la fin. Gilberte vous arrête tout de suite si "
                  "vous la racontez.", True),
        ("MAI", "Et si je n'ai rien lu cette semaine ?", True),
        ("NADIA", "Alors vous écoutez. Et vous repartez avec trois suggestions.", False),
    ], notes="La dernière réplique est celle qui rassure le plus le groupe : on peut venir "
             "sans rien apporter. Le club n'est pas un examen. La première, en revanche, "
             "est la règle du module, et elle reviendra à chaque séance du bloc B.")

    d.regle("On ne raconte jamais la fin",
            "Celui qui dévoile le dénouement enlève à l'autre la seule chose "
            "qu'il ne pourra jamais lui rendre : la découverte.",
            precision="Ce n'est pas une règle de grammaire, c'est une règle de "
                      "conversation. Elle vaut au club, au comptoir, dans l'autobus "
                      "et devant le cinéma. Savoir donner envie sans tout dire est "
                      "une compétence, et elle s'apprend comme le reste.",
            notes="Diapositive à photographier. Elle reviendra à la séance B4, qui en fait "
                  "un exercice complet, et à la séance E1, où l'assistant arrête l'élève "
                  "s'il commence à raconter le dénouement.")

    d.cartes("Cinq supports", "Ce qu'on peut apporter au club", [
        ("Un roman",
         "Une histoire inventée, en un seul livre, du début à la fin."),
        ("Une bande dessinée",
         "Un album grand et cartonné, souvent le tome d'une série."),
        ("Un film",
         "Deux heures, une fois — on dit la durée et où il joue encore."),
        ("Une série",
         "Des épisodes qu'on regarde l'un après l'autre : dire combien."),
        ("Une chanson",
         "Quatre minutes : la présentation la plus courte qui soit."),
        ("Une œuvre",
         "Le mot qui couvre les cinq, quand on ne veut pas encore préciser."),
    ], notes="Insister sur la dernière carte : « œuvre » ne se dit pas en première phrase, "
             "parce que personne ne saurait encore s'il s'agit d'un livre ou d'un film. "
             "Il sert à la deuxième ou à la troisième mention, pour éviter de répéter. "
             "C'est le sujet de la séance C4.")

    d.tableau('Deux façons de parler', "Ce qui change au niveau 5",
              ['Répondre à des questions', 'Tenir un discours'],
              [["Quelqu'un demande, je réponds", "J'avance seul, du début à la fin"],
               ["Une phrase à la fois", "Cinq phrases qui se suivent"],
               ["L'autre décide de l'ordre", "C'est moi qui décide de l'ordre"],
               ["« J'aime lire. »", "« C'est un roman, une histoire de famille… »"],
               ["Si j'oublie, on me relance", "Si j'oublie, le silence reste"]],
              cle=1,
              notes="Faire remplir la colonne de droite par le groupe avant de l'afficher. "
                    "C'est ici qu'on nomme ce que le niveau 5 demande de neuf : « des "
                    "discours simples mais organisés », dit le programme. Rassurer : "
                    "organisé ne veut pas dire compliqué, ça veut dire dans un ordre.")

    d.piege("Commencer par « j'ai lu quelque chose de bien »",
            "J'ai lu quelque chose de bien la semaine passée…",
            "C'est un roman, une histoire de famille, trois cents pages.",
            "La première phrase ne dit ni ce que c'est, ni de quoi ça parle : tout le "
            "monde attend la suite pour comprendre de quoi on parle, et les dix "
            "premières secondes sont perdues. Le support et le genre, tout de suite.",
            notes="Faire répéter la deuxième phrase à voix haute par plusieurs élèves, "
                  "avec leur propre œuvre. Trois ou quatre passages suffisent : c'est la "
                  "phrase la plus rentable du module, et elle se réemploie partout.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Le club du jeudi se réunit dans la petite salle du fond.", "vrai"),
        ("Il faut avoir lu un livre précis pour participer.", "faux — chacun apporte ce qu'il veut"),
        ("Une chanson peut être présentée au club.", "vrai"),
        ("Chaque personne parle pendant dix minutes.", "faux — deux minutes"),
        ("Personne ne coupe la parole pendant la présentation.", "vrai"),
        ("Il faut raconter la fin de l'histoire aux autres.", "faux — surtout pas la fin"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte du dialogue. C'est "
             "l'exercice `pr1` du module interactif : les élèves le retrouveront tel quel "
             "à l'écran, et l'avoir fait à l'oral d'abord leur donne de l'avance.")

    d.billet(
        "Nommez une œuvre que vous avez aimée, et dites en une phrase ce que c'est.",
        exemples=[
            "Dites le support : un roman, un film, une série, une chanson, une bande dessinée.",
            "Ajoutez le genre en deux mots : une histoire de famille, un policier, une comédie.",
        ],
        notes="Le billet sert de vérification de fin de séance et de matière pour tout le "
              "module : c'est l'œuvre que l'élève présentera au bloc E. Ramasser les "
              "billets et les rendre à la séance B1 — plusieurs auront changé d'idée, ce "
              "qui n'est pas un problème.")

    return d.save(dossier)
