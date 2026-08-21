# -*- coding: utf-8 -*-
"""B2 · Je tousse, j'ai de la fièvre, je me suis coupé.
Bloc B « Défi 1 · Dire ce qui ne va pas » · couleur teal · 75 min.
Source : exercices `t1symptomes` et `t1decrire`, mini-leçon `t1decrire`.

Les verbes viennent tous de la liste que le programme rattache à cette
situation : tousser, avoir de la fièvre, se couper, s'étouffer, se faire mal,
consulter, questionner, administrer, persister, rincer.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='teal',
        titre="Je tousse, j'ai de la fièvre, je me suis coupé",
        chapeau="Six verbes règlent presque tout ce qu'on dit d'un malaise. "
                "Trois se disent au présent parce que ça dure ; trois au passé "
                "parce que c'est arrivé.",
        duree='75 minutes')

    d.titre(notes="Séance de langue orale. Les verbes de la séance sont exactement ceux "
                  "de la liste du programme : ne pas en ajouter, ils sont déjà "
                  "nombreux pour un débutant.")

    d.objectifs([
        "nommer un malaise avec le bon verbe ;",
        "choisir entre le présent et le passé composé ;",
        "comprendre « persister », « consulter » et « administrer » ;",
        "dire trois malaises différents à voix haute.",
    ])

    d.declencheur(
        'Mise en situation', "Comment dites-vous ce qui ne va pas ?",
        pistes=[
            "Est-ce que ça dure encore, ou est-ce arrivé une fois ?",
            "Quelle différence entre « je tousse » et « j'ai toussé » ?",
            "Quels malaises connaissez-vous déjà nommer en français ?",
        ],
        notes="La distinction entre ce qui dure et ce qui est arrivé est le cœur de la "
              "séance. La poser dès le départ, sans grammaire : « c'est fini ? ça "
              "continue ? »")

    d.tableau('Analyse', "Ce qui dure, et ce qui est arrivé",
              ["Ça dure encore — le présent", "C'est arrivé — le passé composé"],
              [["je tousse", "je me suis coupé le doigt"],
               ["j'ai de la fièvre", "je me suis fait mal au genou"],
               ["j'ai mal à la gorge", "je suis tombée dans l'escalier"],
               ["ça persiste", "ça a commencé samedi"]],
              cle=0,
              note="Les verbes de droite se construisent tous avec être.",
              notes="Diapositive à photographier. Insister sur « je me suis » : c'est la "
                    "forme la plus utile de la colonne de droite, et la plus fautive.")

    d.regle("Un accident déjà arrivé",
            "« Je me suis coupé le doigt. »",
            precision="Le petit mot « me » dit que c'est votre doigt : on garde "
                      "donc « le doigt », pas « mon doigt ». Et l'auxiliaire est "
                      "toujours être : je me suis coupé, je me suis fait mal.",
            notes="Diapositive à photographier. La construction est très différente de "
                  "l'anglais et de plusieurs autres langues : prévoir du temps.")

    d.cartes("Les verbes du malaise", "Six verbes du programme", [
        ("tousser",
         "Faire un bruit fort avec la gorge, sans le vouloir. « Je tousse depuis quatre "
         "jours » : c'est la phrase la plus dite au comptoir en hiver."),
        ("avoir de la fièvre",
         "Avoir le corps trop chaud. On dit « j'ai de la fièvre », jamais « je suis "
         "fièvre » — comme « j'ai faim » et « j'ai froid »."),
        ("se couper, se faire mal",
         "Deux accidents, deux phrases au passé : « je me suis coupé », « je me suis "
         "fait mal au genou »."),
        ("persister",
         "Continuer, ne pas partir. C'est le mot du pharmacien : « si ça persiste, "
         "consultez un médecin »."),
    ], notes="Faire employer chaque verbe dans une phrase avant de passer au suivant. "
             "Les quatre reviennent dans la production orale de la séance E1.")

    d.piege('Construction',
            "« j'ai coupé mon doigt »",
            "« je me suis coupé le doigt »",
            "La phrase calquée sur l'anglais se comprend, mais elle sonne étrange et "
            "elle laisse croire à un geste volontaire. La forme juste met « me » devant "
            "et garde l'article : le doigt, la main, le genou.",
            notes="Faire barrer la forme fautive au tableau par un élève, puis faire "
                  "produire trois phrases justes par trois élèves différents.")

    d.pratique('Association', "Le malaise et la phrase",
               "Dites la phrase qui convient à chaque situation.", [
        ("Votre corps est trop chaud, vous avez 38,5 degrés.", "« J'ai de la fièvre depuis hier. »"),
        ("Vous faites un bruit fort avec la gorge, surtout la nuit.", "« Je tousse et je ne dors pas. »"),
        ("Vous vous êtes coupé en préparant le souper.", "« Je me suis coupé le doigt. »"),
        ("Vous êtes tombé et votre genou est enflé.", "« Je me suis fait mal au genou. »"),
        ("Votre nez coule depuis trois jours.", "« Je pense que j'ai un rhume. »"),
    ], corrige=True,
       notes="Reprend l'exercice interactif `t1symptomes`. Faire dire les phrases "
             "debout, à voix haute : c'est de la production orale, pas de la lecture.")

    d.pratique('Application', "Le bon verbe, à la bonne forme",
               "Complétez chaque phrase.", [
        ("Depuis samedi, je ___ beaucoup la nuit. (tousser)", "tousse"),
        ("Mon garçon ___ de la fièvre depuis hier soir. (avoir)", "a"),
        ("Hier, je me suis ___ le doigt avec un couteau. (couper)", "coupé"),
        ("La toux ___ depuis plus de sept jours. (persister)", "persiste"),
        ("Si la fièvre revient, il faut ___ un médecin. (consulter)", "consulter"),
    ], corrige=True,
       notes="Les items de l'exercice interactif. Faire remarquer que « consulter » "
             "reste à l'infinitif après « il faut » : la séance C2 y reviendra.")

    d.billet(
        "Écrivez trois phrases : deux au présent, une au passé composé.",
        exemples=[
            "Ce qui dure : je tousse, j'ai mal à…",
            "Ce qui est arrivé : je me suis coupé, je me suis fait mal…",
        ],
        notes="Devoir court. Ramasser et relever seulement l'auxiliaire du passé "
              "composé : c'est la faute à corriger cette semaine.")

    return d.save(dossier)
