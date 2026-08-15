# -*- coding: utf-8 -*-
"""A1 · La collecte de mitaines — mise en situation.
Bloc A « Je découvre » · couleur teal · 75 min.
Source du module : dialogue `prep`, exercices `prVocab` et `pr1`, cartes mémoire.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A1', section='teal',
        titre='La collecte de mitaines',
        chapeau="Marc, Sophie et Dany regardent le bulletin régional. Le reportage parle "
                "de la classe de Sophie : deux cents paires de mitaines amassées en "
                "quelques semaines, à partir de l'idée d'un seul élève.",
        duree='75 minutes')

    d.titre(notes="Ouverture du module 5. Demander qui écoute ou lit les nouvelles en "
                  "français, et sur quel support. Les réponses varient beaucoup et "
                  "orientent tout le module.")

    d.objectifs([
        "comprendre un reportage court à la radio ou à la télévision ;",
        "repérer les informations essentielles d'une nouvelle ;",
        "distinguer ce que dit le journaliste de ce que disent les gens ;",
        "nommer le vocabulaire des médias.",
    ])

    d.declencheur(
        'Mise en situation', "Vous écoutez les nouvelles. Qu'est-ce que vous retenez ?",
        pistes=[
            "Qu'est-ce que vous comprenez d'un bulletin en français ?",
            "Qu'est-ce qui est le plus difficile : la vitesse, les mots, les noms ?",
            "Est-ce que vous écoutez les nouvelles dans une autre langue aussi ?",
            "Qu'est-ce qui vous intéresse le plus : le local, le national, le monde ?",
        ],
        notes="Cinq minutes en grand groupe. La deuxième question est la plus utile : "
              "elle nomme la difficulté réelle, et les noms propres arrivent souvent en "
              "tête.")

    d.cartes('La situation', "Ce que le reportage raconte", [
        ("Ce qui s'est passé",
         "Des élèves de troisième secondaire ont amassé plus de deux cents paires de "
         "mitaines et de tuques pour les enfants du quartier."),
        ("Où et quand",
         "Dans une école de Longueuil. Le reportage dit « hier » ; Dany précise que la "
         "collecte était avant-hier."),
        ("Qui a eu l'idée",
         "Noah, un élève de la classe. Il en a parlé à son enseignante dès septembre."),
        ("Qui a aidé",
         "L'organisme Les Cœurs d'hiver. Une nouvelle mentionne presque toujours un "
         "organisme ou une institution."),
    ], notes="Faire remarquer la deuxième carte : le journaliste et Dany ne donnent pas la "
             "même date. C'est fréquent, et c'est un point d'écoute fine.")

    d.dialogue('Dialogue · 1 de 3', "Le reportage", [
        ("MARC", "Chut, écoutez ! Ils parlent de la collecte de mitaines organisée par "
                 "la classe de Sophie !", False),
        ("LE JOURNALISTE", "Hier, dans une école de Longueuil, des élèves de 3e "
                           "secondaire ont amassé plus de deux cents paires de mitaines "
                           "et de tuques pour les enfants du quartier.", True),
        ("LE JOURNALISTE", "L'activité a été organisée avec l'aide de l'organisme Les "
                           "Cœurs d'hiver.", True),
    ], consigne="Écoutez d'abord l'enregistrement, diapo masquée. Lisez ensuite.",
       notes="Passer l'audio de « Je découvre ». Faire compter les informations de la "
             "première phrase du journaliste : quand, où, qui, quoi, combien, pour qui. "
             "Six en une phrase.")

    d.dialogue('Dialogue · 2 de 3', "C'est Noah qui a eu l'idée", [
        ("DANY", "Ah, c'est vrai ! C'était avant-hier, la collecte !", True),
        ("SOPHIE", "C'est Noah qui a eu l'idée. Il en a parlé à son enseignante dès "
                   "septembre !", True),
        ("DANY", "Noah était tellement content quand il a vu toutes les boîtes pleines.",
         False),
    ], notes="« C'est Noah qui a eu l'idée » : la construction du défi 1. La signaler "
             "sans l'expliquer — elle sera le sujet de la séance B3.")

    d.dialogue('Dialogue · 3 de 3', "Trente paires, puis deux cents", [
        ("SOPHIE", "Et dire qu'avant-hier, il n'y avait que trente paires de mitaines "
                   "dans les boîtes. Aujourd'hui, il y en a plus de deux cents !", True),
        ("MARC", "C'est Noah qu'on doit remercier pour cette belle initiative !", True),
    ], notes="Deux chiffres à comparer : trente, puis deux cents. Une nouvelle donne "
             "souvent un chiffre de départ et un chiffre d'arrivée.")

    d.regle('La règle du module',
            "Une nouvelle répond à cinq questions : qui, quoi, où, quand, pourquoi.",
            precision="Le journaliste les donne presque toujours dans les deux premières "
                      "phrases. Écouter en cherchant ces cinq réponses est beaucoup plus "
                      "efficace qu'essayer de tout comprendre.",
            notes="Écrire les cinq questions au tableau et les y laisser tout le module. "
                  "C'est la grille d'écoute et de lecture de toutes les séances.")

    d.tableau('Analyse', "Le reportage, selon les cinq questions",
              ['La question', 'La réponse'],
              [["qui ?", "des élèves de 3e secondaire"],
               ["quoi ?", "ils ont amassé 200 paires de mitaines et de tuques"],
               ["où ?", "dans une école de Longueuil"],
               ["quand ?", "hier, selon le journaliste"],
               ["pourquoi ?", "pour les enfants du quartier"]],
              cle=0,
              note="Cinq réponses en deux phrases. C'est la densité normale d'un "
                   "reportage : il n'y a presque rien à jeter.",
              notes="Faire retrouver les cinq réponses dans le texte du dialogue, avant "
                    "d'afficher la colonne de droite.")

    d.vocabulaire('Vocabulaire · 1 de 2', "Les sortes de nouvelles", [
        ("un fait divers", "Une nouvelle sur des faits quotidiens qui attire la curiosité."),
        ("une nouvelle régionale", "Une nouvelle qui touche une région de la province."),
        ("une nouvelle nationale", "Une nouvelle qui touche la province ou le pays."),
        ("une nouvelle internationale", "Une nouvelle qui provient de l'extérieur du pays."),
        ("un reportage", "Un texte ou une émission qui présente une nouvelle en détail."),
    ], notes="Ces cinq mots sont le sujet de la séance A2. Les installer ici, les "
             "travailler là-bas.")

    d.vocabulaire('Vocabulaire · 2 de 2', "Les mots du reportage", [
        ("un témoin", "Une personne qui a vu un événement."),
        ("un organisme", "Un groupe organisé qui offre un service ou mène une cause."),
        ("amasser", "Réunir, accumuler peu à peu."),
        ("avertir", "Informer quelqu'un d'un danger ou d'une nouvelle importante."),
        ("un franc succès", "Une vraie réussite, un grand succès."),
        ("à ce jour", "Jusqu'à maintenant, jusqu'à aujourd'hui."),
    ], notes="« Un franc succès » et « à ce jour » sont des expressions figées : les "
             "faire employer telles quelles, sans les décomposer.")

    d.pratique('Pratique', "Le bulletin de nouvelles",
               "Répondez sans relire le dialogue.", [
        ("Combien de paires les élèves ont-ils amassées ?", "plus de deux cents"),
        ("Quel organisme a aidé la classe ?", "Les Cœurs d'hiver"),
        ("Qui a eu l'idée de la collecte ?", "Noah, un élève de la classe"),
        ("Dans quelle ville se trouve l'école ?", "à Longueuil"),
        ("Combien y avait-il de paires avant-hier ?", "trente"),
        ("Quand Noah en a-t-il parlé à son enseignante ?", "dès septembre"),
    ], corrige=True,
       notes="Les deux dernières questions demandent une écoute fine : les réponses sont "
             "dans les répliques des amis, pas dans le reportage.")

    d.piege("Le piège du « tout comprendre »",
            "J'écoute chaque mot et je perds le fil.",
            "J'écoute en cherchant qui, quoi, où, quand, pourquoi.",
            "Un bulletin va vite et contient des noms propres, des chiffres et des "
            "expressions figées. Vouloir tout saisir fait tout manquer. Chercher cinq "
            "réponses précises permet de comprendre l'essentiel dès la première écoute.",
            notes="Faire l'expérience : réécouter le reportage en ne cherchant que « où ». "
                  "Presque tout le monde l'obtient, alors que la compréhension globale "
                  "reste partielle.")

    d.billet(
        "Racontez une nouvelle que vous avez entendue cette semaine, en cinq lignes.",
        exemples=[
            "Une ligne par question : qui, quoi, où, quand, pourquoi.",
            "Dans n'importe quelle langue — mais écrivez-la en français.",
        ],
        notes="Ramasser. Ces nouvelles serviront en A2, où l'on classera celles du groupe "
              "selon leur portée.")

    return d.save(dossier)
