# -*- coding: utf-8 -*-
"""A3 · Quarante dollars et cinquante cents.
Bloc A « Je découvre » · couleur teal · 60 min.
Source : exercices `prImg` et `prMont`, mini-leçon `prMont`.

Séance de lexique. Elle ferme le bloc A en donnant les six étapes du retrait
en images, puis la façon de dire un montant — les deux choses que le Défi 1
suppose acquises.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-guichet/images/')


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre="Quarante dollars et cinquante cents",
        chapeau="Nommer les six étapes d'un retrait, et dire un montant "
                "d'argent dans le bon ordre.",
        duree='60 minutes')

    d.titre(notes="Dernière séance du bloc A. À la fin, chaque élève doit pouvoir dire "
                  "les six étapes du retrait dans l'ordre, sans lire.")

    d.objectifs([
        "nommer les six étapes d'un retrait ;",
        "dire un montant en dollars ;",
        "dire un montant avec des cents ;",
        "écrire un montant à la façon d'ici : 45,50 $.",
    ])

    d.declencheur(
        'Observation', "Que fait cette main ?",
        image=IMG + 'etape-nip.jpg',
        pistes=[
            "Que fait la main du dessous ?",
            "Que fait la main du dessus ?",
            "Pourquoi cache-t-elle le clavier ?",
            "Est-ce qu'on fait la même chose au magasin ?",
        ],
        notes="La réponse « pour cacher les chiffres » vient vite. Enchaîner : oui, et "
              "on le fait aussi sur la petite machine du dépanneur.")

    d.cartes("Les six étapes d'un retrait", "Toujours dans cet ordre", [
        ("1 · la carte", "Je mets ma carte dans le guichet."),
        ("2 · le NIP", "Je tape mon NIP. Je cache le clavier."),
        ("3 · le choix", "J'appuie sur « retrait »."),
        ("4 · le montant", "Je choisis quarante dollars."),
        ("5 · l'argent", "Je prends ma carte, puis mon argent."),
        ("6 · le relevé", "Je prends mon relevé."),
    ], cols=3, notes="Diapositive à photographier. Faire redire les six étapes debout, "
                     "en mimant : la mémoire du geste tient mieux que celle du mot.")

    d.regle("Le nombre d'abord, le mot après",
            "quarante dollars, jamais dollars quarante.",
            precision="Les cents suivent la même règle : <b>vingt-cinq cents</b>. Et le "
                      "signe $ ne se dit pas — il s'écrit après le nombre, avec une "
                      "espace : 40 $.",
            notes="Diapositive à photographier. C'est l'inverse de ce que beaucoup ont "
                  "vu écrit en anglais ; le dire explicitement évite dix corrections.")

    d.tableau('Analyse', "Un montant complet",
              ['On écrit', 'On dit'],
              [["20 $", "vingt dollars"],
               ["0,25 $", "vingt-cinq cents"],
               ["45,50 $", "quarante-cinq dollars et cinquante cents"],
               ["« Ça fait quarante-cinq et cinquante. »", "ce qu'on entend à la caisse"]],
              cle=2,
              note="À la caisse, les mots « dollars » et « cents » tombent souvent. Le "
                   "prix, lui, ne change pas.",
              notes="Diapositive à photographier. La dernière ligne surprend toujours : "
                    "la faire entendre trois fois, à vitesse réelle.")

    d.pratique('Pratique', "Écrivez le montant en chiffres",
               "L'enseignante dit ; vous écrivez à la façon d'ici.", [
        ("Série 1", "vingt dollars · quarante dollars · soixante dollars"),
        ("Série 2", "vingt-cinq cents · dix cents · cinq cents"),
        ("Série 3", "quarante-cinq dollars et cinquante cents"),
    ], corrige=True, cols=1,
       notes="Quinze minutes. Corriger surtout la virgule : beaucoup écrivent 45.50, ce "
             "qui est la façon anglaise.")

    d.pratique('Pratique · à deux', "Combien ça coûte ?",
               "Deux par deux. L'un dit un prix, l'autre l'écrit, puis on échange.", [
        ("Étape 1", "Ça fait quarante-cinq dollars."),
        ("Étape 2", "Quarante-cinq ? Quatre-cinq ?"),
        ("Étape 3", "Oui. Et cinquante cents."),
        ("Étape 4", "45,50 $. Merci."),
    ], cols=1,
       notes="Vingt minutes. Réutiliser la vérification chiffre par chiffre vue en A2 : "
             "c'est la même compétence, appliquée à de l'argent.")

    d.billet(
        "Notez trois prix que vous avez payés cette semaine, en chiffres et en mots.",
        exemples=[
            "12,75 $ — douze dollars et soixante-quinze cents",
            "40,00 $ — quarante dollars",
            "3,50 $ — trois dollars et cinquante cents",
        ],
        notes="Devoir court. Les prix réels marquent mieux que les prix inventés, et "
              "ouvrent la séance suivante sur une matière que le groupe apporte.")

    return d.save(dossier)
