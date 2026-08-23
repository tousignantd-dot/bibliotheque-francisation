# -*- coding: utf-8 -*-
"""C4 · Qui, que, dont, où
Bloc C « Défi 2 · La visite avec la courtière » · couleur ambre · grammaire du
texte · 75 min.
Source : exercice `t2rel` et sa mini-leçon ; savoir « phrases subordonnées
relatives » du niveau 7.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre="Qui, que, dont, où",
        chapeau="« J'ai visité un condo. Il est au deuxième. Le fonds est "
                "de quarante mille. » Trois phrases, trois arrêts. Au "
                "niveau 7, le fil doit tenir sur deux ou trois lignes.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du défi 2. Elle prépare directement la production "
                  "orale de E1 : un exposé se fait de phrases liées, pas de phrases "
                  "juxtaposées.")

    d.objectifs([
        "relier deux phrases avec qui, que, dont ou où ;",
        "reconnaître quand le relatif est sujet et quand il est complément ;",
        "employer « dont » au lieu de couper la phrase en deux ;",
        "dire « le jour où », et non « le jour quand ».",
    ], notes="Le troisième objectif est le seul difficile. Les trois autres se règlent "
             "par un test mécanique, celui-là par de la répétition.")

    d.declencheur(
        'Observation', "Trois phrases ou une seule ?",
        pistes=[
            "« La courtière ouvre la porte. Elle travaille pour le vendeur. »",
            "« La courtière qui ouvre la porte travaille pour le vendeur. »",
            "Laquelle des deux versions se retient mieux ?",
            "Qu'est-ce qu'on gagne à lier, et qu'est-ce qu'on risque ?",
        ],
        notes="On gagne le fil ; on risque de se perdre au milieu. C'est pour ça qu'on "
              "s'en tient à quatre mots : qui, que, dont, où.")

    d.tableau('Analyse', "Quatre relatifs, quatre emplois",
              ['Le mot', 'Ce quil remplace'],
              [["qui", "le sujet : le verbe suit directement"],
               ["que", "le complément direct : un sujet suit"],
               ["dont", "ce qui était introduit par « de »"],
               ["où", "un lieu, ou un moment"],
               ["Le test de dont", "refaire la petite phrase : y a-t-il un « de » ?"]],
              cle=0,
              notes="Diapositive à photographier. La cinquième rangée est la méthode, "
                    "pas un cinquième relatif. Le préciser en la lisant.")

    d.cartes('Analyse', "Les quatre, sur le dossier de Sokhna", [
        ("qui", "La courtière qui ouvre la porte travaille pour le vendeur. Après « qui », rien : le verbe arrive tout de suite."),
        ("que", "Le condo que j'ai visité samedi date de 1992. Après « que », un autre sujet apparaît — j', elle, le vendeur."),
        ("dont", "Le fonds dont elle parle contient quarante mille dollars. On parle DE quelque chose : donc dont."),
        ("où", "Le jour où j'ai reçu l'avis, il neigeait. Un moment se dit « où » — « le jour quand » n'existe pas."),
    ], notes="Faire produire une phrase de chaque type par le groupe, sur la visite de "
             "C1, avant l'exercice écrit.")

    d.pratique('Écriture', "Complétez avec qui, que, dont ou où",
               "Un seul mot par trou.", [
        ("La courtière ___ m'a fait visiter travaille pour le vendeur.", "qui"),
        ("Le condo ___ j'ai visité samedi date de 1992.", "que"),
        ("Le fonds de prévoyance ___ elle m'a parlé contient 40 000 $.", "dont"),
        ("L'immeuble ___ j'habite depuis sept ans compte six logements.", "où"),
        ("Le jour ___ j'ai reçu l'avis, je ne savais pas ce qu'était un délai.", "où"),
        ("C'est une dépense ___ personne ne parle : les droits de mutation.", "dont"),
    ], corrige=True,
       notes="Six des huit items de `t2rel`. Pour les deux « dont », faire refaire la "
             "petite phrase toute seule à voix haute : « elle parle DE ce fonds ».")

    d.piege('Grammaire',
            "Le fonds dont elle en parle est petit.",
            "Le fonds dont elle parle est petit.",
            "Le « de » est déjà contenu dans « dont » : le répéter avec « en » ou avec "
            "« de lui » double la préposition. C'est une faute fréquente chez ceux qui "
            "commencent à employer « dont », donc chez ceux qui progressent : la "
            "corriger sans décourager.",
            notes="Faire remarquer que l'erreur prouve qu'on a compris à quoi sert "
                  "« dont ». Ceux qui ne l'emploient jamais ne la font jamais.")

    d.billet(
        "Décris le condo en deux phrases liées par un relatif.",
        exemples=[
            "« Le condo que Sokhna a visité… »",
            "Deux lignes au maximum.",
        ],
        notes="Trois minutes. Relever les billets : ceux qui contiennent un « dont » "
              "juste se lisent à voix haute au groupe entier.")

    return d.save(dossier)
