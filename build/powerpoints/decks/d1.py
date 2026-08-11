# -*- coding: utf-8 -*-
"""D1 · Quatre situations inacceptables.
Bloc D · couleur acier (compréhension orale) · 55 min.
Source : dialogue `t3` (quatre témoignages), exercices `t3q` et `t3assoc`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre='Quatre situations inacceptables',
        chapeau="Quatre personnes de l'immeuble décrivent une situation qu'elles ne "
                "tolèrent plus : les ordures, le bruit, le stationnement, l'odeur. "
                "Écoutez comment chacune s'y prend.",
        duree='55 minutes')

    d.titre(notes="Ouverture du bloc D. Quatre témoignages indépendants, à écouter d'abord "
                  "en entier, puis un par un. Prévoir que le groupe reconnaisse ses propres "
                  "situations : laisser un peu de place à ça.")

    d.objectifs([
        "comprendre quatre témoignages sur des problèmes de voisinage ;",
        "repérer dans chacun le fait, l'effet sur la personne et la demande ;",
        "constater qu'une description n'est pas encore une plainte ;",
        "reconnaître la situation à partir d'un seul énoncé.",
    ])

    d.dialogue('Situation 1', "Le local à ordures", [
        ("CAMILLE", "Le local à ordures est au bout du corridor du sous-sol. Depuis que le bac de recyclage est plein, les gens déposent leurs boîtes par terre, devant la porte. Il y a des restes de nourriture dans le tas et ça sent mauvais jusque dans l'escalier. Je pense que ça peut attirer de la vermine.", True),
    ], consigne="Écoutez d'abord, diapo masquée. Cherchez : le fait, l'effet, la demande.",
       notes="Faire chercher la demande. Il n'y en a pas — Camille décrit et s'inquiète, "
             "mais ne demande rien. C'est exactement ce qu'on travaillera à la séance D2. "
             "Ne pas le dire tout de suite : laisser le groupe s'en apercevoir.")

    d.dialogue('Situation 2', "Le bruit du vendredi soir", [
        ("OKSANA", "Mes voisins du dessous reçoivent des amis presque tous les vendredis. Ils mettent la musique très fort et ils rient sur le balcon jusqu'à deux heures du matin. Moi, je commence à sept heures à la pharmacie. Ça fait cinq semaines que ça dure et je ne peux plus le tolérer.", True),
    ], notes="Ici, l'effet sur la personne est explicite : elle commence à sept heures. "
             "Et la formule « je ne peux plus le tolérer » est une vraie plainte. "
             "Mais il manque encore la demande.")

    d.dialogue('Situation 3', "Le stationnement", [
        ("JEAN-PHILIPPE", "Les visiteurs du 2C se stationnent dans les cases réservées aux locataires. La semaine passée, j'ai dû laisser mon auto dans la rue trois soirs de suite. Je demande à la propriétaire de faire installer une affiche à l'entrée du stationnement.", True),
    ], notes="C'est le seul des quatre témoignages complet : fait, effet, demande précise. "
             "Le faire remarquer. Noter aussi la structure « faire installer » de la "
             "séance C3.")

    d.dialogue('Situation 4', "L'odeur de dégraissant", [
        ("SAMIR", "L'atelier de vélos du rez-de-chaussée utilise un produit dégraissant très fort. L'odeur monte par la cage d'escalier et entre dans les logements du premier étage. Les fenêtres du corridor ne s'ouvrent pas. C'est vraiment désagréable, surtout le samedi matin.", True),
    ], notes="Samir explique aussi pourquoi le problème persiste : les fenêtres ne s'ouvrent "
             "pas. Une bonne plainte contient souvent la cause, pas seulement le symptôme.")

    d.tableau('Analyse', "Ce que contient chaque témoignage",
              ['Situation', 'Le fait', 'La demande ?'],
              [["1 · les ordures", "des boîtes par terre, ça sent mauvais", "aucune"],
               ["2 · le bruit", "musique jusqu'à deux heures", "aucune"],
               ["3 · le stationnement", "des visiteurs dans les cases", "une affiche à l'entrée"],
               ["4 · l'odeur", "un dégraissant très fort", "aucune"]],
              cle=2,
              note="Trois témoignages sur quatre n'aboutiront probablement à rien. Ce n'est "
                   "pas parce qu'ils sont mal dits : c'est parce qu'il leur manque la "
                   "dernière phrase.",
              notes="Diapo pivot de tout le bloc D. Laisser le groupe réagir avant de "
                    "commenter.")

    d.pratique('Pratique', 'Les quatre situations',
               "Répondez par une phrase complète.", [
        ("Situation 1 — Où les gens déposent-ils leurs boîtes ?",
         "Par terre, devant la porte du local à ordures."),
        ("Situation 1 — Qu'est-ce que Camille craint que cela attire ?", "De la vermine."),
        ("Situation 2 — Depuis combien de temps la situation dure-t-elle ?",
         "Depuis cinq semaines."),
        ("Situation 2 — Pourquoi le bruit dérange-t-il autant Oksana ?",
         "Parce qu'elle commence à travailler à sept heures le matin."),
    ], corrige=True,
       notes="Exiger la phrase complète, pas le mot seul. C'est un exercice de production "
             "orale déguisé en compréhension.")

    d.pratique('Pratique', 'Suite',
               "Même consigne.", [
        ("Situation 3 — Quel est le problème avec les visiteurs du 2C ?",
         "Ils se stationnent dans les cases réservées aux locataires."),
        ("Situation 3 — Que demande Jean-Philippe à la propriétaire ?",
         "De faire installer une affiche à l'entrée du stationnement."),
        ("Situation 4 — Par où l'odeur monte-t-elle ?", "Par la cage d'escalier."),
        ("Situation 4 — Pourquoi l'odeur reste-t-elle dans le corridor ?",
         "Parce que les fenêtres du corridor ne s'ouvrent pas."),
    ], corrige=True)

    d.pratique('Pratique', "À quelle situation cet énoncé correspond-il ?",
               "Un seul énoncé suffit à reconnaître la situation.", [
        ("Ça m'empêche de dormir avant mon quart du matin.", "situation 2 — le bruit"),
        ("Ça peut attirer de la vermine et devenir insalubre.", "situation 1 — les ordures"),
        ("Je dois laisser mon auto dans la rue trois soirs de suite.", "situation 3 — le stationnement"),
        ("L'odeur entre dans les logements et ne part pas.", "situation 4 — le dégraissant"),
    ], corrige=True,
       notes="Faire remarquer que les quatre énoncés retenus sont tous des effets sur la "
             "personne, jamais des faits bruts. C'est ce qui les rend reconnaissables — et "
             "c'est ce qui donne envie d'agir.")

    d.regle('Ce que la séance a montré',
            "Décrire une situation ne suffit pas à la faire changer.",
            precision="Les quatre personnes ont raison, et toutes décrivent bien. Mais trois "
                      "sur quatre s'arrêtent avant la dernière phrase — celle qui dit ce "
                      "qu'on attend. C'est cette phrase qu'on apprend à écrire à la "
                      "prochaine séance.",
            notes="Fermer la séance là-dessus, sans donner la formule en trois temps : "
                  "elle ouvre la séance D2.")

    d.billet(
        "Reprenez le problème de partie commune que vous avez écrit à la séance C1.",
        exemples=[
            "Ajoutez une phrase : l'effet que ça a sur vous, personnellement.",
            "Exemple : « Les machines restent pleines toute la journée. Je dois refaire ma lessive le soir. »",
        ],
        notes="Rendre les billets de la séance C1 au début du cours. Ces billets, complétés, "
              "serviront de matière première à la séance D2.")

    return d.save(dossier)
