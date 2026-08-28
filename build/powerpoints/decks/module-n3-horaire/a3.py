# -*- coding: utf-8 -*-
"""A3 · Les lieux, les objets, les verbes.
Bloc A « Je découvre » · couleur teal · 60 min.
Source : exercices `prImg` et `prVerbes`, cartes mémoire.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-horaire/images/')


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre="Les lieux, les objets, les verbes",
        chapeau="Huit endroits, huit objets, six verbes. C'est tout le "
                "décor du module — et c'est le vocabulaire qu'un employé "
                "entend dès sa première journée, sans qu'on le lui "
                "explique.",
        duree='60 minutes')

    d.titre(notes="Séance de vocabulaire. Commencer par la lecture à voix haute des six "
                  "mots rapportés au billet de A2 : ça revoit la prononciation et ça "
                  "ouvre sur le métier de chacun.")

    d.objectifs([
        "nommer les lieux et les objets d'une cuisine de résidence ;",
        "associer chaque photo à sa description ;",
        "comprendre six verbes du travail ;",
        "employer « poinçonner », « aviser » et « remplacer ».",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qu'on voit dans une salle du personnel ?",
        image=IMG + 'casiers-vestiaire.jpg',
        pistes=[
            "Comment s'appelle cette pièce ?",
            "Qu'est-ce qu'on y laisse ?",
            "Est-ce qu'on s'y change, à votre travail ?",
            "Qu'est-ce qui est affiché sur les murs ?",
        ],
        notes="La quatrième question ramène souvent d'autres affiches : les consignes de "
              "sécurité, le numéro d'urgence, les congés fériés. Toutes se lisent, et "
              "presque personne ne les lit.")

    d.pratique('Vocabulaire', "Les lieux et les objets du travail",
               "À quelle photo va chaque description ?", [
        ("Le grand tableau blanc où les heures de chacun sont écrites.", "l'horaire"),
        ("La petite machine où on marque son heure d'arrivée.", "la poinçonneuse"),
        ("La rangée d'armoires étroites où les employés laissent leurs choses.", "les casiers du vestiaire"),
        ("Le chariot à roulettes chargé de plateaux vides.", "le chariot à plateaux"),
        ("La grande pièce froide où on garde la nourriture.", "la chambre froide"),
        ("L'appareil chaud qu'il faut éteindre avant midi.", "le four"),
        ("Les boîtes de carton laissées dans le corridor par le camion.", "la livraison"),
        ("Le petit papier qu'on laisse sur le bureau du chef d'équipe.", "la note"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `prImg` du module interactif, qui se fait avec les photos. "
             "Ici, faire deviner le mot à partir de la description seule : c'est plus "
             "difficile, et c'est ce que fait un employé qui entend un mot nouveau.")

    d.tableau('Analyse', "Six verbes de la journée de travail",
              ["Le verbe", "Ce qu'il veut dire au travail"],
              [["poinçonner", "marquer son heure d'arrivée et de départ"],
               ["remplacer", "faire le travail de quelqu'un qui n'est pas là"],
               ["aviser", "prévenir la personne responsable à l'avance"],
               ["éteindre", "arrêter un appareil pour qu'il cesse de fonctionner"]],
              cle=1,
              note="Deux autres au tableau suivant : « s'occuper de » et "
                   "« emprunter ».",
              notes="Diapo à photographier. « Aviser » est le verbe du défi 2 : il "
                    "reviendra dans la règle des trois jours. Le souligner au passage.")

    d.tableau('Analyse', "Deux verbes qu'on confond souvent",
              ["Le verbe", "Ce qu'il veut dire au travail"],
              [["s'occuper de", "prendre une tâche en charge, du début à la fin"],
               ["emprunter", "prendre une chose à quelqu'un et la lui rendre après"],
               ["prêter", "donner une chose pour un moment — c'est l'inverse d'emprunter"]],
              cle=1,
              note="J'emprunte à quelqu'un ; je prête à quelqu'un. Les deux "
                   "verbes décrivent le même geste, vu des deux côtés.",
              notes="Diapo à photographier. Faire jouer la paire : « Est-ce que tu peux "
                    "me prêter ton crayon ? — Oui, tiens. » L'un prête, l'autre "
                    "emprunte, dans la même seconde.")

    d.pratique('Vocabulaire', "Le mot et sa définition",
               "Reliez chaque mot du module à ce qu'il veut dire.", [
        ("un quart de travail", "le bloc d'heures qu'on fait dans une journée"),
        ("un chef d'équipe", "celui qui donne les tâches et répond aux questions"),
        ("une tâche", "un travail précis, qui a un début et une fin"),
        ("un uniforme", "les vêtements pareils que tous les employés portent"),
        ("une pause", "le moment court où on arrête pour manger ou se reposer"),
        ("un congé", "une journée où on ne travaille pas"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `prVocab` du module interactif, qui reprend les cartes "
             "mémoire. Insister sur « quart » : le mot n'a rien à voir avec le quart "
             "d'une heure, et beaucoup d'élèves le comprennent ainsi.")

    d.billet(
        "Nommez cinq objets de votre lieu de travail, avec leur article.",
        exemples=[
            "« un chariot », « la chambre froide », « le vestiaire ».",
            "Si vous ne travaillez pas : cinq objets de votre école.",
        ],
        notes="Devoir court. L'article est la vraie difficulté : le faire écrire "
              "obligatoirement. Un nom appris sans son article est un nom à réapprendre.")

    return d.save(dossier)
