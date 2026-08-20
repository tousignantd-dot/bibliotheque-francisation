# -*- coding: utf-8 -*-
"""C2 · Prenez-la, ne la lâchez pas.
Bloc C · couleur ambre (écriture) · 90 min.
Source : mini-leçon `t2imper`, exercice `t2imper`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre='Prenez-la, ne la lâchez pas',
        chapeau="Le même verbe, le même pronom — et deux places différentes. "
                "C'est la seule chose à comprendre, et c'est ce qui rend les "
                "consignes du moniteur difficiles à suivre.",
        duree='90 minutes')

    d.titre(notes="Séance de grammaire longue. Écrire les deux phrases du chapeau au "
                  "tableau, l'une sous l'autre, et demander ce qui change.")

    d.objectifs([
        "placer le pronom après le verbe à la forme affirmative ;",
        "le placer avant le verbe à la forme négative ;",
        "employer moi et toi à l'affirmative, me et te à la négative ;",
        "reconnaître deux pronoms enchaînés : donne-les-leur.",
    ])

    d.tableau('Analyse', "Une règle, deux places",
              ['La forme', 'Où va le pronom'],
              [["Affirmative", "après le verbe, avec un trait d'union"],
               ["Négative", "avant le verbe, sans trait d'union"]],
              cle=0,
              note="Prenez-la. / Ne la lâchez pas. Le même mot, deux places.",
              notes="Diapo centrale. Très courte volontairement : toute la leçon tient en "
                    "deux lignes. Faire recopier.")

    d.regle("À l'affirmative : le pronom suit",
            "Il se colle après le verbe, avec un trait d'union.",
            precision="« Prenez-la. » · « Compte-les. » · « Envoie-le à la douche. » · "
                      "« Laissez-les au bord. » Le trait d'union n'est pas décoratif : il "
                      "montre que le pronom remplace le nom.",
            notes="Sans trait d'union, « prenez la » attend un nom. Le faire remarquer : "
                  "c'est une raison, pas une convention arbitraire.")

    d.regle("À la négative : le pronom précède",
            "Il repasse devant le verbe, et le trait d'union disparaît.",
            precision="« Ne la lâchez pas. » · « Ne les jetez pas. » · « Ne le cherche pas "
                      "toi-même. » Le « ne » et le « pas » entourent l'ensemble "
                      "pronom + verbe.",
            notes="C'est l'erreur numéro un : on garde en tête la forme affirmative et on "
                  "écrit « ne lâchez-la pas ». Y consacrer du temps.")

    d.regle('me devient moi, te devient toi',
            "À l'affirmative seulement.",
            precision="« Regarde-moi. » · « Assieds-toi. » · « Mets-toi à côté de Sofia. » "
                      "Mais à la négative, ils reprennent leur forme courte : « ne me "
                      "regarde pas », « ne te lève pas ».",
            notes="C'est la seule irrégularité de la séance, et elle ne touche que deux "
                  "pronoms.")

    d.piege('Garder le pronom après le verbe à la négative',
            "Ne lâchez-la pas !",
            "Ne la lâchez pas !",
            "À la négative, tout revient devant le verbe. C'est la faute la plus fréquente, "
            "parce qu'on a la forme affirmative en tête. Le repère : s'il y a un « ne », "
            "le pronom est <b>avant</b>.",
            notes="Écrire le repère au tableau et l'y laisser : « s'il y a un ne, le pronom "
                  "est avant ».")

    d.pratique('Pratique · 1 de 2', "Remplacez par un pronom",
               "Récrivez la consigne à la forme affirmative.", [
        ("Prenez la planche à deux mains.", "Prenez-la à deux mains."),
        ("Laissez les planches au bord.", "Laissez-les au bord."),
        ("Compte les enfants quand ils entrent.", "Compte-les quand ils entrent."),
        ("Envoie l'enfant à la douche chaude.", "Envoie-le à la douche chaude."),
        ("Regarde le moniteur.", "Regarde-le."),
    ], corrige=True, cols=1,
       notes="Vérifier le trait d'union à chaque ligne. C'est ce qui distingue la forme "
             "juste de la forme approximative.")

    d.pratique('Pratique · 2 de 2', "Maintenant à la négative",
               "Récrivez la même consigne, en négatif.", [
        ("Ne lâchez pas la planche.", "Ne la lâchez pas."),
        ("Ne jetez pas les planches dans l'eau.", "Ne les jetez pas dans l'eau."),
        ("Ne cherche pas l'enfant toi-même.", "Ne le cherche pas toi-même."),
        ("Ne donne pas les serviettes avant la sortie.", "Ne les donne pas avant la sortie."),
        ("Ne ferme pas les yeux.", "Ne les ferme pas."),
    ], corrige=True, cols=1,
       notes="Faire venir cinq élèves au tableau. Demander à chacun de dire où va le "
             "pronom avant d'écrire.")

    d.cartes('Deux pronoms ensemble', "La forme la plus difficile", [
        ("L'exemple du module",
         "« Donne les serviettes aux enfants » devient « Donne-les-leur. » Deux pronoms, "
         "deux traits d'union."),
        ("L'ordre",
         "Verbe, puis <b>le / la / les</b>, puis <b>moi / lui / leur</b>. Toujours dans "
         "cet ordre."),
        ("Ce qu'on vous demande",
         "La reconnaître, pas la produire. « Donne les serviettes aux enfants » est "
         "parfaitement correct et beaucoup plus simple."),
    ], notes="Le dire clairement : personne n'est obligé d'employer cette forme. Mais on "
             "l'entend, et il faut la comprendre.")

    d.billet(
        "Écrivez six consignes pour une activité : trois affirmatives, trois négatives.",
        exemples=[
            "Chacune doit contenir un pronom : le, la, les, moi ou toi.",
            "Vérifiez le trait d'union à l'affirmative, et son absence à la négative.",
        ],
        notes="Corriger individuellement. Ces consignes servent à la production orale de "
              "E1 — expliquer une activité qu'on connaît.")

    return d.save(dossier)
