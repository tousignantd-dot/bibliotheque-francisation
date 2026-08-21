# -*- coding: utf-8 -*-
"""C4 · Le compte rendu : décision, responsable, échéance.
Bloc C « Défi 2 » · couleur ambre · 75 min. Fin du Défi 2.
Source : exercices `t2cr` et `t2dir`, et leurs mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre="Le compte rendu",
        chapeau="Personne ne relira ce que chacun a dit. Ce qu'on cherche "
                "dans un compte rendu, trois semaines plus tard, c'est : "
                "qu'est-ce qui a été décidé, qui le fait, pour quand.",
        duree='75 minutes')

    d.titre(notes="Deuxième production écrite du module. Une réunion d'une heure tient "
                  "en une demi-page : le dire d'emblée, c'est la moitié de la leçon.")

    d.objectifs([
        "rapporter au passé une parole entendue au présent ;",
        "adapter les pronoms et les repères de temps ;",
        "transformer une question directe en question rapportée ;",
        "écrire une ligne de décision : quoi, qui, quand.",
    ], notes="Les trois premiers objectifs sont grammaticaux, le quatrième est "
             "professionnel. C'est le quatrième qui sera évalué.")

    d.regle("Une ligne de compte rendu",
            "Ce qui a été décidé — qui le fait — pour quand.",
            precision="Rien d'autre. Une ligne qui ne porte pas ces trois informations "
                      "n'est pas une décision : c'est une discussion. Exemple : "
                      "« Demander à Lachance un prix sur une liste courte — N. Kessab — "
                      "12 septembre. » Court, daté, vérifiable un mois plus tard.",
            notes="Diapositive à photographier. C'est le format exact attendu au devoir.")

    d.tableau('Analyse · 1 de 2', "Le recul des temps",
              ['Ce qui a été dit', 'Ce qui s\'écrit'],
              [["« Je vérifie »", "elle a précisé qu'elle vérifiait"],
               ["« J'ai fait le calcul »", "elle a indiqué qu'elle avait fait le calcul"],
               ["« On tranchera »", "elle a annoncé qu'on trancherait"]],
              cle=1,
              note="Quand le verbe introducteur est au passé, tout recule d'un cran.",
              notes="Diapositive à photographier. Si le verbe introducteur est au "
                    "présent, rien ne recule : c'est le passé qui déclenche.")

    d.tableau('Analyse · 2 de 2', "Les pronoms et les repères",
              ['Dans la salle', 'Dans le compte rendu'],
              [["je", "elle, il, ou le nom"],
               ["aujourd'hui · demain · hier", "ce jour-là · le lendemain · la veille"],
               ["ici · ce bureau-ci", "là · ce bureau-là"]],
              cle=1,
              note="Un compte rendu qui garde « demain » oblige le lecteur à retrouver la date de la réunion.",
              notes="C'est l'oubli le plus fréquent, et le plus coûteux : le lecteur du "
                    "compte rendu n'était pas dans la salle.")

    d.cartes("Le verbe porte l'intention", "Ne pas écrire « a dit » huit fois", [
        ("a rappelé", "l'information était déjà connue du groupe"),
        ("a précisé", "il manquait un détail, il l'a fourni"),
        ("a objecté", "il n'était pas d'accord, et il l'a dit"),
        ("a proposé", "il a avancé une solution, sans l'imposer"),
        ("s'est engagé à", "il le fera — et un mois plus tard, on s'en souviendra"),
        ("a reconnu", "il a admis un point, souvent contre son propre intérêt"),
    ], notes="Choisir le bon verbe est un acte de rédaction, pas de style : « a "
             "proposé » et « s'est engagé à » n'ont pas les mêmes conséquences.")

    d.piege("Rapporter la question telle quelle",
            "Il a demandé est-ce qu'elle était sûre ?",
            "Il lui a demandé si elle était sûre.",
            "La question rapportée n'est plus une question : elle perd l'inversion, le "
            "« est-ce que » devient « si », et le point d'interrogation disparaît. La "
            "faute est très visible parce qu'elle laisse dans le texte un mot qui n'a "
            "plus de raison d'être.",
            notes="Faire transformer trois questions du dialogue de C1 avant de passer "
                  "à l'exercice.")

    d.pratique('Grammaire', "Au discours rapporté",
               "Transformez la parole en phrase de compte rendu.", [
        ("« Je vérifie deux fois. »", "Elle a précisé qu'elle vérifiait deux fois."),
        ("« Ça me force à doubler mon stock. »", "Il a objecté que cela le forçait à doubler son stock."),
        ("« Es-tu sûre de ton affaire ? »", "Il lui a demandé si elle était sûre."),
        ("« On tranche à la réunion du seize. »", "Elle a annoncé qu'on trancherait le seize."),
        ("« J'ai fait le calcul. »", "Elle a indiqué qu'elle avait fait le calcul."),
        ("« C'est ma faute. »", "Elle a reconnu que c'était sa faute."),
        ("« Je note les trois décisions. »", "Elle s'est engagée à noter les trois décisions."),
    ], corrige=True,
       notes="Accepter tout verbe introducteur juste. Corriger le temps et les pronoms, "
             "qui sont la vraie matière de l'exercice.")

    d.pratique('Rédaction', "Les trois lignes de décision",
               "Manon a donné trois consignes. Écrivez-les au format : quoi — qui — quand.", [
        ("La demande de prix à Lachance", "Demander un prix sur une liste courte — N. Kessab — 12 septembre"),
        ("Le calcul d'espace", "Chiffrer l'espace du stock doublé — Y. Boudreault — 12 septembre"),
        ("Le choix du fournisseur", "Décision reportée à la réunion du 16 septembre"),
    ], corrige=True,
       notes="La troisième ligne est celle qu'on oublie : ne pas trancher est aussi une "
             "décision, et elle se note.")

    d.billet(
        "Rédigez le compte rendu complet de la réunion, en une demi-page.",
        exemples=[
            "Deux phrases de contexte, puis les trois lignes de décision.",
            "Aucune parole rapportée mot à mot.",
        ],
        notes="Travail à remettre. Deuxième des trois productions écrites du module.")

    return d.save(dossier)
