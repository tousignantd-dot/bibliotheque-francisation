# -*- coding: utf-8 -*-
"""A2 · « an » ou « on » ?
Bloc A « Je découvre » · couleur indigo · 60 min. Graphie-phonie.
Source : exercice `prNasales`, mini-leçon du même nom.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="« an » ou « on » ?",
        chapeau="Le vocabulaire du travail est plein de sons nasaux : "
                "expérience, formation, permanent, fonction, promotion. Deux "
                "sons y reviennent sans arrêt, et l'oreille doit les séparer.",
        duree='60 minutes')

    d.titre(notes="Séance de prononciation. Elle ne rend pas la parole parfaite : elle "
                  "rend l'écoute moins fatigante pour l'interlocuteur, ce qui compte "
                  "beaucoup dans une entrevue de vingt minutes.")

    d.objectifs([
        "entendre la différence entre le son AN et le son ON ;",
        "produire les deux sons en plaçant correctement les lèvres ;",
        "appliquer la règle des mots en -tion et en -ment ;",
        "prononcer sans détacher le « n » qui suit la voyelle.",
    ])

    d.declencheur(
        'Écoute', "Formation, ou « formatian » ?",
        pistes=[
            "Dites « formation » à voix haute.",
            "Vos lèvres bougent-elles ?",
            "Maintenant dites « permanent ».",
            "Est-ce le même son ?",
        ],
        notes="Faire dire les deux mots à trois ou quatre élèves. La différence "
              "s'entend tout de suite dans le groupe, et c'est ce qui rend la séance "
              "utile plutôt que théorique.")

    d.regle("Un son nasal",
            "L'air passe par le nez, et la lettre « n » ne se prononce pas.",
            precision="Dans « permanent », on n'entend aucun « n » détaché. La lettre "
                      "indique seulement que le son passe par le nez. Posez deux doigts "
                      "sur votre nez et dites « on » : ça vibre. C'est le test.",
            notes="Diapositive à photographier. Le test des deux doigts marche avec "
                  "tout le monde et ne demande aucun métalangage.")

    d.tableau('Anatomie', "Deux sons, deux positions de bouche",
              ['Le son', 'Comment on le fait'],
              [["le son AN  ·  an, en, am, em",
                "La bouche s'ouvre franchement, comme pour dire « ah ». Les lèvres ne bougent pas."],
               ["le son ON  ·  on, om",
                "Les lèvres s'arrondissent, comme pour souffler une bougie."],
               ["Le test qui ne rate pas",
                "Si vos lèvres ne bougent pas, vous dites AN, quoi que vous croyiez."]],
              cle=0,
              note="Un miroir de poche vaut mieux qu'une explication : on voit ses propres lèvres.",
              notes="Si des miroirs sont disponibles, les distribuer. Sinon, faire "
                    "travailler par deux, chacun regardant les lèvres de l'autre.")

    d.cartes("Le repère qui règle presque tout", "Deux terminaisons, deux sons", [
        ("Les mots en -tion et -sion  ·  le son ON",
         "formation, fonction, production, promotion, décision, profession. Sans exception."),
        ("Les mots en -ment et -ent  ·  le son AN",
         "remplacement, département, permanent, compétent, souvent."),
        ("« em » et « am » sont aussi AN",
         "Devant un b ou un p, on écrit em ou am, mais le son ne change pas : emploi, employeur."),
        ("Et ces mots sont partout",
         "Une offre d'emploi ordinaire en contient une dizaine. La règle sert tous les jours."),
    ], notes="Les noms en -tion sont tous féminins : la formation, la fonction. C'est une "
             "des rares règles sans exception du français. En profiter.")

    d.pratique('Discrimination', "Quel son entendez-vous ?",
               "L'enseignante lit le mot. Le groupe répond « an » ou « on ».", [
        ("expérience", "le son AN"),
        ("formation", "le son ON"),
        ("permanent", "le son AN — deux fois"),
        ("fonction", "le son ON — deux fois"),
        ("entrepôt", "le son AN"),
        ("promotion", "le son ON"),
        ("remplacement", "le son AN"),
        ("employeur", "le son AN — em se dit comme an"),
    ], corrige=True, cols=2,
       notes="Lire une première fois à débit normal, une seconde fois lentement. Ne pas "
             "exagérer l'articulation : un employeur ne le fera pas.")

    d.pratique('Production', "Six paires à répéter",
               "Le premier mot est AN, le second ON. Répétez chaque paire deux fois.", [
        ("l'expérience et la formation", "AN puis ON"),
        ("un poste permanent et une promotion", "AN puis ON"),
        ("l'entrepôt et la production", "AN puis ON"),
        ("un remplacement et une fonction", "AN puis ON"),
        ("un employé compétent", "deux fois AN"),
        ("une bonne recommandation", "ON, ON, puis le son AN et le son ON"),
    ], corrige=True,
       notes="La dernière paire est difficile et c'est voulu : « recommandation » "
             "contient les deux sons. La garder pour la fin, et la faire dire par le "
             "groupe entier plutôt que par une seule personne.")

    d.piege("Dire « formatian »",
            "Ma formatian est en logistique.",
            "Ma formation est en logistique.",
            "C'est l'erreur la plus fréquente, et la plus facile à corriger : tous les "
            "mots en -tion finissent par ON, lèvres arrondies. Un seul mot corrigé "
            "règle du coup une trentaine d'autres, parce qu'ils suivent tous la même "
            "terminaison.",
            notes="Corriger ce mot-là en priorité. Il revient dans chaque entrevue, chaque "
                  "formulaire et chaque lettre du module.")

    d.billet(
        "Enregistrez-vous en disant cinq mots de votre métier.",
        exemples=[
            "Écoutez-vous : vos lèvres s'arrondissent-elles sur les mots en -tion ?",
            "Recommencez jusqu'à ce que la différence s'entende.",
        ],
        notes="Le module a un enregistreur dans « Je me lance » : montrer où il se trouve "
              "pour que le devoir puisse se faire à la maison.")

    return d.save(dossier)
