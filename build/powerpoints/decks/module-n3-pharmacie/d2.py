# -*- coding: utf-8 -*-
"""D2 · Trois fois par jour, pas plus de quatre.
Bloc D « Défi 3 · Lire la posologie » · couleur ambre (écriture) · 75 min.
Source : exercices `t3frequence`, `t3imperatif`, `t3plusde` et `t3pictos`.

Trois points de langue pour un seul moment : dire quand et combien de fois,
comprendre les consignes à l'impératif, lire les mises en garde chiffrées.
Le programme les nomme tous les trois pour cette situation — marqueurs de
fréquence, impératif présent, « de plus de » et « de moins de ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre='Trois fois par jour, pas plus de quatre',
        chapeau="Trois points de langue pour la même étiquette : compter les "
                "prises, comprendre les ordres polis, et lire les chiffres qui "
                "protègent.",
        duree='75 minutes')

    d.titre(notes="Dernière séance de contenu du module. Elle réunit les trois points de "
                  "langue du défi 3. Prévoir du temps : c'est la séance la plus dense, "
                  "et la plus utile hors de la classe.")

    d.objectifs([
        "dire combien de fois par jour et pendant combien de jours ;",
        "comprendre « aux huit heures » et « avec de la nourriture » ;",
        "lire les consignes à l'impératif, à la forme positive et négative ;",
        "comprendre « pas plus de », « de moins de » et « au moins ».",
    ])

    d.tableau('Analyse · 1', "Compter les prises",
              ["Ce qu'on lit", "Ce que ça veut dire"],
              [["trois fois par jour", "le matin, le midi et le soir"],
               ["deux fois par semaine", "deux jours, pas tous les jours"],
               ["aux huit heures", "huit heures entre deux comprimés"],
               ["avec de la nourriture", "pendant le repas ou juste après"],
               ["au coucher", "juste avant de dormir"]],
              cle=0,
              note="Après « par », le mot reste au singulier.",
              notes="Diapositive à photographier. « Aux huit heures » est une formule "
                    "d'ici que personne ne devine : la faire répéter et expliquer deux "
                    "fois.")

    d.regle("La formule la plus fréquente",
            "« un comprimé, trois fois par jour »",
            precision="Un comprimé chaque fois, trois fois dans la journée — "
                      "jamais trois comprimés d'un coup. C'est la confusion la "
                      "plus dangereuse de toute l'étiquette.",
            notes="Diapositive à photographier. Faire dire la différence à voix haute "
                  "par plusieurs élèves : « un comprimé trois fois » et non « trois "
                  "comprimés une fois ».")

    d.tableau('Analyse · 2', "Comment l'étiquette donne ses ordres",
              ["La forme", "Exemple"],
              [["le verbe en -ez", "Prenez un comprimé."],
               ["ne… pas + verbe en -ez", "Ne prenez pas deux comprimés."],
               ["ne pas + infinitif", "Ne pas donner aux enfants."],
               ["autres verbes utiles", "Agitez. Rincez. Terminez."]],
              cle=0,
              note="Sur les boîtes, « ne pas donner » est la forme la plus fréquente.",
              notes="Diapositive à photographier. Faire remarquer que le verbe est "
                    "toujours en premier : c'est ce qui distingue une consigne d'une "
                    "phrase ordinaire.")

    d.piege('Lecture',
            "« plus de quatre comprimés par jour »",
            "« pas plus de quatre comprimés par jour »",
            "Sans le mot « pas », la phrase dit exactement le contraire de ce qu'elle "
            "veut dire. C'est le mot le plus court de la mise en garde et le plus "
            "important : « pas plus de » fixe un maximum.",
            notes="Écrire les deux au tableau et faire dire à voix haute laquelle "
                  "autorise cinq comprimés. Le contraste fait mieux que l'explication.")

    d.tableau('Analyse · 3', "Les chiffres qui protègent",
              ["L'expression", "Ce qu'elle fixe"],
              [["pas plus de quatre comprimés", "un maximum"],
               ["au moins quatre heures", "un minimum"],
               ["de moins de six ans", "les plus jeunes : interdit"],
               ["de plus de dix-huit ans", "les plus âgés : permis"]],
              cle=0,
              note="Sur une boîte, « 6 ans + » veut dire six ans et plus.",
              notes="Diapositive à photographier. Prendre un cas concret : un enfant de "
                    "cinq ans et un sirop marqué « 6 ans et plus ». Faire trancher le "
                    "groupe.")

    d.pratique('Application · 1', "Combien de fois, et quand ?",
               "Complétez chaque phrase.", [
        ("Prenez un comprimé trois ___ par jour.", "fois"),
        ("Un comprimé deux fois ___ semaine.", "par"),
        ("Prenez ce médicament ___ huit heures.", "aux"),
        ("Ce comprimé se prend ___ les repas, l'estomac plein.", "après"),
        ("Ce sirop se prend ___ les repas, l'estomac vide.", "avant"),
    ], corrige=True,
       notes="Les items de l'exercice interactif `t3frequence`. Corriger à l'oral en "
             "faisant redire la phrase entière, pas seulement le mot manquant.")

    d.pratique('Application · 2', "Écrivez la consigne",
               "Écrivez chaque consigne comme sur une étiquette.", [
        ("Dire de prendre un comprimé.", "« Prenez un comprimé. »"),
        ("Dire de ne pas en prendre deux en même temps.", "« Ne prenez pas deux comprimés en même temps. »"),
        ("Dire d'agiter le sirop avant de l'ouvrir.", "« Agitez avant d'ouvrir. »"),
        ("Dire de ne pas donner aux enfants.", "« Ne pas donner aux enfants. »"),
        ("Dire de terminer les sept jours.", "« Terminez le traitement. »"),
    ], corrige=True,
       notes="Les items de l'exercice `t3imperatif`. Faire écrire au tableau par cinq "
             "élèves différents, puis corriger ensemble.")

    d.pratique('Application · 3', "Les mises en garde",
               "Complétez, puis expliquez ce que ça interdit ou permet.", [
        ("Ne pas donner aux enfants ___ six ans.", "de moins de — un enfant de cinq ans : interdit"),
        ("Ce sirop est pour les adultes ___ dix-huit ans.", "de plus de — dix-neuf ans : permis"),
        ("Prendre ___ quatre comprimés par jour.", "pas plus de — cinq : trop"),
        ("Attendez ___ quatre heures entre deux doses.", "au moins — deux heures : trop tôt"),
    ], corrige=True,
       notes="Les items de l'exercice `t3plusde`. Exiger l'explication après la réponse : "
             "c'est elle qui prouve que la mise en garde est comprise.")

    d.billet(
        "Écrivez la posologie d'un médicament que vous connaissez.",
        exemples=[
            "Combien, combien de fois, quand, pendant combien de jours.",
            "Ajoutez une mise en garde avec « pas plus de » ou « de moins de ».",
        ],
        notes="Devoir de fin de bloc. Il sert directement à la production écrite de la "
              "séance E1 : la note laissée à la personne qui ira à la pharmacie.")

    return d.save(dossier)
