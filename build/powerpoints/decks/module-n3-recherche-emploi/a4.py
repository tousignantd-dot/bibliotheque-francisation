# -*- coding: utf-8 -*-
"""A4 · Les quatre choses qu'on dit en entrant.
Bloc A « Je découvre » · couleur ambre · 75 min. Écriture et préparation.
Source du module : exercice `prQuatre` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="Les quatre choses qu'on dit en entrant",
        chapeau="Pourquoi je viens, ce que je sais faire, quand je suis "
                "libre, où on me joint. Quatre renseignements, toujours les "
                "mêmes, toujours dans le même ordre. Trente secondes.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc A. Elle prépare tout le défi 1 : à la fin, "
                  "chacun doit avoir ses quatre phrases écrites sur un papier qu'il "
                  "garde dans sa poche.")

    d.objectifs([
        "connaître les quatre renseignements à donner ;",
        "écrire ses propres quatre phrases ;",
        "dire son nom et l'épeler ;",
        "donner un numéro de téléphone chiffre par chiffre.",
    ])

    d.declencheur(
        'Mise en situation', "Vous entrez. La personne lève les yeux. Vous dites quoi ?",
        pistes=[
            "Quelle est la toute première phrase ?",
            "Combien de temps avez-vous, à votre avis ?",
            "Qu'est-ce qui est le plus difficile à dire ?",
            "Qu'est-ce qu'on oublie toujours de laisser ?",
        ],
        notes="Faire jouer la scène une fois, sans préparation, avec un volontaire. "
              "Le silence qui suit « Bonjour » est ce que la séance vient combler.")

    d.tableau('Analyse', "Les quatre renseignements, dans l'ordre",
              ['Ce qu\'on donne', 'La phrase'],
              [["1. Pourquoi je viens", "J'ai vu votre affiche dans la vitrine."],
               ["2. Ce que je sais faire", "Je sais faire le ménage."],
               ["3. Quand je suis libre", "Je suis libre du lundi au vendredi, le matin."],
               ["4. Où on me joint", "Vous pouvez me joindre au 438 555-0192."]],
              cle=0,
              note="Quatre phrases. Apprises par cœur, elles servent dans tous les commerces.",
              notes="Diapo à photographier, la plus importante du bloc A. Faire recopier "
                    "à la main : ce qui est écrit de sa main se retient autrement.")

    d.regle("Des jours et des heures, jamais « n'importe quand »",
            "Je suis libre du lundi au vendredi, de 8 h à 13 h.",
            precision="Le patron ne vous écoute pas : il remplit un tableau. Chaque mot "
                      "que vous dites doit pouvoir entrer dans une case. « Je suis "
                      "disponible n'importe quand » sonne bien et ne remplit rien.",
            notes="Diapo à photographier. Demander à trois élèves de dire leurs "
                  "disponibilités réelles à voix haute, et corriger la forme.")

    d.cartes("Dire son nom et son numéro", "Deux gestes qui se ratent souvent", [
        ("Épeler son nom",
         "Traoré : T-R-A-O-R-É. On épelle lentement, une lettre à la fois, et on "
         "s'arrête si la personne écrit. Un nom mal noté, c'est un rappel qui n'arrive pas."),
        ("Les lettres qui se confondent",
         "B et P, D et T, M et N, G et J. Quand l'une d'elles est dans votre nom, "
         "ajoutez un mot : « B comme bateau »."),
        ("Donner son numéro",
         "438, 555, 0192 : par groupes, pas d'un trait. On laisse le temps d'écrire "
         "entre les groupes."),
        ("Le geste qui change tout",
         "« Je peux vous l'écrire ? » Un numéro dit à l'oral se perd. Écrit de votre "
         "main, il reste sur le comptoir."),
    ], notes="Faire épeler son propre nom à chaque élève, debout, à voix haute. "
             "C'est l'exercice le plus utile de la séance et le plus vite bâclé.")

    d.piege("Réciter dix choses qu'on sait faire",
            "Je sais faire le ménage, la cuisine, la couture, le repassage…",
            "Je sais faire le ménage. J'ai de l'expérience en garde d'enfants.",
            "Une liste de dix choses ne laisse rien en tête. Deux choses précises, "
            "dites avec assurance, restent. On garde le reste pour la deuxième "
            "conversation, celle qui suivra le rappel.",
            notes="Point délicat : plusieurs élèves croient qu'en dire plus vaut mieux. "
                  "Faire l'expérience — écouter deux versions, redire ce qu'on retient.")

    d.pratique('Écriture', "Complétez chaque phrase",
               "Complétez avec : bonjour, affiche, engagez, faire, libre, joindre.", [
        ("___ , monsieur. Excusez-moi de vous déranger.", "Bonjour"),
        ("J'ai vu votre ___ dans la vitrine.", "affiche"),
        ("Est-ce que vous ___ encore ?", "engagez"),
        ("Le ménage, je sais ___ .", "faire"),
        ("Je suis ___ du lundi au vendredi, le matin.", "libre"),
        ("Vous pouvez me ___ au 438 555-0192.", "joindre"),
    ], corrige=True,
       notes="Même exercice que prQuatre dans le module. Faire lire chaque phrase "
             "complétée à voix haute avant de passer à la suivante.")

    d.pratique('Production', "Écrivez vos quatre phrases",
               "À vous. Quatre lignes, sur un papier que vous gardez.", [
        ("1. Pourquoi vous venez", "J'ai vu votre affiche. / Est-ce que vous cherchez quelqu'un ?"),
        ("2. Ce que vous savez faire", "Je sais faire… / J'ai de l'expérience en…"),
        ("3. Quand vous êtes libres", "Je suis libre du… au…, de… à…"),
        ("4. Votre nom et votre numéro", "Je m'appelle… Vous pouvez me joindre au…"),
    ], notes="Vingt minutes. Passer dans les rangées et corriger à voix basse, une "
             "personne à la fois. Les quatre phrases doivent tenir sur un seul papier.")

    d.billet(
        "Dites vos quatre phrases à voix haute, à quelqu'un, avant demain.",
        exemples=[
            "À un membre de votre famille, ou devant un miroir.",
            "Trois fois de suite, sans regarder votre papier la troisième fois.",
        ],
        notes="Devoir oral. Vérifier en B1 : demander qui l'a fait et devant qui.")

    return d.save(dossier)
