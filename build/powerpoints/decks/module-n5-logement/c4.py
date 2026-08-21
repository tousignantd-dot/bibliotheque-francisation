# -*- coding: utf-8 -*-
"""C4 · Le gérondif : en visitant, en écoutant.
Bloc C « Défi 2 · La visite » · couleur ambre · 75 min.
Source : exercice `t2gerondif` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre="Le gérondif : en visitant, en écoutant",
        chapeau="« Elle prend des notes en écoutant la propriétaire. » Une "
                "seule personne, deux actions en même temps. Et la même forme "
                "sert à dire comment on fait quelque chose.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire. Le gérondif est explicitement au programme du "
                  "niveau 5 — exprimer la simultanéité et la manière — et il ferme le "
                  "défi 2.")

    d.objectifs([
        "former un gérondif à partir de la personne « nous » ;",
        "exprimer deux actions en même temps ;",
        "exprimer la manière : comment on fait quelque chose ;",
        "vérifier que les deux verbes ont le même sujet.",
    ])

    d.declencheur(
        'Observation', "Que fait Nadège, exactement ?",
        pistes=[
            "« Elle prend des notes en écoutant la propriétaire. »",
            "Combien d'actions y a-t-il dans cette phrase ?",
            "Qui fait la première ? Qui fait la seconde ?",
            "Est-ce que ce sont deux personnes différentes ?",
        ],
        notes="Faire compter les actions — deux — et les acteurs — un seul. C'est la "
              "condition d'emploi du gérondif, et elle se découvre bien mieux ainsi qu'en "
              "l'annonçant.")

    d.regle("En + le verbe en -ant",
            "On part de la personne « nous » au présent, on enlève -ons, on ajoute -ant.",
            precision="nous regardONS donne en regardANT · nous finissONS donne en finissANT · "
                      "nous prenONS donne en prenANT. Cette règle vaut pour toute la langue, y "
                      "compris pour les verbes irréguliers au singulier : c'est la forme "
                      "« nous » qui porte le bon radical.",
            notes="Diapositive à photographier. Faire conjuguer trois verbes au « nous » "
                  "avant d'appliquer la règle : c'est l'étape que les élèves sautent.")

    d.tableau('La formation', "Cinq verbes du module",
              ['La personne « nous »', 'Le gérondif'],
              [["nous regardons", "en regardant"],
               ["nous finissons", "en finissant"],
               ["nous prenons", "en prenant"],
               ["nous lisons", "en lisant"],
               ["nous arrivons", "en arrivant"]],
              cle=0,
              note="Trois irréguliers seulement : être donne en étant · avoir donne en ayant · savoir donne en sachant.",
              notes="Diapositive à photographier. Insister sur la note : trois exceptions "
                    "dans toute la langue, c'est peu, et ça se retient.")

    d.cartes("Deux emplois", "La même forme, deux usages", [
        ("La simultanéité",
         "Deux actions en même temps : « Elle prend des notes en écoutant. »"),
        ("La manière",
         "Comment on fait : « On apprend le vrai prix en posant des questions. »"),
        ("En tête de phrase",
         "« En arrivant, vous avez vu la ruelle. » Le sens est le même."),
        ("Jamais d'accord",
         "Le gérondif ne change jamais de forme, ni en genre ni en nombre."),
    ], notes="La quatrième carte prévient l'erreur « en visitants ». Le gérondif est "
             "invariable, sans exception.")

    d.piege("Deux sujets différents",
            "En arrivant, la ruelle était bruyante.",
            "En arrivant, vous avez vu la ruelle.",
            "La ruelle n'arrive pas. Le gérondif exige que les deux verbes aient le même "
            "sujet. Si les sujets diffèrent, il faut « quand » ou « pendant que » : "
            "« Quand vous êtes arrivée, la ruelle était bruyante. »",
            notes="C'est le seul vrai piège du gérondif, et il produit des phrases qui "
                  "sonnent bien mais ne veulent pas dire ce qu'on croit. Faire trouver "
                  "d'autres exemples fautifs au groupe : ils s'en amusent.")

    d.pratique('Formation', "Écrivez le gérondif",
               "Passez par la personne « nous ».", [
        ("regarder", "nous regardons donne en regardant"),
        ("finir", "nous finissons donne en finissant"),
        ("prendre", "nous prenons donne en prenant"),
        ("relire", "nous relisons donne en relisant"),
        ("poser", "nous posons donne en posant"),
        ("être", "en étant — irrégulier"),
        ("avoir", "en ayant — irrégulier"),
        ("savoir", "en sachant — irrégulier"),
    ], corrige=True,
       notes="Exiger que la forme « nous » soit écrite avant le gérondif : c'est elle qui "
             "garantit le radical, et l'élève qui la saute se trompe sur « prendre ».")

    d.pratique('Application', "Complétez avec un gérondif",
               "Le verbe est entre parenthèses.", [
        ("Elle prend des notes … (écouter) la propriétaire.", "en écoutant"),
        ("… (arriver), on voit tout de suite la ruelle.", "En arrivant"),
        ("On apprend le vrai prix … (poser) des questions.", "en posant"),
        ("Elle a comparé les logements … (regarder) ses trois fiches.", "en regardant"),
        ("Il a compris l'avis … (relire) le papier lentement.", "en relisant"),
        ("On évite les surprises … (être) précis au téléphone.", "en étant"),
        ("Elle a signé … (savoir) ce qu'elle acceptait.", "en sachant"),
    ], corrige=True,
       notes="Pour chaque phrase, faire nommer l'emploi : simultanéité ou manière. Les "
             "trois dernières sont des manières.")

    d.pratique('Production', "Donnez trois conseils avec un gérondif",
               "À quelqu'un qui cherche un logement pour la première fois.", [
        ("Un conseil sur l'appel", "On gagne du temps en préparant ses questions."),
        ("Un conseil sur la visite", "On voit les vrais défauts en ouvrant les fenêtres."),
        ("Un conseil sur le bail", "On évite les surprises en lisant l'annexe."),
    ], corrige=False,
       notes="Exercice de production libre. Les trois conseils résument le module : c'est "
             "l'occasion de faire le point sur les défis 1 et 2 avant d'entrer dans le bail.")

    d.billet(
        "Écrivez cinq conseils à quelqu'un qui cherche un logement.",
        exemples=[
            "Chacun avec un gérondif.",
            "« On évite les mauvaises surprises en… »",
        ],
        notes="Devoir d'écriture. Les meilleurs conseils seront affichés en classe : c'est "
              "un document utile aux prochains groupes, et les élèves le savent.")

    return d.save(dossier)
