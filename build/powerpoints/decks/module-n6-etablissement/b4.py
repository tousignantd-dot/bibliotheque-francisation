# -*- coding: utf-8 -*-
"""B4 · Celui qui, celle que — et la question qui entre dans la phrase
Bloc B « Défi 1 » · couleur ambre · 75 min. Grammaire du texte et de la phrase.
Source : exercices `t1celui` et `t1indir`, et leurs deux mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="Celui qui, celle que — et la question qui entre dans la phrase",
        chapeau="Deux outils pour parler dans un bureau : désigner sans "
                "répéter, et poser sa question sans la poser.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc B. Elle prépare directement le jeu de "
                  "rôle de E1 : ce sont les deux structures que l'élève emploiera le "
                  "plus devant un conseiller.")

    d.objectifs([
        "employer celui, celle, ceux, celles suivis de qui, que, où ou dont ;",
        "distinguer « celui que » de « ce que » ;",
        "transformer une question directe en question indirecte ;",
        "poser une question avec un mot interrogatif suivi d'un infinitif.",
    ], notes="Le deuxième objectif est celui qui coince : « ce que » quand il n'y a "
             "pas de nom avant, « celui que » quand il y en a un.")

    d.declencheur(
        'Observation', "Comment dit-on sans répéter le mot ?",
        pistes=[
            "« Il y a trois voies. La voie qui vous concerne demande un test. »",
            "Qu'est-ce qui vous dérange dans cette phrase ?",
            "Comment feriez-vous pour ne pas redire « voie » ?",
        ],
        notes="Écrire la phrase au tableau. Le groupe sent tout de suite la lourdeur "
              "sans savoir la nommer. Amener « celle » plutôt que de le donner.")

    d.tableau('Analyse', "Quatre formes, un seul mécanisme",
              ['La forme', 'Ce qu\'elle reprend'],
              [["celui", "un nom masculin singulier : le papier, celui que je crains"],
               ["celle", "un nom féminin singulier : la voie, celle qui vous concerne"],
               ["ceux", "un nom masculin pluriel : les documents, ceux qui portent un sceau"],
               ["celles", "un nom féminin pluriel : les preuves, celles qui comptent"]],
              cle=0,
              note="Le genre et le nombre viennent du nom qu'on ne répète pas. En cas de doute, remettez le nom.",
              notes="Diapositive à photographier. Faire l'essai « remettre le nom » "
                    "sur les quatre exemples : le genre saute aux yeux, et l'élève "
                    "n'a plus besoin de deviner.")

    d.regle("Il ne reste jamais seul",
            "Celui, celle, ceux, celles appellent toujours une suite : qui, que, où, dont, ou « de… ».",
            precision="« Prends celui » n'existe pas en français. Il faut « celui-ci », "
                      "« celui-là », « celui de Bintou » ou « celui qui… ». Après le "
                      "pronom, si le verbe n'a pas de sujet, c'est « qui » ; s'il lui "
                      "manque un complément, c'est « que ».",
            notes="Diapositive à photographier. Le test « verbe sans sujet ou sans "
                  "complément » est le seul qui tranche à coup sûr ; le faire "
                  "appliquer trois fois à voix haute.")

    d.pratique('Pratique', "Complétez avec celui, celle, ceux ou celles",
               "Attention à la majuscule quand le mot ouvre la phrase.", [
        ("Il y a trois voies d'admission. ... qui concerne Bintou demande le test.", "Celle"),
        ("Deux papiers sont arrivés. ... que je crains, c'est l'avis d'une page.", "Celui"),
        ("Parmi tous ses documents, elle garde ... qui portent un sceau.", "ceux"),
        ("De toutes les dates, ... dont personne ne se rappelle est la bonne.", "celle"),
        ("Deux locaux portent le numéro 118. ... où la rencontre a lieu est au fond.", "Celui"),
        ("Parmi les préalables, ... qu'il lui manque sont en mathématiques.", "ceux"),
    ], corrige=True,
       notes="Faire nommer le nom repris avant d'écrire la forme. Le cinquième item "
             "porte « où » avec un lieu, le quatrième « dont » : les signaler, ils "
             "reviennent en C2.")

    d.piege('Grammaire',
            "je ne sais pas celui que je dois faire",
            "je ne sais pas ce que je dois faire",
            "« Ce que » quand aucun nom n'a été posé avant : c'est une chose "
            "sans nom. « Celui que » quand le nom a été dit : le formulaire, "
            "celui que je dois remplir. Un nom avant, on prend celui ; pas de "
            "nom, on prend ce.",
            notes="Faire chercher au groupe deux exemples de chaque, tirés de leur "
                  "propre situation. Trois minutes suffisent et la distinction tient.")

    d.tableau('Analyse', "La question qui entre dans une phrase",
              ['Question directe', 'Question indirecte'],
              [["Est-ce que ça compte ?", "Je me demande si ça compte."],
               ["Est-ce qu'il faut un rendez-vous ?", "Il demande s'il faut un rendez-vous."],
               ["Qu'est-ce que je dois faire ?", "Je ne sais pas ce que je dois faire."],
               ["Qu'est-ce qui manque ?", "J'aimerais savoir ce qui manque."],
               ["Comment est-ce que je m'inscris ?", "Je ne sais pas comment m'inscrire."]],
              cle=1,
              note="Trois choses disparaissent : le point d'interrogation, l'inversion du sujet, et « est-ce que ».",
              notes="Diapositive à photographier. Faire lire les deux colonnes en "
                    "alternance, un élève chacune : l'oreille entend la différence de "
                    "ton avant que la tête comprenne la règle.")

    d.pratique('Pratique', "Transformez la question",
               "Écrivez seulement le mot ou les deux mots qui manquent.", [
        ("Est-ce que mes années comptent ? Je me demande ... mes années comptent.", "si"),
        ("Qu'est-ce que je dois faire ? Je ne sais pas ... je dois faire.", "ce que"),
        ("Où est-ce que je dépose ça ? Je voudrais savoir ... je dépose ça.", "où"),
        ("Qu'est-ce qui manque à mon dossier ? J'aimerais savoir ... manque.", "ce qui"),
        ("Que faire de mes six ans ? Je ne sais pas ... faire de mes six ans.", "quoi"),
        ("Est-ce qu'il faut un rendez-vous ? Il demande ... faut un rendez-vous.", "s'il"),
    ], corrige=True, cols=2,
       notes="Le dernier item est celui à surveiller : « s'il », jamais « si il ». "
             "Le cinquième aussi : c'est « quoi » devant un infinitif, jamais "
             "« que ». Les écrire tous les deux au tableau.")

    d.billet(
        "Écris trois questions que tu poserais à un conseiller, en question indirecte.",
        exemples=[
            "Commence par « Je me demande… », « Je voudrais savoir… », « Je ne sais pas… ».",
            "Ce sont celles que tu emploieras dans le jeu de rôle.",
        ],
        notes="Huit minutes. Faire lire quelques questions à voix haute et les "
              "corriger ensemble. Demander aux élèves de les garder : elles servent "
              "telles quelles en E1.")

    return d.save(dossier)
