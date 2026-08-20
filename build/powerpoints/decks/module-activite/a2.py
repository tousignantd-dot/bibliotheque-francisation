# -*- coding: utf-8 -*-
"""A2 · Entendre les chiffres.
Bloc A « Je découvre » · couleur teal · 75 min.
Source : mini-leçon `prTarif`, exercices `prChiffres` et `prTarif`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='teal',
        titre='Entendre les chiffres',
        chapeau="On comprend toute la conversation, et puis arrive le montant. "
                "« Quatre-vingt-quinze » ou « quatre-vingt-cinq » ? Une syllabe "
                "sépare dix dollars.",
        duree='75 minutes')

    d.titre(notes="Séance d'écoute. Prévoir le son. Commencer en dictant trois montants et "
                  "en faisant écrire : l'écart entre les réponses est saisissant.")

    d.objectifs([
        "reconnaître 70, 80 et 90 à l'oral ;",
        "ne pas confondre soixante et soixante-quinze, cinq et quinze ;",
        "convertir une heure officielle en heure parlée ;",
        "faire répéter un montant sans gêne.",
    ])

    d.tableau('Analyse', "Les trois dizaines difficiles",
              ['Le nombre', 'Comment il se dit'],
              [["70", "soixante-dix"],
               ["80", "quatre-vingts"],
               ["90", "quatre-vingt-dix"],
               ["Le reste", "régulier : vingt, trente, quarante, cinquante, cent"]],
              cle=3,
              note="Trois nombres seulement font vraiment hésiter — et ce sont ceux des tarifs.",
              notes="Diapo centrale. Faire recopier. La quatrième ligne rassure : le reste "
                    "ne pose pas de problème.")

    d.regle('Le piège de soixante',
            "« Soixante » et « soixante-dix » commencent exactement pareil.",
            precision="Il faut attendre la fin du mot. S'il y a un deuxième nombre après "
                      "« soixante », c'est 70 et plus. Le même piège existe entre "
                      "« quatre-vingts » et « quatre-vingt-dix ».",
            notes="Faire l'expérience : dire « soixante… » puis marquer une pause de deux "
                  "secondes avant « quinze ». Le groupe comprend immédiatement.")

    d.regle('Cinq ou quinze',
            "Dix dollars d'écart, une syllabe de différence.",
            precision="« Quatre-vingt-cinq » et « quatre-vingt-quinze » sont l'erreur la "
                      "plus fréquente sur les prix. La seule parade est de faire répéter : "
                      "« quatre-vingt-cinq, c'est bien ça ? »",
            notes="Faire répéter cette question par tout le groupe, deux fois. C'est une "
                  "phrase de six mots qui évite des malentendus coûteux.")

    d.tableau('Les heures', "Écrit et parlé",
              ['Sur le dépliant', 'Ce que les gens disent'],
              [["9 h", "neuf heures"],
               ["13 h", "une heure"],
               ["19 h", "sept heures du soir"],
               ["21 h", "neuf heures du soir"]],
              cle=2,
              note="Les deux formes sont correctes. C'est la même heure.",
              notes="Faire calculer à voix haute : 19 moins 12 égale 7. Le calcul devient "
                    "automatique après une dizaine de fois.")

    d.piege('Noter avant la fin du mot',
            "— Soixante… — J'écris 60. — …quinze dollars.",
            "J'attends la fin, puis j'écris 75.",
            "Le nombre n'est pas fini tant que la personne parle. Écrire trop tôt donne un "
            "montant faux, et on ne s'en aperçoit qu'à la caisse. Attendez, puis répétez.",
            notes="Faire l'exercice en dictée lente, avec des pauses au milieu des nombres.")

    d.pratique('Pratique · 1 de 2', "Quel montant ?",
               "Écoutez et écrivez le nombre en chiffres.", [
        ("Quatre-vingt-cinq dollars.", "85 $"),
        ("Quatre-vingt-quinze dollars.", "95 $"),
        ("Soixante-quinze dollars.", "75 $"),
        ("Cent dix dollars.", "110 $"),
        ("Soixante dollars.", "60 $"),
        ("Quatre-vingt-dix dollars.", "90 $"),
    ], corrige=True,
       notes="Utiliser l'exercice 2 du module pour l'écoute. Deux passages avant de "
             "corriger. Les élèves peuvent le refaire seuls.")

    d.pratique('Pratique · 2 de 2', "Quelle heure ?",
               "Traduisez l'heure officielle en heure parlée.", [
        ("9 h", "neuf heures du matin"),
        ("13 h", "une heure de l'après-midi"),
        ("17 h 30", "cinq heures et demie"),
        ("19 h", "sept heures du soir"),
        ("21 h", "neuf heures du soir"),
    ], corrige=True, cols=1,
       notes="Faire faire le calcul à voix haute. Après cinq fois, la conversion devient "
             "automatique.")

    d.cartes('Les chiffres du module', "Ceux qu'il faut avoir entendus", [
        ("Le tarif",
         "85 $ pour les résidents, 110 $ pour les autres. Vingt-cinq dollars d'écart : "
         "c'est ce qui rend la preuve de résidence intéressante."),
        ("L'horaire",
         "Le cours de natation : 9 h à 10 h, le samedi. La chorale : 19 h à 21 h, le "
         "jeudi."),
        ("La durée",
         "Douze semaines pour la natation, dix pour la chorale. C'est le troisième chiffre "
         "du dépliant."),
    ], notes="Ces chiffres reviendront dans tous les blocs. Les écrire au tableau et les y "
             "laisser jusqu'à la fin du module.")

    d.billet(
        "Trouvez le tarif d'une activité de votre ville et notez-le en toutes lettres.",
        exemples=[
            "Sur le site de la ville, sur un dépliant, ou en téléphonant.",
            "Écrivez aussi l'horaire, en heures officielles et en heures parlées.",
        ],
        notes="Devoir court et concret. Les relevés servent d'exemples réels aux séances "
              "suivantes.")

    return d.save(dossier)
