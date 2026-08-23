# -*- coding: utf-8 -*-
"""D2 · Les mots qui tiennent une lettre debout
Bloc D « Défi 3 · La lettre qui règle » · couleur ambre · écriture et
grammaire · 75 min.
Source : exercices `t3conn`, `t3ponct` et `t3emph`, et leurs mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="Les mots qui tiennent une lettre debout",
        chapeau="Trois paragraphes posés l'un après l'autre ne font pas une "
                "lettre : ils font un empilement. Les connecteurs, la "
                "ponctuation et la mise en relief font le reste.",
        duree='75 minutes')

    d.titre(notes="Dernière séance avant les productions. Tout ce qui s'y apprend est "
                  "réemployé tel quel dans la lettre du bloc E.")

    d.objectifs([
        "annoncer un sujet avec quant à, en ce qui concerne ;",
        "refermer une explication avec autrement dit, en somme ;",
        "citer exactement, avec deux-points et guillemets ;",
        "mettre en relief avec c'est… qui, c'est… que, ce que… c'est.",
    ], notes="Trois savoirs en une séance, mais ils travaillent tous au même endroit : "
             "la lettre. Ne pas les traiter comme trois leçons séparées.")

    d.declencheur(
        'Observation', "Lis un paragraphe sans connecteurs. Qu'est-ce qui manque ?",
        pistes=[
            "Sais-tu de quoi il va parler avant de commencer ?",
            "Sais-tu ce qu'il faut retenir en le finissant ?",
            "Sais-tu ce que l'auteur en tire ?",
            "Qui fait ce travail, normalement ?",
        ],
        notes="Sans connecteurs, c'est le lecteur qui devine les liens. Avec, c'est "
              "l'auteur qui les pose — et il choisit ce qu'on retiendra.")

    d.cartes('Analyse', "Trois familles de connecteurs", [
        ("Annoncer le sujet", "Quant à… · En ce qui concerne… · À propos de… Ces mots ouvrent un paragraphe."),
        ("Redire plus court", "Autrement dit… · En somme… On referme une explication longue en dix mots."),
        ("Tirer la suite", "Par conséquent… à l'écrit formel · Donc… à l'oral. Jamais les deux dans la même lettre."),
    ], cols=3,
       notes="Trois ou quatre connecteurs par page, jamais un par phrase. Au-delà, la "
             "lettre se lit comme un devoir d'école et perd son autorité.")

    d.regle("Les deux-points suivis de guillemets",
            "Ils annoncent les mots exacts de quelqu'un.",
            precision="« Vous m'aviez dit : “ Revenez me le dire si ça ne suffit pas. ” » "
                      "C'est la partie la plus solide d'une lettre, à une condition : "
                      "ce qui est entre guillemets doit être exact. Si vous n'êtes pas "
                      "sûr des mots, écrivez « vous m'aviez dit que… » sans guillemets. "
                      "Un résumé honnête vaut mieux qu'une citation approximative.",
            notes="Diapositive à photographier. Ce point-là peut coûter un dossier : "
                  "une citation fausse fait perdre la crédibilité de tout le reste.")

    d.tableau('Analyse', "Trois signes, trois emplois",
              ['Le signe', 'Ce qu\'il fait'],
              [["Deux-points et guillemets", "annoncent des mots exacts"],
               ["Point-virgule", "relie deux idées qu'un point séparerait trop"],
               ["Tiret", "ouvre chaque terme d'une liste verticale"],
               ["Après un point-virgule", "une minuscule, jamais une majuscule"],
               ["Dans une liste à tirets", "un point-virgule par ligne, un point à la fin"]],
              cle=0,
              notes="Diapositive à photographier. La liste à tirets est ce qui rend une "
                    "demande impossible à contourner : chaque ligne appelle sa réponse.")

    d.tableau('Analyse', "Mettre en relief : la phrase choisit à la place du lecteur",
              ['Phrase ordinaire', 'Phrase mise en relief'],
              [["L'appareil me réveille.", "C'est l'appareil qui me réveille."],
               ["Je me plains du matin.", "C'est du matin que je me plains."],
               ["La répétition me dérange.", "Ce qui me dérange, c'est la répétition."],
               ["Je veux dormir.", "Ce que je veux, c'est dormir."],
               ["Le bruit de l'escalier a cessé.", "Le bruit de l'escalier, lui, a cessé."]],
              cle=1,
              notes="Diapositive à photographier. Deux mises en relief par lettre "
                    "suffisent : au-delà, l'effet s'annule.")

    d.piege('Grammaire',
            "C'est moi qui a écrit la lettre",
            "C'est moi qui ai écrit la lettre",
            "Le pronom relatif « qui » reprend l'élément encadré : le verbe s'accorde "
            "avec lui, pas avec « c'est ». C'est moi qui ai, c'est vous qui avez, ce "
            "sont eux qui ont. Autre test utile : si l'élément encadré est le sujet, "
            "c'est « qui » ; sinon, c'est « que ».",
            notes="Faire produire cinq phrases avec « c'est moi qui » à la première "
                  "personne. C'est l'accord le plus souvent raté du niveau.")

    d.pratique('Pratique', "Complétez la lettre",
               "Connecteur, ponctuation ou mise en relief, selon la phrase.", [
        ("___ à une diminution de loyer, ce n'est pas ce que je recherche.", "Quant"),
        ("En ce qui ___ le déplacement de l'appareil, rien n'a bougé.", "concerne"),
        ("___ dit, deux des trois mesures convenues ont été prises.", "Autrement"),
        ("Le bruit persiste ; ___ conséquent, je m'adresse à vous.", "par"),
        ("Le caoutchouc a été posé ___ l'appareil, lui, n'a pas bougé.", "point-virgule"),
        ("Vous m'aviez dit ___ Revenez me le dire. ___", "deux-points et guillemets"),
        ("La répétition me dérange. — rapporté : ___ me dérange, c'est la répétition.", "Ce qui"),
        ("C'est moi ___ ai écrit la lettre.", "qui"),
    ], corrige=True,
       notes="Faire relire les huit phrases à la suite : c'est le squelette de la "
             "lettre que le groupe écrira en E2.")

    d.billet(
        "Écris la phrase de ta lettre qui dit ce qui compte vraiment pour toi.",
        exemples=[
            "Emploie « Ce qui… , c'est » ou « Ce que… , c'est ».",
            "Une seule phrase, et pas un adjectif de trop.",
        ],
        notes="Deux minutes. Fin du défi 3. Les réponses se reprennent telles quelles "
              "dans la lettre de E2.")

    return d.save(dossier)
