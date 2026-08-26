# -*- coding: utf-8 -*-
"""C3 · Quel, quelle, quels, quelles.
Bloc C · couleur ambre (écriture) · 75 min.
Source : exercice `t2quel` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre='Quel, quelle, quels, quelles',
        chapeau="Quatre formes, une seule prononciation. À l'oral, personne ne peut vous "
                "corriger. À l'écrit, c'est l'une des erreurs les plus visibles d'un "
                "courriel professionnel.",
        duree='75 minutes')

    d.titre(notes="Dire les quatre formes à voix haute et demander au groupe combien il "
                  "en entend. Réponse : une seule. C'est exactement le problème de la "
                  "séance.")

    d.objectifs([
        "accorder quel avec le nom qui suit ou qui précède ;",
        "choisir entre les quatre formes sans hésiter ;",
        "poser une question précise dans un message professionnel ;",
        "relire un texte en vérifiant ces accords.",
    ])

    d.regle('La règle',
            "Quel prend le genre et le nombre du nom auquel il se rapporte.",
            precision="Quel est ton nom ? — nom, masculin singulier. Quelle est ton "
                      "adresse ? — adresse, féminin singulier. Quels sont les "
                      "critères ? — pluriel masculin. Quelles sont tes habiletés ? — "
                      "pluriel féminin.",
            notes="Écrire les quatre exemples au tableau, avec le nom entouré. C'est le "
                  "nom qui commande, jamais autre chose.")

    d.tableau('Analyse', "Les quatre formes",
              ['La forme', 'Genre et nombre', 'Un exemple'],
              [["quel", "masculin singulier", "Quel est ton objectif ?"],
               ["quelle", "féminin singulier", "Quelle est ton adresse ?"],
               ["quels", "masculin pluriel", "Quels sont les avantages ?"],
               ["quelles", "féminin pluriel", "Quelles sont tes habiletés ?"]],
              cle=0,
              note="Les quatre se prononcent exactement pareil. Seul l'écrit les "
                   "distingue.",
              notes="Faire lire la colonne du milieu à voix haute : c'est elle qu'il faut "
                    "chercher avant d'écrire.")

    d.regle('La méthode en trois temps',
            "Trouver le nom · trouver son genre · trouver son nombre.",
            precision="« ___ est la raison de ton retard ? » Le nom est « raison ». "
                      "Raison est féminin. Il est singulier. Donc : quelle. Trois "
                      "questions, dans cet ordre, et il n'y a plus d'hésitation.",
            notes="Faire appliquer la méthode à voix haute sur trois exemples avant de "
                  "lancer les exercices écrits.")

    d.cartes('Ouvrir la mini-leçon', "Quatre choses à savoir en plus", [
        ("Le nom peut venir après le verbe",
         "« Quelle est ton adresse ? » — le nom « adresse » est après « est ». On "
         "l'accorde quand même : c'est de lui qu'on parle."),
        ("Quel peut être collé au nom",
         "« Quel jour ? » « Quelle heure ? » Ici, le nom suit immédiatement. C'est le "
         "cas le plus facile."),
        ("Ne pas confondre avec « qu'elle »",
         "« Quelle est la raison ? » et « la raison qu'elle donne » sont deux choses "
         "différentes. « Qu'elle » se remplace par « qu'il » ; « quelle », non."),
        ("Dans une question indirecte",
         "« Je voudrais savoir quelle est la procédure. » Pas de point "
         "d'interrogation, mais le même accord."),
    ], notes="La troisième carte donne un test mécanique très fiable. Le faire pratiquer "
             "sur deux ou trois phrases.")

    d.pratique('Pratique · 1 de 4', "Quel, quelle, quels ou quelles ?",
               "Trouvez le nom, son genre, son nombre.", [
        ("___ est la raison de ton retard ce matin ?", "quelle — raison, féminin singulier"),
        ("___ sont les avantages de ton nouvel horaire ?", "quels — avantages, masculin pluriel"),
        ("___ sont tes habitudes le matin ?", "quelles — habitudes, féminin pluriel"),
        ("___ est ton objectif principal ce trimestre ?", "quel — objectif, masculin singulier"),
        ("___ sont les inconvénients de ce trajet ?", "quels — inconvénients, masculin pluriel"),
        ("___ sont les matières que tu préfères ?", "quelles — matières, féminin pluriel"),
    ], corrige=True,
       notes="Faire nommer le genre et le nombre à voix haute avant chaque réponse. Sans "
             "cette étape, l'exercice devient un jeu de hasard.")

    d.pratique('Pratique · 2 de 4', "Quatre autres, plus difficiles",
               "Le nom n'est pas toujours au même endroit.", [
        ("___ est le but principal de ta demande ?", "quel — but"),
        ("___ est ton opinion sur le nouveau règlement ?", "quelle — opinion"),
        ("___ est ton moyen de transport préféré ?", "quel — moyen"),
        ("___ sont les ressources que tu me conseilles ?", "quelles — ressources"),
    ], corrige=True,
       notes="« Opinion » et « ressources » sont les deux mots dont le genre pose "
             "problème. Les faire vérifier dans un dictionnaire si nécessaire.")

    d.piege("Le piège du « qu'elle »",
            "Qu'elle est la raison de ton retard ?",
            "Quelle est la raison de ton retard ?",
            "« Qu'elle » veut dire « que elle » : il faut pouvoir le remplacer par "
            "« qu'il ». Ici, « qu'il est la raison » ne veut rien dire — c'est donc "
            "« quelle », en un seul mot. Le test fonctionne à tous les coups.",
            notes="Faire appliquer le test à trois phrases au tableau. C'est mécanique et "
                  "ça règle définitivement la confusion.")

    d.piege("Le piège du genre du nom",
            "Quel est ton adresse ?",
            "Quelle est ton adresse ?",
            "« Adresse » est féminin, même si on dit « ton adresse » et non « ta "
            "adresse » — le « ton » vient du son, pas du genre. Ne vous fiez jamais au "
            "déterminant devant une voyelle : cherchez le genre du nom lui-même.",
            notes="Relier au module 2, séance C3 : « mon adresse », « ton adresse » sont "
                  "des exceptions de son. Le genre du nom, lui, ne change pas.")

    d.pratique('Pratique · 3 de 4', "Écrivez la question",
               "Employez quel, quelle, quels ou quelles.", [
        ("Vous voulez connaître l'heure du rendez-vous.", "Quelle est l'heure du rendez-vous ?"),
        ("Vous voulez connaître les documents à apporter.", "Quels sont les documents à apporter ?"),
        ("Vous voulez connaître la procédure à suivre.", "Quelle est la procédure à suivre ?"),
        ("Vous voulez connaître les dates d'inscription.", "Quelles sont les dates d'inscription ?"),
    ], corrige=True,
       notes="Ces quatre questions sont exactement celles qu'on pose au téléphone à un "
             "centre de formation. Les faire copier dans le cahier.")

    d.pratique('Pratique · 4 de 4', "Relisez et corrigez",
               "Chaque phrase contient une erreur d'accord.", [
        ("Quel est ton adresse ?", "Quelle — adresse est féminin"),
        ("Quelles sont les documents à apporter ?", "Quels — documents est masculin"),
        ("Qu'elle est la raison de ton absence ?", "Quelle — en un seul mot"),
        ("Quel sont tes disponibilités ?", "Quelles — disponibilités, féminin pluriel"),
    ], corrige=True,
       notes="Exercice de relecture, la compétence qui sert vraiment. Faire chercher "
             "d'abord le nom dans chaque phrase.")

    d.billet(
        "Écrivez quatre questions, une avec chacune des quatre formes.",
        exemples=[
            "Elles doivent porter sur une inscription ou un horaire de cours.",
            "Soulignez le nom qui commande l'accord dans chaque question.",
        ],
        notes="Corriger les billets en dehors du cours. Le nom souligné montre si la "
              "méthode est acquise, même quand la réponse est fausse.")

    return d.save(dossier)
