# -*- coding: utf-8 -*-
"""A2 · Le « é » fermé et le « è » ouvert.
Bloc A · couleur indigo (graphie-phonie) · 60 min.
Source : exercices `prPhon` et `prAccent`.

Le module affiche ces sons en alphabet phonétique. Pas ici : Verdana ne
possède aucun caractère de l'API. On nomme donc les deux sons par leur
accent — « é » fermé, « è » ouvert — ce que l'élève peut réécrire lui-même.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Le « é » fermé et le « è » ouvert",
        chapeau="« Dépanner » et « dépanné » s'écrivent presque pareil et se prononcent "
                "pareil. « Père » et « dépanné », non. Un accent, deux sons, et une "
                "règle qui tient à la place dans le mot.",
        duree='60 minutes')

    d.titre(notes="Écrire au tableau « père » et « dépanné ». Faire dire les deux mots "
                  "par cinq élèves et demander si la voyelle est la même. Les avis "
                  "seront partagés : c'est le point de départ.")

    d.objectifs([
        "entendre la différence entre le « é » fermé et le « è » ouvert ;",
        "savoir quelles lettres écrivent chacun des deux ;",
        "connaître la règle de la fin de mot ;",
        "écrire correctement les mots du module.",
    ])

    d.regle('La règle de place',
            "À la fin d'un mot, c'est presque toujours le « é » fermé.",
            precision="Dépanné, travailler, j'aimerais, dépanner : tous se terminent par "
                      "le son « é ». Au milieu d'un mot, devant deux consonnes ou "
                      "devant l ou r prononcés, c'est le « è » ouvert : père, nouvelle, "
                      "hiver.",
            notes="Écrire la règle au tableau. Elle a des exceptions, mais elle explique "
                  "la grande majorité des cas — et surtout les mots du module.")

    d.tableau('Analyse', "Deux sons, leurs lettres, un mot repère",
              ['Le son', "Il s'écrit", 'Mot repère'],
              [["le « é » fermé", "é, er, ez, ai en finale", "dépanné"],
               ["le « è » ouvert", "è, ê, ei, ai + consonne, e + l, e + r", "père"]],
              cle=0,
              note="Le « é » fermé : la bouche presque fermée, un son court et net. Le "
                   "« è » ouvert : la bouche plus ouverte, un son plus long.",
              notes="Faire dire les deux mots repères en alternance, en exagérant "
                    "l'ouverture de la bouche. Dix allers-retours.")

    d.cartes('La bouche', "Comment les distinguer", [
        ("Le « é » fermé",
         "La bouche est presque fermée, les lèvres étirées comme pour un sourire. Le "
         "son est court. Comme dans dépanné, travailler, j'aimerais."),
        ("Le « è » ouvert",
         "La bouche s'ouvre davantage, la mâchoire descend. Le son est plus long. "
         "Comme dans père, tête, treize, semaine."),
        ("Le test de la main",
         "Placez la main sous le menton. Pour « è », la mâchoire descend et pousse la "
         "main. Pour « é », elle ne bouge presque pas."),
        ("Les deux dans un mot",
         "« Répète » contient les deux : « ré » fermé, « pè » ouvert. C'est le "
         "meilleur exercice de la séance."),
    ], notes="Faire faire le test de la main par tout le groupe en même temps. C'est le "
             "seul critère qui ne demande pas d'oreille exercée.")

    d.tableau('Analyse', "Les lettres qui donnent le « è » ouvert",
              ['Les lettres', 'Exemple'],
              [["è", "père, très"],
               ["ê", "tête, être"],
               ["ei", "treize, seize"],
               ["ai + consonne", "semaine, aime"],
               ["e + l ou e + r prononcé", "nouvelle, hiver"]],
              cle=0,
              note="La dernière ligne explique « hiver » et « mer », qui font exception à "
                   "la règle du « er » final.",
              notes="« Hiver » et « mer » sont les deux exceptions à retenir. Les faire "
                    "écrire au tableau, entourées.")

    d.pratique('Pratique · 1 de 3', "Quel son entendez-vous ?",
               "Écoutez le mot, écrivez « é fermé » ou « è ouvert ».", [
        ("père", "è ouvert"),
        ("travaillerai", "é fermé"),
        ("nouvelle", "è ouvert"),
        ("dépanné", "é fermé"),
        ("semaine", "è ouvert"),
        ("hiver", "è ouvert — exception"),
        ("dépanner", "é fermé"),
        ("treize", "è ouvert"),
    ], corrige=True, cols=2,
       notes="Dire chaque mot deux fois, sans le montrer. « Hiver » est l'exception : "
             "le garder pour la fin de la correction.")

    d.piege("Le piège de « dépanner » et « dépanné »",
            "On les prononce différemment.",
            "Ils se prononcent exactement pareil.",
            "L'infinitif « dépanner » et le participe « dépanné » ont le même son final : "
            "le « é » fermé. À l'oral, rien ne les distingue. C'est le contexte qui "
            "décide, et à l'écrit, la grammaire.",
            notes="Cette confusion cause l'erreur d'orthographe la plus fréquente du "
                  "français écrit. Le signaler ici, sans encore donner la règle du "
                  "choix : elle viendra plus tard.")

    d.piege("Le piège de « hiver »",
            "hi-vé",
            "hi-vèr — le r se prononce",
            "La finale « -er » donne presque toujours le « é » fermé : travailler, "
            "manger, dépanner. Mais dans « hiver » et « mer », le r se prononce, et la "
            "voyelle devient un « è » ouvert. Ce sont deux mots à retenir, pas une "
            "règle.",
            notes="Faire dire « hiver » dix fois. Le mot revient tout l'hiver dans les "
                  "conversations sur les retards : il vaut la peine d'être juste.")

    d.pratique('Pratique · 2 de 3', "Complétez avec é, è, ê, ei ou ai",
               "Un seul groupe de lettres par trou.", [
        ("le p___re (le parent)", "père — è"),
        ("la sem___ne (sept jours)", "semaine — ai"),
        ("la nouv___lle (l'information)", "nouvelle — e devant deux l"),
        ("d___pann___ (le participe passé)", "dépanné — é deux fois"),
        ("l'hiv___r (la saison froide)", "hiver — e devant r prononcé"),
        ("tr___ze (le nombre)", "treize — ei"),
    ], corrige=True,
       notes="Ici on va du son vers l'écriture : c'est le sens le plus difficile. "
             "Laisser trois minutes de recherche.")

    d.pratique('Pratique · 3 de 3', "Trois phrases à lire à voix haute",
               "Le groupe corrige uniquement les « é » et les « è ».", [
        ("Mon père travaille dehors même en hiver.", "è · é · è"),
        ("J'aimerais être dépanné cette semaine.", "é · è · é · è"),
        ("La nouvelle grille horaire commence en janvier.", "è · è · é"),
    ], corrige=True,
       notes="Faire lire debout et lentement. La deuxième phrase contient les deux sons "
             "en alternance : c'est le vrai test.")

    d.billet(
        "Écrivez quatre mots du module : deux avec le « é » fermé, deux avec le « è » ouvert.",
        exemples=[
            "Soulignez la lettre ou le groupe de lettres qui fait le son.",
            "Exemple : « père » — le « è » ouvert, lettre è.",
        ],
        notes="Corriger en circulant. Un élève qui place « hiver » dans la colonne du "
              "« é » n'a pas retenu l'exception : le reprendre individuellement.")

    return d.save(dossier)
