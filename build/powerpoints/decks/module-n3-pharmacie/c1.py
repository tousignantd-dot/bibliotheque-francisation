# -*- coding: utf-8 -*-
"""C1 · Il me reste deux comprimés.
Bloc C « Défi 2 · Renouveler l'ordonnance » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t2vf`.

Seconde intention du programme en production orale : « demander le
renouvellement de l'ordonnance d'un médicament ».
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-pharmacie/images/')


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre='Il me reste deux comprimés',
        chapeau="Le flacon est presque vide et l'ordonnance est finie. Au "
                "Québec, il n'est pas toujours nécessaire de revoir le "
                "médecin : le pharmacien peut prolonger l'ordonnance lui-même.",
        duree='75 minutes')

    d.titre(notes="Première séance du défi 2. Le fait central de la séance est vérifié "
                  "et récent : depuis 2021, un pharmacien peut prolonger une ordonnance "
                  "qui vient à échéance, sans dépasser un an. Beaucoup d'élèves "
                  "l'ignorent et cessent leur traitement en attendant un rendez-vous.")

    d.objectifs([
        "demander un renouvellement d'ordonnance ;",
        "donner son nom et sa carte d'assurance maladie ;",
        "comprendre ce qu'est le dossier de la pharmacie ;",
        "comprendre le délai de préparation et ce qu'on aura à payer.",
    ])

    d.declencheur(
        'Mise en situation', "Il vous reste deux comprimés. Que faites-vous ?",
        image=IMG + 'sac-pharmacie.jpg',
        pistes=[
            "Faut-il attendre le rendez-vous chez le médecin ?",
            "Qui peut vous aider en attendant ?",
            "Qu'est-ce qu'il faut apporter à la pharmacie ?",
        ],
        notes="Recueillir les réponses avant de corriger. La croyance la plus répandue "
              "est qu'il faut absolument revoir le médecin : c'est ce que la séance vient "
              "défaire.")

    d.dialogue('Dialogue · 1 de 3', "Mon ordonnance est finie", [
        ("NADIA", "Bonjour. Il me reste deux comprimés pour la pression, et mon ordonnance est finie.", True),
        ("GAÉTANE", "Votre nom, s'il vous plaît ?", True),
        ("NADIA", "Nadia Belhadj. B, E, L, H, A, D, J.", True),
        ("GAÉTANE", "Merci. Votre carte d'assurance maladie ?", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Nadia épelle son nom sans qu'on le lui demande. Le faire remarquer : "
             "c'est le geste qui fait gagner le plus de temps au comptoir. Faire épeler "
             "son propre nom à chaque élève.")

    d.dialogue('Dialogue · 2 de 3', "Je regarde votre dossier", [
        ("GAÉTANE", "Je regarde votre dossier… Le médicament a été servi la dernière fois le 3 mai.", True),
        ("NADIA", "Mon rendez-vous chez le médecin est seulement dans six semaines.", True),
        ("GAÉTANE", "Ce n'est pas un problème. Le pharmacien peut prolonger votre ordonnance en attendant.", True),
        ("NADIA", "Vraiment ? Sans revoir le médecin ?", True),
    ], notes="C'est la découverte centrale du défi. La réplique de Nadia est celle que "
             "beaucoup d'élèves auraient : la laisser être posée par le groupe.")

    d.dialogue('Dialogue · 3 de 3', "Combien de temps, combien ça coûte", [
        ("GAÉTANE", "Oui, pour un certain temps. Jamais plus d'un an.", True),
        ("NADIA", "Est-ce que ça prend beaucoup de temps ?", True),
        ("GAÉTANE", "Une vingtaine de minutes. Vous pouvez attendre ou revenir plus tard.", True),
        ("NADIA", "Combien est-ce que je vais payer ?", True),
    ], notes="Les deux questions de Nadia sont celles que tout le monde a et que peu de "
             "gens osent poser. Les faire répéter telles quelles.")

    d.tableau('Analyse', "Ce que le pharmacien peut faire, et ce qu'il ne peut pas",
              ["Il peut", "Il ne peut pas"],
              [["prolonger une ordonnance qui finit", "la prolonger plus d'un an"],
               ["conseiller un médicament en vente libre", "poser un diagnostic"],
               ["voir vos médicaments dans son dossier", "deviner ceux d'ailleurs"],
               ["expliquer une posologie", "vous forcer à la suivre"]],
              cle=0,
              note="La prolongation d'ordonnance par le pharmacien existe au Québec depuis 2021.",
              notes="Diapositive à photographier. Les élèves qui viennent de pays où le "
                    "pharmacien ne fait que vendre sont souvent surpris par la colonne "
                    "de gauche.")

    d.regle("La phrase du renouvellement",
            "« Est-ce que je peux faire renouveler mon ordonnance ? »",
            precision="Elle contient tout : la demande, la politesse, et le mot "
                      "exact. On peut aussi dire « il me reste deux comprimés » "
                      "avant : le pharmacien comprend tout de suite l'urgence.",
            notes="Diapositive à photographier. Faire répéter la phrase entière par tout "
                  "le groupe, puis par cinq élèves seuls.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("L'ordonnance de Nadia est finie.", "vrai"),
        ("On lui demande son nom et sa carte d'assurance maladie.", "vrai"),
        ("La pharmacie garde un dossier de ses médicaments.", "vrai"),
        ("Elle doit absolument revoir le médecin avant.", "faux — le pharmacien peut prolonger"),
        ("Le pharmacien peut prolonger une ordonnance pour dix ans.", "faux — jamais plus d'un an"),
        ("La préparation prend une vingtaine de minutes.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte du dialogue.")

    d.billet(
        "Écrivez la première phrase que vous diriez au comptoir pour un renouvellement.",
        exemples=[
            "Dites ce qui vous reste, et ce que vous demandez.",
            "Ajoutez votre nom, épelé.",
        ],
        notes="Devoir court. Ces phrases servent d'ouverture au jeu de rôle de la "
              "séance E1.")

    return d.save(dossier)
