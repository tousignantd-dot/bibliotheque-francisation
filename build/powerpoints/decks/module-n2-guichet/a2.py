# -*- coding: utf-8 -*-
"""A2 · Treize ou trente ?
Bloc A « Je découvre » · couleur indigo · 60 min.
Source : exercice `prSon`, mini-leçon `prSon`.

Séance d'écoute. Un nombre mal entendu au guichet, c'est de l'argent en moins
ou en trop : c'est le seul point de phonétique du module, et il se travaille
tôt, avant que les montants n'arrivent partout.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Treize ou trente ?",
        chapeau="Entendre la différence entre les petits nombres et les "
                "grands, et savoir lever le doute quand elle échappe.",
        duree='60 minutes')

    d.titre(notes="Séance courte et très orale. Prévoir de faire écouter beaucoup plus "
                  "que de faire écrire. Annoncer d'entrée que la confusion 14 / 40 est "
                  "normale, et qu'elle se règle par une question, pas par de l'oreille.")

    d.objectifs([
        "entendre la fin des nombres de 13 à 16 ;",
        "entendre la fin des nombres de 30 à 60 ;",
        "dire un nombre chiffre par chiffre pour lever un doute ;",
        "demander de répéter sans gêne.",
    ])

    d.tableau('Analyse', "Deux familles, deux fins",
              ['La famille', 'Les quatre nombres'],
              [["Les petits, fin en ze", "treize · quatorze · quinze · seize"],
               ["Les grands, fin en ante", "trente · quarante · cinquante · soixante"],
               ["Ce qui décide", "la fin du mot, jamais le début"]],
              cle=2,
              note="Mettez la main sous le nez en disant « quarante » : ça vibre. En "
                   "disant « quatorze », non.",
              notes="Diapositive à photographier. Faire l'essai de la main sous le nez "
                    "avec tout le groupe : c'est ce qui reste en mémoire.")

    d.regle("Écoutez la fin du mot",
            "Le début se ressemble ; la fin décide.",
            precision="quator<b>ze</b> et quar<b>ante</b> · quin<b>ze</b> et "
                      "cinqu<b>ante</b> · sei<b>ze</b> et soix<b>ante</b>. Un mot dont "
                      "la fin est avalée ne se comprend pas.",
            notes="Diapositive à photographier. Faire prononcer les trois paires en "
                  "tenant la dernière syllabe plus longtemps que d'habitude.")

    d.cartes("Trois paires qui se confondent", "À dire l'une après l'autre", [
        ("14 et 40", "quatorze · quarante"),
        ("15 et 50", "quinze · cinquante"),
        ("16 et 60", "seize · soixante"),
    ], cols=3, notes="Diapositive à photographier. Les faire dire en chœur, puis un élève "
                     "à la fois, en variant l'ordre pour que le groupe devine.")

    d.pratique('Écoute', "Quel nombre entendez-vous ?",
               "L'enseignante dit un nombre ; écrivez-le en chiffres.", [
        ("Série 1", "13 · 30 · 14 · 40 · 15 · 50"),
        ("Série 2", "16 · 60 · 40 · 14 · 60 · 16"),
        ("Série 3", "à deux : l'un dit, l'autre écrit, puis on échange"),
    ], cols=1,
       notes="Quinze minutes. Dire les nombres sans les montrer, à vitesse normale — pas "
             "plus lentement : c'est la vitesse normale qui pose problème dehors.")

    d.regle("Pour lever le doute",
            "On donne les chiffres un par un.",
            precision="« Quarante ? <b>Quatre-zéro</b> ? » · « Quatorze ? "
                      "<b>Un-quatre</b> ? » Personne ne trouve ça bizarre : les gens "
                      "d'ici le font aussi au téléphone.",
            notes="Diapositive à photographier. Insister : ce n'est pas un aveu "
                  "d'ignorance, c'est une habitude d'adulte prudent.")

    d.pratique('Pratique · à deux', "Un montant, une vérification",
               "Deux par deux. L'un donne un montant, l'autre le vérifie.", [
        ("Étape 1", "Je retire quarante dollars."),
        ("Étape 2", "Quarante ? Quatre-zéro ?"),
        ("Étape 3", "Oui, quatre-zéro."),
        ("Étape 4", "On recommence avec un autre montant."),
    ], cols=1,
       notes="Vingt minutes. Faire varier les montants : 15, 50, 16, 60. Circuler et "
             "noter qui n'ose pas encore poser la question de vérification.")

    d.piege('Le piège', "quaran…",
            "quarante",
            "Avaler la fin du mot rend « quarante » et « quatorze » identiques. "
            "La différence est <b>seulement</b> dans les dernières lettres : il faut "
            "les prononcer en entier, même si ça paraît exagéré.",
            notes="Exagérer soi-même la fin en le disant : le groupe imite ce qu'il "
                  "entend, pas ce qu'on lui explique.")

    d.billet(
        "Écrivez cinq nombres en lettres, puis dites-les à voix haute.",
        exemples=[
            "13 : treize",
            "40 : quarante",
            "60 : soixante",
        ],
        notes="Devoir court. Demander de dire les cinq nombres tout haut chez eux, une "
              "fois : la lecture silencieuse ne règle rien ici.")

    return d.save(dossier)
