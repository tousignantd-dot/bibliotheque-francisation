# -*- coding: utf-8 -*-
"""C3 · Le gérondif : en suivant les étapes.
Bloc C · couleur ambre (écriture) · 75 min.
Source : exercice `t2gerond` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre='En suivant les étapes',
        chapeau="« Il a réglé le problème en appelant les finances. » Un seul mot — "
                "« en » — et le verbe qui suit dit comment on a fait, ou ce qu'on "
                "faisait en même temps.",
        duree='75 minutes')

    d.titre(notes="Écrire la phrase du chapeau au tableau et demander ce que « en "
                  "appelant » ajoute. Le groupe répondra « comment il a fait » : c'est "
                  "la moitié de la leçon.")

    d.objectifs([
        "former un gérondif : en + le verbe en -ant ;",
        "distinguer la simultanéité de la manière ;",
        "employer le gérondif quand les deux actions ont le même sujet ;",
        "choisir entre « pendant que » et le gérondif.",
    ])

    d.regle('La formation',
            "En + le verbe avec la terminaison -ant.",
            precision="Suivre donne en suivant. Lire donne en lisant. Attendre donne en "
                      "attendant. On part de la forme « nous » du présent, on enlève "
                      "-ons et on ajoute -ant : nous suivons donne suivant.",
            notes="Écrire la méthode au tableau : nous suivons, moins -ons, plus -ant. "
                  "Elle fonctionne pour presque tous les verbes.")

    d.tableau('Analyse', "Deux sens, un seul outil",
              ['Le sens', 'Ce qu\'il répond', 'Un exemple'],
              [["la simultanéité", "quand ?", "Il lit ses courriels en attendant l'ascenseur."],
               ["la manière", "comment ?", "Elle a réglé le problème en appelant les finances."]],
              cle=0,
              note="Pour trancher, posez la question : est-ce que ça dit quand, ou "
                   "comment ?",
              notes="Écrire les deux questions au tableau. Elles servent à tous les "
                    "exercices de la séance.")

    d.cartes('Analyse', "Comment reconnaître le sens", [
        ("Le test du « comment »",
         "« Comment a-t-elle réglé le problème ? En appelant les finances. » Si la "
         "réponse fonctionne, c'est la manière."),
        ("Le test du « en même temps »",
         "« Il lit ses courriels et il attend l'ascenseur en même temps. » Si cela "
         "fonctionne, c'est la simultanéité."),
        ("Le verbe principal donne un indice",
         "Un verbe de résultat — régler, trouver, corriger, réussir — annonce presque "
         "toujours la manière."),
        ("Un verbe d'état ou de durée",
         "Travailler, parler, marcher, discuter : ce sont des actions qui durent, donc "
         "souvent de la simultanéité."),
    ], notes="Les deux dernières cartes donnent un raccourci fiable, mais pas infaillible. "
             "Les tests des deux premières restent le critère.")

    d.pratique('Pratique · 1 de 4', "Simultanéité ou manière ?",
               "Posez la question : quand, ou comment ?", [
        ("Samuel remplit le formulaire en suivant les étapes.", "manière — comment"),
        ("Diane a trouvé la réponse en lisant la directive.", "manière — comment"),
        ("Il parle à son collègue en attendant son tour.", "simultanéité — quand"),
        ("Elle travaille en écoutant une baladodiffusion.", "simultanéité — quand"),
        ("Le technicien a réglé le problème en vérifiant chaque pièce.", "manière"),
        ("La commis a corrigé l'erreur en relisant le formulaire.", "manière"),
    ], corrige=True,
       notes="Faire poser la question à voix haute avant chaque réponse. Sans elle, "
             "l'exercice devient une intuition.")

    d.pratique('Pratique · 2 de 4', "Formez le gérondif",
               "Partez de la forme « nous » du présent.", [
        ("suivre (nous suivons)", "en suivant"),
        ("lire (nous lisons)", "en lisant"),
        ("attendre (nous attendons)", "en attendant"),
        ("remplir (nous remplissons)", "en remplissant"),
        ("choisir (nous choisissons)", "en choisissant"),
        ("appuyer (nous appuyons)", "en appuyant"),
    ], corrige=True,
       notes="Les trois derniers sont ceux du module : remplir, choisir, appuyer. Les "
             "faire employer dans une phrase après correction.")

    d.regle('Gérondif ou « pendant que » ?',
            "Le gérondif quand c'est la même personne. « Pendant que » quand ce sont deux personnes.",
            precision="« Il attend l'approbation en continuant son travail » — c'est lui "
                      "qui fait les deux. « Il attend l'approbation pendant que la "
                      "commis vérifie » — deux personnes, donc « pendant que ».",
            notes="Diapo charnière. Faire transformer trois phrases de C2 en gérondif et "
                  "constater lesquelles fonctionnent.")

    d.piege("Le piège du sujet différent",
            "Je remplis le formulaire en prenant la photo, toi.",
            "Je remplis le formulaire pendant que tu prends la photo.",
            "Le gérondif se rapporte toujours au sujet de la phrase principale. « En "
            "prenant la photo » voudrait dire que c'est moi qui la prends. Quand ce sont "
            "deux personnes différentes, il faut « pendant que ».",
            notes="Erreur logique plus que grammaticale, et elle change le sens sans "
                  "qu'on s'en aperçoive. Y consacrer du temps.")

    d.piege("Le piège de la terminaison",
            "en remplisant le formulaire",
            "en remplissant le formulaire",
            "Le gérondif se forme sur la forme « nous » du présent : nous remplissons, "
            "donc en remplissant, avec deux s. Ceux qui partent de l'infinitif écrivent "
            "« remplisant » et se trompent. Passez toujours par « nous ».",
            notes="Faire écrire au tableau la chaîne complète pour trois verbes : "
                  "infinitif, forme nous, gérondif.")

    d.pratique('Pratique · 3 de 4', "Gérondif ou pendant que ?",
               "Combien de personnes font les actions ?", [
        ("Il attend l'approbation. Il continue son travail.",
         "gérondif — même personne : il attend en continuant son travail"),
        ("Je remplis le formulaire. Tu prends la photo.",
         "pendant que — deux personnes"),
        ("Elle vérifie le montant. Elle relit le formulaire.",
         "gérondif — même personne : elle vérifie en relisant"),
        ("Le superviseur approuve. Les finances traitent la demande.",
         "pendant que — deux services"),
    ], corrige=True,
       notes="Faire compter les personnes avant de choisir. C'est un test mécanique et "
             "il ne se trompe jamais.")

    d.pratique('Pratique · 4 de 4', "Écrivez comment vous avez fait",
               "Un gérondif de manière dans chaque phrase.", [
        ("Vous avez trouvé la bonne catégorie.", "J'ai trouvé la bonne catégorie en lisant la liste."),
        ("Vous avez évité une erreur de montant.", "J'ai évité l'erreur en relisant mon reçu."),
        ("Vous avez compris la procédure.", "J'ai compris la procédure en posant des questions."),
        ("Vous avez gagné du temps.", "J'ai gagné du temps en préparant mes documents d'avance."),
    ], corrige=True,
       notes="Ce sont les phrases qu'on écrit dans un courriel pour expliquer sa "
             "démarche. Les faire relire à voix haute.")

    d.billet(
        "Écrivez deux phrases avec un gérondif.",
        exemples=[
            "Une de simultanéité, une de manière.",
            "Écrivez à côté de chacune : quand, ou comment ?",
        ],
        notes="Corriger la terminaison et le sujet. Rendre avant C4 : l'impératif et le "
              "gérondif se combinent souvent dans une directive.")

    return d.save(dossier)
