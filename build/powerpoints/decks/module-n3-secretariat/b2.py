# -*- coding: utf-8 -*-
"""B2 · Je vais être absente : le futur proche.
Bloc B « Défi 1 · Prévenir avant » · couleur teal (écoute et réponds) · 75 min.
Source : exercice `t1futur`, mini-leçon `t1futur`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='teal',
        titre='Je vais être absente',
        chapeau="Prévenir, c'est parler de demain. Le français a une forme "
                "faite exactement pour ça, et elle tient en deux verbes : "
                "aller au présent, puis le verbe qui ne change pas.",
        duree='75 minutes')

    d.titre(notes="Séance de langue orale. Tout le défi 1 repose sur cette forme : la "
                  "faire dire debout, à voix haute, plus que l'expliquer.")

    d.objectifs([
        "employer le futur proche pour annoncer une absence ;",
        "conjuguer aller au présent aux quatre personnes utiles ;",
        "mettre l'annonce à la forme négative ;",
        "distinguer ce qui n'est pas arrivé de ce qui est fini.",
    ])

    d.regle("Aller au présent, puis le verbe tel quel",
            "« Je vais être absente jeudi. »",
            precision="Un seul verbe se conjugue : aller. Le second reste "
                      "exactement comme dans le dictionnaire — être, manquer, "
                      "arriver. Rien ne se met entre les deux : ni à, ni de, "
                      "ni pour.",
            notes="Diapo à photographier. Faire répéter la phrase par tout le groupe, "
                  "deux fois, puis par chacun avec sa propre journée.")

    d.tableau('Analyse', "Les quatre formes utiles au comptoir",
              ["Qui", "On dit"],
              [["moi", "je vais être absente"],
               ["toi", "tu vas prévenir le secrétariat"],
               ["ma fille, mon fils", "elle va avoir un rendez-vous"],
               ["mes enfants", "ils vont manquer l'école"]],
              cle=1,
              note="« Nous allons » existe aussi, mais au comptoir on parle "
                   "presque toujours de soi ou de son enfant.",
              notes="Diapo à photographier. Faire produire une phrase par personne, avec "
                    "un vrai membre de sa famille.")

    d.pratique('Écoute et réponds', "Vais, vas, va ou vont ?",
               "Complétez à l'oral, puis par écrit.", [
        ("Je ___ être absente jeudi matin.", "vais"),
        ("Ma fille ___ avoir un rendez-vous à la clinique.", "va"),
        ("Mes deux enfants ___ manquer l'école vendredi.", "vont"),
        ("Tu ___ prévenir le secrétariat avant ?", "vas"),
        ("Je ne ___ pas être là lundi, mais je reviens mardi.", "vais"),
        ("Le camion de déménagement ___ arriver lundi matin.", "va"),
    ], corrige=True,
       notes="Faire d'abord à l'oral, en chaîne : un élève lit, le suivant complète. "
             "L'écrit vient ensuite, pour fixer.")

    d.regle("Pour dire non : ne et pas autour de aller",
            "« Je ne vais pas être là lundi. »",
            precision="Les deux morceaux entourent le premier verbe seulement. "
                      "Le second reste au bout, tout seul. À l'oral on entend "
                      "souvent « je vais pas être là » — au comptoir, dites la "
                      "forme complète.",
            notes="Diapo à photographier. Ne pas condamner la forme orale : elle est "
                  "partout et les élèves l'entendront. Situer les deux, c'est tout.")

    d.tableau('Analyse', "Avant ou après l'absence ?",
              ["Ce n'est pas arrivé", "C'est fini"],
              [["Je vais être absente jeudi.", "J'ai été absente jeudi."],
               ["Ma fille va avoir un rendez-vous.", "Ma fille a eu un rendez-vous."],
               ["Je vais manquer le cours.", "J'ai manqué le cours."]],
              cle=1,
              note="La secrétaire n'écrit pas la même chose : à gauche « absence "
                   "prévenue », à droite « absence à justifier ».",
              notes="Diapo à photographier. C'est le pont entre le défi 1 et le défi 2 : "
                    "la colonne de droite est celle de la semaine prochaine.")

    d.piege("Conjuguer le second verbe",
            "je vais suis absente",
            "je vais être absente",
            "Un seul verbe se conjugue : aller. Le second garde la forme du "
            "dictionnaire. C'est l'erreur la plus fréquente et la plus facile à "
            "corriger : on l'entend tout de suite.",
            notes="La signaler avant qu'elle ne se produise. Faire répéter trois fois la "
                  "forme juste, à voix haute, tout le groupe.")

    d.pratique('Production orale', "Annoncez votre absence",
               "Une phrase par élève, avec sa vraie journée.", [
        ("La forme", "je vais + un verbe qui ne change pas"),
        ("Le jour", "jeudi, lundi prochain, le 12 mars"),
        ("Le moment", "l'avant-midi, toute la journée"),
        ("La raison", "une phrase courte avec parce que"),
    ], corrige=False,
       notes="Tour de table debout, deux minutes. Corriger une seule chose par élève : "
             "la forme du verbe, et rien d'autre.")

    d.billet(
        "Écrivez trois phrases au futur proche sur votre semaine prochaine.",
        exemples=[
            "« Lundi, je vais travailler. »",
            "« Jeudi, je ne vais pas être au cours. »",
        ],
        notes="Devoir court. Il prépare B3, où le petit mot « le » devant le jour "
              "changera le sens de ces mêmes phrases.")

    return d.save(dossier)
