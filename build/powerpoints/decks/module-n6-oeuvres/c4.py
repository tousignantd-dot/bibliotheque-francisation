# -*- coding: utf-8 -*-
"""C4 · « Où », et les petits mots qui renvoient en arrière
Bloc C « Défi 2 · La biographie de la réalisatrice » · couleur ambre · 75 min.
Bilan du bloc. Source : exercices `t2ou` et `t2repr`, et leurs mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre="« Où », et les petits mots qui renvoient en arrière",
        chapeau="Une biographie de dix lignes contient six mots de deux "
                "lettres. Perdre le fil, ce n'est pas manquer un mot : c'est "
                "perdre à quoi il renvoie.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du Défi 2, et le cœur du niveau 6. Si une seule "
                  "séance du module devait être gardée, ce serait celle-ci : la "
                  "cohésion est ce qui sépare le niveau 6 des niveaux 3 et 5.")

    d.objectifs([
        "réunir deux phrases avec « où », pour un lieu ou pour un moment ;",
        "retrouver à quoi renvoient « le », « en » et « y » ;",
        "reprendre un mot sans le répéter, par un synonyme ;",
        "ne plus écrire « le jour que » à la place de « le jour où ».",
    ], notes="Le quatrième objectif est une faute précise et très fréquente au "
             "niveau 6. Elle se corrige en une séance et ne revient plus.")

    d.declencheur(
        'Observation', "Ces petits mots renvoient à quoi ?",
        pistes=[
            "« Elle y resta onze ans. » - où ?",
            "« Elle y vint, et elle refusa de parler. » - où ?",
            "« Elle n'en parle qu'à ses étudiants. » - de quoi ?",
            "Chaque fois, il faut reculer d'une phrase. Essayons.",
        ],
        notes="Faire chercher sur la feuille verte, doigt sur la ligne. Le geste de "
              "reculer d'une phrase est la vraie compétence : le faire faire "
              "physiquement.")

    d.tableau('Analyse', "Trois pronoms, trois emplois",
              ['Le pronom', 'Ce qu\'il remplace'],
              [["le", "toute une idée : qu'elle a appris son métier au montage"],
               ["en", "un groupe avec « de » : de son premier court métrage"],
               ["y", "un lieu, ou un groupe avec « à » : à la salle Beauchemin"],
               ["le geste", "reculer d'une phrase, jamais plus loin"]],
              cle=0,
              note="Si le référent n'est pas dans la phrase d'avant, c'est le texte qui est mal écrit.",
              notes="Diapositive à photographier. La note déculpabilise, et elle est "
                    "vraie : un texte bien écrit ne fait jamais reculer de trois "
                    "phrases.")

    d.regle("« Où » fait deux métiers",
            "Il remplace un complément de lieu, ou un complément de temps.",
            precision="« Sherbrooke, où il avait été présenté en premier » parle d'une "
                      "ville. « L'année où elle cessa de tourner » parle d'un moment. "
                      "C'est le même mot, écrit pareil. Ce qui les distingue est le "
                      "mot juste avant : une ville, une salle, une maison pour le "
                      "lieu ; une année, un jour, un moment pour le temps.",
            notes="Diapositive à photographier. Faire chercher les deux emplois dans "
                  "la feuille verte : ils y sont tous les deux.")

    d.regle("Jamais « le jour que »",
            "Avec un mot de temps, c'est « où », et rien d'autre.",
            precision="« Le jour que je suis arrivée » est la faute la plus fréquente "
                      "du niveau 6, et elle vient d'une bonne logique : « que » "
                      "fonctionne partout ailleurs. Ici, non. Le jour où, l'année où, "
                      "le moment où, l'époque où.",
            notes="Diapositive à photographier. Faire répéter les quatre groupes en "
                  "chœur : c'est un automatisme de rythme, pas une règle à "
                  "comprendre.")

    d.pratique('Grammaire', "Réunissez les deux phrases avec « où »",
               "Écrivez une seule phrase.", [
        ("Elle est née dans une famille. Personne n'y allait au cinéma.", "une famille où personne n'allait au cinéma"),
        ("Elle est entrée dans une salle. Elle y a appris son métier.", "la salle où elle a appris son métier"),
        ("Le film est sorti en 1994. Cette année-là...", "1994, l'année où le film est sorti"),
        ("Estelle revient au village. Elle avait grandi là.", "le village où elle avait grandi"),
        ("L'autobus est tombé en panne ce jour-là.", "le jour où l'autobus est tombé en panne"),
        ("Tu viens mercredi ... jeudi, comme tu veux.", "ou, sans accent"),
    ], corrige=True, cols=2,
       notes="Le dernier item est le seul sans accent. Le garder pour la fin : il "
             "montre que « ou » et « où » n'ont aucun rapport entre eux.")

    d.pratique('Grammaire', "Remplacez par le, en ou y",
               "Récrivez la deuxième phrase avec le bon pronom.", [
        ("Une rétrospective eut lieu à la salle. Elle est venue à la salle.", "elle y est venue"),
        ("Elle a appris son métier au montage. Elle répète cela partout.", "elle le répète partout"),
        ("Elle parle rarement de son court métrage. Elle en parle à ses étudiants.", "elle n'en parle qu'à ses étudiants"),
        ("Le film compte quatre retours en arrière. Bruno a compté quatre retours.", "Bruno en a compté quatre"),
        ("Personne ne sait pourquoi elle a cessé. Personne ne sait cela.", "personne ne le sait"),
        ("Elle a besoin de silence. Elle a toujours eu besoin de silence.", "elle en a toujours eu besoin"),
    ], corrige=True, cols=2,
       notes="Les items 2 et 5 emploient « le » pour une idée entière : c'est le plus "
             "difficile des trois pronoms. Les corriger ensemble.")

    d.cartes("Reprendre sans répéter", "L'autre façon d'éviter la répétition", [
        ("Par un synonyme",
         "le film, l'œuvre, ce long métrage."),
        ("Par un mot plus général",
         "« Les Marées de novembre », ce film, cette histoire."),
        ("Par une nominalisation",
         "elle a cessé de tourner : cet arrêt, cette décision."),
        ("Deux fois, pas trois",
         "à la troisième reprise, le lecteur ne sait plus de quoi on parle."),
    ], notes="Quatre gestes, à copier dans le cahier. Le quatrième est celui qui "
             "manque le plus souvent : trop de synonymes brouille autant que trop de "
             "répétitions.")

    d.billet(
        "Écris une phrase avec « où », et une avec « le », « en » ou « y ».",
        exemples=[
            "Deux phrases, courtes.",
            "Dis ce que le pronom remplace, entre parenthèses.",
        ],
        notes="Trois minutes. Les billets qui ne disent pas ce que le pronom remplace "
              "signalent exactement les élèves à reprendre avant le Défi 3.")

    return d.save(dossier)
