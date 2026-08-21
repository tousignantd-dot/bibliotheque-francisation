# -*- coding: utf-8 -*-
"""D1 · Numéro 42 !
Bloc D « Défi 3 · Comprendre le préposé » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3vf` et `t3demander`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-restaurant/images/')


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre='Numéro 42 !',
        chapeau="Le repas est prêt, et il manque une cuillère. C'est le moment "
                "du module où un élève renonce et repart sans rien dire. "
                "Trois phrases suffisent à l'éviter.",
        duree='75 minutes')

    d.titre(notes="Première séance du défi 3. Elle porte sur le moment le plus court du "
                  "repas et le plus souvent raté : le poste de ramassage.")

    d.objectifs([
        "reconnaître son numéro appelé dans le bruit ;",
        "dire qu'il manque quelque chose sur le plateau ;",
        "demander où se trouvent les ustensiles et les serviettes ;",
        "signaler poliment une erreur de commande.",
    ])

    d.declencheur(
        'Observation', "Il manque quelque chose. On fait quoi ?",
        image=IMG + 'plateau-repas.jpg',
        pistes=[
            "Qu'est-ce qu'il y a sur ce plateau ?",
            "Qu'est-ce qui manque pour manger la soupe ?",
            "Est-ce qu'on peut aller le chercher soi-même ?",
            "Et si le breuvage manquait, on dirait quoi ?",
        ],
        notes="Laisser le groupe chercher la phrase avant de la donner. Beaucoup "
              "proposent une phrase longue et hésitante : c'est exactement ce que la "
              "séance vient corriger.")

    d.dialogue('Dialogue · 1 de 3', "C'est moi", [
        ("MARCEL", "Numéro 42 ! Le trio poulet, numéro 42 !", True),
        ("YOLETTE", "C'est moi. Bonjour.", True),
        ("MARCEL", "Voilà. Le sandwich, la salade, le jus. Et votre petite soupe.", True),
        ("YOLETTE", "Merci. Excusez-moi, je n'ai pas de cuillère pour la soupe.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="« C'est moi » suffit pour se présenter au comptoir. La quatrième réplique "
             "est la phrase centrale de la séance : la faire répéter tout de suite.")

    d.dialogue('Dialogue · 2 de 3', "Servez-vous", [
        ("MARCEL", "Les ustensiles sont là, à votre gauche, dans les bacs.", True),
        ("YOLETTE", "D'accord. Est-ce qu'il y a des serviettes de table aussi ?", True),
        ("MARCEL", "Oui, juste à côté. Prenez-en deux, la soupe est pleine.", True),
        ("YOLETTE", "Merci. Et est-ce que je peux avoir du sel et du poivre ?", True),
    ], notes="Trois demandes en quatre répliques, toutes construites pareil. Le faire "
             "remarquer : c'est une formule, pas trois phrases à apprendre.")

    d.dialogue('Dialogue · 3 de 3', "Il manque le jus", [
        ("MARCEL", "Servez-vous. Il y a aussi de la moutarde et du ketchup au bout.", True),
        ("YOLETTE", "Une dernière chose. Il manque le jus dans mon plateau.", True),
        ("MARCEL", "Ah, excusez-moi. Vous avez pris quoi ? Un jus de pomme ?", True),
        ("YOLETTE", "Oui, un jus de pomme.", True),
    ], notes="Yolette signale calmement, en une phrase, et le problème se règle en dix "
             "secondes. C'est le modèle à imiter.")

    d.regle("Signaler tient en une phrase",
            "« Excusez-moi, il manque le jus. »",
            precision="Courte, calme, et on attend. Plus la phrase est longue, "
                      "moins elle est claire dans le bruit — et plus elle a "
                      "l'air d'une plainte. Ce n'en est pas une : c'est un "
                      "renseignement.",
            notes="Diapo à photographier. Faire dire la phrase à voix haute par chaque "
                  "élève, sur un ton neutre. Le ton compte autant que les mots.")

    d.tableau('Analyse', "Quatre phrases qui règlent presque tout",
              ['La situation', "Ce qu'on dit"],
              [["il manque un ustensile", "Je n'ai pas de cuillère."],
               ["il manque un plat", "Il manque le jus."],
               ["on cherche quelque chose", "Où sont les serviettes ?"],
               ["ce n'est pas la bonne commande", "Ce n'est pas ma commande."]],
              cle=1,
              note="Après « je n'ai pas », toujours « de » : pas de cuillère.",
              notes="Diapo à photographier. Faire recopier les quatre phrases dans le "
                    "cahier, telles quelles. Elles s'apprennent par cœur.")

    d.regle("« Servez-vous » est une invitation",
            "« — Où sont les serviettes ? — Servez-vous. »",
            precision="Ça veut dire : prenez-en vous-même, autant qu'il vous "
                      "en faut. Ce n'est ni un refus ni un reproche. Les "
                      "ustensiles, les serviettes et les condiments sont "
                      "presque toujours en libre-service.",
            notes="Diapo à photographier. C'est l'information la plus utile du module "
                  "pour un élève qui n'ose pas se servir.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Marcel appelle le numéro à voix haute.", "vrai"),
        ("Yolette a déjà une cuillère sur son plateau.", "faux — elle en demande une"),
        ("Les ustensiles sont dans des bacs, à gauche.", "vrai"),
        ("Il faut demander la moutarde au préposé.", "faux — servez-vous"),
        ("Il manque le jus sur le plateau de Yolette.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte du dialogue.")

    d.billet(
        "Écrivez trois phrases pour trois choses qui manquent.",
        exemples=[
            "Une cuillère, une serviette, un breuvage.",
            "Commencez par « Excusez-moi ».",
        ],
        notes="Devoir court. Il prépare la séance D2, sur les condiments et sur ce que "
              "le préposé répond quand il n'en reste plus.")

    return d.save(dossier)
