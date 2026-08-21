# -*- coding: utf-8 -*-
"""A1 · Deux comptoirs, une pharmacie.
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-pharmacie/images/')


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre='Deux comptoirs, une pharmacie',
        chapeau="Devant, la caisse. Au fond, le comptoir des ordonnances. "
                "C'est au fond qu'on parle au pharmacien — sans rendez-vous, "
                "et sans payer pour le conseil.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Demander au groupe qui a déjà parlé à un "
                  "pharmacien en français, et ce qui a été difficile. Beaucoup d'élèves "
                  "ignorent qu'on peut demander un conseil sans ordonnance et sans "
                  "payer : c'est la découverte principale de la séance.")

    d.objectifs([
        "reconnaître les deux comptoirs d'une pharmacie ;",
        "savoir qu'un conseil du pharmacien est gratuit et sans rendez-vous ;",
        "savoir ce qu'il faut apporter : la carte d'assurance maladie ;",
        "distinguer un médicament en vente libre d'un médicament sur ordonnance.",
    ])

    d.declencheur(
        'Observation', "Où faut-il aller pour parler au pharmacien ?",
        image=IMG + 'comptoir-fond.jpg',
        pistes=[
            "Qu'est-ce qu'on voit derrière ce comptoir ?",
            "Est-ce que c'est là qu'on paie son shampooing ?",
            "Est-ce qu'il faut un rendez-vous pour parler à cette personne ?",
            "Qu'est-ce qu'on apporte avec soi ?",
        ],
        notes="Laisser venir les mots dans n'importe quelle langue, puis les traduire "
              "ensemble au tableau. Dans plusieurs pays, le pharmacien vend et ne "
              "conseille pas ; au Québec, le conseil fait partie de son travail et il "
              "est gratuit. C'est là que se joue toute la différence du module.")

    d.dialogue('Dialogue · 1 de 3', "Je tousse depuis quatre jours", [
        ("NADIA", "Moussa, je tousse depuis quatre jours. Je dors mal.", True),
        ("MOUSSA", "Tu as un médecin de famille ?", True),
        ("NADIA", "Non, pas encore. Je suis sur la liste d'attente.", True),
        ("MOUSSA", "Alors viens à la pharmacie. On peut parler au pharmacien sans rendez-vous.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="La situation de Nadia est celle de beaucoup d'élèves : pas encore de "
             "médecin de famille, une liste d'attente. Le faire dire par le groupe "
             "plutôt que par l'enseignante.")

    d.dialogue('Dialogue · 2 de 3', "Devant, au fond", [
        ("NADIA", "Il y a deux comptoirs. Je vais où ?", True),
        ("MOUSSA", "Devant, c'est la caisse. Au fond, à droite, c'est le comptoir des ordonnances.", True),
        ("NADIA", "Et il faut une ordonnance pour parler au pharmacien ?", True),
        ("MOUSSA", "Non. Tu peux juste demander un conseil. C'est gratuit.", True),
    ], notes="C'est la découverte centrale de la séance. Faire répéter « le comptoir des "
             "ordonnances » : quatre mots, un seul souffle.")

    d.dialogue('Dialogue · 3 de 3', "Dans l'allée deux", [
        ("NADIA", "Le sirop pour la toux, il est où ?", True),
        ("MOUSSA", "Dans l'allée deux, en vente libre. Tu le prends toi-même.", True),
        ("NADIA", "Alors pourquoi aller au comptoir ?", True),
        ("MOUSSA", "Parce que le pharmacien va te dire lequel prendre. Il y en a dix sur la tablette.", True),
    ], notes="Répondre à la vraie question de l'élève : si le sirop est en libre-service, "
             "pourquoi déranger le pharmacien ? Parce que dix bouteilles se ressemblent "
             "et qu'une seule convient à ce qu'on prend déjà.")

    d.tableau('Analyse', "Les deux comptoirs, et ce qu'on y fait",
              ["L'endroit", "Ce qu'on y fait"],
              [["La caisse, en avant", "on paie ce qu'on a pris dans les allées"],
               ["Les allées", "les médicaments en vente libre"],
               ["Le comptoir du fond", "on parle au pharmacien"],
               ["La salle d'attente", "on attend son nom"]],
              cle=1,
              note="Le conseil du pharmacien est gratuit et sans rendez-vous.",
              notes="Diapositive à photographier. Faire nommer chaque ligne par un élève "
                    "différent. C'est le plan du module entier.")

    d.regle("Ce qu'il faut apporter",
            "« ma carte d'assurance maladie »",
            precision="On la demande chaque fois, même pour un renouvellement. "
                      "Elle sert à vérifier qui vous êtes et à savoir ce que "
                      "l'assurance paie. Le flacon vide de l'ancien médicament "
                      "aide aussi : il porte le nom exact et le numéro.",
            notes="Diapositive à photographier. Demander qui a sa carte sur soi "
                  "aujourd'hui. Rappeler qu'elle a une date d'expiration et qu'elle se "
                  "renouvelle avant, pas après.")

    d.cartes("Les mots de l'endroit", "Quatre mots", [
        ("le comptoir des ordonnances",
         "Le comptoir du fond, souvent plus haut que les autres. C'est là qu'on dépose "
         "son ordonnance, qu'on pose ses questions et qu'on récupère son sac."),
        ("une ordonnance",
         "Le papier signé par un médecin ou une autre professionnelle autorisée. Sans "
         "lui, la pharmacie n'a pas le droit de donner certains médicaments."),
        ("un médicament en vente libre",
         "Il s'achète sans papier du médecin : sirop, pastilles, pansements. Certains "
         "restent quand même derrière le comptoir, et le pharmacien décide de les "
         "donner ou non."),
        ("la carte d'assurance maladie",
         "La carte du gouvernement du Québec. On la présente chaque fois, à la "
         "pharmacie comme à la clinique."),
    ], notes="Faire dire chaque mot avec son article. Les quatre reviennent dans toutes "
             "les séances du module.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Nadia a déjà un médecin de famille.", "faux — elle est sur la liste d'attente"),
        ("On peut parler au pharmacien sans rendez-vous.", "vrai"),
        ("Le comptoir des ordonnances est au fond, à droite.", "vrai"),
        ("Il faut une ordonnance pour demander un conseil.", "faux — le conseil est gratuit"),
        ("Il faut apporter sa carte d'assurance maladie.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte du dialogue.")

    d.billet(
        "Écrivez où est votre pharmacie et ce que vous y avez déjà acheté.",
        exemples=[
            "Est-ce que vous y êtes déjà allé pour un conseil ?",
            "Avez-vous votre carte d'assurance maladie ?",
        ],
        notes="Devoir court. Il prépare la séance A3 sur le vocabulaire et donne des "
              "exemples personnels pour le défi 1.")

    return d.save(dossier)
