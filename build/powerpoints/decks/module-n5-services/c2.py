# -*- coding: utf-8 -*-
"""C2 · Qui, que, dont, où.
Bloc C « Défi 2 · L'écran » · couleur ambre · 75 min.
Source : exercice `t2rel` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Qui, que, dont, où",
        chapeau="Le niveau 5 n'attend plus des phrases courtes, mais un "
                "discours organisé. Quatre petits mots suffisent à joindre "
                "deux idées — et ce sont eux qui tiennent les longues "
                "phrases des pages officielles.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire. Commencer par relever au tableau, dans le "
                  "dialogue de C1, les quatre relatifs que Leïla et Pierre-Luc emploient "
                  "sans y penser. Le groupe les cherche : cinq minutes, et ça pose la séance.")

    d.objectifs([
        "choisir entre qui et que par le test de trois secondes ;",
        "employer dont quand la phrase de départ contient « de » ;",
        "employer où pour le lieu et pour le moment ;",
        "accorder le participe passé après « que ».",
    ])

    d.declencheur(
        'Comparaison', "Deux phrases courtes, ou une seule ?",
        pistes=[
            "« C'est un lieu. On y apporte les vieux appareils. »",
            "« C'est un lieu où on apporte les vieux appareils. »",
            "Laquelle sonne comme un adulte qui parle ?",
            "Qu'est-ce qu'on a gagné ? Qu'est-ce qu'on a perdu ?",
        ],
        notes="Le groupe préfère presque toujours la seconde sans savoir dire pourquoi. "
              "Nommer la raison : on ne répète plus, et les deux idées deviennent une "
              "seule information.")

    d.regle("Le test de trois secondes",
            "Un verbe seul après le trou : qui. Un sujet puis un verbe : que.",
            precision="« L'encadré ___ est en haut » : après le trou vient « est », un "
                      "verbe seul, donc qui. « Le formulaire ___ j'ai rempli » : après le "
                      "trou vient « j'ai », un sujet et un verbe, donc que. Ce test règle "
                      "neuf cas sur dix sans aucune grammaire.",
            notes="Diapositive à photographier. C'est l'outil de toute la séance. Le faire "
                  "appliquer à voix haute, lentement, sur les deux exemples.")

    d.tableau('Les quatre relatifs', "Quand employer lequel",
              ['Relatif', 'Ce qui suit', 'Exemple'],
              [["qui", "un verbe tout de suite", "le préposé qui a ouvert ma requête"],
               ["que", "un sujet, puis un verbe", "le formulaire que j'ai rempli"],
               ["dont", "la phrase avait « de »", "la page dont tu m'as parlé"],
               ["où", "un lieu ou un moment", "le jour où le camion passe"]],
              cle=0,
              note="« qui » ne s'élide jamais : on écrit « qui a », jamais « qu'a ».",
              notes="Diapositive à photographier. Le tableau de référence : le laisser "
                    "affiché pendant tous les exercices de la séance.")

    d.cartes("Comment trouver « dont »", "Un seul test", [
        ("Cherchez le « de »",
         "« Tu m'as parlé DE cette page. » devient « la page dont tu m'as parlé »."),
        ("Les verbes qui l'appellent",
         "parler de · avoir besoin de · s'occuper de · être content de · avoir envie de."),
        ("S'il n'y a pas de « de »",
         "Ce n'est pas « dont ». C'est le seul test nécessaire."),
        ("L'erreur classique",
         "« La page que tu m'as parlé » — il manque le « de », donc il faut « dont »."),
    ], notes="Faire lister par le groupe d'autres verbes avec « de ». Ils en trouvent "
             "toujours plus qu'on ne pense, et la liste leur appartient ensuite.")

    d.regle("« où » sert aussi pour le moment",
            "le jour où le camion passe · l'année où je suis arrivée.",
            precision="La moitié de l'usage de « où » est ignorée par la plupart des "
                      "élèves, qui le réservent au lieu. « Le jour que » s'entend beaucoup "
                      "à l'oral d'ici, mais dans un courriel à un service, c'est « le jour "
                      "où ».",
            notes="Diapositive à photographier. Faire trouver trois exemples de temps par "
                  "le groupe : le moment où, l'année où, la semaine où.")

    d.pratique('Choix du relatif', "Complétez",
               "qui, que, dont ou où.", [
        ("C'est l'encadré ___ est en haut à droite.", "qui"),
        ("Le formulaire ___ j'ai rempli s'est bloqué.", "que"),
        ("J'ai enfin trouvé la page ___ tu m'avais parlé.", "dont"),
        ("L'écocentre est un lieu ___ on apporte les vieux appareils.", "où"),
        ("Le préposé ___ m'a répondu s'appelait Gaétan.", "qui"),
        ("La preuve de résidence ___ j'ai besoin, c'est mon bail.", "dont"),
        ("Le mardi est le jour ___ le camion passe.", "où"),
        ("Les pièces ___ elle a apportées étaient les bonnes.", "que (qu')"),
    ], corrige=True,
       notes="Faire appliquer le test à voix haute pour les six premières. Les deux "
             "dernières demandent un autre raisonnement : les garder pour la fin.")

    d.piege("Oublier l'accord après « que »",
            "les pièces d'identité qu'elle a apporté",
            "les pièces d'identité qu'elle a apportées",
            "Avec « que », le participe passé s'accorde avec ce qui précède — ici « les "
            "pièces », féminin pluriel. Avec « qui », jamais cet accord. C'est la seule "
            "différence grammaticale sérieuse entre les deux.",
            notes="Erreur presque universelle et qui persiste longtemps. Ne pas en faire "
                  "un drame : la signaler, la corriger, et y revenir en E2 à l'écrit.")


    d.pratique('Production', "Joignez les deux phrases",
               "Une seule phrase, avec le bon relatif.", [
        ("C'est un lieu. On y apporte les vieux appareils.",
         "C'est un lieu où on apporte les vieux appareils."),
        ("J'ai trouvé la page. Tu m'as parlé de cette page.",
         "J'ai trouvé la page dont tu m'as parlé."),
        ("Voici le formulaire. Il se bloque toujours.",
         "Voici le formulaire qui se bloque toujours."),
        ("C'est la facture. J'ai besoin de cette facture.",
         "C'est la facture dont j'ai besoin."),
        ("Le mardi est un jour. Le camion passe ce jour-là.",
         "Le mardi est le jour où le camion passe."),
        ("Voilà les pièces. Elle les a apportées.",
         "Voilà les pièces qu'elle a apportées."),
    ], corrige=True,
       notes="Exercice de synthèse. Faire écrire au tableau par des élèves différents, et "
             "faire vérifier l'accord de la dernière par le groupe.")

    d.billet(
        "Décrivez en cinq phrases un service que vous connaissez, avec les quatre relatifs.",
        exemples=[
            "Une au moins avec « dont », une au moins avec « où » pour un moment.",
            "Un service réel : votre école, votre clinique, votre banque.",
        ],
        notes="Devoir d'écriture qui prépare directement le courriel de E2. Le dire, pour "
              "que les élèves gardent leurs phrases.")

    return d.save(dossier)
