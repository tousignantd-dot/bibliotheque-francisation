# -*- coding: utf-8 -*-
"""E1 · L'appel en trois temps
Bloc E « Je me lance » · couleur teal · 90 min. Production orale.
Source : exercice `t3tel`, jeu de rôle et production orale de « Je me lance ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="L'appel en trois temps",
        chapeau="Se présenter, exposer le motif, conclure sur une date. "
                "Trois minutes, et l'appel se termine sur ce qui est convenu "
                "plutôt que sur ce qui a été refusé.",
        duree='90 minutes')

    d.titre(notes="Avant-dernière séance. Elle se joue debout, au téléphone, dos à "
                  "dos : ne pas voir l'autre change tout, et c'est le point de la "
                  "séance.")

    d.objectifs([
        "se présenter en trois éléments, en dix secondes ;",
        "exposer le motif en une phrase avant de raconter ;",
        "rapporter ce qui avait été dit, sans reprocher ;",
        "conclure en reformulant et en proposant une date.",
    ], notes="Le deuxième objectif est celui que tout le monde rate : on raconte "
             "d'abord et on dit pourquoi on appelle à la fin, quand l'autre n'écoute "
             "plus.")

    d.declencheur(
        'Observation', "Que dites-vous dans les vingt premières secondes ?",
        pistes=[
            "Votre nom ? Votre numéro de dossier ?",
            "Pourquoi vous appelez, ou ce qui vous est arrivé ?",
            "Combien d'appels cette personne reçoit-elle aujourd'hui ?",
            "En combien de temps décide-t-elle de vous transférer ?",
        ],
        notes="Une personne au secrétariat reçoit trente appels par jour et décide en "
              "dix secondes. Ce n'est pas de l'impatience, c'est une charge de "
              "travail — le dire évite que le groupe le prenne personnellement.")

    d.tableau('Analyse', "Trois temps, et ce qu'on dit dans chacun",
              ['Le temps', 'Ce qu\'on dit'],
              [['je me présente', "nom, numéro de dossier, lien avec l'établissement"],
               ["j'expose le motif", "une phrase, avant l'histoire"],
               ['je rapporte', "vous m'aviez dit de rappeler après la décision"],
               ['je demande', "qu'est-ce que je peux faire d'ici là ?"],
               ['je conclus', "je reformule, je propose une date, je remercie"]],
              cle=0,
              notes="Cinq rangées sans note : la densité tient. Diapositive à "
                    "photographier — c'est la fiche que les élèves garderont à côté "
                    "du téléphone.")

    d.regle("Le motif vient avant l'histoire",
            "« Je vous appelle au sujet de la lettre du 10 avril. » Puis, si on la "
            "demande, l'histoire.",
            precision="Au bout d'une minute de récit, l'autre n'écoute plus : il "
                      "cherche encore ce qu'on veut. Une phrase de motif place tout "
                      "le reste dans le bon dossier, au sens propre.",
            notes="Diapositive à photographier. Faire l'exercice inverse une fois, "
                  "pour rire : quelqu'un raconte deux minutes avant de dire ce qu'il "
                  "veut. Le groupe comprend immédiatement.")

    d.pratique('Compréhension', "Quel moment de l'appel ?",
               "Dites si la phrase se dit au début, au milieu ou à la fin.", [
        ("Bonjour, Rania Nassar, dossier 41-2887.", "je me présente"),
        ("Je vous appelle au sujet de la lettre reçue lundi.", "j'expose le motif"),
        ("Vous m'aviez dit de vous rappeler après la décision.", "j'expose le motif"),
        ("Ce que je voudrais savoir, c'est ce que je peux faire d'ici l'an prochain.", "j'expose le motif"),
        ("Autrement dit, je m'inscris et je vous rappelle en décembre ?", "je conclus"),
        ("Merci de m'avoir rappelée ; je vous reparle le 10 décembre.", "je conclus"),
    ], corrige=True,
       notes="Faire remarquer que quatre phrases sur six appartiennent au motif : "
             "c'est le cœur de l'appel, et il tient en quatre phrases.")

    d.cartes('Jeu de rôle', "Trois appels, dos à dos", [
        ("Appel 1 · le secrétariat",
         "La personne ne peut rien dire du rang. Obtenez malgré tout à qui parler, et "
         "laissez un message précis."),
        ("Appel 2 · le conseiller",
         "Il rappelle. Rapportez ce qu'il vous avait dit, demandez ce qui a manqué, "
         "puis ce que vous pouvez faire."),
        ("Appel 3 · la proposition",
         "Proposez quelque chose : une mise à niveau, une entrée plus petite, une "
         "démarche de reconnaissance des acquis."),
        ("Ce qu'on écoute",
         "Les vingt premières secondes, le motif en une phrase, et la date à la fin."),
    ], notes="Quarante minutes, dos à dos, en équipes de deux. Ne pas voir l'autre "
             "supprime les gestes et oblige à nommer : c'est exactement la difficulté "
             "du téléphone.")

    d.piege('Piège', "Est-ce qu'on pourrait me passer devant ?",
            "Qu'est-ce que je peux faire d'ici l'an prochain ?",
            "La première demande une faveur, et elle ferme la conversation. La seconde "
            "demande une information, et elle ouvre presque toujours quelque chose.",
            notes="C'est la phrase que le module veut laisser. La faire répéter par "
                  "tout le monde, à voix haute, avant la fin de la séance.")

    d.billet("Écris les trois phrases de la fin de ton appel : reformulation, date, "
             "remerciement.",
             exemples=["Autrement dit, je m'inscris à la mise à niveau ?",
                       "Je vous rappelle le 10 décembre. Merci de m'avoir rappelée."],
             notes="Ramasser les billets. Ils servent d'aide-mémoire pour la "
                   "production orale à déposer, que les élèves enregistrent chez eux.")

    return d.save(dossier)
