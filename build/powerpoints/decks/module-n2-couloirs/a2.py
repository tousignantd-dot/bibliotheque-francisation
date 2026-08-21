# -*- coding: utf-8 -*-
"""A2 · Quatorze ou quarante ?
Bloc A « Je découvre » · couleur indigo · 75 min. Séance de graphie-phonie.
Source : exercice `prSons`, mini-leçon `prSons`, dialogue `t1b`.

Le savoir de phonétique du niveau 2 porte ici sur les nombres, et ce n'est
pas un choix de style : dans un bâtiment, tout ce qui guide est un chiffre.
Un élève qui entend « quarante » quand on lui dit « quatorze » monte deux
étages pour rien.

On ne fait donc pas de l'alphabet phonétique : on fait entendre des paires,
et on fait répéter des numéros de porte réels.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-couloirs/images/')


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Quatorze ou quarante ?",
        chapeau="Entendre la différence entre les nombres qui se ressemblent, "
                "et dire un numéro de local sans se tromper.",
        duree='75 minutes')

    d.titre(notes="Séance d'oreille. Prévoir beaucoup d'écoute et peu de lecture. "
                  "Le tableau sert à écrire les chiffres, pas les mots.")

    d.objectifs([
        "compter de un à vingt à voix haute ;",
        "distinguer deux et douze, trois et treize, quatre et quatorze ;",
        "entendre la différence entre quatorze et quarante ;",
        "redire un numéro de local pour le vérifier.",
    ])

    d.declencheur(
        'Écoute', "Quel numéro est-ce que vous entendez ?",
        image=IMG + 'ascenseur-porte.jpg',
        pistes=[
            "Deux, ou douze ?",
            "Quatre, ou quatorze ?",
            "Quatorze, ou quarante ?",
            "Comment on fait pour être sûr ?",
        ],
        notes="Dire chaque paire deux fois, sans rien écrire au tableau. La quatrième "
              "piste amène la réponse du module : on répète le numéro à voix haute.")

    d.tableau('Analyse', "Les quatre paires à ne plus confondre",
              ["Avant dix", "Après dix"],
              [["deux", "douze"],
               ["trois", "treize"],
               ["quatre", "quatorze"],
               ["six", "seize"]],
              cle=1,
              note="Les grands nombres finissent presque tous sur le son « z ».",
              notes="Diapositive à photographier. Faire lire la colonne de gauche et "
                    "dire celle de droite : c'est l'exercice, en une page.")

    d.regle("Onze, douze, treize, quatorze, quinze, seize",
            "Ce ne sont pas « dix et quelque chose » : ce sont des mots à eux.",
            precision="Un élève qui construit « deux-ze » pour douze ne sera jamais "
                      "compris. Ces six nombres s'apprennent par cœur, comme six mots "
                      "de vocabulaire. À partir de <b>dix-sept</b>, la règle change et "
                      "le nombre se construit vraiment.",
            notes="Diapositive à photographier. Faire compter le groupe de un à vingt, "
                  "en chœur puis un par un, trois fois dans la séance.")

    d.piege('Le piège du jour',
            "« quaranze »",
            "quatorze, ou quarante",
            "Quator<b>ze</b> est 14, quaran<b>te</b> est 40, et le mot « quaranze » "
            "n'existe pas. Au Centre Bellevue, le 214 existe et le 240 n'existe pas : "
            "c'est exactement l'erreur que Soraya fait, et elle monte un étage pour "
            "rien.",
            notes="Faire entendre les deux versions, la fausse d'abord, la juste "
                  "ensuite. Le groupe rit, et il retient.")

    d.pratique('Écoute', "Avant dix, ou après dix ?",
               "Écoutez chaque nombre et levez la main si c'est un grand nombre.", [
        ("deux", "avant dix"),
        ("douze", "après dix"),
        ("trois", "avant dix"),
        ("treize", "après dix"),
        ("quatre", "avant dix"),
        ("quatorze", "après dix"),
        ("six", "avant dix"),
        ("seize", "après dix"),
    ], corrige=True, cols=2,
       notes="Huit nombres, dits lentement, deux fois chacun. Les mains levées disent "
             "tout de suite qui suit et qui devine.")

    d.dialogue('Dialogue', "Le local qui n'existe pas", [
        ("SORAYA", "Monsieur, le 240, c'est où ?", True),
        ("GILLES", "Le 240 ? Il n'y a pas de 240 ici.", True),
        ("SORAYA", "Ah… Sur ma feuille, c'est écrit 214.", True),
        ("GILLES", "Écoutez la fin du mot : quatorze, quarante.", True),
    ], consigne="Écoutez, puis dites où est l'erreur.",
       notes="Le dialogue met en scène l'erreur au lieu de l'expliquer. Demander au "
             "groupe à quel moment exact Soraya se trompe.")

    d.pratique('Pratique · à deux', "Le jeu des numéros",
               "Un élève dit, l'autre écrit. Puis on échange.", [
        ("Étape 1", "A dit un numéro de local du centre. B l'écrit en chiffres."),
        ("Étape 2", "B redit le numéro à voix haute pour vérifier."),
        ("Étape 3", "On compare avec ce que A avait en tête."),
        ("Étape 4", "On recommence avec les numéros de la vraie liste du groupe."),
    ], cols=1,
       notes="Vingt minutes. L'étape 2 est le cœur : c'est la stratégie que le module "
             "installe, et elle sert bien au-delà du centre.")

    d.billet(
        "Écrivez en lettres les quatre nombres que vous entendez le plus souvent au centre.",
        exemples=[
            "quatorze",
            "douze",
            "quinze",
            "huit",
        ],
        notes="Devoir court. Corriger l'orthographe sans insister : ce qui compte "
              "aujourd'hui, c'est que le nombre entendu soit le bon.")

    return d.save(dossier)
