# -*- coding: utf-8 -*-
"""B4 · « Ce que je ferai »
Bloc B « Défi 1 · L'invitation » · couleur ambre · 75 min.
Source : exercices `t1fut` et `t1mail`, mini-leçon `t1fut`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="« Ce que je ferai »",
        chapeau="Accepter une invitation, c'est promettre quelque chose : "
                "d'être là, d'apporter un plat, de répondre avant jeudi. Le "
                "futur simple est le temps de ces promesses, et c'est celui "
                "de l'écrit.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du défi 1. Elle réunit une grammaire — le futur simple "
                  "— et une production écrite courte : le refus de madame Faye, ligne par "
                  "ligne. Prévoir la moitié du temps pour chacune.")

    d.objectifs([
        "former le futur simple des verbes réguliers ;",
        "employer les huit irréguliers des invitations ;",
        "garder le futur après « quand » et « dès que » ;",
        "écrire un refus poli en cinq lignes.",
    ], notes="Le troisième objectif est celui qui demande le plus de répétition : "
             "beaucoup de langues mettent le présent après « quand ».")

    d.regle("L'infinitif, plus six terminaisons",
            "Le futur simple est le temps le plus régulier du français : "
            "l'infinitif entier, puis -ai, -as, -a, -ons, -ez, -ont.",
            precision="apporter donne j'apporterai · finir donne je finirai · "
                      "répondre perd son e et donne je répondrai. Un repère à "
                      "l'oreille : on entend toujours le r avant la terminaison. "
                      "Sans ce r, ce n'est pas du futur.",
            notes="Diapositive à photographier. Le repère du r est le plus utile à l'oral, "
                  "où les terminaisons se ressemblent : « je répondai » ne veut rien dire, "
                  "mais on l'entend souvent.")

    d.cartes("Les huit irréguliers", "Ceux dont on a besoin pour répondre à une invitation", [
        ("être, avoir",
         "je serai, j'aurai"),
        ("aller, faire",
         "j'irai, je ferai"),
        ("venir, pouvoir",
         "je viendrai, je pourrai"),
        ("vouloir, devoir",
         "je voudrai, je devrai"),
    ], notes="Seul le radical est irrégulier : les terminaisons ne changent jamais. Faire "
             "remarquer la proximité de « j'aurai » et « j'irai », qui se confondent à "
             "l'oreille et qui ne veulent pas du tout dire la même chose.")

    d.regle("Après « quand », le futur reste au futur",
            "Je vous préviendrai quand je saurai mon horaire.",
            precision="Et de même après « dès que » : dès qu'il fera beau, on "
                      "sortira les tables. Beaucoup de langues mettent le présent à "
                      "cet endroit ; le français, non.",
            notes="Faire apprendre trois phrases entières plutôt que la règle : « quand je "
                  "saurai », « dès qu'il fera beau », « quand vous arriverez ». Les "
                  "modèles se retiennent mieux que l'explication.")

    d.pratique('Grammaire', "Mettez au futur simple",
               "Chaque phrase est une promesse.", [
        ("J' ___ (apporter) un plat pour six personnes.", "apporterai"),
        ("Je ___ (être) là vers midi et demi.", "serai"),
        ("Nous ___ (sortir) les tables à onze heures.", "sortirons"),
        ("Il ___ (faire) le tour des portes le matin même.", "fera"),
        ("Elle ___ (venir) le dimanche si la fête est reportée.", "viendra"),
        ("Je vous ___ (répondre) d'ici jeudi, sans faute.", "répondrai"),
        ("Dès qu'il ___ (faire) beau, on installera tout dehors.", "fera"),
    ], corrige=True,
       notes="Exercice t1fut de l'activité. Faire lire chaque phrase à voix haute après "
             "l'avoir complétée : on vérifie le r à l'oreille en même temps que la forme "
             "à l'écrit.")

    d.tableau('Le refus écrit', "Cinq lignes, pas une de plus",
              ['La ligne', 'Ce qu\'elle contient'],
              [["Bonjour monsieur Deslauriers,", "Le nom, une virgule"],
               ["Merci pour votre invitation.", "Le remerciement, avant tout"],
               ["Je ne pourrai pas être là.", "Le refus, au futur"],
               ["Je travaille ce jour-là.", "La raison, une phrase"],
               ["Bonne journée, Ndeye Faye, logement 3", "La signature et le logement"]],
              cle=1,
              notes="Faire remarquer la signature : dans un immeuble de douze portes, le "
                    "prénom seul ne suffit pas. C'est un détail concret que les élèves "
                    "n'inventent jamais seuls.")

    d.pratique('Écriture', "Le refus de madame Faye",
               "Complétez son message, ligne par ligne.", [
        ("Bonjour ___ Deslauriers,", "monsieur"),
        ("___ beaucoup pour votre invitation à la fête de la ruelle.", "Merci"),
        ("___ , je ne pourrai pas être là le 7 juin.", "Malheureusement"),
        ("Si la fête est ___ au dimanche, je serai libre.", "reportée"),
        ("Au ___ de vous voir dans la ruelle cet été.", "plaisir"),
    ], corrige=True,
       notes="Exercice t1mail de l'activité. Le faire au tableau d'abord, puis laisser "
             "chacun écrire son propre refus sur le même patron, pour une invitation "
             "inventée.")

    d.piege("Oublier le r du futur",
            "je répondai, je viendai",
            "je répondrai, je viendrai",
            "Le r est la marque du futur, à toutes les personnes. Sans lui, la forme "
            "n'existe pas. Dire lentement : ré-pon-d-r-ai.",
            notes="Faire dire la syllabe en trois temps, en tapant la table. C'est "
                  "mécanique et ça règle le problème en une séance.")

    d.billet(
        "Écrivez trois promesses au futur simple, pour une invitation que vous acceptez.",
        exemples=[
            "Une promesse sur l'heure, une sur ce que vous apportez, une sur la suite.",
            "Vérifiez le r dans chacune avant de remettre.",
        ],
        notes="Fin du bloc B. Les trois promesses se réinvestissent directement dans le "
              "message téléphonique de la séance E1.")

    return d.save(dossier)
