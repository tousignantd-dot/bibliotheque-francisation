# -*- coding: utf-8 -*-
"""A3 · Les parties d'un courriel, et ce que chacune apprend
Bloc A « Je découvre » · couleur ambre · écriture · 75 min.
Source : exercice `prCourriel` et sa mini-leçon — le savoir de grammaire du
texte « tenir compte de la présentation matérielle et de la mise en page ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='ambre',
        titre="Les parties d'un courriel",
        chapeau="Avant d'avoir lu une seule phrase, la page t'a déjà dit "
                "de quoi il s'agit, à qui l'on parle et combien de "
                "nouvelles arrivent.",
        duree='75 minutes')

    d.titre(notes="Projeter au démarrage un courriel long, écran masqué de loin, et "
                  "demander au groupe ce qu'il voit sans lire. On voit des blocs, des "
                  "blancs, une ligne isolée en haut : c'est exactement la matière de "
                  "la séance.")

    d.objectifs([
        "nommer les six parties d'un courriel et dire ce que chacune apprend ;",
        "compter les idées d'un texte en comptant ses paragraphes ;",
        "choisir une formule d'appel qui va avec le reste du texte ;",
        "écrire un objet de trois à six mots qui se lit seul.",
    ], notes="Le quatrième objectif se retrouve tel quel dans la production écrite "
             "de E2 : l'objet y est une des exigences.")

    d.declencheur(
        'Observation', "Qu'est-ce que tu regardes en premier dans un courriel ?",
        pistes=[
            "L'objet, le nom de la personne, la longueur du texte ?",
            "Qu'est-ce qui te fait ouvrir un message tout de suite ?",
            "Qu'est-ce qui te fait remettre à plus tard ?",
            "As-tu déjà reçu un courriel sans objet ?",
        ],
        notes="Beaucoup répondent la longueur. C'est une bonne entrée : un texte long "
              "fait peur tant qu'on ne sait pas qu'il se découpe.")

    d.tableau('Analyse', "Six parties, six renseignements",
              ['La partie', 'Ce qu\'elle apprend'],
              [["L'objet", "de quoi il sera question, et souvent sur quel ton"],
               ["La formule d'appel", "à qui l'on écrit, et si l'on tutoie"],
               ["Un blanc", "qu'une idée est finie et qu'une autre commence"],
               ["La première phrase", "l'idée principale de tout le paragraphe"],
               ["La salutation", "que le texte est fini, et quel lien unit les deux"],
               ["La signature", "qui écrit, quand la boîte ne le dit pas clairement"]],
              cle=0,
              notes="Diapositive à photographier. Six rangées, pas de note : c'est la "
                    "densité maximale lisible de loin.")

    d.cartes('Comparer', "Trois objets pour le même courriel", [
        ("Des nouvelles, enfin",
         "Trois mots. On sait le sujet et le ton avant d'ouvrir : ce sera long et ce sera bon."),
        ("Important, à lire aujourd'hui",
         "Le sujet manque et l'urgence est annoncée. On ouvre avec inquiétude, souvent pour rien."),
        ("Bonjour",
         "Ne dit rien du tout. Dans une liste de cent courriels, six mois plus tard, il est introuvable."),
        ("Un programme de jumelage à Saint-Hyacinthe",
         "Long, mais chaque mot sert. Un objet peut aller jusqu'à six ou sept mots s'il informe."),
    ], notes="Faire choisir le meilleur objet par le groupe, puis demander pourquoi. "
             "La règle sort d'elle-même : un objet doit pouvoir se lire seul.")

    d.regle("Un blanc annonce un changement d'idée",
            "Compter les blancs, c'est compter les nouvelles.",
            precision="Ce n'est pas de la décoration. Quatre paragraphes veulent dire "
                      "quatre idées principales, et la première phrase de chacun les "
                      "porte. Lire les quatre premières phrases donne le plan complet "
                      "du courriel en vingt secondes.",
            notes="Diapositive à photographier. Faire faire l'expérience : lire à voix "
                  "haute seulement les quatre premières phrases du courriel d'Ousmane, "
                  "et demander de quoi il parle.")

    d.pratique('Association', "Qu'est-ce que cette partie t'apprend ?",
               "Associez chaque partie du courriel à ce qu'elle vous apprend.", [
        ("L'objet", "de quoi il sera question, et sur quel ton"),
        ("La formule d'appel", "à qui l'on écrit, et si l'on tutoie"),
        ("Un blanc entre deux paragraphes", "qu'une idée est finie et qu'une autre commence"),
        ("La première phrase d'un paragraphe", "l'idée principale de tout le paragraphe"),
        ("La formule de salutation", "que le texte est fini, et quel lien unit les deux"),
        ("La signature", "qui écrit, quand la boîte ne le dit pas clairement"),
    ], corrige=True,
       notes="Même exercice que dans le module, à l'oral d'abord. Les élèves le "
             "referont ensuite à l'écran, en glissant les réponses.")

    d.piege('Ton', "Cher Ousmane, puis vous tout le long",
            "Cher Ousmane, puis tu jusqu'à la fin",
            "La formule d'appel décide du ton de tout le texte. Une formule amicale "
            "suivie d'un vouvoiement sonne faux et laisse le lecteur incertain du "
            "lien. On choisit une fois, et on s'y tient jusqu'à la signature.",
            notes="Erreur très fréquente chez les scripteurs de niveau 6, qui "
                  "commencent chaleureusement puis se raidissent en cours de texte.")

    d.billet(
        "Écris l'objet du courriel que tu enverras à la fin du module.",
        exemples=[
            "Trois à six mots.",
            "Il doit se lire seul, sans le texte.",
        ],
        notes="Deux minutes. Garder les billets : ils reviennent en E2, où chacun "
              "compare l'objet écrit aujourd'hui avec celui qu'il finit par choisir.")

    return d.save(dossier)
