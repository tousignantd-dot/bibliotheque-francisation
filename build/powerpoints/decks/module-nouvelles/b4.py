# -*- coding: utf-8 -*-
"""B4 · La phrase passive.
Bloc B · couleur ambre (écriture) · 75 min.
Source : exercices `t1passive` et `t1activepassive`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre='La phrase passive',
        chapeau="« Les élèves ont organisé la collecte » ou « la collecte a été "
                "organisée par les élèves » ? Même événement, deux phrases — et la "
                "seconde est celle des journalistes.",
        duree='75 minutes')

    d.titre(notes="Écrire les deux phrases au tableau et demander laquelle on lirait dans "
                  "un journal. Le groupe choisira la seconde sans savoir pourquoi : "
                  "c'est la leçon.")

    d.objectifs([
        "reconnaître une phrase passive ;",
        "trouver qui fait l'action dans une phrase passive ;",
        "transformer une phrase active en phrase passive ;",
        "comprendre pourquoi les nouvelles emploient souvent le passif.",
    ])

    d.regle('La règle',
            "Dans une phrase passive, le sujet ne fait pas l'action : il la subit.",
            precision="« Les élèves ont organisé la collecte » : les élèves font "
                      "l'action. « La collecte a été organisée par les élèves » : la "
                      "collecte ne fait rien, elle subit l'action. Elle est pourtant "
                      "sujet de la phrase.",
            notes="Écrire la règle au tableau. Le test « qui fait l'action ? » est le "
                  "même qu'en B3 : le signaler.")

    d.tableau('Analyse', "Active et passive, côte à côte",
              ['Active', 'Passive'],
              [["Les élèves ont organisé la collecte.", "La collecte a été organisée par les élèves."],
               ["Une fillette a retrouvé le chat.", "Le chat a été retrouvé par une fillette."],
               ["La classe a fabriqué l'affiche.", "L'affiche a été fabriquée par la classe."]],
              cle=0,
              note="Ce qui était complément devient sujet, et celui qui fait l'action "
                   "passe après « par ».",
              notes="Faire tracer les flèches au tableau : le complément monte en tête, "
                    "le sujet descend après « par ».")

    d.tableau('Analyse', "Comment reconnaître une phrase passive",
              ['Le repère', 'Un exemple'],
              [["être + participe passé", "a été organisée, sont interviewés"],
               ["souvent « par » ensuite", "par les élèves, par le journaliste"],
               ["le sujet ne fait rien", "la collecte, le chat, l'affiche"]],
              cle=0,
              note="Les trois repères ne sont pas toujours réunis : « par » peut manquer "
                   "quand on ne sait pas qui a fait l'action.",
              notes="Le deuxième repère est le plus visible, mais le premier est le plus "
                    "fiable. Insister sur « être + participe passé ».")

    d.cartes('En apprendre plus', "Pourquoi les nouvelles emploient le passif", [
        ("Pour mettre l'événement en tête",
         "« La collecte a été organisée » commence par la collecte, qui est le sujet du "
         "reportage. C'est ce que le lecteur cherche."),
        ("Quand on ne sait pas qui a fait l'action",
         "« Le prix a été remis à l'équipe gagnante. » Qui l'a remis ? Le texte ne le "
         "dit pas, et ce n'est pas important."),
        ("Pour éviter d'accuser",
         "« Une erreur a été commise » ne dit pas qui. C'est un usage courant, et il "
         "vaut la peine de le remarquer en lisant."),
        ("Ce n'est pas plus poli",
         "Le passif n'est ni meilleur ni plus soigné. C'est un outil : il change ce "
         "qu'on met en tête de phrase."),
    ], notes="La troisième carte est une observation de lecture critique. La donner sans "
             "insister : elle éveille l'attention.")

    d.pratique('Pratique · 1 de 4', "Qui fait l'action ?",
               "Cherchez ce qui suit « par ». S'il n'y a rien, dites-le.", [
        ("Le chat a été retrouvé par une fillette de six ans.", "une fillette de six ans"),
        ("Les mitaines ont été amassées par les élèves.", "les élèves"),
        ("La sculpture a été admirée par des centaines de curieux.", "des centaines de curieux"),
        ("Le prix a été remis à l'équipe gagnante.", "non précisé"),
        ("L'affiche a été fabriquée par la classe de la fillette.", "la classe de la fillette"),
    ], corrige=True,
       notes="Le quatrième item est le plus instructif : « à l'équipe gagnante » n'est "
             "pas « par ». Faire remarquer la différence.")

    d.pratique('Pratique · 2 de 4', "Active ou passive ?",
               "Cherchez « être + participe passé ».", [
        ("Nous avons été invités par les organisateurs.", "passive"),
        ("Les gagnants du concours sont repartis très fiers.", "active"),
        ("Le chat s'est faufilé par la fenêtre entrouverte.", "active"),
        ("Les élèves de cette classe sont interviewés par le journaliste.", "passive"),
        ("Un bris de chauffage a causé une panne dans l'école.", "active"),
        ("La sculpture a été admirée par des centaines de visiteurs.", "passive"),
    ], corrige=True,
       notes="Les items 2 et 3 contiennent « sont » et « s'est » sans être passifs. "
             "C'est le piège de l'exercice : le corriger lentement.")

    d.piege("Le piège du « par » trompeur",
            "« Le chat s'est faufilé par la fenêtre » est une phrase passive.",
            "« Par » indique ici le passage, pas l'auteur de l'action.",
            "Le mot « par » a plusieurs emplois. Dans une phrase passive, il introduit "
            "celui qui fait l'action. Ailleurs, il indique un lieu de passage ou un "
            "moyen. Le vrai repère reste « être + participe passé ».",
            notes="Faire chercher trois emplois différents de « par » au tableau. La "
                  "distinction devient claire en deux minutes.")

    d.piege("Le piège du verbe de mouvement",
            "« Les gagnants sont repartis » est une phrase passive.",
            "« Sont repartis » est un passé composé avec l'auxiliaire être.",
            "Certains verbes forment leur passé composé avec « être » : partir, arriver, "
            "rester. Cela ne les rend pas passifs. Le test : est-ce que le sujet fait "
            "l'action ? Les gagnants repartent eux-mêmes, donc c'est actif.",
            notes="Lier au module 2, séance B2. C'est la difficulté la plus fine de la "
                  "séance : y consacrer du temps.")

    d.pratique('Pratique · 3 de 4', "Transformez en phrase passive",
               "Ce qui était complément devient sujet.", [
        ("Les élèves ont organisé la collecte.", "La collecte a été organisée par les élèves."),
        ("Une voisine a reconnu le chat.", "Le chat a été reconnu par une voisine."),
        ("Le jury a apprécié les détails.", "Les détails ont été appréciés par le jury."),
        ("Un enseignant a proposé le projet.", "Le projet a été proposé par un enseignant."),
    ], corrige=True,
       notes="Faire vérifier l'accord du participe passé avec le nouveau sujet. C'est le "
             "point d'écriture de l'exercice.")

    d.pratique('Pratique · 4 de 4', "Transformez en phrase active",
               "Celui qui suit « par » redevient sujet.", [
        ("Le documentaire a été proposé par l'enseignant.", "L'enseignant a proposé le documentaire."),
        ("Les mitaines ont été amassées par les élèves.", "Les élèves ont amassé les mitaines."),
        ("La sculpture a été admirée par des visiteurs.", "Des visiteurs ont admiré la sculpture."),
        ("Le prix a été remis à l'équipe gagnante.",
         "impossible — on ne sait pas qui a remis le prix"),
    ], corrige=True,
       notes="Le dernier item est volontairement impossible. C'est ce qui montre à quoi "
             "sert le passif : dire une action sans nommer son auteur.")

    d.billet(
        "Écrivez deux phrases passives sur une nouvelle du module.",
        exemples=[
            "Une avec « par », une sans.",
            "Soulignez « être + participe passé » dans chacune.",
        ],
        notes="Corriger l'accord du participe avec le sujet. Rendre avant C3, où le même "
              "accord reviendra avec l'auxiliaire être du passé composé.")

    return d.save(dossier)
