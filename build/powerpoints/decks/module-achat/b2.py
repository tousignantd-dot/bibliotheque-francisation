# -*- coding: utf-8 -*-
"""B2 · Où mettre l'adjectif.
Bloc B · couleur ambre (écriture) · 75 min.
Source : mini-leçon `t1adj`, exercice `t1adj`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre="Où mettre l'adjectif",
        chapeau="« Une laveuse silencieuse », pas « une silencieuse laveuse ». "
                "En français, l'adjectif suit le nom — sauf une petite liste "
                "qu'on apprend par cœur.",
        duree='75 minutes')

    d.titre(notes="Écrire les deux formes du chapeau au tableau et demander laquelle sonne "
                  "juste. Le groupe entend la différence même sans connaître la règle.")

    d.objectifs([
        "placer l'adjectif après le nom, par défaut ;",
        "connaître la petite famille qui précède ;",
        "accorder l'adjectif en genre et en nombre ;",
        "décrire un appareil en trois adjectifs.",
    ])

    d.tableau('Analyse', "Après, sauf une petite liste",
              ['Position', 'Exemples'],
              [["Après le nom (la règle)", "silencieux, économe, récent, frontal, blanc"],
               ["Avant le nom (la liste)", "grand, petit, gros, beau, bon"],
               ["Avant aussi", "nouveau, vieux, jeune, joli, premier, dernier"]],
              cle=0,
              note="Une dizaine d'adjectifs précèdent. Tous les autres suivent.",
              notes="Diapo centrale. Faire recopier la liste : elle s'apprend comme une "
                    "liste, pas comme une règle.")

    d.regle("La règle par défaut",
            "Dans le doute, mettez l'adjectif après le nom.",
            precision="Vous aurez raison neuf fois sur dix. C'est l'inverse de l'anglais, "
                      "du chinois et de plusieurs autres langues — d'où l'erreur "
                      "fréquente. « Une laveuse silencieuse », « un appareil économe », "
                      "« un modèle récent ».",
            notes="Diapo à photographier. Elle suffit à la majorité des cas.")

    d.regle("L'accord en genre et en nombre",
            "L'adjectif prend la forme du nom qu'il décrit.",
            precision="un appareil silencieu<b>x</b> · une laveuse silencieu<b>se</b> · "
                      "des modèles récent<b>s</b> · des laveuses silencieu<b>ses</b>. "
                      "Au féminin, la fin du mot change souvent — et ça s'entend.",
            notes="Faire produire les quatre formes de « silencieux » à voix haute. La "
                  "différence sonore est nette au féminin.")

    d.cartes('Cinq féminins irréguliers', "À connaître par cœur", [
        ("nouveau › nouvelle",
         "« une nouvelle laveuse ». Attention aussi à « nouvel » devant une voyelle : "
         "« un nouvel appareil »."),
        ("beau › belle · vieux › vieille",
         "Même famille, même irrégularité. Et « bel appareil », « vieil appareil » devant "
         "une voyelle."),
        ("blanc › blanche · sec › sèche",
         "La consonne finale change de forme au féminin."),
        ("complet › complète",
         "« une garantie complète ». Le -et devient -ète."),
    ], notes="Ces cinq-là couvrent presque tous les cas rencontrés dans un magasin "
             "d'électroménagers.")

    d.piege("Placer l'adjectif avant le nom",
            "une silencieuse laveuse",
            "une laveuse silencieuse",
            "Cette place est celle de l'anglais et de plusieurs autres langues. En "
            "français, elle est réservée à une dizaine d'adjectifs très courants. Employée "
            "ailleurs, elle sonne poétique ou étrange — jamais neutre.",
            notes="Ne pas dire que c'est une faute grave : c'est compris, mais ça se "
                  "remarque.")

    d.pratique('Pratique · 1 de 2', "Place et forme",
               "Mettez l'adjectif à la bonne place et à la bonne forme.", [
        ("une laveuse (silencieux)", "une laveuse silencieuse"),
        ("un appareil (économe)", "un appareil économe"),
        ("des modèles (récent)", "des modèles récents"),
        ("un réfrigérateur (petit)", "un petit réfrigérateur"),
        ("le modèle (dernier)", "le dernier modèle"),
        ("une garantie (complet)", "une garantie complète"),
    ], corrige=True,
       notes="Faire dire à chaque ligne : est-il dans la liste, oui ou non ?")

    d.pratique('Pratique · 2 de 2', "Décrivez en trois adjectifs",
               "Écrivez une phrase complète pour chaque appareil.", [
        ("Une laveuse : 68 cm, 52 dB, économe en eau", "C'est une petite laveuse silencieuse et économe."),
        ("Un réfrigérateur : 145 cm, 300 kWh, récent", "C'est un grand réfrigérateur récent et économe."),
        ("Une cuisinière : 76 cm, vitrocéramique, facile à nettoyer", "C'est une cuisinière vitrocéramique, facile à nettoyer."),
    ], corrige=True, cols=1,
       notes="Plusieurs formulations sont bonnes. Vérifier la place et l'accord, pas le "
             "choix des mots.")

    d.billet(
        "Décrivez trois appareils de chez vous, en trois adjectifs chacun.",
        exemples=[
            "Au moins un adjectif de la liste qui précède le nom.",
            "Vérifiez chaque accord au féminin.",
        ],
        notes="Corriger individuellement. Ces descriptions sont le brouillon de la "
              "production orale de E1.")

    return d.save(dossier)
