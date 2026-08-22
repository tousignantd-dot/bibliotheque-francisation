# -*- coding: utf-8 -*-
"""C4 · Exigé, aucune expérience, un atout.
Bloc C « Défi 2 » · couleur ambre · 60 min. Écriture et décision.
Source du module : exercice `t2faut` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre='Exigé, aucune expérience, un atout',
        chapeau="Le bas d'une offre décide qui peut se présenter. Trois mots "
                "y suffisent, et beaucoup de gens renoncent à un poste qu'ils "
                "pouvaient avoir, faute de les avoir lus.",
        duree='60 minutes')

    d.titre(notes="Dernière séance du défi 2. Relire les billets de C2 : la ligne que "
                  "chacun regarde en premier. Beaucoup n'auront pas nommé celle-ci.")

    d.objectifs([
        "distinguer ce qui est exigé de ce qui est un atout ;",
        "comprendre « aucune expérience exigée » ;",
        "comprendre « formation donnée sur place » ;",
        "décider si l'on peut se présenter.",
    ])

    d.tableau('Analyse', "Trois mots, trois portes",
              ['Ce qui est écrit', 'Ce que ça veut dire', 'Est-ce que j\'y vais ?'],
              [["Expérience exigée", "c'est obligatoire", "oui, en disant ce que je sais faire"],
               ["Aucune expérience exigée", "ouvert aux débutants", "oui, sans hésiter"],
               ["Anglais un atout", "utile, pas obligatoire", "oui, le français suffit"],
               ["Formation donnée sur place", "ils vont m'apprendre", "oui, c'est fait pour moi"]],
              cle=2,
              note="Dans les quatre cas, la réponse est la même. C'est la leçon de la séance.",
              notes="Diapo à photographier. Laisser le groupe découvrir la colonne de "
                    "droite ligne par ligne avant de la commenter.")

    d.regle("Un atout n'est jamais une exigence",
            "« Anglais un atout » veut dire : présentez-vous quand même.",
            precision="Cette ligne est écrite exprès pour dire que l'absence de cette "
                      "chose ne bloque pas. Beaucoup de postes sont donnés à quelqu'un "
                      "qui n'avait pas l'atout mais qui s'est présenté.",
            notes="Diapo à photographier. Demander qui, dans le groupe, a déjà renoncé "
                  "à cause d'une ligne comme celle-là. Il y en a toujours.")

    d.cartes("Le bas de l'annonce, mot par mot", "Ce qu'il faut savoir lire", [
        ("Il faut, exigé, obligatoire",
         "Les trois disent la même chose : sans cela, on ne prend personne. « Exigé » "
         "s'accorde avec ce qu'il suit : expérience exigée, diplôme exigé."),
        ("Aucune expérience exigée",
         "La ligne qui ouvre la porte. Elle va presque toujours avec « formation "
         "donnée sur place » : le travail sera montré au nouvel employé."),
        ("Un atout",
         "Utile, pas obligatoire. Si vous l'avez, dites-le sans insister ; si vous ne "
         "l'avez pas, présentez-vous quand même."),
        ("La dernière ligne",
         "Se présenter en personne, apporter son curriculum vitæ, demander telle "
         "personne, entre telle et telle heure. C'est la marche à suivre : la respecter."),
    ], notes="Faire chercher ces quatre formulations dans des annonces réelles, si le "
             "groupe en a apporté. Elles y sont presque toutes.")

    d.piege("Renoncer devant le mot « exigé »",
            "Expérience exigée. Ce n'est pas pour moi.",
            "Je me présente en disant ce que je sais faire d'autre.",
            "Souvent, « exigé » veut bien dire obligatoire. Mais si vous savez faire un "
            "travail proche, la visite coûte quinze minutes et peut se retourner : "
            "« Je n'ai pas travaillé en cuisine, mais je sais faire le ménage et "
            "j'apprends vite. »",
            notes="Nuance à tenir des deux côtés : ne pas promettre que ça marche, ne "
                  "pas laisser croire que c'est fermé d'avance.")

    d.pratique('Écriture', "Complétez le bas de l'annonce",
               "Complétez avec : faut, exigée, demandé, aucune, atout.", [
        ("Il ___ parler français pour ce poste-là.", "faut"),
        ("« ___ expérience exigée » : je peux me présenter.", "Aucune"),
        ("Deux ans d'expérience sont ___ pour ce poste.", "exigés"),
        ("Parler anglais n'est pas obligatoire : c'est un ___ .", "atout"),
        ("Il est ___ de se présenter entre 9 h et 11 h.", "demandé"),
        ("Aucun diplôme n'est ___ : formation sur place.", "exigé"),
    ], corrige=True,
       notes="Même exercice que t2faut dans le module. Faire remarquer l'accord de "
             "« exigé » d'une ligne à l'autre.")

    d.pratique('Décision', "Est-ce que je peux me présenter ?",
               "L'annonce dit ceci, et vous avez cela. Vous y allez ?", [
        ("Aucune expérience exigée / vous n'en avez aucune", "oui, sans hésiter"),
        ("Aucune expérience exigée / vous en avez", "oui, et dites-le"),
        ("Expérience exigée / vous n'en avez pas", "oui, en disant ce que vous savez faire"),
        ("Expérience exigée / vous en avez", "oui, dites le nombre d'années"),
        ("Anglais un atout / vous ne parlez pas anglais", "oui, le français suffit"),
        ("Anglais un atout / vous parlez anglais", "oui, mentionnez-le sans insister"),
    ], corrige=True,
       notes="Six cas, six fois « oui ». Le faire remarquer à la fin : c'est le message "
             "de la séance, et il vaut mieux que le groupe le trouve lui-même.")

    d.pratique('Oral', "Que dire quand on n'a pas ce qui est exigé ?",
               "Chacun compose sa phrase et la dit à voix haute.", [
        ("La structure", "Je n'ai pas… , mais je sais… et j'apprends vite."),
        ("Avec un travail proche", "Je n'ai pas travaillé en cuisine, mais je fais le ménage depuis…"),
        ("Sans aucune expérience", "Je n'ai jamais fait ce travail, mais je peux apprendre."),
    ], notes="Dix minutes. C'est la phrase la plus utile du module après « Est-ce que "
             "vous engagez ? ». Faire le tour du groupe.")

    d.billet(
        "Écrivez la phrase que vous direz si l'on vous demande une expérience que vous n'avez pas.",
        exemples=[
            "Avec un « mais » au milieu.",
            "Une seule phrase, celle que vous pourrez vraiment dire.",
        ],
        notes="Deux minutes. La ramasser et la redonner en E1 : elle servira au jeu de "
              "rôle.")

    return d.save(dossier)
