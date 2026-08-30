# -*- coding: utf-8 -*-
"""P4 · Le point express — la gamme qui occupe la place vide.

Section teal, comme les autres diaporamas de la trousse. Se projette seul :
c'est une présentation de concept, pas le troisième quart d'heure d'une
rencontre de vente. D'où son propre parcours, et non les trois temps de
`parcours.py`.

Les chiffres viennent de `chiffres.py` — relevés sur le dépôt — sauf ceux des
points express, qui n'y sont pas encore : ils sont comptés ici, à la même
source que la page écran (`build/point_express.py`).
"""
import os
import pathlib
import re
import sys

from theme import Deck
from chiffres import CH, n

RACINE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(RACINE, 'build'))

TEMPS = [("Le problème", "3 min"),
         ("Ce que c'est", "5 min"),
         ("Ce que ça coûte", "3 min"),
         ("Ce qui reste à faire", "2 min")]


def compter():
    """Les deux chiffres que `chiffres.py` ne relève pas encore."""
    base = pathlib.Path(RACINE)
    modules = len(list((base / 'assets' / 'interactive').glob('module-*')))
    minilecons = sum(len(re.findall(r"eye:'Mini-leçon'", f.read_text(encoding='utf-8')))
                     for f in (base / 'build' / 'contenu').glob('*/plus.js'))
    return modules, minilecons


def points_express():
    """Les points produits, comptés sur le disque. Jamais une liste écrite ici."""
    from storyline import lire_bloc, fichiers
    out = []
    for f in fichiers():
        if f.parent.name != 'parcours':
            continue
        src = f.read_text(encoding='utf-8')
        p = lire_bloc(src, 'PARCOURS') or {}
        e = lire_bloc(src, 'ECRANS') or []
        out.append((p.get('titre', f.stem), p.get('savoir', ''), len(e)))
    return out


