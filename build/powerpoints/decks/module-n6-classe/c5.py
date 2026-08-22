# -*- coding: utf-8 -*-
"""C5 · Le temps qu'on lit, et le passé du passé
Bloc C « Défi 2 » · couleur ambre · 75 min. Grammaire du texte.
Source du module : exercices `t2ps` et `t2avant`, et leurs deux mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C5', section='ambre',
        titre="Le temps qu'on lit, et le passé du passé",
        chapeau="Deux temps de verbe qu'on ne parle jamais et qu'on lit "
                "partout. L'un raconte le décor ; l'autre décide de l'ordre "
                "des faits — et deux dates inversées font dire à un travail "
                "le contraire de sa source.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du défi 2. Les deux temps sont des savoirs "
                  "de compréhension : le programme demande de les "
                  "reconnaître, jamais de les produire. Le dire d'entrée de "
                  "jeu soulage beaucoup de monde.")

    d.objectifs([
        "reconnaître un passé simple et le traduire en passé composé ;",
        "connaître trois formes par cœur : il fut, il eut, il fit ;",
        "reconnaître un plus-que-parfait à son participe passé ;",
        "dire lequel de deux faits passés est arrivé le premier.",
    ], notes="Personne n'aura à écrire un passé simple, ici ni ailleurs. Le "
             "répéter à la fin de la séance : c'est ce que les élèves "
             "retiennent le moins.")

    d.declencheur(
        'Observation', "« Le conseil adopta le règlement. » Qui parle comme ça ?",
        pistes=[
            "Est-ce que vous l'avez déjà entendu à l'oral ?",
            "Où l'avez-vous déjà lu ?",
            "Comment le diriez-vous, vous ?",
        ],
        notes="Personne ne l'a entendu à l'oral, et c'est la bonne réponse. "
              "Le rendre rassurant tout de suite : ce temps ne se produit "
              "pas, il se lit.")

    d.tableau('Analyse', "Trois séries de terminaisons",
              ['La série', 'Les formes'],
              [["-a et -èrent", "il adopta, ils adoptèrent"],
               ["-it et -irent", "elle partit, elles partirent"],
               ["-ut et -urent", "il disparut, ils disparurent"],
               ["les trois par cœur", "il fut, il eut, il fit"]],
              cle=0,
              note="« Il choisit » s'écrit pareil au présent : c'est le récit autour qui tranche.",
              notes="Diapositive à photographier. Les trois formes de la "
                    "dernière ligne suffisent à comprendre la moitié des "
                    "textes historiques.")

    d.regle("On le traduit dans sa tête, et on continue",
            "Dans un document, le passé simple porte le décor — jamais l'information dont vous avez besoin.",
            precision="Ralentir dessus fait perdre le fil du paragraphe, et "
                      "c'est le seul dommage réel qu'il puisse causer.",
            notes="Diapositive à photographier. Faire lire un paragraphe du "
                  "bulletin municipal à voix haute, en traduisant au vol : "
                  "l'exercice est plus facile qu'il n'en a l'air.")

    d.pratique('Pratique', "Comment le dirait-on ?",
               "Traduisez chaque forme écrite en passé composé.", [
        ("le conseil adopta le règlement", "le conseil a adopté le règlement"),
        ("les premiers bacs arrivèrent en avril", "les premiers bacs sont arrivés en avril"),
        ("la collecte ne commença qu'en juin", "la collecte n'a commencé qu'en juin"),
        ("il y eut deux années difficiles", "il y a eu deux années difficiles"),
        ("les plaintes disparurent peu à peu", "les plaintes ont disparu peu à peu"),
        ("on installa un point de dépôt", "on a installé un point de dépôt"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `t2ps` du module. Le faire à l'oral, en "
             "chaîne : chacun traduit une forme, sans écrire.")

    d.regle("Avait ou était, plus un participe : le fait est arrivé avant",
            "La ville avait distribué les bacs quand la collecte commença. — Les bacs d'abord.",
            precision="« Il avait un bac » est un imparfait : un état. « Il "
                      "avait reçu un bac » est un plus-que-parfait : un fait "
                      "antérieur. Un mot de plus, et le sens change.",
            notes="Diapositive à photographier. Le contraste imparfait / "
                  "plus-que-parfait est le point le plus utile de la "
                  "deuxième moitié de la séance.")

    d.piege('Lecture',
            "se fier au mot de liaison pour connaître l'ordre",
            "se fier au temps du verbe",
            "« Parce que », « quand », « mais » ne disent rien de l'ordre des "
            "faits. « Ils se plaignirent parce que personne ne leur avait "
            "expliqué la règle » : c'est le plus-que-parfait, et lui seul, "
            "qui place l'explication manquante avant la plainte.",
            notes="Faire tracer la ligne de temps au tableau : deux points, "
                  "une flèche. Trente secondes, et c'est la vérification la "
                  "moins chère de tout le travail.")

    d.pratique('Pratique', "Lequel est arrivé le premier ?",
               "Le fait souligné est-il arrivé avant l'autre, ou après ?", [
        ("La ville avait distribué les bacs quand la collecte commença.", "avant"),
        ("Le conseil adopta le règlement, puis il fit imprimer le dépliant.", "après"),
        ("Quand Milagros trouva la page, Youssef avait déjà lu l'article.", "avant"),
        ("L'équipe remit son plan, et l'enseignante le corrigea le soir même.", "après"),
        ("Ils se plaignirent parce que personne ne leur avait expliqué la règle.", "avant"),
        ("La lectrice écrivit parce qu'elle avait vu un sac de plastique.", "avant"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `t2avant` du module. Terminer sur la première "
             "phrase : les gens ont eu un bac vide pendant deux mois, et "
             "c'est ce détail-là qui fait un bon travail de recherche.")

    d.billet(
        "Écris deux faits de ton sujet, dans l'ordre où ils sont arrivés.",
        exemples=[
            "Emploie « avait » plus un participe pour celui qui est arrivé avant.",
            "Exemple : « La ville avait distribué les bacs quand la collecte a commencé. »",
        ],
        notes="Trois minutes. Vérifier surtout la ligne de temps, pas la "
              "forme du verbe : c'est l'ordre qui compte pour le travail.")

    return d.save(dossier)
