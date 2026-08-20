# -*- coding: utf-8 -*-
"""A2 · Le son « u » et le son « ou ».
Bloc A · couleur indigo (graphie-phonie) · 60 min.
Source : exercice `prPhon` et sa mini-leçon.

Le module affiche ces sons en alphabet phonétique. Pas ici : Verdana ne
possède aucun caractère de l'API. On nomme donc chaque son par ses lettres,
avec un mot repère — « brûlure » et « douleur », les deux mots du module.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Le son « u » et le son « ou »",
        chapeau="« Brûlure » et « douleur » : les deux mots de la séance précédente, et "
                "les deux sons que les élèves confondent le plus. Une lettre de "
                "différence, deux positions de lèvres.",
        duree='60 minutes')

    d.titre(notes="Commencer par écrire « brûlure » et « douleur » au tableau et faire "
                  "dire les deux mots par cinq élèves. Les erreurs se manifesteront "
                  "toutes seules.")

    d.objectifs([
        "entendre la différence entre le son « u » et le son « ou » ;",
        "savoir quelles lettres écrivent chacun des deux ;",
        "prononcer les mots du module sans les confondre ;",
        "reconnaître le son « i », le troisième de la famille.",
    ])

    d.regle('La règle',
            "La lettre u seule fait le son « u ». Les lettres o et u ensemble font le son « ou ».",
            precision="Brûlure, urgence, minute, sucre : le son « u ». Douleur, pouce, "
                      "soupe, soutien : le son « ou ». L'orthographe est fiable ici — "
                      "c'est l'oreille qui doit rattraper les yeux.",
            notes="Contrairement aux nasales, l'orthographe ne piège pas ici. Le "
                  "problème est purement articulatoire.")

    d.tableau('Analyse', "Deux sons, deux positions de bouche",
              ['Le son', 'Les lettres', 'La bouche', 'Mot repère'],
              [["le son « u »", "u, û", "lèvres arrondies, langue en avant", "brûlure"],
               ["le son « ou »", "ou, oû", "lèvres arrondies, langue en arrière", "douleur"]],
              cle=0,
              note="Les lèvres font la même chose dans les deux cas. C'est la langue qui "
                   "change de place, et elle ne se voit pas.",
              notes="C'est pour cela que le son « u » est si difficile : on ne peut pas "
                    "l'imiter en regardant. Il faut sentir la position de la langue.")

    d.cartes('La bouche', "Comment fabriquer le son « u »", [
        ("Étape 1 · dites « i »",
         "La langue monte à l'avant de la bouche, les lèvres sont plates et étirées. "
         "Gardez cette position de langue."),
        ("Étape 2 · arrondissez les lèvres",
         "Sans bouger la langue, arrondissez les lèvres comme pour dire « ou ». Le son "
         "qui sort est « u »."),
        ("Le contraste",
         "Pour « ou », la langue recule vers le fond. Pour « u », elle reste en avant. "
         "Les lèvres, elles, ne changent pas."),
        ("L'exercice qui marche",
         "Dites « i - u - i - u » dix fois, lentement. Seules les lèvres bougent. "
         "C'est le seul exercice qui installe vraiment ce son."),
    ], notes="Faire faire l'exercice de la quatrième carte par tout le groupe, en même "
             "temps. C'est bruyant et cela fonctionne.")

    d.pratique('Pratique · 1 de 3', "Quel son entendez-vous ?",
               "Écoutez le mot, écrivez « u » ou « ou ».", [
        ("brûlure", "le son « u »"),
        ("douleur", "le son « ou »"),
        ("urgence", "le son « u »"),
        ("pouce", "le son « ou »"),
        ("minute", "le son « u »"),
        ("soupe", "le son « ou »"),
        ("sucre", "le son « u »"),
        ("soutien", "le son « ou »"),
    ], corrige=True, cols=2,
       notes="Dire chaque mot deux fois, sans le montrer. Ne pas laisser voir "
             "l'orthographe avant la réponse.")

    d.tableau('Analyse', "Les paires qui se distinguent par ce seul son",
              ['Avec « u »', 'Avec « ou »', 'Deux mots différents'],
              [["su", "sou", "il a su · un sou"],
               ["pu", "pou", "il a pu · un pou"],
               ["rue", "roue", "une rue · une roue"],
               ["dessus", "dessous", "au-dessus · au-dessous"]],
              cle=2,
              notes="La dernière paire est celle qui compte au travail : « au-dessus » "
                    "et « au-dessous » sont des consignes de sécurité opposées.")

    d.piege('Le piège de « au-dessus »',
            "Mets ça au-dessous, quand on veut dire au-dessus",
            "au-dessus — le son « u » à la fin",
            "Ces deux mots disent le contraire l'un de l'autre, et un seul son les "
            "sépare. Dans une cuisine ou un entrepôt, cela change complètement une "
            "consigne. Quand vous n'êtes pas sûr d'être compris, montrez avec la main.",
            notes="Conseil pratique à donner : le geste double la parole. Ce n'est pas "
                  "un aveu de faiblesse, c'est ce que font tous les gens qui "
                  "travaillent dans le bruit.")

    d.regle('Le troisième de la famille',
            "Le son « i » s'écrit i, î ou y : cuisine, infirmière, plaie.",
            precision="Les trois sons — i, u, ou — se font tous avec la bouche presque "
                      "fermée. Le « i » a les lèvres étirées, le « u » et le « ou » les "
                      "ont arrondies. C'est le premier tri à faire.",
            notes="Faire dire « cuisine » : le mot contient « ui », donc les deux "
                  "premiers sons de la famille collés l'un à l'autre.")

    d.pratique('Pratique · 2 de 3', "Complétez avec u ou ou",
               "Un seul groupe de lettres par trou.", [
        ("la brûl___re (la blessure)", "brûlure — u"),
        ("la d___leur (ce qu'on sent)", "douleur — ou"),
        ("l'___rgence (le service de l'hôpital)", "urgence — u"),
        ("le p___ce (le premier doigt)", "pouce — ou"),
        ("la min___te (soixante secondes)", "minute — u"),
        ("le s___tien (l'aide qu'on reçoit)", "soutien — ou"),
    ], corrige=True,
       notes="Ici on va du son vers l'écriture. Laisser deux minutes de recherche avant "
             "de corriger.")

    d.pratique('Pratique · 3 de 3', "Trois phrases à lire à voix haute",
               "Chacun lit une phrase. Le groupe corrige les deux sons, rien d'autre.", [
        ("La brûlure de Fatou est douloureuse.", "u · ou · ou"),
        ("À l'urgence, l'infirmière a nettoyé la plaie en quinze minutes.", "u · i · u"),
        ("Il a mis son pouce sous l'eau froide.", "ou · ou · ou"),
    ], corrige=True,
       notes="Faire lire lentement et debout. La troisième phrase est un enchaînement de "
             "« ou » : c'est le meilleur test de la séance.")

    d.billet(
        "Écrivez quatre mots du module : deux avec le son « u », deux avec le son « ou ».",
        exemples=[
            "Soulignez la ou les lettres qui font le son.",
            "Exemple : « brûlure » — le son « u », lettre û.",
        ],
        notes="Corriger en circulant. Un élève qui écrit « douleur » dans la colonne du "
              "« u » n'entend pas encore la différence : le reprendre individuellement.")

    return d.save(dossier)