def build(dossier):
    pts = points_express()
    n_pts = len(pts)
    n_ecr = sum(x[2] for x in pts)
    n_modules, n_minilecons = compter()

    d = Deck(
        code='P4', section='teal',
        titre="Le point express",
        chapeau="Dix minutes de temps mort transformées en une notion réglée. La gamme "
                "qui occupe la seule place que ni le cours du matin ni l'atelier de "
                "l'après-midi n'occupent : l'élève seul, entre deux cours.",
        duree='13 minutes')

    d.titre(surtitre="LE POINT EXPRESS",
            notes="Ne pas commencer par l'outil. Demander d'abord ce que font leurs élèves "
                  "dans l'autobus, et laisser répondre. Tout le monde connaît la réponse.")

    d.parcours(TEMPS, 0,
               notes="Quatre temps, treize minutes. Annoncer la durée : une salle qui sait "
                     "combien il reste écoute mieux.")

    # ── 1. Le problème ────────────────────────────────────────────────────
    d.chapitre("PREMIER TEMPS", "Deux personnes, la même impasse",
               "L'élève a le temps mais pas l'occasion. L'enseignant a le diagnostic "
               "mais pas le remède.",
               notes="Jalon. Laisser deux secondes de silence : c'est la phrase que la "
                     "salle doit emporter.")

    d.cartes("LE PROBLÈME", "Ce que chacun a, et ce qui lui manque", [
        ("L'élève, le mardi soir",
         "Il sait qu'il se trompe, sans savoir sur quoi. Une longue page de module ne lui "
         "dit ni par où entrer ni quand il aura fini. Alors il fait défiler autre chose. "
         "Le temps est là — l'occasion, non."),
        ("L'enseignant, le lendemain",
         "Il voit la faute, il sait laquelle, il sait même qui l'a faite trois fois. Et il "
         "n'a rien à envoyer, sinon reprendre la notion devant vingt-quatre personnes dont "
         "vingt n'en ont pas besoin. Le diagnostic est là — le remède, non."),
    ], notes="Insister sur la deuxième carte devant des enseignants : c'est celle qu'ils "
             "reconnaissent tout de suite. Devant une direction, c'est la première.")

    d.regle("CE QUE C'EST",
            "Un point express, c'est une notion, dix minutes, "
            "envoyée à une personne.",
            precision="Ni un cours ni un exercice de plus : une réponse. Et elle se referme "
                      "quand la difficulté est réglée.",
            notes="La diapositive qu'on photographie. Ne rien ajouter à l'oral, laisser "
                  "lire.")

    # ── 2. Ce que c'est ───────────────────────────────────────────────────
    d.chapitre("DEUXIÈME TEMPS", "Comment ça circule",
               "Constater, envoyer, faire, refermer. Un cycle qui a une fin — c'est ce "
               "qui le distingue de tout le reste du matériel.",
               notes="Le mot important est « refermer ». Aujourd'hui, rien ne se referme.")

    d.tableau("LE CYCLE", "Quatre moments, et qui les tient",
              ["", "Ce qui se passe", "Qui"],
              [["1 · Constater", "Une lacune se voit dans une production écrite.",
                "L'enseignant"],
               ["2 · Envoyer", "Un bouton à côté du point faible.", "L'enseignant"],
               ["3 · Faire", "Dix minutes, le soir, sur son téléphone.", "L'élève, seul"],
               ["4 · Refermer", "Réussi sans rattrapage : c'est réglé.", "Le point"]],
              cle=0,
              notes="Si on ne retient qu'une chose de la présentation, c'est ce tableau. "
                    "À dire à voix haute, parce que ça ne tient pas sur la diapositive : "
                    "le diagnostic reste à l'enseignant, rien ne se déclenche tout seul, "
                    "et ce n'est pas une étape en attendant mieux — c'est une décision de "
                    "conception. C'est ce qui rassure les enseignants.")

    d.piege("CE QUE CE N'EST PAS",
            "« C'est une petite leçon de grammaire sur le téléphone. »",
            "L'élève tranche des cas AVANT qu'aucune règle ne lui soit dite.",
            "Nos modules portent déjà %s mini-leçons. Un élève envoyé sur un point express "
            "en a probablement lu deux sur le même sujet : redire la même chose autrement "
            "ne servirait à rien. La leçon donne la règle puis la fait appliquer ; le point "
            "express fait l'inverse, et n'énonce la règle qu'une fois les cas tranchés."
            % n(n_minilecons),
            notes="C'est l'objection numéro un, et elle vient toujours d'un enseignant "
                  "d'expérience. Répondre par l'exemple du passé composé : on fait ranger "
                  "huit verbes avant d'avoir dit un mot de la règle.")

    d.cartes("LES TROIS GAMMES", "Où ça se range", [
        ("Le module · 4 h, le matin, en groupe",
         "Une situation de la vie réelle en seize séances. « Que faut-il savoir faire pour "
         "prendre un rendez-vous ? » L'enseignant est là, et c'est sa force."),
        ("L'atelier · 2 h, l'après-midi",
         "Une pratique libre, sans date. « Comment m'exercer à ce que je viens de voir ? »"),
        ("Le point express · 10 min, seul",
         "Une notion précise, envoyée à une personne. « Pourquoi est-ce que je me trompe "
         "encore là-dessus ? » Personne n'est à côté : l'explication est dans l'écran."),
    ], cols=3,
       notes="Trois questions différentes, trois gammes. Le point express ne remplace "
             "rien : il occupe une place vide.")

    # ── 3. Ce que ça coûte ────────────────────────────────────────────────
    d.chapitre("TROISIÈME TEMPS", "Ce que ça coûte",
               "Dix écrans, pas soixante-dix-sept. La question s'est posée autrement au "
               "départ, et le calcul a tranché.",
               notes="Ici on parle argent et temps. C'est le moment où une direction se "
                     "réveille.")

    d.tableau("LE CALCUL", "Pourquoi on ne refait pas les modules dans cette forme",
              ["", "", "Écrans"],
              [["Un module entier", "six sections, trois défis", "~77"],
               ["Le catalogue", "les %s modules" % n(n_modules), "~6 700"],
               ["Un point express", "un savoir, dix minutes", "~10"],
               ["Quatorze points", "ce qui coince le plus", "~140"]],
              notes="Ne pas lire les chiffres un par un. Dire seulement : « refaire les "
                    "modules coûterait quarante fois le prix, et leur ferait perdre ce "
                    "qu'ils savent faire » — la projection, les fiches papier, le jeu de "
                    "rôle à deux, la production orale relue par un humain.")

    d.regle("COÛT MÉDIA",
            "Un point express ne fait produire aucun son, aucune image.",
            precision="Il rejoue les extraits déjà en place — %s fichiers sonores — et n'en "
                      "copie aucun." % n(CH['mp3']),
            notes="Celui sur le passé composé n'a même pas de son : cette faute n'existe "
                  "qu'à l'écrit, et c'est le sujet du point. Le dire, ça marque.")

    # ── 4. Ce qui reste ───────────────────────────────────────────────────
    d.chapitre("QUATRIÈME TEMPS", "Où en est le chantier",
               "Le moteur tourne et les premiers points se jouent. Ce qui manque est le "
               "chaînon du milieu, et il est court.",
               notes="Finir sur ce qui reste, jamais sur ce qui est fait : c'est ce qui "
                     "appelle une décision.")

    d.tableau("L'ÉTAT", "Fait, à faire, plus tard",
              ["", "Ce que ça couvre"],
              [["Fait", "Le moteur et ses trois types d'écran. %d points jouables, "
                        "%d écrans écrits." % (n_pts, n_ecr)],
               ["À faire", "L'envoi : le bouton chez l'enseignant, la bande chez l'élève, "
                           "le retour du résultat."],
               ["Plus tard", "Étiqueter les exercices par savoir, pour proposer — sans "
                             "jamais décider."]],
              cle=0,
              notes="La ligne « plus tard » est celle qu'on vous demandera. Répondre que "
                    "le diagnostic reste à l'enseignant, et que c'est un choix, pas une "
                    "limite technique.")

    d.billet("Ce qu'on peut essayer dès demain : ouvrir un point express sur un téléphone, "
             "devant la classe, et le faire jusqu'au bout. Il dure dix minutes.",
             notes="Terminer là-dessus. Une démonstration de dix minutes vaut mieux "
                   "qu'une promesse.")

    return d.save(dossier)
