# -*- coding: utf-8 -*-
"""D1 · Quatre pages sur quarante.
Bloc D « Défi 3 · Le mode d'emploi » · couleur acier · 75 min.
Source : mini-leçon `t3mode`, dialogue `t3`, exercices `t3vf`, `t3mode` et `t3pages`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-achat/images/')


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre='Quatre pages sur quarante',
        chapeau="Quarante pages en trois langues. En réalité, quatre pages "
                "comptent : l'installation, la première utilisation, les "
                "avertissements, et le tableau des problèmes.",
        duree='75 minutes')

    d.titre(notes="Apporter un vrai mode d'emploi d'électroménager si possible. La séance "
                  "prend tout son sens sur un document réel.")

    d.objectifs([
        "trouver la section française d'un livret trilingue ;",
        "repérer les quatre parties utiles ;",
        "savoir ce qu'il faut faire avant le premier usage ;",
        "reconnaître un avertissement.",
    ])

    d.declencheur(
        'Observation', "Par où commencer dans un livret comme celui-ci ?",
        image=IMG + 'mode-emploi-appareil.jpg',
        pistes=[
            "Pourquoi est-il si épais ?",
            "Où se trouve la partie en français ?",
            "Que faut-il lire avant de brancher l'appareil ?",
            "Qu'est-ce que vous lisez, vous, dans un mode d'emploi ?",
        ],
        notes="La dernière piste est honnête : presque personne ne lit. C'est justement "
              "pour cela qu'il faut savoir quelles quatre pages ouvrir.")

    d.dialogue('Dialogue · 1 de 2', "Le tiers du livret", [
        ("THÉRÈSE", "Tu as reçu ta laveuse ? Tu as lu le mode d'emploi ?", False),
        ("YIN", "Je l'ai ouvert. Il fait quarante pages, en trois langues.", True),
        ("THÉRÈSE", "Il n'y a que quatre pages à lire, en réalité. Le reste, ce sont les mêmes pages en anglais et en espagnol.", True),
        ("YIN", "Lesquelles ?", False),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Le soulagement du groupe est audible à ce moment-là. Le livret cesse d'être "
             "intimidant.")

    d.dialogue('Dialogue · 2 de 2', "Les quatre pages", [
        ("THÉRÈSE", "L'installation, la première utilisation, les avertissements, et le tableau des problèmes.", True),
        ("YIN", "Et la première utilisation ?", False),
        ("THÉRÈSE", "On fait un cycle à vide, sans linge, avant tout. Ça enlève ce qui reste de l'usine.", True),
        ("THÉRÈSE", "C'est écrit à la page trois. Personne ne la lit.", True),
    ], notes="« Personne ne la lit » : la phrase qui fait sourire et qui installe la "
             "leçon. La reprendre.")

    d.tableau('Analyse', "Les quatre parties",
              ['Partie', 'Ce qu\'on y trouve'],
              [["1 · L'installation", "boulons de transport, mise de niveau, raccordement"],
               ["2 · La première utilisation", "un cycle à vide, sans linge"],
               ["3 · Les avertissements", "ce qui peut blesser ou briser l'appareil"],
               ["4 · Le tableau des problèmes", "le problème, et quoi vérifier"]],
              cle=3,
              note="La quatrième est la plus rentable et la moins lue.",
              notes="Diapo à photographier. Faire chercher les quatre parties dans le "
                    "livret apporté.")

    d.regle("Les boulons de transport",
            "Quatre boulons à l'arrière, à enlever avant le premier lavage.",
            precision="Ils bloquent le tambour pendant le transport. Oubliés, ils font "
                      "sauter la machine au premier essorage — et le dommage n'est pas "
                      "couvert par la garantie : c'est une mauvaise utilisation.",
            notes="Diapo à photographier. C'est le dommage le plus fréquent d'une première "
                  "installation.")

    d.regle("Le cycle à vide",
            "Un lavage sans linge, avant la première brassée.",
            precision="Il enlève les résidus d'usine — poussière de métal, huile de "
                      "montage. Deux lignes à la page trois, que personne ne lit, et qui "
                      "évitent que la première brassée sorte tachée.",
            notes="Faire lever la main à ceux qui l'ont fait sur leur propre appareil. "
                  "Presque personne.")

    d.piege("Jeter le livret avec l'emballage",
            "Les livreurs ont tout emporté.",
            "Je sors le livret de la boîte avant qu'ils repartent.",
            "Le livret contient le tableau des problèmes, qui règle neuf appels de service "
            "sur dix. Un déplacement de technicien coûte environ quatre-vingt-dix dollars. "
            "Ce petit livre vaut donc plusieurs centaines de dollars sur la vie de "
            "l'appareil.",
            notes="Le calcul rend la consigne concrète. C'est la meilleure façon de la "
                  "faire retenir.")

    d.pratique('Pratique', "Dans quelle partie ?",
               "Dites où se trouve chaque phrase.", [
        ("« Retirer les quatre boulons de transport. »", "l'installation"),
        ("« Ajuster les pieds pour que l'appareil soit de niveau. »", "l'installation"),
        ("« Effectuer un cycle à vide avant la première utilisation. »", "la première utilisation"),
        ("« Ne pas laver de vêtements imbibés de solvant. »", "les avertissements"),
        ("« L'appareil vibre : vérifier trois choses. »", "le tableau des problèmes"),
        ("« L'eau ne se vide pas : vérifier le tuyau. »", "le tableau des problèmes"),
    ], corrige=True,
       notes="Faire chercher dans le livret apporté avant de corriger.")

    d.billet(
        "Trouvez le mode d'emploi d'un appareil de chez vous et repérez les quatre parties.",
        exemples=[
            "Notez la page de chacune.",
            "Lisez la première utilisation : l'aviez-vous faite ?",
        ],
        notes="Devoir concret. Beaucoup découvrent des consignes qu'ils n'avaient jamais "
              "suivies.")

    return d.save(dossier)
