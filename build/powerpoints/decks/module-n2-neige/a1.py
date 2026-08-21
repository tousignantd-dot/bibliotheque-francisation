# -*- coding: utf-8 -*-
"""A1 · Il neige !
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercices `prVocab` et `pr1`.

Huitième module court du projet. L'élève de niveau 2 tient une phrase à la
fois : les diapositives portent peu de mots, et chaque phrase projetée est
une phrase qu'il dira vraiment en sortant de chez lui.

La situation du programme est « Météo », et son unique intention est en
compréhension écrite. Mais avant de lire un bulletin, il faut savoir nommer
ce qu'on voit par la fenêtre. La séance commence donc par les quatre mots du
ciel — la neige, la pluie, le vent, le soleil — et par la première neige
d'une personne qui n'en avait jamais vu.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-neige/images/')


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Il neige !",
        chapeau="Nommer le temps qu'il fait et dire s'il fait froid.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Commencer sans diapositive : demander à "
                  "chacun s'il avait déjà vu de la neige avant d'arriver ici, et ce "
                  "qu'il a pensé la première fois. Le groupe se sépare toujours en "
                  "deux, et la conversation part toute seule.")

    d.objectifs([
        "nommer quatre choses du ciel ;",
        "dire « il neige », « il pleut », « il vente » ;",
        "dire s'il fait froid ou s'il fait beau ;",
        "demander la température en une question.",
    ])

    d.declencheur(
        'Observation', "Quel temps fait-il sur cette photo ?",
        image=IMG + 'temps-neige.jpg',
        pistes=[
            "Qu'est-ce qui tombe du ciel ?",
            "De quelle couleur est la rue ?",
            "Est-ce qu'il fait froid ou chaud ?",
            "Vous, la première fois que vous avez vu la neige ?",
        ],
        notes="Laisser chercher le mot « neige » avant de le donner. La quatrième "
              "piste ouvre le groupe : certains l'ont vue à trente ans, d'autres "
              "sont nés dedans.")

    d.dialogue('Dialogue · 1 de 2', "Zina voit sa première neige", [
        ("ZINA", "Bonjour, monsieur Pelchat. Regardez dehors !", True),
        ("ROLAND", "Bonjour, madame Berrada. Oui, il neige depuis la nuit.", True),
        ("ZINA", "C'est ma première neige. C'est beau.", True),
        ("ROLAND", "C'est beau, oui. Mais il fait froid.", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Faire écouter deux fois, diapositive masquée. « Il neige » et « il fait "
             "froid » sont les deux phrases du module : les faire répéter par chacun, "
             "debout, avant de continuer.")

    d.dialogue('Dialogue · 2 de 2', "Il fait combien de degrés ?", [
        ("ZINA", "Il fait combien de degrés ?", True),
        ("ROLAND", "Moins douze. Et il vente.", True),
        ("ZINA", "Moins douze… Je n'ai pas de tuque.", True),
        ("ROLAND", "Alors mettez un foulard. Le vent, c'est le pire.", True),
    ], notes="Quatre répliques, et la journée est réglée. Faire remarquer que Zina "
             "répète le nombre entendu avant de répondre : c'est la stratégie du "
             "module au complet.")

    d.tableau('Analyse', "Ce que dit Zina, ce que répond son voisin",
              ["Zina dit", "Roland répond"],
              [["Regardez dehors !", "Il neige depuis la nuit."],
               ["C'est ma première neige.", "C'est beau. Mais il fait froid."],
               ["Il fait combien de degrés ?", "Moins douze. Et il vente."],
               ["Je n'ai pas de tuque.", "Alors mettez un foulard."]],
              cle=1,
              note="Deux ou trois mots par réplique. C'est tout ce qu'il faut.",
              notes="Diapositive à photographier. Faire jouer les quatre lignes à deux, "
                    "debout, avant de passer au vocabulaire.")

    d.vocabulaire('Vocabulaire', "Les quatre mots du ciel", [
        ("la neige", "L'eau blanche et froide qui tombe du ciel en hiver."),
        ("la pluie", "L'eau qui tombe du ciel quand il ne fait pas froid."),
        ("le vent", "L'air qui bouge fort et qui pousse tout dehors."),
        ("le soleil", "La lumière jaune du ciel quand il fait beau."),
    ], notes="Diapositive à photographier. Faire répéter chaque mot avec son article : "
             "l'article s'apprend avec le mot, jamais après.")

    d.regle("« Il neige. » — deux mots, et tout est dit.",
            "La météo se dit toujours avec « il ».",
            precision="Ce <b>il</b> ne remplace personne : ni un homme, ni le ciel. "
                      "C'est un mot obligatoire. On dit <b>il neige</b>, "
                      "<b>il pleut</b>, <b>il vente</b> — jamais « la neige neige ».",
            notes="Diapositive à photographier. Ne pas expliquer la phrase "
                  "impersonnelle : la faire répéter. L'explication vient en A3.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Il neige depuis la nuit.", "vrai"),
        ("C'est la première neige de Zina.", "vrai"),
        ("Il fait moins vingt degrés.", "faux - il fait moins douze"),
        ("Zina a une tuque.", "faux - elle met un foulard"),
    ], corrige=True, cols=1,
       notes="Quatre énoncés seulement. Les faire d'abord à l'oral, en groupe, avant de "
             "les faire écrire.")

    d.pratique('Pratique · à la fenêtre', "Deux par deux, debout",
               "Vingt minutes. Un élève regarde dehors, l'autre demande.", [
        ("Étape 1", "A dit bonjour et demande : « Quel temps fait-il ? »"),
        ("Étape 2", "B regarde vraiment par la fenêtre et répond en deux mots."),
        ("Étape 3", "A demande : « Il fait combien de degrés ? »"),
        ("Étape 4", "B répond, A répète le nombre, puis on échange les rôles."),
    ], cols=1,
       notes="Ouvrir le vrai bulletin du jour sur le téléphone avant de commencer. La "
             "température réelle vaut mieux qu'une température inventée.")

    d.billet(
        "Écrivez le temps qu'il fait aujourd'hui et le nom de trois choses du ciel.",
        exemples=[
            "Aujourd'hui, il neige.",
            "la neige",
            "le vent",
            "le soleil",
        ],
        notes="Devoir court. Demander l'article avec le mot : c'est là qu'il s'apprend, "
              "et le corriger plus tard coûte trois fois plus cher.")

    return d.save(dossier)
