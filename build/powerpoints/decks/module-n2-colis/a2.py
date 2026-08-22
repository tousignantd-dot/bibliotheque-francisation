# -*- coding: utf-8 -*-
"""A2 · Le son de « timbre » et le son de « enveloppe ».
Bloc A « Je découvre » · couleur indigo · 75 min.
Source : exercice `prSon`, mini-leçon `prSon`.

La séance de graphie-phonie du module. Les deux premiers mots de la poste
portent chacun une voyelle nasale, et ce sont les deux que le niveau 2
confond le plus : celle de « cinq » et celle de « cent ». Deux nombres qu'on
dit tous les jours au comptoir — la phonétique sert ici tout de suite.
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
        code='A2', section='indigo',
        titre="Le son de « timbre », le son de « enveloppe »",
        chapeau="Deux sons qui passent par le nez. Ce qui les sépare, c'est "
                "la bouche : étirée pour l'un, grande ouverte pour l'autre.",
        duree='75 minutes')

    d.titre(notes="Séance d'oreille avant tout. Parler peu, faire écouter beaucoup. "
                  "Certains élèves n'entendront pas la différence au premier cours : "
                  "c'est normal, elle vient avec la répétition.")

    d.objectifs([
        "entendre la différence entre le son de « timbre » et celui de « enveloppe » ;",
        "reconnaître les quatre façons d'écrire chaque son ;",
        "appliquer la règle du m devant b et p ;",
        "dire « cinq » et « cent » sans les confondre.",
    ])

    d.declencheur(
        'Observation', "Écoutez : cinq, cent. Est-ce le même son ?",
        image=_photo('poste-colis.jpg'),
        pistes=[
            "Dites les deux nombres à voix haute.",
            "Est-ce que la bouche bouge de la même façon ?",
            "Écoutez maintenant : timbre, enveloppe.",
            "Où est la différence, à votre avis ?",
        ],
        notes="Dire les paires plusieurs fois, lentement, sans expliquer. Laisser le "
              "groupe chercher. La règle vient après l'oreille, jamais avant.")

    d.tableau('Analyse', "Deux sons du nez",
              ['Le son', 'On l\'entend dans'],
              [["Le son de <b>timbre</b>", "cinq · vingt · demain · un chemin"],
               ["Le son de <b>enveloppe</b>", "cent · trente · dedans · comment"],
               ["La bouche, pour le premier", "étirée, comme pour sourire"],
               ["La bouche, pour le second", "grande ouverte, la mâchoire descend"]],
              cle=2,
              note="Les deux passent par le nez. C'est la bouche qui décide lequel sort.",
              notes="Diapositive à photographier. Faire poser la main sous le menton : "
                    "pour le son de « enveloppe », la mâchoire descend. C'est le repère "
                    "le plus sûr, et il ne demande aucun vocabulaire.")

    d.cartes("Un son, quatre écritures", "Comment ça s'écrit", [
        ("Le son de « timbre »", "in · im · ain · ein — un chem<b>in</b>, un t<b>im</b>bre, "
                                 "dem<b>ain</b>, pl<b>ein</b>"),
        ("Le son de « enveloppe »", "an · am · en · em — ded<b>ans</b>, une l<b>am</b>pe, "
                                    "une <b>en</b>veloppe, nov<b>em</b>bre"),
        ("La règle du m", "Devant <b>b</b> et <b>p</b>, on écrit m et jamais n : "
                          "t<b>im</b>bre, l<b>am</b>pe, nov<b>em</b>bre"),
    ], cols=3, notes="Diapositive à photographier. Une seule règle, et l'orthographe de "
                     "quatre mots du module devient sûre. Faire chercher au groupe un "
                     "cinquième mot avec m devant b ou p.")

    d.regle("Le s entre le nez et la bouche",
            "Devant b et p, jamais n. On écrit m.",
            precision="C'est pour cela qu'on écrit un t<b>im</b>bre et non « un tinbre », "
                      "une l<b>am</b>pe et non « une lanpe ». Le son ne change pas ; "
                      "seule la lettre change.",
            notes="Diapositive à photographier. Écrire les deux formes au tableau, la "
                  "fausse barrée. Les élèves qui écrivent déjà en français font cette "
                  "faute-là plus que toute autre.")

    d.pratique('Écoute', "Le son de « timbre » ou celui de « enveloppe » ?",
               "Écoutez chaque mot et écrivez quel son vous entendez.", [
        ("un timbre", "le son de timbre"),
        ("une enveloppe", "le son de enveloppe"),
        ("cinq", "le son de timbre"),
        ("cent", "le son de enveloppe"),
        ("demain", "le son de timbre"),
        ("dedans", "le son de enveloppe"),
        ("un chemin", "le son de timbre"),
        ("trente", "le son de enveloppe"),
    ], corrige=True, cols=2,
       notes="Dire chaque mot trois fois, dans le désordre. Ne pas montrer l'écriture "
             "pendant l'écoute : c'est l'oreille qui travaille. Les huit mêmes mots sont "
             "dans le module en ligne, exercice `prSon`, avec un bouton d'écoute.")

    d.piege('Le piège', "un tambre", "un timbre",
            "Le mot le plus employé du module est aussi celui qui se déforme le plus. "
            "Dites-le en souriant : la bouche étirée donne le bon son toute seule. Même "
            "chose pour « une enveloppe », qu'on entend souvent « une inveloppe » : là, "
            "il faut au contraire ouvrir grand.",
            notes="Faire répéter les deux mots en chœur, lentement, puis à vitesse "
                  "normale. Y revenir en début de chaque séance suivante, trente secondes.")

    d.pratique('Pratique · à deux', "Le tri des deux sons",
               "Deux par deux, chacun son tour.", [
        ("Étape 1", "Choisissez huit mots dans la liste de l'écoute."),
        ("Étape 2", "Dites-les à votre voisin, un par un, dans le désordre."),
        ("Étape 3", "Votre voisin dit lequel des deux sons il entend."),
        ("Étape 4", "Changez de rôle, puis ajoutez deux mots à vous."),
    ], cols=1,
       notes="Vingt minutes. Circuler et redire soi-même le mot quand les deux élèves "
             "hésitent : ils ont besoin d'un modèle, pas d'un arbitre.")

    d.billet(
        "Dites ces trois phrases à voix haute, trois fois chacune.",
        exemples=[
            "Un timbre, s'il vous plaît.",
            "Cinq enveloppes, s'il vous plaît.",
            "Le colis arrive demain.",
        ],
        notes="Devoir d'oreille. Rappeler que la mini-leçon en ligne fait entendre chaque "
              "phrase autant de fois qu'on veut, et que le laboratoire y trie les deux "
              "sons tout seul.")

    return d.save(dossier)
