# -*- coding: utf-8 -*-
"""C1 · Venez prendre un café samedi.
Bloc C « Défi 2 · Venez prendre un café » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t2vf`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-voisins/images/')


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Venez prendre un café samedi",
        chapeau="Une invitation qui ne dit ni le jour, ni l'heure, ni "
                "l'endroit n'est pas une invitation : c'est une intention. "
                "Rachid, lui, donne les trois.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 2. Le lien avec le défi 1 est direct : Rachid a "
                  "obtenu sa permission, Manon l'a aidé avec ses boîtes, et il veut "
                  "rendre la politesse. C'est ce qui rend l'invitation naturelle.")

    d.objectifs([
        "comprendre une invitation dite de vive voix ;",
        "relever le jour, l'heure et l'endroit ;",
        "reconnaître une réponse qui accepte ;",
        "entendre un compliment et ce qu'il porte.",
    ])

    d.declencheur(
        'Observation', "Qui a déjà invité un voisin chez lui ?",
        image=IMG + 'palier-portes.jpg',
        pistes=[
            "Est-ce qu'on invite ses voisins, chez vous ?",
            "Qu'est-ce qui empêche d'inviter quelqu'un du même immeuble ?",
            "Qu'est-ce qu'on dit quand on invite ?",
            "Et si la personne dit non ?",
        ],
        notes="La deuxième question ramène presque toujours la même réponse : la peur de "
              "déranger, et la peur de mal parler. Le module répond aux deux, et il vaut "
              "la peine de le dire tout de suite.")

    d.dialogue('Dialogue · 1 de 3', "Je voudrais vous remercier", [
        ("RACHID", "Madame Lachapelle, vous avez deux minutes ?", True),
        ("MANON", "Oui, oui. Qu'est-ce qui se passe ?", False),
        ("RACHID", "Vous m'avez aidé avec mes boîtes. Je voudrais vous remercier.", True),
        ("MANON", "Ce n'était rien, voyons.", False),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Même ordre qu'au défi 1 : la raison d'abord, la demande ensuite. Rachid "
             "n'invite pas encore — il explique pourquoi il va inviter. Faire remarquer "
             "la réponse de Manon : « ce n'était rien » ne refuse pas, c'est de la "
             "modestie.")

    d.dialogue('Dialogue · 2 de 3', "C'est quand ?", [
        ("RACHID", "On fait un petit café chez nous. Est-ce que vous voulez venir ?", True),
        ("MANON", "Avec plaisir. C'est quand ?", True),
        ("RACHID", "Samedi, à deux heures. Chez nous, au 3A.", True),
        ("MANON", "Samedi, deux heures. Je vais l'écrire sur mon calendrier.", True),
    ], notes="Le cœur de la séance tient dans deux répliques : Manon demande « c'est "
             "quand ? », et Rachid répond par les trois renseignements d'un coup. Faire "
             "compter les renseignements sur les doigts : jour, heure, endroit.")

    d.dialogue('Dialogue · 3 de 3', "Elle est belle, votre porte", [
        ("MANON", "Est-ce que j'apporte quelque chose ?", True),
        ("RACHID", "Apportez seulement votre bonne humeur.", True),
        ("MANON", "Ah non, je vais apporter mes biscuits. J'insiste.", False),
        ("MANON", "Dites donc, elle est belle, votre porte repeinte !", True),
    ], notes="Trois choses à relever : la question qu'on pose toujours quand on est "
             "invité, la réponse polie de celui qui reçoit, et le compliment — qui porte "
             "sur ce que la personne a fait, pas sur ce qu'elle est. Le compliment se "
             "travaille en C4.")

    d.tableau('Analyse', "Ce que l'invitation dit",
              ["Le renseignement", "Dans le dialogue"],
              [["Le jour", "samedi"],
               ["L'heure", "à deux heures"],
               ["L'endroit", "chez nous, au 3A"],
               ["L'occasion", "pour vous remercier"]],
              cle=1,
              note="Les trois premiers ne se négocient pas. Le quatrième "
                   "rassure : on sait pourquoi on est invité.",
              notes="Diapo à photographier. C'est la grille de la production écrite de "
                    "E1 — le carton devra contenir exactement ces quatre lignes.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Rachid invite Manon pour la remercier de son aide.", "vrai"),
        ("Le café a lieu vendredi soir.", "faux — samedi, à deux heures"),
        ("Manon écrit le rendez-vous sur son calendrier.", "vrai"),
        ("Rachid demande à Manon d'apporter un dessert.", "faux — « apportez seulement votre bonne humeur »"),
        ("Manon décide quand même d'apporter ses biscuits.", "vrai — elle insiste"),
        ("Manon fait un compliment sur la porte repeinte.", "vrai"),
    ], corrige=True,
       notes="C'est l'exercice `t2vf` du module interactif, mot pour mot. Faire justifier "
             "chaque « faux » par la réplique exacte.")

    d.billet(
        "Écrivez l'invitation que vous feriez, en une seule phrase.",
        exemples=[
            "Le jour, l'heure et l'endroit doivent y être.",
            "« Venez prendre un thé dimanche, à trois heures, chez moi au 402. »",
        ],
        notes="Devoir court. Ramasser et compter les trois renseignements : c'est le "
              "diagnostic le plus rapide du défi. Ceux qui en oublient un le referont "
              "en C2, sur leur propre phrase.")

    return d.save(dossier)
