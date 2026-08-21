# -*- coding: utf-8 -*-
"""C1 · Case par case.
Bloc C « Défi 2 · Le formulaire d'inscription » · couleur acier · 75 min.
Source : dialogue `t2`, exercices `t2vf`, `t2case` et `t2form`, mini-leçon
`t2form`.

La seconde intention du programme, et la seule qui soit une production
écrite pure : remplir un formulaire d'inscription. Sept cases, et six d'entre
elles reviennent sur tous les papiers du Québec — à la clinique, à la banque,
à la bibliothèque municipale.

La case qui pose vraiment problème n'est pas la plus longue, c'est la plus
courte : « scolarité ». Personne ne comprend ce mot la première fois, et la
seule chose à savoir est de demander.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-inscription/images/')


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Case par case",
        chapeau="Comprendre chaque case d'un formulaire et écrire dedans la "
                "bonne réponse.",
        duree='75 minutes')

    d.titre(notes="Séance de papier. Photocopier un vrai formulaire vierge pour chacun — "
                  "inscription, bibliothèque, carte de la ville. Rien ne remplace une "
                  "feuille qu'on remplit pour de bon.")

    d.objectifs([
        "nommer les sept cases du formulaire ;",
        "écrire la bonne réponse dans chaque case ;",
        "comprendre le mot « scolarité » ;",
        "demander « c'est quoi, cette case ? ».",
    ])

    d.declencheur(
        'Observation', "Regardez ce formulaire. Quelle case vous fait hésiter ?",
        pistes=[
            "Combien de cases est-ce que vous comprenez tout de suite ?",
            "Laquelle est la plus difficile ?",
            "Qu'est-ce que vous faites quand vous ne comprenez pas ?",
            "Est-ce que vous laissez la case vide ?",
        ],
        notes="La quatrième piste est la vraie : beaucoup laissent une case vide plutôt "
              "que de demander, et le dossier s'arrête là. C'est ce que la séance "
              "vient corriger.")

    d.dialogue('Dialogue · 1 de 2', "Le nom, le prénom, la naissance", [
        ("MME BOURGEOIS", "Votre nom de famille, s'il vous plaît.", True),
        ("YARA", "Haddad.", True),
        ("MME BOURGEOIS", "Et votre prénom ?", True),
        ("YARA", "Yara.", True),
        ("MME BOURGEOIS", "Votre date de naissance ?", True),
        ("YARA", "Le 7 mars 1994.", True),
    ], consigne="Écoutez, puis comptez les mots de chaque réponse.",
       notes="Un mot, un mot, cinq mots. Faire compter par le groupe : au comptoir, une "
             "réponse courte est une réponse complète.")

    d.dialogue('Dialogue · 2 de 2', "La case qu'on ne comprend pas", [
        ("MME BOURGEOIS", "Combien d'années d'école, dans votre pays ?", True),
        ("YARA", "Onze ans. Je mets onze dans la case ?", True),
        ("MME BOURGEOIS", "Oui, onze. C'est la case « scolarité ».", True),
    ], notes="Trois répliques, et le mot le plus difficile du module se règle. Faire "
             "remarquer que Yara vérifie avant d'écrire, pas après.")

    d.tableau('Analyse', "Les sept cases, dans l'ordre",
              ["La case", "Ce qu'on écrit dedans"],
              [["Nom de famille", "HADDAD — en lettres majuscules"],
               ["Prénom", "Yara — une majuscule, puis des petites lettres"],
               ["Date de naissance", "1994-03-07 — année, mois, jour"],
               ["Adresse", "3420, rue Papineau, Montréal"]],
              cle=0,
              note="Une case, une réponse. Jamais deux choses dans la même case.",
              notes="Diapositive à photographier. Faire remplir les quatre premières "
                    "cases du vrai formulaire pendant que la diapositive est affichée.")

    d.tableau('Analyse · suite', "Et les trois dernières",
              ["La case", "Ce qu'on écrit dedans"],
              [["Téléphone et courriel", "dix chiffres, puis son adresse de messages"],
               ["Scolarité", "11 — le nombre d'années d'école"],
               ["Signature", "son nom écrit à la main, au bas de la page"]],
              cle=0,
              note="Un formulaire sans signature n'est pas accepté.",
              notes="Diapositive à photographier. Le tableau a été coupé en deux : sept "
                    "rangées ne tiennent pas sur une diapositive projetée.")

    d.regle("« C'est quoi, cette case ? »",
            "Quatre mots qui débloquent tout le formulaire.",
            precision="Une case vide arrête le dossier entier. Une question de quatre "
                      "mots le débloque. La personne au comptoir répond à celle-là dix "
                      "fois par jour : elle ne se fâche jamais, et elle a l'habitude "
                      "d'expliquer avec d'autres mots.",
            notes="Diapositive à photographier. Faire dire la phrase par chaque élève. "
                  "Elle vaut pour toute la vie administrative, pas seulement pour ce "
                  "formulaire.")

    d.pratique('Pratique', "Dans quelle case ?",
               "Dites le nom de la case pour chaque renseignement.", [
        ("HADDAD", "nom de famille"),
        ("1994-03-07", "date de naissance"),
        ("3420, rue Papineau", "adresse"),
        ("11", "scolarité"),
        ("son nom écrit à la main", "signature"),
    ], corrige=True, cols=2,
       notes="Cinq énoncés, faits à l'oral d'abord, puis écrits sur le vrai formulaire.")

    d.pratique('Pratique · avec un vrai formulaire', "Remplissez le vôtre",
               "Vingt-cinq minutes. Chacun remplit sa propre feuille.", [
        ("Étape 1", "Chacun remplit les sept cases de son formulaire."),
        ("Étape 2", "Il entoure au crayon la case qu'il n'a pas comprise."),
        ("Étape 3", "Il demande « c'est quoi, cette case ? » à son voisin."),
        ("Étape 4", "Si le voisin ne sait pas, il pose la question à l'enseignant."),
    ], cols=1,
       notes="Le cœur de la séance. Passer dans les rangées : les cases entourées "
             "disent exactement quels mots manquent au groupe, et elles ne sont jamais "
             "les mêmes d'une classe à l'autre.")

    d.billet(
        "Écrivez ce que vous mettez dans les sept cases de votre formulaire.",
        exemples=[
            "Nom de famille : …",
            "Date de naissance : …",
            "Scolarité : … années",
        ],
        notes="Devoir court. Ceux qui l'ont écrit une fois le refont ensuite de "
              "mémoire, et c'est tout l'enjeu du module.")

    return d.save(dossier)
