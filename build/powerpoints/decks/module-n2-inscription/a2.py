# -*- coding: utf-8 -*-
"""A2 · Comment ça s'écrit ?
Bloc A « Je découvre » · couleur indigo · 75 min. Séance de graphie-phonie.
Source : exercice `prAlpha`, mini-leçon `prAlpha`, dialogue `t2b`.

Le savoir de phonétique du niveau 2 porte ici sur le nom des lettres, et ce
n'est pas un choix de style : au comptoir, personne ne connaît le nom de
l'élève, et c'est lui qui doit le faire écrire juste. Un nom mal orthographié
le suivra sur tous les papiers du centre pendant des années.

L'épellation existe déjà au niveau 1, dans `module-n1-presenter` : elle y sert
à se présenter. Ici, elle sert à faire écrire — ce n'est plus une politesse,
c'est une correction.

On ne fait pas d'alphabet phonétique : on fait entendre deux familles de
lettres, et on fait épeler de vrais noms.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-inscription/images/')


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Comment ça s'écrit ?",
        chapeau="Dire le nom des lettres, épeler son nom lentement, et faire "
                "corriger quand c'est mal écrit.",
        duree='75 minutes')

    d.titre(notes="Séance d'oreille et de bouche. Prévoir beaucoup d'écoute et peu de "
                  "lecture. Le tableau sert à écrire les lettres une à une, pendant que "
                  "les élèves les disent.")

    d.objectifs([
        "dire le nom des vingt-six lettres ;",
        "reconnaitre la famille du « é » et celle du « è » ;",
        "épeler son nom de famille lentement ;",
        "dire « B comme bonjour » quand la personne hésite.",
    ])

    d.declencheur(
        'Écoute', "Quelle lettre est-ce que vous entendez ?",
        pistes=[
            "B, ou V ?",
            "M, ou N ?",
            "G, ou J ?",
            "Comment on fait pour être sûr ?",
        ],
        notes="Dire chaque paire deux fois, sans rien écrire au tableau. La quatrième "
              "piste amène la réponse du module : on ajoute un mot connu derrière la "
              "lettre.")

    d.tableau('Analyse', "L'alphabet se dit en deux familles",
              ["La lettre vient avant le son", "Le son vient avant la lettre"],
              [["B, C, D — « bé », « cé », « dé »", "F, L, M — « èf », « èl », « èm »"],
               ["G, P, T — « gé », « pé », « té »", "N, R, S — « èn », « èr », « ès »"],
               ["V — « vé »", "Ces six-là commencent par « è »"]],
              cle=0,
              note="Sept lettres finissent sur « é ». Six commencent par « è ».",
              notes="Diapositive à photographier. Faire lire la colonne de gauche en "
                    "chœur, puis celle de droite. La différence s'entend tout de suite.")

    d.regle("« B comme bonjour, D comme dimanche »",
            "Un mot connu derrière la lettre, et le doute disparaît.",
            precision="Quand la personne au comptoir hésite entre deux lettres, "
                      "répéter la lettre ne sert à rien : elle l'entend déjà mal. On "
                      "ajoute un mot que tout le monde connaît. Chacun choisit ses "
                      "mots une fois et les garde toute l'année.",
            notes="Diapositive à photographier. Faire choisir à chacun un mot pour B, "
                  "V, M et N, et l'écrire dans son cahier. Un mot familier vaut mieux "
                  "qu'un mot juste.")

    d.piege('Le piège du jour',
            "« ma lettre E se dit i »",
            "en français, E se dit « eu » et I se dit « i »",
            "En anglais, le E se dit « i » et le I se dit « aïe ». Un élève qui garde "
            "l'alphabet anglais fait écrire son nom avec les mauvaises voyelles, et "
            "personne ne s'en aperçoit avant la carte d'étudiant. C'est l'erreur la "
            "plus fréquente au comptoir.",
            notes="Faire entendre les deux versions, l'anglaise d'abord, la française "
                  "ensuite. Beaucoup d'élèves découvrent ici que leur alphabet n'est "
                  "pas celui d'ici.")

    d.pratique('Écoute', "Son « é » ou son « è » ?",
               "Écoutez chaque lettre et levez la main pour la famille du « è ».", [
        ("la lettre B", "son « é »"),
        ("la lettre F", "son « è »"),
        ("la lettre D", "son « é »"),
        ("la lettre M", "son « è »"),
        ("la lettre P", "son « é »"),
        ("la lettre S", "son « è »"),
        ("la lettre T", "son « é »"),
        ("la lettre L", "son « è »"),
    ], corrige=True, cols=2,
       notes="Huit lettres, dites lentement, deux fois chacune. Les mains levées disent "
             "tout de suite qui suit et qui devine.")

    d.dialogue('Dialogue', "Deux D, pas deux B", [
        ("MME BOURGEOIS", "Haddad… Comment ça s'écrit ?", True),
        ("YARA", "H, A, deux D, A, D.", True),
        ("MME BOURGEOIS", "Deux D ? Doucement, s'il vous plaît.", True),
        ("YARA", "H. A. D. D. A. D.", True),
        ("MME BOURGEOIS", "B comme bonjour ou D comme dimanche ?", True),
        ("YARA", "D comme dimanche.", True),
    ], consigne="Écoutez, puis dites à quel moment il y a un doute.",
       notes="Le dialogue met en scène le doute au lieu de l'expliquer. Demander au "
             "groupe qui règle le problème : c'est Yara, pas la secrétaire.")

    d.pratique('Pratique · à deux', "Le jeu des noms",
               "Un élève épelle, l'autre écrit. Puis on échange.", [
        ("Étape 1", "A épelle son nom de famille, une lettre par seconde."),
        ("Étape 2", "B l'écrit sans poser de question."),
        ("Étape 3", "A regarde et dit « c'est bien écrit » ou corrige la lettre."),
        ("Étape 4", "On recommence avec le nom de sa rue."),
    ], cols=1,
       notes="Vingt minutes. L'étape 3 est le cœur : c'est la stratégie que le module "
             "installe, et elle sert bien au-delà du centre. Passer dans les rangées "
             "pour attraper ceux qui vont trop vite.")

    d.billet(
        "Écrivez votre nom de famille lettre par lettre, et un mot pour deux lettres difficiles.",
        exemples=[
            "H, A, deux D, A, D",
            "B comme bonjour",
            "V comme vendredi",
        ],
        notes="Devoir court. Demander de l'apprendre par cœur : au comptoir, on n'a pas "
              "son cahier dans les mains.")

    return d.save(dossier)
