# -*- coding: utf-8 -*-
"""A2 · Trois sons dans le nez.
Bloc A · couleur indigo (graphie-phonie) · 60 min.
Source : exercice `prPhon` et sa mini-leçon.

Le module affiche les sons en alphabet phonétique. **Pas ici** : Verdana ne
possède aucun caractère de l'API, et un `.pptx` livré avec eux afficherait des
carrés vides chez l'enseignant. On nomme donc chaque son par ses lettres les
plus fréquentes — le son « an », le son « on », le son « in » — et par un mot
repère d'une syllabe. C'est aussi la notation que l'élève peut réécrire.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre='Trois sons dans le nez',
        chapeau="« Patient », « front », « médecin » : trois mots de la salle d'attente, "
                "trois sons nasaux différents. Les confondre change le mot — et "
                "l'orthographe ne prévient pas.",
        duree='60 minutes')

    d.titre(notes="Séance de graphie-phonie. Commencer bouche fermée : dire les trois "
                  "mots sans les écrire et demander au groupe s'il entend une différence. "
                  "Beaucoup répondront non — c'est le point de départ.")

    d.objectifs([
        "entendre la différence entre le son « an », le son « on » et le son « in » ;",
        "savoir quelles lettres écrivent chacun des trois ;",
        "prononcer correctement les mots du module qui les contiennent ;",
        "reconnaître les finales trompeuses comme « examen ».",
    ], notes="Les trois sons sont nommés par leurs lettres, pas par des symboles "
             "phonétiques : c'est une notation que l'élève peut réécrire lui-même.")

    d.regle('Le point de départ',
            "Une voyelle suivie de n ou de m se prononce dans le nez.",
            precision="Le français a trois sons nasaux principaux. Ils ne s'écrivent pas "
                      "comme ils se disent : il faut donc les apprendre par l'oreille "
                      "avant de les apprendre par les yeux.",
            notes="Faire poser un doigt sur le nez pendant qu'on dit « dent » puis "
                  "« dais » : la vibration se sent au premier mot, pas au second.")

    d.tableau('Analyse', "Les trois sons, leurs lettres, un mot repère",
              ['Le son', "Il s'écrit", 'Mot repère'],
              [["le son « an »", "an, am, en, em", "dent"],
               ["le son « on »", "on, om", "front"],
               ["le son « in »", "in, im, ain, ein", "main"]],
              cle=0,
              note="Trois mots repères d'une syllabe : dent, front, main. À apprendre "
                   "par cœur — ils servent de mesure pour tous les autres.",
              notes="Écrire les trois mots repères au tableau et les y laisser toute la "
                    "séance. Chaque fois qu'un élève hésite, on revient à eux.")

    d.cartes('La bouche', "Comment la bouche fabrique chacun des trois", [
        ("Le son « an » — la bouche ouverte",
         "La bouche s'ouvre grand et les lèvres restent plates. Le son part du fond. "
         "Comme dans dent, jambe, temps, patient."),
        ("Le son « on » — les lèvres arrondies",
         "Les lèvres se ferment en cercle, comme pour dire « oh ». Comme dans front, "
         "nom, tendon, consultation."),
        ("Le son « in » — la bouche presque fermée",
         "C'est le plus aigu des trois. La bouche s'ouvre à peine. Comme dans main, "
         "médecin, examen."),
        ("Le test du miroir",
         "Si les lèvres s'arrondissent, c'est « on ». Si la bouche s'ouvre sans "
         "s'arrondir, c'est « an ». Si elle reste presque fermée, c'est « in »."),
    ], notes="Faire faire les trois positions en même temps par tout le groupe, sans "
             "son d'abord, puis avec le son. La quatrième carte est le critère à retenir.")

    d.regle('Le mot qui contient deux des trois',
            "Tendon : la première syllabe fait « an », la deuxième fait « on ».",
            precision="Ten-don. Si vous entendez la différence entre les deux syllabes "
                      "de ce mot, vous l'entendrez partout ailleurs. C'est le meilleur "
                      "exercice de la séance, et il tient en un mot.",
            notes="Faire répéter « tendon » dix fois de suite, lentement, en exagérant "
                  "l'arrondissement des lèvres sur la deuxième syllabe.")

    d.pratique('Pratique · 1 de 3', 'Quel son entendez-vous ?',
               "Écoutez le mot, écrivez « an », « on » ou « in ».", [
        ("patient", "le son « an »"),
        ("tendon", "« an » puis « on »"),
        ("jambe", "le son « an »"),
        ("front", "le son « on »"),
        ("temps", "le son « an »"),
        ("nom", "le son « on »"),
        ("dent", "le son « an »"),
        ("consultation", "le son « on »"),
    ], corrige=True, cols=2,
       notes="Dire chaque mot deux fois, sans le montrer. Ne pas laisser le groupe voir "
             "l'orthographe avant d'avoir répondu : c'est un exercice d'oreille.")

    d.tableau('Analyse', "Les mots du module, classés",
              ['Mot', 'Son', 'Lettres'],
              [["patient", "« an »", "en"],
               ["jambe", "« an »", "am"],
               ["médecin", "« in »", "in final"],
               ["examen", "« in »", "en final"],
               ["consultation", "« on »", "on"]],
              cle=1,
              note="« Examen » et « patient » se terminent par les mêmes lettres et ne "
                   "se prononcent pas pareil : c'est le piège de la séance.",
              notes="Faire lire la colonne des lettres à voix haute avant la colonne des "
                    "sons : les élèves verront que l'orthographe ne suffit pas.")

    d.piege('Le piège de « examen »',
            "exa-min",
            "examen — la finale se dit comme « main »",
            "La finale « -en » de « examen » fait le son « in ». Mais la finale « -ent » "
            "de « patient » fait le son « an ». Deux orthographes très proches, deux "
            "sons différents : il faut retenir le mot entier, pas une règle.",
            notes="C'est l'erreur la plus tenace du module. La faire entendre dans une "
                  "phrase : « le patient passe un examen » contient les deux.")

    d.piege('Le piège de « front » et « franc »',
            "franc, quand on veut dire front",
            "front — les lèvres arrondies",
            "« on » et « an » se ressemblent à l'oreille d'un débutant. Le seul critère "
            "fiable est la position des lèvres : arrondies en cercle pour « on », plates "
            "et ouvertes pour « an ». L'oreille suit la bouche, pas l'inverse.",
            notes="Faire dire les deux mots en alternance, en regardant sa propre bouche "
                  "dans un téléphone. Cinq allers-retours suffisent souvent.")

    d.pratique('Pratique · 2 de 3', 'Complétez avec les bonnes lettres',
               "Un seul groupe de lettres par trou : an, en, am, om, on, in ou ain.", [
        ("le méd___ (le professionnel)", "médecin — in"),
        ("le t___d___ (ce qui attache le muscle)", "tendon — en puis on"),
        ("la j___be (au-dessus du genou)", "jambe — am"),
        ("la m___ (au bout du bras)", "main — ain"),
        ("le n___ (comment on s'appelle)", "nom — om"),
        ("la consultati___", "consultation — on"),
    ], corrige=True,
       notes="Ici on passe du son à l'écriture : c'est le sens le plus difficile. "
             "Laisser chercher deux minutes avant de corriger.")

    d.pratique('Pratique · 3 de 3', 'Trois phrases à lire à voix haute',
               "Chacun lit une phrase. Le groupe dit si les sons nasaux sont justes.", [
        ("Le patient attend son examen depuis longtemps.", "an · in · an"),
        ("Le médecin examine le tendon de sa jambe.", "in · an puis on · an"),
        ("On prend son nom à la consultation.", "on · an · on · on"),
    ], corrige=True,
       notes="Faire lire debout et lentement. Le groupe n'a le droit de corriger que les "
             "sons nasaux, rien d'autre — sinon la lecture s'arrête à chaque mot.")

    d.billet(
        "Écrivez trois mots du module : un avec « an », un avec « on », un avec « in ».",
        exemples=[
            "Soulignez les lettres qui font le son nasal dans chaque mot.",
            "Exemple : « dent » — le son « an », lettres « en ».",
        ],
        notes="Corriger rapidement en circulant. Un élève qui écrit trois mots justes a "
              "compris ; celui qui écrit trois fois le même son sera repris en B1.")

    return d.save(dossier)
