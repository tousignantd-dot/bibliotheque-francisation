# -*- coding: utf-8 -*-
"""D1 · Ce qui est écrit sur l'étiquette.
Bloc D « Défi 3 · Lire la posologie » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3vf` et `t3etiquette`.

C'est la seule intention du programme en compréhension écrite pour cette
situation : « lire une posologie ». Le défi 3 lui est entièrement consacré.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-pharmacie/images/')


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Ce qui est écrit sur l'étiquette",
        chapeau="Quatre lignes sur un petit papier blanc : combien, combien de "
                "fois, quand, pendant combien de jours. Tout le reste est du "
                "décor administratif.",
        duree='75 minutes')

    d.titre(notes="Première séance du défi 3. Apporter un vrai flacon vide si possible — "
                  "n'importe quelle étiquette de pharmacie fera l'affaire, en masquant "
                  "le nom. Rien ne remplace l'objet.")

    d.objectifs([
        "trouver les quatre renseignements d'une posologie ;",
        "comprendre « avec de la nourriture » ;",
        "savoir qu'on termine le traitement même si ça va mieux ;",
        "savoir quoi faire quand un comprimé est oublié.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qui est écrit sur cette étiquette ?",
        image=IMG + 'sac-pharmacie.jpg',
        pistes=[
            "Combien de lignes faut-il vraiment lire ?",
            "Où est écrit le nombre de comprimés par jour ?",
            "Qu'est-ce qu'on fait si on ne comprend pas ?",
        ],
        notes="La dernière question a une réponse simple et il faut la donner : on "
              "demande au pharmacien, sur place, avant de partir. Il n'y a pas de "
              "question idiote sur une posologie.")

    d.dialogue('Dialogue · 1 de 3', "Trois fois par jour, c'est quand ?", [
        ("ÉTIENNE", "Madame Belhadj ? Votre médicament est prêt.", True),
        ("NADIA", "Merci. Je peux vous poser une question sur l'étiquette ?", True),
        ("ÉTIENNE", "Bien sûr. Regardons ensemble. « Un comprimé, trois fois par jour. »", True),
        ("NADIA", "Trois fois par jour, c'est quand ?", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="La deuxième réplique de Nadia est la clé du module : elle demande. Faire "
             "répéter « Je peux vous poser une question sur l'étiquette ? » par tout le "
             "groupe.")

    d.dialogue('Dialogue · 2 de 3', "Avec de la nourriture", [
        ("ÉTIENNE", "Le matin, le midi et le soir. À peu près aux huit heures.", True),
        ("NADIA", "Et ici, c'est écrit « avec de la nourriture ».", True),
        ("ÉTIENNE", "Ça veut dire pendant le repas, ou juste après. Jamais l'estomac vide.", True),
        ("ÉTIENNE", "Vous finissez les sept jours, même si vous vous sentez mieux avant.", True),
    ], notes="Deux points à retenir : « avec de la nourriture » n'exige pas un gros "
             "repas, et on termine le traitement. Le second est le conseil que les "
             "pharmaciens répètent le plus.")

    d.dialogue('Dialogue · 3 de 3', "Et si j'oublie ?", [
        ("NADIA", "Si j'oublie un comprimé, qu'est-ce que je fais ?", True),
        ("ÉTIENNE", "Vous le prenez quand vous y pensez. Mais jamais deux en même temps.", True),
        ("NADIA", "Est-ce qu'il y a des effets secondaires ?", True),
        ("NADIA", "Je répète : un comprimé, trois fois par jour, avec de la nourriture, pendant sept jours.", True),
    ], notes="La dernière réplique est la meilleure habitude du module : répéter la "
             "posologie à voix haute avant de partir. La faire pratiquer par tout le "
             "groupe, mot à mot.")

    d.tableau('Analyse', "L'étiquette de Nadia, ligne par ligne",
              ["La ligne", "Ce qu'elle dit"],
              [["BELHADJ, Nadia", "votre nom, votre dossier"],
               ["21 comprimés de 250 mg", "ce qu'il y a dans le flacon"],
               ["1 comprimé, 3 fois par jour, 7 jours", "la posologie"],
               ["Ne pas en prendre 2 ensemble", "la mise en garde"],
               ["Renouvellements : 0", "ce qui reste"],
               ["Température de la pièce", "la conservation"]],
              cle=1,
              notes="Diapositive à photographier. Faire vérifier le calcul par le groupe : "
                    "3 × 7 = 21. Un compte qui ne tombe pas juste est une raison de "
                    "reposer une question au comptoir.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue et l'étiquette.", [
        ("Il faut prendre trois comprimés en même temps.", "faux — un comprimé, trois fois par jour"),
        ("Le traitement dure sept jours.", "vrai"),
        ("Il y a vingt et un comprimés dans le flacon.", "vrai"),
        ("On peut arrêter dès qu'on se sent mieux.", "faux — on termine les sept jours"),
        ("Si on oublie un comprimé, on peut en prendre deux.", "faux — jamais deux en même temps"),
        ("Ce médicament donne parfois mal au cœur.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la ligne exacte de l'étiquette ou la "
             "réplique du pharmacien.")

    d.billet(
        "Recopiez la posologie de Nadia et expliquez-la avec vos mots.",
        exemples=[
            "Combien de comprimés ? Combien de fois ?",
            "Quand, par rapport aux repas ? Pendant combien de jours ?",
        ],
        notes="Devoir court. Il prépare la séance D2, où les quatre renseignements "
              "deviennent quatre points de langue.")

    return d.save(dossier)
