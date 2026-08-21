# -*- coding: utf-8 -*-
"""A1 · Où est le local 214 ?
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercices `prVocab` et `pr1`.

Sixième module court du projet. L'élève de niveau 2 tient une phrase à la
fois : les diapositives portent peu de mots, et chaque phrase projetée est
une phrase qu'il dira vraiment dans le corridor du centre.

La situation du programme est « Orientation dans l'établissement ». Elle est
la plus concrète de toutes, parce que le bâtiment est là, autour du groupe :
la séance se termine debout, dans le vrai corridor.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-couloirs/images/')


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Où est le local 214 ?",
        chapeau="Nommer les endroits du centre et poser la première question "
                "du premier matin.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Commencer sans diapositive : demander à "
                  "chacun le numéro de son local. Ceux qui ne le savent pas sont "
                  "exactement ceux pour qui le module est fait.")

    d.objectifs([
        "nommer six endroits du centre ;",
        "reconnaitre un numéro de local ;",
        "demander où est un endroit ;",
        "redire une indication pour vérifier.",
    ])

    d.declencheur(
        'Observation', "Où est-ce que cette photo a été prise ?",
        image=IMG + 'corridor-etage.jpg',
        pistes=[
            "Qu'est-ce qu'il y a des deux côtés ?",
            "Comment on appelle ce long passage ?",
            "Qu'est-ce qu'il y a sur chaque porte ?",
            "Vous, votre local, c'est quel numéro ?",
        ],
        notes="Laisser chercher le mot « corridor » avant de le donner. La quatrième "
              "piste est la vraie : beaucoup d'élèves ne connaissent pas le numéro de "
              "leur propre local, et le découvrent ici.")

    d.dialogue('Dialogue · 1 de 2', "Le premier matin de Soraya", [
        ("SORAYA", "Bonjour. Excusez-moi, je cherche le local 214.", True),
        ("GILLES", "Bonjour ! Le 214, c'est au deuxième étage.", True),
        ("SORAYA", "Au deuxième étage ?", True),
        ("GILLES", "Oui. Prenez l'escalier, là, au milieu du corridor.", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Faire écouter deux fois, diapositive masquée. Insister sur la troisième "
             "réplique : Soraya répète ce qu'elle a entendu. C'est le comportement que "
             "le module veut installer, plus encore que le vocabulaire.")

    d.dialogue('Dialogue · 2 de 2', "L'escalier ou l'ascenseur ?", [
        ("SORAYA", "L'escalier ou l'ascenseur ?", True),
        ("GILLES", "Les deux montent. L'ascenseur est juste à côté.", True),
        ("SORAYA", "Merci beaucoup, monsieur.", True),
        ("GILLES", "Bonne journée ! Et bienvenue au centre.", True),
    ], notes="Quatre répliques, et une personne perdue qui ne l'est plus. Faire "
             "remarquer que Soraya ne s'excuse pas d'avoir demandé : elle remercie.")

    d.tableau('Analyse', "Ce que demande Soraya, ce que répond Gilles",
              ["Soraya dit", "Gilles répond"],
              [["Je cherche le local 214.", "C'est au deuxième étage."],
               ["Au deuxième étage ?", "Oui."],
               ["L'escalier ou l'ascenseur ?", "Les deux montent."],
               ["Merci beaucoup, monsieur.", "Bonne journée !"]],
              cle=1,
              note="Gilles donne une seule chose à la fois : l'étage, puis le chemin.",
              notes="Diapositive à photographier. Faire jouer les quatre lignes à deux, "
                    "debout, avant de passer au vocabulaire.")

    d.vocabulaire('Vocabulaire', "Les endroits du centre", [
        ("un corridor", "Le long passage étroit qui va d'une porte à l'autre."),
        ("un étage", "Un niveau du bâtiment : on monte pour y aller."),
        ("un escalier", "Les marches qu'on monte pour changer d'étage."),
        ("un ascenseur", "La petite pièce qui monte et qui descend toute seule."),
    ], notes="Diapositive à photographier. Faire répéter chaque mot avec son article : "
             "l'article s'apprend avec le mot, jamais après.")

    d.regle("« Excusez-moi, où est… ? »",
            "Quatre mots qui ouvrent toutes les portes du centre.",
            precision="On commence par « <b>excusez-moi</b> », puis on pose la "
                      "question, puis on <b>remercie</b>. Trois temps, toujours les "
                      "mêmes. Personne ne se fâche jamais d'avoir été dérangé pour ça.",
            notes="Diapositive à photographier. Faire dire la phrase par chaque élève, "
                  "un par un, à voix haute. C'est la phrase la plus utile du module.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Soraya cherche le local 214.", "vrai"),
        ("Le local 214 est au rez-de-chaussée.", "faux - il est au deuxième étage"),
        ("Gilles montre l'escalier à Soraya.", "vrai"),
        ("Il n'y a pas d'ascenseur dans le centre.", "faux - il est à côté de l'escalier"),
    ], corrige=True, cols=1,
       notes="Quatre énoncés seulement. Les faire d'abord à l'oral, en groupe, avant de "
             "les faire écrire.")

    d.pratique('Pratique · dans le vrai corridor', "Sortez de la classe",
               "Vingt minutes, debout, dans le bâtiment.", [
        ("Étape 1", "Le groupe sort et marche jusqu'au bout du corridor."),
        ("Étape 2", "Chacun nomme ce qu'il voit : une porte, un escalier, un casier."),
        ("Étape 3", "Chacun lit le numéro d'une porte à voix haute."),
        ("Étape 4", "Chacun montre où est son propre local."),
    ], cols=1,
       notes="La séance la plus utile du module se passe hors de la classe. Prévenir le "
             "secrétariat avant. L'étape 4 révèle qui est encore perdu.")

    d.billet(
        "Écrivez le numéro de votre local et le nom de trois endroits du centre.",
        exemples=[
            "Mon local : le 214",
            "un corridor",
            "un escalier",
            "un ascenseur",
        ],
        notes="Devoir court. Demander l'article avec le mot : c'est là qu'il s'apprend, "
              "et le corriger plus tard coûte trois fois plus cher.")

    return d.save(dossier)
