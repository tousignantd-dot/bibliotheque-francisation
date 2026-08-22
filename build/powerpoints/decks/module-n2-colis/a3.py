# -*- coding: utf-8 -*-
"""A3 · Combien ça coûte ?
Bloc A « Je découvre » · couleur teal · 75 min. Dernière séance du bloc A.
Source : exercices `prImg`, `prCombien`, mini-leçon `prCombien`.

La question « Combien ça coûte ? » est écrite telle quelle dans le lexique du
programme pour cette situation. Elle vaut au comptoir postal, mais aussi
partout ailleurs : c'est la séance qui rapporte le plus longtemps.

Le module ne demande jamais de comprendre un prix compliqué : il demande de
l'entendre, de le redire, et de le faire répéter quand il est allé trop vite.
"""
import os

from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-colis/images/')


def _photo(nom):
    """La photo si elle est sur le disque, sinon rien. Voir `a1.py`."""
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre="Combien ça coûte ?",
        chapeau="Demander un prix, l'entendre en dollars, le redire pour "
                "vérifier, et faire répéter quand ça va trop vite.",
        duree='75 minutes')

    d.titre(notes="Séance de chiffres et de politesse. Apporter de la monnaie et des "
                  "billets : les élèves les manipulent pendant qu'on dit les montants. "
                  "Le prix se comprend plus vite quand il est dans la main.")

    d.objectifs([
        "poser la question « Combien ça coûte ? » ;",
        "lire un prix en dollars, à la virgule près ;",
        "redire un montant pour le vérifier ;",
        "demander poliment de répéter.",
    ])

    d.declencheur(
        'Observation', "Que se passe-t-il sur cette balance ?",
        image=_photo('poste-balance.jpg'),
        pistes=[
            "Pourquoi pèse-t-on un colis ?",
            "Est-ce que le prix est le même pour une lettre et pour une boîte ?",
            "Comment savoir le prix avant de payer ?",
            "Que dire si on n'a pas compris le montant ?",
        ],
        notes="La quatrième question est le cœur de la séance. Beaucoup d'élèves paient "
              "sans avoir compris, par gêne. Dire clairement que demander de répéter est "
              "poli, et que personne ne s'en formalise.")

    d.tableau('Analyse', "Un prix, et ce qu'on en fait",
              ['Ce qui est écrit', 'Ce qu\'on dit'],
              [["1,44 $", "un dollar quarante-quatre"],
               ["2,00 $", "deux dollars"],
               ["13,15 $", "treize dollars quinze"],
               ["0,95 $", "quatre-vingt-quinze cents"]],
              cle=2,
              note="La virgule sépare les dollars des cents. On ne dit jamais le mot "
                   "« virgule » : on dit les dollars, puis le nombre qui suit.",
              notes="Diapositive à photographier. Faire lire les quatre montants par "
                    "chaque élève, une fois. Écrire deux montants de plus au tableau et "
                    "les faire lire sans préparation.")

    d.cartes("Quatre phrases pour le comptoir", "À dire dans cet ordre", [
        ("Demander", "<b>Combien</b> ça coûte ?"),
        ("Vérifier", "Un dollar quarante-quatre ? — on redit le nombre, la voix monte."),
        ("Faire répéter", "Pouvez-vous <b>répéter</b>, s'il vous plaît ?"),
        ("Remercier", "Merci beaucoup. Bonne journée."),
    ], cols=2, notes="Diapositive à photographier. Faire dire les quatre phrases en chaîne, "
                     "par toute la classe, deux fois. Ce sont exactement les phrases "
                     "attendues à la séance E1.")

    d.regle("Redire le montant",
            "Un dollar quarante-quatre ?",
            precision="On répète le nombre qu'on a entendu, et la voix monte à la fin. "
                      "Ce n'est pas une hésitation : c'est une vérification. Le préposé "
                      "répond « oui » ou corrige, et l'affaire est réglée avant de payer.",
            notes="Diapositive à photographier. Faire entendre la différence entre la "
                  "voix qui descend (on affirme) et la voix qui monte (on vérifie). Deux "
                  "essais suffisent, la plupart des langues font pareil.")

    d.pratique('Vocabulaire', "Qu'est-ce qu'on voit sur la photo ?",
               "Associez chaque photo à ce qu'elle montre.", [
        ("Une enveloppe blanche, avec un timbre en haut, à droite.", "l'enveloppe"),
        ("Une boîte brune, fermée avec du ruban.", "le colis"),
        ("Une boîte rouge, au coin d'une rue.", "la boîte aux lettres"),
        ("Un comptoir, au fond d'une pharmacie.", "le comptoir postal"),
        ("Un carton qui dépasse d'une boîte aux lettres d'immeuble.", "l'avis de livraison"),
        ("Une boîte posée sur une balance.", "la balance du comptoir"),
    ], corrige=True, cols=2,
       notes="Les six mêmes photos sont dans le module en ligne, exercice `prImg`, à "
             "glisser sur la bonne phrase. Ici, on les nomme à voix haute avant de les "
             "manipuler ce soir.")

    d.pratique('Écriture', "Complétez la phrase du comptoir",
               "Un seul mot par phrase.", [
        ("___ ça coûte ?", "Combien"),
        ("Un timbre, s'il vous ___.", "plaît"),
        ("Je ___ envoyer cette lettre.", "veux"),
        ("1,44 $ : un dollar ___-quatre.", "quarante"),
        ("Pouvez-vous ___, s'il vous plaît ?", "répéter"),
        ("___ beaucoup. Bonne journée.", "Merci"),
    ], corrige=True, cols=2,
       notes="Les six mêmes phrases sont dans le module en ligne, exercice `prCombien`. "
             "Les faire d'abord à l'oral : le mot vient plus vite quand la phrase a été "
             "dite une fois.")

    d.pratique('Pratique · à deux', "Le prix change à chaque fois",
               "Deux par deux. L'un tient le comptoir, l'autre entre.", [
        ("Étape 1", "Celui du comptoir écrit un prix sur un papier, sans le montrer."),
        ("Étape 2", "L'autre demande : « Combien ça coûte ? »"),
        ("Étape 3", "Le prix est dit une seule fois, vite. On le fait répéter."),
        ("Étape 4", "On redit le montant, on vérifie sur le papier, on change de rôle."),
    ], cols=1,
       notes="Vingt minutes. C'est l'étape 3 qui compte : dire le prix trop vite exprès, "
             "pour que la phrase « pouvez-vous répéter » serve pour de vrai. Le prévenir "
             "au groupe, sinon certains croiront avoir échoué.")

    d.billet(
        "Écrivez trois prix en toutes lettres.",
        exemples=[
            "1,44 $ : un dollar quarante-quatre.",
            "2,50 $ : deux dollars cinquante.",
            "13,15 $ : treize dollars quinze.",
        ],
        notes="Devoir court. Demander d'en relever trois vrais, vus dans un magasin cette "
              "semaine, plutôt que d'en inventer.")

    return d.save(dossier)
