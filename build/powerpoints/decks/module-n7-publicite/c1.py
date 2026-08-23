# -*- coding: utf-8 -*-
"""C1 · Lire un dépliant du bas vers le haut
Bloc C « Défi 2 · L'astérisque et les petits caractères » · acier · 75 min.
Source : dialogue `t2`, exercices `t2vf` et `t2depliant`.
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n7-publicite' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Lire un dépliant du bas vers le haut",
        chapeau="Le haut d'une publicité est écrit pour vous faire venir. Le "
                "bas est écrit pour protéger l'annonceur. C'est le bas que "
                "vous signez.",
        duree='75 minutes')

    d.titre(notes="Première séance du Défi 2. Faire sortir les circulaires et les "
                  "dépliants rapportés en A3 : la séance fonctionne beaucoup mieux "
                  "avec du vrai papier sur les tables.")

    d.objectifs([
        "lire une publicité écrite en commençant par le bas ;",
        "suivre un astérisque jusqu'à sa condition ;",
        "poser à un dépliant les quatre questions qui comptent ;",
        "calculer le total réel d'une première année.",
    ], notes="Le quatrième objectif se refait devant n'importe quelle offre. C'est le "
             "geste le plus transférable de tout le module.")

    d.declencheur(
        'Observation', "Par où commencez-vous à lire ?",
        image=IMG + 'vitrine-rue.jpg',
        pistes=[
            "Le titre, la photo, ou la petite ligne du bas ?",
            "Combien de temps donnez-vous à un dépliant, en général ?",
            "Avez-vous déjà lu une condition écrite en entier ?",
            "Qu'est-ce qui vous en a empêché : le temps, ou les mots ?",
        ],
        notes="La dernière question est celle qui vaut la peine. Ce n'est presque "
              "jamais le temps : ce sont les tournures, et c'est exactement ce que "
              "les trois séances suivantes travaillent.")

    d.dialogue('Dialogue · 1 de 3', "On lit à l'envers", [
        ("DORIANE", "Posez les deux sur la table, côte à côte. On va lire le dépliant à l'envers.", True),
        ("YAMILÉ", "À l'envers ?", True),
        ("DORIANE", "En commençant par le bas. Le haut est écrit pour vous faire venir ; le bas pour protéger l'annonceur.", True),
        ("DORIANE", "C'est en bas que se trouve ce que vous avez signé. Lisez-moi la plus petite ligne.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire faire le geste réellement : chaque élève retourne son dépliant et "
             "cherche la plus petite ligne. Certains ne la trouvent pas — c'est aussi "
             "une donnée.")

    d.dialogue('Dialogue · 2 de 3', "Quatre renseignements dans une ligne", [
        ("YAMILÉ", "« Terme minimal de douze mois. Frais d'adhésion uniques de soixante dollars exigibles à la signature. »", True),
        ("YAMILÉ", "« Le tarif hebdomadaire est prélevé aux quatre semaines. Les taxes ne sont pas comprises. » Ce n'est pas court.", True),
        ("DORIANE", "Ce n'est jamais court. Combien de renseignements y a-t-il là-dedans ?", True),
        ("YAMILÉ", "Quatre. Et pas un seul dans la grosse ligne.", True),
    ], notes="Faire compter par le groupe avant de donner la réponse. Quatre "
             "renseignements, dont trois coûtent de l'argent.")

    d.dialogue('Dialogue · 3 de 3', "Le vrai total", [
        ("YAMILÉ", "Alors mon vrai prix, la première année, c'est combien ?", True),
        ("DORIANE", "Neuf quatre-vingt-dix-neuf par semaine, cinquante-deux semaines : cinq cent dix-neuf dollars et quarante-huit cents.", True),
        ("DORIANE", "Plus soixante de frais d'adhésion. Cinq cent soixante-dix-neuf dollars et quarante-huit cents, avant les taxes.", True),
        ("YAMILÉ", "L'annonce aurait pu écrire ce chiffre-là.", True),
    ], notes="Le calcul se refait au tableau, calculatrice permise. C'est le chiffre "
             "que l'annonce n'écrit jamais, et c'est le seul qui compte.")

    d.tableau('Analyse', "Quatre questions à poser à un dépliant",
              ['La question', 'Où se trouve la réponse'],
              [["Combien en tout ?", "nulle part : il faut la calculer"],
               ["Pendant combien de temps ?", "terme, minimal, adhésion de … mois"],
               ["Qu'est-ce qui s'ajoute ?", "exigible, applicable, en sus"],
               ["Comment est-ce que je sors ?", "annulation, préavis, mensualités"]],
              cle=0,
              note="La première n'a jamais de réponse écrite. C'est elle qui compte.",
              notes="Diapositive à photographier. Les quatre questions se posent dans "
                    "cet ordre, et la première se répond avec une calculatrice.")

    d.regle("L'étoile est un renvoi, jamais une décoration",
            "Un astérisque annonce qu'une condition existe ailleurs sur la "
            "page. Votre œil doit descendre avant de faire quoi que ce soit.",
            precision="Et s'il n'y a rien en bas, c'est plus grave, pas moins : une "
                      "promesse à laquelle aucune condition écrite ne correspond est "
                      "précisément ce que la loi appelle une représentation trompeuse.",
            notes="Diapositive à photographier. Conseil pratique à donner : "
                  "photographier le dépliant en entier, bas de page compris, avant de "
                  "signer quoi que ce soit.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Doriane conseille de lire le dépliant en commençant par le bas.", "vrai"),
        ("La plus petite ligne contient quatre renseignements.", "vrai"),
        ("Les frais d'adhésion sont prélevés chaque semaine.", "faux - une seule fois"),
        ("Le total de la première année dépasse cinq cent soixante-dix dollars.", "vrai"),
        ("Un astérisque sans condition écrite est moins grave.", "faux - c'est plus grave"),
        ("« Des frais sont exigibles » dit qui les exige.", "faux - personne n'est nommé"),
    ], corrige=True,
       notes="Exercice `t2vf` du module. Le dernier item ouvre la séance C2 : garder "
             "la remarque pour la fin et l'annoncer.")

    d.billet(
        "Sur votre dépliant, trouvez la plus petite ligne et recopiez-la.",
        exemples=[
            "Recopiez-la en entier, même si vous ne comprenez pas tout.",
            "Soulignez les mots que vous ne comprenez pas.",
        ],
        notes="Devoir de lecture. Les mots soulignés donnent la liste de vocabulaire "
              "réelle du groupe pour C4 — souvent plus juste que celle du module.")

    return d.save(dossier)
