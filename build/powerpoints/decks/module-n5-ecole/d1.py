# -*- coding: utf-8 -*-
"""D1 · Ce qui me bloque, c'est l'horaire
Bloc D « Défi 3 · Demander un changement » · couleur acier · 75 min.
Source du module : dialogue `t3`, exercices `t3a` et `t3emph`.
"""
import os
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-ecole/images/')


def img(nom):
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Ce qui me bloque, c'est l'horaire",
        chapeau="Amelia est revenue, et sa vie a changé pendant qu'elle "
                "était partie : elle travaille le matin. Demander un "
                "changement, ce n'est pas se plaindre — c'est nommer ce qui "
                "bloque et proposer une solution.",
        duree='75 minutes')

    d.titre(notes="Première séance du Défi 3. Ouvrir en posant la question au groupe : "
                  "« qui a déjà eu besoin de changer quelque chose à son dossier ? ». "
                  "Presque toutes les mains se lèvent, et presque personne n'a osé le "
                  "demander. C'est exactement le sujet.")

    d.objectifs([
        "séparer ce qui bloque de ce qui déplaît ;",
        "proposer une solution et accepter ce qu'elle coûte ;",
        "mettre en avant l'essentiel avec « ce qui…, c'est… » ;",
        "distinguer l'attestation de fréquentation du relevé des apprentissages.",
    ])

    d.declencheur(
        'Observation', "Que vient-on faire dans ce bureau ?",
        image=img('bureau-conseiller.jpg'),
        pistes=[
            "À qui parle-t-on dans un centre quand l'horaire ne tient plus ?",
            "Est-ce qu'on demande un changement au secrétariat ou au conseiller ?",
            "Qu'est-ce qu'on apporte avec soi, à un rendez-vous comme celui-là ?",
            "Combien de temps dure ce genre de conversation ?",
        ],
        notes="La deuxième question reprend le bloc A : le secrétariat imprime et "
              "reçoit, le conseiller décide et oriente. Beaucoup d'élèves frappent à "
              "la mauvaise porte et repartent découragés.")

    d.dialogue('Dialogue · 1 de 4', "Il faut que je vous parle de mon horaire", [
        ("AMELIA", "Monsieur Gauthier, il faut que je vous parle de mon horaire.", True),
        ("RÉMI", "Asseyez-vous. Qu'est-ce qui se passe depuis votre retour ?", True),
        ("AMELIA", "J'ai trouvé un emploi. Je commence à sept heures le matin.", True),
        ("RÉMI", "Ah. Et nos cours de jour finissent à midi et demi.", True),
    ], consigne="Écoutez deux fois avant de lire le texte.",
       notes="Faire remarquer la première réplique : Amelia annonce le sujet avant "
             "d'expliquer quoi que ce soit. C'est la règle des demandes, à l'oral "
             "comme à l'écrit.")

    d.dialogue('Dialogue · 2 de 4', "L'horaire, pas le cours", [
        ("AMELIA", "Ce qui me bloque, c'est l'horaire, pas le cours. J'aime le cours.", True),
        ("RÉMI", "Vous voulez passer au groupe du soir, si je comprends bien.", True),
        ("AMELIA", "Oui. Il faut que je travaille, sinon je ne paie pas mon loyer.", True),
        ("RÉMI", "C'est légitime. Par contre, le soir, c'est quatre soirs par semaine.", True),
    ], notes="La première réplique est la phrase-clé du module. L'écrire au tableau et "
             "la laisser toute la séance : elle sépare le problème de tout le reste, "
             "et la personne en face se met alors à chercher une solution.")

    d.dialogue('Dialogue · 3 de 4', "Quatre soirs, je peux", [
        ("AMELIA", "Quatre soirs, je peux. Comme je finis à trois heures, ça se place.", True),
        ("RÉMI", "Bien. Pour que le transfert se fasse, il me faut une demande écrite.", True),
        ("AMELIA", "Je dois l'écrire comment ? Je n'ai jamais fait ça en français.", True),
        ("RÉMI", "Court. Qui vous êtes, ce que vous demandez, pourquoi, et à partir de quand.", True),
    ], notes="Amelia accepte le prix de ce qu'elle demande avant qu'on le lui "
             "demande. Une demande sans contrepartie acceptée n'est qu'un souhait : "
             "le dire au groupe en ces mots.")

    d.dialogue('Dialogue · 4 de 4', "Gardez-en une copie", [
        ("AMELIA", "Et mon employeur veut une preuve que je suis inscrite ici.", True),
        ("RÉMI", "Une attestation de fréquentation. Le secrétariat l'imprime sur-le-champ.", True),
        ("AMELIA", "Ce n'est pas la même chose que le relevé, alors ?", True),
        ("RÉMI", "Non. Le relevé des apprentissages vient du ministère, à la fin du cours.", True),
    ], notes="Terminer sur la dernière réplique du dialogue, qu'on lira au groupe : "
             "« gardez-en une copie : c'est votre dossier, pas le nôtre ». C'est la "
             "phrase la plus utile du module hors de la classe.")

    d.regle("Nommer ce qui bloque, pas ce qui déplaît",
            "Ce qui me bloque, c'est l'horaire, pas le cours.",
            precision="Une phrase qui sépare le problème de tout le reste. La personne "
                      "en face cesse alors de chercher ce qui ne va pas et se met à "
                      "chercher une solution — ce sont deux conversations très "
                      "différentes.",
            notes="Diapositive à photographier. Faire produire à chaque élève une "
                  "phrase sur ce modèle, à propos d'une vraie situation. C'est le "
                  "meilleur travail de la séance.")

    d.tableau('Analyse', "Deux papiers qu'on confond",
              ["Le papier", "Ce qu'il dit, et d'où il vient"],
              [["L'attestation de fréquentation", "vous êtes inscrit ici en ce moment ; le secrétariat l'imprime"],
               ["Le relevé des apprentissages", "ce que vous avez réussi ; il vient du ministère, après le cours"],
               ["Ce que l'employeur demande", "presque toujours l'attestation, avec les heures par semaine"],
               ["Ce qu'il faut demander avant de partir", "le délai : combien de temps ça prend, d'habitude"]],
              cle=1,
              notes="Diapositive à photographier. Demander l'un pour l'autre fait "
                    "perdre un voyage, et c'est arrivé à quelqu'un dans le groupe : "
                    "laisser raconter.")

    d.regle("Ce qui…, c'est… — mettre un mot devant tous les autres",
            "L'horaire me bloque devient : Ce qui me bloque, c'est l'horaire.",
            precision="La même information, mais l'horaire est maintenant au bout de "
                      "la phrase, à l'endroit où l'oreille s'arrête. Une seule par "
                      "demande : trois de suite, et plus rien n'est éclairé.",
            notes="Diapositive à photographier. C'est la phrase emphatique du "
                  "programme du niveau 5. Elle revient au Défi 3 du module 13 : ceux "
                  "qui l'ont déjà vue la reconnaissent, les autres la découvrent ici.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Relisez le dialogue du bureau, puis répondez.", [
        ("Amelia a trouvé un emploi qui commence à sept heures le matin.", "vrai"),
        ("Elle n'aime plus le cours et veut arrêter.", "faux — c'est l'horaire"),
        ("Le groupe du soir demande quatre soirs par semaine.", "vrai"),
        ("Le transfert se fait sans demande écrite.", "faux — il en faut une"),
        ("Le relevé des apprentissages s'imprime au secrétariat.", "faux — il vient du ministère"),
        ("Monsieur Gauthier lui conseille de garder une copie.", "vrai"),
    ], corrige=True,
       notes="Six des huit énoncés de l'exercice `t3a`. Les faire d'abord sans le "
             "texte sous les yeux : c'est de la compréhension orale.")

    d.pratique('Écriture', "Ce qui, ce que, c'est, c'est que",
               "Complétez pour mettre en avant ce qui compte.", [
        ("___ me bloque, c'est l'horaire du matin, pas le cours.", "Ce qui"),
        ("Ce que je demande, ___ un transfert au groupe du soir.", "c'est"),
        ("___ je ne comprends pas, c'est la date écrite en gras.", "Ce que"),
        ("Ce qui me dérange, ___ le cours finit à midi et demi.", "c'est que"),
        ("___ me manque, c'est une attestation pour mon employeur.", "Ce qui"),
        ("Ce qui compte pour moi, ___ de finir le cours cette année.", "c'est"),
    ], corrige=True, cols=2,
       notes="Ce sont les six items de l'exercice `t3emph`. Le quatrième est le seul "
             "difficile : dès qu'un verbe conjugué suit, il faut « c'est que ». Sans "
             "le que, la phrase s'arrête au milieu.")

    d.billet(
        "Écrivez ce qui vous bloque, dans une vraie situation, avec « ce qui…, c'est… ».",
        exemples=[
            "Une seule phrase, sur quelque chose de vrai.",
            "Ajoutez ce que vous demanderiez, et à partir de quand.",
        ],
        notes="Ramasser les billets et les rendre en D2 : ils sont la deuxième phrase "
              "de la demande écrite, déjà prête.")

    return d.save(dossier)
