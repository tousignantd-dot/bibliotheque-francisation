# -*- coding: utf-8 -*-
"""B2 · Répondre court, et dire où l'on est.
Bloc B « Défi 1 » · couleur acier · 75 min. Compréhension orale et repérage.
Source : exercices `t1ordre` et `t1adresse`, et leurs mini-leçons.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-urgence/images/')


def build(dossier):
    d = Deck(
        code='B2', section='acier',
        titre="Répondre court, et dire où l'on est",
        chapeau="Sept questions, sept réponses de moins de dix mots. Et "
                "une adresse qui ne s'arrête pas au nom de la rue : "
                "l'étage, la porte, la lumière allumée.",
        duree='75 minutes')

    d.titre(notes="Deuxième séance du défi 1. Relire deux billets de B1 — les adresses "
                  "écrites — et faire remarquer ce qui manque presque toujours : l'étage "
                  "et la façon d'entrer.")

    d.objectifs([
        "répondre à chaque question du répartiteur en une phrase courte ;",
        "dire « je ne sais pas » plutôt que d'inventer ;",
        "situer un endroit avec les bons mots : hauteur, façade, repère ;",
        "préparer l'arrivée des secours pendant l'appel.",
    ])

    d.declencheur(
        'Problème', "L'ambulance est devant l'immeuble depuis deux minutes. "
                    "Pourquoi personne n'est encore monté ?",
        image=IMG + 'ambulance.jpg',
        pistes=[
            "Douze logements, une seule adresse : où frapper ?",
            "La porte de l'immeuble est-elle barrée ?",
            "Le corridor est-il éclairé ?",
            "Qui attend en bas ?",
        ],
        notes="Cette diapositive vaut toute la séance. Faire calculer : douze portes, "
              "trente secondes chacune, cela fait six minutes perdues.")

    d.cartes("Les mots qui situent", "Trois éléments suffisent presque toujours", [
        ("La hauteur", "au premier étage · au sous-sol · en bas de l'escalier"),
        ("La façade", "devant l'entrée · derrière l'immeuble · dans la cour arrière"),
        ("Le repère", "à côté de la pharmacie · entre la 3e et la 4e Avenue"),
        ("Dehors", "la porte 3 du stationnement · devant le dépanneur · à l'arrêt "
                   "d'autobus"),
    ], notes="Faire construire oralement l'adresse de l'école avec les trois éléments. "
             "Puis celle du domicile de deux ou trois volontaires.")

    d.tableau('Question, réponse', "Sept échanges, aucun de plus de dix mots",
              ['Le répartiteur demande', 'On répond'],
              [["L'endroit de votre urgence ?", "5412, rue des Ormeaux, app. 2."],
               ["Le numéro d'où vous appelez ?", "Le 514 555-0198."],
               ["Dites-moi ce qui se passe.", "Ma mère est tombée dans l'escalier."],
               ["Est-ce qu'elle est consciente ?", "Oui, elle me répond."],
               ["Est-ce qu'elle respire ?", "Oui, elle respire."],
               ["S'est-elle frappé la tête ?", "Je ne sais pas."],
               ["Quel âge a-t-elle ?", "Soixante et onze ans."]],
              cle=1,
              notes="Faire lire à deux voix, debout, dos à dos : c'est la seule façon de "
                    "sentir qu'on ne se voit pas. Puis inverser les rôles.")

    d.regle("« Je ne sais pas » est une bonne réponse",
            "Une invention peut envoyer la mauvaise équipe ; une ignorance avouée, jamais.",
            precision="Le répartiteur pose ensuite une question plus simple, ou il note "
                      "l'incertitude pour les ambulanciers. Ce qu'il ne peut pas faire, "
                      "c'est corriger une information fausse qu'il croit vraie.",
            notes="Diapositive à photographier. Elle enlève une pression réelle : "
                  "beaucoup d'élèves croient qu'il faut tout savoir pour avoir le droit "
                  "d'appeler.")

    d.cartes("Quatre gestes qui font gagner une minute", "Pendant que vous attendez", [
        ("Déverrouiller", "La porte de l'immeuble, et celle du logement."),
        ("Éclairer", "La lumière de l'entrée et celle du corridor."),
        ("Dégager", "Enfermer le chien, écarter ce qui bloque le passage."),
        ("Accueillir", "Envoyer quelqu'un attendre en bas, s'il y a quelqu'un d'autre."),
    ], notes="Ajouter : dire au répartiteur ce qu'on fait pendant qu'on le fait. Il le "
             "note, et les ambulanciers l'entendent avant d'arriver.")

    d.piege("Donner un repère que vous seul connaissez",
            "C'est en face de chez Ana, la maison avec les fleurs.",
            "C'est au coin de Bélanger, à côté de la pharmacie.",
            "Donnez ce qui est écrit et visible depuis la rue : un numéro, une enseigne, "
            "un nom de rue. Une ambulance ne cherche pas une maison, elle cherche un "
            "point sur une carte.",
            notes="Faire trouver au groupe trois repères visibles autour de l'école. "
                  "L'exercice dure trois minutes et il est toujours utile.")

    d.pratique('Emploi', "Le mot qui situe",
               "Complétez à l'oral, puis vérifiez.", [
        ("Nous sommes ___ l'appartement 2, ___ premier étage.", "dans · au"),
        ("Elle est ___ bas de l'escalier intérieur.", "en"),
        ("Je vous attends ___ l'entrée principale.", "devant"),
        ("L'immeuble est ___ la pharmacie.", "à côté de"),
        ("Le stationnement est ___ l'immeuble, par la ruelle.", "derrière"),
        ("C'est ___ la rue Bélanger et la rue Jean-Talon.", "entre"),
        ("Il est tombé ___ le trottoir, devant le dépanneur.", "sur"),
        ("Ma mère est ___ la salle de bain et la porte est bloquée.", "dans"),
    ], corrige=True,
       notes="Faire relire la phrase entière une fois corrigée. Le mot seul ne se retient "
             "pas ; la phrase, oui.")

    d.billet(
        "Décrivez en trois phrases comment on arrive jusqu'à vous, chez vous.",
        exemples=[
            "L'adresse · l'étage et la porte · un repère visible de la rue.",
            "Ajoutez ce que vous feriez pendant l'attente.",
        ],
        notes="Ramasser : ces trois phrases serviront de fiche personnelle. Suggérer de "
              "les copier dans le téléphone, à côté des contacts d'urgence.")

    return d.save(dossier)
