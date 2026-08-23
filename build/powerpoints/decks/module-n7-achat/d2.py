# -*- coding: utf-8 -*-
"""D2 · Un paragraphe, une fonction
Bloc D « Défi 3 · La lettre de réclamation » · couleur ambre · grammaire du
texte · 75 min.
Source : exercices `t3plan`, `t3conn` et `t3subj` et leurs mini-leçons ;
savoirs « connecteurs et relations logiques » (dix points) et « subjonctif
présent » (cinq points) du niveau 7.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="Un paragraphe, une fonction",
        chapeau="Ce qui bloque dans une lettre de réclamation n'est presque "
                "jamais l'orthographe : c'est le paragraphe qui raconte, "
                "argumente et exige en même temps.",
        duree='75 minutes')

    d.titre(notes="Dernière séance avant la production. Tout ce qui est vu ici se "
                  "retrouve en E2, et le groupe doit le savoir : c'est la séance de "
                  "préparation, pas une leçon de plus.")

    d.objectifs([
        "nommer la fonction de chaque paragraphe avant de rédiger ;",
        "placer un connecteur en tête de paragraphe, suivi d'une virgule ;",
        "employer le subjonctif après un verbe de demande ;",
        "préférer l'infinitif quand le destinataire est celui qui agit.",
    ], notes="Le quatrième objectif surprend : on enseigne le subjonctif et on montre "
             "en même temps comment l'éviter. C'est pourtant ce que font les modèles "
             "officiels de mise en demeure.")

    d.declencheur(
        'Observation', "Pourquoi une lettre d'une page bien découpée obtient-elle plus qu'une lettre pleine ?",
        pistes=[
            "Combien de temps la personne y consacrera-t-elle ?",
            "Que voit-elle avant d'avoir lu un seul mot ?",
            "À quoi sert la ligne blanche entre deux paragraphes ?",
            "Qu'arrive-t-il quand un paragraphe fait deux choses ?",
        ],
        notes="La deuxième question amène la réponse : elle voit la structure. Le blanc "
              "n'est pas de l'espace perdu, c'est un signe de ponctuation.")

    d.tableau('Analyse', "Sept étiquettes, écrites avant de rédiger",
              ['Le paragraphe', 'Sa fonction'],
              [["1", "les faits de l'achat : date, bien, prix"],
               ["2", "la chronologie du défaut, une date par phrase"],
               ["3", "l'état au moment du défaut"],
               ["4", "la garantie chiffrée, et la preuve"],
               ["5", "la garantie légale, en appui"],
               ["6", "la demande, une seule, et le délai"],
               ["7", "les pièces jointes, sans commentaire"]],
              cle=0,
              notes="Diapositive à photographier. Sept rangées et aucune note en plus : "
                    "elle tient telle quelle et elle se recopie en trente secondes dans "
                    "un cahier.")

    d.regle("L'ordre n'est pas libre",
            "Faits, puis droit, puis demande, puis délai.",
            precision="Demander avant d'avoir raconté fait paraître la demande "
                      "arbitraire ; raconter après avoir demandé la fait oublier. La "
                      "lettre se résume en une phrase : voici ce qui s'est passé, voici "
                      "pourquoi vous devez agir, voici ce que je veux, voici jusqu'à "
                      "quand. C'est aussi l'ordre d'une plaidoirie.",
            notes="Diapositive à photographier. Faire relire la lettre d'Ernestine dans "
                  "cet ordre-là : les sept paragraphes y sont, et dans cet ordre exact.")

    d.tableau('Analyse', "Quatre familles de connecteurs",
              ['La famille', 'Les mots'],
              [["Ajouter", "en outre, par ailleurs, de plus"],
               ["Opposer", "or, toutefois, cependant"],
               ["Conclure", "en conséquence, par conséquent"],
               ["Situer", "dès, à compter de, à ce jour"],
               ["La place", "en tête, suivi d'une virgule"]],
              cle=0,
              notes="Diapositive à photographier. Deux règles de nombre : « or » une "
                    "seule fois par lettre, sur le fait le plus fort ; « en "
                    "conséquence » une seule fois, sur la demande.")

    d.pratique('Grammaire', "Complétez avec le bon connecteur",
               "Un connecteur par trou, jamais deux fois le même.", [
        ("___ le lendemain de la livraison, j'ai noté le kilométrage.", "Dès"),
        ("Je vous rappelle ___ que la garantie légale s'applique.", "en outre"),
        ("Vous invoquez l'usure normale. ___ , l'auto avait 24 jours.", "Or"),
        ("___ , je vous demande de procéder à la réparation.", "En conséquence"),
        ("Vous disposez de dix jours ___ la réception de la présente.", "à compter de"),
        ("J'ai téléphoné le 2 mai ; ___ , personne ne m'a rappelée.", "par la suite"),
    ], corrige=True,
       notes="Huit items dans le module ; en projeter six. Faire remarquer que « à ce "
             "jour, je n'ai reçu aucune réponse » constate, là où « vous ne m'avez "
             "jamais répondu » accuse. Même fait, deux lettres différentes.")

    d.tableau('Analyse', "Indicatif ou subjonctif ?",
              ['Le verbe d\'avant', 'Ce qui suit'],
              [["je constate que", "indicatif : un fait"],
               ["je vous informe que", "indicatif : un fait transmis"],
               ["je demande que", "subjonctif : pas encore un fait"],
               ["j'exige que", "subjonctif"],
               ["il faut que", "subjonctif : nécessité"],
               ["je vous demande de", "infinitif : plus court et plus ferme"]],
              cle=0,
              notes="Diapositive à photographier. Ce n'est pas le sens de la phrase qui "
                    "décide, c'est le verbe d'avant. Le dire dans ces mots-là : c'est ce "
                    "qui débloque les élèves qui cherchent une logique.")

    d.pratique('Grammaire', "Mettez au subjonctif présent",
               "Le verbe entre parenthèses.", [
        ("Je demande que la réparation (être) ___ effectuée à vos frais.", "soit"),
        ("J'exige que votre réponse me (parvenir) ___ par écrit.", "parvienne"),
        ("Il faut que vous (répondre) ___ dans les dix jours.", "répondiez"),
        ("J'aimerais que nous (pouvoir) ___ régler cela sans tribunal.", "puissions"),
        ("Je souhaite que le garage de mon choix (faire) ___ le travail.", "fasse"),
        ("Je demande que les pièces (être) ___ comprises.", "soient"),
    ], corrige=True,
       notes="« Soit » et « soient » font la moitié des subjonctifs d'une lettre de "
             "réclamation, parce que la demande porte presque toujours sur un passif. "
             "Le faire remarquer : c'est rassurant.")

    d.billet(
        "Écris les deux phrases centrales de ta lettre : la demande, et le délai.",
        exemples=[
            "« Je vous demande de… à vos frais. »",
            "« Vous disposez d'un délai de dix jours à compter de… »",
        ],
        notes="Cinq minutes. Ramasser et relire avant E2 : ceux qui ont écrit « je "
              "vous demanderais » au conditionnel ont manqué le point de C4, et il "
              "faut le reprendre en trente secondes au début de la production.")

    return d.save(dossier)
