# -*- coding: utf-8 -*-
"""A3 · Le mot précis fait le travail à ta place
Bloc A « Je découvre » · couleur teal · 75 min.
Source : exercice `prChamp` et sa mini-leçon sur les champs lexicaux.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre="Le mot précis fait le travail à ta place",
        chapeau="« Un film » suffit pour se faire comprendre. « Un court "
                "métrage » évite d'avoir à expliquer pourquoi ça ne durait "
                "que douze minutes.",
        duree='75 minutes')

    d.titre(notes="Troisième séance du bloc A. C'est la séance de vocabulaire du "
                  "module, mais elle n'est pas une liste : elle enseigne un "
                  "mécanisme, celui du champ lexical.")

    d.objectifs([
        "ranger les mots du cinéma selon ce qui les distingue ;",
        "choisir le mot précis quand on le connaît ;",
        "ajouter un détail quand on ne le connaît pas ;",
        "remplacer un jugement vague par un jugement précis.",
    ], notes="Le troisième objectif est celui qui déculpabilise : ne pas connaître le "
             "mot précis n'est pas une faute, c'est une situation qui a une solution.")

    d.declencheur(
        'Observation', "Comment dirais-tu ces quatre choses en un seul mot ?",
        pistes=[
            "Un film de douze minutes.",
            "Un film qui montre des faits réels, avec une voix hors champ.",
            "Une histoire découpée en épisodes, à la télévision.",
            "La reprise de tous les films d'une même personne, des années après.",
        ],
        notes="Laisser chercher deux minutes sans donner les réponses. Les mots "
              "arriveront au tableau d'analyse ; l'effort de les chercher est ce qui "
              "les fixe.")

    d.tableau('Analyse', "Le champ lexical du cinéma",
              ['Le mot', 'Ce qu\'il dit de plus que « film »'],
              [["un long métrage", "plus d'une heure, en salle"],
               ["un court métrage", "moins de vingt minutes"],
               ["un documentaire", "des faits réels, pas une fiction"],
               ["une série", "une histoire en épisodes"],
               ["une scène", "un seul lieu, d'un seul tenant"],
               ["une rétrospective", "tous les films d'une personne"]],
              cle=0,
              notes="Diapositive à photographier. Faire remarquer que ce n'est pas la "
                    "difficulté du mot qui compte, mais le détail qu'il porte.")

    d.regle("Un champ lexical, ce n'est pas une liste",
            "C'est un groupe de mots proches, que distingue un seul détail.",
            precision="Le programme donne lui-même deux exemples : le cinéma "
                      "(documentaire, film, reportage, court métrage) et le logis "
                      "(condo, maison, château, villa). On ne dit pas « maison » pour "
                      "tout, parce que « maison » ne dit ni la taille, ni l'étage, ni "
                      "le propriétaire.",
            notes="Diapositive à photographier. Demander au groupe un champ lexical de "
                  "leur métier : ils en ont tous un, et ils le maîtrisent souvent "
                  "mieux en français qu'ils ne le croient.")

    d.regle("Le même mécanisme dans le jugement",
            "Un adjectif précis appelle une réponse ; un adjectif vague ferme la discussion.",
            precision="« C'était plate » ne se discute pas. « La première demi-heure "
                      "est lente » se discute : on peut demander pourquoi, on peut "
                      "répondre que c'est voulu. C'est ce qui sépare le niveau 6 du "
                      "niveau 5, et c'est ce que le Défi 3 va travailler.",
            notes="Diapositive à photographier. Annoncer le Défi 3 dès maintenant : "
                  "l'avis nuancé se prépare de loin.")

    d.pratique('Vocabulaire', "Le mot précis",
               "Remplacez le mot vague par le mot exact.", [
        ("J'ai vu un film de douze minutes.", "un court métrage"),
        ("C'est un film avec des vraies affaires.", "un documentaire"),
        ("Le bout où elle ouvre l'armoire.", "la scène de l'armoire"),
        ("Ils repassent tous ses films.", "une rétrospective"),
        ("C'était bon.", "le personnage est convaincant"),
        ("C'était long.", "la première demi-heure est lente"),
    ], corrige=True, cols=2,
       notes="Les deux derniers items changent de nature : ils passent du vocabulaire "
             "au jugement. Le faire remarquer, c'est la charnière de la séance.")

    d.vocabulaire('Vocabulaire', "Quatre mots pour dire ce qu'on en pense", [
        ("une critique", "Un texte signé qui raconte un peu l'œuvre et qui dit surtout ce que son auteur en pense."),
        ("un reproche", "Ce qu'on dit à quelqu'un pour lui signaler ce qu'on trouve mal fait."),
        ("convaincant", "Se dit de ce qui donne envie de croire, parce que c'est bien amené."),
        ("un parti pris", "Un choix assumé d'avance, qu'on garde même s'il déplaît."),
    ], notes="Ces quatre mots servent au Défi 3. Les poser ici donne trois semaines "
             "pour qu'ils décantent.")

    d.billet(
        "Écris une phrase avec un mot précis du cinéma.",
        exemples=[
            "Par exemple : « J'ai vu un court métrage la semaine passée. »",
            "Une phrase, pas plus.",
        ],
        notes="Deux minutes. Les billets où le mot est mal employé se reprennent "
              "en A4 : un mot précis mal employé fait plus de dégâts qu'un mot vague "
              "bien employé.")

    return d.save(dossier)
