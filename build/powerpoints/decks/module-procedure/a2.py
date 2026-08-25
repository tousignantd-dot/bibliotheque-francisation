# -*- coding: utf-8 -*-
"""A2 · Trois sons du bureau : « ui », « j » et « gn ».
Bloc A · couleur indigo (graphie-phonie) · 60 min.
Source : exercice `prPhon` et sa mini-leçon.

Le module affiche ces sons en alphabet phonétique. Pas ici : Verdana ne
possède aucun caractère de l'API. On nomme donc chaque son par ses lettres et
par un mot repère — nuit, jour, ligne.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre='Trois sons du bureau',
        chapeau="« Aujourd'hui, je joins ma signature en ligne. » Trois sons difficiles "
                "dans une seule phrase de travail — et trois orthographes qui ne se "
                "devinent pas.",
        duree='60 minutes')

    d.titre(notes="Écrire la phrase du chapeau au tableau et la faire lire par trois "
                  "élèves. Les trois sons difficiles apparaîtront tout de suite.")

    d.objectifs([
        "prononcer le son de « nuit » : deux voyelles collées ;",
        "prononcer le son de « jour », écrit j ou g ;",
        "prononcer le son de « ligne », écrit gn ;",
        "écrire correctement les mots du module qui les contiennent.",
    ])

    d.tableau('Analyse', "Trois sons, leurs lettres, un mot repère",
              ['Le son', "Il s'écrit", 'Mot repère'],
              [["le son de « nuit »", "ui", "nuit, aujourd'hui"],
               ["le son de « jour »", "j · g devant e, i, y", "jour, joindre, orangé"],
               ["le son de « ligne »", "gn", "ligne, signature, gagner"]],
              cle=0,
              note="Le deuxième est le seul qui s'écrit de deux façons. C'est celui qui "
                   "cause le plus d'erreurs d'orthographe.",
              notes="Écrire les trois mots repères au tableau et les y laisser toute la "
                    "séance.")

    d.regle('Le son de « nuit »',
            "On dit « u » puis « i » très vite, sans arrêt entre les deux.",
            precision="Nuit, aujourd'hui, juillet, huit, depuis. Ce n'est pas « nou-i » "
                      "ni « nu-i » en deux temps : les deux voyelles se collent et "
                      "forment un seul son glissé.",
            notes="Faire dire « nu… i » lentement, puis de plus en plus vite, jusqu'à ce "
                  "que les deux se collent. C'est l'exercice qui marche.")

    d.regle('Le son de « jour »',
            "Il s'écrit j partout, et g seulement devant e, i ou y.",
            precision="Jour, joindre, juillet : la lettre j. Orangé, gestion, agir : la "
                      "lettre g, mais seulement devant e, i ou y. Devant a, o ou u, la "
                      "lettre g fait un autre son : gare, gomme, légume.",
            notes="Écrire au tableau : g + e, i, y = le son de « jour ». g + a, o, u = le "
                  "son de « gare ». C'est la règle la plus rentable de la séance.")

    d.cartes('Ouvrir la mini-leçon', "Quatre choses à savoir en plus", [
        ("Le « e » qui sert de pont",
         "Dans « orangé », le g garde son son parce qu'il est devant e. Dans "
         "« mangeons », on ajoute un e exprès pour garder le son devant o."),
        ("Le son de « ligne » est un seul son",
         "Les lettres g et n s'unissent : ligne, signature, gagner, montagne. Ce n'est "
         "ni « lig-ne » ni « li-ne »."),
        ("Ne pas confondre gn et g + n",
         "Dans « diagnostic », le g et le n se prononcent séparément. C'est rare, mais "
         "cela existe."),
        ("Les mots du travail",
         "Signature, signaler, ligne, gagner, joindre, jour ouvrable, aujourd'hui, "
         "juillet. Tous sont dans ce module."),
    ], notes="La quatrième carte relie la phonétique au vocabulaire du module. Faire "
             "prononcer les huit mots à voix haute, en chœur.")

    d.pratique('Pratique · 1 de 3', "Quel son entendez-vous ?",
               "Écoutez le mot, écrivez « nuit », « jour » ou « ligne ».", [
        ("aujourd'hui", "le son de « nuit » — ui"),
        ("nuit", "le son de « nuit » — ui"),
        ("juillet", "le son de « jour » — j"),
        ("orangé", "le son de « jour » — g devant e"),
        ("joindre", "le son de « jour » — j"),
        ("gagner", "le son de « ligne » — gn"),
        ("ligne", "le son de « ligne » — gn"),
        ("signature", "le son de « ligne » — gn"),
    ], corrige=True, cols=2,
       notes="« Aujourd'hui » et « juillet » contiennent deux des trois sons chacun. Le "
             "signaler à la correction : c'est ce qui rend ces mots difficiles.")

    d.piege("Le piège de « g » devant a, o, u",
            "orangé lu comme « oran-gué »",
            "orangé — g devant e fait le son de « jour »",
            "La lettre g change de son selon ce qui suit. Devant e, i ou y, elle fait le "
            "son de « jour ». Devant a, o ou u, elle fait le son de « gare ». Ce n'est "
            "pas une exception : c'est une règle, et elle vaut pour tous les mots.",
            notes="Faire classer dix mots au tableau selon la lettre qui suit le g. Le "
                  "motif apparaît immédiatement.")

    d.piege("Le piège de « signature »",
            "sig-na-ture, en séparant le g et le n",
            "si-gna-ture, gn en un seul son",
            "Les lettres g et n forment un seul son, comme dans « ligne » ou "
            "« montagne ». Les séparer donne un mot que personne ne reconnaît. C'est un "
            "son qui n'existe pas dans beaucoup de langues : il demande de la pratique.",
            notes="Faire répéter « signature » et « signaler » cinq fois chacun. Ce sont "
                  "les deux mots du module qui contiennent ce son.")

    d.pratique('Pratique · 2 de 3', "Complétez avec ui, j, g ou gn",
               "Un seul groupe de lettres par trou.", [
        ("la si___ature (ce qu'on écrit au bas d'un formulaire)", "signature — gn"),
        ("a___ourd'hui (le jour où on est)", "aujourd'hui — j puis ui"),
        ("___oindre un reçu (l'ajouter à un envoi)", "joindre — j"),
        ("la li___e (une rangée, ou en ligne)", "ligne — gn"),
        ("la n___t (quand il fait noir)", "nuit — ui"),
        ("oran___é (la couleur)", "orangé — g devant e"),
    ], corrige=True,
       notes="Le deuxième item contient deux des trois sons. Le garder pour la fin de la "
             "correction.")

    d.pratique('Pratique · 3 de 3', "Trois phrases à lire à voix haute",
               "Le groupe corrige uniquement les trois sons.", [
        ("Aujourd'hui, je joins ma signature en ligne.", "les trois sons"),
        ("Depuis juillet, il travaille de nuit.", "ui · j · ui"),
        ("Il faut signaler le bris avant de gagner du temps.", "gn · gn"),
    ], corrige=True,
       notes="Faire lire debout et lentement. La première phrase contient les trois "
             "sons : c'est le test de la séance.")

    d.billet(
        "Écrivez trois mots du module, un pour chacun des trois sons.",
        exemples=[
            "Soulignez les lettres qui font le son.",
            "Exemple : « signature » — le son de « ligne », lettres gn.",
        ],
        notes="Corriger en circulant. Un élève qui écrit « aujourd'hui » pour le son de "
              "« jour » a raison aussi : le mot contient les deux.")

    return d.save(dossier)
