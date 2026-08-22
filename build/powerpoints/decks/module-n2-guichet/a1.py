# -*- coding: utf-8 -*-
"""A1 · C'est ma première fois.
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercices `prVocab` et `pr1`.

Neuvième module court du projet. L'élève de niveau 2 tient une phrase à la
fois : les diapositives portent peu de mots, et chaque phrase projetée est une
phrase qu'il pourra dire lui-même en sortant.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-guichet/images/')


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="C'est ma première fois",
        chapeau="Nommer l'argent et les objets du guichet, et dire ce qu'on "
                "veut faire avant d'appuyer sur quoi que ce soit.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Commencer par une question au groupe, dans "
                  "la langue qu'on peut : « Qui a déjà utilisé un guichet automatique "
                  "ici ? » Beaucoup lèveront la main ; certains diront qu'ils demandent "
                  "toujours à quelqu'un de le faire. C'est exactement le sujet.")

    d.objectifs([
        "nommer l'argent : un billet, une pièce, un montant ;",
        "nommer les objets du guichet : la carte, le NIP, le relevé ;",
        "dire ce qu'on veut faire au guichet ;",
        "savoir qu'on ne dit jamais son NIP à voix haute.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qu'on fait sur cette photo ?",
        image=IMG + 'etape-carte.jpg',
        pistes=[
            "Que voit-on sur cette photo ?",
            "Qu'est-ce que la main tient ?",
            "Où est-ce qu'elle la met ?",
            "Qu'est-ce qui arrive après ?",
        ],
        notes="Laisser répondre dans la langue qu'on peut. Amener les mots « la carte » et "
              "« le guichet » sans les forcer : ils reviendront tout le module.")

    d.dialogue('Dialogue · 1 de 2', "Bonjour, c'est ma première fois", [
        ("AMADOU", "Bonjour, monsieur. C'est ma première fois.", True),
        ("CLAUDE", "Bonjour ! Vous voulez retirer de l'argent ?", True),
        ("AMADOU", "Oui. Quarante dollars.", True),
        ("CLAUDE", "Vous avez votre carte ?", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Faire écouter deux fois, diapositive masquée. Puis afficher et faire répéter "
             "réplique par réplique, en chœur. Insister sur « C'est ma première fois » : "
             "c'est la phrase qui autorise à être lent.")

    d.dialogue('Dialogue · 2 de 2', "Ne dites jamais votre NIP", [
        ("AMADOU", "Oui, elle est là. Et j'ai mon NIP.", True),
        ("CLAUDE", "Parfait. Ne dites jamais votre NIP à voix haute.", True),
        ("AMADOU", "Ah ! D'accord. Merci.", True),
        ("CLAUDE", "Le guichet est libre. Je reste ici.", True),
    ], notes="La consigne de sécurité vient d'un personnage, pas de l'enseignante : c'est "
             "voulu. Demander ensuite au groupe : « Est-ce que quelqu'un peut demander "
             "votre NIP ? » La réponse est non, jamais, même un employé.")

    d.vocabulaire('Vocabulaire', "Les six mots de l'argent", [
        ("l'argent", "Ce qu'on donne pour payer : des billets et des pièces."),
        ("un billet", "Le papier de vingt dollars ou de cinquante dollars."),
        ("une pièce", "Le petit rond de métal qui vaut vingt-cinq cents."),
        ("une carte de débit", "La carte qui ouvre le guichet et qui paie dans les magasins."),
        ("un compte", "L'endroit où la caisse garde ton argent."),
        ("un guichet automatique", "La machine qui donne de l'argent, jour et nuit."),
    ], notes="Diapositive à photographier. Faire dire chaque mot avec son article : au "
             "niveau 2, le nom sans article ne s'installe pas.")

    d.tableau('Analyse', "Ce qu'on dit en arrivant",
              ['Ce qu\'on dit', 'À quoi ça sert'],
              [["Bonjour, monsieur.", "on ouvre poliment"],
               ["C'est ma première fois.", "on demande d'être patient"],
               ["Je veux retirer quarante dollars.", "on dit ce qu'on veut faire"],
               ["J'ai ma carte.", "on montre qu'on est prêt"]],
              cle=2,
              note="Quatre phrases, et personne n'a encore touché la machine. C'est le bon "
                   "ordre.",
              notes="Diapositive à photographier. Faire dire les quatre phrases par chaque "
                    "élève, une fois, sans correction.")

    d.regle("On ne dit jamais son NIP",
            "Quatre chiffres, et personne d'autre que vous.",
            precision="Aucun employé de caisse ou de banque ne demande un NIP — ni au "
                      "comptoir, ni au téléphone, ni par courriel. Au clavier, on cache "
                      "le clavier avec l'autre main.",
            notes="Diapositive à photographier. Le dire deux fois plutôt qu'une : c'est la "
                  "seule chose du module qui protège de l'argent perdu.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("C'est la première fois qu'Amadou vient au guichet.", "vrai"),
        ("Il veut retirer quarante dollars.", "vrai"),
        ("Il a oublié sa carte à la maison.", "faux — elle est là"),
        ("Il faut attendre : le guichet est occupé.", "faux — il est libre"),
    ], corrige=True, cols=1,
       notes="Quatre énoncés seulement. Les faire d'abord à l'oral, en groupe, avant de "
             "les faire écrire.")

    d.pratique('Pratique · à deux', "Vous arrivez au guichet",
               "Deux par deux, trois fois, en changeant de partenaire.", [
        ("Étape 1", "Bonjour, monsieur. / Bonjour, madame."),
        ("Étape 2", "C'est ma première fois."),
        ("Étape 3", "Je veux retirer… (un montant)"),
        ("Étape 4", "Merci beaucoup."),
    ], cols=1,
       notes="Vingt minutes. Circuler, écouter, ne corriger que ce qui empêche de "
             "comprendre. Le montant exact n'a aucune importance ici.")

    d.billet(
        "Écrivez trois choses que vous avez dans votre portefeuille.",
        exemples=[
            "J'ai une carte de débit.",
            "J'ai deux billets de vingt dollars.",
            "J'ai des pièces.",
        ],
        notes="Devoir court. Demander d'écrire ce qu'ils ont vraiment : c'est ce qui fait "
              "retenir les mots.")

    return d.save(dossier)
