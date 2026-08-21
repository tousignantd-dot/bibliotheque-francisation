# -*- coding: utf-8 -*-
"""C1 · Où est le rayon ?
Bloc C « Défi 2 · Trouver le rayon et demander » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t2vf`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-electro/images/')


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre='Où est le rayon ?',
        chapeau="Le magasin est grand comme un aréna et le vendeur ne dit "
                "rien qu'on ne lui demande pas. Trois questions courtes "
                "suffisent — encore faut-il les poser.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 2. On passe de la lecture à la parole : la "
                  "circulaire est dans la main, il s'agit maintenant de s'en servir "
                  "devant quelqu'un.")

    d.objectifs([
        "demander où se trouve un rayon ;",
        "montrer un appareil et demander son prix ;",
        "demander le format d'un appareil, en pouces ;",
        "dire qu'on prend l'appareil.",
    ])

    d.declencheur(
        'Observation', "À qui demande-t-on, et comment ?",
        image=IMG + 'rangee-laveuses.jpg',
        pistes=[
            "Combien de temps passeriez-vous à chercher seul ?",
            "Qui travaille dans un magasin comme celui-là ?",
            "Qu'est-ce qu'on dit avant de poser une question ?",
            "Qu'est-ce qu'on fait si on n'a pas compris la réponse ?",
        ],
        notes="Faire dire la gêne à voix haute : beaucoup d'élèves évitent de demander "
              "et tournent vingt minutes. Nommer la difficulté est la première étape.")

    d.dialogue('Dialogue · 1 de 3', "Au fond, à gauche", [
        ("MARISOL", "Bonjour, monsieur. Excusez-moi. Où est le rayon des laveuses ?", True),
        ("MARIO", "Au fond, à gauche, après les téléviseurs. Suivez l'affichette « Électroménagers ».", True),
        ("MARISOL", "Merci… Bonjour. Je cherche cette laveuse-là. Elle est dans la circulaire.", True),
        ("MARIO", "Faites voir. Ah oui, la Norlac LT 4200. Elle est juste ici, la blanche.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Deux phrases de Marisol, et elle est rendue devant l'appareil. Faire "
             "compter les mots : elle en dit onze en tout.")

    d.dialogue('Dialogue · 2 de 3', "Elle coûte combien ?", [
        ("MARISOL", "Elle coûte combien aujourd'hui ?", True),
        ("MARIO", "Huit cent quarante-neuf dollars. Le spécial finit dimanche.", True),
        ("MARISOL", "Est-ce que vous l'avez en gris ?", True),
        ("MARIO", "En gris, c'est un autre modèle. Il est cinquante dollars plus cher.", True),
    ], notes="Le vendeur ne donne le prix que parce qu'on le lui demande. C'est la règle "
             "du jeu de rôle de E1 : le préparer dès maintenant.")

    d.dialogue('Dialogue · 3 de 3', "Vingt-sept pouces", [
        ("MARISOL", "Non, la blanche, c'est correct. Est-ce qu'elle est grande ?", True),
        ("MARIO", "Vingt-sept pouces de large. Vous avez de la place dans votre logement ?", True),
        ("MARISOL", "J'ai mesuré. J'ai vingt-huit pouces entre le mur et la porte.", True),
        ("MARIO", "Ça entre. Vous la prenez ?", True),
        ("MARISOL", "Oui, je la prends.", True),
    ], notes="Marisol a mesuré avant de partir — c'était le devoir de A3. Faire le lien "
             "à voix haute : le module se tient d'une séance à l'autre.")

    d.tableau('Analyse', "Trois questions, trois réponses",
              ['On demande', 'On obtient'],
              [["Où est le rayon des laveuses ?", "un endroit dans le magasin"],
               ["Elle coûte combien ?", "le prix de cette semaine"],
               ["Est-ce que vous l'avez en gris ?", "oui, non, ou un autre modèle"],
               ["Elle fait combien de large ?", "une mesure en pouces"]],
              cle=0,
              note="Une question à la fois, et on attend la réponse avant la suivante.",
              notes="Diapo à photographier. C'est la carte de route du défi 2, reprise "
                    "en C3.")

    d.regle("Saluer avant de demander",
            "« Bonjour. Excusez-moi, où est… ? »",
            precision="Entrer dans un commerce et poser sa question sans "
                      "saluer surprend ici. Deux mots suffisent, et ils "
                      "changent complètement l'accueil.",
            notes="Diapo à photographier. Faire pratiquer l'entrée en matière : bonjour, "
                  "excusez-moi, la question. Trois temps.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Le rayon des laveuses est au fond, à gauche.", "vrai"),
        ("Marisol montre la circulaire au vendeur.", "vrai"),
        ("La laveuse grise coûte le même prix que la blanche.", "faux — 50 $ de plus"),
        ("La laveuse fait vingt-sept pouces de large.", "vrai"),
        ("Marisol n'a pas mesuré la place chez elle.", "faux — elle a 28 pouces"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte.")

    d.billet(
        "Écrivez les trois questions que vous poseriez au vendeur.",
        exemples=[
            "Une pour trouver le rayon.",
            "Une pour le prix, une pour le format.",
        ],
        notes="Devoir court. Il prépare C3, qui travaille ces questions une à une.")

    return d.save(dossier)
