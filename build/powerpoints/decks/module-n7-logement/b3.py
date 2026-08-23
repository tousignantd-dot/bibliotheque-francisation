# -*- coding: utf-8 -*-
"""B3 · Demander sans exiger : le conditionnel
Bloc B « Défi 1 · L'avis du propriétaire » · couleur ambre · grammaire · 75 min.
Source : exercice `t1cond` et sa mini-leçon ; savoir « indicatif conditionnel
présent » du niveau 7 (cinq points).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Demander sans exiger : le conditionnel",
        chapeau="« Je veux » et « je voudrais » demandent la même chose. "
                "La différence est ce qu'elles laissent à l'autre — et dans "
                "une négociation, cette différence vaut tous les arguments.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire. Reprendre les billets de A2 : les demandes que "
                  "les élèves ont écrites au conditionnel servent d'exemples de départ, "
                  "et elles sont à eux.")

    d.objectifs([
        "former le conditionnel présent de n'importe quel verbe ;",
        "adoucir une demande sans en perdre la précision ;",
        "proposer un chiffre en le disant discutable ;",
        "reconnaître le conditionnel d'un document et ce qu'il signifie.",
    ], notes="Le quatrième objectif est de la compréhension écrite déguisée en "
             "grammaire : « le loyer passerait » veut dire que rien n'est décidé.")

    d.declencheur(
        'Observation', "Deux phrases, une lettre de différence",
        pistes=[
            "« Je vous proposerai cinquante-cinq dollars. »",
            "« Je vous proposerais cinquante-cinq dollars. »",
            "Laquelle annonce une décision ? Laquelle ouvre une discussion ?",
            "Est-ce que ça s'entend, ou seulement ça se lit ?",
        ],
        notes="Ça s'entend à peine, et ça se lit très bien : c'est justement pourquoi "
              "la faute passe inaperçue à l'oral et saute aux yeux dans une lettre.")

    d.regle("Radical du futur, terminaisons de l'imparfait",
            "Le conditionnel se fabrique avec deux moitiés empruntées à deux temps.",
            precision="On prend le radical du futur — proposer-, pourr-, voudr-, ser-, "
                      "faudr- — et on y ajoute les terminaisons de l'imparfait : -ais, "
                      "-ais, -ait, -ions, -iez, -aient. Les verbes irréguliers au futur "
                      "le sont au conditionnel, et de la même façon : il n'y a donc rien "
                      "de nouveau à apprendre par cœur.",
            notes="Diapositive à photographier. Le faire vérifier au tableau sur trois "
                  "verbes proposés par le groupe : la règle tient à chaque fois.")

    d.tableau('Analyse', "Trois emplois, trois usages",
              ["L'emploi", 'Un exemple du module'],
              [["Adoucir une demande", "Je voudrais une réponse écrite."],
               ["Proposer un chiffre discutable", "Je vous proposerais cinquante-cinq dollars."],
               ["Dire ce qui se passerait", "Le loyer passerait à 1 024 $ le 1er juillet."],
               ["Poser une hypothèse", "Si la fenêtre était changée, j'accepterais."],
               ["Ouvrir une phrase, tout simplement", "Il faudrait fixer une date."]],
              cle=0,
              notes="Diapositive à photographier. Le troisième emploi est celui qu'on "
                    "rencontre en lisant, les autres celui qu'on emploie en parlant.")

    d.pratique('Écriture', "Mettez le verbe au conditionnel présent",
               "Un seul mot par trou.", [
        ("(Pouvoir) ___ -vous m'accorder une semaine avant que je réponde ?", "Pourriez"),
        ("J'(aimer) ___ que l'entente soit mise par écrit, avec la date.", "aimerais"),
        ("Je vous (proposer) ___ cinquante-cinq dollars plutôt que quatre-vingt-quatre.", "proposerais"),
        ("Selon l'avis, le loyer (passer) ___ à mille vingt-quatre dollars.", "passerait"),
        ("Si la fenêtre était changée, je ne (discuter) ___ pas la hausse.", "discuterais"),
        ("Il (falloir) ___ que nous fixions une date, sinon l'été va passer.", "faudrait"),
    ], corrige=True,
       notes="Six des huit items de `t1cond`. Faire lire chaque phrase complète à voix "
             "haute après correction : la forme s'installe par l'oreille.")

    d.piege('Grammaire',
            "Si j'aurais le temps, je répondrais.",
            "Si j'avais le temps, je répondrais.",
            "Jamais de conditionnel après « si ». La règle tient en deux mots : "
            "imparfait après si, conditionnel dans l'autre moitié de la phrase. C'est "
            "l'erreur la plus fréquente du niveau, et la plus facile à corriger, parce "
            "qu'elle ne concerne qu'un seul mot dans toute la phrase.",
            notes="Faire produire cinq phrases en « si » par le groupe, à l'oral, en "
                  "corrigeant seulement la moitié fautive. Ne pas expliquer davantage : "
                  "c'est de la répétition qu'il faut ici.")

    d.billet(
        "Réécris une exigence en demande.",
        exemples=[
            "« Vous allez réparer la fenêtre. » devient…",
            "Une phrase, avec un verbe au conditionnel.",
        ],
        notes="Deux minutes. Ramasser : les phrases servent de matière au jeu de rôle "
              "de E1, où le conditionnel devra tenir toute la conversation.")

    return d.save(dossier)
