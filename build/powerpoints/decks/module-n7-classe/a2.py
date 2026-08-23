# -*- coding: utf-8 -*-
"""A2 · Le petit « e » quand on parle à un groupe
Bloc A « Je découvre » · couleur indigo · graphie-phonie · 75 min.
Source : exercice `prPhon`, mini-leçon `prPhon`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Le petit « e » quand on parle à un groupe",
        chapeau="Devant vingt personnes, on ralentit le débit — on ne rajoute "
                "pas des syllabes. Certains « e » se disent, d'autres "
                "tombent, et c'est la place du « e » dans le mot qui décide.",
        duree='75 minutes')

    d.titre(notes="Séance de graphie-phonie. Elle sert deux fois dans le module : à "
                  "l'écoute, pour reconnaître un mot amputé d'une syllabe, et à la "
                  "production, en vue de l'exposé du bloc E.")

    d.objectifs([
        "entendre le petit « e » qui se dit et celui qui disparaît ;",
        "savoir que les deux prononciations sont correctes ;",
        "reconnaître un mot connu qui arrive sans sa syllabe du milieu ;",
        "parler posément devant un groupe sans ajouter de syllabes.",
    ], notes="Le deuxième objectif évite l'inquiétude : personne n'est corrigé ici. "
             "C'est une leçon d'écoute d'abord, de production ensuite.")

    d.declencheur(
        'Observation', "Dites ces trois mots à voix haute, vite puis lentement",
        pistes=[
            "« demain » — combien de syllabes entendez-vous ?",
            "« facilement » — et celui-là ?",
            "« regarder » — commencez-vous par « re » ou par « r » ?",
            "Est-ce que ça change quand vous parlez plus vite ?",
        ],
        notes="Faire dire à voix haute, pas seulement lire. La plupart des élèves "
              "produisent déjà les bonnes formes sans le savoir : la leçon leur "
              "donne la règle de ce qu'ils font.")

    d.regle("Une seule question : qu'est-ce qu'il y a devant ?",
            "Le petit « e » se dit quand une seule chose le protège : une "
            "consonne qui ferme la bouche au début du mot, ou deux consonnes "
            "qui butent devant lui.",
            precision="Partout ailleurs au milieu d'un mot, avec une seule "
                      "consonne devant, il tombe. Et les deux prononciations sont "
                      "correctes : ce n'est pas une question de soin.",
            notes="Diapositive à photographier. Ne pas parler d'alphabet phonétique : "
                  "les lettres et un mot repère suffisent, et c'est la règle des "
                  "diaporamas de ce dépôt.")

    d.tableau('Analyse', "Quand il se dit, quand il tombe",
              ['Ce qu\'il y a devant', 'Ce qui arrive au « e »'],
              [["p, b, t, d, k, g",
                "il se dit : demain, devoir, petit, tenez"],
               ["Deux consonnes",
                "il se dit : justement, exactement, probablement"],
               ["Une seule consonne",
                "il tombe : facilement, acheter, appeler"],
               ["Un r au début",
                "il tombe : regarder, reprendre, relever"]],
              cle=0,
              note="Le couple à retenir : « de » se dit, « re » tombe.",
              notes="Diapositive à photographier. Le dernier cas est le plus "
                    "surprenant pour les élèves qui ont appris à lire chaque lettre.")

    d.pratique('Écoute', "Il se dit, ou il tombe ?",
               "Écoutez chaque mot dit posément, puis décidez.", [
        ("devoir", "il se dit"),
        ("facilement", "il tombe"),
        ("demain", "il se dit"),
        ("acheter", "il tombe"),
        ("justement", "il se dit"),
        ("appeler", "il tombe"),
        ("exactement", "il se dit"),
        ("regarder", "il tombe"),
    ], corrige=True,
       notes="Les huit mots sont dans le module, avec le son. Les faire écouter deux "
             "fois, puis répéter. Ne pas corriger la prononciation d'un élève qui "
             "garde un « e » : cela ne provoque aucun malentendu.")

    d.piege('Prononciation',
            "« Ra-pi-de-ment, en quatre morceaux. »",
            "« Rapid'ment, en trois. »",
            "Devant un groupe, on ralentit le débit, on n'ajoute pas des "
            "syllabes. Dire chaque « e » écrit ne rend pas le propos plus "
            "clair : ça le rend plus long et plus étrange. Personne ne parle "
            "comme ça, pas même dans un exposé soigné.",
            notes="Point important pour le bloc E. Beaucoup d'élèves croient qu'un "
                  "exposé se dit en détachant tout. C'est ce qui fait la voix de "
                  "robot, et l'auditoire décroche.")

    d.cartes('Analyse', "Six mots que vous direz devant la classe", [
        ("demain", "de-main, deux syllabes pleines"),
        ("justement", "jus-te-ment, le « e » tient entre st et m"),
        ("exactement", "e-xac-te-ment, même cas"),
        ("facilement", "facil'ment, le « e » tombe"),
        ("acheter", "ach'ter, deux syllabes et non trois"),
        ("regarder", "r'garder, le « e » du début tombe"),
    ], notes="Faire répéter chaque mot deux fois : d'abord au débit d'une "
             "conversation, puis au débit d'un exposé. Le résultat est le même.")

    d.pratique('Production', "Lisez à voix haute, posément",
               "Un élève lit, les autres écoutent les petits « e ».", [
        ("Demain, nous devons appeler la personne-ressource.", "de-main, ap'ler"),
        ("Il faut justement relever les arbres de la rue.", "jus-te-ment, r'lever"),
        ("Je vais reprendre exactement ce que tu viens de dire.", "r'prendre, e-xac-te-ment"),
        ("On peut facilement acheter la carte du quartier.", "facil'ment, ach'ter"),
    ], corrige=True,
       notes="Exercice de lecture à voix haute, deux tours. Au premier, on cherche "
             "les « e » ; au second, on lit sans y penser. Le second est meilleur.")

    d.billet(
        "Écrivez un mot que vous avez déjà mal reconnu parce qu'il allait vite.",
        exemples=[
            "Un mot que vous connaissez, mais que vous n'avez pas entendu.",
            "Dites où : à la radio, au travail, en classe ?",
        ],
        notes="Billet de sortie. Les réponses ramènent presque toujours des mots à "
              "« e » tombant, et c'est la meilleure preuve que la leçon sert.")

    return d.save(dossier)
