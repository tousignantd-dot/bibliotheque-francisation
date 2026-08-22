# -*- coding: utf-8 -*-
"""B2 · Est-ce que je peux, est-ce que je pourrais.
Bloc B « Défi 1 · Est-ce que je peux ? » · couleur ambre (écriture) · 60 min.
Source : exercice `t1perm`, mini-leçon `t1perm`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre="Est-ce que je peux, est-ce que je pourrais",
        chapeau="Un seul morceau de mot sépare la demande de tous les jours "
                "de la demande polie. C'est le morceau qui décide de la "
                "réponse quand on connaît peu la personne.",
        duree='60 minutes')

    d.titre(notes="Séance d'écriture. Reprendre les demandes ramassées au billet de B1 : "
                  "chacun travaillera la sienne plutôt qu'un exemple inventé.")

    d.objectifs([
        "demander une permission de trois façons ;",
        "choisir la forme polie quand on connaît peu la personne ;",
        "employer le nom « permission » et l'adjectif « permis » ;",
        "ne plus dire « je veux » à la place de « je peux ».",
    ])

    d.regle("Le -rais adoucit tout",
            "Est-ce que je peux…  →  Est-ce que je pourrais…",
            precision="La première forme est courte, directe et parfaitement "
                      "correcte entre voisins. La seconde est celle qu'on "
                      "emploie avec quelqu'un qu'on connaît peu, ou quand on "
                      "demande quelque chose d'un peu plus gros.",
            notes="Diapo à photographier. Faire dire les deux versions de la même "
                  "demande, l'une après l'autre : la différence de ton s'entend "
                  "immédiatement, même sans explication.")

    d.tableau('Analyse', "Quatre façons de demander",
              ["La formule", "Quand l'employer"],
              [["Est-ce que je peux… ?", "tous les jours, avec quelqu'un qu'on connaît"],
               ["Est-ce que je pourrais… ?", "plus poli — avec quelqu'un qu'on connaît peu"],
               ["Est-ce que vous pourriez… ?", "quand c'est l'autre qui doit faire quelque chose"],
               ["Est-ce que vous permettez que… ?", "la plus formelle — devant le concierge"]],
              cle=1,
              note="La troisième déplace la demande : « je peux » demande pour "
                   "soi, « vous pourriez » demande à l'autre.",
              notes="Diapo à photographier. Faire trouver un exemple de la troisième "
                    "ligne : « Est-ce que vous pourriez me prêter la clé deux minutes ? »")

    d.tableau('Analyse', "Le mot permission et sa famille",
              ["Le mot", "Comment il s'emploie"],
              [["la permission", "on la demande, on la donne, on la refuse"],
               ["permettre", "Est-ce que vous permettez que je passe par la cour ?"],
               ["permis", "Ce n'est pas permis de bloquer la sortie de secours."],
               ["Il faut la permission de…", "quand quelqu'un d'autre décide"]],
              cle=1,
              note="« La permission », c'est le droit qu'on te donne — pas la "
                   "phrase qui le demande.",
              notes="Diapo à photographier. La quatrième ligne prépare le passage chez le "
                    "concierge : il y a des permissions que le voisin ne peut pas donner.")

    d.pratique('Écriture', "Complétez la demande",
               "Employez « peux », « pourrais », « permis », « pouvez » ou "
               "« permission ».", [
        ("Est-ce que je ___ mettre mon vélo dans la remise ?", "peux"),
        ("Est-ce que je ___ l'accrocher au mur du fond ?", "pourrais"),
        ("J'ai demandé la ___ avant de toucher à la remise.", "permission"),
        ("Ce n'est pas ___ de bloquer la sortie de secours.", "permis"),
        ("Est-ce que vous ___ me prêter la clé deux minutes ?", "pouvez / pourriez"),
        ("Il faut la ___ du concierge pour entrer dans la remise.", "permission"),
    ], corrige=True,
       notes="C'est l'exercice `t1perm` du module interactif. Le faire par écrit ici, "
             "puis à l'écran. Insister sur la deuxième ligne : c'est la forme du jeu de "
             "rôle.")

    d.piege("Dire « je veux » à la place de « je peux »",
            "Je veux mettre mon vélo dans la remise.",
            "Est-ce que je peux mettre mon vélo dans la remise ?",
            "« Je veux » annonce une décision, pas une demande : entre voisins, il "
            "sonne comme une porte qu'on pousse. Les deux mots se ressemblent à "
            "l'oreille, et l'erreur coûte cher pour une seule lettre.",
            notes="Faire dire la paire « je veux / je peux » à voix haute. La différence "
                  "est une voyelle, et elle change tout le ton de la phrase.")

    d.cartes("Ce qui entoure la demande", "Trois phrases à savoir par cœur", [
        ("Avant : la politesse",
         "« Excusez-moi de vous déranger. » Elle prévient qu'on prend du temps à "
         "quelqu'un, et elle ouvre toutes les portes."),
        ("Avant : la raison",
         "« Mon vélo gêne dans le corridor. » Une demande sans raison inquiète. Une "
         "phrase suffit, jamais deux."),
        ("Après : le remerciement",
         "« Merci, c'est gentil. » Même si la réponse est non. C'est ce qui rend la "
         "prochaine demande possible."),
        ("Et si c'est non",
         "On remercie et on cherche autre chose. Insister coûte la permission suivante — "
         "et dans un immeuble, on se recroise tous les jours."),
    ], notes="Faire écrire les trois phrases dans le cahier, dans l'ordre. C'est le "
             "squelette de toute la production orale de E1.")

    d.pratique('Production', "Deux par deux : demandez, répondez",
               "L'un demande, l'autre répond par « bien sûr », « oui, mais » ou "
               "« je préfère que non ».", [
        ("La remise, pour un vélo.", "Est-ce que je peux… ? — Bien sûr, allez-y."),
        ("La corde à linge, un jour de beau temps.", "Est-ce que je pourrais… ?"),
        ("Passer par la cour avec une poussette.", "Est-ce que vous permettez que… ?"),
        ("Laisser une boîte dans le corridor deux jours.", "Je préfère que non, et voici pourquoi."),
        ("Emprunter la clé de la remise dix minutes.", "Est-ce que vous pourriez me prêter… ?"),
    ], corrige=False,
       notes="Quinze minutes, puis on inverse les rôles. Ne corriger que la forme de la "
             "demande : la réponse se travaille en B3.")

    d.billet(
        "Écrivez votre demande au complet, en trois phrases.",
        exemples=[
            "La politesse, la raison, la demande.",
            "« Excusez-moi de vous déranger. Ma poussette bloque l'entrée. Est-ce que je pourrais… ? »",
        ],
        notes="Devoir court. Ramasser : ces trois phrases sont exactement ce que l'élève "
              "dira dans sa production orale de E1.")

    return d.save(dossier)
