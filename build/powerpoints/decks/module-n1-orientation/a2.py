# -*- coding: utf-8 -*-
"""A2 · Trois sons : [a], [i], [ou].
Bloc A « Je découvre » · couleur indigo (graphie-phonie) · 60 min.
Source : exercice `prSons` (cartes à écouter) et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre='Trois sons pour commencer',
        chapeau="Le français a beaucoup de sons. Trois se disent dans presque "
                "tous les mots du centre, et ce sont les trois plus faciles.",
        duree='60 minutes')

    d.titre(notes="Séance d'écoute. Prévoir le son. Écrire les trois lettres au tableau "
                  "avant l'arrivée du groupe — a, i, ou — et les laisser affichées.")

    d.objectifs([
        "entendre la différence entre [a], [i] et [ou] ;",
        "reconnaître les lettres qui les écrivent ;",
        "comprendre que « ou » fait un seul son ;",
        "dire six mots du centre à voix haute.",
    ])

    d.declencheur(
        'Écoute', "Ces deux mots sont-ils pareils ?",
        pistes=[
            "la — lit",
            "la — loup",
            "lit — loup",
            "Qu'est-ce qui change : la bouche, ou la voix ?",
        ],
        notes="Faire écouter chaque paire deux fois. Demander de lever la main quand "
              "les deux mots sont différents. Ne pas encore montrer l'écriture.")

    d.tableau('Analyse', "Trois sons, trois bouches",
              ['On entend', 'La bouche'],
              [["[a]", "grande ouverte"],
               ["[i]", "étirée, comme un sourire"],
               ["[ou]", "les lèvres en rond, en avant"]],
              cle=0,
              note="Se regarder dans une vitre en le disant : la bouche se voit.",
              notes="Diapositive à photographier. Faire produire les trois sons en "
                    "chœur, longuement, sans mot autour : aaaa, iiii, ouou.")

    d.tableau('Analyse', "Comment ça s'écrit",
              ['Le son', "Les lettres"],
              [["[a]", "a"],
               ["[i]", "i, et parfois y"],
               ["[ou]", "o + u, ensemble"]],
              cle=1,
              note="« ou » prend deux lettres et fait un seul son.",
              notes="C'est la première chose surprenante de l'écriture française. La "
                    "dire clairement maintenant fait gagner des semaines plus tard.")

    d.regle("ou fait un seul son",
            "Deux lettres, une seule bouche.",
            precision="On écrit <b>o</b> puis <b>u</b>, mais on ne dit pas « o-u » : "
                      "on dit un seul son, les lèvres en rond. "
                      "<b>l<u>ou</u>p</b> · <b>n<u>ou</u>s</b> · "
                      "<b>p<u>ou</u>ssez</b>.",
            notes="Diapositive à photographier. Faire lire les trois mots en chœur, "
                  "puis un par un.")

    d.vocabulaire('Vocabulaire', "Six mots du centre",
                  [("la salle", "[a] deux fois"),
                   ("la cafétéria", "[a] trois fois"),
                   ("ici", "[i] deux fois"),
                   ("la sortie", "[i] à la fin"),
                   ("poussez", "[ou] au début"),
                   ("nous", "[ou] à la fin")],
                  notes="Faire répéter chaque mot deux fois. Demander où est le son : "
                        "au début, au milieu, à la fin.")

    d.pratique('Écoute', "Quel son entendez-vous ?",
               "Écoutez le mot. [a], [i] ou [ou] ?", [
        ("la", "[a]"),
        ("lit", "[i]"),
        ("loup", "[ou]"),
        ("salle", "[a]"),
        ("sortie", "[i]"),
        ("poussez", "[ou]"),
    ], corrige=True, cols=2,
       notes="Même exercice que dans l'activité interactive : ils le retrouveront "
             "sur l'écran et le réussiront plus vite.")

    d.piege("Lire « ou » en deux sons",
            "« o-u », en deux temps.",
            "« ou », les lèvres en rond, d'un seul coup.",
            "C'est le piège numéro un de la lecture au début. Deux lettres qui font "
            "un seul son, il y en a d'autres en français — mais celle-ci est la "
            "première qu'on rencontre, et elle est dans « poussez », qui est écrit "
            "sur la moitié des portes du centre.",
            notes="Revenir à ce piège chaque fois qu'un élève bute sur « ou » dans "
                  "les séances suivantes.")

    d.billet(
        "Écrivez trois mots : un avec [a], un avec [i], un avec [ou].",
        exemples=[
            "Vous pouvez prendre les mots de la séance.",
            "Soulignez la lettre qui fait le son.",
        ],
        notes="Deux minutes. Ramasser : c'est le seul relevé écrit du bloc A, et il "
              "dit qui décode déjà et qui n'y est pas encore.")

    return d.save(dossier)
