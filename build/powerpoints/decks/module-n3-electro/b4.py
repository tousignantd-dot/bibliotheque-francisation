# -*- coding: utf-8 -*-
"""B4 · Du mardi au dimanche.
Bloc B « Défi 1 · Lire la circulaire » · couleur ambre (écriture) · 60 min.
Source : exercice `t1dates`, mini-leçon `t1dates`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre='Du mardi au dimanche',
        chapeau="Un spécial a toujours une fin. Deux dates en bas de page "
                "décident si le déplacement vaut la peine — et le lundi, il "
                "ne la vaut plus.",
        duree='60 minutes')

    d.titre(notes="Séance d'écriture sur les dates. Avoir un calendrier du mois au "
                  "tableau : tout se montre du doigt, et c'est ce qui fait comprendre "
                  "« du… au… » en trente secondes.")

    d.objectifs([
        "comprendre « du mardi au dimanche » et « jusqu'à dimanche » ;",
        "nommer les sept jours dans l'ordre ;",
        "écrire une date à la française : le 9 novembre ;",
        "dire jusqu'à quand un prix est bon.",
    ])

    d.regle("Les deux jours nommés sont compris",
            "« Du mardi 4 au dimanche 9 novembre »",
            precision="Le mardi 4, oui. Le dimanche 9, oui aussi. C'est le "
                      "lundi 10 qui ne compte plus. « Jusqu'à dimanche » veut "
                      "dire exactement la même chose.",
            notes="Diapo à photographier. Montrer les deux dates sur le calendrier du "
                  "tableau et encercler la semaine du spécial.")

    d.tableau('Analyse', "Les sept jours",
              ['Début de semaine', 'Fin de semaine'],
              [["lundi", "vendredi"],
               ["mardi — la circulaire arrive", "samedi — la livraison"],
               ["mercredi", "dimanche — le spécial finit"],
               ["jeudi — la livraison", ""]],
              cle=0,
              note="Les jours ne prennent pas de majuscule en français.",
              notes="Diapo à photographier. Faire dire les sept jours dans l'ordre, puis "
                    "à l'envers : c'est plus difficile et ça installe la série.")

    d.tableau('Analyse', "Écrire une date",
              ['On écrit', 'On dit'],
              [["le 9 novembre", "le neuf novembre"],
               ["du 4 au 9 novembre", "du quatre au neuf novembre"],
               ["samedi 8 novembre", "samedi huit novembre"]],
              cle=0,
              note="Le jour d'abord, le mois ensuite. Jamais « novembre 9 ».",
              notes="L'ordre inverse vient de l'anglais et se voit souvent dans les "
                    "cahiers. Le corriger ici évite qu'il ne s'installe.")

    d.pratique('Écriture', "Complétez",
               "D'après l'encadré et le dialogue.", [
        ("Le spécial commence le mardi 4 et finit le ___ 9 novembre.", "dimanche"),
        ("« Jusqu'à dimanche » veut dire que le lundi, c'est ___ .", "fini"),
        ("Le jour après mercredi est ___ .", "jeudi"),
        ("La circulaire arrive dans la boîte aux lettres le ___ .", "mardi"),
        ("Quand il reste peu d'appareils, on écrit « quantité ___ ».", "limitée"),
    ], corrige=True,
       notes="Faire écrire, puis corriger au tableau. Insister sur l'absence de "
             "majuscule aux jours.")

    d.cartes("Quatre façons de dire la fin", "Ce qu'on lit en bas de page", [
        ("Du 4 au 9 novembre",
         "Les deux dates sont comprises. C'est la forme la plus fréquente."),
        ("Jusqu'à dimanche",
         "La même chose, en plus court. Dimanche oui, lundi non."),
        ("Pendant 3 jours seulement",
         "Il faut alors chercher la date de début : trois jours à partir de quand ?"),
        ("Quantité limitée",
         "La seule mention qui rend la date inutile : le spécial finit quand il n'y en "
         "a plus."),
    ], notes="Faire chercher ces quatre formes dans les circulaires rapportées. Il y en "
             "a toujours au moins deux.")

    d.piege("Mettre le mois avant le jour",
            "novembre 9",
            "le 9 novembre",
            "C'est l'ordre de l'anglais, et il se glisse partout : dans les cahiers, "
            "dans les courriels, sur les formulaires. En français, le jour vient "
            "toujours en premier, à l'écrit comme à l'oral.",
            notes="Le signaler une fois, fermement, puis corriger sans commentaire "
                  "chaque fois qu'il revient.")

    d.pratique('Production', "Dites jusqu'à quand",
               "Regardez la date de fin et répondez à voix haute.", [
        ("Le spécial finit dimanche. On est samedi.", "le prix est encore bon"),
        ("Le spécial finit dimanche. On est lundi.", "c'est fini, le prix est remonté"),
        ("Du 4 au 9 novembre. On est le 9.", "le prix est bon aujourd'hui"),
        ("Quantité limitée. On est le premier jour.", "il faut y aller tôt"),
    ], corrige=True,
       notes="Exercice à l'oral, en paires : l'un lit la situation, l'autre répond. "
             "Inverser à mi-chemin.")

    d.billet(
        "Écrivez trois phrases sur un spécial de votre circulaire.",
        exemples=[
            "« Le spécial dure du mardi 4 au dimanche 9 novembre. »",
            "« Le prix est bon jusqu'à dimanche. »",
        ],
        notes="Devoir d'écriture. Ramasser : c'est la dernière trace écrite du défi 1.")

    return d.save(dossier)
