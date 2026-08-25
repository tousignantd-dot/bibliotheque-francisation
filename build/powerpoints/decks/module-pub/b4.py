# -*- coding: utf-8 -*-
"""B4 · Les préfixes.
Bloc B · couleur ambre (écriture) · 60 min.
Source : exercice `t1prefixe` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre='Les préfixes',
        chapeau="« Réutiliser », « débrancher », « irréparable ». Un petit élément devant "
                "le mot, et le sens change — parfois jusqu'à devenir son contraire.",
        duree='60 minutes')

    d.titre(notes="Écrire « utiliser » au tableau et demander au groupe d'en fabriquer "
                  "d'autres mots. « Réutiliser » viendra vite : c'est le point de "
                  "départ.")

    d.objectifs([
        "reconnaître un préfixe dans un mot ;",
        "connaître huit préfixes courants et leur sens ;",
        "fabriquer un mot nouveau avec un préfixe ;",
        "deviner le sens d'un mot inconnu grâce à son préfixe.",
    ])

    d.regle('La règle',
            "Un préfixe se place devant le mot et en change le sens.",
            precision="« Utiliser » devient « réutiliser » : utiliser à nouveau. Le mot "
                      "de base ne change pas — on ajoute seulement devant. C'est ce qui "
                      "rend les préfixes faciles à repérer.",
            notes="Écrire la règle au tableau. Insister sur « devant » : le suffixe, à la "
                  "séance suivante, se place derrière.")

    d.tableau('Analyse · 1 de 2', "Quatre préfixes",
              ['Le préfixe', 'Il veut dire', 'Un exemple'],
              [["re-, ré-", "à nouveau", "réutiliser, recoudre"],
               ["dé-, dés-", "le contraire de", "débrancher, désinstaller"],
               ["in-, im-, ir-", "le contraire de", "impossible, irréparable"],
               ["sur-", "trop", "surchauffer, surcharger"]],
              cle=0, props=[0.24, 0.28, 0.48],
              notes="Les deux préfixes du contraire — dé- et in- — ne s'emploient pas "
                    "avec les mêmes mots. C'est l'usage qui décide, pas une règle.")

    d.tableau('Analyse · 2 de 2', "Quatre préfixes de plus",
              ['Le préfixe', 'Il veut dire', 'Un exemple'],
              [["anti-", "contre", "antibruit, antirouille"],
               ["en-, em-", "dans", "emballer, encadrer"],
               ["inter-", "entre", "interurbain, international"],
               ["pré-", "avant", "préinscription, préavis"]],
              cle=0, props=[0.24, 0.28, 0.48],
              notes="« Pré- » et « inter- » sont fréquents dans les documents "
                    "administratifs. Le signaler : ils servent au-delà du module.")

    d.cartes('Ouvrir la mini-leçon', "Quatre choses à savoir en plus", [
        ("Le préfixe s'adapte au mot",
         "« In- » devient « im- » devant m, b, p (impossible), et « ir- » devant r "
         "(irréparable). C'est une question de prononciation."),
        ("Deviner un mot inconnu",
         "« Irrécupérable » : ir- veut dire le contraire, récupérer veut dire reprendre. "
         "Donc : qu'on ne peut pas reprendre. On devine sans dictionnaire."),
        ("Les préfixes de la publicité",
         "« Réutiliser », « réparer », « recycler », « redonner » : le préfixe re- "
         "porte à lui seul l'idée de l'atelier."),
        ("Attention aux faux préfixes",
         "Dans « repas », le « re- » n'est pas un préfixe : « pas » n'a aucun rapport. "
         "Vérifiez que le mot de base existe seul."),
    ], notes="La deuxième carte est la plus utile : le préfixe est un outil de lecture "
             "autant que d'écriture.")

    d.pratique('Pratique · 1 de 4', "Ajoutez le préfixe",
               "Un préfixe par mot.", [
        ("brancher (le contraire)", "débrancher"),
        ("utiliser (à nouveau)", "réutiliser"),
        ("possible (le contraire)", "impossible"),
        ("chauffer (trop)", "surchauffer"),
        ("inscription (avant)", "préinscription"),
        ("urbain (entre)", "interurbain"),
    ], corrige=True,
       notes="Faire nommer le sens du préfixe avant d'écrire. C'est le sens qui guide, "
             "pas la mémoire.")

    d.pratique('Pratique · 2 de 4', "Devinez le sens",
               "Servez-vous du préfixe.", [
        ("irréparable", "qu'on ne peut pas réparer"),
        ("désinstaller", "faire le contraire d'installer"),
        ("antirouille", "qui protège contre la rouille"),
        ("surcharger", "charger trop"),
        ("préavis", "un avis donné avant"),
        ("interurbain", "entre deux villes"),
    ], corrige=True,
       notes="Aucun de ces mots n'a besoin d'être connu : le préfixe et le mot de base "
             "suffisent. C'est la compétence de la séance.")

    d.piege("Le piège du mauvais préfixe du contraire",
            "inbrancher, irpossible",
            "débrancher, impossible",
            "Les deux préfixes du contraire — dé- et in- — ne se choisissent pas au "
            "hasard, mais il n'y a pas de règle : c'est l'usage. En cas de doute, "
            "essayez les deux à voix haute — celui qui sonne juste est presque toujours "
            "le bon.",
            notes="Le dire honnêtement : ici, il n'y a pas de règle à apprendre, "
                  "seulement des mots. C'est plus rassurant que de chercher une logique "
                  "qui n'existe pas.")

    d.piege("Le piège du faux préfixe",
            "Dans « repas », re- veut dire à nouveau.",
            "« Pas » n'a aucun rapport : ce n'est pas un préfixe.",
            "Pour qu'il y ait un préfixe, il faut que le mot de base existe seul et ait "
            "un rapport de sens. « Réutiliser » : utiliser existe, et le sens colle. "
            "« Repas » : pas existe, mais le sens n'a rien à voir.",
            notes="Faire tester trois mots : recevoir, remercier, retourner. Seul le "
                  "dernier a un vrai préfixe.")

    d.pratique('Pratique · 3 de 4', "Vrai préfixe ou non ?",
               "Le mot de base existe-t-il, et le sens colle-t-il ?", [
        ("réutiliser", "oui — utiliser à nouveau"),
        ("repas", "non — « pas » n'a aucun rapport"),
        ("retourner", "oui — tourner à nouveau"),
        ("remercier", "non — « mercier » n'existe pas"),
        ("débrancher", "oui — le contraire de brancher"),
    ], corrige=True,
       notes="Exercice difficile et instructif. Le faire en grand groupe plutôt "
             "qu'individuellement.")

    d.pratique('Pratique · 4 de 4', "Les mots de l'atelier",
               "Fabriquez le mot qui convient.", [
        ("Utiliser un objet une deuxième fois", "réutiliser"),
        ("Un objet qu'on ne peut pas réparer", "irréparable"),
        ("Coudre à nouveau un vêtement déchiré", "recoudre"),
        ("Enlever la prise d'un appareil", "débrancher"),
        ("Mettre un cadre autour", "encadrer"),
    ], corrige=True,
       notes="Ces cinq mots sont ceux de l'atelier de réparation. Ils serviront dans les "
             "capsules de E1.")

    d.billet(
        "Fabriquez cinq mots avec cinq préfixes différents.",
        exemples=[
            "Écrivez le mot de base, le préfixe, et le mot obtenu.",
            "Puis le sens du mot obtenu, en trois mots.",
        ],
        notes="Corriger le sens autant que la forme. Un mot bien formé mais mal compris "
              "ne sert à rien.")

    return d.save(dossier)
