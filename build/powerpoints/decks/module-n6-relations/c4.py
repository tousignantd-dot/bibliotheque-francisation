# -*- coding: utf-8 -*-
"""C4 · Qui, que, où : tout dire en une seule phrase
Bloc C « Défi 2 » · couleur teal · écoute et réponds · 75 min.
Source : exercices `t2ou` (cols:1) et `t2fiche` et leurs mini-leçons — la
subordonnée relative, le « où » de lieu et de temps, et la structure
Dét + nom + relative que le programme du niveau 6 demande.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='teal',
        titre="Qui, que, où : tout dire en une seule phrase",
        chapeau="Attends près du banc qui fait face au guichet. Une seule "
                "phrase, et rien ne se perd — c'est à ça que sert la "
                "subordonnée relative.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du Défi 2. Écrire au tableau trois phrases courtes "
                  "— il y a un banc, le banc fait face au guichet, attends là — et "
                  "demander au groupe de n'en faire qu'une. La solution est le sujet "
                  "de la séance.")

    d.objectifs([
        "choisir entre qui et que selon ce qui suit ;",
        "employer où pour un lieu et pour un moment ;",
        "attacher une description à un nom : Dét, nom, relative ;",
        "remplir une fiche de description à partir d'une conversation.",
    ], notes="Le deuxième objectif est celui que le programme nomme explicitement : "
             "le où complément de lieu ou de temps.")

    d.declencheur(
        'Observation', "Comment dis-tu où quelqu'un doit t'attendre ?",
        pistes=[
            "Devant quoi, près de quoi, à côté de quoi ?",
            "Et si l'endroit n'a pas de nom ?",
            "Comment fais-tu quand il y a deux portes ?",
            "Quelle phrase donnes-tu au téléphone ?",
        ],
        notes="Les réponses contiennent presque toujours une relative sans que "
              "personne ne l'ait cherchée. Les relever au tableau et y revenir après "
              "la règle.")

    d.tableau('Analyse', "Trois pronoms, trois emplois",
              ['Le pronom', 'Quand on l\'emploie'],
              [["qui", "un verbe suit : la femme qui porte un foulard vert"],
               ["que", "un autre sujet suit : le manteau qu'il porte"],
               ["où, lieu", "la ville où il travaille, le terminus où l'autobus arrive"],
               ["où, moment", "le jour où il est tombé, l'automne où elle est arrivée"],
               ["Dét, nom, relative", "une femme de taille moyenne qui tire une valise rouge"]],
              cle=0,
              note="Qui ne s'élide jamais, même devant il.",
              notes="Diapositive à photographier. La quatrième rangée est celle qu'on "
                    "oublie : après un nom de temps, c'est où, jamais que.")

    d.regle("Le jour où, et non le jour que",
            "Où sert pour un lieu et pour un moment.",
            precision="Le jour où il est tombé. L'automne où ma sœur est arrivée. "
                      "L'année où nous sommes arrivés. On entend souvent « le jour que "
                      "je suis arrivé » dans le français parlé d'ici ; à l'écrit, et "
                      "au niveau 6, c'est où.",
            notes="Diapositive à photographier. Ne pas dévaloriser la forme entendue : "
                  "dire simplement qu'elle appartient à l'oral familier et que l'écrit "
                  "demande l'autre.")

    d.pratique('Grammaire', "Qui, que ou où ?",
               "Complétez chaque phrase.", [
        ("Mettez-vous près du banc ... fait face au guichet.", "qui"),
        ("C'est par là ... les autobus du Nord arrivent.", "que"),
        ("Rouyn-Noranda, c'est la ville ... Ousmane travaille.", "où"),
        ("L'automne ... Kadiatou est arrivée a été difficile.", "où"),
        ("La femme ... tu cherches porte un foulard vert.", "que"),
        ("Le jour ... il est tombé, sa sœur venait de s'installer.", "où"),
    ], corrige=True,
       notes="Faire dire le test à voix haute avant de répondre : qu'est-ce qui suit ? "
             "Un verbe, un sujet, ou un nom de lieu ou de temps ?")

    d.cartes('Assembler', "Une description en un seul groupe", [
        ("On commence par le nom",
         "une femme de taille moyenne. C'est le noyau : tout va s'y accrocher."),
        ("On ajoute une relative",
         "qui porte des lunettes rondes. La description se précise sans nouvelle phrase."),
        ("On en ajoute une seconde",
         "et qui tire une grosse valise rouge. Deux relatives : c'est la limite utile."),
        ("Trois, c'est trop",
         "Une femme qui porte des lunettes qui a une valise qui est rouge : à l'oral, celui qui écoute a perdu le début."),
    ], notes="Faire construire une description complète par groupe de deux, à l'oral, "
             "avec exactement deux relatives. C'est l'entraînement direct de E1.")

    d.pratique('Écoute', "La fiche de Kadiatou",
               "Réécoutez la conversation, puis complétez la fiche.", [
        ("Âge", "32 ans"),
        ("Taille", "de taille moyenne"),
        ("Visage", "un visage allongé"),
        ("Cheveux", "ondulés, attachés en chignon bas"),
        ("Lunettes", "rondes, monture fine et dorée"),
        ("Signe particulier", "une petite cicatrice au-dessus du sourcil gauche"),
        ("Vêtements", "un foulard vert et une longue veste grise"),
        ("Bagage", "une grosse valise rouge à roulettes"),
    ], corrige=True, cols=2,
       notes="Fiche à recopier dans le cahier : elle sert de modèle à la production "
             "orale de E1, où chacun décrira quelqu'un de son choix.")

    d.billet(
        "Écris une phrase avec où, sur un lieu ou sur un moment.",
        exemples=[
            "Exemple : l'année où je suis arrivé au Québec.",
            "Une seule phrase.",
        ],
        notes="Deux minutes. Fin du Défi 2 : annoncer le Défi 3, où l'on passe du "
              "téléphone au journal de quartier.")

    return d.save(dossier)
