# -*- coding: utf-8 -*-
"""E2 · Je retiens des mots.
Bloc E « Je me lance » · couleur framboise · 60 min.
Source : banc `FC_CARDS`, cartes mémoire et autoévaluation du module.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre='Je retiens des mots',
        chapeau="Seize mots, quatre familles, et une question : qu'est-ce que "
                "je suis maintenant capable de dire au comptoir du "
                "secrétariat ?",
        duree='60 minutes')

    d.titre(notes="Dernière séance du module — et dernière du niveau 3. Prévoir les "
                  "cartes mémoire du module interactif : la révision se fait à l'écran, "
                  "en paires.")

    d.objectifs([
        "revoir les seize mots du module, par familles ;",
        "employer chaque mot dans une phrase ;",
        "évaluer ce qu'on est capable de faire ;",
        "nommer ce qui reste à travailler.",
    ])

    d.cartes("Le centre et les gens", "Cinq mots", [
        ("le secrétariat, le comptoir",
         "Le bureau et le meuble. C'est là qu'on va pour tout ce qui est écrit."),
        ("la secrétaire",
         "La personne qui reçoit et qui écrit dans les dossiers. Elle a un nom : "
         "l'apprendre vaut la peine."),
        ("le groupe, le dossier",
         "Ce qui vous nomme au centre. Le groupe se donne chaque fois, sans attendre "
         "qu'on le demande."),
    ], cols=3,
       notes="Faire dire chaque mot avec son article, puis dans une phrase complète.")

    d.cartes("L'absence et le papier", "Onze mots", [
        ("une absence, prévenir",
         "Le fait de manquer, et le geste de le dire avant."),
        ("l'avant-midi, un rendez-vous",
         "Le moment de la journée, et l'heure fixée d'avance."),
        ("un billet d'absence, justifier, une photocopie, l'original",
         "Le papier de la clinique, ce qu'il fait, et ce que le centre en fait."),
        ("un abandon, une attestation de fréquentation, signer",
         "Les trois mots du défi 3, ceux qu'on n'emploie qu'une fois — mais où il faut "
         "les employer juste."),
    ], notes="Faire retrouver chaque mot dans les dialogues du module. Ce qui ne se "
             "retrouve pas se réexplique.")

    d.pratique('Vocabulaire', "Le mot juste",
               "Complétez avec un mot du module.", [
        ("Le bureau où on annonce une absence est le ___ .", "secrétariat"),
        ("Le papier de la clinique est un ___ d'absence.", "billet"),
        ("Dire à l'avance qu'on sera absent, c'est ___ .", "prévenir"),
        ("Le papier qui prouve qu'on a suivi le cours est une ___ .", "attestation"),
        ("Arrêter le cours pour de bon, c'est un ___ .", "abandon"),
        ("La secrétaire fait une ___ et rend l'original.", "photocopie"),
    ], corrige=True,
       notes="Exercice d'entrée. Il reprend exactement l'exercice 2 de « Je me lance » "
             "du module interactif.")

    d.tableau('Analyse', "Ce que le module a appris à faire",
              ["Compétence", "Ce qu'on sait faire"],
              [["Parler", "annoncer une absence ou un abandon au comptoir"],
               ["Écrire", "un courriel d'absence de cinq à huit phrases"],
               ["Écouter", "comprendre les questions de la secrétaire"],
               ["Lire", "une affiche, un billet, un formulaire"]],
              cle=1,
              note="Les deux premières lignes sont les deux intentions que le "
                   "programme donne à cette situation ; les deux autres les "
                   "servent.",
              notes="Diapo à photographier. C'est la carte du module entier, et le point "
                    "de départ de l'autoévaluation.")

    d.pratique('Autoévaluation', "Qu'est-ce que je suis capable de faire ?",
               "Pour chaque énoncé : pas encore, un peu, ou oui.", [
        ("Je peux nommer le secrétariat, le comptoir, mon groupe.", ""),
        ("Je salue et je vouvoie le personnel du centre.", ""),
        ("Je peux annoncer une absence au futur proche.", ""),
        ("Je fais la différence entre jeudi et le jeudi.", ""),
        ("Je peux dire quelles journées j'ai manquées.", ""),
        ("Je peux demander une attestation avant de partir.", ""),
    ], corrige=False,
       notes="Les mêmes énoncés que dans le module interactif. Les élèves répondent à "
             "l'écran ; la diapositive sert à la mise en commun.")

    d.regle("La phrase à emporter",
            "« Je vais être absente jeudi, l'avant-midi. »",
            precision="Une phrase, une date, un moment. Elle se dit au "
                      "comptoir, au téléphone et dans un courriel sans rien "
                      "changer. C'est ce qui reste du module dans un an.",
            notes="Faire dire la phrase à voix haute par chaque élève, en tour de table, "
                  "avec une vraie journée. Cinq minutes, et le module se ferme sur du "
                  "concret.")

    d.billet(
        "Écrivez la phrase que vous direz la prochaine fois.",
        exemples=[
            "« La prochaine fois, je vais prévenir avant. »",
            "Gardez-la dans votre cahier, avec le numéro du secrétariat.",
        ],
        notes="Fin du module et fin du niveau 3. Rappeler que les cartes mémoire restent "
              "accessibles et que le jeu de rôle peut se refaire autant de fois qu'on "
              "veut.")

    return d.save(dossier)
