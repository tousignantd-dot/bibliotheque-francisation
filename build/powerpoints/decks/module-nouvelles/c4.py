# -*- coding: utf-8 -*-
"""C4 · Avoir ou être ?
Bloc C · couleur ambre (écriture) · 75 min.
Source : exercice `t2auxiliaire` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre='Avoir ou être ?',
        chapeau="La question qui décide de tout : de l'auxiliaire dépend l'accord, et de "
                "l'accord dépend l'orthographe de la phrase entière. Trois listes "
                "suffisent à ne plus jamais se tromper.",
        duree='75 minutes')

    d.titre(notes="Séance de synthèse du passé composé. Prévenir : c'est la séance la "
                  "plus grammaticale du module, et celle qui sert le plus longtemps.")

    d.objectifs([
        "choisir entre avoir et être au passé composé ;",
        "connaître la liste des verbes qui prennent être ;",
        "savoir que tous les verbes pronominaux prennent être ;",
        "accorder le participe seulement quand il le faut.",
    ])

    d.tableau('Analyse', "Trois cas, trois auxiliaires",
              ['Le cas', "L'auxiliaire", 'Un exemple'],
              [["la plupart des verbes", "avoir", "il a parlé, ils ont amassé"],
               ["verbes de mouvement ou d'état", "être", "elle est arrivée, ils sont restés"],
               ["tous les verbes pronominaux", "être", "elle s'est levée, ils se sont rencontrés"]],
              cle=1, props=[0.35, 0.18, 0.47],
              notes="Trois cas seulement. Le premier couvre la grande majorité : c'est "
                    "avoir par défaut, être par exception.")

    d.regle('La règle par défaut',
            "Avoir, sauf pour deux familles de verbes.",
            precision="La grande majorité des verbes prennent avoir. Deux exceptions : "
                      "une courte liste de verbes de mouvement ou de changement d'état, "
                      "et tous les verbes pronominaux. Tout le reste prend avoir.",
            notes="Formuler ainsi soulage : il n'y a pas deux listes à apprendre, il y en "
                  "a une, et le reste est avoir.")

    d.tableau('Analyse', "Les verbes qui prennent être",
              ['Le mouvement', "Le changement d'état"],
              [["aller, venir, arriver, partir", "naître, mourir"],
               ["entrer, sortir, monter, descendre", "devenir, rester"],
               ["tomber, retourner, passer", "revenir, repartir"]],
              cle=0,
              note="Presque tous ont un contraire dans la liste : aller et venir, entrer "
                   "et sortir, monter et descendre. Cela aide à les retenir.",
              notes="Faire chercher les paires de contraires. C'est le meilleur moyen "
                    "mnémotechnique pour cette liste.")

    d.cartes('Ouvrir la mini-leçon', "Quatre pièges de l'auxiliaire", [
        ("« Passer » prend les deux",
         "« Je suis passé à la bibliothèque » (déplacement). « J'ai passé une "
         "radiographie » (faire quelque chose). Deux sens, deux auxiliaires."),
        ("« Monter » et « descendre » aussi",
         "« Elle est montée sur la scène » (elle se déplace). « Elle a monté les "
         "boîtes » (elle transporte quelque chose)."),
        ("Les pronominaux, sans exception",
         "Se lever, se rencontrer, se blesser, se sauver : tous avec être, dans tous "
         "les cas. C'est la seule règle sans exception du passé composé."),
        ("Avec avoir, jamais d'accord avec le sujet",
         "« Elle a organisé » — pas de e. C'est l'erreur la plus fréquente après "
         "l'apprentissage de l'accord avec être."),
    ], notes="Les deux premières cartes dépassent un peu le niveau. Les montrer et "
             "passer : les élèves les rencontreront en lisant.")

    d.pratique('Pratique · 1 de 4', "Avoir ou être ?",
               "La plupart prennent avoir. Cherchez les exceptions.", [
        ("Les élèves ___ décidé d'organiser une collecte.", "ont"),
        ("Elle ___ arrivée en retard au concours.", "est"),
        ("Mes voisins ___ déménagé le mois dernier.", "ont"),
        ("Une journaliste ___ venue filmer l'événement.", "est"),
        ("Samedi dernier, mon frère ___ invité toute la famille.", "a"),
        ("La tempête ___ retardé le concours d'une heure.", "a"),
    ], corrige=True,
       notes="Quatre sur six prennent avoir : c'est la proportion habituelle. Le faire "
             "remarquer pour rassurer.")

    d.pratique('Pratique · 2 de 4', "Quatre de plus",
               "Attention aux verbes pronominaux.", [
        ("Les sculptures ___ fondu à cause du redoux.", "ont fondu"),
        ("Les organisateurs ___ restés jusqu'à la fin.", "sont restés"),
        ("Le chat ___ sauvé par une fenêtre entrouverte.", "s'est sauvé — pronominal"),
        ("La voisine ___ averti la famille.", "a averti"),
    ], corrige=True,
       notes="Le troisième item est pronominal : « se sauver ». Sans le pronom, "
             "« sauver » prendrait avoir. Le signaler.")

    d.piege("Le piège du verbe qui ressemble",
            "Elle a arrivée hier.",
            "Elle est arrivée hier.",
            "« Arriver » est dans la liste des verbes de mouvement : il prend toujours "
            "être. L'erreur est fréquente parce que la grande majorité des verbes "
            "prennent avoir, et le réflexe l'emporte. Vérifiez la liste avant d'écrire.",
            notes="Faire réciter la liste des verbes de mouvement au début de chaque "
                  "exercice écrit, pendant quelques semaines.")

    d.piege("Le piège de l'accord avec avoir",
            "Elle a organisée la collecte.",
            "Elle a organisé la collecte.",
            "Avec l'auxiliaire avoir, le participe ne s'accorde pas avec le sujet. "
            "L'erreur vient de l'accord avec être, appris juste avant. La règle est "
            "simple : être accorde, avoir n'accorde pas.",
            notes="Écrire les deux phrases côte à côte : « elle est arrivée » et « elle a "
                  "organisé ». Même sujet, deux traitements opposés.")

    d.pratique('Pratique · 3 de 4', "Auxiliaire et accord",
               "Deux choses à décider pour chaque phrase.", [
        ("La fillette (retrouver) ___ son chat.", "a retrouvé — avoir, pas d'accord"),
        ("La fillette (sortir) ___ de la maison.", "est sortie — être, accord"),
        ("Les élèves (fabriquer) ___ des affiches.", "ont fabriqué — avoir, pas d'accord"),
        ("Les élèves (partir) ___ à midi.", "sont partis — être, accord"),
        ("La voisine (se lever) ___ tôt ce matin-là.", "s'est levée — pronominal, accord"),
    ], corrige=True,
       notes="Exercice apparié : même sujet, deux auxiliaires. C'est le contraste qui "
             "enseigne.")

    d.pratique('Pratique · 4 de 4', "Écrivez le fait divers",
               "Cinq phrases au passé composé, auxiliaires variés.", [
        ("Ce qui est arrivé", "Une fillette a retrouvé son chat."),
        ("Le début de l'histoire", "Le chat s'est sauvé il y a trois jours."),
        ("Ce que la classe a fait", "Sa classe a fabriqué des affiches."),
        ("Ce que la fillette a fait", "Elle est sortie les distribuer dans le quartier."),
        ("La fin", "Une voisine l'a reconnu et a averti la famille."),
    ], corrige=True,
       notes="Faire compter les auxiliaires : trois avoir, deux être. C'est la "
             "proportion normale d'un récit.")

    d.billet(
        "Racontez un événement en cinq phrases au passé composé.",
        exemples=[
            "Au moins une phrase avec l'auxiliaire être, accordée correctement.",
            "Au moins une phrase avec un verbe pronominal.",
        ],
        notes="Corriger l'auxiliaire d'abord, l'accord ensuite. Un auxiliaire juste avec "
              "un accord manqué vaut mieux que l'inverse.")

    return d.save(dossier)
