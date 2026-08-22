# -*- coding: utf-8 -*-
"""A1 · Chaque question a sa personne
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `prVF`, cinq premières cartes de FC_CARDS.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Chaque question a sa personne",
        chapeau="Bintou termine sa francisation en février et ne sait pas ce "
                "qui vient après. Au comptoir, elle apprend une chose que "
                "personne ne dit à voix haute : ici, tout finit en papier.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir par une question au groupe : "
                  "qu'est-ce que vous ferez quand la francisation sera finie ? "
                  "Beaucoup répondront « je ne sais pas », et c'est exactement le "
                  "point de départ. Ne pas répondre à leur place aujourd'hui.")

    d.objectifs([
        "nommer les personnes d'un établissement et dire ce que chacune peut "
        "faire ;",
        "distinguer ce qui se règle au comptoir de ce qui demande un "
        "rendez-vous ;",
        "comprendre pourquoi une chose dite ne compte pas tant qu'elle n'est "
        "pas écrite ;",
        "employer les cinq premiers mots du dossier avec leur article.",
    ], notes="Le troisième objectif est celui de tout le module. Il surprend les "
             "élèves venus de systèmes où la parole d'un fonctionnaire engage.")

    d.declencheur(
        'Observation', "À qui poses-tu tes questions, dans ton centre ?",
        pistes=[
            "Sais-tu qui travaille au comptoir de l'accueil ?",
            "As-tu déjà rencontré un conseiller ou une conseillère d'orientation ?",
            "Qu'est-ce qu'on t'a déjà répondu que tu n'as pas compris ?",
            "Est-ce qu'on t'a déjà donné quelque chose par écrit ?",
        ],
        notes="Question sans mauvaise réponse. Noter au tableau les personnes que le "
              "groupe nomme : la liste sera presque toujours incomplète, et c'est ce "
              "manque qui rend le tableau d'analyse utile tout à l'heure.")

    d.dialogue('Dialogue · 1 de 3', "Ce n'est pas à moi qu'il faut demander ça", [
        ("BINTOU", "Bonjour. Je m'excuse, je ne sais pas si c'est ici qu'il faut demander ça.", True),
        ("RÉAL", "Bonjour. Demandez toujours, on verra bien. Vous êtes en francisation ?", True),
        ("BINTOU", "Oui, au local 214, le soir. Je finis mon dernier cours en février et je voudrais savoir ce que je fais après.", True),
        ("RÉAL", "Ah. Ça, c'est une belle question, et ce n'est pas à moi qu'il faut la poser.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Faire remarquer la phrase d'ouverture de Bintou : elle s'excuse avant "
             "de parler. C'est très fréquent et ça n'aide personne. On y reviendra "
             "en D2, quand il faudra prendre la parole dans une rencontre.")

    d.dialogue('Dialogue · 2 de 3', "Choisir un programme, c'est autre chose", [
        ("RÉAL", "Des inscriptions, oui. Des dossiers, des relevés de notes, des changements d'horaire : tout ce qui est papier passe par le comptoir. Mais choisir un programme, c'est autre chose.", True),
        ("BINTOU", "L'orientation, c'est une personne ?", True),
        ("RÉAL", "C'est une personne, oui. Son métier, c'est de s'asseoir avec quelqu'un et de regarder avec lui ce qui est possible.", True),
        ("BINTOU", "Et il décide si je peux entrer dans un programme ?", True),
    ], notes="Arrêter sur la dernière question et la faire deviner au groupe avant "
             "d'écouter la suite. La plupart répondront « oui ». La réponse est non, "
             "et c'est la découverte la plus utile de la séance.")

    d.dialogue('Dialogue · 3 de 3', "Toujours par écrit", [
        ("RÉAL", "Non. Personne ne décide en parlant. La décision arrive après, par écrit, du centre de formation professionnelle.", True),
        ("BINTOU", "Par écrit.", True),
        ("RÉAL", "Toujours par écrit. Ici, une chose qui compte finit toujours en papier : un avis, une lettre, une ligne dans votre dossier. Ce qui se dit au comptoir ne compte pas.", True),
        ("BINTOU", "Et mon enseignant, monsieur Béliveau, il sert à quoi là-dedans ?", True),
    ], notes="Écrire au tableau : « Ce qui se dit au comptoir ne compte pas. » et la "
             "laisser toute la session. Annoncer la production écrite de E2 : dans "
             "quatre semaines, chacun écrira son propre courriel au secrétariat.")

    d.tableau('Analyse', "Quatre personnes, quatre pouvoirs",
              ['La personne', 'Ce qu\'elle peut faire pour toi'],
              [["Au comptoir", "recevoir les papiers, ouvrir un dossier, donner un relevé de notes"],
               ["À l'orientation", "expliquer, calculer tes préalables, nommer ce qui bloque"],
               ["Ton enseignant", "dire où tu en es en français ; son avis pèse, il ne tranche pas"],
               ["La direction", "décider, et sa décision arrive toujours par écrit"]],
              cle=0,
              note="Aucune de ces personnes ne peut faire le travail d'une autre. Poser sa question au mauvais endroit fait perdre une semaine.",
              notes="Diapositive à photographier. C'est le tableau de référence du "
                    "module ; il revient à chaque ouverture de bloc.")

    d.regle("Ce qui compte finit en papier",
            "Une chose dite au comptoir n'engage personne ; une ligne au dossier engage l'établissement.",
            precision="Ce n'est pas de la mauvaise volonté. La personne qui vous a "
                      "parlé changera de poste, partira, oubliera. Le dossier, lui, "
                      "reste. Un adulte qui sait demander un écrit avance deux fois "
                      "plus vite qu'un adulte qui parle bien.",
            notes="Diapositive à photographier. Donner tout de suite la phrase à "
                  "réutiliser : « Est-ce que je peux avoir ça par écrit ? » Elle est "
                  "polie, normale, et elle ne froisse personne.")

    d.vocabulaire('Vocabulaire', "Les cinq premiers mots, avec leur article", [
        ("une conseillère d'orientation", "La personne dont le métier est de regarder avec toi quels programmes te sont ouverts."),
        ("un dossier scolaire", "L'ensemble des papiers qu'un établissement garde sur toi et qui te suit."),
        ("un relevé de notes", "Le papier officiel qui montre les cours réussis et le résultat de chacun."),
        ("l'enseignement individualisé", "Une façon d'apprendre où chacun avance à son rythme dans son cahier."),
        ("une matière", "Un domaine d'étude à part, avec ses propres cours et ses unités."),
    ], notes="Faire répéter chaque mot avec son article. « L'enseignement "
             "individualisé » est long : le découper en trois temps et le faire dire "
             "deux fois. C'est le mot du module que les élèves emploieront le plus.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la conversation de Bintou et de Réal.", [
        ("Bintou termine sa francisation en février.", "vrai"),
        ("Tout ce qui est papier passe par le comptoir de l'accueil.", "vrai"),
        ("C'est le comptoir qui choisit le programme d'un élève.", "faux - c'est l'orientation qui explique"),
        ("Le conseiller d'orientation décide lui-même de l'admission.", "faux - la décision arrive par écrit"),
        ("Réal conseille d'amener son enseignant à la rencontre.", "vrai"),
        ("Il faut n'apporter que les papiers qu'on juge utiles.", "faux - on apporte tout, le conseiller trie"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le dernier "
             "surprend : beaucoup d'élèves trient d'avance et jettent le document qui "
             "aurait tout expliqué.")

    d.billet(
        "Quelle question voudrais-tu poser, et à qui la poserais-tu ?",
        exemples=[
            "Une phrase suffit, et elle peut commencer par « je me demande ».",
            "Nomme la personne : le comptoir, l'orientation, ton enseignant.",
        ],
        notes="Deux minutes. Ramasser les billets : ils donnent la matière du jeu de "
              "rôle de E1, et ils disent quelles questions le groupe n'ose pas poser.")

    return d.save(dossier)
