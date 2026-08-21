# -*- coding: utf-8 -*-
"""B1 · Je vous appelle pour l'annonce.
Bloc B « Défi 1 · L'appel » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t1vf`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Je vous appelle pour l'annonce",
        chapeau="Au téléphone, on ne voit rien : ni le logement, ni le visage "
                "de la personne. Tout passe par ce qu'on demande et par ce "
                "qu'on note.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 1. Demander qui, dans le groupe, évite de téléphoner "
                  "en français et préfère écrire. La gêne du téléphone est presque "
                  "universelle : la nommer d'entrée détend la salle.")

    d.objectifs([
        "ouvrir et fermer un appel au sujet d'une annonce ;",
        "comprendre les renseignements donnés au téléphone ;",
        "faire répéter un mot sans gêne ;",
        "vérifier une adresse et une heure avant de raccrocher.",
    ])

    d.declencheur(
        'Discussion', "Pourquoi le téléphone est-il plus difficile que face à face ?",
        pistes=[
            "Qu'est-ce qu'on perd, au téléphone ?",
            "Les gestes, les lèvres, le visage.",
            "Qu'est-ce qu'on peut faire pour compenser ?",
            "Que faites-vous, vous, quand vous ne comprenez pas ?",
        ],
        notes="Faire sortir les stratégies déjà employées par le groupe : faire répéter, "
              "épeler, demander de parler plus lentement, rappeler plus tard. Les valider "
              "toutes — elles seront reprises dans la séance.")

    d.dialogue('Dialogue · 1 de 4', "Ouvrir l'appel", [
        ("HÉLÈNE", "Oui, allô ?", True),
        ("NADÈGE", "Bonjour, madame. Je vous appelle pour le quatre et demie de la "
                   "rue Bowen. Est-ce qu'il est encore libre ?", True),
        ("HÉLÈNE", "Il est encore libre, oui. Le premier juillet.", True),
        ("NADÈGE", "Parfait. J'aimerais vous poser quelques questions, si vous avez "
                   "deux minutes. Je prends des notes.", False),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Deux choses à faire remarquer : Nadège dit tout de suite pourquoi elle "
             "appelle, et elle annonce qu'elle prend des notes. Cette annonce fait ralentir "
             "l'interlocutrice — c'est une stratégie, pas une politesse.")

    d.dialogue('Dialogue · 2 de 4', "Ce qui est inclus", [
        ("NADÈGE", "Le loyer est de mille cinquante dollars. Est-ce que le chauffage "
                   "est inclus ?", True),
        ("HÉLÈNE", "Le chauffage n'est pas inclus. C'est électrique, et c'est à la "
                   "charge du locataire. Comptez à peu près cent dollars par mois "
                   "l'hiver.", True),
        ("NADÈGE", "Cent dollars l'hiver, d'accord. Et les électroménagers ?", True),
        ("HÉLÈNE", "Le poêle et le réfrigérateur sont fournis. La laveuse et la "
                   "sécheuse, non, mais il y a une buanderie au sous-sol.", True),
    ], notes="Nadège répète le chiffre — « cent dollars l'hiver » — avant de passer à la "
             "question suivante. C'est la technique de vérification de la séance B4.")

    d.dialogue('Dialogue · 3 de 4', "Faire répéter", [
        ("NADÈGE", "Excusez-moi, vous pouvez répéter le dernier mot ?", True),
        ("HÉLÈNE", "Une buanderie. Deux laveuses et deux sécheuses, au sous-sol de "
                   "l'immeuble, deux dollars la brassée.", True),
        ("NADÈGE", "Merci. Et pour le stationnement ?", True),
        ("HÉLÈNE", "Il y a une case derrière l'immeuble, incluse dans le loyer. Une "
                   "seule, par exemple.", True),
    ], notes="« Vous pouvez répéter le dernier mot ? » est plus efficace que « pardon ? » : "
             "elle dit exactement ce qui manque, et l'interlocutrice reprend juste ça, en "
             "l'expliquant. Faire répéter la formule en chœur.")

    d.dialogue('Dialogue · 4 de 4', "Fermer l'appel", [
        ("NADÈGE", "Une seule, ça me suffit. Dernière question : est-ce que je peux "
                   "visiter cette semaine ?", True),
        ("HÉLÈNE", "Jeudi soir, dix-huit heures ? L'adresse, c'est le quatre cent "
                   "douze, rue Bowen, appartement trois.", True),
        ("NADÈGE", "Jeudi dix-huit heures, quatre cent douze Bowen, appartement "
                   "trois. C'est noté. Merci beaucoup, madame.", True),
    ], notes="La dernière réplique est un modèle : elle répète l'heure, l'adresse et le "
             "numéro d'appartement. Une erreur d'un chiffre, et la visite est perdue.")

    d.regle("Annoncez que vous prenez des notes",
            "« J'aimerais vous poser quelques questions. Je prends des notes. »",
            precision="Cette phrase fait trois choses à la fois : elle prévient que l'appel "
                      "durera quelques minutes, elle fait ralentir la personne, et elle "
                      "vous donne le droit de demander une pause pour écrire. Personne ne "
                      "la trouve étrange.",
            notes="Diapositive à photographier. C'est la phrase la plus utile du défi.")

    d.cartes("Quatre façons de faire répéter", "Aucune n'est impolie", [
        ("Vous pouvez répéter le dernier mot ?",
         "La plus précise : elle dit exactement ce qui manque."),
        ("Pouvez-vous parler un peu plus lentement, s'il vous plaît ?",
         "Pour une phrase entière, pas pour un mot."),
        ("Vous pouvez épeler, s'il vous plaît ?",
         "Pour un nom de rue, un nom de famille, un mot inconnu."),
        ("Donc, mille cinquante dollars. C'est bien ça ?",
         "La vérification : on répète ce qu'on a compris et on fait confirmer."),
    ], notes="Faire pratiquer les quatre à voix haute, deux par deux, dos à dos pour "
             "supprimer les lèvres et le visage. C'est l'exercice le plus proche du réel.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Le logement est libre le premier juillet.", "vrai"),
        ("Le chauffage est inclus dans le loyer.", "faux — il est à la charge du locataire"),
        ("Le poêle et le réfrigérateur sont fournis.", "vrai"),
        ("Il y a une laveuse et une sécheuse dans le logement.",
         "faux — une buanderie au sous-sol"),
        ("Nadège fait répéter un mot qu'elle n'a pas compris.", "vrai — « buanderie »"),
        ("Deux cases de stationnement sont incluses.", "faux — une seule"),
        ("Nadège répète l'adresse et l'heure avant de raccrocher.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte.")

    d.billet(
        "Écrivez les huit questions que vous poseriez au téléphone.",
        exemples=[
            "Une par ligne, avec de la place à droite pour la réponse.",
            "Apportez la feuille : elle servira à la séance B2 et à l'appel réel.",
        ],
        notes="Devoir de préparation. C'est littéralement la feuille d'appel de la séance "
              "B4 : les élèves la construisent eux-mêmes avant qu'on la leur donne.")

    return d.save(dossier)
