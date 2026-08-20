# -*- coding: utf-8 -*-
"""E1 · À toi : s'informer et décrire.
Bloc E « Je me lance » · couleur teal · 90 min.
Source : dialogue `appli`, jeu de rôle et productions orale et écrite.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="À toi : s'informer et décrire",
        chapeau="Trois productions, dans l'ordre : une conversation au rayon "
                "avec l'assistant, un appareil décrit à voix haute, un message "
                "au service à la clientèle.",
        duree='90 minutes')

    d.titre(notes="Séance de production. Prévoir les postes et les écouteurs. Rendre "
                  "d'abord les billets corrigés de A3, B2 et D2 : ce sont les brouillons.")

    d.objectifs([
        "m'informer sur un appareil, à l'oral, avec un interlocuteur ;",
        "décrire un appareil avec des adjectifs justes ;",
        "écrire au service à la clientèle pour un problème précis ;",
        "me relire et me corriger avant d'envoyer.",
    ])

    d.dialogue('Le modèle', "Le réfrigérateur du sous-sol", [
        ("YIN", "Un mètre cinquante de haut, soixante centimètres de large, pas plus.", True),
        ("MARTIN", "Celui-ci fait cent quarante-cinq sur cinquante-cinq. Il entre.", True),
        ("YIN", "Il consomme beaucoup ?", True),
        ("MARTIN", "C'est un des plus économes de sa catégorie. Trois cents kilowattheures par année.", False),
    ], consigne="Repérez tout ce que vous avez appris dans ces quatre répliques.",
       notes="Faire chercher : des dimensions données dans l'ordre, un pronom démonstratif, "
             "un superlatif, une unité de consommation. Tout le module y est.")

    d.cartes('Production 1 · Le jeu de rôle', "Comment ça marche", [
        ("Tu choisis l'appareil",
         "Une laveuse, un réfrigérateur ou une cuisinière. Trois situations ordinaires."),
        ("Tu choisis ton rôle",
         "L'acheteur, ou le vendeur. Renseigner quelqu'un est plus difficile que "
         "s'informer."),
        ("L'assistant commence par ton espace",
         "Comme le vendeur du module. Il ne parlera ni de la livraison, ni de "
         "l'installation, ni de la garantie prolongée avant que tu ne demandes."),
        ("Ton but",
         "Savoir si l'appareil entre, ce qu'il consomme, ce que couvre la garantie, et "
         "combien ça fait en tout."),
    ], notes="Vingt-cinq minutes. Rappeler les six questions du bloc B au tableau : "
             "beaucoup d'élèves en oublient deux.")

    d.cartes('Production 2 · Un appareil décrit', "Trois temps, quarante-cinq secondes", [
        ("Temps 1 · Ce que c'est, et ses dimensions",
         "« C'est une laveuse frontale. Elle fait soixante-huit centimètres de large. »"),
        ("Temps 2 · Ce qui la distingue, avec des adjectifs",
         "« Elle est silencieuse et économe en eau. C'est un modèle récent. »"),
        ("Temps 3 · Ce que tu conseilles",
         "« Prends celle-là si ton local est petit. Elle sera livrée en une semaine. »"),
    ], notes="Les billets de A3 et B2 contiennent déjà les mesures et les adjectifs. Le "
             "rappeler : le travail est à moitié fait.")

    d.cartes('Production 3 · Le message', "Au service à la clientèle", [
        ("Ce qu'il doit contenir",
         "L'appareil et la date d'achat ; ce qui ne va pas, précisément ; ce que tu as "
         "déjà vérifié ; ce que tu demandes."),
        ("Ce qu'on vérifie",
         "Au moins deux adjectifs accordés, et une phrase au futur : ce que tu attends du "
         "magasin. Cinq à huit phrases."),
        ("Pourquoi « ce que j'ai vérifié »",
         "C'est ce qui fait avancer le dossier. Sans cela, la première réponse du service "
         "sera de vous demander de vérifier."),
    ], notes="Le billet de D2 — décrire un problème en trois éléments — est le brouillon "
             "direct de cette production.")

    d.regle("Avant d'envoyer",
            "Relis-toi une fois, à voix basse.",
            precision="Trois choses à vérifier, toujours les mêmes : la place et l'accord "
                      "de l'adjectif, la base du futur simple, et le mélange ce/celui. Ce "
                      "sont les trois fautes du module.",
            notes="Diapo à photographier. C'est la liste de vérification de tout le module.")

    d.piege("Écrire au service sans rien avoir vérifié",
            "Ma laveuse vibre, envoyez un technicien.",
            "Ma laveuse vibre à l'essorage. J'ai vérifié les boulons et le niveau.",
            "La première réponse du service à un message vague est toujours de demander "
            "des vérifications. Les faire d'avance et le dire fait gagner plusieurs jours "
            "— et évite parfois le déplacement.",
            notes="Faire comparer les deux versions à voix haute. La différence de "
                  "traitement est évidente.")

    d.cartes("Ce que l'enseignant reçoit", "Et ce qu'il ne reçoit pas", [
        ("L'appareil décrit",
         "Ton enregistrement et sa transcription, si tu choisis de les envoyer. Rien ne "
         "part tant que tu n'as pas cliqué."),
        ("Le message écrit",
         "Le texte que tu déposes, tel que tu l'as écrit. Tu peux le reprendre autant de "
         "fois que tu veux."),
        ("Ce qui n'est jamais conservé",
         "Les corrections de l'assistant et la conversation du jeu de rôle. Elles servent "
         "à t'entraîner, pas à t'évaluer."),
    ], notes="Le dire clairement, comme dans les autres modules.")

    d.billet(
        "Après avoir envoyé : notez une chose que vous corrigeriez si vous recommenciez.",
        exemples=[
            "Une seule chose, la plus importante pour vous.",
            "Exemple : « j'ai oublié de demander si l'installation était comprise ».",
        ],
        notes="Rendre annoté à la séance E2, où les élèves font leur autoévaluation.")

    return d.save(dossier)
