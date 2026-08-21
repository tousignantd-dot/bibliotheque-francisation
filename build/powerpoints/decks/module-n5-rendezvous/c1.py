# -*- coding: utf-8 -*-
"""C1 · « Racontez-moi ce qui se passe. »
Bloc C « Défi 2 · Dans le bureau » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t2vf`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-rendezvous/images/')


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="« Racontez-moi ce qui se passe. »",
        chapeau="Un médecin dispose de trente minutes et pose peu de "
                "questions : c'est vous qui racontez. Un problème qui dure "
                "ne se dit pas avec une liste de mots — il se raconte.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 2. Demander au groupe combien de temps dure un "
                  "rendez-vous chez le médecin, puis combien de minutes le patient parle. "
                  "Les élèves sous-estiment toujours la seconde réponse.")

    d.objectifs([
        "raconter un problème de santé en quatre temps ;",
        "situer le début, décrire ce qui se passait, dire ce qui a changé ;",
        "donner les trois précisions que tout médecin cherche ;",
        "dire ce qu'on a arrêté de faire à cause du problème.",
    ])

    d.declencheur(
        'Observation', "« J'ai mal à la tête, je suis fatigué, ça tourne. » "
                       "Qu'est-ce qui manque à cette réponse ?",
        image=IMG + 'brassard-tension.jpg',
        pistes=[
            "Depuis quand ?",
            "À quel moment exactement ?",
            "Est-ce que ça empire ?",
            "Qu'est-ce que vous avez arrêté de faire ?",
        ],
        notes="Les quatre pistes sont exactement ce que le médecin va chercher. Les écrire "
              "au tableau et les y laisser toute la séance.")

    d.dialogue('Dialogue · 1 de 3', "Le début, et le décor", [
        ("DRE FONGANG", "Bonjour, monsieur Benali. Assoyez-vous. Racontez-moi ce qui "
                        "se passe.", True),
        ("RACHID", "Ça a commencé au mois de mars. Je me levais le matin et tout "
                   "tournait pendant quelques secondes.", True),
        ("DRE FONGANG", "Quelques secondes. Et ça arrive à quel moment, exactement ?", True),
        ("RACHID", "En me levant du lit, surtout. Et parfois en montant l'escalier de "
                   "l'école, quand je porte mes seaux.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire remarquer les deux temps dans la deuxième réplique : « ça a commencé » "
             "au passé composé, « je me levais » et « tout tournait » à l'imparfait. C'est "
             "toute la séance C2.")

    d.dialogue('Dialogue · 2 de 3', "Ce qui a changé", [
        ("RACHID", "Au début, c'était une fois par semaine. Maintenant, c'est presque "
                   "tous les matins.", True),
        ("DRE FONGANG", "Est-ce que vous avez perdu connaissance ? Est-ce que vous "
                        "êtes tombé ?", True),
        ("RACHID", "Non, jamais. Je me tiens au mur, ça passe. Mais la semaine "
                   "dernière, j'ai dû m'asseoir par terre.", True),
        ("DRE FONGANG", "Et la fatigue ? Vous en avez parlé à Manon au téléphone.", False),
    ], notes="« Non, jamais » suivi d'une exception précise : c'est ce qui distingue une "
             "bonne réponse d'une réponse polie. Le faire remarquer.")

    d.dialogue('Dialogue · 3 de 3', "La vie qui rétrécit", [
        ("RACHID", "Je dors huit heures et je me réveille fatigué. Avant, je jouais "
                   "au soccer le dimanche. J'ai arrêté au mois d'avril.", True),
        ("DRE FONGANG", "Bon. Je vous prends la tension couché, puis debout, tout de "
                        "suite après. On va voir si elle descend.", True),
        ("DRE FONGANG", "Couché, cent vingt sur quatre-vingts. Debout… elle descend "
                        "de vingt points. C'est ce que je cherchais.", True),
        ("RACHID", "Ça veut dire quoi ?", False),
    ], notes="« J'ai arrêté le soccer » est un symptôme au même titre qu'une douleur. "
             "Beaucoup d'élèves ne pensent jamais à le dire — insister.")

    d.regle("Un problème qui dure se raconte, il ne se liste pas",
            "Le début, le décor, ce qui a changé, aujourd'hui. Quatre temps, dans cet ordre.",
            precision="Une liste de symptômes dit ce qu'on a. Un récit dit comment ça "
                      "évolue — et c'est l'évolution qui fait agir un médecin. Aucun mot "
                      "savant ne remplace ces quatre phrases.",
            notes="Diapositive à photographier. Elle structure toute la production orale "
                  "de E1 : le dire dès maintenant.")

    d.cartes("Les quatre temps du récit", "Ce que chacun apporte", [
        ("1 · Le début",
         "Une phrase qui situe. « Ça a commencé au mois de mars. »"),
        ("2 · Le décor, à l'imparfait",
         "Ce qui se répétait. « Je me levais et tout tournait. »"),
        ("3 · Ce qui a changé, au passé composé",
         "Les faits, datés. « La semaine dernière, j'ai dû m'asseoir. »"),
        ("4 · Aujourd'hui, au présent",
         "« Maintenant, c'est presque tous les matins. »"),
    ], notes="Faire produire les quatre phrases à l'oral sur un problème inventé, en tour "
             "de table. Une phrase par personne, dans l'ordre.")

    d.tableau('Trois précisions que tout médecin cherche',
              "Et qu'aucun mot savant ne remplace",
              ['La question', 'Ce que Rachid répond'],
              [["À quel moment ça arrive ?", "en me levant, et à l'effort"],
               ["Combien de temps ça dure ?", "quelques secondes"],
               ["Est-ce que ça empire ?", "une fois par semaine, puis tous les matins"],
               ["Qu'avez-vous arrêté de faire ?", "le soccer, depuis avril"]],
              cle=0,
              notes="Les quatre réponses de Rachid tiennent en une phrase chacune, sans un "
                    "seul terme technique. C'est l'argument de la séance.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la consultation.", [
        ("Rachid situe le début au mois de mars.", "vrai"),
        ("Les étourdissements arrivent au lever et à l'effort.", "vrai"),
        ("Rachid a déjà perdu connaissance deux fois.", "faux — jamais"),
        ("Le problème arrive moins souvent qu'au début.", "faux — presque tous les matins"),
        ("La docteure prend la tension couché, puis debout.", "vrai"),
        ("La tension monte quand il se met debout.", "faux — elle descend de vingt points"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte.")

    d.billet(
        "Écrivez les deux premières phrases de votre récit : le début et le décor.",
        exemples=[
            "« Ça a commencé… » puis « Je… et… » à l'imparfait.",
            "Un problème vrai ou inventé — la langue travaille pareil.",
        ],
        notes="Le récit se construira sur quatre séances. Garder les billets : ils "
              "s'assemblent en E1.")

    return d.save(dossier)
