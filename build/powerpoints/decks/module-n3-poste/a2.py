# -*- coding: utf-8 -*-
"""A2 · Le « eu » de deux et le « eu » de neuf.
Bloc A « Je découvre » · couleur indigo (graphie-phonie) · 60 min.
Source : mini-leçon `prPhon`, exercice `prPhon` (cartes à écouter).

Les deux sons sont nommés par un mot repère — « le son de deux », « le son de
neuf ». L'alphabet phonétique reste dans le module interactif : sur une
diapositive projetée, il ne servirait à personne.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre='Le « eu » de deux et le « eu » de neuf',
        chapeau="Deux kilos, neuf heures, un peu, l'expéditeur : les mêmes "
                "deux lettres, deux sons différents. Et « deux heures » "
                "n'est pas « neuf heures ».",
        duree='60 minutes')

    d.titre(notes="Séance de phonétique. Prévoir les haut-parleurs : tout se joue à "
                  "l'oreille, et les élèves doivent entendre avant de voir écrit.")

    d.objectifs([
        "entendre la différence entre le son de « deux » et celui de « neuf » ;",
        "prononcer les deux sons en plaçant la bouche ;",
        "connaître la règle de la lettre qui suit ;",
        "dire une heure d'ouverture sans se faire comprendre de travers.",
    ])

    d.regle("Deux lettres, deux sons",
            "deux  ·  neuf",
            precision="Les lettres e et u ensemble ne se disent pas toujours de "
                      "la même façon. Dans « deux », la bouche est petite et "
                      "ronde. Dans « neuf », elle s'ouvre. Personne ne vous "
                      "corrigera si vous vous trompez, mais deux heures et neuf "
                      "heures ne sont pas la même heure.",
            notes="Diapo à photographier. Faire dire les deux mots l'un après l'autre, "
                  "lentement, en exagérant la forme de la bouche.")

    d.tableau('Analyse', "Où va la bouche ?",
              ['Le son', 'La bouche', 'Mots repères'],
              [["celui de « deux »", "arrondie, presque fermée, comme pour siffler",
                "deux, jeudi, un peu, mieux, monsieur"],
               ["celui de « neuf »", "plus ouverte, détendue",
                "neuf, une heure, plusieurs, l'expéditeur"]],
              cle=0,
              note="Les lèvres décident : petites et rondes, ou ouvertes.",
              notes="Faire prononcer les deux sons deux par deux, chacun regardant la "
                    "bouche de l'autre. La forme des lèvres se voit de loin.")

    d.regle("La règle qui décide presque toujours",
            "regarde ce qu'il y a APRÈS les lettres e-u",
            precision="Rien après, ou un e muet : le son est fermé, comme dans "
                      "« deux », « un peu », « jeudi ». Une consonne prononcée "
                      "après : le son est ouvert, comme dans « neuf », « une "
                      "heure », « l'expéditeur ».",
            notes="Diapo à photographier. Cette règle n'est pas parfaite dans toute la "
                  "langue, mais elle règle tous les mots du bureau de poste — le dire "
                  "au groupe, plutôt que de laisser croire à une loi absolue.")

    d.tableau('Graphie-phonie', "Ce qu'il y a après décide",
              ['Le mot', 'Après e-u', 'Le son'],
              [["deux", "rien", "fermé"],
               ["un peu", "rien", "fermé"],
               ["neuf", "un f prononcé", "ouvert"],
               ["une heure", "un r prononcé", "ouvert"],
               ["l'expéditeur", "un r prononcé", "ouvert"]],
              cle=2,
              note="Tous les mots en -eur ont le son ouvert : facteur, erreur, ordinateur.",
              notes="Diapo à photographier. Insister sur la famille des mots en -eur : "
                    "elle est immense et elle ne connaît pas d'exception utile.")

    d.pratique('Écoute', "Le son de « deux » ou le son de « neuf » ?",
               "Écoutez chaque mot, puis dites quel son vous entendez.", [
        ("deux", "le son de deux — fermé"),
        ("neuf", "le son de neuf — ouvert"),
        ("jeudi", "le son de deux — fermé"),
        ("une heure", "le son de neuf — ouvert"),
        ("un peu", "le son de deux — fermé"),
        ("l'expéditeur", "le son de neuf — ouvert"),
        ("monsieur", "le son de deux — fermé"),
        ("plusieurs", "le son de neuf — ouvert"),
    ], corrige=True, cols=2,
       notes="C'est l'exercice `prPhon` du module interactif, où chaque mot s'écoute. "
             "Le faire ici à la voix, puis le refaire à l'écran en A3.")

    d.pratique('Répétition', "Six phrases du bureau de poste",
               "Écoutez, puis répétez à voix haute.", [
        ("Ça ouvre à neuf heures, le jeudi.", "les deux sons dans la même phrase"),
        ("Deux kilos et cent grammes.", "son fermé"),
        ("L'expéditeur est en haut à gauche.", "son ouvert"),
        ("Elle parle un peu vite pour moi.", "son fermé"),
        ("Il y a plusieurs personnes devant moi.", "son ouvert"),
        ("Merci monsieur, bonne journée.", "son fermé"),
    ], corrige=True,
       notes="Faire répéter chaque phrase par tout le groupe, puis par un élève seul. "
             "La première phrase est la plus difficile : elle enchaîne les deux sons.")

    d.piege(
        "Prononciation",
        "à deux heures",
        "à neuf heures",
        "C'est le piège coûteux du module : vous arrivez sept heures trop tard, "
        "et l'erreur ne se voit qu'une fois devant une porte fermée. Devant une "
        "heure, répétez toujours pour vérifier : « Neuf heures ? Neuf ? »",
        notes="Demander qui a déjà manqué un rendez-vous à cause d'une heure mal "
              "comprise. Dédramatiser, puis donner la parade : faire répéter le chiffre.")

    d.vocabulaire('Graphie-phonie', "Les mots du module à prononcer", [
        ("deux", "son fermé — rien de prononcé après les lettres e-u"),
        ("jeudi", "son fermé — un des jours où beaucoup de gens vont à la poste"),
        ("un peu", "son fermé — « elle parle un peu vite »"),
        ("neuf", "son ouvert — le f se prononce, et l'heure d'ouverture"),
        ("une heure", "son ouvert — le r se prononce"),
        ("l'expéditeur", "son ouvert — comme facteur, erreur, ordinateur"),
    ], notes="Faire lire les six mots à voix haute en descendant la colonne : le son "
             "change exactement au milieu du tableau.")

    d.billet(
        "Écrivez l'heure d'ouverture d'un endroit près de chez vous, et dites-la à voix haute.",
        exemples=[
            "Est-ce que c'est le son de « deux » ou celui de « neuf » ?",
            "Neuf heures, deux heures, huit heures : lequel est le plus difficile pour vous ?",
        ],
        notes="Deux minutes. Passer entre les rangées et écouter les heures dites à voix "
              "basse : c'est là qu'on entend qui a compris la règle.")

    return d.save(dossier)
