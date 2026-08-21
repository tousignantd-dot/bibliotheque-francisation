# -*- coding: utf-8 -*-
"""B1 · Qu'est-ce que vous avez, madame ?
Bloc B « Défi 1 · Dire ce qui ne va pas » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t1vf`.

C'est la première des deux intentions que le programme donne à cette
situation en production orale : « décrire un problème de santé courant ».
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-pharmacie/images/')


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Qu'est-ce que vous avez, madame ?",
        chapeau="Le pharmacien pose toujours les mêmes questions, dans le "
                "même ordre. Trois phrases courtes suffisent pour y répondre — "
                "à condition de les avoir dans la bouche avant d'en avoir besoin.",
        duree='75 minutes')

    d.titre(notes="Première séance du défi 1. C'est l'intention que le programme met au "
                  "centre de cette situation au niveau 3 : décrire un problème de santé "
                  "courant. Tout le bloc B y revient.")

    d.objectifs([
        "comprendre les questions du pharmacien ;",
        "dire son malaise en une phrase ;",
        "répondre au sujet de la fièvre et des autres médicaments ;",
        "reconnaître le conseil « allez voir un médecin ».",
    ])

    d.declencheur(
        'Observation', "Que se passe-t-il à ce comptoir ?",
        image=IMG + 'comptoir-fond.jpg',
        pistes=[
            "Qui parle en premier, le client ou le pharmacien ?",
            "Quelles questions le pharmacien va-t-il poser ?",
            "Est-ce qu'il faut tout raconter, ou seulement l'essentiel ?",
        ],
        notes="Faire deviner les questions avant d'écouter le dialogue. Le groupe en "
              "trouve souvent trois sur quatre : la séance sert alors à confirmer.")

    d.dialogue('Dialogue · 1 de 3', "J'aurais besoin d'un conseil", [
        ("NADIA", "Bonjour. J'aurais besoin d'un conseil, s'il vous plaît.", True),
        ("ÉTIENNE", "Bonjour. Qu'est-ce que je peux faire pour vous ?", True),
        ("NADIA", "Je tousse beaucoup. La nuit, je ne dors pas.", True),
        ("ÉTIENNE", "Depuis quand est-ce que ça dure ?", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Noter la première phrase de Nadia : elle annonce ce qu'elle veut avant de "
             "raconter. C'est la façon la plus rapide de se faire comprendre.")

    d.dialogue('Dialogue · 2 de 3', "Les questions du pharmacien", [
        ("NADIA", "Depuis quatre jours. Ça a commencé samedi.", True),
        ("ÉTIENNE", "Est-ce que vous avez de la fièvre ?", True),
        ("NADIA", "Un peu, hier soir. Aujourd'hui, non.", True),
        ("ÉTIENNE", "Est-ce que vous avez mal à la gorge, ou mal à la tête ?", True),
    ], notes="Trois questions d'affilée : la durée, la fièvre, la douleur. Les faire "
             "repérer et compter par le groupe.")

    d.dialogue('Dialogue · 3 de 3', "Et si ça continue ?", [
        ("ÉTIENNE", "Est-ce que vous prenez d'autres médicaments ?", True),
        ("NADIA", "Oui, un comprimé pour la pression, tous les matins.", True),
        ("ÉTIENNE", "Bon. Je vais vous donner un sirop. Il n'a rien contre votre comprimé.", True),
        ("ÉTIENNE", "Si la toux persiste plus de sept jours, ou si la fièvre revient, allez voir un médecin.", True),
    ], notes="La question sur les autres médicaments n'est pas de la curiosité : c'est "
             "la raison pour laquelle le pharmacien tient un dossier. Le dire clairement, "
             "certains élèves hésitent à répondre.")

    d.tableau('Analyse', "Les quatre questions, toujours les mêmes",
              ["Ce qu'il demande", "Ce que vous répondez"],
              [["Qu'est-ce que je peux faire pour vous ?", "je tousse, j'ai mal à la gorge"],
               ["Depuis quand est-ce que ça dure ?", "depuis quatre jours"],
               ["Avez-vous de la fièvre ?", "un peu, hier soir"],
               ["Prenez-vous d'autres médicaments ?", "oui, un comprimé pour la pression"]],
              cle=0,
              note="Quatre questions, quatre réponses courtes. Rien d'autre n'est demandé.",
              notes="Diapositive à photographier. C'est le plan de la production orale "
                    "de la séance E1 : le laisser affiché jusqu'à la fin du module.")

    d.regle("Le mot du pharmacien",
            "« si la toux persiste »",
            precision="Persister veut dire : continuer, ne pas partir. Quand le "
                      "pharmacien dit « si ça persiste », il vous demande de "
                      "revenir ou d'aller voir un médecin. C'est un mot que le "
                      "programme nomme pour cette situation.",
            notes="Diapositive à photographier. Faire répéter le mot et sa traduction "
                  "simple : « ça continue ».")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Nadia tousse depuis quatre jours.", "vrai"),
        ("Le pharmacien demande depuis quand ça dure.", "vrai"),
        ("Nadia a de la fièvre aujourd'hui.", "faux — un peu, hier soir seulement"),
        ("Elle a mal à la gorge le matin.", "vrai"),
        ("Elle ne prend aucun autre médicament.", "faux — un comprimé pour la pression"),
        ("Si la toux persiste plus de sept jours, il faut voir un médecin.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte.")

    d.billet(
        "Écrivez les quatre réponses que vous donneriez, aujourd'hui, au pharmacien.",
        exemples=[
            "Qu'est-ce que vous avez ? Depuis quand ?",
            "De la fièvre ? D'autres médicaments ?",
        ],
        notes="Devoir court. Même si l'élève va bien, lui faire inventer un malaise "
              "plausible : c'est le brouillon de sa production orale.")

    return d.save(dossier)
