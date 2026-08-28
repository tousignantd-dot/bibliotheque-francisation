# -*- coding: utf-8 -*-
"""B4 · Ce qu'on entend dans la réponse.
Bloc B « Défi 1 · Est-ce que je peux ? » · couleur acier (écoute) · 50 min.
Source : exercices `t1rep` et `t1qui`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='acier',
        titre="Ce qu'on entend dans la réponse",
        chapeau="Demander est la moitié du travail. L'autre moitié, c'est "
                "de comprendre ce qui revient — un oui franc, un oui avec "
                "une condition, un non poli, ou un « ce n'est pas à moi de "
                "décider ».",
        duree='50 minutes')

    d.titre(notes="Séance d'écoute, la dernière du défi 1. Elle ferme la boucle ouverte "
                  "en B1 : on a appris à demander, on apprend maintenant à entendre.")

    d.objectifs([
        "associer une demande à la réponse qu'elle appelle ;",
        "distinguer un refus poli d'un renvoi vers quelqu'un d'autre ;",
        "reconnaître à l'oreille qui parle : celui qui demande ou celle qui répond ;",
        "entendre la condition cachée dans un « oui, mais ».",
    ])

    d.tableau('Analyse', "Quatre réponses possibles à une demande",
              ["Ce que Manon dit", "Ce que ça veut dire"],
              [["Bien sûr, allez-y.", "oui, franchement"],
               ["Oui, mais accrochez-le au mur.", "oui, à une condition"],
               ["Le concierge a la clé.", "je ne décide pas : voyez la bonne personne"],
               ["Je préfère que non.", "non, poliment"]],
              cle=1,
              note="Aucune des quatre ne commence par « non ». C'est ce qui "
                   "rend l'écoute difficile, et ce qui s'apprend ici.",
              notes="Diapo à photographier. Faire remarquer que la troisième n'est ni un "
                    "oui ni un non : beaucoup d'élèves l'entendent comme un refus et "
                    "abandonnent, alors que la permission est simplement ailleurs.")

    d.pratique('Écoute', "À chaque demande, sa réponse",
               "Reliez ; plusieurs réponses semblent possibles, une seule va.", [
        ("Est-ce que je peux mettre mon vélo dans la remise ?",
         "Bien sûr, allez-y. Il y a de la place au fond."),
        ("Est-ce que je peux attacher mon vélo à la rampe ?",
         "Je préfère que non : il faut garder la sortie libre."),
        ("Est-ce qu'il faut demander à quelqu'un d'autre ?",
         "Le concierge a la clé. Voyez monsieur Nadeau."),
        ("Est-ce que je peux étendre mon linge dehors ?",
         "Pas de problème, la corde est à tout le monde."),
        ("Est-ce que je vous dérange ?",
         "Pas du tout. Entrez une minute."),
        ("Est-ce que je peux laisser la porte de la cour ouverte ?",
         "J'aimerais mieux pas. Le chat sortirait."),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `t1rep` du module interactif. Le faire à l'oral d'abord, "
             "livre fermé : la réponse se devine au ton avant de se lire.")

    d.cartes("Deux refus, deux façons de le dire", "Et pourquoi ça compte", [
        ("« Je préfère que non »",
         "Le refus le plus courant entre voisins. Il ne dit pas « non » : il dit ce que "
         "la personne préfère. On n'insiste pas."),
        ("« J'aimerais mieux pas »",
         "Le même refus, encore plus doux. Souvent suivi de la raison — « le chat "
         "sortirait ». La raison, c'est la politesse."),
        ("Ce qu'on répond dans les deux cas",
         "« Je comprends, merci quand même. » Et on cherche autre chose. Insister coûte "
         "la permission suivante."),
        ("Ce qu'on ne fait pas",
         "Demander pourquoi sur un ton fâché, ou redemander le lendemain en espérant une "
         "autre réponse. Dans un immeuble, on se recroise tous les jours."),
    ], notes="La quatrième carte vaut d'être discutée : dans plusieurs cultures, insister "
             "poliment est une marque de respect. Ici, non. Le dire sans jugement — ce "
             "n'est pas une question de bien ou de mal, mais d'usage local.")

    d.pratique('Écoute', "Qui parle : Rachid ou Manon ?",
               "Écoutez chaque phrase. Est-ce celui qui demande, ou celle qui répond ?", [
        ("Est-ce que je peux le mettre dans la remise ?", "Rachid demande"),
        ("Bien sûr, allez-y.", "Manon répond"),
        ("Est-ce que je vous dérange deux minutes ?", "Rachid demande"),
        ("Je préfère que non.", "Manon répond"),
        ("Il faudrait demander au concierge.", "Manon répond"),
        ("Est-ce que je pourrais l'accrocher au mur ?", "Rachid demande"),
    ], corrige=True,
       notes="C'est l'exercice `t1qui` du module interactif, qui se fait avec l'audio. Le "
             "faire ici sans le texte sous les yeux : c'est la forme de la phrase — "
             "question ou affirmation — qui donne la réponse, pas le vocabulaire.")

    d.piege("Entendre un refus là où il n'y en a pas",
            "« Le concierge a la clé. » — Bon, tant pis, je laisse faire.",
            "« Le concierge a la clé. » — D'accord, je vais le voir. Merci !",
            "Un renvoi vers quelqu'un d'autre n'est pas un refus : c'est une "
            "permission qui a une adresse. Beaucoup d'élèves abandonnent ici, "
            "à une porte de la réponse qu'ils cherchaient.",
            notes="C'est le piège le plus utile du module. Le faire jouer à deux : l'un "
                  "renvoie, l'autre remercie et demande où trouver la personne.")

    d.billet(
        "Notez les quatre réponses de Manon dans votre cahier.",
        exemples=[
            "Une ligne chacune, avec ce qu'elle veut dire.",
            "Vous les entendrez toutes les quatre en E1.",
        ],
        notes="Devoir de cinq minutes. C'est la grille d'écoute du jeu de rôle : l'élève "
              "qui l'a écrite reconnaît les réponses de l'assistant au lieu de les subir.")

    return d.save(dossier)
