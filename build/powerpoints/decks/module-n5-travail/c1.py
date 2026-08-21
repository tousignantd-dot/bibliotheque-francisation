# -*- coding: utf-8 -*-
"""C1 · Quatre-vingts pages, et une seule qui vous concerne
Bloc C « Défi 2 · Le mode d'emploi » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t2a`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-travail/images/')


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Quatre-vingts pages, et une seule qui vous concerne",
        chapeau="Le photocopieur du corridor a été remplacé un jeudi, sans "
                "que personne soit prévenu. Le livret livré avec l'appareil "
                "fait quatre-vingts pages et personne ne le lira.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 2. Demander au groupe qui a déjà eu peur d'un "
                  "appareil au travail. Les mains se lèvent, et souvent avec des "
                  "histoires : une carte avalée, une commande partie trois fois. La peur "
                  "des appareils est un vrai obstacle d'emploi, et elle est réparable.")

    d.objectifs([
        "chercher dans un mode d'emploi la seule page qui concerne sa tâche ;",
        "comprendre une marche à suivre en trois ou quatre gestes ;",
        "distinguer le chargeur du bac à papier ;",
        "savoir ce qu'un livret ne dira jamais, et qu'un collègue sait.",
    ])

    d.declencheur(
        'Observation', "Un appareil neuf au bout d'un corridor. Par où "
                       "commencez-vous ?",
        image=IMG + 'photocopieur-corridor.jpg',
        pistes=[
            "Est-ce qu'on lit un mode d'emploi du début à la fin ?",
            "Qu'est-ce qu'on cherche en premier dans un livret épais ?",
            "Qui, dans un lieu de travail, sait vraiment se servir des appareils ?",
            "Que se passe-t-il quand personne n'a écrit la marche à suivre ?",
        ],
        notes="La troisième piste amène toujours la même réponse : ce n'est jamais la "
              "personne prévue, c'est un collègue qui a appris tout seul. Le défi 2 "
              "consiste à mettre ce que ce collègue sait par écrit.")

    d.dialogue('Dialogue · 1 de 3', "Chercher sa page", [
        ("KEVIN", "Tu as vu ? Ils ont changé le photocopieur pendant la fin de "
                  "semaine.", True),
        ("DORINE", "J'ai vu. Et j'ai vu aussi que personne ne sait s'en servir.", True),
        ("KEVIN", "Il y a le livret, là, sur la tablette.", True),
        ("DORINE", "Quatre-vingts pages. En deux langues. Je cherche seulement à "
                   "numériser une feuille et à me l'envoyer par courriel.", True),
        ("KEVIN", "Regarde la table des matières. Tu ne lis jamais un mode d'emploi "
                  "du début à la fin : tu cherches ta page.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="La dernière réplique de Kevin est une stratégie de lecture, et c'est "
             "l'intention de compréhension écrite du programme : « lire un mode "
             "d'emploi ». On ne le lit pas, on y cherche.")

    d.dialogue('Dialogue · 2 de 3', "Trois gestes, page trente-quatre", [
        ("DORINE", "« Numérisation vers un courriel », page trente-quatre. Bon. "
                   "« Placer le document face vers le haut dans le chargeur. »", True),
        ("KEVIN", "Le chargeur, c'est le bac du dessus. Le bac à papier, lui, c'est "
                  "le tiroir d'en bas.", True),
        ("DORINE", "« Appuyer sur Numériser. Entrer l'adresse courriel. Confirmer. » "
                   "C'est tout ?", True),
        ("KEVIN", "C'est tout. Trois gestes.", True),
    ], notes="Faire remarquer que le livret emploie l'infinitif — placer, appuyer, "
             "entrer, confirmer — et que Kevin, lui, parle à l'impératif. C'est le sujet "
             "de la séance C4 ; l'annoncer sans le développer.")

    d.dialogue('Dialogue · 3 de 3', "Écrire la demi-page qui manque", [
        ("DORINE", "Trois gestes et une page trente-quatre. Kevin, tu as combien de "
                   "temps devant toi ?", True),
        ("KEVIN", "Dix minutes. Pourquoi ?", True),
        ("DORINE", "On écrit une demi-page. Les quatre choses que le monde fait ici : "
                   "copier, numériser, changer le papier, débloquer une feuille "
                   "coincée. Et on la colle sur le mur.", True),
        ("KEVIN", "Ghislain va aimer ça.", True),
        ("DORINE", "Ghislain va surtout arrêter d'être dérangé quatre fois par jour.", False),
    ], notes="C'est le programme des trois séances qui suivent : les quatre opérations "
             "nommées par Dorine sont exactement celles que les élèves écriront en C3 et "
             "C4. Le dire.")

    d.regle("On ne lit pas un mode d'emploi, on y cherche",
            "Table des matières, numéro de page, trois lignes. Le reste ne "
            "vous concerne pas aujourd'hui.",
            precision="Un livret d'appareil est écrit pour tous les usages et pour "
                      "tous les modèles. Chercher sa page n'est pas de la paresse : "
                      "c'est la façon dont ces textes sont faits pour être lus.",
            notes="Beaucoup d'élèves ont appris qu'il faut tout lire. Le dire "
                  "explicitement les soulage, et améliore leur lecture tout de suite.")

    d.tableau('Deux tiroirs, deux usages', "La confusion la plus fréquente",
              ['Le chargeur', 'Le bac à papier'],
              [["En haut, sur le dessus", "En bas, un tiroir"],
               ["Reçoit ce qu'on veut copier", "Reçoit les feuilles blanches"],
               ["Se vide après chaque usage", "Se remplit quand il est vide"],
               ["On y oublie son original", "On s'y trompe de format"]],
              cle=0,
              notes="Faire le geste avec les mains : un plateau en haut, un tiroir en "
                    "bas. Les élèves retiennent le geste plus longtemps que les mots.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Le photocopieur a été remplacé pendant la fin de semaine.", "vrai"),
        ("Le livret de l'appareil fait une dizaine de pages.", "faux — quatre-vingts"),
        ("Kevin conseille de lire le mode d'emploi du début à la fin.", "faux — de chercher sa page"),
        ("Le chargeur est le bac du dessus.", "vrai"),
        ("Pour numériser vers un courriel, il faut trois gestes.", "vrai"),
        ("Dorine veut coller une demi-page sur le mur.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. La troisième fait "
             "toujours discuter : c'est le contraire de ce qu'on a appris à l'école.")

    d.billet(
        "Nommez un appareil de votre quotidien dont vous n'avez jamais lu le mode "
        "d'emploi.",
        exemples=[
            "Écrivez une chose que vous ne savez pas faire avec.",
            "Écrivez la question exacte que vous chercheriez dans la table des matières.",
        ],
        notes="La dernière consigne est l'exercice réel : formuler sa question avant de "
              "chercher. C'est ce qui distingue une recherche de trente secondes d'une "
              "demi-heure de feuilletage.")

    return d.save(dossier)
