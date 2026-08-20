# -*- coding: utf-8 -*-
"""B1 · La commande.
Bloc B « Défi 1 · Lire le menu et commander » · couleur acier · 75 min.
Source : dialogue `t1`, exercices `t1vf` et `t1question`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre='La commande',
        chapeau="Le serveur arrive. Trois choses à faire : choisir sa "
                "formule, poser la question qui manque, et signaler une "
                "allergie avant qu'il ne soit trop tard.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc B. Rappeler les quatre formules de A3 : elles sont le "
                  "socle de toute la séance.")

    d.objectifs([
        "demander ce que comprend une formule ;",
        "demander ce qu'il y a dans un plat ;",
        "signaler une allergie au bon moment ;",
        "commander une boisson.",
    ])

    d.declencheur(
        'Mise en situation', "Le serveur arrive et vous n'avez pas fini de lire. Que dites-vous ?",
        pistes=[
            "Quelle phrase employez-vous pour gagner du temps ?",
            "Quelle est la première question à poser sur une formule ?",
            "À quel moment faut-il signaler une allergie ?",
            "Que demandez-vous comme boisson ?",
        ],
        notes="Cinq minutes. La troisième piste est la plus importante : une allergie se "
              "signale au moment de commander, jamais quand le plat arrive.")

    d.dialogue('Dialogue · 1 de 3', "Ce que comprend la formule", [
        ("VINCENT", "Bonsoir. Vous avez fait votre choix ?", False),
        ("ANDRÉS", "Presque. Qu'est-ce qu'il y a dans la table d'hôte ce soir ?", True),
        ("VINCENT", "Soupe ou salade en entrée, ensuite le poisson du jour ou le poulet, et dessert au choix.", True),
        ("ANDRÉS", "Le poisson du jour, c'est quoi aujourd'hui ?", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Deux questions en trois répliques : ce que comprend la formule, puis ce "
             "qu'est le plat du jour. Les faire répéter.")

    d.dialogue('Dialogue · 2 de 3', "Commander", [
        ("VINCENT", "De la truite, servie avec des légumes et du riz.", False),
        ("ANDRÉS", "Je prendrais la table d'hôte, avec la soupe et la truite.", True),
        ("VINCENT", "Très bien. Et pour vous, madame ?", False),
        ("MANON", "Je vais prendre le poulet, mais à la carte. Sans entrée.", True),
    ], notes="« Je prendrais » et « je vais prendre » : deux formes également correctes. "
             "Faire remarquer la précision de Manon — « à la carte, sans entrée » — qui "
             "évite tout malentendu.")

    d.dialogue('Dialogue · 3 de 3', "La boisson et l'allergie", [
        ("ANDRÉS", "De l'eau, s'il vous plaît. Est-ce que l'eau du robinet est gratuite ?", True),
        ("VINCENT", "Oui, bien sûr. Une carafe pour deux ?", False),
        ("ANDRÉS", "Oui, merci. Ah — est-ce qu'il y a des arachides dans le dessert ?", True),
        ("VINCENT", "Je vérifie en cuisine et je vous le dis avant de le servir.", True),
    ], notes="La question d'allergie arrive au bon moment : à la commande. Le serveur "
             "vérifie en cuisine — c'est la réponse normale et attendue.")

    d.tableau('Analyse', "Quatre questions, quatre moments",
              ['La question', 'Quand la poser'],
              [["Qu'est-ce qu'il y a dans la table d'hôte ?", "avant de choisir"],
               ["Le plat du jour, c'est quoi ?", "avant de choisir"],
               ["Est-ce qu'il y a des arachides dedans ?", "au moment de commander"],
               ["L'eau du robinet est gratuite ?", "au moment de commander"]],
              cle=2,
              note="Une allergie se signale à la commande — jamais quand le plat arrive.",
              notes="Diapo à photographier. La note peut éviter un accident sérieux.")

    d.regle("Signaler une allergie",
            "Au moment de commander, et pour chaque service.",
            precision="Une allergie se dit avant que la cuisine ne prépare le plat. "
                      "Attendre que l'assiette arrive est trop tard, et le restaurant ne "
                      "peut plus rien faire. Andrés pose la question pour le dessert dès "
                      "la commande : c'est exactement le bon moment.",
            notes="Point de sécurité autant que de langue. Le traiter sérieusement, et "
                  "faire écrire la phrase par chacun.")

    d.piege("Attendre le plat pour signaler",
            "[le dessert arrive] Ah, est-ce qu'il y a des arachides dedans ?",
            "[à la commande] Est-ce qu'il y a des arachides dans le dessert ?",
            "À la commande, la cuisine peut choisir un autre dessert ou adapter le plat. "
            "Quand l'assiette est devant vous, il est trop tard : soit vous ne mangez pas, "
            "soit vous prenez un risque.",
            notes="Faire écrire à chacun la phrase correspondant à sa propre situation — "
                  "allergie, régime, restriction religieuse.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("La table d'hôte comprend trois services.", "vrai"),
        ("Le poisson du jour est du saumon.", "faux — de la truite"),
        ("Manon prend aussi la table d'hôte.", "faux — le poulet à la carte"),
        ("L'eau du robinet est payante.", "faux — gratuite"),
        ("Andrés pose une question sur les arachides.", "vrai"),
        ("Le serveur répond sans vérifier.", "faux — il vérifie en cuisine"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte.")

    d.billet(
        "Écrivez votre commande complète pour un repas au restaurant.",
        exemples=[
            "La formule, l'entrée, le plat, la boisson.",
            "Ajoutez une question sur un plat, et une sur une allergie ou un régime.",
        ],
        notes="Ramasser. Ces commandes servent directement au jeu de rôle de E1.")

    return d.save(dossier)
