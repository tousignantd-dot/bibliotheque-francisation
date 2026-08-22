# -*- coding: utf-8 -*-
"""B1 · Une demi-heure après le cours
Bloc B « Défi 1 » · couleur acier · 75 min. Compréhension orale.
Source du module : dialogue `t1` et exercice `t1vf`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Une demi-heure après le cours",
        chapeau="Deux personnes ont lu la même feuille et n'en tirent pas la "
                "même chose. Ce n'est pas un défaut d'attention : c'est qu'on "
                "ne lit pas une consigne comme on lit un texte.",
        duree='75 minutes')

    d.titre(notes="Première séance du défi 1. Le dialogue fait vingt "
                  "répliques et plusieurs sont longues : trois écoutes, et "
                  "l'enseignante y parle en phrases suivies, comme le "
                  "niveau 6 le demande.")

    d.objectifs([
        "suivre une explication détaillée sans en perdre le fil ;",
        "relever ce qu'il faut remettre, et en quelle quantité ;",
        "entendre qu'un futur, dans un document, donne un ordre ;",
        "reconnaître les mots qui rangent les étapes.",
    ], notes="Les deux derniers points sont repris et travaillés dans les "
             "séances B4 et B5 : ici, il s'agit seulement de les entendre.")

    d.declencheur(
        'Avant d\'écouter', "Deux personnes lisent la même feuille. Peuvent-elles comprendre autre chose ?",
        pistes=[
            "Ça vous est déjà arrivé ? Sur quoi ?",
            "Qui avait raison, à la fin ?",
            "Comment auriez-vous pu le savoir plus tôt ?",
        ],
        notes="La dernière question amène la seule bonne réponse : en allant "
              "demander. C'est ce que font Marisol et Youssef, et c'est ce "
              "que la classe doit retenir.")

    d.dialogue('Écoute 1', "Le désaccord", [
        ("MARISOL", "Madame, on a lu la feuille tous les deux et on n'est pas d'accord sur ce qu'il faut remettre.", False),
        ("MIREILLE", "Assoyez-vous. Ça arrive à toutes les équipes, et c'est pour ça que je reste une demi-heure après le cours cette semaine.", True),
        ("YOUSSEF", "Sur le nombre de textes. Moi je comprends qu'on remet un seul document. Marisol pense qu'il y en a deux.", False),
        ("MIREILLE", "Relisez-moi la deuxième ligne du paragraphe deux, celle qui commence par « chaque équipe remettra ».", False),
    ], consigne="Première écoute : qui a raison, à votre avis ?",
       notes="Laisser le groupe se prononcer avant la réponse. Le partage "
             "des voix est presque toujours le même que celui du dialogue.")

    d.dialogue('Écoute 2', "La réponse est dans la phrase", [
        ("MARISOL", "« Chaque équipe remettra un texte de deux pages et le plan qui a servi à l'écrire. »", True),
        ("MIREILLE", "Deux documents, donc. Le texte et le plan. Youssef, tu as lu trop vite, et je ne t'en blâme pas : cette phrase-là est une phrase de consigne, et une consigne ne se lit pas comme un roman.", True),
        ("YOUSSEF", "Elle se lit comment ?", False),
        ("MIREILLE", "Une ligne à la fois, avec un crayon. Chaque fois qu'un verbe vous dit de faire quelque chose, vous le soulignez. Il y en a sept dans ma feuille, et je les ai comptés.", True),
    ], consigne="Deuxième écoute : où était l'information ?",
       notes="Le point à faire ressortir : l'information manquante était "
             "après le « et ». C'est l'endroit le plus sauté d'une consigne.")

    d.dialogue('Écoute 3', "Le futur qui ordonne, et la grille", [
        ("MARISOL", "C'est écrit « vous choisirez votre sujet avant le 3 novembre ». Ce n'est pas une question de ce qui va arriver, ça. C'est un ordre.", True),
        ("MIREILLE", "C'en est un. Dans un document écrit, le futur donne souvent un ordre poli. « Vous choisirez » veut dire « choisissez ».", True),
        ("YOUSSEF", "Parlez-nous de la grille. Il y a quatre lignes et je ne comprends pas la dernière.", False),
        ("MIREILLE", "Un paragraphe par idée principale. Un blanc entre les paragraphes. Et des mots qui relient une idée à la suivante.", False),
    ], consigne="Troisième écoute : notez les chiffres du barème.",
       notes="Faire relever : vingt points en tout, huit pour le contenu, "
             "quatre pour les sources, quatre pour la langue, quatre pour "
             "l'organisation.")

    d.regle("Dans un document, le futur donne souvent un ordre",
            "« Vous choisirez votre sujet avant le 3 novembre » veut dire : choisissez-le.",
            precision="Ni « peut-être », ni « probablement », ni « on verra ». "
                      "Un élève qui lit ça comme une possibilité manque une "
                      "obligation, et il la manque poliment.",
            notes="Diapositive à photographier. Le même emploi se retrouve "
                  "sur un avis d'hôpital, une convocation, un formulaire de "
                  "la ville : le dire, ça sert bien au-delà du cours.")

    d.pratique('Pratique', "Vrai ou faux",
               "Réécoutez au besoin, puis répondez.", [
        ("Il faut remettre deux documents : le texte et le plan.", "vrai"),
        ("Une consigne se lit une ligne à la fois, avec un crayon.", "vrai"),
        ("« Vous choisirez » annonce ce qui va arriver.", "faux : c'est un ordre"),
        ("Le contenu vaut huit points sur vingt.", "vrai"),
        ("L'organisation du texte vaut deux points.", "faux : quatre"),
        ("Un travail remis le 26 novembre est encore reçu.", "faux : rien après le 24"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `t1vf` du module. Terminer sur la dernière "
             "affirmation : la date est la seule chose qui ne se discute "
             "jamais, et l'enseignante du dialogue le dit elle-même.")

    d.billet(
        "Écris ce que ton équipe doit remettre, en comptant les documents.",
        exemples=[
            "Combien de documents ? Lesquels ?",
            "Une phrase, avec un chiffre dedans.",
        ],
        notes="Deux minutes. Ceux qui écrivent « un texte » ont fait la même "
              "lecture que Youssef : le leur montrer sans commenter, la "
              "séance B2 fera le reste.")

    return d.save(dossier)
