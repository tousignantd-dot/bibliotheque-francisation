# -*- coding: utf-8 -*-
"""B1 · L'écran parle, on répond.
Bloc B « Défi 1 · Au guichet automatique » · couleur acier · 75 min.
Source : dialogue `t1`, exercices `t1vf` et `t1ecran`, mini-leçon `t1imp`.

Séance centrale du premier défi. C'est ici qu'on lit vraiment un écran de
guichet : six phrases, toujours les mêmes, toujours dans le même ordre.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-guichet/images/')


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="L'écran parle, on répond",
        chapeau="Lire les six phrases d'un guichet automatique, comprendre "
                "l'ordre qu'elles donnent, et faire un retrait complet.",
        duree='75 minutes')

    d.titre(notes="Première séance du Défi 1. Annoncer le contrat : à la fin de la "
                  "séance, chacun sait ce que l'écran demande, dans l'ordre, et n'a "
                  "plus besoin de deviner.")

    d.objectifs([
        "lire les six phrases de l'écran ;",
        "reconnaître un ordre : un verbe sans sujet ;",
        "répondre à chaque ordre avec « je » ;",
        "faire un retrait du début à la fin.",
    ])

    d.declencheur(
        'Observation', "Sur quoi appuie ce doigt ?",
        image=IMG + 'etape-choix.jpg',
        pistes=[
            "Où sont les boutons sur un guichet ?",
            "Est-ce qu'on touche l'écran, ou un bouton à côté ?",
            "Qu'est-ce qu'on fait si on se trompe de bouton ?",
            "Que veut dire « annuler » ?",
        ],
        notes="Beaucoup de guichets d'ici ont des boutons de chaque côté de l'écran, pas "
              "un écran tactile. Le dire : ça évite une hésitation réelle.")

    d.dialogue('Dialogue · 1 de 2', "Entrez votre NIP", [
        ("ÉCRAN", "Bonjour. Entrez votre NIP.", True),
        ("AMADOU", "Quatre chiffres… non, je ne dis rien.", True),
        ("ÉCRAN", "Choisissez une opération : retrait, dépôt, solde.", True),
        ("AMADOU", "Retrait. J'appuie sur retrait.", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="L'écran a une voix, dans le module en ligne : la faire entendre avant de "
             "montrer le texte. Les élèves reconnaissent la situation aussitôt.")

    d.dialogue('Dialogue · 2 de 2', "Prenez votre argent", [
        ("ÉCRAN", "Choisissez un montant : vingt, quarante, soixante dollars.", True),
        ("AMADOU", "Quarante dollars.", True),
        ("ÉCRAN", "Prenez votre carte. Prenez votre argent.", True),
        ("AMADOU", "Ma carte. Mon argent. Deux billets de vingt.", True),
        ("ÉCRAN", "Voulez-vous un relevé ?", True),
        ("AMADOU", "Oui. Je prends le relevé.", True),
    ], notes="Faire remarquer l'ordre : la carte sort AVANT l'argent. C'est ce qui fait "
             "qu'on l'oublie, parce qu'on regarde déjà les billets.")

    d.tableau('Analyse', "Les six phrases de l'écran",
              ['L\'écran écrit', 'Ce qu\'il veut'],
              [["Entrez votre NIP.", "vos quatre chiffres"],
               ["Choisissez une opération.", "retrait, dépôt ou solde"],
               ["Choisissez un montant.", "20, 40, 60 ou 100 dollars"],
               ["Prenez votre carte.", "la carte d'abord"],
               ["Prenez votre argent.", "les billets ensuite"],
               ["Voulez-vous un relevé ?", "oui ou non"]],
              cle=2, props=[0.5, 0.5],
              notes="Diapositive à photographier. C'est la page la plus utile du module : "
                    "faire recopier à la main dans le cahier. Six phrases suffisent pour "
                    "tout un retrait, et elles ne changent pas d'un guichet à l'autre.")

    d.regle("Un ordre, c'est un verbe sans sujet",
            "Entrez. Choisissez. Appuyez. Prenez.",
            precision="Il n'y a ni « tu » ni « vous » devant le verbe. C'est la même "
                      "forme que sur les affiches et dans les recettes : "
                      "<b>Poussez</b>, <b>Tirez</b>, <b>Mélangez</b>.",
            notes="Diapositive à photographier. Chercher avec le groupe deux ordres vus "
                  "dans l'école même : « Poussez » sur une porte, par exemple.")

    d.cartes("L'écran dit, vous répondez", "La même chose, avec « je »", [
        ("Entrez votre NIP.", "J'entre mon NIP."),
        ("Choisissez une opération.", "Je choisis le retrait."),
        ("Prenez votre argent.", "Je prends mon argent."),
    ], cols=3, notes="Diapositive à photographier. Faire remarquer les deux changements : "
                     "le verbe, et « votre » qui devient « mon ».")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Le guichet demande le NIP en premier.", "vrai"),
        ("Amadou dit son NIP à voix haute.", "faux — il ne dit rien"),
        ("Il choisit « retrait ».", "vrai"),
        ("Il retire soixante dollars.", "faux — quarante"),
        ("Il prend un relevé avant de partir.", "vrai"),
    ], corrige=True, cols=1,
       notes="Cinq énoncés. Les faire à l'oral en groupe, puis à l'écrit seul.")

    d.pratique('Pratique · à deux', "Faites le retrait",
               "Deux par deux. L'un joue l'écran, l'autre répond. Puis on échange.", [
        ("L'écran", "Entrez votre NIP."),
        ("Vous", "J'entre mon NIP."),
        ("L'écran", "Choisissez un montant."),
        ("Vous", "Je choisis quarante dollars."),
        ("L'écran", "Prenez votre carte, prenez votre argent."),
        ("Vous", "Je prends ma carte et mon argent."),
    ], cols=1,
       notes="Vingt minutes. Faire jouer debout, en mimant la machine. Exiger que la "
             "carte soit « reprise » avant l'argent : le geste ancre l'ordre.")

    d.billet(
        "Écrivez les six étapes de votre retrait, avec « je ».",
        exemples=[
            "Je mets ma carte.",
            "Je tape mon NIP.",
            "Je choisis le retrait.",
        ],
        notes="Devoir court. C'est aussi le brouillon de la production orale de la "
              "séance E1 : le dire à la classe.")

    return d.save(dossier)
