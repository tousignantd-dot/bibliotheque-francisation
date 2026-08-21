# -*- coding: utf-8 -*-
"""C3 · À partir du, jusqu'au, d'ici.
Bloc C « Défi 2 · La nouvelle adresse » · couleur ambre · 75 min.
Source : exercice `t2prep` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="À partir du, jusqu'au, d'ici",
        chapeau="Une démarche est une affaire de dates, et une date ne se "
                "donne jamais toute seule.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire utilitaire. Se tromper de préposition, ici, ce "
                  "n'est pas une faute de style : c'est un compte ouvert le mauvais jour.")

    d.objectifs([
        "employer « à partir de » pour un début et « jusqu'à » pour une fin ;",
        "employer « d'ici » pour un délai ;",
        "distinguer « dans » et « en » ;",
        "construire « avant de » et « après avoir » avec un infinitif.",
    ])

    d.tableau('Les prépositions · 1 de 2', "Le début, la fin, le délai",
              ['La préposition', "Ce qu'elle dit", 'Exemple'],
              [["à partir de", "le jour où ça commence", "à partir du premier juillet"],
               ["jusqu'à", "le jour où ça finit", "jusqu'au trente juin"],
               ["d'ici", "le temps qu'il reste", "d'ici vendredi"]],
              cle=0,
              note="de + le = du. On dit « à partir du », « jusqu'au ».",
              notes="Diapositive à photographier avec la suivante. Les trois premières "
                    "sont celles d'un appel de démarche.")

    d.tableau('Les prépositions · 2 de 2', "Les durées",
              ['La préposition', "Ce qu'elle dit", 'Exemple'],
              [["dans", "une durée à venir", "dans six semaines"],
               ["en", "le temps que ça prend", "en quatre heures"],
               ["depuis", "commencé avant, continue", "depuis vingt-six ans"]],
              cle=0,
              note="« Dans » compte à partir d'aujourd'hui ; « en » mesure le travail.",
              notes="Ces trois-là sont celles du récit. Elles reviennent en D2, dans le "
                    "récit de la journée de déménagement.")

    d.regle("« Dans » regarde vers l'avant, « en » mesure",
            "Le camion arrive dans six semaines. Ils ont tout monté en quatre heures.",
            precision="Beaucoup de langues emploient le même mot pour les deux. En "
                      "français, ce sont deux idées différentes : « dans » compte à "
                      "partir d'aujourd'hui, « en » dit combien de temps a duré le "
                      "travail.",
            notes="Faire dire la phrase fausse : « ils ont tout monté dans quatre heures ». "
                  "Elle veut dire qu'ils n'ont pas encore commencé.")

    d.cartes("« D'ici », la préposition de celui qui organise", "Rarement enseignée, très employée", [
        ("D'ici vendredi", "Entre maintenant et vendredi, à un moment ou à un autre."),
        ("D'ici deux semaines", "Dans les deux semaines qui viennent."),
        ("Ce qu'elle ajoute", "Une idée de délai, sans promettre quel jour."),
        ("Pourquoi elle est utile", "Elle dit ce qui sera fait avant tel moment. C'est la "
                                   "phrase de quelqu'un qui a un plan."),
    ], notes="Faire employer « d'ici » pour trois choses de la vraie semaine des élèves. "
             "Elle entre vite dans l'usage une fois comprise.")

    d.regle("Avec « depuis », le verbe reste au présent",
            "Thérèse habite ici depuis vingt-six ans.",
            precision="L'action continue aujourd'hui, donc le verbe est au présent — "
                      "contrairement à ce qui se fait dans bien d'autres langues. Et "
                      "devant un verbe, on dit « depuis que » : depuis que j'ai déménagé.",
            notes="Erreur très fréquente : « j'ai habité ici depuis deux ans ». Faire "
                  "corriger à voix haute.")

    d.piege("Employer « que » après « avant de »",
            "Avant que signer, faites le tour.",
            "Avant de signer, faites le tour.",
            "« Avant de » et « après avoir » se construisent avec un infinitif, jamais "
            "avec « que ». La forme avec « que » existe, mais demande le subjonctif — "
            "plus compliqué pour rien quand le sujet est le même.",
            notes="Donner la paire à retenir : avant de signer / après avoir signé. Deux "
                  "formes, un seul sujet.")

    d.pratique('Choix', "Quelle préposition ?",
               "L'enseignante lit ; le groupe complète.", [
        ("Le compte sera à mon nom ___ premier juillet.", "à partir du"),
        ("L'ancien compte reste ouvert ___ trente juin.", "jusqu'au"),
        ("___ vendredi, j'aurai prévenu la banque et l'école.", "D'ici"),
        ("Le déménagement est ___ six semaines.", "dans"),
        ("Les déménageurs ont tout monté ___ quatre heures.", "en"),
        ("Thérèse habite l'immeuble ___ vingt-six ans.", "depuis"),
        ("___ signer le bail, faites le tour du logement.", "Avant de"),
        ("Appelez Hydro-Québec ___ avoir relevé le compteur.", "après"),
    ], corrige=True,
       notes="Ce sont les items de l'exercice t2prep. Faire justifier chaque choix par la "
             "colonne « ce qu'elle dit » du tableau.")

    d.pratique('Production', "Vos dates à vous",
               "Chacun répond avec une vraie date de sa vie.", [
        ("Depuis quand habitez-vous votre logement ?", "J'habite ici depuis…"),
        ("Jusqu'à quand votre bail court-il ?", "Jusqu'au 30 juin."),
        ("Qu'est-ce que vous aurez fait d'ici la fin de la semaine ?", "D'ici vendredi, j'aurai…"),
        ("Quand est votre prochain rendez-vous ?", "Dans deux semaines."),
        ("Combien de temps prend votre trajet ?", "En vingt minutes."),
        ("Que faites-vous avant de sortir le matin ?", "Avant de sortir, je…"),
    ], corrige=True,
       notes="Sortir du vocabulaire du déménagement est voulu : ces prépositions servent "
             "partout, et c'est ce qui les fixe.")

    d.billet(
        "Écrivez quatre phrases sur votre mois qui vient, avec quatre prépositions différentes.",
        exemples=[
            "Une avec « à partir du », une avec « jusqu'au », une avec « d'ici », une avec « dans ».",
            "Ce sont les quatre phrases d'un appel de démarche.",
        ],
        notes="Ramasser les billets : les erreurs sur « d'ici » et « en » se voient tout de "
              "suite, et se corrigent en une phrase.")

    return d.save(dossier)
