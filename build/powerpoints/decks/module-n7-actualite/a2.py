# -*- coding: utf-8 -*-
"""A2 · Le « e » qu'on entend et celui qui disparaît
Bloc A « Je découvre » · couleur indigo · graphie-phonie · 75 min.
Source : exercice `prE` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Le « e » qu'on entend et celui qui disparaît",
        chapeau="Un mot très connu devient méconnaissable à la radio parce "
                "qu'un petit « e » est tombé. Ce n'est pas du vocabulaire qui "
                "manque : c'est une prononciation qu'on n'a jamais apprise.",
        duree='75 minutes')

    d.titre(notes="Séance de graphie-phonie. Prévenir dès le départ que l'objectif "
                  "n'est pas de mieux prononcer, mais de mieux entendre. C'est un "
                  "renversement, et il faut le dire.")

    d.objectifs([
        "entendre quand le « e » du milieu d'un mot se dit et quand il tombe ;",
        "reconnaître un mot connu sous sa forme courte, à l'écoute ;",
        "connaître les deux cas où le « e » se maintient toujours ;",
        "cesser d'attribuer à un manque de vocabulaire ce qui est un fait de prononciation.",
    ], notes="Le quatrième objectif est le vrai. Beaucoup d'élèves qui lisent très bien "
             "croient être mauvais à l'oral ; c'est souvent cela qu'ils entendent mal.")

    d.declencheur(
        'Écoute', "Combien de morceaux entendez-vous ?",
        pistes=[
            "Dites « maintenant » lentement : combien de syllabes ?",
            "Écoutez-le à vitesse normale : combien en reste-t-il ?",
            "Et « samedi » ? Et « acheter » ?",
            "Le mot a-t-il changé, ou seulement sa prononciation ?",
        ],
        notes="Faire l'expérience à voix haute avant toute explication. L'écart entre "
              "les deux comptages est le déclencheur de la séance.")

    d.regle("Le « e » qui tombe",
            "Au milieu d'un mot, quand une seule consonne le précède, le « e » s'efface.",
            precision="« Samedi » se dit « sam-di ». « Maintenant » se dit "
                      "« main-t'nant ». « Acheter » se dit « ach-té ». Le mot écrit ne "
                      "change pas ; la bouche, elle, saute la syllabe. C'est la "
                      "prononciation ordinaire, pas du relâchement.",
            notes="Diapositive à photographier. Insister : ce n'est pas familier ni "
                  "négligé. Un présentateur de radio le fait aussi.")

    d.tableau('Analyse', "Deux cas où le « e » se maintient toujours",
              ['Le cas', 'Des exemples'],
              [["Première syllabe, après p, b, t, d, k, g",
                "petit, demain, tenir, un degré, dehors"],
               ["Devant les sons « ri » et « li »",
                "un atelier, un hôtelier"],
               ["Et s'il y a deux consonnes devant",
                "appartement, justement, autrement - le « e » revient"]],
              cle=0,
              note="Partout ailleurs, au milieu du mot, il tombe.",
              notes="Ces consonnes s'appellent des occlusives : l'air est bloqué un "
                    "instant, puis relâché. Le mot technique n'est pas exigible, la "
                    "liste des six lettres l'est.")

    d.cartes("Le mot écrit et le mot entendu", "À écouter par paires", [
        ("petit", "« pe-tit » - le e se dit : première syllabe après un p."),
        ("samedi", "« sam-di » - le e tombe : une seule consonne devant."),
        ("demain", "« de-main » - le e se dit : première syllabe après un d."),
        ("maintenant", "« main-t'nant » - le e tombe : c'est cette forme qu'on entend à la radio."),
        ("un atelier", "« a-te-lier » - le e se dit : il est devant le son « li »."),
        ("franchement", "« franch'ment » - le e tombe."),
    ], notes="Faire écouter deux fois chaque mot dans l'activité interactive, puis "
             "répéter. Ne pas corriger la production : on travaille l'oreille.")

    d.piege("Croire qu'on a manqué un mot",
            "Il a dit un mot que je ne connais pas.",
            "Il a dit un mot que je connais, sans son « e ».",
            "C'est la première cause d'incompréhension à l'oral chez les adultes qui "
            "lisent pourtant très bien. L'élève cherche « samedi » dans sa mémoire et "
            "entend « samdi » : il conclut qu'il lui manque du vocabulaire, alors qu'il "
            "lui manque une forme. Entraîner l'oreille à la forme courte règle des "
            "dizaines de mots d'un coup.",
            notes="Piège central de la séance. Le nommer explicitement et y revenir "
                  "chaque fois qu'un élève dit « je n'ai pas compris ce mot ».")

    d.pratique('Discrimination', "On l'entend, ou il disparaît ?",
               "Écoutez chaque mot, puis classez-le.", [
        ("petit", "on l'entend"),
        ("samedi", "il disparaît"),
        ("un atelier", "on l'entend"),
        ("acheter", "il disparaît"),
        ("un degré", "on l'entend"),
        ("la semaine", "il disparaît"),
        ("dehors", "on l'entend"),
        ("franchement", "il disparaît"),
    ], corrige=True,
       notes="Corrigé à garder masqué au premier passage. Faire écouter, faire lever la "
             "main, puis dévoiler. « La semaine » surprend : le s n'est pas une "
             "occlusive, donc le e tombe malgré la première syllabe.")

    d.billet(
        "Écrivez trois mots où vous entendez le « e », et trois où il disparaît.",
        exemples=[
            "Vous pouvez reprendre des mots de la liste d'aujourd'hui.",
            "Dites-les à voix haute avant de les écrire.",
        ],
        notes="Deux minutes. Ramasser : les erreurs de classement disent quels cas "
              "reprendre en A3.")

    return d.save(dossier)
