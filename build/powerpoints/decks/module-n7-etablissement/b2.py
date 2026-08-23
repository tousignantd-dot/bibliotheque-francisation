# -*- coding: utf-8 -*-
"""B2 · Les sept parties de la lettre
Bloc B « Défi 1 · La lettre de motivation » · couleur ambre · 90 min.
Source : exercices `t1lettre` (type texte) et `t1plan`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre='Les sept parties de la lettre',
        chapeau="Une lettre formelle se juge en deux secondes, avant le "
                "premier mot : une date, un objet, des paragraphes séparés, "
                "une signature. La mise en page est de la politesse visible.",
        duree='90 minutes')

    d.titre(notes="Séance longue et très concrète. Distribuer la lettre modèle sur "
                  "papier et travailler dessus au crayon, partie par partie.")

    d.objectifs([
        "nommer les sept parties d'une lettre formelle et leur fonction ;",
        "écrire un objet de six ou sept mots, sans verbe conjugué ;",
        "répartir le contenu en trois paragraphes, un par idée ;",
        "choisir une formule de courtoisie qui laisse debout.",
    ], notes="Le quatrième objectif est celui que les élèves traduisent de leur "
             "langue, avec des résultats étranges. Insister : la formule se choisit "
             "dans une liste courte, elle ne s'invente pas.")

    d.declencheur(
        'Observation', "Que voyez-vous avant de lire ?",
        pistes=[
            "Y a-t-il une date ? un objet ?",
            "Les paragraphes sont-ils séparés ?",
            "Combien de temps donneriez-vous à cette lettre ?",
            "Et si vous en aviez soixante-huit à lire aujourd'hui ?",
        ],
        notes="Montrer deux lettres au projecteur, l'une bien disposée et l'autre en "
              "un seul bloc, sans les lire. Le groupe tranche en trois secondes, et "
              "c'est la démonstration de la séance.")

    d.tableau('Analyse', "Sept parties, sept fonctions",
              ['La partie', 'Ce qu\'elle fait'],
              [['lieu et date', "permettent de dire « ma lettre du 26 février »"],
               ["l'objet", "dit de quoi il s'agit, sans verbe conjugué"],
               ["l'appel", "s'adresse à quelqu'un : Madame, Monsieur,"],
               ['paragraphe 1', "la demande, et pourquoi cet établissement-là"],
               ['paragraphe 2', "les faits datés, et le trou expliqué"],
               ['paragraphe 3', "l'après-diplôme, et ce qui est déjà commencé"],
               ['la courtoisie', "ferme la lettre et reprend les mots de l'appel"]],
              cle=0,
              notes="Sept rangées, aucune note au bas : c'est la limite du contrôle de "
                    "densité. Diapositive à photographier — c'est le plan que les "
                    "élèves suivront en E2.")

    d.regle("Le premier paragraphe nomme l'établissement",
            "Une raison qui vaut pour tous les centres ne vaut pour aucun.",
            precision="« Votre établissement a une excellente réputation » se lit "
                      "soixante-huit fois par jour. « J'ai choisi votre centre parce "
                      "que le premier stage y a lieu avant Noël » se lit une fois — et "
                      "elle prouve que la fiche a été lue.",
            notes="Diapositive à photographier. Faire chercher, dans la fiche du "
                  "bloc A, une raison propre au centre : dix minutes, en équipes de "
                  "deux.")

    d.regle("Le troisième paragraphe est celui qui distingue",
            "Une formation contingentée cherche des personnes qui finissent.",
            precision="Dire où l'on va après le diplôme, et ce qu'on fait déjà pour y "
                      "arriver, sépare deux dossiers autrement identiques. C'est aussi "
                      "le paragraphe qu'on saute quand on écrit tard le soir.",
            notes="Faire écrire tout de suite deux phrases de ce paragraphe-là, avant "
                  "les deux autres : c'est le seul moyen qu'il existe.")

    d.pratique('Lecture', "À quoi sert chaque passage ?",
               "Retrouvez dans la lettre modèle le passage qui remplit chaque "
               "fonction.", [
        ("Il dit en six mots de quoi parle la lettre.", "l'objet"),
        ("Il annonce ce que la personne demande, et pour quand.", "la première phrase du paragraphe 1"),
        ("Il dit pourquoi ce centre-là plutôt qu'un autre.", "la deuxième phrase du paragraphe 1"),
        ("Il remplace l'adjectif « expérimentée ».", "cinq ans à l'unité prothétique, douze résidents"),
        ("Il explique le trou du parcours.", "deux années faites, l'établissement a fermé"),
        ("Il montre que l'organisation est réglée, pas souhaitée.", "l'horaire obtenu par écrit"),
    ], corrige=True,
       notes="Faire souligner dans la lettre plutôt que recopier. Corriger en "
             "projetant la lettre et en soulignant au fur et à mesure.")

    d.piege('Piège', "Merci beaucoup pour votre temps !",
            "Veuillez agréer, Madame, Monsieur, mes salutations distinguées.",
            "La première remercie d'avance de ce qui n'a pas encore été accordé, et "
            "ça se sent. Une formule de courtoisie ferme la lettre sans rien demander "
            "de plus.",
            notes="Donner trois formules acceptables au tableau et s'en tenir là. "
                  "Trois suffisent pour toute une vie de lettres formelles.")

    d.billet("Écris l'objet de ta propre lettre de motivation : six ou sept mots, "
             "sans verbe conjugué.",
             exemples=["Candidature au programme Santé, assistance et soins infirmiers",
                       "Candidature au diplôme en soutien informatique"],
             notes="Ramasser les billets et corriger uniquement la longueur et la "
                   "présence d'un verbe. Le contenu se travaille en E2.")

    return d.save(dossier)
