# -*- coding: utf-8 -*-
"""C1 · Poussez, tirez.
Bloc C « Défi 2 · Le panneau qui dit quoi faire » · couleur acier · 75 min.
Source : dialogue `t2`, exercices `t2vf` et `t2ordre`, mini-leçon `t2ordre`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre='Poussez, tirez',
        chapeau="Certains panneaux ne nomment aucun endroit : ils disent quoi "
                "faire, tout de suite, et ils finissent tous pareil.",
        duree='75 minutes')

    d.titre(notes="Première séance du Défi 2. Prévoir une vraie porte : la séance se "
                  "termine debout, la main sur la poignée.")

    d.objectifs([
        "comprendre POUSSEZ, TIREZ et ENTREZ ;",
        "faire le geste que le panneau demande ;",
        "reconnaître la terminaison -EZ ;",
        "savoir que le Z ne se prononce pas.",
    ])

    d.declencheur(
        'Observation', "Que faites-vous devant cette porte ?",
        pistes=[
            "La porte ne s'ouvre pas.",
            "Un mot est écrit dessus : TIREZ.",
            "Qu'est-ce que vous faites ?",
            "Et si c'était écrit POUSSEZ ?",
        ],
        notes="Presque tout le groupe aura déjà vécu la scène. Laisser raconter : ça "
              "dédramatise, et ça installe le vocabulaire tout seul.")

    d.dialogue('Dialogue', "La porte ne s'ouvre pas", [
        ("ROSA", "La porte ne s'ouvre pas.", True),
        ("KOFI", "C'est écrit un mot dessus. Regarde.", True),
        ("ROSA", "TIREZ. Ça veut dire quoi ?", True),
        ("KOFI", "Tirez, c'est vers toi. Poussez, c'est loin de toi.", True),
        ("ROSA", "Ah ! Comme ça. Ça marche !", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Faire mimer les deux gestes pendant l'écoute, sans parler. Le geste "
             "s'apprend avant le mot.")

    d.regle("Un mot, un geste",
            "Le panneau demande quelque chose.",
            precision="<b>POUSSEZ</b> : la porte va loin de moi, la main pousse. "
                      "<b>TIREZ</b> : la porte vient vers moi, la main ramène. "
                      "<b>ENTREZ</b> : on peut entrer sans frapper.",
            notes="Diapositive à photographier. Faire faire les trois gestes debout, "
                  "en chœur, en disant le mot.")

    d.tableau('Analyse', "Tous finissent par -EZ",
              ['On écrit', 'On entend'],
              [["poussez", "pou-ssé"],
               ["tirez", "ti-ré"],
               ["entrez", "en-tré"],
               ["attendez", "a-tten-dé"]],
              cle=1,
              note="Le Z de la fin ne se prononce jamais.",
              notes="Diapositive à photographier. Cette terminaison revient partout en "
                    "français, bien au-delà des panneaux : la reconnaître maintenant "
                    "fait gagner des mois.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("La porte ne s'ouvre pas tout de suite.", "vrai"),
        ("Sur la porte, c'est écrit POUSSEZ.", "faux — c'est écrit TIREZ"),
        ("« Tirez » veut dire : vers moi.", "vrai"),
        ("Le petit dessin rouge montre une cigarette.", "vrai"),
    ], corrige=True, cols=1,
       notes="Quatre énoncés. Le quatrième prépare la séance C2.")

    d.pratique('Pratique', "Poussez, tirez ou entrez ?",
               "Complétez le mot du panneau.", [
        ("La porte va de l'autre côté.", "poussez"),
        ("La porte vient vers moi.", "tirez"),
        ("Le bureau est ouvert.", "entrez"),
        ("Les trois mots finissent par…", "-ez"),
    ], corrige=True, cols=1,
       notes="Court. Le vrai exercice est celui qui suit, debout.")

    d.piege("Tirer une porte qui dit POUSSEZ",
            "On tire, la porte résiste, on insiste.",
            "On regarde la poignée avant de toucher.",
            "Tout le monde le fait, y compris les gens nés ici. Un indice matériel "
            "vaut le mot : une <b>plaque de métal plate</b> se pousse, une <b>vraie "
            "poignée</b> se tire. Les portes bien faites le disent sans écrire.",
            notes="Aller vérifier sur trois portes du corridor. C'est la meilleure "
                  "minute de la séance.")

    d.pratique('Pratique · debout', "Le tour des portes",
               "En groupe, dans le corridor. Quinze minutes.", [
        ("Étape 1", "Trouvez une porte avec un mot écrit dessus."),
        ("Étape 2", "Lisez le mot à voix haute."),
        ("Étape 3", "Faites le geste, puis ouvrez."),
        ("Étape 4", "Regardez la poignée : plaque plate, ou poignée ?"),
    ], cols=1,
       notes="Sortir vraiment. Faire passer chaque élève au moins une fois.")

    d.billet(
        "Écrivez les trois mots des panneaux, et le geste de chacun.",
        exemples=[
            "POUSSEZ — …",
            "TIREZ — …",
            "ENTREZ — …",
        ],
        notes="Deux minutes. Accepter le geste décrit dans n'importe quels mots.")

    return d.save(dossier)
