# -*- coding: utf-8 -*-
"""D2 · Mettre en avant, et s'exclamer
Bloc D « Défi 3 · Dire ce qu'on en pense » · couleur ambre · 75 min.
Grammaire et écriture. Source : exercices `t3disl`, `t3quel` et
`t3nuance`, et leurs mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="Mettre en avant, et s'exclamer",
        chapeau="« Le silence entre les deux sœurs m'a touchée » est "
                "correct. « Moi, ce qui m'a touchée, c'est le silence entre "
                "les deux sœurs » se retient. Deux tournures, et une "
                "présentation change de niveau.",
        duree='75 minutes')

    d.titre(notes="Dernière séance avant « Je me lance ». Rendre les billets de D1 au "
                  "début : chacun a déjà son adjectif et sa raison, et la séance "
                  "d'aujourd'hui lui apprend à les placer.")

    d.objectifs([
        "employer « moi, ce qui…, c'est… » pour mettre son avis en avant ;",
        "choisir entre « ce qui » et « ce que » ;",
        "accorder quel, quelle, quels, quelles avec le nom qui suit ;",
        "écrire un avis en cinq phrases, réserve comprise.",
    ])

    d.regle("Moi, ce qui m'a touchée, c'est…",
            "La tournure déplace vers la fin le mot qui compte, et prévient qu'il s'en vient.",
            precision="Comparez : « Le silence entre les deux sœurs m'a touchée » et "
                      "« Moi, ce qui m'a touchée, c'est le silence entre les deux "
                      "sœurs ». La seconde annonce clairement que ce qui suit est un "
                      "avis, et elle vous donne une seconde pour penser à la suite — "
                      "ce qui, devant un groupe, n'est pas rien.",
            notes="Diapositive à photographier. Le « moi » détaché n'est pas une "
                  "faute : c'est du français parlé du Québec parfaitement correct. À "
                  "l'écrit, il se remplace par « personnellement » ou « à mon avis ».")

    d.tableau('Analyse', "Ce qui, ou ce que ?",
              ["La phrase", "Pourquoi"],
              [["Ce qui m'a plu, c'est le dessin.", "le dessin plaît : il fait l'action"],
               ["Ce que j'ai aimé, c'est la fin.", "c'est moi qui aime : un sujet suit"],
               ["Ce qui me dérange, c'est que…", "suite = phrase complète, d'où le que"],
               ["Ce que les gens remarquent, c'est…", "les gens remarquent : sujet"]],
              cle=1,
              note="Même test que pour les relatives du Défi 1 : après « que », il y a "
                   "toujours un sujet.",
              notes="Diapositive à photographier. Le test du sujet est le seul à "
                    "retenir : il règle « qui / que » ici comme au Défi 1, et les "
                    "élèves qui l'ont compris là-bas le retrouvent tout de suite.")

    d.pratique('Grammaire', "Ce qui, ce que, c'est",
               "Complétez chaque phrase.", [
        ("Moi, ___ m'a touchée, c'est le silence entre les deux sœurs.", "ce qui"),
        ("___ j'ai le moins aimé, c'est la longueur des trois derniers chapitres.", "Ce que"),
        ("Ce qui m'a surprise, ___ la lenteur du début.", "c'est"),
        ("___ me dérange, c'est que la fin arrive trop vite.", "Ce qui"),
        ("Ce que les gens remarquent d'abord, ___ le dessin.", "c'est"),
        ("___ fait la force de cet album, c'est le silence des cases.", "Ce qui"),
    ], corrige=True, cols=2,
       notes="Ce sont les six items de l'exercice `t3disl`. Faire dire chaque phrase à "
             "voix haute une fois corrigée : la tournure s'installe par l'oreille, pas "
             "par la règle.")

    d.regle("Quel s'accorde avec le nom qui suit",
            "Quel personnage ! Quelle histoire ! Quels dessins ! Quelles couleurs !",
            precision="Les quatre se prononcent exactement pareil : l'accord ne "
                      "s'entend pas, il s'écrit. Et si un adjectif se glisse au "
                      "milieu — quelle belle planche —, c'est toujours le nom, à la "
                      "fin, qui commande tout le groupe.",
            notes="Diapositive à photographier. Dans une présentation de deux minutes, "
                  "une seule exclamation bien placée fait plus qu'un paragraphe "
                  "d'adjectifs. Le dire au groupe : une, pas cinq.")

    d.cartes("Deux emplois des mêmes mots", "Ce qui les distingue", [
        ("La question",
         "Quelle est votre œuvre préférée ? La voix monte à la fin, et la phrase "
         "attend une réponse."),
        ("L'exclamation",
         "Quelle œuvre ! La voix tombe, et la phrase n'attend rien : elle dit le "
         "degré."),
    ], cols=2, notes="Faire dire les deux phrases au groupe, l'une après l'autre, "
                     "sans les écrire. La différence de voix s'entend tout de suite et "
                     "ne s'oublie plus.")

    d.pratique('Grammaire', "S'exclamer : quel, quelle, quels, quelles",
               "Complétez chaque exclamation.", [
        ("___ belle façon de le dire !", "Quelle"),
        ("___ personnage ! Je ne l'oublierai pas de sitôt.", "Quel"),
        ("___ couleurs dans le dernier tome de la série !", "Quelles"),
        ("___ beaux dessins il y a dans cet album !", "Quels"),
        ("___ histoire ! Je l'ai lue en deux soirées.", "Quelle"),
        ("___ dénouement ! Je ne vous en dis pas un mot.", "Quel"),
    ], corrige=True, cols=2,
       notes="Ce sont les six items de `t3quel`. Faire souligner le nom dans chaque "
             "phrase avant de choisir : l'accord se décide là, jamais ailleurs.")

    d.pratique('Écriture', "Donnez votre avis, et tenez-le",
               "Cinq phrases, sur l'œuvre du Défi 1. Interdiction d'écrire "
               "« c'est bon ».", [
        ("1 — Ce que vous avez aimé, avec un adjectif précis.",
         "Moi, ce qui m'a touché, c'est…"),
        ("2 — La raison qui vient derrière.",
         "…parce que le temps du livre est le temps du village."),
        ("3 — Une chose moins aimée, dite sans démolir l'œuvre.",
         "Ce que j'ai le moins aimé, c'est…"),
        ("4 — Quelqu'un trouve ça trop lent : accordez, puis tournez.",
         "C'est vrai que c'est lent. Par contre,…"),
        ("5 — À qui vous le recommandez, et pourquoi à cette personne-là.",
         "Je le recommande à quelqu'un qui…"),
    ], corrige=True,
       notes="Ce sont les cinq étapes de l'exercice `t3nuance`. Les corrigés sont des "
             "amorces, pas des réponses : lire trois productions d'élèves à voix haute "
             "avant de les afficher. Ces cinq phrases sont le temps 4 et le temps 5 de "
             "la présentation de E1 — le dire au groupe, ça change l'effort qu'on y "
             "met.")

    d.billet(
        "Réécrivez votre avis de D1 avec « moi, ce qui…, c'est… » et une exclamation.",
        exemples=[
            "Une seule exclamation, bien placée.",
            "Relisez-vous : est-ce qu'on sait ce qui est bon, et pour qui ?",
        ],
        notes="Ramasser les billets et les rendre au début de E1 : ils sont deux des "
              "cinq temps de la présentation, déjà écrits.")

    return d.save(dossier)
