# -*- coding: utf-8 -*-
"""C1 · Diane explique, étape par étape.
Bloc C · couleur acier (compréhension orale) · 60 min.
Source : dialogue `t2` et exercice `t2ord`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre='Diane explique, étape par étape',
        chapeau="Cinq étapes dites en six répliques, sans papier, sans écran. C'est "
                "l'exercice d'écoute le plus difficile du module : il faut retenir un "
                "ordre, pas seulement des informations.",
        duree='60 minutes')

    d.titre(notes="Ouverture du défi 2. Prévenir : on écoutera deux fois, et il faudra "
                  "noter les étapes dans l'ordre. Distribuer des feuilles numérotées "
                  "de 1 à 5.")

    d.objectifs([
        "suivre une explication orale en cinq étapes ;",
        "noter un ordre pendant l'écoute ;",
        "repérer les mots qui marquent le passage d'une étape à l'autre ;",
        "vérifier son ordre en reformulant.",
    ])

    d.dialogue('Dialogue · 1 de 3', "D'abord, tu ouvres l'application", [
        ("DIANE", "D'abord, tu ouvres l'application Ressources+ et tu appuies sur "
                  "Nouvelle demande.", True),
        ("SAMUEL", "D'accord, et ensuite ?", False),
    ], consigne="Écoutez deux fois, diapo masquée. Notez les étapes dans l'ordre.",
       notes="Passer l'audio du défi 2. Faire remarquer « D'abord » : le mot d'ordre "
             "travaillé en A4 apparaît ici dans une vraie explication.")

    d.dialogue('Dialogue · 2 de 3', "Tu prends une photo claire", [
        ("DIANE", "Tu prends une photo claire de ton reçu directement avec "
                  "l'application.", True),
        ("SAMUEL", "Et pour le montant ?", False),
    ], notes="« Directement avec l'application » : le détail qui compte. Une photo prise "
             "avant, dans la galerie, ne se joint pas de la même façon.")

    d.dialogue('Dialogue · 3 de 3', "Tu inscris le montant exact", [
        ("DIANE", "Tu inscris le montant exact, tu choisis la catégorie « équipement de "
                  "sécurité », puis tu appuies sur Envoyer.", True),
        ("SAMUEL", "Merci, Diane, c'est très clair !", False),
    ], notes="Trois actions dans une seule réplique : montant, catégorie, envoi. C'est "
             "là que les élèves perdent le compte. Le signaler avant la deuxième "
             "écoute.")

    d.tableau('Analyse', "Les cinq étapes, dans l'ordre",
              ['Rang', 'L\'étape'],
              [["1", "ouvrir l'application Ressources+"],
               ["2", "appuyer sur Nouvelle demande"],
               ["3", "prendre une photo claire du reçu"],
               ["4", "inscrire le montant exact"],
               ["5", "choisir la catégorie et appuyer sur Envoyer"]],
              cle=0, props=[0.12, 0.88],
              note="La cinquième étape en contient deux : c'est fréquent dans une "
                   "explication orale, et c'est ce qui trompe.",
              notes="Faire compter les verbes de la dernière réplique : inscris, "
                    "choisis, appuies. Trois actions, une seule phrase.")

    d.regle("Ce qui marque le passage d'une étape à l'autre",
            "D'abord · ensuite · puis · enfin — ou simplement un nouveau verbe.",
            precision="Diane n'emploie qu'un seul mot d'ordre : « d'abord ». Ensuite, "
                      "elle enchaîne les verbes : tu prends, tu inscris, tu choisis, tu "
                      "appuies. À l'oral, c'est le verbe qui marque l'étape.",
            notes="C'est la difficulté réelle de l'écoute : compter les verbes, pas les "
                  "mots d'ordre. Le dire explicitement.")

    d.pratique('Pratique · 1 de 4', "Remettez les étapes dans l'ordre",
               "Numérotez de 1 à 5.", [
        ("Prendre une photo claire du reçu.", "3"),
        ("Ouvrir l'application Ressources+.", "1"),
        ("Choisir la catégorie et appuyer sur Envoyer.", "5"),
        ("Appuyer sur Nouvelle demande.", "2"),
        ("Inscrire le montant exact.", "4"),
    ], corrige=True,
       notes="Corriger avant de réécouter. Puis réécouter une troisième fois : c'est là "
             "que les élèves voient où ils ont perdu le fil.")

    d.pratique('Pratique · 2 de 4', "Comptez les verbes",
               "Combien d'actions dans chaque réplique de Diane ?", [
        ("« Tu ouvres l'application et tu appuies sur Nouvelle demande. »", "deux"),
        ("« Tu prends une photo claire de ton reçu. »", "une"),
        ("« Tu inscris le montant, tu choisis la catégorie, puis tu appuies sur Envoyer. »",
         "trois"),
    ], corrige=True,
       notes="Exercice court mais décisif : c'est la méthode d'écoute de toute la "
             "séance. Compter les verbes, pas les phrases.")

    d.piege("Le piège de la phrase à trois verbes",
            "Trois actions comptées pour une seule étape.",
            "Chaque verbe est une étape à faire.",
            "À l'oral, on enchaîne les actions dans une seule phrase : « tu inscris, tu "
            "choisis, tu appuies ». Compter les phrases donne cinq étapes au lieu de "
            "sept. Comptez les verbes, et vous ne manquerez rien.",
            notes="Faire réécouter la dernière réplique en levant un doigt à chaque "
                  "verbe. L'exercice est physique et il fonctionne.")

    d.piege("Le piège du détail sauté",
            "Tu prends une photo du reçu.",
            "Tu prends une photo claire du reçu, directement avec l'application.",
            "« Claire » et « directement avec l'application » sont deux détails qui "
            "décident du succès de la demande. Une photo floue fait refuser ; une photo "
            "prise ailleurs ne se joint parfois pas. Les adjectifs et les compléments "
            "comptent dans une procédure.",
            notes="Faire chercher, dans les cinq étapes, tous les mots de précision : "
                  "claire, exact, bonne catégorie, original. Ils sont tous décisifs.")

    d.pratique('Pratique · 3 de 4', "Repérez le mot de précision",
               "Quel mot rend l'étape exacte ?", [
        ("Tu prends une photo ___ du reçu.", "claire"),
        ("Tu inscris le montant ___.", "exact"),
        ("Tu choisis la ___ catégorie.", "bonne"),
        ("Garde ton reçu ___.", "original"),
    ], corrige=True,
       notes="Ces quatre mots sont ceux qui distinguent une demande acceptée d'une "
             "demande refusée. Les faire souligner dans le cahier.")

    d.pratique('Pratique · 4 de 4', "Reformulez les cinq étapes",
               "À voix haute, sans notes, avec les mots d'ordre.", [
        ("Étape 1", "D'abord, j'ouvre l'application Ressources+."),
        ("Étape 2", "Ensuite, j'appuie sur Nouvelle demande."),
        ("Étape 3", "Puis je prends une photo claire de mon reçu."),
        ("Étape 4", "Après ça, j'inscris le montant exact."),
        ("Étape 5", "Enfin, je choisis la catégorie et j'appuie sur Envoyer."),
    ], corrige=True,
       notes="Faire dire les cinq d'un seul trait par trois élèves différents, debout. "
             "C'est la synthèse de la séance.")

    d.billet(
        "Écrivez les cinq étapes, dans l'ordre, avec un mot d'ordre chacune.",
        exemples=[
            "D'abord · ensuite · puis · après ça · enfin.",
            "N'oubliez pas les mots de précision : claire, exact, bonne.",
        ],
        notes="Ramasser. Ces billets serviront en E1, où la même procédure sera écrite "
              "pour un collègue.")

    return d.save(dossier)
