# -*- coding: utf-8 -*-
"""B3 · Annoncer son sujet
Bloc B « Défi 1 · La lettre de motivation » · couleur ambre · 75 min.
Source : exercice `t1topic` et sa mini-leçon (connecteurs de topicalisation).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre='Annoncer son sujet',
        chapeau="Trois mots préviennent le lecteur du changement de sujet "
                "avant qu'il ne l'ait deviné. Dans une lettre formelle, ils "
                "remplacent le paragraphe qu'on n'a pas la place d'écrire.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire du texte. Les items sont longs : prévoir de "
                  "faire lire chaque phrase en entier à voix haute avant de la "
                  "compléter.")

    d.objectifs([
        "employer « quant à » devant un groupe du nom ;",
        "employer « en ce qui concerne » dans une lettre ;",
        "reconnaître « à l'égard de » dans un avis administratif ;",
        "distinguer annoncer un sujet et relier deux idées.",
    ], notes="Le quatrième objectif est le vrai enjeu : ces connecteurs annoncent, ils "
             "ne relient pas. Un texte qui n'a que des annonces n'a aucune "
             "progression.")

    d.declencheur(
        'Observation', "Comment savez-vous qu'un texte change de sujet ?",
        pistes=[
            "Un nouveau paragraphe ? Un mot en particulier ?",
            "Que faites-vous quand le changement n'est pas annoncé ?",
            "Combien de fois relisez-vous alors la phrase ?",
            "Qui perd du temps : celui qui écrit ou celui qui lit ?",
        ],
        notes="Faire lire un paragraphe sans connecteur, puis le même avec. La "
              "différence de vitesse de lecture est mesurable au chronomètre, et le "
              "groupe l'entend.")

    d.tableau('Analyse', "Quatre façons d'annoncer un sujet",
              ['Le connecteur', 'Où il va'],
              [['quant à', "le plus court : quant à mes disponibilités"],
               ['en ce qui concerne', "le plus neutre, passe partout à l'écrit"],
               ["à l'égard de", "le plus formel, souvent dans un avis officiel"],
               ['pour ce qui est de', "la forme parlée, juste en entrevue"]],
              cle=0,
              note="Ils annoncent le sujet du paragraphe ; ils ne remplacent ni "
                   "« donc », ni « parce que », ni « par contre ».",
              notes="Diapositive à photographier. Faire remarquer la contraction : "
                    "quant au transport, quant aux stages.")

    d.regle("Quant à se met devant un nom, jamais devant un verbe",
            "Quant à mes disponibilités, quant au transport, quant aux stages.",
            precision="Devant un verbe conjugué, il faut « en ce qui concerne le fait "
                      "que », ce qui est lourd : mieux vaut alors nommer la chose. "
                      "Écrire « quand à » au lieu de « quant à » est la faute la plus "
                      "fréquente, et elle se voit dans une lettre relue.",
            notes="Diapositive à photographier. Le truc qui marche : « quant » a la "
                  "même racine que « quantité », et rien à voir avec le temps.")

    d.pratique('Grammaire', "Complétez avec le bon connecteur",
               "Un connecteur par phrase, en tête et suivi d'une virgule.", [
        ("___ mes disponibilités, elles sont réglées depuis février.", "Quant à"),
        ("___ le préalable de mathématiques, je suis inscrite à la mise à niveau.", "En ce qui concerne"),
        ("La décision rendue ___ ma candidature m'a été communiquée le 10 avril.", "à l'égard de"),
        ("___ stages, je peux me rendre partout dans la région.", "Quant aux"),
        ("___ transport, j'ai mon permis depuis deux ans.", "Pour ce qui est du"),
        ("___ mes deux années d'études, je n'en demande aucune reconnaissance.", "Quant à"),
    ], corrige=True,
       notes="Faire lire la phrase complète à voix haute une fois corrigée. La "
             "virgule après le connecteur s'entend, et c'est ainsi qu'on la retient.")

    d.piege('Piège', "Quand à mes disponibilités, elles sont réglées.",
            "Quant à mes disponibilités, elles sont réglées.",
            "« Quand » parle du temps ; « quant à » annonce un sujet. À l'oral ils se "
            "ressemblent, à l'écrit la faute saute aux yeux dans une lettre formelle.",
            notes="Écrire les deux au tableau, côte à côte, et les laisser jusqu'à la "
                  "fin du bloc.")

    d.cartes('Emploi', "Un connecteur, un paragraphe", [
        ("Un seul par paragraphe",
         "Deux annonces veulent dire deux sujets : coupez le paragraphe en deux, il "
         "sera plus clair."),
        ("Toujours en tête",
         "Le lecteur doit savoir de quoi on parle avant de lire la phrase, pas après."),
        ("Suivi d'une virgule",
         "Quant à mes disponibilités, elles sont réglées depuis février."),
        ("Jamais pour relier",
         "Pour relier : donc, parce que, par contre, par conséquent."),
    ], notes="Quatre cartes qui tiennent le reste du bloc. Les faire recopier dans le "
             "cahier : elles serviront à l'écriture de E2.")

    d.billet("Écris deux phrases de ta lettre qui commencent par un connecteur "
             "d'annonce.",
             exemples=["Quant à mon horaire, il est réglé depuis le mois de mars.",
                       "En ce qui concerne le préalable, je suis déjà inscrite."],
             notes="Ramasser les billets. Vérifier une seule chose : un nom après le "
                   "connecteur, jamais un verbe conjugué.")

    return d.save(dossier)
