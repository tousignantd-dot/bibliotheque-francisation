# -*- coding: utf-8 -*-
"""B2 · Le passé composé.
Bloc B · couleur ambre (écriture) · 90 min.
Source : exercice `t1pc` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre='Le passé composé',
        chapeau="« L'huile a éclaboussé », « elle est arrivée » : deux verbes au passé, "
                "deux auxiliaires différents. Choisir le bon est la difficulté centrale "
                "du module.",
        duree='90 minutes')

    d.titre(notes="Séance longue et centrale. Prévoir une pause au milieu, après "
                  "l'auxiliaire être. Ne pas essayer d'aller plus vite : c'est le savoir "
                  "que tout le module réutilise.")

    d.objectifs([
        "former un passé composé : auxiliaire au présent + participe passé ;",
        "choisir entre avoir et être ;",
        "accorder le participe passé quand l'auxiliaire est être ;",
        "raconter un accident au passé composé.",
    ])

    d.regle('La formation',
            "Auxiliaire au présent, puis participe passé. Deux mots, toujours.",
            precision="J'ai appelé. Elle est arrivée. Le premier mot dit qui et quand, "
                      "le second dit quoi. On ne peut jamais en enlever un.",
            notes="Écrire les deux moitiés au tableau, dans deux couleurs. Beaucoup "
                  "d'élèves écrivent « j'appelé » ou « elle arrivée » : l'auxiliaire "
                  "manquant est l'erreur la plus fréquente.")

    d.tableau('Analyse', "La grande majorité des verbes : avoir",
              ['La personne', 'La forme', 'Un exemple'],
              [["je", "j'ai appelé", "J'ai appelé Info-Santé."],
               ["tu", "tu as mis", "Tu as mis de l'eau froide."],
               ["il, elle", "elle a éclaboussé", "L'huile a éclaboussé son bras."],
               ["nous", "nous avons mis", "Nous avons mis le bras sous l'eau."],
               ["vous", "vous avez percé", "Vous avez percé la cloque ?"]],
              cle=1,
              notes="Avec avoir, le participe ne change jamais de forme. C'est le cas le "
                    "plus simple : commencer par lui et l'installer solidement.")

    d.regle("Le petit groupe qui prend être",
            "Aller, venir, arriver, partir, entrer, sortir, monter, descendre, tomber, rester, naître, mourir.",
            precision="Ce sont presque tous des verbes de déplacement ou de changement "
                      "d'état. Ils sont peu nombreux, et ils reviennent constamment : il "
                      "faut les connaître par cœur.",
            notes="Écrire la liste au tableau et la laisser toute la séance. Ne pas "
                  "chercher de règle : c'est une liste, elle s'apprend comme telle.")

    d.tableau('Analyse', "Avec être, le participe s'accorde",
              ['Le sujet', 'La forme', 'La marque'],
              [["il", "il est arrivé", "rien"],
               ["elle", "elle est arrivée", "un e"],
               ["ils", "ils sont arrivés", "un s"],
               ["elles", "elles sont arrivées", "un e et un s"]],
              cle=2,
              note="Le participe se comporte comme un adjectif : il s'accorde avec le "
                   "sujet, en genre et en nombre.",
              notes="Relier à l'accord de l'adjectif travaillé en A4. C'est exactement la "
                    "même logique, appliquée à un autre mot.")

    d.cartes('En apprendre plus', "Quatre choses à savoir en plus", [
        ("Avec avoir, pas d'accord avec le sujet",
         "« Elle a mis » — pas de e. Beaucoup d'élèves accordent par réflexe. Avec "
         "avoir, le participe ne bouge pas."),
        ("Les participes irréguliers",
         "Mettre donne mis, prendre donne pris, faire donne fait, voir donne vu. Ils "
         "s'apprennent un par un, comme du vocabulaire."),
        ("La négation encadre l'auxiliaire",
         "« Je n'ai pas appelé » — ne et pas entourent « ai », pas le participe. Le "
         "verbe conjugué, c'est l'auxiliaire."),
        ("Passer peut prendre les deux",
         "« Je suis passé à l'urgence » (déplacement) ou « j'ai passé une radiographie » "
         "(faire quelque chose). Deux sens, deux auxiliaires."),
    ], notes="La troisième carte est très utile et rarement enseignée : elle relie le "
             "passé composé à la négation du module 1.")

    d.pratique('Pratique · 1 de 4', "Avoir ou être ?",
               "Choisissez l'auxiliaire avant d'écrire le participe.", [
        ("L'huile (éclabousser) ___ son avant-bras.", "a éclaboussé — avoir"),
        ("Mathieu (appeler) ___ Info-Santé.", "a appelé — avoir"),
        ("Fatou (arriver) ___ à l'urgence vers midi.", "est arrivée — être, accord"),
        ("Nous (mettre) ___ le bras sous l'eau froide.", "avons mis — avoir"),
        ("Les secours (partir) ___ tout de suite.", "sont partis — être, accord"),
        ("Le médecin (nettoyer) ___ la plaie.", "a nettoyé — avoir"),
    ], corrige=True,
       notes="Faire nommer l'auxiliaire à voix haute avant d'écrire. C'est ce choix qui "
             "détermine tout le reste.")

    d.piege("Le piège de l'auxiliaire oublié",
            "Elle arrivée à l'urgence.",
            "Elle est arrivée à l'urgence.",
            "Le passé composé est fait de deux mots. Sans l'auxiliaire, il ne reste "
            "qu'un participe, qui fonctionne comme un adjectif : « elle arrivée » ne "
            "veut rien dire. C'est l'erreur la plus fréquente à l'écrit et elle vient "
            "de ce qu'on n'entend presque pas « est » dans la phrase parlée.",
            notes="Faire lire la phrase fautive à voix haute : le groupe entendra qu'il "
                  "manque quelque chose, même sans savoir quoi.")

    d.piege("Le piège de l'accord avec avoir",
            "Elle a mise le bras sous l'eau.",
            "Elle a mis le bras sous l'eau.",
            "Avec l'auxiliaire avoir, le participe ne s'accorde pas avec le sujet. Le "
            "réflexe d'accorder vient de l'auxiliaire être, où l'accord est obligatoire. "
            "La règle est simple : être accorde, avoir n'accorde pas.",
            notes="Écrire les deux phrases côte à côte : « elle est arrivée » et « elle "
                  "a mis ». Le même sujet, deux traitements opposés.")

    d.pratique('Pratique · 2 de 4', "Accordez le participe",
               "L'auxiliaire est donné. Accordez seulement quand c'est être.", [
        ("Elle est (arriver) ___ à onze heures.", "arrivée"),
        ("Elle a (mettre) ___ son bras sous l'eau.", "mis — pas d'accord"),
        ("Ils sont (partir) ___ en ambulance.", "partis"),
        ("Ils ont (appeler) ___ le 911.", "appelé — pas d'accord"),
        ("Les infirmières sont (rester) ___ avec elle.", "restées"),
        ("Les infirmières ont (poser) ___ un pansement.", "posé — pas d'accord"),
    ], corrige=True,
       notes="Les items sont appariés deux par deux : même sujet, deux auxiliaires. "
             "Corriger par paires pour que le contraste soit visible.")

    d.tableau('Analyse', "Six participes irréguliers du module",
              ['Le verbe', 'Le participe', 'Un exemple'],
              [["mettre", "mis", "j'ai mis de l'eau froide"],
               ["prendre", "pris", "il a pris ma tension"],
               ["faire", "fait", "on a fait une radiographie"],
               ["voir", "vu", "j'ai vu le médecin"],
               ["dire", "dit", "elle m'a dit de ne pas y toucher"],
               ["venir", "venu", "elle est venue me chercher"]],
              cle=1,
              notes="Les cinq premiers prennent avoir, le dernier prend être. Le faire "
                    "remarquer : « venir » est dans la liste des verbes de déplacement.")

    d.pratique('Pratique · 3 de 4', "Mettez au passé composé",
               "Attention aux participes irréguliers.", [
        ("Je mets mon bras sous l'eau froide.", "J'ai mis mon bras sous l'eau froide."),
        ("Elle vient me chercher à l'hôpital.", "Elle est venue me chercher à l'hôpital."),
        ("Nous faisons une radiographie.", "Nous avons fait une radiographie."),
        ("Ils voient le médecin à midi.", "Ils ont vu le médecin à midi."),
        ("L'infirmière dit de ne rien percer.", "L'infirmière a dit de ne rien percer."),
    ], corrige=True,
       notes="Exercice de transformation. Faire souligner l'auxiliaire dans chaque "
             "réponse avant de corriger le participe.")

    d.pratique('Pratique · 4 de 4', "Racontez au passé composé",
               "Trois phrases par situation, toutes au passé composé.", [
        ("L'accident de Fatou",
         "L'huile a éclaboussé son bras. Elle a mis son bras sous l'eau froide. "
         "Elle est arrivée à l'urgence vers midi."),
        ("Votre propre journée d'hier",
         "Réponse personnelle — au moins un verbe avec être."),
        ("Une visite à l'hôpital",
         "Je suis arrivé à l'accueil. J'ai attendu deux heures. Le médecin m'a vu."),
    ], corrige=True,
       notes="Le deuxième item est libre : c'est celui qui montre si le savoir est "
             "transférable. Circuler et corriger individuellement.")

    d.billet(
        "Écrivez trois phrases au passé composé sur une journée de travail.",
        exemples=[
            "Au moins une avec l'auxiliaire être, et accordée correctement.",
            "Soulignez l'auxiliaire dans chaque phrase.",
        ],
        notes="Corriger les billets en dehors du cours et rendre à la séance suivante : "
              "cette notion demande une rétroaction individuelle.")

    return d.save(dossier)
