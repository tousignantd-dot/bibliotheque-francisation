# -*- coding: utf-8 -*-
"""D2 · Prendre sa place autour de la table
Bloc D « Défi 3 » · couleur ambre · 75 min. Grammaire et conventions de la parole.
Source : exercices `t3tour`, `t3subj`, `t3si` et `t3pdv`, et leurs mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="Prendre sa place autour de la table",
        chapeau="Beaucoup d'adultes sortent d'une rencontre sans avoir dit "
                "ce qu'ils voulaient dire. Ce n'est presque jamais un manque "
                "de courage : c'est qu'on ne sait pas où entrer.",
        duree='75 minutes')

    d.titre(notes="Séance la plus dense du module : quatre points de langue. Les "
                  "traiter dans l'ordre et accepter de ne pas tout finir — les deux "
                  "premiers sont indispensables, les deux derniers se reprennent en "
                  "E1.")

    d.objectifs([
        "s'introduire dans une discussion sans couper celui qui parle ;",
        "employer le subjonctif après un verbe de volonté suivi de « que » ;",
        "poser une condition avec « si », sans futur juste après ;",
        "annoncer son point de vue comme un point de vue.",
    ], notes="Les quatre objectifs sont les quatre outils du jeu de rôle de E1. Le "
             "dire : rien ici n'est de la grammaire pour la grammaire.")

    d.declencheur(
        'Observation', "Où entre-t-on dans une conversation à quatre ?",
        pistes=[
            "Faut-il parler plus fort ? Lever la main ?",
            "Comment savez-vous qu'une personne a fini sa phrase ?",
            "Que faites-vous quand vous n'osez pas ?",
        ],
        notes="La bonne réponse est : à la fin d'une phrase, quand la voix descend. "
              "La faire trouver plutôt que de la donner ; le groupe la connaît sans "
              "l'avoir formulée.")

    d.tableau('Analyse', "Sept façons de prendre la parole",
              ['La formule', 'Ce qu\'elle fait'],
              [["Si je peux me permettre…", "prendre la parole sans couper"],
               ["J'ajoute une chose.", "compléter ce qu'on vient de dire soi-même"],
               ["Si je comprends bien…", "vérifier avant d'aller plus loin"],
               ["Est-ce que je peux poser une question ?", "demander la parole pour interroger"],
               ["Vous disiez tantôt que…", "reprendre les mots d'un autre pour répondre"],
               ["C'est tout pour moi.", "rendre la parole en disant qu'on a fini"]],
              cle=0,
              notes="Diapositive à photographier. Faire répéter les six formules à "
                    "voix haute, en groupe. Elles s'apprennent une fois et servent "
                    "toute une vie.")

    d.regle("On entre à la fin d'une phrase, pas au milieu",
            "Écoutez la fin des phrases plutôt que leur début : c'est là que la place s'ouvre.",
            precision="Le signal est un souffle, un « donc », un « bon » — la "
                      "personne cherche sa suite. Entrer au milieu d'une phrase ne "
                      "fonctionne pas : l'autre reprend, et vous perdez le tour sans "
                      "avoir rien dit.",
            notes="Diapositive à photographier. Faire un exercice de deux minutes : "
                  "l'enseignant parle sans arrêt, les élèves doivent entrer. Ils "
                  "sentent immédiatement où c'est possible.")

    d.tableau('Analyse', "Le subjonctif après un verbe de volonté",
              ['Le verbe introducteur', 'Ce qui suit'],
              [["il faut que", "il faut que quelqu'un envoie le compte rendu"],
               ["vouloir que", "elle veut que la preuve soit au dossier"],
               ["exiger que", "elle exige que les documents arrivent avant la date"],
               ["aimerait que", "elle aimerait que la visite ait lieu après le test"],
               ["craindre que", "elle craint qu'il fasse tout à la dernière minute"]],
              cle=0,
              note="Cinq irréguliers suffisent : sois, aie, aille, fasse, sache. Et espérer, lui, prend l'indicatif.",
              notes="Diapositive à photographier. L'exception « espérer » est la "
                    "faute la plus fréquente : on dit « j'espère qu'il sera là », "
                    "jamais « qu'il soit là ». L'écrire à part au tableau.")

    d.pratique('Pratique', "Complétez après « que »",
               "Écrivez le verbe entre parenthèses à la forme qui convient.", [
        ("Elle veut que la preuve ... au dossier avant le 6 février. (être)", "soit"),
        ("Il faut que quelqu'un lui ... le compte rendu. (envoyer)", "envoie"),
        ("Elle exige que les documents ... avant la date. (arriver)", "arrivent"),
        ("Elle aimerait que la visite ... lieu après le test. (avoir)", "ait"),
        ("Il souhaite que le plan de formation ... la date. (porter)", "porte"),
        ("Il faut que tout le monde ... la même chose. (savoir)", "sache"),
    ], corrige=True, cols=2,
       notes="Trois irréguliers dans la liste : soit, ait, sache. Les signaler avant, "
             "pas après. Faire relire la phrase entière à voix haute une fois "
             "corrigée.")

    d.piege('Grammaire',
            "si elle viendra demain, on regardera son dossier",
            "si elle vient demain, on regardera son dossier",
            "Jamais de futur juste après « si ». Le futur va de l'autre côté "
            "de la virgule, dans la conséquence. Et devant « il », « si » se "
            "colle : s'il réussit, s'ils arrivent — mais « si elle », en deux "
            "mots.",
            notes="C'est la faute la plus fréquente du niveau, tous groupes "
                  "confondus. Faire répéter cinq phrases correctes plutôt que "
                  "d'expliquer une deuxième fois.")

    d.tableau('Analyse', "Annoncer que ce qui suit est un avis",
              ['La formule', 'À qui appartient l\'avis'],
              [["À mon avis, …", "à vous : c'est le plus courant"],
               ["Pour ma part, …", "à vous, par rapport aux autres"],
               ["Personnellement, …", "à vous, et vous insistez"],
               ["Selon la responsable, …", "à elle, pas à vous"],
               ["Il me semble que…", "à vous, mais vous n'êtes pas sûr"]],
              cle=0,
              note="« C'est trop court » oblige l'autre à vous contredire. « À mon avis, c'est trop court » lui laisse la place de répondre.",
              notes="Diapositive à photographier. Faire dire les deux versions à voix "
                    "haute par deux élèves : la différence de température s'entend, "
                    "et l'explication devient inutile.")

    d.billet(
        "Écris ce que tu dirais si tu n'étais pas d'accord avec une date.",
        exemples=[
            "Emploie « pour ma part » et une condition avec « si ».",
            "Ne refuse pas : propose autre chose et dis pourquoi.",
        ],
        notes="Huit minutes, et c'est le cœur du bloc D. Faire lire trois productions "
              "à voix haute. Rappeler la phrase de Bintou : « Si j'y vais avant, je "
              "vais penser à ça pendant l'épreuve. »")

    return d.save(dossier)
